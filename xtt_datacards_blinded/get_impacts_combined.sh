


cmb_2017(){
    # bash get_impacts_2017_signal_0.sh -c
    bash get_impacts_2017_signal_1.sh -c
}
cmb_2018(){
    # bash get_impacts_2018_signal_0.sh -c
    bash get_impacts_2018_signal_1.sh -c
}

cmb(){
    combineTool.py -M T2W -i 2hdma_med400_ps100/xtt_cmb_1_13TeV_20172018.txt -o cmb_workspace_400_20172018.root
    combineTool.py -M Impacts -d 2hdma_med400_ps100/cmb_workspace_400_20172018.root -m 400 --expectSignal=1 --doInitialFit --parallel 10 --rMin -20 --rMax 20 --cminDefaultMinimizerStrategy 0 --robustFit 1 --X-rtd MINIMIZER_analytic
    combineTool.py -M Impacts -d 2hdma_med400_ps100/cmb_workspace_400_20172018.root -m 400 --expectSignal=1 --doFits --parallel 10 --rMin -20 --rMax 20 --robustFit 1 --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_analytic
    combineTool.py -M Impacts -d 2hdma_med400_ps100/cmb_workspace_400_20172018.root -m 400 -o impacts_cmb_m400_20172018_signal1.json --parallel 10
    plotImpacts.py -i impacts_cmb_m400_20172018_signal1.json -o impacts_cmb_m400_20172018_signal1
    cp impacts_cmb_m400_20172018_signal1.pdf $output_dir/2017_till2000GeV/
    cp impacts_cmb_m400_20172018_signal1.pdf $output_dir/2018_till2000GeV/
}

all(){
    cmb_2017
    cmb_2018
    cmb
}

expect_signal="1"
while getopts abcd option
do
    case "${option}"
	in
	a) cmb_2017 ;;
	b) cmb_2018 ;;
	c) cmb ;;
	d) all ;;
	\? ) echo "Usage: bash file.sh  [-c] "
    esac
done

if [ $# -eq 0 ]; then
    echo "No arguments provided
    a) 2017 combined
    b) 2018 combined
    c) get 3 channls combined both years
    d) all 
   "
    echo "Enter option a, b, c, d "
    exit 1
fi
