from Consts import *

import json

def read() -> dict:
    with open(CHAT_DATA_FILE) as data_file:
        file_data = data_file.read()
        chat_data_temp = json.loads(file_data)

    chat_data = {int(key): val for key, val in chat_data_temp.items()}
    return chat_data

def write(chat_data: dict) -> None:
    with open(CHAT_DATA_FILE, "w") as data_file:
        file_data = json.dumps(chat_data).replace("}},", "}},\n")
        data_file.write(file_data)

def update(chat_id: int) -> dict:
    chat_data = read()

    if chat_id not in chat_data:
        chat_data[chat_id] = DEFAULT_USER_DATA
        write(chat_data)

    return chat_data