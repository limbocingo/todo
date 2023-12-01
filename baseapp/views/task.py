import json
import os

from pypulse import Aplication
from pypulse.Template import Redirect, RenderTemplate
from pypulse.View import view

from baseapp.views.util import del_task, get_task


@view(name='task', path_trigger='/task/<int:id>')
def task(request: dict, id: int):
    data_file_path = os.path.join(
        Aplication.Vars.APLICATION_PATH, 'baseapp', 'data.json')
    with open(data_file_path, 'r') as fr:
        data = json.load(fr)

    task = get_task(data, id)

    if request.get('method') == 'POST':
        task['description'] = request.get('body')['description']
        task['name'] = request.get('body')['task']

        for i in range(len(data)):
            if task[i]['id'] == data[i]['id']:
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

    task = del_task(data, id)

    with open(data_file_path, 'w') as fw:
        json.dump(data, fw, indent=4)

    return RenderTemplate('home.html', {'data': data})
