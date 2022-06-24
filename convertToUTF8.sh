for F in `find hashes -type f`
do 
	echo "Translating $F"
	iconv -f iso-8859-1 -t utf-8//transl $F > ${F}tr
	mv ${F}tr $F
done
