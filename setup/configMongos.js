//(C) Copyright 2012, 10gen

//=========================================#
//         Configure Mongos                #
//=========================================#

db._adminCommand({addShard: "waste-some-time/localhost:27117"});
//printjson(db._adminCommand({enablesharding: "waste-some-time/localhost:27117/sources"}));
