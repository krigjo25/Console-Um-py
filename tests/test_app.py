# Importing responsories

import pytest
from app import count


def test_assertion():

    #   Creating strings to test
    a = "Um, thanks for the album"
    b = "Hello, um, world"
    c = "This is, um... CS50."
    d = "Um, thanks, um..."
    e = "Um... what are regular expressions?"
    f = "Um, thanks, um, regular expressions make sense now."
    g = "Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?"
    
    
    #   Counting how many 'um'
    assert count(a) == 1
    assert count(b) == 1
    assert count(c) == 1
    assert count(d) == 2
    assert count(e) == 1
    assert count(f) == 2
    assert count(g) == 2