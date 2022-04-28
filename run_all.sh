set -e

for ch in 'tt' #'et' 'mt' 'tt'
do
    for yr in '2017' '2018'
    do	
	echo "running --year ${yr} --ch ${ch}  "
	MonoHiggs_V3 --med 200 --ps 100 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 200 --ps 150 --year ${yr} --ch ${ch}

	MonoHiggs_V3 --med 300 --ps 100 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 300 --ps 150 --year ${yr} --ch ${ch}

	MonoHiggs_V3 --med 400 --ps 100 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 400 --ps 150 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 400 --ps 200 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 400 --ps 250 --year ${yr} --ch ${ch}

	MonoHiggs_V3 --med 500 --ps 150 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 500 --ps 200 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 500 --ps 250 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 500 --ps 300 --year ${yr} --ch ${ch}

	MonoHiggs_V3 --med 600 --ps 100 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 600 --ps 150 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 600 --ps 200 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 600 --ps 250 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 600 --ps 300 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 600 --ps 350 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 600 --ps 400 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 600 --ps 500 --year ${yr} --ch ${ch}

	MonoHiggs_V3 --med 700 --ps 250 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 700 --ps 300 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 700 --ps 350 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 700 --ps 400 --year ${yr} --ch ${ch}
	
	MonoHiggs_V3 --med 800 --ps 250 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 800 --ps 300 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 800 --ps 350 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 800 --ps 500 --year ${yr} --ch ${ch}
	
	MonoHiggs_V3 --med 900 --ps 300 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 900 --ps 350 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 900 --ps 400 --year ${yr} --ch ${ch}
	MonoHiggs_V3 --med 900 --ps 500 --year ${yr} --ch ${ch}

    done
done

#MonoHiggs_V3 --med 400 --ps 100 --year 2017 --ch tt
