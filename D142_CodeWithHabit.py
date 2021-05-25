# decoratoros

def func_neeeds_decorations():
    print("This func needs a decorator")


def new_decorator(func):
    print("This is the decoration")
    func()


func_needs_decorations = new_decorator(func_neeeds_decorations)

func_needs_decorations()

#check tomorrow



