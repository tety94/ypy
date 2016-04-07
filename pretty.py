from __future__ import print_function, division

def print_namespace(ns, name_width=25):
    for name, val in sorted(vars(ns).items()):
        if not name.startswith('_'):
            print(('{:<'+str(name_width)+'}{}').format(name, val))
