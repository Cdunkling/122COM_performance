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

	echo "=== Compile the C++ program ======"
	echo "g++ --std=c++11 -pg \"$sourcefile\" -o test"
	g++ --std=c++11 -pg "$sourcefile" -o test
	echo

	if [[ $? -ne 0 ]]
	then
		return
	fi

	echo "=== Run the C++ program ======"
	echo "./test"
	./test
	echo

	echo "=== Format the profiling results ======"
	echo "gprof test | gprof2dot -n0 -e0 -o gprof.dot"
	gprof test | gprof2dot -o gprof.dot
	echo

	echo "=== Create profiling graph ======"
	echo "dot -T pdf gprof.dot -o \"$outfile\""
	dot -T pdf gprof.dot -o "$outfile"

else
	echo "You've got to tell me which file to profile"
fi
