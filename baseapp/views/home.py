from pypulse.View import view
from pypulse.Template import RenderTemplate

from baseapp.views.util import get_task, del_task

import os

from pypulse import Aplication

import json


@view(name='home', path_trigger='/')
def home(request: dict):
    data_file_path = os.path.join(Aplication.Vars.APLICATION_PATH, 'baseapp', 'data.json')
    with open(data_file_path, 'r') as fr:
        data = json.load(fr)

    if request.get("method") == "GET":
        return RenderTemplate('home.html', {'data': data})

    if request.get("method") == "POST":
        body = request.get("body")
        body_keys = list(body.keys())

        if 'create' in body_keys:
            with open(data_file_path, 'w') as fw:
                print(data)
                data.append({
                    'id': data[-1]['id'] + 1 if len(data) >= 1 else 0,
                    'name': request.get("body")['task'].replace('%2', ' '),
                    'description': request.get("body")['description'].replace('%2', ' '),
                })

                json.dump(data, fw, indent=4)

            return RenderTemplate('home.html', {'data': data})

        if 'update' in body_keys:
            task = get_task(data, int(body['id']))

            with open(data_file_path, 'w') as fw:
                task['name'] = body['task'].replace('%2', ' ') 
                task['description'] = body['description'].replace('%2', ' ')

                json.dump(data, fw, indent=4)

            return RenderTemplate('task.html', {'id': task["id"], 'name': task['name'], 'description': task['description']})

        if 'delete' in body_keys:
            with open(data_file_path, 'w') as fw:
                data = del_task(data, int(body['id']))
                json.dump(data, fw, indent=4)

            return RenderTemplate('home.html', {'data': data})

        else: 
            task = get_task(data, int(body_keys[0]))

            return RenderTemplate('task.html', {'id': task["id"], 'name': task["name"], 'description': task['description']})
