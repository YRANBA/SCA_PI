#!/bin/bash

#initial value of script is 2
car=2

while [ $car -le 20 ]
	do
		echo $car
	((car = $car +3))
	
	done
echo "All done"


