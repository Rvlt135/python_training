import yaml

host = ['192.168.0.1', '8080']
env = [{'browsers': [{'version': '87.0.1',
                      'browser': 'chrome', 'lang': 'en'}]}]
creds = ['user_name', 'password']
ci = ['jenkins', 'selenide']


config_yaml = {'host': host, 'environment': env, 'log': 'user_name',
               'password': '123qwe', 'ci_cd': ci}

with open('config.yaml', 'w') as config:
    yaml.dump(config_yaml, config)
