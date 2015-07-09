from ROOT import TFile, TTree, gROOT, TH1F, TCanvas, gStyle, TF1, TProfile, TH2F
from sys import exit
import os
#import argparse

#Open Apr TDR analysis file
aprDataFileName = 'Run-1300-TDR-Analysis-drift-times.root'
aprDataFile = TFile(aprDataFileName, 'READ')
if (aprDataFile.IsOpen == False): 
  print "ERROR: ROOT file does not exist"
  exit(-1)
aprDataDir = aprDataFile.Get('Run-1300-TDR-Analysis')

#Open sim ROOT file
simFileName = 'Run-SIM-TDR-Analysis-drift-times.root'
simFile = TFile(simFileName, 'READ')
if (simFile.IsOpen == False): 
  print "ERROR: ROOT file does not exist"
  exit(-1)
aprSimDir = simFile.Get('Run-SIM-TDR-Analysis')

'''
Drift time plots
'''

#Create drift time canvas
driftTimeCanvas = TCanvas("driftTimeCanvas","", 1000, 600)
driftTimeCanvas.Divide(2,1)
driftTimeCanvas.cd(1)

#Format Apr data drift times plot
dataDriftTimesHist = aprDataDir.Get('Straw_Drift_Times_Channel_24')
#dataDriftTimesHist.SetTitle('Straw drift times (April data)')
dataDriftTimesHist.SetTitle('(a)')
dataDriftTimesHist.GetXaxis().SetTitle('Drift time [ns]')
dataDriftTimesHist.GetYaxis().SetTitle('Counts')
dataDriftTimesHist.GetYaxis().SetTitleOffset(1.6)
#resHist.GetXaxis().SetRangeUser(-60,60)
dataDriftTimesHist.SetStats(False)
dataDriftTimesHist.Draw()

#Change pad
driftTimeCanvas.cd(2)

#Format april sim drift times plot
simDriftTimesHist = aprSimDir.Get('Straw_Drift_Times_Channel_0')
#simDriftTimesHist.SetTitle('Straw drift times (Simulation)')
simDriftTimesHist.SetTitle('(b)')
simDriftTimesHist.GetXaxis().SetTitle('Drift time [ns]')
simDriftTimesHist.GetYaxis().SetTitle('Counts')
simDriftTimesHist.GetYaxis().SetTitleOffset(1.6)
#resHist.GetXaxis().SetRangeUser(-60,60)
simDriftTimesHist.SetStats(False)
simDriftTimesHist.Draw()

#Wait for user input
raw_input("Press Enter to continue...")


'''
Hit time differences plots
'''

#Create drift time diffs canvas
driftTimeDiffsCanvas = TCanvas("driftTimeDiffsCanvas","", 1000, 600)
driftTimeDiffsCanvas.Divide(2,1)
driftTimeDiffsCanvas.cd(1)

#Format Apr data drift times diffs plot
dataDriftDiffsTimesHist = aprDataDir.Get('Hit_Pair_Time_Diffs_Channels_24_25')
#dataDriftDiffsTimesHist.SetTitle('Straw doublet hit pair time diffence (April data)')
dataDriftDiffsTimesHist.SetTitle('(a)')
dataDriftDiffsTimesHist.GetXaxis().SetTitle('Hit time difference [ns]')
dataDriftDiffsTimesHist.GetYaxis().SetTitle('Counts')
dataDriftDiffsTimesHist.GetYaxis().SetTitleOffset(1.6)
#resHist.GetXaxis().SetRangeUser(-60,60)
dataDriftDiffsTimesHist.SetStats(False)
dataDriftDiffsTimesHist.Draw()

#Change pad
driftTimeDiffsCanvas.cd(2)

#Format april sim drift time diffs plot
simDriftDiffsTimesHist = aprSimDir.Get('Hit_Pair_Time_Diffs_Channels_0_1')
#simDriftDiffsTimesHist.SetTitle('Straw doublet hit pair time diffence (Simulation)')
simDriftDiffsTimesHist.SetTitle('(b)')
simDriftDiffsTimesHist.GetXaxis().SetTitle('Hit time difference [ns]')
simDriftDiffsTimesHist.GetYaxis().SetTitle('Counts')
simDriftDiffsTimesHist.GetYaxis().SetTitleOffset(1.6)
#resHist.GetXaxis().SetRangeUser(-60,60)
simDriftDiffsTimesHist.SetStats(False)
simDriftDiffsTimesHist.Draw()

#Wait for user input
raw_input("Press Enter to continue...")
