#!/bin/bash

ADDRESS_FROM="ikeuchi@hiroaki.com"
ADDRESS_TO="rationaltrader2018@gmail.com"

DATETIME=`date "+%H:%M on %Y/%m/%d "`
DAYOFWEEK=`date "+%w"`
echo $DATETIME 
python get_fx_rates.py > tmp.txt
if [ $DAYOFWEEK != 0 ] ; then
cat tmp.txt | mail -r "FX Sender <$ADDRESS_FROM>" -s "FX Rates at $DATETIME" $ADDRESS_TO
echo "Mail sent"
fi
rm tmp.txt
