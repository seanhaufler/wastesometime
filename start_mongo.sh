datapath="$PWD/data" 
logpath="$PWD/mongo.log" 

mongod --fork --port 27017 --dbpath $datapath --logpath $logpath --logappend &

