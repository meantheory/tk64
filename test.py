import string

from tk64 import Token
from tk64 import TokenError

from py.test import raises

HEX_ALPHABET = '0123456789ABCDEF'
BIN_ALPHABET = '01'
ABC_ALPHABET = 'abc'
WRD_ALPHABET = '!@#$%^&*()_+-{}][<>.,?='
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

def test_hex_pos_error():
	tk = Token(HEX_ALPHABET)
	with raises(TokenError):
		tk.encode(9223372036854775808)

def test_hex_neg_error():
	tk = Token(HEX_ALPHABET)
	with raises(TokenError):
		tk.encode(-9223372036854775809)

def test_wrd_22():
	tk = Token(WRD_ALPHABET)
	assert tk.encode(22) == '='
	assert tk.decode('=') == 22

def test_wrd_23():
	tk = Token(WRD_ALPHABET)
	assert tk.encode(23) == '@!'
	assert tk.decode('@!') == 23

def test_empty_str():
	tk = Token(HEX_ALPHABET)
	with raises(TokenError):
		tk.encode('')

def test_bad_alpha():
	tk = Token(ABC_ALPHABET)
	with raises(TokenError):
		tk.decode('bcd')


