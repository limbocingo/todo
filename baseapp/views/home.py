import json
import os

from pypulse import Aplication
from pypulse.Template import RenderTemplate, Reload
from pypulse.View import view


@view('home', '/')
def home(request: dict):
    data_file_path = os.path.join(
        Aplication.Vars.APLICATION_PATH, 'baseapp', 'data.json')
    
    with open(data_file_path, 'r') as fr:
        data = json.load(fr)

    if request.command == "GET":
        return RenderTemplate('home.html', {'data': data})

    if request.command == "POST":
        parameters = request.parameters

        if not parameters:
            return Reload()

        task = parameters.get('task')
        description = parameters.get('description')

        data.append({
            'id': data[-1]['id'] + 1 if len(data) >= 1 else 0,
            'name': task.replace('%2', ' '),
            'description': description.replace('%2', ' '),
        })

        with open(data_file_path, 'w') as fw:
            json.dump(data, fw, indent=4)

        return Reload()
