from django.shortcuts import render
from random import randrange

y = [0] * 6
def sorteio():
    for i in range(6):
        x = randrange(1, 60 )
        y[i] = x
        if x in y:
            tem = True
            while tem == True:
                tem = False
                x = randrange(1, 60)
                if x in y:
                    tem = True
                y[i] = x
    return y
def home(request):
    a = sorteio()
    if request.method == 'POST':
        a = sorteio()
    return render(request, 'index.html', { 'a': a})
