import tkinter as tk
import json


class JSONVar(tk.StringVar):
    """A Tk variable that can hold dicts and lists"""
    """When overriding methods in a class you didn't write, it's always a 
    good idea to include *args and **kwargs to to catch any arguments 
    that you don't explicitly list. That way, the method will continue 
    to allow all the arguments that the superclass version did, but you 
    won't have to explicitly enumerate them all"""

    def __init__(self, *args, **kwargs):
        kwargs['value'] = json.dumps(kwargs.get('value'))
        super().__init__(*args, **kwargs)

    def set(self, value, *args, **kwargs):
        string = json.dumps(value)
        super().set(string, *args, **kwargs)

    def get(self, *args, **kwargs):
        string = super().get(*args, **kwargs)
        return json.loads(string)


if __name__ == "__main__":
    root = tk.Tk()
    var1 = JSONVar(root)
    var1.set([1, 2, 3])
    var2 = JSONVar(root, valuevalue={'a': 10, 'b': 15})

    print("Var1, var1.get()[1]")
    # Should print 2

    print("var: "), var.get()[b]
