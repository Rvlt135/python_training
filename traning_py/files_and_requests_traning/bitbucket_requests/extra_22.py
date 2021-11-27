import requests
from AccessTokenBitbucket import AccessToken
access_token = AccessToken()
# Если access_token_by_code нужно добавить в init user_code
# Если access_token_by_password нужно добавить креды в класс
get_access_token = access_token.access_token_by_code()


def get_user(acs_tkn):
    url = 'https://api.bitbucket.org/2.0/user'
    token = {'access_token': acs_tkn}
    request = requests.get(url, params=token)
    response = request.json()
    print(response)


"""Получаем данные по доступным репозиториям"""


def get_repository(acs_tkn):
    url = 'https://api.bitbucket.org/2.0/repositories'
    query = {'access_token': acs_tkn, 'role': 'owner'}
    request = requests.get(url, params=query)
    response_json = request.json()
    """values.name в основном объекте == имя репозитория"""
    for i in response_json['values']:
        main_branch = i['mainbranch']
        uuid = i['workspace']
        print(f"Name: {i['name']}, Main Branch: {main_branch['name']}")
        """C корневым uuid получаем No user with username"""
        """Возвращаем с которым будем работать, как для пользователя"""
        print(f"values.uuid: {uuid['uuid']}")
        return uuid['uuid']


"""Получаем данные по доступным pull request"""


def get_pull_requests(acs_tkn, uuid):
    url = f'https://api.bitbucket.org/2.0/pullrequests/{uuid}'
    query = {'access_token': acs_tkn}
    request = requests.get(url, params=query)
    response_json = request.json()
    """также можно собрать объекты value"""
    print(f"Кол-во PR: {response_json['size']}")
    for i in response_json['values']:
        source = i['source']
        print(f"PR: {source['branch']['name']}, status: {i['state']}")
        print(f"comment_count: {i['comment_count']}")


get_user(get_access_token)
workspace_uuid = get_repository(get_access_token)
get_pull_requests(get_access_token, workspace_uuid)
