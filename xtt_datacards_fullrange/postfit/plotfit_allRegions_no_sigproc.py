#!/usr/bin/env python
import os
from shutil import copyfile
import sys
from argparse import ArgumentParser
from subprocess import Popen,PIPE,STDOUT
from time import time
import json
import re
from ROOT import *
from PlotTool import *

gROOT.SetBatch(1)

outdir_base = "/afs/hep.wisc.edu/home/mallampalli/private/Analysis/MonoJet/test/postfit/Plots%s/"

prefit_color = kOrange+8
postfit_color = kGreen+2
other_color = kAzure+1

sr_colormap = {
  'ZJets':{'leg':'Z #rightarrow #nu#nu','col':kRed},
  'WJets':{'leg':'W #rightarrow l#nu','col':kViolet},
  'DYJets':{'leg':'Z #rightarrow ll','col':kSpring},
  'GJets':{'leg':'#gamma + jets','col':kYellow},
  'TTJets':{'leg':'TT Jets','col':kPink},
  'QCD':{'leg':'QCD','col':kYellow+3},
  'DiBoson':{'leg':'WW/WZ/ZZ','col':kCyan},  
}

def loop_iterator(iterator):
  object = iterator.Next()
  while object:
    yield object
    object = iterator.Next()

def iter_collection(rooAbsCollection):
  iterator = rooAbsCollection.createIterator()
  return loop_iterator(iterator)
def plotCR(cr,fitfile,info):
  fitfile.getRegion(cr)
  c = TCanvas("c", "canvas",800,800);
  gStyle.SetOptStat(0);
  gStyle.SetLegendBorderSize(0);
  
  pad1 = TPad("pad1","pad1",0.,0.33,1.0,1.0)
  pad1.Draw(); pad1.cd()
  pad1.SetLogy()
  pad1.SetBottomMargin(0)

  prefit_hs = fitfile.prefit_hs
  postfit_hs = fitfile.postfit_hs
  data_graph = fitfile.data_graph
  fitfile.getOtherBkg(cr)
  other_bkg = fitfile.other_bkg
  
  prefit_hs.Draw("hist"); fit_style(prefit_hs,prefit_color);
  set_bounds(prefit_hs)
  if postfit_hs: postfit_hs.Draw("hist same"); fit_style(postfit_hs,postfit_color)
  other_bkg.Draw("hist same"); other_style(other_bkg,other_color)
  data_graph.Draw("pex0 same"); data_style(data_graph)
  # prefit_hs.Draw("Axis same")
  pad1.RedrawAxis()
  
  leg = getLegend()
  leg.AddEntry(data_graph,"Data","lp")
  leg.AddEntry(postfit_hs,"Post-fit (%s)" % regionmap[cr]['leg'],'f')
  leg.AddEntry(prefit_hs,"Pre-fit (%s)" % regionmap[cr]['leg'],'f')
  leg.AddEntry(other_bkg,"Other Backgrounds",'f')
  leg.Draw()
  
  texCMS,texLumi = getCMSText(info.lumi_label,info.year)
  
  ##############################
  c.cd()
  pad2 = TPad("pad2","pad2",0.,0.,1.0,0.33)
  pad2.Draw(); pad2.cd()
  pad2.SetTopMargin(0)
  
  pad3 = TPad("pad3","pad3",0.,0.65,1.,1.)
  pad3.Draw(); pad3.cd()
  pad3.SetTopMargin(0); pad3.SetBottomMargin(0)

  fitfile.getFitRatio()
  prefit_ratio = fitfile.prefit_ratio
  postfit_ratio = fitfile.postfit_ratio
  
  prefit_ratio.Draw('pe'); ratio_style(prefit_ratio,prefit_color)
  if postfit_ratio: postfit_ratio.Draw('pesame'); ratio_style(postfit_ratio,postfit_color)
  
  ###############################
  pad2.cd()
  pad4 = TPad("pad4","pad4",0.,0.,1.,0.65)
  pad4.Draw(); pad4.cd()
  pad4.SetTopMargin(0);
  pad4.SetBottomMargin(0.5)

  if postfit_hs:
    fitfile.getSigmaPull()
    sigma_pull = fitfile.sigma_pull
    sigma_pull.Draw('hist'); pull_style(sigma_pull,postfit_color)
    xname = sigma_pull.GetXaxis().GetTitle().replace("(","[").replace(")","]")
    sigma_pull.GetXaxis().SetTitle( xname )
  
  ##############################

  outname = 'fit_CRonly_%s_%s.png' % (cr,info.sysdir)
  output = info.getOutputDir(outdir_base)
  import os
  if not os.path.isdir(output): os.makedirs(output)
  output = '%s/%s' % (output,outname)
  c.SaveAs(output)

def plotSR(sr,fitfile,info):
  fitfile.getRegion(sr)
  c = TCanvas("c", "canvas",800,800);
  gStyle.SetOptStat(0);
  gStyle.SetLegendBorderSize(0);
  
  pad1 = TPad("pad1","pad1",0.,0.33,1.0,1.0)
  pad1.Draw(); pad1.cd()
  pad1.SetLogy()
  pad1.SetBottomMargin(0)

  prefit_hs = fitfile.prefit_hs
  postfit_hs = fitfile.postfit_hs
  data_graph = fitfile.data_graph
  all_bkg = fitfile.getAllBkg(sr)

  leg = getLegend()

  bkg_stack = THStack("postfit_stacked_bkg","")
  i= 0 
  for tmp in all_bkg:
       tmp[0].SetFillColor(sr_colormap[tmp[1]]['col'])
       bkg_stack.Add(tmp[0],"hist")
       leg.AddEntry(tmp[0],'Postfit %s'%(sr_colormap[tmp[1]]['leg']),'f')       
       if (i==0):  set_bounds(tmp[0]);i+=1
  bkg_stack.Draw()   

  data_graph.Draw("pex0 same"); data_style(data_graph) 
  leg.AddEntry(data_graph,"Data","lp")

  # prefit_hs.Draw("Axis same")
  pad1.RedrawAxis()
  leg.Draw()
  
  texCMS,texLumi = getCMSText(info.lumi_label,info.year)
  
  ##############################
  c.cd()
  pad2 = TPad("pad2","pad2",0.,0.,1.0,0.33)
  pad2.Draw(); pad2.cd()
  pad2.SetTopMargin(0)
  
  pad3 = TPad("pad3","pad3",0.,0.65,1.,1.)
  pad3.Draw(); pad3.cd()
  pad3.SetTopMargin(0); pad3.SetBottomMargin(0)

  fitfile.getFitRatio()
  prefit_ratio = fitfile.prefit_ratio
  postfit_ratio = fitfile.postfit_ratio
  
  prefit_ratio.Draw('pe'); ratio_style(prefit_ratio,prefit_color)
  if postfit_ratio: postfit_ratio.Draw('pesame'); ratio_style(postfit_ratio,postfit_color)
  
  ###############################
  pad2.cd()
  pad4 = TPad("pad4","pad4",0.,0.,1.,0.65)
  pad4.Draw(); pad4.cd()
  pad4.SetTopMargin(0);
  pad4.SetBottomMargin(0.5)

  if postfit_hs:
    fitfile.getSigmaPull()
    sigma_pull = fitfile.sigma_pull
    sigma_pull.Draw('hist'); pull_style(sigma_pull,postfit_color)
    xname = sigma_pull.GetXaxis().GetTitle().replace("(","[").replace(")","]")
    sigma_pull.GetXaxis().SetTitle( xname )
  
  ##############################

  outname = 'fit_CRonly_%s_%s.png' % (sr,info.sysdir)
  output = info.getOutputDir(outdir_base)
  import os
  if not os.path.isdir(output): os.makedirs(output)
  output = '%s/%s' % (output,outname)
  c.SaveAs(output) 


def plotFit_result(path):
  import os  # need to add these as not working for some strange reason..
  from PlotTool import regionmap
  global regionmap
  if 'nCR' in path: return
  cwd = os.getcwd()
  info = SysInfo(path)
  os.chdir('%s/allRegions_no_sigproc_fit' % path)
  tfile = FitFile("fitDiagnostics_fit_allRegions_no_sigproc_result.root")
  crlist = [ crdir.GetName() for crdir in tfile.Get('shapes_prefit').GetListOfKeys() if any( cr in crdir.GetName() for cr in regionmap ) ]
  srlist = [ srdir.GetName() for srdir in tfile.Get('shapes_prefit').GetListOfKeys() if 'sr' in srdir.GetName()]
  for cr in crlist:
    regionmap[cr] = regionmap[cr.split('_')[0]]
    plotCR(cr,tfile,info)
  for sr in srlist:
    plotSR(sr,tfile,info)
  os.chdir(cwd)
##############################################################################
def getargs():
    def directory(arg):
        if os.path.isdir(arg): return arg
        raise ValueError()
    parser = ArgumentParser(description='Run all avaiable limits in specified directory')
    parser.add_argument("-d","--dir",help='Specify the directory to run limits in',nargs='+',action='store',type=directory,required=True)
    parser.add_argument("-r","--reset")
    try: args = parser.parse_args()
    except:
        parser.print_help()
        exit()
    return args
##############################################################################
if __name__ == "__main__":
#    args = getargs()
#    for dir in args.dir: plotFit_result(dir)
     plotFit_result('Limits_LQ_Run2_postfit_test/recoil/recoil_Run2.sys/')