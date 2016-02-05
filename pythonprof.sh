#!/bin/bash
IFS=$'\n'

if [[ $# -ge 1 && -f $1 ]]
then 
	sourcefile=$1

	outfile="out.pdf"
	if [[ $# -ge 2 ]]
	then
		outfile=$2
	fi

	echo "=== Run the python program ======"
	echo "python3 -m cProfile -o python.prof \"$sourcefile\""
	python3 -m cProfile -o python.prof "$sourcefile"
	echo

	echo "=== Format the profiling results ======"
	echo "gprof2dot -fpstats python.prof -o gprof.dot"
	gprof2dot -fpstats python.prof -o gprof.dot
	echo

	echo "=== Create profiling graph ======"
	echo "dot -T pdf gprof.dot -o \"$outfile\""
	dot -T pdf gprof.dot -o "$outfile"

else
	echo "You've got to tell me which file to profile"
fi
