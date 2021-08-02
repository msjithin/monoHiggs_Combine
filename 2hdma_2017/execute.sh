set -e
# From 
# https://cms-analysis.github.io/CombineHarvester/limits.html
#bash get_files.sh
execute_tt(){
    combineTool.py -M T2W -i tautau/*/* -o workspace.root
    combineTool.py -M AsymptoticLimits -d tautau/*/workspace.root --there -n .limit_tautau
    combineTool.py -M CollectLimits tautau/*/*.limit_tautau.* --use-dirs -o limits/limits_tautau.json
    python gather_limits.py -ch tautau
}
execute_et(){
    combineTool.py -M T2W -i etau/*/* -o workspace.root
    combineTool.py -M AsymptoticLimits -d etau/*/workspace.root --there -n .limit_etau
    combineTool.py -M CollectLimits etau/*/*.limit_etau.* --use-dirs -o limits/limits_etau.json
    python gather_limits.py -ch etau
}
execute_mt(){
    combineTool.py -M T2W -i mutau/*/* -o workspace.root
    combineTool.py -M AsymptoticLimits -d mutau/*/workspace.root --there -n .limit_mutau
    combineTool.py -M CollectLimits mutau/*/*.limit_mutau.* --use-dirs -o limits/limits_mutau.json
    python gather_limits.py -ch mutau
}
execute_cmb(){
    combineTool.py -M T2W -i cmb/*/* -o workspace.root
    combineTool.py -M AsymptoticLimits -d cmb/*/workspace.root --there -n .limit_cmb
    combineTool.py -M CollectLimits cmb/*/*.limit_cmb.* --use-dirs -o limits/limits_cmb.json
    python gather_limits.py -ch cmb
}
execute_sample(){
    echo "Which channel do you want to test? Enter etau , mutau, tautau or cmb"
    read chName
    combineTool.py -M T2W -i ${chName}/MH3_200*/* -o workspace.root
    combineTool.py -M AsymptoticLimits -d  ${chName}/MH3_200*/workspace.root --there -n .limit_${chName}  --expectSignal=0
    combineTool.py -M CollectLimits  ${chName}/MH3_200*/*.limit_${chName}.* --use-dirs -o limits/limits_${chName}.json

}
cleanup(){
    bash cleanup.sh
}
plotscan(){
    python make_1Dplot.py
    cd scan1D
    bash runall.sh
    cd ..
}
all(){
    cleanup
    execute_et
    execute_mt
    execute_tt
    #execute_cmb
    plotscan
}


while getopts 123456at option
do
    case "${option}"
    in
        1) execute_et  ;;
        2) execute_mt ;;
        3) execute_tt ;;
	4) execute_cmb ;;
	5) cleanup ;;
	6) plotscan ;;
	a) all ;;
	t) execute_sample ;;
    esac
done

if [ $# -eq 0 ]; then
    echo "No arguments provided"
    echo "bash execute.sh -1"
    echo "Please choose one of the options:
        1) et  ;; --- to run etau only
        2) mt ;; --- to run etau only
        3) tt ;;--- to run etau only
	4) cmb ;;--- to run etau only
	5) cleanup ;; --- cleanup the area and create datacards for each channel again
	6) plotscan ;; --- to make 1D scans
	a) all ;;  --- to run everything
        t) execute_sample ;;  --- to run test samples
   "
fi
