from django.contrib import admin #admin 툴을 사용하겠다
from .models import User #우리의 위치와 동일하게있는 python 파일을 가져오겠다 모델을 가져오겠다

# Register your models here.
admin.site.register(User) # 이 코드가 나의 User을 Admin에 추가 해 줍니다