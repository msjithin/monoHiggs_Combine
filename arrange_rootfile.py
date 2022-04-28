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
import os
# from sys import path
# path.append("../../../MacrosAndScripts/")
# from myPlotStyle import *
ROOT.gStyle.SetFrameLineWidth(1)
ROOT.gStyle.SetLineWidth(2)
ROOT.gStyle.SetOptStat(0)

        
def checkHistogram(f, histogram):
    isthere=  f.GetListOfKeys().Contains(histogram)
    #print(isthere)
    return isthere


def GetKeyNames( self, dir = "" ):
    self.cd(dir)
    return [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]
ROOT.TFile.GetKeyNames = GetKeyNames


def getHistList(inFile):
    
    #outFile =  ROOT.TFile('sample_v2_etau.root',"UPDATE")
    channels = ['etau', 'mutau' , 'tautau']
    
    for ch in channels:
        keyList = inFile.GetKeyNames(ch)
        print 'channel : ', ch
        if not os.path.isdir('bin/aux/'+ch):
            os.mkdir('bin/aux/'+ch)
        for tdir in keyList:
            print tdir
            outfilepath = 'bin/aux/'+ch+'/'+tdir
            if not os.path.isdir(outfilepath):
                os.mkdir(outfilepath)
            outFile =  ROOT.TFile(outfilepath+'/'+ch+'.root',"UPDATE")
            if not outFile.GetDirectory(ch):
                outFile.mkdir(ch)
            hlist = inFile.GetKeyNames(ch+'/'+tdir)
            for h in hlist:
                tmpHist = inFile.Get(ch+'/'+tdir+'/'+h)
                print 'integral for {} = {}'.format(h , tmpHist.Integral())
                outFile.cd(ch)
                tmpHist.Write()
                if 'signal' in h:
                    newName = h.replace('signal', tdir)
                    tmpHist.SetName(newName)
                    tmpHist.Write()
            outFile.Close()
    return 

fname = 'bin/aux/datacard_shapes_v2.root'
rootfile = ROOT.TFile(fname,"READ")
getHistList(rootfile)
rootfile.Close()
    
