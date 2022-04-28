set -e

out_directory=~/public_html/limits/sample_v2
get_et(){

    combineTool.py -M T2W -i ../2hdma_med400_ps100/xtt_et_1_13TeV_${year}.txt -o et_workspace_400_${year}.root
    combine -M FitDiagnostics -d ../2hdma_med400_ps100/et_workspace_400_${year}.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --freezeParameters r --setParameters r=0 --customStartingPoint -t -1 --expectSignal=0 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH
    
    # draw post fit 
    # do this to get information on backgrounds
    PostFitShapesFromWorkspace -w ../2hdma_med400_ps100/et_workspace_400_${year}.root -f fitDiagnostics.root:fit_s --postfit --print -d ../2hdma_med400_ps100/xtt_et_1_13TeV_${year}.txt -o postfit_shapes_et_${year}.root -m 400
    
    # now draw postfit plot using output from above
    python draw_POSTPREFIT.py -ch et -y ${year}
    cp _Finalplot_xtt_et_1_*${year}* $out_directory/${year}/
    #python postFitPlot_v3.py -ch et -y ${year}
    #cp _postfit_*et*${year}*  $out_directory/${year}/
}

get_mt(){
    combineTool.py -M T2W -i ../2hdma_med400_ps100/xtt_mt_1_13TeV_${year}.txt -o mt_workspace_400_${year}.root
    combine -M FitDiagnostics -d ../2hdma_med400_ps100/mt_workspace_400_${year}.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --freezeParameters r --setParameters r=0 --customStartingPoint -t -1 --expectSignal=0 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH
    
    # draw post fit 
    # do this to get information on backgrounds
    PostFitShapesFromWorkspace -w ../2hdma_med400_ps100/mt_workspace_400_${year}.root -f fitDiagnostics.root:fit_s --postfit --print -d ../2hdma_med400_ps100/xtt_mt_1_13TeV_${year}.txt -o postfit_shapes_mt_${year}.root -m 400
    
    # now draw postfit plot using output from above
    python draw_POSTPREFIT.py -ch mt -y ${year}
    cp _Finalplot_xtt_mt_1_*${year}* $out_directory/${year}/
    #python postFitPlot_v3.py -ch mt -y ${year}
    #cp _postfit_*mt*${year}*  $out_directory/${year}/

}

get_tt(){
    combineTool.py -M T2W -i ../2hdma_med400_ps100/xtt_tt_1_13TeV_${year}.txt -o tt_workspace_400_${year}.root
    combine -M FitDiagnostics -d ../2hdma_med400_ps100/tt_workspace_400_${year}.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --freezeParameters r --setParameters r=0 --customStartingPoint -t -1 --expectSignal=0 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH
    
    # draw post fit 
    # do this to get information on backgrounds
    PostFitShapesFromWorkspace -w ../2hdma_med400_ps100/tt_workspace_400_${year}.root -f fitDiagnostics.root:fit_s --postfit --print -d ../2hdma_med400_ps100/xtt_tt_1_13TeV_${year}.txt -o postfit_shapes_tt_${year}.root -m 400
    
    # now draw postfit plot using output from above
    python draw_POSTPREFIT.py -ch tt -y ${year}
    cp _Finalplot_xtt_tt_1_*${year}* $out_directory/${year}/
    #python postFitPlot_v3.py -ch tt -y ${year}
    #cp _postfit_*tt*${year}*  $out_directory/${year}/
}
get_cmb(){
    combineTool.py -M T2W -i ../2hdma_med400_ps100/xtt_cmb_1_13TeV_${year}.txt -o cmb_workspace_400_${year}.root
    combine -M FitDiagnostics -d ../2hdma_med400_ps100/cmb_workspace_400_${year}.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --freezeParameters r --setParameters r=0 --customStartingPoint -t -1 --expectSignal=0 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH
    
    # draw post fit 
    # do this to get information on backgrounds
    PostFitShapesFromWorkspace -w ../2hdma_med400_ps100/cmb_workspace_400_${year}.root -f fitDiagnostics.root:fit_s --postfit --print -d ../2hdma_med400_ps100/xtt_cmb_1_13TeV_${year}.txt -o postfit_shapes_cmb_${year}.root -m 400
    
    # now draw postfit plot using output from above
    python draw_POSTPREFIT.py -ch cmb -y ${year}
    cp _Finalplot_xtt_cmb_1_*${year}* $out_directory/${year}/
    # python postFitPlot_v3.py -ch cmb -y ${year}
    # cp _postfit_*cmb*  $out_directory/${year}/

}


year="2017" #default can take 2017 or 2018 
while getopts emtcy: option
do
    case "${option}"
    in
        e) get_et ;;
	m) get_mt ;;
	t) get_tt ;;
	c) get_cmb ;;
	y) year=${OPTARG} ;;
    esac
done

echo "year = $year "
if [ $# -eq 0 ]; then
    echo "No arguments provided"
    echo "Please choose one of the options: This copies blinded region plots to public_html
    e) get etau ;;
    m) get mutau ;;
    t) get tautau ;;
    c) combined ;;
    y) year : 2017 or 2018
   "
    echo "Enter option e, m, t , c and/or y"
    exit 1
fi
