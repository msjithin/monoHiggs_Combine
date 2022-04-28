
set -e

# combineCards.py card_1.txt card_2.txt card_3.txt > card_combined.txt
out_directory_2017=$output_dir/2017_till2000GeV/
out_directory_2018=$output_dir/2018_till2000GeV/
fitdiag_file="fitDiagnostics.root"
et_2017(){
    if [ -f "$fitdiag_file" ] ; then
	rm "$fitdiag_file"
    fi
    echo "###################################################"
    echo "etau 2017"
    combineTool.py -M T2W -i 2hdma_med400_ps100/xtt_et_1_13TeV_2017.txt -o et_workspace_400_2017.root
    combine -M FitDiagnostics -d 2hdma_med400_ps100/et_workspace_400_2017.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --expectSignal=1
    python diffNuisances.py fitDiagnostics.root --all --abs -g etau_plotdiff_2017.root
    cp *etau*2017.png $out_directory_2017
}

mt_2017(){
    if [ -f "$fitdiag_file" ] ; then
	 rm "$fitdiag_file"
    fi
    echo "###################################################"
    echo "mutau 2017"
    combineTool.py -M T2W -i 2hdma_med400_ps100/xtt_mt_1_13TeV_2017.txt -o mt_workspace_400_2017.root
    combine -M FitDiagnostics -d 2hdma_med400_ps100/mt_workspace_400_2017.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --expectSignal=1 
    #--X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerStrategy 0
    python diffNuisances.py fitDiagnostics.root --all --abs -g mutau_plotdiff_2017.root
    cp *mutau*2017.png $out_directory_2017
}

tt_2017(){
    if [ -f "$fitdiag_file" ] ; then
	rm "$fitdiag_file"
    fi
    echo "###################################################"
    echo "tatau 2017"
    combineTool.py -M T2W -i 2hdma_med400_ps100/xtt_tt_1_13TeV_2017.txt -o tt_workspace_400_2017.root
    combine -M FitDiagnostics -d 2hdma_med400_ps100/tt_workspace_400_2017.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --expectSignal=1 
    python diffNuisances.py fitDiagnostics.root --all --abs -g tautau_plotdiff_2017.root
    cp *tautau*2017.png $out_directory_2017
}

et_2018(){
    if [ -f "$fitdiag_file" ] ; then
	 rm "$fitdiag_file"
    fi
    echo "###################################################"
    echo "etau 2018"
    combineTool.py -M T2W -i 2hdma_med400_ps100/xtt_et_1_13TeV_2018.txt -o et_workspace_400_2018.root
    combine -M FitDiagnostics -d 2hdma_med400_ps100/et_workspace_400_2018.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --expectSignal=1 
    python diffNuisances.py fitDiagnostics.root --all --abs -g etau_plotdiff_2018.root
    cp *etau*2018.png $out_directory_2018
}

mt_2018(){
    if [ -f "$fitdiag_file" ] ; then
	rm "$fitdiag_file"
    fi
    echo "###################################################"
    echo "mutau 2018"
    combineTool.py -M T2W -i 2hdma_med400_ps100/xtt_mt_1_13TeV_2018.txt -o mt_workspace_400_2018.root
    combine -M FitDiagnostics -d 2hdma_med400_ps100/mt_workspace_400_2018.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --expectSignal=1 
    python diffNuisances.py fitDiagnostics.root --all --abs -g mutau_plotdiff_2018.root
    cp *mutau*2018.png $out_directory_2018
}

tt_2018(){
    if [ -f "$fitdiag_file" ] ; then
	 rm "$fitdiag_file"
    fi
    echo "###################################################"
    echo "tatau 2017"
    combineTool.py -M T2W -i 2hdma_med400_ps100/xtt_tt_1_13TeV_2018.txt -o tt_workspace_400_2018.root
    combine -M FitDiagnostics -d 2hdma_med400_ps100/tt_workspace_400_2018.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --expectSignal=1 
    python diffNuisances.py fitDiagnostics.root --all --abs -g tautau_plotdiff_2018.root
    cp *tautau*2018.png $out_directory_2018
}
cmb_2017(){
    if [ -f "$fitdiag_file" ] ; then
	 rm "$fitdiag_file"
    fi
    echo "###################################################"
    echo "cmb 2017"
    combineTool.py -M T2W -i 2hdma_med400_ps100/xtt_cmb_1_13TeV_2017.txt -o cmb_workspace_400_2017.root
    combine -M FitDiagnostics -d 2hdma_med400_ps100/cmb_workspace_400_2017.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --expectSignal=1 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH 
    python diffNuisances.py fitDiagnostics.root --all --abs -g cmb_plotdiff_2017.root
    cp *cmb*_2017.png $out_directory_2017
}
cmb_2018(){
    if [ -f "$fitdiag_file" ] ; then
	 rm "$fitdiag_file"
    fi
    echo "###################################################"
    echo "cmb 2018"
    combineTool.py -M T2W -i 2hdma_med400_ps100/xtt_cmb_1_13TeV_2018.txt -o cmb_workspace_400_2018.root
    combine -M FitDiagnostics -d 2hdma_med400_ps100/cmb_workspace_400_2018.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --expectSignal=1 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH 
    python diffNuisances.py fitDiagnostics.root --all --abs -g cmb_plotdiff_2018.root
    cp *cmb*_2018.png $out_directory_2018
}
cmb_20172018(){
    if [ -f "$fitdiag_file" ] ; then        
	rm "$fitdiag_file"
    fi
    echo "###################################################"
    echo "cmb 20172018"
    combineTool.py -M T2W -i 2hdma_med400_ps100/xtt_cmb_1_13TeV_20172018.txt -o cmb_workspace_400_20172018.root
    combine -M FitDiagnostics -d 2hdma_med400_ps100/cmb_workspace_400_20172018.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --expectSignal=1 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH 
    python diffNuisances.py fitDiagnostics.root --all --abs -g cmb_plotdiff_20172018.root
    cp *cmb*_20172018.png $out_directory_2018
}

all(){
    et_2017
    et_2018
    
    mt_2017
    mt_2018

    tt_2017
    tt_2018

    # cmb_2017
    # cmb_2018
    # cmb_20172018
}

cmb(){
    cmb_2017
    cmb_2018
    cmb_20172018
}
echo "bash get_pull_plots.sh  et_2017 , all"
"$@"
