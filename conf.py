import secrets

ACCEPTED_HOSTS = secrets.HOSTS

BAMBUSER_API_KEY = secrets.API_KEYS['bambuser']['api_key']
BAMBUSER_USERNAME = secrets.API_KEYS['bambuser']['user']
MEERKAT_API_KEY = secrets.API_KEYS['meerkat']
PERISCOPE_API_KEY = secrets.API_KEYS['periscope']
# for a tool we're not using currently but good to have
LIVESTREAM_API_KEY = secrets.API_KEYS['livestream']