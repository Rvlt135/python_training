import requests
from requests.auth import HTTPBasicAuth


class AccessToken:
    def __init__(self):
        self.key = 'nuFrwtBYVJwRkFddJC'  # key == client_id
        self.secret = '2daSGv4pm3Q7F7FQW7kTCHbFYgQGTsq4'
        self.url = 'https://bitbucket.org/site/oauth2/access_token'
        """
        Получаем код для авторизации
        The full-blown 3-LO flow. Request authorization from the end user
        by sending their browser to:
        https://bitbucket.org/site/oauth2/authorize?client_id={client_id}&
        response_type=code
        grant_type: authorization_code
        """
        self.user_code = ''  # Для авторизации по коду
        self.authorize_type = 'authorization_code'
        self.refresh_type = 'refresh_token'
        """login:
        password:
        Использовать для авторизации по кредам
        grant_type: password
        """
        self.login = ''
        self.password = ''
        self.password_type = 'password'

    def access_token_by_password(self):
        key = self.key
        secret = self.secret
        url = self.url
        req_body = {'grant_type': self.password_type,
                    'username': self.login, 'password': self.password}
        request = requests.post(url, data=req_body,
                                auth=HTTPBasicAuth(key, secret))
        acs_token = request.json()
        return acs_token['access_token']

    def access_token_by_code(self):
        key = self.key
        secret = self.secret
        code = self.user_code
        url = self.url
        req_body = {'grant_type': self.authorize_type,
                    'code': code}

        request = requests.post(url, data=req_body,
                                auth=HTTPBasicAuth(key, secret))
        acs_token = request.json()
        return acs_token['access_token']

    def refresh_token(self):
        key = self.key
        secret = self.secret
        code = self.user_code
        password_type = self.password_type
        url = self.url
        req_body = {'grant_type': self.authorize_type,
                    'code': code}
        if code:
            request = requests.post(url, data=req_body,
                                    auth=HTTPBasicAuth(key, secret))
            acs_token = request.json()
            return acs_token['access_token']
        elif password_type:
            url = 'https://bitbucket.org/site/oauth2/access_token'
            req_body = {'grant_type': password_type,
                        'username': self.login, 'password': self.password}
            request = requests.post(url, data=req_body,
                                    auth=HTTPBasicAuth(key, secret))
            acs_token = request.json()
            return acs_token['access_token']
