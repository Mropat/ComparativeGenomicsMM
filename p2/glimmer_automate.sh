mkdir out
for f in *.fa; do tigr-glimmer long-orfs -n -t 1.15 $f out/$f.long-orf-coords; done
for f in *.fa; do tigr-glimmer extract -t $f out/$f.long-orf-coords > out/$f.longorf; done
for f in *.fa; do tigr-glimmer build-icm -r $f < out/$f.longorf; done
for f in *.fa; do tigr-glimmer glimmer3 -o50 -g110 -t30 $f out/$f.icm out/$f.glimmer; done



