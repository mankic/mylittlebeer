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
            return render(request, 'user/signup.html',{'error':'패스워드를 확인해주세요!'})
        else:
            if username == '' or password == '' or email == '':
                return render(request, 'user/signup.html', {'error': '사용자 이름과 비밀번호는 필수 값입니다!'})

            exist_user = get_user_model().objects.filter(username=username)
            exist_email = get_user_model().objects.filter(email=email)

            if exist_user:
                return render(request, 'user/signup.html', {'error':'사용자가 존재합니다'})  # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
            elif exist_email:
                return render(request, 'user/signup.html', {'error':'이메일이 존재합니다'})  # 이메일이 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
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
    return redirect('/sign-in')






@login_required()
def delete(request):
    if request.method == 'GET':
        return render(request,'user/user_delete.html')
    elif request.method == 'POST':
        user = request.user
        password = request.POST.get("password", "")
        if user.check_password(password):
            auth.logout(request)
            user.delete()
            return render(request,"user/signin.html")
        else:
            raise Exception("잘못된 비밀번호를 입력했습니다.")
            return redirect('/user')

@login_required()
def update(request):

    if request.method == 'GET':
        return render(request, 'user/user_update.html')

    elif request.method == 'POST':
        user = request.user


        email = request.POST.get("email", "")



        user.email = email
        user.save()

    return redirect('/recommend')


