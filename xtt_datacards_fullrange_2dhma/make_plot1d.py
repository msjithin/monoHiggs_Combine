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

mA_ticks = [200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1200.0, 1600.0]
ma_ticks = [100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0, 500.0]

def add_text(text="", lowX=0.5, lowY=0.5 , color=1, font=42, size=0.04):
    lumi  = ROOT.TPaveText(lowX, lowY, lowX+0.1, lowY+0.1, "NDC")
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    color )
    lumi.SetTextSize(0.04)
    lumi.SetTextFont (   font )
    lumi.AddText(text)
    return lumi

def get_json(mchi = '1', cat='gg'):
    mchi = str(mchi)
    files = glob.glob('limits/limits_cmb_2HDMa_'+cat+'_sinp_0p35_tanb_1p0_*_MH4_'+mchi+'.json')
    if cat =='bbgg':
        files = glob.glob('limits_bbgg/limits_cmb_2HDMa_'+cat+'_sinp_0p35_tanb_1p0_*_MH4_'+mchi+'.json')
    #inFile = 'limits/limits_cmb_2HDMa_bb_sinp_0p35_tanb_1p0_mXd_10_MH3_1200_MH4_250.json'
    out = {}
    nPoint = 0
    if not files :
        return
    for inFile in files:
        print inFile
        with open(inFile) as f:
            data = json.load(f)
        
        inFile = inFile.split('/')[-1]
        inFile = inFile.replace('.json', '')
        inFile = inFile.split('_')

        mA = float(inFile[1 + inFile.index('MH3')])
        ma = float(inFile[1 + inFile.index('MH4')])
        values = data['120.0']
        values['mA'] = mA
        values['ma'] = ma
        values['proc']  = inFile[1 + inFile.index('2HDMa')]
        values['sinetheta']  = inFile[1 + inFile.index('sinp')].replace('p', '.')
        values['tanbeta']  = inFile[1 + inFile.index('tanb')].replace('p', '.')
        _name = '_'.join(inFile[inFile.index('2HDMa') : ])
        # values['exp0'] = values['exp0'] / xsec_map[_name]
        # values['exp+1'] = values['exp+1'] / xsec_map[_name]
        # values['exp-1'] = values['exp-1'] / xsec_map[_name]
        # values['exp+2'] = values['exp+2'] / xsec_map[_name]
        # values['exp-2'] = values['exp-2'] / xsec_map[_name]
        #print _name,  xsec_map[_name]
        values['obs'] = 0.0
        #xsec_map[_name]
        print values
        out[ str(mA) ] = values
        data_json = json.dumps(out)
        
        with open(cat+'_ma'+mchi+'.json', 'w+') as json_file:
            json.dump(out, json_file, indent=4, sort_keys=True)

def make_plotid(mchi="", cat='gg'):
    if not os.path.exists(cat+'_ma'+str(mchi)+'.json'):
        return

    # Style and pads
    ModTDRStyle()
    canv = ROOT.TCanvas('2hdma_limit_1d_'+cat+'_ma_'+mchi, 'limit_1d'+' ma '+mchi)
    canv.SetCanvasSize(1000, 800)
    pads = OnePad()
    try:
        # Get limit TGraphs as a dictionary
        graphs = StandardLimitsFromJSONFile(cat+'_ma'+str(mchi)+'.json')
    except:
        return
    # Create an empty TH1 from the first TGraph to serve as the pad axis and frame
    axis = CreateAxisHist(graphs.values()[0])
    axis.SetTitle('Limit 1D scan '+cat+' ma ='+mchi+'GeV')
    axis.GetXaxis().SetTitle('mass A [GeV]')
    axis.GetYaxis().SetTitle('95% CL limit on #mu')
    pads[0].cd()
    axis.Draw('axis')
    
    # Create a legend in the top left
    legend = PositionedLegend(0.3, 0.2, 3, 0.015)
    
    # Set the standard green and yellow colors and draw
    StyleLimitBand(graphs)
    DrawLimitBand(pads[0], graphs, legend=legend)
    legend.Draw()
    
    title_text = add_text('2HDMa Limit 1D scan '+cat+' ma ='+mchi+'GeV', 0.35, 0.91)
    title_text.Draw('SAME')

    
    label_text = add_text('ma = '+mchi+'GeV', 0.7, 0.65)
    label_text.Draw('SAME')

    cat_text = add_text(cat, 0.5, 0.85, color=2, font=61, size=0.08)
    cat_text.Draw('SAME')

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
    ma_ticks = [100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0, 500.0]
    for ma in ma_ticks:
        for cat in ['gg', 'bb']:
            get_json(str(int(ma)), cat)
            make_plotid(str(ma) , cat)
            
