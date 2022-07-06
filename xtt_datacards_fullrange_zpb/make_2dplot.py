from ROOT import TCanvas, TPad, TFormula, TF1, TPaveLabel, TH1F, TH2F, TFile, TColor
from ROOT import gROOT, gBenchmark, gStyle, gRandom, gPad
import numpy as np
from array import array 
mA_ticks = [100, 200, 300, 350, 500, 650, 800, 1000, 1500, 2000, 2500, 3000, 3500]
ma_ticks = [1, 50, 100, 150, 200, 400, 600, 800]
def set_palette(name="", ncontours=999):
    """Set a color palette from a given RGB list
    stops, red, green and blue should all be lists of the same length
    see set_decent_colors for an example"""

    if name == "gray" or name == "grayscale":
        stops = [0.00, 0.34, 0.61, 0.84, 1.00]
        red   = [1.00, 0.84, 0.61, 0.34, 0.00]
        green = [1.00, 0.84, 0.61, 0.34, 0.00]
        blue  = [1.00, 0.84, 0.61, 0.34, 0.00]
    # elif name == "whatever":
        # (define more palettes)
    else:
        # default palette, looks cool
        stops = [0.00, 0.34, 0.61, 0.84, 1.00]
        #red   = [0.00, 0.00, 0.87, 1.00, 0.51]
        red = [0.00, 0.00, 0.0, 0.00, 0.0]
        green = [0.00, 0.81, 1.00, 0.20, 0.00]
        blue  = [0.51, 1.00, 0.12, 0.00, 0.00]

    s = array('d', stops)
    r = array('d', red)
    g = array('d', green)
    b = array('d', blue)

    npoints = len(s)
    TColor.CreateGradientColorTable(npoints, s, r, g, b, ncontours)
    gStyle.SetNumberContours(ncontours)

def make_plot(channel = '', year='2017', data_obs=[], data_exp=[], data_exp_p1=[], data_exp_m1=[]):
    c03 = TCanvas("c03","c03", 1200, 900)
    gStyle.SetOptStat(0)
    #set_palette()
    #gStyle.SetNumberContours(255)
    #palette = [15, 20, 23, 30, 32]
    gStyle.SetPalette(57)
    gStyle.SetNumberContours(999)
    #gStyle.SetPalette("kBird")

    xi = [i for i in range(len(mA_ticks))]
    yi = [i for i in range(len(ma_ticks))]
    
    _year = year
    if _year=='20172018':
        _year = '2017+2018'
    h_col = TH2F("h_col","Zprime Baryonic Limit "+channel+" "+_year, len(mA_ticks), 0, len(mA_ticks), len(ma_ticks), 0, len(ma_ticks))
    obs = TH2F("obs","obs",len(mA_ticks), 0, len(mA_ticks), len(ma_ticks), 0, len(ma_ticks))
    exp = TH2F("exp","exp",len(mA_ticks), 0, len(mA_ticks), len(ma_ticks), 0, len(ma_ticks))
    exp_p1 = TH2F("exp_p1","exp_p1",len(mA_ticks), 0, len(mA_ticks), len(ma_ticks), 0, len(ma_ticks))
    exp_m1 = TH2F("exp_m1","exp_m1",len(mA_ticks), 0, len(mA_ticks), len(ma_ticks), 0, len(ma_ticks))
    data_obs = np.array(data_obs)
    data_exp = np.array(data_exp)
    data_exp_p1 = np.array(data_exp_p1)
    data_exp_m1 = np.array(data_exp_m1)
    
    for i in range(len(mA_ticks)):
        for j in range(len(ma_ticks)):
            mA = i
            ma = j
            #h_col.Fill(mA, ma, round(data_obs[i][j], 3))
            #print mA, ma, data_obs[i][j]
            #obs.Fill(mA, ma, data_obs[i][j])
            h_col.Fill(mA, ma, round(data_exp[i][j],3))
            exp.Fill(mA, ma, round(data_exp[i][j],3))
            exp_p1.Fill(mA, ma, round(data_exp_p1[i][j],3))
            exp_m1.Fill(mA, ma, round(data_exp_m1[i][j],3))
    
    for i in range(len(mA_ticks)):
        h_col.GetXaxis().SetBinLabel(i+1, str(mA_ticks[i]))
    for i in range(len(ma_ticks)):
        h_col.GetYaxis().SetBinLabel(i+1, str(ma_ticks[i]))


    gPad.SetLogz(1)
    h_col.GetZaxis().SetRangeUser(0.1, 10000);
    h_col.Draw("COLZ")
    # write obs
    # obs.SetMarkerSize(0.9)
    # obs.SetMarkerColor(4)
    # obs.SetBarOffset(0.1)
    # obs.Draw("TEXT SAME")
    # write exp
    exp.SetMarkerSize(0.9)
    exp.SetMarkerColor(1)
    exp.SetBarOffset(-0.1)
    exp.Draw("TEXT SAME")
    # write exp_p1
    exp_p1.SetMarkerSize(0.9)
    exp_p1.SetMarkerColor(2)
    exp_p1.SetBarOffset(0.3)
    exp_p1.Draw("TEXT SAME")
    # write exp_m1
    exp_m1.SetMarkerSize(0.9)
    exp_m1.SetMarkerColor(2)
    exp_m1.SetBarOffset(-0.3)
    exp_m1.Draw("TEXT SAME")
    
    h_col.GetXaxis().SetTitle('m Zp [GeV]')
    h_col.GetYaxis().SetTitle('m Chi [GeV]')
    gPad.SetGrid()
    gPad.SetRightMargin(0.2) 
    c03.SaveAs("zprimeb_limit_"+channel+"_"+year+".png")
