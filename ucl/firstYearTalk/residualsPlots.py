from ROOT import TFile, TTree, gROOT, TH1F, TCanvas, gStyle, TF1, TProfile, TH2F
from sys import exit
import os
#import argparse

#Open Jan TDR analysis file
janDataFileName = 'Run-497-TDR-Analysis-Residuals.root'
janDataFile = TFile(janDataFileName, 'READ')
if (janDataFile.IsOpen == False): 
  print "ERROR: ROOT file does not exist"
  exit(-1)
janDataDir = janDataFile.Get('Run-497-TDR-Analysis')

#Open garfield ROOT file
garfieldFileName = 'garfieldPlots.root'
garfieldFile = TFile(garfieldFileName, 'READ')
if (garfieldFile.IsOpen == False): 
  print "ERROR: ROOT file does not exist"
  exit(-1)

doubletID = 25

'''
Anti-correlation plots
'''

#Get antiCorrCanvas with drift time plot from Jan data
driftTimesCanvas = janDataFile.Get('Drift_Times_Doublet_'+str(doubletID))
driftTimesGraph = driftTimesCanvas.GetPrimitive('Graph')
driftTimesFit = driftTimesCanvas.GetPrimitive('linfit')

#Create antiCorrCanvas
antiCorrCanvas = TCanvas("antiCorrCanvas","", 1000, 600)
antiCorrCanvas.Divide(2,1)
antiCorrCanvas.cd(1)

#Format Jan data drift times plot
#driftTimesGraph.SetTitle('Doublet hit pairs drift times (January data)')
driftTimesGraph.SetTitle('(a)')
driftTimesGraph.GetXaxis().SetTitle('Front straw drift time [ns]')
driftTimesGraph.GetYaxis().SetTitle('Back straw drift time [ns]')
driftTimesGraph.GetYaxis().SetTitleOffset(1.2)
driftTimesGraph.GetXaxis().SetRangeUser(-10.,60.)
driftTimesGraph.GetYaxis().SetRangeUser(-10.,60.)
driftTimesGraph.SetMarkerStyle(7)
driftTimesGraph.Draw('AP')
driftTimesFit.Draw('same')

#Change pad
antiCorrCanvas.cd(2)

#Get drift time plot from garfield
garfieldDriftTimesGraph = garfieldFile.Get('g_doubletDriftTimesNs')
#driftTimesFit = driftTimesCanvas.GetPrimitive('linfit')

#Format garfield drift times plot
#garfieldDriftTimesGraph.SetTitle('Doublet hit pairs drift times (Simulation)')
garfieldDriftTimesGraph.SetTitle('(b)')
garfieldDriftTimesGraph.GetXaxis().SetTitle('Front straw drift time [ns]')
garfieldDriftTimesGraph.GetYaxis().SetTitle('Back straw drift time [ns]')
garfieldDriftTimesGraph.GetYaxis().SetTitleOffset(1.2)
garfieldDriftTimesGraph.SetMarkerStyle(7)
garfieldDriftTimesGraph.GetXaxis().SetRangeUser(-10.,60.)
garfieldDriftTimesGraph.GetYaxis().SetRangeUser(-10.,60.)
#garfieldDriftTimesGraph.GetYaxis().SetRangeUser(-10.,60.)
garfieldDriftTimesGraph.Draw('AP')
#driftTimesFit.Draw('same')

#Wait for user input
raw_input("Press Enter to continue...")


'''
residuals plots
'''

#Create antiCorrCanvas
residualsCanvas = TCanvas("residualsCanvas","", 1000, 600)
residualsCanvas.Divide(2,1)
residualsCanvas.cd(1)

#Format data residuals plot
resHist = janDataDir.Get('Self_Triggered_Drift_Time_Residuals_Doublet_'+str(doubletID))
#resHist.GetXaxis().SetRangeUser(115e3,170e3)
#resHist.SetTitle('Doublet hit pairs drift time residuals (January data)')
resHist.SetTitle('(a)')
resHist.GetXaxis().SetTitle('Doublet drift time residuals [ns]')
resHist.GetYaxis().SetTitle('Counts')
resHist.GetYaxis().SetTitleOffset(1.5)
resHist.GetXaxis().SetRangeUser(-60,60)
resHist.SetStats(False)
resHist.Draw()

#Change to sim canvas
residualsCanvas.cd(2)

#Format sim residuals plot
simResHist = garfieldFile.Get('h_residuals')
#simResHist.GetXaxis().SetRangeUser(115e3,170e3)
#simResHist.SetTitle('Doublet hit pairs drift time residuals (Simulation)')
simResHist.SetTitle('(b)')
simResHist.GetXaxis().SetTitle('Doublet drift time residuals [ns]')
simResHist.GetYaxis().SetTitle('Counts')
simResHist.GetYaxis().SetTitleOffset(1.5)
simResHist.GetXaxis().SetRangeUser(-60,60)
simResHist.SetStats(False)
simResHist.Draw()

#Wait for user input
raw_input("Press Enter to continue...")
