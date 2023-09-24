import json
import os

from pypulse import Aplication
from pypulse.Template import RenderTemplate
from pypulse.View import view


@view(name='home', path_trigger='/')
def home(request: dict):
    data_file_path = os.path.join(
        Aplication.Vars.APLICATION_PATH, 'baseapp', 'data.json')
    with open(data_file_path, 'r') as fr:
        data = json.load(fr)

    if request.get("method") == "GET":
        return RenderTemplate('home.html', {'data': data})

    if request.get("method") == "POST":
        with open(data_file_path, 'w') as fw:

            data.append({
                'id': data[-1]['id'] + 1 if len(data) >= 1 else 0,
                'name': request.get("body")['task'].replace('%2', ' '),
                'description': request.get("body")['description'].replace('%2', ' '),
            })
            json.dump(data, fw, indent=4)

        return RenderTemplate('home.html', {'data': data})
