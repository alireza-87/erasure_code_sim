KB = 1024  # bytes
MB = 1024 ** 2  # bytes
GB = 1024 ** 3  # bytes
TB = 1024 ** 4  # bytes
MINUTE = 60
HOUR = 60 * 60  # seconds
DAY = 24 * HOUR  # seconds
YEAR = 365 * DAY
### SYSTEM PARAMETERS
N = 10  # number of servers storing data
K = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # number of blocks needed to recover data
# parameters about the node backing up the data
# parameters about the node backing up the data
NODE_LIFETIME = 30 * DAY  # average time before node crashes and loses data
NODE_UPTIME = 8 * HOUR  # average time spent online by the node
NODE_DOWNTIME = 16 * HOUR  # average time spent offline
#REAL DATA
#DATA_SIZE = [10*GB, 100 * GB, 200 * GB, 400 * GB]  # amount of data to backup 100*GB,250*GB
#UPLOAD_SPEED = [100 * KB, 2 * MB]  # node's speed, per second
#DOWNLOAD_SPEED = [200 * KB, 4 * MB]  # per second
#UPLOAD_SPEED_LABEL = ["100*KB", "2*MB"]  # node's speed LABEL, per second
#DOWNLOAD_SPEED_LABEL = ["200*KB", "4*MB"]  # per second

# Test
DATA_SIZE = [5*GB, 10 * GB]  # amount of data to backup 100*GB,250*GB
UPLOAD_SPEED = [100 * KB, 2 * MB]  # node's speed, per second
DOWNLOAD_SPEED = [200 * KB, 4 * MB]  # per second
UPLOAD_SPEED_LABEL = ["100*KB", "2*MB"]  # node's speed LABEL, per second
DOWNLOAD_SPEED_LABEL = ["200*KB", "4*MB"]  # per second

# parameters as before, for the server
SERVER_LIFETIME = 1 * YEAR
SERVER_UPTIME = 30 * DAY
SERVER_DOWNTIME = 2 * HOUR

# length of the simulation
MAXT = 5 * YEAR
NUMBER_OF_ITERATION = 5
B = 1  # number of Block in a server
