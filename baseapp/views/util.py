def get_task(data, id):
    for i in data:
        if i['id'] == id:
            return i

def del_task(data, id):
    for i in range(len(data)):
        if data[i]['id'] == id:
            del data[i]
            break
    
    return data
