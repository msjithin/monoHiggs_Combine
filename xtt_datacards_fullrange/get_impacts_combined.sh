


cmb(){
    combineTool.py -M T2W -i 2hdma_med400_ps100/xtt_cmb_1_13TeV_20172018.txt -o cmb_workspace_400_20172018.root
    combineTool.py -M Impacts -d 2hdma_med400_ps100/cmb_workspace_400_20172018.root -m 400 -t -1 --expectSignal=0 --doInitialFit --parallel 10 --rMin -20 --rMax 20 --cminDefaultMinimizerStrategy 0 --robustFit 1 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH
    combineTool.py -M Impacts -d 2hdma_med400_ps100/cmb_workspace_400_20172018.root -m 400 -t -1 --expectSignal=0 --doFits --parallel 10 --rMin -20 --rMax 20 --robustFit 1 --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH
    combineTool.py -M Impacts -d 2hdma_med400_ps100/cmb_workspace_400_20172018.root -m 400 -o impacts_cmb_m400_20172018_signal0.json --parallel 10
    plotImpacts.py -i impacts_cmb_m400_20172018_signal0.json -o impacts_cmb_m400_20172018_signal0
    cp impacts_cmb_m400_20172018_signal0.pdf $output_dir/2017_v2/
    cp impacts_cmb_m400_20172018_signal0.pdf $output_dir/2018_v2/
}

expect_signal="1"
while getopts c option
do
    case "${option}"
	in
	c) cmb ;;
	\? ) echo "Usage: bash file.sh  [-c] "
    esac
done

if [ $# -eq 0 ]; then
    echo "No arguments provided
    c) get 3 channls combined both years
   "
    echo "Enter option c "
    exit 1
fi
