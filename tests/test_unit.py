from cipher.encrypt.core import encrypt
from cipher.decrypt.core import decrypt
from cipher.helpers import exit_session


def test_should_shift_string_by_number():
    assert encrypt("cat", 1) == "dbu"
    assert encrypt("zuzu", 1) == "avav"
    assert encrypt("aaa zzz bbb", 1) == "bbb aaa ccc"
    assert encrypt("Aa", 2) == "cc"


def test_should_decipher_string_by_shift():
    assert decrypt("dbu", 1) == "cat"
    assert decrypt("avav", 1) == "zuzu"
    assert decrypt("bbb aaa ccc", 1) == "aaa zzz bbb"


def test_should_return_true_to_exit_and_false_to_continue():
    assert exit_session("Yes")
    assert not exit_session("No")
