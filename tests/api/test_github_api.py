import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_get_not_exist_user(github_api):
    r = github_api.get_user('defunkt22')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become_qa_auto')
    # print(r['items'])
    assert r['total_count'] == 50
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('become_qa_auto_not_exist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('b')
    assert r['total_count'] != 0


@pytest.mark.api
def test_emojis_find_specific_emojis(github_api):
    r = github_api.search_emojis()
    assert r['smile'] == "https://github.githubassets.com/images/icons/emoji/unicode/1f604.png?v8"
    assert r['desert'] == "https://github.githubassets.com/images/icons/emoji/unicode/1f3dc.png?v8"

@pytest.mark.api
def test_emojis_find_numbers_of_emojis(github_api):
    r = github_api.search_emojis()
    assert len(r) > 100 