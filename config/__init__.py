import os

from .config import BrowserConfig

path_to_dir = os.path.dirname(__file__)
path_to_config = os.path.join(path_to_dir, 'config.env')

file = os.getenv('ENV_FILE', path_to_config)

browser = BrowserConfig(_env_file=file)

os.getenv('CHROME')