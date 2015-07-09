from ROOT import TFile, TTree, gROOT, TH1F, TCanvas, gStyle, TF1, TProfile, TH2F
from sys import exit
import os
#import argparse

#Open Jan TDR analysis file
janName = 'Run-497-TDR-Analysis'
janFileName = janName + '-BeamPeriod.root'
janFile = TFile(janFileName, 'READ')
if (janFile.IsOpen == False): 
  print "ERROR: ROOT file does not exist"
  exit(-1)
janDir = janFile.Get(janName)

#Open Jan sim TDR analysis file
simName = 'Run-SIM-TDR-Analysis'
janSimFileName = simName + '-JanBeamPeriod.root'
janSimFile = TFile(janSimFileName, 'READ')
if (janSimFile.IsOpen == False): 
  print "ERROR: ROOT file does not exist"
  exit(-1)
janSimDir = janSimFile.Get(simName)

#Open April TDR analysis file
aprName = 'Run-1300-TDR-Analysis'
aprFileName = aprName + '-BeamPeriod.root'
aprFile = TFile(aprFileName, 'READ')
if (aprFile.IsOpen == False): 
  print "ERROR: ROOT file does not exist"
  exit(-1)
aprDir = aprFile.Get(aprName)

#Open April sim TDR analysis file
aprSimFileName = simName + '-AprBeamPeriod.root'
aprSimFile = TFile(aprSimFileName, 'READ')
if (aprSimFile.IsOpen == False): 
  print "ERROR: ROOT file does not exist"
  exit(-1)
aprSimDir = aprSimFile.Get(simName)

#Hit times Jan
beamPeriodCanvas = TCanvas("beamPeriodCanvas","Hit times [ns] (data and sim)", 1000, 600)
beamPeriodCanvas.SetTitle('')
beamPeriodCanvas.Divide(2,1)
beamPeriodCanvas.cd(1)
janHitTimeHist = janDir.Get('Hit_Time_Structure_Channel_8')
janHitTimeHist.GetXaxis().SetRangeUser(115e3,170e3)
#janHitTimeHist.SetTitle('Hits times (January data)')
janHitTimeHist.SetTitle('(a)')
janHitTimeHist.GetXaxis().SetTitle('Hit time [ns]')
janHitTimeHist.GetYaxis().SetTitle('Counts')
janHitTimeHist.GetYaxis().SetTitleOffset(1.5)
janHitTimeHist.SetStats(False)
janHitTimeHist.Draw()
beamPeriodCanvas.cd(2)
janSimHitTimeHist = janSimDir.Get('Hit_Time_Structure_Channel_0')
janSimHitTimeHist.GetXaxis().SetRangeUser(115e3,170e3)
#janSimHitTimeHist.SetTitle('Hits times (Simulation)')
janSimHitTimeHist.SetTitle('(b)')
janSimHitTimeHist.GetXaxis().SetTitle('Hit time [ns]')
janSimHitTimeHist.GetYaxis().SetTitle('Counts')
janSimHitTimeHist.GetYaxis().SetTitleOffset(1.5)
janSimHitTimeHist.SetStats(False)
janSimHitTimeHist.Draw()

#Wait for user input
raw_input("Press Enter to continue...")

#Hit times gaps Jan
janGapsCanvas = TCanvas("janGapsCanvas","", 1000, 600)
janGapsCanvas.Divide(2,1)
janGapsCanvas.cd(1)
janTimeGapsHist = janDir.Get('Straw_Hit_Time_Gaps_Channel_8')
janTimeGapsHist.GetXaxis().SetRangeUser(6e3,40e3)
#janTimeGapsHist.SetTitle('Time gaps between consecutive straw hits (January data)')
janTimeGapsHist.SetTitle('(a)')
janTimeGapsHist.GetXaxis().SetTitle('Hit time [ns]')
janTimeGapsHist.GetYaxis().SetTitle('Counts')
janTimeGapsHist.GetYaxis().SetTitleOffset(1.5)
janTimeGapsHist.SetStats(False)
janTimeGapsHist.Draw()
janGapsCanvas.cd(2)
janSimTimeGapsHist = janSimDir.Get('Straw_Hit_Time_Gaps_Channel_0')
janSimTimeGapsHist.GetXaxis().SetRangeUser(6e3,40e3)
#
janSimTimeGapsHist.SetTitle('Time gaps between consecutive straw hits (Simulation)')
janSimTimeGapsHist.SetTitle('(b)')
janSimTimeGapsHist.GetXaxis().SetTitle('Hit time [ns]')
janSimTimeGapsHist.GetYaxis().SetTitle('Counts')
janSimTimeGapsHist.GetYaxis().SetTitleOffset(1.5)
janSimTimeGapsHist.SetStats(False)
janSimTimeGapsHist.Draw()

#Wait for user input
raw_input("Press Enter to continue...")

#Hit times gaps April
aprGapsCanvas = TCanvas("aprGapsCanvas","", 1000, 600)
aprGapsCanvas.Divide(2,1)
aprGapsCanvas.cd(1)
aprTimeGapsHist = aprDir.Get('Straw_Hit_Time_Gaps_Channel_8')
aprTimeGapsHist.GetXaxis().SetRangeUser(9e3,40e3)
#aprTimeGapsHist.SetTitle('Time gaps between consecutive straw hits (April data)')
aprTimeGapsHist.SetTitle('(a)')
aprTimeGapsHist.GetXaxis().SetTitle('Hit time [ns]')
aprTimeGapsHist.GetYaxis().SetTitle('Counts')
aprTimeGapsHist.GetYaxis().SetTitleOffset(1.5)
aprTimeGapsHist.SetStats(False)
aprTimeGapsHist.Draw()
aprGapsCanvas.cd(2)
aprSimTimeGapsHist = aprSimDir.Get('Straw_Hit_Time_Gaps_Channel_0')
aprSimTimeGapsHist.GetXaxis().SetRangeUser(9e3,40e3)
#aprSimTimeGapsHist.SetTitle('Time gaps between consecutive straw hits (Simulation)')
aprSimTimeGapsHist.SetTitle('(b)')
aprSimTimeGapsHist.GetXaxis().SetTitle('Hit time [ns]')
aprSimTimeGapsHist.GetYaxis().SetTitle('Counts')
aprSimTimeGapsHist.GetYaxis().SetTitleOffset(1.5)
aprSimTimeGapsHist.SetStats(False)
aprSimTimeGapsHist.Draw()

#Wait for user input
raw_input("Press Enter to continue...")
