objects = [[],[],[]] #list of list 객체 먼저 오는것 뒤로

def add_object(o,depth = 0):
    objects[depth].append(o)

def update():
    for layer in objects:
        for o in layer:
            o.update()

def render():
    for layer in objects:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('Cannot delete non existing object')

