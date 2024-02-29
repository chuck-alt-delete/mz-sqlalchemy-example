from sqlalchemy import create_engine
from pathlib import Path
from sqlalchemy import URL
from dotenv import dotenv_values


# Load values from .env file into config dictionary.
path_to_env = Path(__file__).parent.absolute() / ".env"
config = dotenv_values(path_to_env)

# configure postgres connection options
config["options"] = ''
if config["MZ_CLUSTER"]:
    config["options"] += f'--cluster={config["MZ_CLUSTER"]}'
else:
    config["options"] += '--cluster=quickstart'

if config["MZ_TRANSACTION_ISOLATION"]:
    config["options"] += f' -c transaction_isolation={config["MZ_TRANSACTION_ISOLATION"]}'

if config["MZ_SCHEMA"]:
    config["options"] += f' -c search_path={config["MZ_SCHEMA"]}'

# create connection url
url = URL.create(
    "postgresql+psycopg2",
    database=config["MZ_DB"],
    username=config["MZ_USER"],
    password=config["MZ_PASSWORD"],
    host=config["MZ_HOST"],
    port=6875,
    query={
        "sslmode": "require",
        "application_name": "sqlalchemy app",
        "options": config["options"]
    }
)

# Create a connection engine
engine = create_engine(
    url=url,
    # avoid wrapping queries in transactions
    isolation_level="AUTOCOMMIT"
    )

if __name__ == "__main__":
    print(url)
