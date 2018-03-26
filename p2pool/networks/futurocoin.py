from p2pool.futurocoin import networks

PARENT = networks.nets['futurocoin']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 24*60*60//20 # shares
REAL_CHAIN_LENGTH = 24*60*60//20 # shares
TARGET_LOOKBEHIND = 100 # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD = 10 # blocks
IDENTIFIER = '2215722753d31000'.decode('hex')
PREFIX = '68f397b220d20c00'.decode('hex')
COINBASEEXT = '00'.decode('hex')
P2P_PORT = 8999
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 7903
BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-futurocoin'
VERSION_CHECK = lambda v: v >= 120100
