DIR1="/home/leet/taco/"
DIR2="/home/leet/bell/"
LOGS="/home/leet/cron.rsync-log"

if [ -d "$DIR1" ] && [ -d "$DIR2" ]; then
  rsync -c -r -v $DIR1 $DIR2 >> $LOGS
else
	echo -e "\n Destination or source dir, dir is non existent \n Source: $DIR1 \n Dest: $DIR2" >> $LOGS
	echo -e "Failed Check logs at $LOGS"
fi