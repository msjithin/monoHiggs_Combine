from ROOT import *

colormap = {
    '1':kRed,
    '10':kAzure+10,
    '50':kViolet,
    '100':kBlack,
    '150':kOrange-2,
    '500':kGreen,
    '1000':kBlue
}
def getLegend():
    output = TLegend(0.5, 0.6, 0.92, 0.85, "", "brNDC")
    output.SetLineWidth(0)
    output.SetLineStyle(0)
    output.SetFillStyle(0)
    output.SetBorderSize(0)
    output.SetTextFont(62)
    output.SetNColumns(2)
    
    return output
    
# leg = TLegend(xmin,ymin,xmax,ymax,"")
# leg.SetFillColor(kWhite);
# leg.SetFillStyle(0);
# leg.SetTextSize(0.045);
# return leg

def getCMSText(channel_="et" , year="2017"):
    x1,y1 = 0.58,0.95
    if year=="2018":
        lumi_label="11.94"
    else:
        lumi_label="8.2"
    ch_label = "e#tau_{h} "
    if channel_=="mt":
        ch_label = "#mu#tau_{h} "
    if channel_=="et":
        ch_label = "e#tau_{h} "
    if channel_=="tt":
        ch_label = "#tau_{h}#tau_{h} "

    texS = TLatex(x1,y1,("%s  %s fb^{-1} (13 TeV, %s)" % (ch_label, lumi_label,year)));#VS
    texS.SetNDC();
    texS.SetTextFont(42);
    texS.SetTextSize(0.048);
    texS.Draw();

    x2,y2 = 0.2,0.8
    texS1 = TLatex(x2,y2,"#bf{CMS} #it{Preliminary}"); 
    texS1.SetNDC();
    texS1.SetTextFont(42);
    texS1.SetTextSize(0.060);
    texS1.Draw();
    return texS,texS1
def data_style(graph,color=kBlack):
    graph.SetTitle("")
    graph.SetMarkerStyle(20)
    graph.SetMarkerColor(kBlack)
    graph.SetLineColor(kBlack)
def fit_style(hs,color):
    hs.SetTitle("")
    hs.GetYaxis().SetTitle("Events / GeV")
    hs.GetYaxis().SetTitleSize(0.058)
    hs.GetYaxis().SetTitleOffset(0.8)
    hs.GetYaxis().SetLabelSize(0.038)
    hs.SetLineColor(color)
    hs.SetLineWidth(2)
    hs.SetFillStyle(0)
    hs.SetFillColor(0)
def other_style(hs,color,outline=kBlack):
    hs.SetFillColor(color)
    hs.SetLineColor(outline)
def set_bounds(hs):
    ymin = min( hs[ibin] for ibin in range(1,hs.GetNbinsX()+1) if hs[ibin] != 0)
    ymax = max( hs[ibin] for ibin in range(1,hs.GetNbinsX()+1) if hs[ibin] != 0)

    hs.SetMinimum(0.005)
    hs.SetMaximum(ymax*(10**2.5))
def ratio_style(ratio,color,rymin=0.5,rymax=1.5,name='#frac{Data}{Bkg}'):
    gPad.SetGridy();
    ratio.SetMarkerSize(1);
    ratio.SetMarkerStyle(20)
    ratio.SetMarkerColor(color)
    ratio.SetLineColor(color)
    ratio.SetLineWidth(1)
    ratio.SetTitle("")
    if type(ratio) == TH1: ratio.SetStats(0);
    
    ratio.GetYaxis().CenterTitle();
    ratio.GetYaxis().SetTitle(name)
    ratio.GetYaxis().SetLabelSize(0.18);
    ratio.GetYaxis().SetTitleSize(0.18);
    ratio.GetYaxis().SetLabelFont(42);
    ratio.GetYaxis().SetTitleFont(42);
    ratio.GetYaxis().SetTitleOffset(0.2);
    ratio.GetYaxis().SetNdivisions(208);
    ratio.GetYaxis().SetRangeUser(rymin,rymax);
    # ratio.GetYaxis().SetTickLength(0.05);
    
    ratio.GetXaxis().SetLabelSize(0.15);
    ratio.GetXaxis().SetTitleSize(0.15);
    ratio.GetXaxis().SetLabelFont(42);
    ratio.GetXaxis().SetTitleFont(42);
    ratio.GetXaxis().SetTitleOffset(1.2);
    ratio.GetXaxis().SetTickLength(0.05);
def pull_style(pull,color,outline=kBlack,pymin=-3,pymax=3):
    gPad.SetGridy();
    # pull.SetMarkerStyle(20)
    pull.SetFillStyle(1001)
    pull.SetFillColor(color)
    pull.SetLineColor(outline)
    pull.SetLineWidth(1)
    pull.SetTitle("")
    pull.GetYaxis().SetRangeUser(pymin,pymax);
    pull.SetStats(0);
    pull.GetYaxis().CenterTitle();
    pull.GetYaxis().SetTitle("#frac{(Data-Bkg)}{#sigma}")
    pull.SetMarkerStyle(20);
    pull.SetMarkerSize(1);
    pull.GetYaxis().SetLabelSize(0.1);
    pull.GetYaxis().SetTitleSize(0.1);
    pull.GetYaxis().SetLabelFont(42);
    pull.GetYaxis().SetTitleFont(42);
    pull.GetYaxis().SetTitleOffset(0.35);
    pull.GetYaxis().SetNdivisions(403);
    # pull.GetYaxis().SetTickLength(0.05);
    
    pull.GetXaxis().SetLabelSize(0.15);
    pull.GetXaxis().SetTitleSize(0.18);
    pull.GetXaxis().SetLabelFont(42);
    pull.GetXaxis().SetTitleFont(42);
    pull.GetXaxis().SetTitleOffset(1.2);
    pull.GetXaxis().SetTickLength(0.05);
