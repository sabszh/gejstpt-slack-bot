import json
import os
from state_store.user_identity import UserIdentity
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


def get_user_state(user_id: str, is_app_home: bool):
    filepath = f"./data/{user_id}"
    if not is_app_home and not os.path.exists(filepath):
        raise FileNotFoundError("Der er ikke valgt nogen indstilling endnu. Gå venligst til appens forside (App Home) og vælg en mulighed for at komme i gang.")
    try:
        if os.path.exists(filepath):
            with open(filepath, "r") as file:
                user_identity: UserIdentity = json.load(file)
                return user_identity["provider"], user_identity["model"]
    except Exception as e:
        logger.error(e)
        raise e
