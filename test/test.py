from mypackage import mymodule

def test_top_n():

    """

    make sure top_n works properly

    """

    assert mymodule.top_n([3,6,1,8,4,2,0, 3]) == [8,6,4], 'incorrect'
    assert mymodule.top_n([3,7,1,8,4,2,9, 3]) == [9,8,7], 'incorrect'
    assert mymodule.top_n([9,6,1,8,4,8,7, 4]) == [9,8,8,7], 'incorrect'