import requests
import json

server_url = "http://localhost:8080"



def get_ondemand_envs():
    x = requests.get(f"{server_url}/envs")
    return x.json()

def get_ondemand_env_status(env_name):
    x = requests.get(f"{server_url}/envs/{env_name}")
    return x.json()[env_name]

