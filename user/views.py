from django.shortcuts import render, redirect  # html 화면에 보여주는 역할
from .models import User
from django.contrib.auth import get_user_model  # 사용자가 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models.deletion import Collector
from django.db import (
    router,
)


# Create your views here.
def user(request):
    return render(request, 'recommend/index.html')


def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')

        if password != password2:
            # 패스워드가 같지 않다고 알람
            return render(request, 'user/signup.html', {'error': '패스워드를 확인해주세요!'})
        else:
            if username == '' or password == '' or email == '':
                return render(request, 'user/signup.html', {'error': '빈칸을 채워주세요!'})

            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html',
                              {'error': '사용자가 존재합니다'})  # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
            else:
                User.objects.create_user(username=username, password=password, email=email)
                return redirect('/sign-in')


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'user/signin.html', {'error': '이름(아이디) 혹은 패스워드를 확인 해 주세요'})

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')





@login_required()
def update_confirm(request):
    if request.method == 'POST':
        user = request.user
        password = request.POST.get("password", "")
        if user.check_password(password):
            return render("/update")
        else:
            raise Exception("잘못된 비밀번호를 입력했습니다.")
            return redirect('/update_confirm')

@login_required()
def delete_confirm(request):
    if request.method == 'POST':
        user = request.user
        password = request.POST.get("password", "")
        if user.check_password(password):
            return render("/delete")
        else:
            raise Exception("잘못된 비밀번호를 입력했습니다.")
            return redirect('/delete_confirm')

@login_required()
def update(request):
    if request.method == 'POST':
        user = request.user
        username = request.POST.get("username,", "")
        password = request.POST.get("password", "")
        email = request.POST.get("email", "")

        user.username = username
        user.password = password
        user.email = email
        user.save()
    return render("/")
@login_required()
def delete(request):
    user = request.user
    user.delete()
    return redirect('/')


