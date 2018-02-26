#!/bin/sh
# this script has been written by Eddy 
#
#		recognize_pdf - распознает pdf-файлы при помощи cuneiform
# зависит от cuneiform и pdftoppm
#
# Создан 25-го Апрель 2012 года в 18:12
#

if [ $# == 0 ]; then
	echo -e "\nUsage: $(basename $0) filename.pdf,\n\tneeds some space for temporary ppm-files,\n\tsaves results to file filename.txt\n"
	exit -1
fi

NAME=$(basename $1)

# 1. Преобразуем pdf в ppm'ы
echo -e "\nConvert pdf to a lot of ppms"
# pdftoppm $1 $NAME

gs -o $NAME-%d.png -sDEVICE=png256 \
 -r300 -dPrinted -dUseCropBox -dTextAlphaBits=4\
 -dGraphicsAlphaBits=4 $1

# 2. Распознаем каждый рисунок
echo -e "\nRecognize every file\n"
for PPM in $(ls -1 ${NAME}-*.png)
do
	echo -n "$PPM .. "
	cuneiform -l ruseng -f smarttext ${PPM} -o ${PPM}.txt
	echo "done!"
done

# 3. Собираем все вместе
rm -f ${NAME}.txt
cat $(ls -1 ${NAME}-*txt) > ${NAME}.txt

# 4. Подчищаем мусор
echo -n "Ready, cleaning ..."

rm -f ${NAME}-*.txt ${NAME}-*.png

echo "Done!"