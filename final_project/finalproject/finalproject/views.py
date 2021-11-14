import sys

import builtins

from django.shortcuts import render

res = ''

def home(request):
    return render(request, 'home.html')


def new_print(*args, sep=' ', end='\n', file=None):
    builtins.print(*args, sep, end, file)
    global res
    res = str(*args)


def result(request):
    global res
    code = request.GET["usercode"]
    print = new_print
    if "import sys" in code:
        print("You are not allowed to use 'import sys' in your code!")
    if "exec" in code:
        print("You are not allowed to use 'exec' in your code!")
    if "eval" in code:
        print("You are not allowed to use 'eval' in your code!")
    if "import os" in code:
        print("You are not allowed to use 'import os' in your code!")
    return render(request, 'result.html', {"res": res})
    try:
        exec(code)
    except Exception as e:
        res = type(e).__name__
        res = res + ":   " + str(e)
    return render(request, 'result.html', {"res":res})


