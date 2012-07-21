datapath="$PWD/data" 
logpath="$PWD/mongo.log" 

mongod --fork --port 27117 --dbpath $datapath --logpath $logpath --logappend &

