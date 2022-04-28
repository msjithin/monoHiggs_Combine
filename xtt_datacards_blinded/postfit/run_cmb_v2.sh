set -e


cmb_2017(){
    combineTool.py -M T2W -i ../2hdma_med400_ps100/xtt_cmb_1_13TeV_2017.txt -o cmb_workspace_400_2017.root
    
    combine -M FitDiagnostics -d ../2hdma_med400_ps100/cmb_workspace_400_2017.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --expectSignal=1
    
    PostFitShapesFromWorkspace -w ../2hdma_med400_ps100/cmb_workspace_400_2017.root -f fitDiagnostics.root:fit_s --postfit --print -d ../2hdma_med400_ps100/xtt_cmb_1_13TeV_2017.txt -o postfit_shapes_cmb_2017.root -m 400
    
    #python draw_POSTPREFIT.py 
    #cp _Finalplot_combined_* ~/public_html/limits/sample_new/sample/combined_fit/
    
    # cp _Finalplot_xtt_et_1_*${year}* ~/public_html/limits/sample_new/sample/${year}_till2000GeV/
    #python postFitPlot_v3_cmb.py
    #cp _postfit_combined_* ~/public_html/limits/sample_new/sample/combined_fit/
}


cmb_2018(){
    combineTool.py -M T2W -i ../2hdma_med400_ps100/xtt_cmb_1_13TeV_2018.txt -o cmb_workspace_400_2018.root
    
    combine -M FitDiagnostics -d ../2hdma_med400_ps100/cmb_workspace_400_2018.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --expectSignal=1
    
    PostFitShapesFromWorkspace -w ../2hdma_med400_ps100/cmb_workspace_400_2018.root -f fitDiagnostics.root:fit_s --postfit --print -d ../2hdma_med400_ps100/xtt_cmb_1_13TeV_2018.txt -o postfit_shapes_cmb_2018.root -m 400
    
    #python draw_POSTPREFIT.py 
    #cp _Finalplot_combined_* ~/public_html/limits/sample_new/sample/combined_fit/
    
    # cp _Finalplot_xtt_et_1_*${year}* ~/public_html/limits/sample_new/sample/${year}_till2000GeV/
    #python postFitPlot_v3_cmb.py
    #cp _postfit_combined_* ~/public_html/limits/sample_new/sample/combined_fit/
}

cmb_20172018(){
    combineTool.py -M T2W -i ../2hdma_med400_ps100/xtt_cmb_1_13TeV_20172018.txt -o cmb_workspace_400_20172018.root
    
    combine -M FitDiagnostics -d ../2hdma_med400_ps100/cmb_workspace_400_20172018.root -m 400 --saveShapes --saveWithUncertainties --robustFit 1 --rMin -20 --rMax 20 --expectSignal=1
    
    PostFitShapesFromWorkspace -w ../2hdma_med400_ps100/cmb_workspace_400_20172018.root -f fitDiagnostics.root:fit_s --postfit --print -d ../2hdma_med400_ps100/xtt_cmb_1_13TeV_20172018.txt -o postfit_shapes_cmb_20172018.root -m 400
    
    #python draw_POSTPREFIT.py 
    #cp _Finalplot_combined_* ~/public_html/limits/sample_new/sample/combined_fit/
    
    # cp _Finalplot_xtt_et_1_*${year}* ~/public_html/limits/sample_new/sample/${year}_till2000GeV/
    #python postFitPlot_v3_cmb.py
    #cp _postfit_combined_* ~/public_html/limits/sample_new/sample/combined_fit/
}

plot(){
    python postFitPlot_v3_cmb.py
    cp _postfit_combined_* $output_dir/combined_fit/
}

#"$@"
cmb_2017
cmb_2018
cmb_20172018
plot
