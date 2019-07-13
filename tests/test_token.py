from rundeck import CreateTokenOption, Rundeck


def test_create_token(rd):
    o = CreateTokenOption(
        user='admin',
        duration='12d'
    )
    r = rd.create_token(options=o)
    assert r.data
    assert r.token


def test_list_tokens(rd):
    r = rd.list_tokens()
    assert r.tokens


def test_get_token(rd):
    r = rd.get_token(rd.list_tokens().token_ids[-1])

    assert r.token


def test_delete_token(rd):
    r = rd.list_tokens()
    length1 = len(r.tokens)
    rd.delete_token(rd.list_tokens().token_ids[-1])
    r = rd.list_tokens()
    length2 = len(r.tokens)
    assert length1 == length2 + 1


def test_token(rd):
    token = rd.get_token(rd.list_tokens().token_ids[-1]).token['token']
    test_rd = Rundeck(token=token)
    test_rd.list_projects()
    o = CreateTokenOption(
        user='admin',
        duration='12d'
    )
    rd.create_token(options=o)
