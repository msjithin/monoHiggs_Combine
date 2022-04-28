set -e

out_directory=~/public_html/limits/sample_v2
signal_array=("2hdma_med200_ps100" "2hdma_med200_ps150" "2hdma_med300_ps100" "2hdma_med300_ps150" "2hdma_med400_ps100" "2hdma_med500_ps150" "2hdma_med600_ps150" "2hdma_med600_ps200" "2hdma_med600_ps250" "2hdma_med600_ps300" "2hdma_med600_ps350" "2hdma_med600_ps400" "2hdma_med600_ps500" "2hdma_med700_ps250" "2hdma_med700_ps300" "2hdma_med700_ps350" "2hdma_med700_ps400" "2hdma_med800_ps250" "2hdma_med800_ps300" "2hdma_med800_ps350" "2hdma_med800_ps500" "2hdma_med900_ps300" "2hdma_med900_ps350" "2hdma_med900_ps400" "2hdma_med900_ps500")

get_et(){
    
    for i in "${signal_array[@]}"         
    do 
	echo $i
	
        combineTool.py -M T2W -i ../${i}/xtt_et_1_13TeV_${year}.txt -o et_workspace_${i}_${year}.root
	combine -M FitDiagnostics -d ../${i}/et_workspace_${i}_${year}.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --freezeParameters r --setParameters r=0 --customStartingPoint -t -1 --expectSignal=0 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH
	
	PostFitShapesFromWorkspace -w ../${i}/et_workspace_${i}_${year}.root -f fitDiagnostics.root:fit_s --postfit --print -d ../${i}/xtt_et_1_13TeV_${year}.txt -o postfit_shapes_et_${i}_${year}.root -m 400
    done
}
get_mt(){
    
    for i in "${signal_array[@]}"         
    do 
	echo $i
	
        combineTool.py -M T2W -i ../${i}/xtt_mt_1_13TeV_${year}.txt -o mt_workspace_${i}_${year}.root
	combine -M FitDiagnostics -d ../${i}/mt_workspace_${i}_${year}.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --freezeParameters r --setParameters r=0 --customStartingPoint -t -1 --expectSignal=0 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH
	
	PostFitShapesFromWorkspace -w ../${i}/mt_workspace_${i}_${year}.root -f fitDiagnostics.root:fit_s --postfit --print -d ../${i}/xtt_mt_1_13TeV_${year}.txt -o postfit_shapes_mt_${i}_${year}.root -m 400
    done
}
get_tt(){
    
    for i in "${signal_array[@]}"         
    do 
	echo "________________________ next _________________________"
	echo $i	
	#rm fitDiagnostics.root 
        combineTool.py -M T2W -i ../${i}/xtt_tt_1_13TeV_${year}.txt -o tt_workspace_${i}_${year}.root
	combine -M FitDiagnostics -d ../${i}/tt_workspace_${i}_${year}.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --freezeParameters r --setParameters r=0 --customStartingPoint -t -1 --expectSignal=0 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH
	
	PostFitShapesFromWorkspace -w ../${i}/tt_workspace_${i}_${year}.root -f fitDiagnostics.root:fit_s --postfit --print -d ../${i}/xtt_tt_1_13TeV_${year}.txt -o postfit_shapes_tt_${i}_${year}.root -m 400
    done
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
