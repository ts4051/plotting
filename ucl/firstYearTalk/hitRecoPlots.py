from ROOT import TFile, TTree, gROOT, TH1F, TCanvas, gStyle, TF1, TProfile, TH2F
from sys import exit
import os
#import argparse

#Open Jan TDR analysis file
rootFileName = 'Run-497-TDR-Analysis-SIMPLE_GEOM.root' #simple geometry version
rootFile = TFile(rootFileName, 'READ')
if (rootFile.IsOpen == False): 
  print "ERROR: ROOT file does not exist"
  exit(-1)

#Get canvas with hit pos plot
hitPosCanvas = rootFile.Get('protonHitPositionsWires')
activeRegionsHist = hitPosCanvas.GetPrimitive('Straws_Active_Regions')
activeRegionsHist.SetTitle('2D hit positions')
activeRegionsHist.SetStats(False)
activeRegionsHist.GetXaxis().SetTitle('x [mm]')
activeRegionsHist.GetYaxis().SetTitle('y [mm]')

hitPosCanvas.Draw()
raw_input("Press Enter to continue...")
