

y_2017(){
    
    cp /afs/hep.wisc.edu/home/ms/monoHiggs_2018_wDnn/CMSSW_10_2_18/src/analysis/2017_post_analyzer/etau_blinded/plotting_script/data_full/etau.root bin/aux/2017/
    cp /afs/hep.wisc.edu/home/ms/monoHiggs_2018_wDnn/CMSSW_10_2_18/src/analysis/2017_post_analyzer/mutau_blinded/plotting_script/data_full/mutau.root bin/aux/2017/
    cp /afs/hep.wisc.edu/home/ms/monoHiggs_2018_wDnn/CMSSW_10_2_18/src/analysis/2017_post_analyzer/tautau_blinded/plotting_script/data_full/tautau.root bin/aux/2017/
}

y_2018(){
    
    cp /afs/hep.wisc.edu/home/ms/monoHiggs_2018_wDnn/CMSSW_10_2_18/src/analysis/2018_post_analyzer/etau_blinded/plotting_script/data_full/etau.root bin/aux/2018/
    cp /afs/hep.wisc.edu/home/ms/monoHiggs_2018_wDnn/CMSSW_10_2_18/src/analysis/2018_post_analyzer/mutau_blinded/plotting_script/data_full/mutau.root bin/aux/2018/
    cp /afs/hep.wisc.edu/home/ms/monoHiggs_2018_wDnn/CMSSW_10_2_18/src/analysis/2018_post_analyzer/tautau_blinded/plotting_script/data_full/tautau.root bin/aux/2018/
}


y_2017_0to200(){
    
    cp /afs/hep.wisc.edu/home/ms/monoHiggs_2018_wDnn/CMSSW_10_2_18/src/analysis/2017_post_analyzer/etau_blinded/plotting_script/data_5th/etau_tmass200.root bin/aux/2017/
    cp /afs/hep.wisc.edu/home/ms/monoHiggs_2018_wDnn/CMSSW_10_2_18/src/analysis/2017_post_analyzer/mutau_blinded/plotting_script/data_5th/mutau_tmass200.root bin/aux/2017/
    cp /afs/hep.wisc.edu/home/ms/monoHiggs_2018_wDnn/CMSSW_10_2_18/src/analysis/2017_post_analyzer/tautau_blinded/plotting_script/data_5th/tautau_tmass200.root bin/aux/2017/
}

y_2018_0to200(){
    
    cp /afs/hep.wisc.edu/home/ms/monoHiggs_2018_wDnn/CMSSW_10_2_18/src/analysis/2018_post_analyzer/etau_blinded/plotting_script/data_5th/etau_tmass200.root bin/aux/2018/
    cp /afs/hep.wisc.edu/home/ms/monoHiggs_2018_wDnn/CMSSW_10_2_18/src/analysis/2018_post_analyzer/mutau_blinded/plotting_script/data_5th/mutau_tmass200.root bin/aux/2018/
    cp /afs/hep.wisc.edu/home/ms/monoHiggs_2018_wDnn/CMSSW_10_2_18/src/analysis/2018_post_analyzer/tautau_blinded/plotting_script/data_5th/tautau_tmass200.root bin/aux/2018/
}



all(){
     echo "copying files with 0to2000 full range"
    y_2017
    y_2018
}

all_short(){
    echo "copying files with 0to200"
    y_2017_0to200
    y_2018_0to200
}
echo "bash get_files.sh all , all_short , y_2017, y_2017_0to200"
"$@"
