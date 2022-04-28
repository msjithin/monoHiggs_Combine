import CombineHarvester.CombineTools.plotting as plot
import ROOT
import numpy

ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(ROOT.kTRUE)

plot.ModTDRStyle()

def fixBinning(hist=None , refHist=None ):
    if hist is None or refHist is None:
        print "Define input histograms"
        return
    nDivXAxis= refHist.GetNbinsX()
    tmpHist = refHist.Clone()
    tmpHist.Reset()
    for ibin in range(1, nDivXAxis+1):
        tmpHist.SetBinContent(ibin , hist.GetBinContent(ibin))
    return tmpHist

canvas = ROOT.TCanvas("canvas","",0,0,1300,1200)
pad1 = ROOT.TPad("pad1","pad1",0,0.25,1,1)
pad1.SetLeftMargin(0.15) #0.15
pad1.SetRightMargin(0.15) #0.1
pad1.SetTopMargin(0.122)
pad1.SetBottomMargin(0.025)
pad2 = ROOT.TPad("pad2","pad2",0,0,1,0.25)
pad2.SetTopMargin(0.02);
pad2.SetBottomMargin(0.35);
pad2.SetLeftMargin(0.15);
pad2.SetRightMargin(0.15);

fin = ROOT.TFile('fitDiagnostics.root')
f_prefit = ROOT.TFile('common/et_2017_2hdma_med400_ps150.root')

first_dir = 'shapes_fit_b'
prefit_dir = 'shapes_prefit'
second_dir = 'xtt_et_1_13TeV'
h_bkg = fin.Get(first_dir + '/' + second_dir + '/total_background')
h_sig = fin.Get(first_dir + '/' + second_dir + '/total_signal')
h_dat = fin.Get(first_dir + '/' + second_dir + '/data')  # This is a TGraphAsymmErrors, not a TH1F

h_bkg_prefit = fin.Get(prefit_dir + '/' + second_dir + '/total_background')
#xbins = numpy.array((40, 60, 90, 120, 150, 180, 210, 235, 260, 285, 325, 400, 2000))
#h_dat = h_dat.Rebin(12 , 'data' , xbins)
#h_sig = h_sig.Rebin(12 , 'signal' , xbins)
#h_bkg = h_bkg.Rebin(12 , 'bkg' , xbins)

h2_data = f_prefit.Get(second_dir +'/'+'data_obs')
h2_bkg = f_prefit.Get(second_dir  +'/'+'jetFakes')
h2_bkg.Add(f_prefit.Get(second_dir +'/'+ 'ZTTjet'))
h2_bkg.Add(f_prefit.Get(second_dir +'/'+ 'ZLLjet'))
h2_bkg.Add(f_prefit.Get(second_dir +'/'+ 'TT'))
h2_bkg.Add(f_prefit.Get(second_dir +'/'+ 'otherMC'))
h2_bkg.Add(f_prefit.Get(second_dir +'/'+ 'STT'))
h2_bkg.Add(f_prefit.Get(second_dir +'/'+ 'VVT'))

# h_bkg = fixBinning(h_bkg , h2_data)
# h_sig = fixBinning(h_sig , h2_data)
h2_data = fixBinning(h2_data , h_bkg)

canvas.cd()
pad1.Draw()
pad1.cd()
h_bkg.SetFillColor(ROOT.TColor.GetColor(100, 192, 232))
h_bkg.Draw('HIST')

h_err = h_bkg.Clone()
h_err.SetFillColorAlpha(12, 0.3)  # Set grey colour (12) and alpha (0.3)
h_err.SetMarkerSize(0)
h_err.Draw('E2SAME')

h_sig.SetLineColor(ROOT.kRed)
h_sig.Draw('HISTSAME')

h_bkg_prefit.SetLineColor(ROOT.kBlue)
h_bkg_prefit.SetMarkerStyle(4)
h_bkg_prefit.Draw('HISTSAME')
h_dat.Draw('PSAME')
h2_data.SetMarkerStyle(22)
h2_data.SetMarkerSize(2)
h2_data.Draw('e0PSAME')

print " Data = {} \n prefit = {} \n postfit = {} \n signal = {} \n".format(h_dat.Integral(), h_bkg.Integral(), h_bkg_prefit.Integral() , h_sig.Integral())
print "From original file :"
print " Data = {} \n prefit = {} \n".format(h2_data.Integral(), h2_bkg.Integral() )

h_bkg.SetMaximum(h_bkg.GetMaximum() * 1.4)
h_bkg.GetXaxis().SetTitle("")
h_bkg.GetXaxis().SetTitleSize(0)
h_bkg.GetXaxis().SetLabelSize(0)
legend = ROOT.TLegend(0.60, 0.70, 0.85, 0.87, '', 'NBNDC')
legend.AddEntry(h_bkg, 'prefit Background', 'F')
legend.AddEntry(h_bkg_prefit, 'postfit', 'L')
legend.AddEntry(h_sig, 'Signal', 'L')
legend.AddEntry(h_err, 'Background uncertainty', 'F')
legend.Draw()

canvas.cd()
pad2.Draw()
pad2.cd()
denominator = h_bkg.Clone()
ratio_prefit = h_bkg_prefit.Clone()
ratio_postfit = h_bkg.Clone()

ratio_prefit.Divide(denominator)
ratio_postfit.Divide(denominator)
ratio_postfit.Draw()
ratio_prefit.GetXaxis().SetTitle("tot tr mass")
ratio_prefit.SetMarkerColor(1)
ratio_prefit.SetLineColor(1)
ratio_prefit.SetTitle("")
ratio_prefit.GetXaxis().SetLabelSize(0.1)
ratio_prefit.GetYaxis().SetTitle("prefit/postfit")
ratio_prefit.GetXaxis().SetTitleSize(0.15)
ratio_prefit.GetYaxis().SetTitleSize(0.15)
ratio_prefit.GetYaxis().SetTitleOffset(0.3)
ratio_prefit.GetYaxis().SetLabelSize(0.08)
ratio_prefit.SetMaximum(1.5)
ratio_prefit.SetMinimum(0.5)

ratio_prefit.Draw("e0p")
ratio_postfit.Draw("e2same")

canvas.SaveAs('plot.pdf')
canvas.SaveAs('plot.png')
canvas.Close()
