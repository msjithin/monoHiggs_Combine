from ROOT import TCanvas, TPad, TFormula, TF1, TPaveLabel, TH1F, TH2F, TFile
from ROOT import gROOT, gBenchmark, gStyle, gRandom, gPad
import numpy as np
 
mA_ticks = [200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0]
ma_ticks = [100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0, 500.0]


def make_plot(channel = '', year='2017', data_obs=[], data_exp=[], data_exp_p1=[], data_exp_m1=[]):
    c03 = TCanvas("c03","c03", 900, 900)
    gStyle.SetOptStat(0)
    #palette = [15, 20, 23, 30, 32]
    gStyle.SetPalette(92)
    h_col = TH2F("h_col","Limit "+channel+" "+year, 8, 200, 1000, 9, 100, 550)
    obs = TH2F("obs","obs",8, 200, 1000, 9, 100, 550)
    exp = TH2F("exp","exp",8, 200, 1000, 9, 100, 550)
    exp_p1 = TH2F("exp_p1","exp_p1",8, 200, 1000, 9, 100, 550)
    exp_m1 = TH2F("exp_m1","exp_m1",8, 200, 1000, 9, 100, 550)
    data_obs = np.array(data_obs)
    data_exp = np.array(data_exp)
    data_exp_p1 = np.array(data_exp_p1)
    data_exp_m1 = np.array(data_exp_m1)
    
    for i in range(len(mA_ticks)):
        for j in range(len(ma_ticks)):
            mA = mA_ticks[i]
            ma = ma_ticks[j]
            h_col.Fill(mA, ma, data_obs[i][j])
            #obs.Fill(mA, ma, data_obs[i][j])
            exp.Fill(mA, ma, data_exp[i][j])
            exp_p1.Fill(mA, ma, data_exp_p1[i][j])
            exp_m1.Fill(mA, ma, data_exp_m1[i][j])
        
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
    
    h_col.GetXaxis().SetTitle('mA [GeV]')
    h_col.GetYaxis().SetTitle('ma [GeV]')
    gPad.SetRightMargin(0.2) 
    c03.SaveAs("limit_"+channel+"_"+year+".png")
