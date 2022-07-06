set -e

for ch in 'et'
do
    for yr in '2017' '2018'
    do	
	echo "running --year ${yr} --ch ${ch}  "
	MonoHiggs_ZpB --med 1000 --ps 100 --year ${yr} --chn all
	MonoHiggs_ZpB --med 1000 --ps 1 --year ${yr} --chn all
	MonoHiggs_ZpB --med 1000 --ps 200 --year ${yr} --chn all
	MonoHiggs_ZpB --med 1000 --ps 400 --year ${yr} --chn all
	MonoHiggs_ZpB --med 1000 --ps 600 --year ${yr} --chn all
	MonoHiggs_ZpB --med 1000 --ps 800 --year ${yr} --chn all
	MonoHiggs_ZpB --med 100 --ps 1 --year ${yr} --chn all
	MonoHiggs_ZpB --med 100 --ps 50 --year ${yr} --chn all
	MonoHiggs_ZpB --med 1500 --ps 100 --year ${yr} --chn all
	MonoHiggs_ZpB --med 1500 --ps 1 --year ${yr} --chn all
	MonoHiggs_ZpB --med 1500 --ps 200 --year ${yr} --chn all
	MonoHiggs_ZpB --med 1500 --ps 400 --year ${yr} --chn all
	MonoHiggs_ZpB --med 1500 --ps 600 --year ${yr} --chn all
	MonoHiggs_ZpB --med 1500 --ps 800 --year ${yr} --chn all
	MonoHiggs_ZpB --med 2000 --ps 100 --year ${yr} --chn all
	MonoHiggs_ZpB --med 2000 --ps 1 --year ${yr} --chn all
	MonoHiggs_ZpB --med 2000 --ps 200 --year ${yr} --chn all
	MonoHiggs_ZpB --med 2000 --ps 400 --year ${yr} --chn all
	MonoHiggs_ZpB --med 2000 --ps 600 --year ${yr} --chn all
	MonoHiggs_ZpB --med 2000 --ps 800 --year ${yr} --chn all
	MonoHiggs_ZpB --med 200 --ps 100 --year ${yr} --chn all
	MonoHiggs_ZpB --med 200 --ps 150 --year ${yr} --chn all
	MonoHiggs_ZpB --med 200 --ps 1 --year ${yr} --chn all
	MonoHiggs_ZpB --med 200 --ps 50 --year ${yr} --chn all
	MonoHiggs_ZpB --med 2500 --ps 100 --year ${yr} --chn all
	MonoHiggs_ZpB --med 2500 --ps 1 --year ${yr} --chn all
	MonoHiggs_ZpB --med 2500 --ps 200 --year ${yr} --chn all
	MonoHiggs_ZpB --med 2500 --ps 400 --year ${yr} --chn all
	MonoHiggs_ZpB --med 2500 --ps 600 --year ${yr} --chn all
	MonoHiggs_ZpB --med 2500 --ps 800 --year ${yr} --chn all
	MonoHiggs_ZpB --med 3000 --ps 100 --year ${yr} --chn all
	MonoHiggs_ZpB --med 3000 --ps 1 --year ${yr} --chn all
	MonoHiggs_ZpB --med 3000 --ps 200 --year ${yr} --chn all
	MonoHiggs_ZpB --med 300 --ps 150 --year ${yr} --chn all
	MonoHiggs_ZpB --med 3500 --ps 100 --year ${yr} --chn all
	MonoHiggs_ZpB --med 3500 --ps 1 --year ${yr} --chn all
	MonoHiggs_ZpB --med 350 --ps 50 --year ${yr} --chn all
	MonoHiggs_ZpB --med 500 --ps 100 --year ${yr} --chn all
	MonoHiggs_ZpB --med 500 --ps 1 --year ${yr} --chn all
	MonoHiggs_ZpB --med 500 --ps 200 --year ${yr} --chn all
	MonoHiggs_ZpB --med 500 --ps 400 --year ${yr} --chn all
	MonoHiggs_ZpB --med 650 --ps 50 --year ${yr} --chn all
	MonoHiggs_ZpB --med 800 --ps 50 --year ${yr} --chn all
    done
done
