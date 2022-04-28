



et_2017(){
    
    combine -M GenerateOnly -d 2hdma_med400_ps100/et_workspace_400_2017.root --saveToys --rMin -20 --rMax 20 --expectSignal=1
    combineTool.py -M FastScan -w 2hdma_med400_ps100/et_workspace_400_2017.root:w -d higgsCombineTest.GenerateOnly.mH120.123456.root:toys/toy_asimov -o et_2017_nll
    cp et_2017_nll.pdf ~/public_html/limits/sample_v2/2017_till2000GeV/
    }

mt_2017(){
    
    combine -M GenerateOnly -d 2hdma_med400_ps100/mt_workspace_400_2017.root --saveToys --rMin -20 --rMax 20 --expectSignal=1
    combineTool.py -M FastScan -w 2hdma_med400_ps100/mt_workspace_400_2017.root:w -d higgsCombineTest.GenerateOnly.mH120.123456.root:toys/toy_asimov -o mt_2017_nll
    cp mt_2017_nll.pdf ~/public_html/limits/sample_v2/2017_till2000GeV/
    }

tt_2017(){
    
    combine -M GenerateOnly -d 2hdma_med400_ps100/tt_workspace_400_2017.root --saveToys --rMin -20 --rMax 20 --expectSignal=1
    combineTool.py -M FastScan -w 2hdma_med400_ps100/tt_workspace_400_2017.root:w -d higgsCombineTest.GenerateOnly.mH120.123456.root:toys/toy_asimov -o tt_2017_nll
    cp tt_2017_nll.pdf ~/public_html/limits/sample_v2/2017_till2000GeV/
    }




# combineTool.py -M T2W -i 2hdma_med400_ps100/xtt_mt_1_13TeV_2017.txt -o mt_workspace_400_2017.root
# combine -M FitDiagnostics -d 2hdma_med400_ps100/mt_workspace_400_2017.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --expectSignal=1 
# python diffNuisances.py fitDiagnostics.root --all --abs -g mutau_plotdiff_2017.root
# cp *mutau*2017.png ~/public_html/limits/sample_v2/2017_till2000GeV/


echo "bash debug.sh et_2017 , mt_2017"
"$@"
