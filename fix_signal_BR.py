#!/usr/bin/env python
import ROOT
import re
from array import array
import sys
import csv
from math import sqrt
from math import pi
import datetime
import argparse
# from sys import path
# path.append("../../../MacrosAndScripts/")
# from myPlotStyle import *
ROOT.gStyle.SetFrameLineWidth(1)
ROOT.gStyle.SetLineWidth(2)
ROOT.gStyle.SetOptStat(0)


def GetKeyNames( self, dir = "" ):
    self.cd(dir)
    return [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]
ROOT.TFile.GetKeyNames = GetKeyNames

bkg_mapping = { 'etau_2017' : {}, 'mutau_2017': {}, 'tautau_2017':{}, 'etau_2018' : {}, 'mutau_2018': {}, 'tautau_2018':{} }
    

def fix_binning_v2(inFile, channelName, year):
    inputFile  =  ROOT.TFile(inFile, "READ")
    outputFile =  ROOT.TFile(inFile.replace('_backup', ''),"RECREATE")
    keyList = sorted(set(inputFile.GetKeyNames(channelName)))
    inputFile.cd(channelName)
    outputFile.mkdir(channelName)
    for hist in keyList:
        #print hist
        tmpHist = inputFile.Get(channelName + '/' + hist)
        if 'MH3' in hist:
            tmpHist.Scale(0.06)
        outputFile.cd(channelName)
        tmpHist.Write()
    outputFile.Close()
    inputFile.Close()
        

def main():
    channels = ['etau', 'mutau', 'tautau']
    years = ['2017' , '2018']
    
    for ch in channels:
        for yr in years:
            for blinded in [True, False]:
                channelName = ch
                year = yr
                if blinded:
                    inputFile =  'bin/aux/'+year+'_backup/'+channelName+'_tmass200.root'
                else:
                    inputFile =  'bin/aux/'+year+'_backup/'+channelName+'.root'
                fix_binning_v2(inputFile, channelName, year)
                #inputFile.Close()
                

if __name__=="__main__":
    main()
