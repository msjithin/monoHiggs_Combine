## Combine limit extraction and impacts for monoHiggs


To setup combine area

```
scram project CMSSW CMSSW_10_2_13   
cd CMSSW_10_2_13/src   
cmsenv   
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit   
#### IMPORTANT: Checkout the recommended tag on the link above  
git clone https://github.com/cms-analysis/CombineHarvester.git CombineHarvester    
scram b  
```


TO clone this repo
```
cd CombineHarvester/CombineTools
git clone https://github.com/msjithin/monoHiggs_combine.git
```  

If the above line doesnt work
```
git init .
git remote add origin https://github.com/msjithin/monoHiggs_combine.git
git pull origin master
```

Datacards are created by .cpp files in bin/

Combine throws errors is histograms have zero bins or negative bins.
Use `fix_binning.py` or `fix_neg_binning.py` to fix this.



For Zprime baryonic  
`bash run_zpb_full.sh `

For 2HDMa do   
`bash run_new2hdma.sh`



Once datacards are created, 
cd to the directory  
then  do ,  
`bash get_limits.sh`


