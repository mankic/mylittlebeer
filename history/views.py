from django.shortcuts import render, redirect
from .models import History
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.

def history_view(request):
    if request.method =='GET':
        # user = request.user.is_authenticated
        # if user:
        historys = History.objects.all().order_by('-created_at')
        return render(request, 'history/history.html', {'historys': historys})
        # else:
        #     return redirect('/sign-in')

# @login_required
def delete(request, id):
    historys = History.objects.get(id=id)
    historys.delete()
    return redirect('/history')