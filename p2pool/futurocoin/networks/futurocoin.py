import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'cfd2d4c6'.decode('hex')
P2P_PORT = 9009
ADDRESS_VERSION = 36
SCRIPT_ADDRESS_VERSION = 13
RPC_PORT = 9008
RPC_CHECK = defer.inlineCallbacks(lambda futurocoind: defer.returnValue(
            'futurocoinaddress' in (yield futurocoind.rpc_help()) and
            not (yield futurocoind.rpc_getinfo())['testnet']
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('dash_hash').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('dash_hash').getPoWHash(data))
BLOCK_PERIOD = 60 # s
SYMBOL = 'FTO'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'FuturocoinCore') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/FuturocoinCore/') if platform.system() == 'Darwin' else os.path.expanduser('~/.futurocoincore'), 'futurocoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://explorer.futurocoin.com/insight/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://explorer.futurocoin.com/insight/address/'
TX_EXPLORER_URL_PREFIX = 'https://explorer.futurocoin.com/insight/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUST_THRESHOLD = 0.001e8
