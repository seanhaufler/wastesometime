"""
Module with code to setup cluster and test oplog_manager functions.
    
This is the main tester method. All the functions can be called by finaltests.py
"""

import subprocess
import sys
import time
import os
import json

from pymongo import Connection
from pymongo.errors import ConnectionFailure
from os import path

PORTS_ONE = {"PRIMARY":"27117", "SECONDARY":"27118", "SECONDARY2":"27119", 
    "CONFIG":"27220", "MONGOS":"27217"}

PWD = os.getcwd()
SETUP_DIR = path.expanduser(PWD)
DEMO_SERVER_DATA = SETUP_DIR + "/data"
DEMO_SERVER_LOG = SETUP_DIR + "/logs"
MONGOD_KSTR = " --dbpath " + DEMO_SERVER_DATA
MONGOS_KSTR = "mongos --port " + PORTS_ONE["MONGOS"]


def remove_dir(path):
    """Remove supplied directory
    """
    command = ["rm", "-rf", path]
    subprocess.Popen(command).communicate()


def create_dir(path):
    """Create supplied directory
    """
    command = ["mkdir", "-p", path]
    subprocess.Popen(command).communicate()


def killMongoProc(host, port):
    """ Kill given port
    """
    try:
        conn = Connection(host, int(port))
        conn['admin'].command('shutdown',1, force=True)
    except:
        cmd = ["pgrep -f \"" + str(port) + MONGOD_KSTR + "\" | xargs kill -9"]
        executeCommand(cmd)


def killMongosProc():
    """ Kill all mongos proc
    """
    cmd = ["pgrep -f \"" + MONGOS_KSTR + "\" | xargs kill -9"]
    executeCommand(cmd)


def killAllMongoProc(host, ports):
    """Kill any existing mongods
    """
    for port in ports.values():
        killMongoProc(host, port)


def startMongoProc(port, replSetName, data, log):
    """Create the replica set
    """
    CMD = ["mongod --fork --replSet " + replSetName + " --noprealloc --port " + port + " --dbpath "
    + DEMO_SERVER_DATA + data + " --shardsvr --rest --logpath "
    + DEMO_SERVER_LOG + log + " --logappend &"]
    
    executeCommand(CMD)
    checkStarted(int(port))


def executeCommand(command):
    """Wait a little and then execute shell command
    """
    time.sleep(1)
    #return os.system(command)
    subprocess.Popen(command, shell=True)


#========================================= #
#   Helper functions to make sure we move  #
#   on only when we're good and ready      #
#========================================= #


def tryConnection(port):
    """Uses pymongo to try to connect to mongod
    """
    error = 0
    try:
        Connection('localhost', port)
    except Exception:
        error = 1
    return error


def checkStarted(port):
    """Checks if our the mongod has started
    """
    connected = False

    while not connected:
        error = tryConnection(port)
        if error:
            #Check every 1 second
            time.sleep(1)
        else:
            connected = True



#========================================= #
#   Start Cluster						   #
#========================================= #


def start_cluster(sharded=False):
	"""Sets up cluster with 1 shard, replica set with 3 members
	"""
	# Kill all spawned mongods
	#killAllMongoProc('localhost', PORTS_ONE)

	# Kill all spawned mongos
	#killMongosProc()
	
	remove_dir(DEMO_SERVER_LOG)
	remove_dir(DEMO_SERVER_DATA)        

	create_dir(DEMO_SERVER_DATA + "/standalone/journal")
	
	create_dir(DEMO_SERVER_DATA + "/replset1a/journal")
	create_dir(DEMO_SERVER_DATA + "/replset1b/journal")
	create_dir(DEMO_SERVER_DATA + "/replset1c/journal")
	
	create_dir(DEMO_SERVER_DATA + "/shard1a/journal")
	create_dir(DEMO_SERVER_DATA + "/shard1b/journal")
	create_dir(DEMO_SERVER_DATA + "/config1/journal")
	create_dir(DEMO_SERVER_LOG)
		
	# Create the replica set
	startMongoProc(PORTS_ONE["PRIMARY"], "waste-some-time", "/replset1a", "/replset1a.log")
	startMongoProc(PORTS_ONE["SECONDARY"], "waste-some-time", "/replset1b", "/replset1b.log")
	startMongoProc(PORTS_ONE["SECONDARY2"], "waste-some-time", "/replset1c", "/replset1c.log")
	
	# Setup config server
	CMD = ["mongod --oplogSize 500 --fork --configsvr --noprealloc --port " + PORTS_ONE["CONFIG"] + " --dbpath " + DEMO_SERVER_DATA + "/config1 --rest --logpath "
   + DEMO_SERVER_LOG + "/config1.log --logappend &"]
	executeCommand(CMD)
	checkStarted(int(PORTS_ONE["CONFIG"]))

	# Setup the mongos, same mongos for both shards
	CMD = ["mongos --port " + PORTS_ONE["MONGOS"] + " --fork --configdb localhost:" +
	PORTS_ONE["CONFIG"] + " --chunkSize 1  --logpath "  + DEMO_SERVER_LOG + 
	"/mongos1.log --logappend &"]

	executeCommand(CMD)    
	checkStarted(int(PORTS_ONE["MONGOS"]))
		
	# Configure the shards and begin load simulation
	cmd1 = "mongo --port " + PORTS_ONE["PRIMARY"] + " " + SETUP_DIR + "/setup/configReplSet.js"
    	cmd3 = "mongo --port  "+ PORTS_ONE["MONGOS"] + " " + SETUP_DIR + "/setup/configMongos.js"

	subprocess.call(cmd1, shell=True)
	conn = Connection('localhost:' + PORTS_ONE["PRIMARY"])
	sec_conn = Connection('localhost:' + PORTS_ONE["SECONDARY"])
			 
	while conn['admin'].command("isMaster")['ismaster'] is False:
		time.sleep(1)
			 
	while sec_conn['admin'].command("replSetGetStatus")['myState'] != 2:
		time.sleep(1)
		
	subprocess.call(cmd3, shell=True)
	
	
if __name__ == '__main__':
	start_cluster()
