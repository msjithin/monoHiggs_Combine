#!bin/bash
#example commands to run impact plots, any signal directory is ok. 



#     ......................  original_out ..................
#XTT_CR --mass="400" --signalMass="1200"  control_region=1
#cd output/xtt_cards
# combineTool.py -M T2W -i MH3_300_MH4_150.txt -o workspace.root  --parallel 4
# combineTool.py -M Impacts -d workspace.root -m 300 --doInitialFit --rMin -5 --rMax 5 --robustFit 1 --expectSignal=0 --parallel 24
# combineTool.py -M Impacts -d workspace.root -m 300 --robustFit 1 --rMin -5 --rMax 5  --doFits --expectSignal=0 --minimizerAlgoForMinos Minuit2,Migrad --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --parallel 24
# combineTool.py -M Impacts -d workspace.root -m 300 -o impacts.json
# plotImpacts.py -i impacts.json -o impacts




#     ......................  new_out ..................
combineTool.py -M T2W -i MH3_300_MH4_150.txt -o MH3_300_workspace.root  --parallel 4
combineTool.py -M Impacts -d MH3_300_workspace.root -m 300 --doInitialFit --rMin -20 --rMax 20 --robustFit 1 --expectSignal=0 --parallel 24
combineTool.py -M Impacts -d MH3_300_workspace.root -m 300 --robustFit 1 --rMin -20 --rMax 20  --doFits --expectSignal=0 --cminDefaultMinimizerType=Minuit2 --cminDefaultMinimizerAlgo=Migrad --X-rtd FITTER_NEW_CROSSING_ALGO --parallel 24
combineTool.py -M Impacts -d MH3_300_workspace.root -m 300 -o impacts_MH3_300.json
plotImpacts.py -i impacts_MH3_300.json -o impacts_MH3_300



combineTool.py -M T2W -i MH3_200_MH4_100.txt -o MH3_200_workspace.root  --parallel 4
combineTool.py -M Impacts -d MH3_200_workspace.root -m 200 --doInitialFit --rMin -20 --rMax 20 --robustFit 1 --expectSignal=0 --parallel 24
combineTool.py -M Impacts -d MH3_200_workspace.root -m 200 --robustFit 1 --rMin -20 --rMax 20  --doFits --expectSignal=0 --cminDefaultMinimizerType=Minuit2 --cminDefaultMinimizerAlgo=Migrad --X-rtd FITTER_NEW_CROSSING_ALGO --parallel 24
combineTool.py -M Impacts -d MH3_200_workspace.root -m 200 -o impacts_MH3_200.json
plotImpacts.py -i impacts_MH3_200.json -o impacts_MH3_200
