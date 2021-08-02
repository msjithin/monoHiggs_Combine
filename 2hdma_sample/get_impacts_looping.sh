set -e



etau(){
    cd etau/
    for d in *; do
	if [ -d "$d" ]; then
	    echo "$d"
	    cd $d
	    echo $PWD
	    combineTool.py -M T2W -i ${d}.txt -o et_workspace.root 
	    combineTool.py -M Impacts -d et_workspace.root -m 200 --expectSignal=0 --rMin=-20 --rMax=20 --robustFit 1 --doInitialFit
	    combineTool.py -M Impacts -d et_workspace.root -m 200 --expectSignal=0 --rMin=-20 --rMax=20 --robustFit 1 --doFits
	    combineTool.py -M Impacts -d et_workspace.root -m 200 --expectSignal=0 --rMin=-20 --rMax=20 --robustFit 1 --output impacts_etau.json
	    plotImpacts.py -i impacts_etau.json -o impacts_etau
	fi
	cd ..
	echo $PWD
    done
}





# -t -1





etau
