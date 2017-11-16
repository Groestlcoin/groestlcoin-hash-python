from distutils.core import setup, Extension

groestlcoin_hash_module = Extension('groestlcoin_hash', sources = ['groestlcoinmodule.c', 'groestl.c'])

setup (name = 'groestlcoin_hash',
       version = '1.0.1',
       description = 'Groestlcoin hash algorithm.',
       maintainer = 'Kefkius',
       maintainer_email = 'kefkius@mail.com',
       url = 'https://github.com/Groestlcoin/groestlcoin-hash-python',
       keywords = ['groestlcoin', 'grs'],
       ext_modules = [groestlcoin_hash_module])
