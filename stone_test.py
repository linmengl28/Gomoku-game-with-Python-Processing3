from stone import Stone


def test_init():
    st = Stone(10, 1)
    assert st.size == 9
    assert st.color == 1
    assert st.ls == []
