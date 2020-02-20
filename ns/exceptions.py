def assert_login(username, password):
    """
    Asserts that both the username and password are include or they are both none.
    :param username:
    :param password:
    """
    assert (username is None and password is None) or (username is not None and password is not None), \
        "Both username and password need to be included otherwise use login json file."
