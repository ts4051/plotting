from ROOT import TFile, TTree, gROOT, TH1F, TCanvas, gStyle, TF1, TProfile, TH2F, TGraph, Double
from sys import exit
import os
import math
#import argparse

#TODO MAKE GENERIC FUNCTION TAKING FILE AND TREE NAME

#TODO Make this write events for TDRAnalysis rather than repeating analysis here

#Create canvas
#canvas = TCanvas("canvas","",600,600)
#canvas.cd()

#Open Jan TDR analysis file
inputFilePath = '/tmp/tstuttard/data/'
#inputFileName = 'sim_2Straws_april2014TestBeam_-0.001mA_beamMean0.15cm_beamRMSX0.3cm_1000evts.root'
#inputFileName = 'sim_2Straws_april2014TestBeam_-0.001mA_beamMean0.15cm_beamRMSX0.3cm_10000evts.root'
#inputFileName = 'sim_2Straws_april2014TestBeam_-0.01mA_beamMean0.15cm_beamRMSX0.3cm_10000evts.root'
#inputFileName = 'sim_2Straws_april2014TestBeam_-0.1mA_beamMean0.15cm_beamRMSX0.3cm_10000evts.root'
#inputFileName = 'sim_2Straws_april2014TestBeam_-0.01mA_beamMean0.15cm_beamRMScm_1000evts.root'
#inputFileName = 'sim_2Straws_april2014TestBeam_-0.01mA_beamMean0.15cm_beamRMScm_10000evts.root' #Use for drift times
inputFileName = 'sim_2Straws_april2014TestBeam_-0.001mA_beamMean0.15cm_beamRMScm_10000evts.root' #Use for anticorr/residuals
inputFile = TFile(inputFilePath+inputFileName, 'READ')
if (inputFile.IsOpen == False): 
  print "ERROR: ROOT file does not exist"
  exit(-1)

#Get tuple
straw0 = inputFile.Get('straw0')
straw1 = inputFile.Get('straw1')

#Get num entries in tuple
straw0NumEntries = straw0.GetEntriesFast()
straw1NumEntries = straw1.GetEntriesFast()
print 'Num entries = ',straw0NumEntries,',',straw1NumEntries
#TODO CHECK THE SAME

#Create output file for histos
outputFileName = 'garfieldPlots.root'
outputFile = TFile(outputFileName, 'RECREATE')

#Create TGraph with doublet drift times
g_doubletDriftTimesNs = TGraph()
g_doubletDriftTimesNs.SetName('g_doubletDriftTimesNs');
g_doubletDriftTimesNs.SetTitle('Doublet drift times'); 
g_doubletDriftTimesNs.GetXaxis().SetTitle("Drift time (front straw) [ns]");
g_doubletDriftTimesNs.GetYaxis().SetTitle("Drift time (back straw) [ns]");

#Don't plot finer than LSB of course time, as fine time bits not reliable in Jan data
timeBinSize = 5.

#Create histo with drift times
h_driftTimesFront = TH1F('h_driftTimesFront','Drift Times (front) [ns]', int(150/timeBinSize), -50, 100)
h_driftTimesBack = TH1F('h_driftTimesBack','Drift Times (back) [ns]', int(150/timeBinSize), -50, 100)

#Create histo with drift time diffs
h_driftTimeDiffs = TH1F('h_driftTimeDiffs','Drift Time Differences (front-back) [ns]', int(200/timeBinSize), -100, 100)

#Create histo with drift time sums
h_driftTimeSums = TH1F('h_driftTimeSums','Drift Time Sums [ns]', int(100/timeBinSize), 0, 100)

#Create histo of track positions
h_trackPositions = TH1F('h_trackPositions','Track positions [mm]', 600, -30., 30.)

#Create histo with drift distance sums
h_driftDistSums = TH1F('h_driftDistSums','Drift Distance Sums [mm]', 200, -10., 10.)

#Create histo with residuals
h_residuals = TH1F('h_residuals','Residuals to drift time anti-correlation line [ns]', int(200/timeBinSize), -100., 100.)
h_residuals.SetOption('EHIST')

#Create histos with reconstructed drift times (e.g. using constant sum in doublet)
driftTimeSumNs = 40.
h_driftTimesRecoFront = TH1F('h_driftTimesRecoFront','Reconstructed drift Times (front) [ns]', int(150/timeBinSize), -50, 100)
h_driftTimesRecoBack = TH1F('h_driftTimesRecoBack','Reconstructed drift Times (back) [ns]', int(150/timeBinSize), -50, 100)

#Compare reco drift times/distances to the original sim values
h_driftDistsRecoFront = TH1F('h_driftDistsRecoFront','Reconstructed drift distances (front) [um]', 60, -1.e3, 5.e3)
h_driftDistsRecoBack = TH1F('h_driftDistsRecoBack','Reconstructed drift distances (back) [um]', 60, -1.e3, 5.e3)

#Loop through entries
hitPairCounter = 0
for i_entry in range(0, straw0NumEntries) :

  #Get tuple entries for this event
  straw0.GetEntry(i_entry)
  straw1.GetEntry(i_entry)

  #Fill track positions histo
  h_trackPositions.Fill(straw0.trackPosXGlobalCm*10.)

  #Check event hit both straws
  if straw0.driftTimeUs>-0.9 and straw1.driftTimeUs>-0.9:

    #Fill drift time graph
    g_doubletDriftTimesNs.SetPoint(hitPairCounter, straw0.driftTimeUs*1000., straw1.driftTimeUs*1000.);
    hitPairCounter += 1 #Increment point index (don't use i_entry, as not adding every step)
    #print 'i,d1,d2 = ',i_entry,' , ',(straw0.driftTimeUs*1000.),' , ',(straw1.driftTimeUs*1000.)

    #Fill drift times histos
    h_driftTimesFront.Fill(straw0.driftTimeUs*1000.);
    h_driftTimesBack.Fill(straw1.driftTimeUs*1000.);

    #Fill drift time sum histo
    h_driftTimeSums.Fill(straw0.driftTimeUs*1000. + straw1.driftTimeUs*1000.);

    #Fill drift distance sum histo
    h_driftDistSums.Fill(straw0.driftDistCm*10. + straw1.driftDistCm*10.);

    #Fill drift time diffs histo
    h_driftTimeDiffs.Fill(straw0.driftTimeUs*1000. - straw1.driftTimeUs*1000.);
    
    #Reconstruct drift times and fill histos
    #In GARFIELD, only have drift times. Add a t0 to it and then use normal drift time 
    #technique assuming a constant sum
    t0Dummy = 5000. #arbitrary
    th1 = t0Dummy + straw0.driftTimeUs*1000 #th = t0 + td
    th2 = t0Dummy + straw1.driftTimeUs*1000 
    #Reconstruct t0 using assumption of constant drift time sum
    #th1 + th2 = 2t0 + td1 + td2 = 2t0 + const => t0 = (th1 + th2 - const) / 2
    t0 = (th1 + th2 - driftTimeSumNs) / 2.
    #Now get drift times from the hit times and t0: td = th - t0
    td1 = th1 - t0
    td2 = th2 - t0
    #Fill histos
    h_driftTimesRecoFront.Fill(td1);
    h_driftTimesRecoBack.Fill(td2);
       
    #Determine reco drift distance from reco times
    driftVelocity = 50. # um / ns
    h_driftDistsRecoFront.Fill(td1*driftVelocity)
    h_driftDistsRecoBack.Fill(td2*driftVelocity)

    #Compare reconstructed drift times and distances to sim drift times

        

h_trackPositions.Draw()
#raw_input("Press Enter to continue...")

#Draw drift times histos
h_driftTimesFront.Draw()
#raw_input("Press Enter to continue...")
h_driftTimesBack.Draw()
#raw_input("Press Enter to continue...")

#Draw drift time sum histo
h_driftTimeSums.Draw()
#raw_input("Press Enter to continue...")

#Draw drift distance sum histo
h_driftDistSums.Draw()
#raw_input("Press Enter to continue...")

#Draw drift time diffs histo
h_driftTimeDiffs.Draw()
#raw_input("Press Enter to continue...")

#Draw drift times graph
g_doubletDriftTimesNs.SetMarkerSize(1)
g_doubletDriftTimesNs.GetXaxis().SetRangeUser(-10.,60.)
g_doubletDriftTimesNs.GetYaxis().SetRangeUser(-10.,60.)
g_doubletDriftTimesNs.Draw("AP");

#Fit anticorrelation straight line
linfit = TF1("linfit", "[0] + [1]*x", -100, 100)
linfit.SetParameters(10, -1)
#g_doubletDriftTimesNs.Fit("linfit")
g_doubletDriftTimesNs.Fit(linfit)
intercept = linfit.GetParameter(0)
slope = linfit.GetParameter(1)	
#print 'linfit m,c = ',slope,',',intercept
linfit.Draw("same")
#Write to output file (not automatic for TGraph, unliek histos)
g_doubletDriftTimesNs.Write()

#Wait for user input
#raw_input("Press Enter to continue...")

#Calculate residuals for all points on graph and fill a histo
for i_pair in range(0, hitPairCounter) :

  #Get drift time points from graph
  dtF = Double(0)
  dtB = Double(0)
  g_doubletDriftTimesNs.GetPoint(i_pair, dtF, dtB)

  #Calculate residual
  residual = dtB - ( slope*dtF + intercept );
          
  #Fill histo
  h_residuals.Fill(residual);

#Draw residuals histo
h_residuals.Draw();

#Wait for user input
#raw_input("Press Enter to continue...")

#Write to output file
outputFile.Write()



