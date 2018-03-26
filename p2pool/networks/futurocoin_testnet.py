from p2pool.futurocoin import networks

PARENT = networks.nets['futurocoin_testnet']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 24*60*60//20 # shares
REAL_CHAIN_LENGTH = 24*60*60//20 # shares
TARGET_LOOKBEHIND = 100 # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD = 10 # blocks
IDENTIFIER = '4de3f39803740800'.decode('hex')
PREFIX = '5b40ba3121da2800'.decode('hex')
COINBASEEXT = '00'.decode('hex')
P2P_PORT = 18999
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 17903
BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = ''
VERSION_CHECK = lambda v: True
