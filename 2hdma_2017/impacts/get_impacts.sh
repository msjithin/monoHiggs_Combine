set -e


etau(){
    combineTool.py -M T2W -i etau_MH3_200_MH4_100.txt -o et_workspace.root
    combineTool.py -M Impacts -d et_workspace.root -m 200 -t -1 --expectSignal=0 --rMin=-20 --rMax=20 --robustFit 1 --doInitialFit
    combineTool.py -M Impacts -d et_workspace.root -m 200 -t -1 --expectSignal=0 --rMin=-20 --rMax=20 --robustFit 1 --doFits
    combineTool.py -M Impacts -d et_workspace.root -m 200 -t -1 --expectSignal=0 --rMin=-20 --rMax=20 --robustFit 1 --output impacts_etau.json
    plotImpacts.py -i impacts_etau.json -o impacts_etau
}

mutau(){
    combineTool.py -M T2W -i mutau_MH3_200_MH4_100.txt -o mt_workspace.root
    combineTool.py -M Impacts -d mt_workspace.root -m 200 -t -1 --expectSignal=0 --rMin=-20 --rMax=20 --robustFit 1 --doInitialFit
    combineTool.py -M Impacts -d mt_workspace.root -m 200 -t -1 --expectSignal=0 --rMin=-20 --rMax=20 --robustFit 1 --doFits
    combineTool.py -M Impacts -d mt_workspace.root -m 200 -t -1 --expectSignal=0 --rMin=-20 --rMax=20 --robustFit 1 --output impacts_mutau.json
    plotImpacts.py -i impacts_mutau.json -o impacts_mutau
}


"$@"
