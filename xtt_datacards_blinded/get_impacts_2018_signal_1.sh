#!bin/bash
#example commands to run impact plots, any signal directory is ok. 
set -e
# combineCards.py card_1.txt card_2.txt card_3.txt > card_combined.txt
#~/public_html/limits/sample_new/sample/2018_till2000GeV
out_directory=$output_dir/2018_till2000GeV/

tt(){
    combineTool.py -M T2W -i 2hdma_med400_ps100/xtt_tt_1_13TeV_2018.txt -o tt_workspace_400_2018.root
    combineTool.py -M Impacts -d 2hdma_med400_ps100/tt_workspace_400_2018.root -m 400 --expectSignal=1 --doInitialFit  --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerStrategy 0 --rMin -20 --rMax 20 --robustFit 1 --X-rtd MINIMIZER_analytic --parallel 10
    combineTool.py -M Impacts -d 2hdma_med400_ps100/tt_workspace_400_2018.root -m 400 --expectSignal=1 --doFits  --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerStrategy 0 --rMin -20 --rMax 20 --robustFit 1 --X-rtd MINIMIZER_analytic --parallel 10
    combineTool.py -M Impacts -d 2hdma_med400_ps100/tt_workspace_400_2018.root -m 400 -o impacts_tt_m400_2018.json --parallel 10
    plotImpacts.py -i impacts_tt_m400_2018.json -o impacts_tt_m400_2018_signal1
    cp impacts_tt_m400_2018_signal1.pdf  $out_directory
}
et(){
    echo "expect_signal = 1"
    combineTool.py -M T2W -i 2hdma_med400_ps100/xtt_et_1_13TeV_2018.txt -o et_workspace_400_2018.root
    combineTool.py -M Impacts -d 2hdma_med400_ps100/et_workspace_400_2018.root -m 400 --expectSignal=1 --doInitialFit  --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerStrategy 0 --rMin -20 --rMax 20 --robustFit 1 --X-rtd MINIMIZER_analytic --parallel 10
    combineTool.py -M Impacts -d 2hdma_med400_ps100/et_workspace_400_2018.root -m 400 --expectSignal=1 --doFits  --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerStrategy 0 --rMin -20 --rMax 20 --robustFit 1 --X-rtd MINIMIZER_analytic --parallel 10
    combineTool.py -M Impacts -d 2hdma_med400_ps100/et_workspace_400_2018.root -m 400 -o impacts_et_m400_2018.json --parallel 10
    plotImpacts.py -i impacts_et_m400_2018.json -o impacts_et_m400_2018_signal1
    cp impacts_et_m400_2018_signal1.pdf $out_directory

}
mt(){
    combineTool.py -M T2W -i 2hdma_med400_ps100/xtt_mt_1_13TeV_2018.txt -o mt_workspace_400_2018.root
    combineTool.py -M Impacts -d 2hdma_med400_ps100/mt_workspace_400_2018.root -m 400 --expectSignal=1 --doInitialFit  --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerStrategy 0 --rMin -20 --rMax 20 --robustFit 1 --X-rtd MINIMIZER_analytic --parallel 10
    combineTool.py -M Impacts -d 2hdma_med400_ps100/mt_workspace_400_2018.root -m 400 --expectSignal=1 --doFits  --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerStrategy 0 --rMin -20 --rMax 20 --robustFit 1 --X-rtd MINIMIZER_analytic --parallel 10
    combineTool.py -M Impacts -d 2hdma_med400_ps100/mt_workspace_400_2018.root -m 400 -o impacts_mt_m400_2018.json --parallel 10
    plotImpacts.py -i impacts_mt_m400_2018.json -o impacts_mt_m400_2018_signal1
    cp impacts_mt_m400_2018_signal1.pdf $out_directory

}
cmb(){
    combineTool.py -M T2W -i 2hdma_med400_ps100/xtt_cmb_1_13TeV_2018.txt -o cmb_workspace_400_2018.root
    combineTool.py -M Impacts -d 2hdma_med400_ps100/cmb_workspace_400_2018.root -m 400 --expectSignal=1 --doInitialFit  --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerStrategy 0 --rMin -20 --rMax 20 --robustFit 1 --X-rtd MINIMIZER_analytic --parallel 10
    combineTool.py -M Impacts -d 2hdma_med400_ps100/cmb_workspace_400_2018.root -m 400 --expectSignal=1 --doFits  --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerStrategy 0 --rMin -20 --rMax 20 --robustFit 1 --X-rtd MINIMIZER_analytic --parallel 10
    combineTool.py -M Impacts -d 2hdma_med400_ps100/cmb_workspace_400_2018.root -m 400 -o impacts_cmb_m400_2018.json --parallel 10
    plotImpacts.py -i impacts_cmb_m400_2018.json -o impacts_cmb_m400_2018_signal1
    cp impacts_cmb_m400_2018_signal1.pdf $out_directory
}



while getopts emtc option
do
    case "${option}"
    in
        e) et ;;
	m) mt ;;
	t) tt ;;
	c) cmb ;;
	\? ) echo "Usage: bash runsample_2018.sh  [-e, -m , -t]"
    esac
done

if [ $# -eq 0 ]; then
    echo "No arguments provided
    e) get etau 
    m) get mutau 
    t) get tautau
    c) combined 
    s) --expectSignal = 0/1
   "
    echo "Enter option e, m, t , c and/or s"
    exit 1
fi
