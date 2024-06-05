import os
import pickle

user_save_file = "user.pkl"


def saveUser(user):
    with open(user_save_file, "wb") as f:
        pickle.dump(user, f)


def loadUser():
    if os.path.exists(user_save_file):
        with open(user_save_file, "rb") as f:
            return pickle.load(f)
    else:
        return None
