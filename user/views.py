from django.shortcuts import render, redirect  # html 화면에 보여주는 역할
from .models import User
from django.contrib.auth import get_user_model  # 사용자가 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password


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
        email = request.POST.get('email','')
        password = request.POST.get('password','')

        me = auth.authenticate(request, email=email, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'user/signin.html', {'error': '이메일 혹은 패스워드를 확인 해 주세요'})

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


# # users/views.py
#
# class CheckPasswordForm():
#     if request.method == 'GET':
#         user = request.user.is_authenticated
#     password = form.CharField(label='비밀번호', widget=form.PasswordInput(
#         attrs={'class': 'form-control', }),
#                                )
#
#     def __init__(self, user, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.user = user
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         confirm_password = self.user.password
#
#         if password:
#             if not check_password(password, confirm_password):
#                 self.add_error('password', '비밀번호가 일치하지 않습니다.')
#
#
#
#
#
# @login_message_required
# def user_delete_view(request):
#     if request.method == 'POST':
#         password_form = CheckPasswordForm(request.user, request.POST)
#
#         if password_form.is_valid():
#             request.user.delete()
#             logout(request)
#             messages.success(request, "회원탈퇴가 완료되었습니다.")
#             return redirect('/users/login/')
#     else:
#         password_form = CheckPasswordForm(request.user)
#
#     return render(request, 'users/user_delete.html', {'password_form': password_form})
#
#

# user/views.py

# @login_required
# def user_view(request):
#     if request.method == 'GET':
#         # 사용자를 불러오기, exclude와 request.user.username 를 사용해서 '로그인 한 사용자'를 제외하기
#         user_list = User.objects.all().exclude(email=request.user.email)
#         return render(request, 'user/user_list.html', {'user_list': user_list})


# @login_required
# def user_follow(request, id):
#     me = request.user
#     click_user = User.objects.get(id=id)
#     if me in click_user.followee.all():
#         click_user.followee.remove(request.user)
#     else:
#         click_user.followee.add(request.user)
#     return redirect('/user')
