import ROOT
from CombineHarvester.CombineTools.plotting import *
ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(ROOT.kTRUE)

import json
import os 
import glob
import pandas as pd
import argparse
from get_mu import xsec_map

mA_ticks = [100, 200, 300, 350, 500, 650, 800, 1000, 1500, 2000, 2500, 3000, 3500]
ma_ticks = [1, 50, 100, 150, 200, 400, 600, 800]

def add_text(text="", lowX=0.5, lowY=0.5):
    lumi  = ROOT.TPaveText(lowX, lowY, lowX+0.1, lowY+0.1, "NDC")
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.SetTextSize(0.04)
    lumi.SetTextFont (   42 )
    lumi.AddText(text)
    return lumi

def get_json(mchi = '1'):
    files = glob.glob('limits/limits_cmb_ZprimeBaryonic_mzp*_mchi'+mchi+'.json')
    #inFile = 'limits/limits_etau_MH3_200_MH4_150.json'
    out = {}
    nPoint = 0
    if not files :
        print "File " , 'limits/limits_cmb_ZprimeBaryonic_mzp*_mchi'+mchi+'.json NOT FOUND!!!!!!'
        return
    for inFile in files:
        print inFile
        with open(inFile) as f:
            data = json.load(f)
        
        inFile = inFile.replace('.json', '')
        inFile = inFile.replace('mzp', '')
        inFile = inFile.replace('mchi', '')
        #print 'infile name == ', inFile
        #print inFile.split('_')
        mA = float(inFile.split('_')[-2])
        ma = float(inFile.split('_')[-1])
        values = data['120.0']
        values['mA'] = mA
        values['ma'] = ma
        #values = values.pop('obs')
        values['obs'] = 0.0
        _name = 'MZp_'+str(int(values['mA']))+'_MChi_'+str(int(values['ma']))
        xsec = xsec_map[_name]
        # values['exp+1'] = values['exp+1']/xsec
        # values['exp-1'] = values['exp-1']/xsec
        # values['exp+2'] = values['exp+2']/xsec
        # values['exp-2'] = values['exp-2']/xsec
        # values['exp0'] = values['exp0']/xsec
        print values
        out[ str(mA) ] = values
        data_json = json.dumps(out)
        
        with open('mchi'+mchi+'.json', 'w+') as json_file:
            json.dump(out, json_file, indent=4, sort_keys=True)


def make_plot1d(mchi=""):
    # Style and pads
    ModTDRStyle()
    canv = ROOT.TCanvas('zprimeb_limit_1d_mChi_'+mchi, 'limit_1d'+' mChi '+mchi)
    canv.SetCanvasSize(1000, 800)
    pads = OnePad()
    
    # Get limit TGraphs as a dictionary
    if not os.path.exists('mchi'+mchi+'.json'):
        print "File " , 'mchi'+mchi+'.json NOT FOUND!!!!!!'
        return 
    try:
        graphs = StandardLimitsFromJSONFile('mchi'+mchi+'.json')
    except:
        return
    # Create an empty TH1 from the first TGraph to serve as the pad axis and frame
    axis = CreateAxisHist(graphs.values()[0])
    axis.SetTitle('Limit 1D scan '+' mChi ='+mchi+'GeV')
    axis.GetXaxis().SetTitle('m Zprime [GeV]')
    axis.GetYaxis().SetTitle('95% CL limit on #mu')
    pads[0].cd()
    axis.Draw('axis')
    
    # Create a legend in the top left
    legend = PositionedLegend(0.3, 0.2, 3, 0.015)
    
    # Set the standard green and yellow colors and draw
    StyleLimitBand(graphs)
    DrawLimitBand(pads[0], graphs, legend=legend)
    legend.Draw()

    title_text = add_text('Zprime Baryonic Limit 1D scan '+' mChi ='+mchi+'GeV', 0.35, 0.91)
    title_text.Draw('SAME')

    label_text = add_text('mChi = '+mchi+'GeV', 0.7, 0.55)
    label_text.Draw('SAME')
    # Re-draw the frame and tick marks
    pads[0].SetLogy()
    pads[0].RedrawAxis()
    pads[0].GetFrame().Draw()
    
    # Adjust the y-axis range such that the maximum graph value sits 25% below
    # the top of the frame. Fix the minimum to zero.
    FixBothRanges(pads[0], 0.1, 0.1, 50, 0.25)
    
    # Standard CMS logo
    DrawCMSLogo(pads[0], 'CMS', 'Internal', 11, 0.045, 0.035, 1.2, '', 0.8)
    
    #canv.Print('.pdf')
    canv.Print('.png')
    
if __name__=="__main__":
    
    for mchi in ma_ticks:
        get_json(str(mchi))
        make_plot1d(str(mchi))
