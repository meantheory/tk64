import string

from tk64 import Token
from tk64 import HEX_ALPHABET
from tk64 import BIN_ALPHABET

ABC_ALPHABET = 'abc'
TST_ALPHABET = string.ascii_uppercase + \
	string.ascii_lowercase + \
	string.digits + \
	'-_'

def test_hex_8():
	tk = Token(HEX_ALPHABET)
	assert tk.encode(8) == '8'
	assert tk.decode('8') == 8

def test_hex_neg1():
	tk = Token(HEX_ALPHABET)
	assert tk.encode(-1) == 'FFFFFFFFFFFFFFFF'
	assert tk.decode('FFFFFFFFFFFFFFFF') == -1

def test_hex_1715004():
	tk = Token(HEX_ALPHABET)
	assert tk.encode(1715004) == '1A2B3C'
	assert tk.decode('1A2B3C') == 1715004	

def test_hex_int_max():
	tk = Token(HEX_ALPHABET)
	assert tk.encode(9223372036854775807) == '7FFFFFFFFFFFFFFF'
	assert tk.decode('7FFFFFFFFFFFFFFF') == 9223372036854775807

def test_hex_int_min():
	tk = Token(HEX_ALPHABET)
	assert tk.encode(-9223372036854775808) == '8000000000000000'
	assert tk.decode('8000000000000000') == -9223372036854775808

def test_hex_15():
	tk = Token(HEX_ALPHABET)
	assert tk.encode(15) == 'F'
	assert tk.decode('F') == 15

def test_bin_15():
	tk = Token(BIN_ALPHABET)
	assert tk.encode(15) == '1111'
	assert tk.decode('1111') == 15

def test_bin_neg1():
	tk = Token(BIN_ALPHABET)
	assert tk.encode(-1) == '1' * 64
	assert tk.decode('1' * 64) == -1	

def test_abc_15():
	tk = Token(ABC_ALPHABET)
	assert tk.encode(15) == 'bca'
	assert tk.decode('bca') == 15	

def test_tst_63():
	tk = Token(TST_ALPHABET)
	assert tk.encode(63) == '_'
	assert tk.decode('_') == 63

def test_tst_64():
	tk = Token(TST_ALPHABET)
	assert tk.encode(64) == 'BA'
	assert tk.decode('BA') == 64
