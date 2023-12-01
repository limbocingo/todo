import json
import os

from pypulse import Aplication
from pypulse.Template import Redirect, RenderTemplate, Reload
from pypulse.View import view

from baseapp.views.util import del_task, get_task


@view('task', '/task/<int:id>')
def task(request: dict, id: int):
    data_file_path = os.path.join(
        Aplication.Vars.APLICATION_PATH, 'baseapp', 'data.json')
    with open(data_file_path, 'r') as fr:
        data = json.load(fr)

    task = get_task(data, id)

    if request.command == 'POST':
        task['description'] = request.parameters['description']
        task['name'] = request.parameters['task']

        for i in range(len(data)):
            if task['id'] == data[i]['id']:
                data[i] = task

        with open(data_file_path, 'w') as fw:
            json.dump(data, fw, indent=4)

    return RenderTemplate('task.html', {'id': task["id"], 'name': task["name"], 'description': task['description']})


@view(name='delete_task', path_trigger='/task/<int:id>/delete')
def delete_task(request: dict, id: int):
    data_file_path = os.path.join(
        Aplication.Vars.APLICATION_PATH, 'baseapp', 'data.json')
    with open(data_file_path, 'r') as fr:
        data = json.load(fr)

    del_task(data, id)

    with open(data_file_path, 'w') as fw:
        json.dump(data, fw, indent=4)

    return Redirect('/')
