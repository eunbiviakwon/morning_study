```
> pyenv install 버전
> pyenv virtualenv 버전 환경이름
# 가상환경을 설정할 폴더로 이동 후
> pyenv local 환경이름
> pip install django~=버전
> django-admin startproject 프로젝트이름
> python manage.py startapp 앱이름
> pip install django_extensions notebook (실행할때 python manage.py shell_plus --notebook)
> pip freeze>requirements.txt
setting.py에 들어가서 안에 있는 installedapp에 방금 추가한 앱이름이랑 'django-extensions' 넣기


모델에 클래스 변경 후
> python manage.py makemigrations
> python manage.py migrate
```

----

Python interpreter설정

이 프로젝트에서 사용하는 코드를 어떤 파이썬을 사용해서 해석할지 정해주는 과정.

1. PyCharm의 설정(Preferences)로 진입
2. Project Interpreter선택
3. 우측창의 Project Interpreter: 우측의 드롭다운 메뉴를 클릭
4. 가장 아래로 스크롤하여 Show All선택
5. 초록색 + 버튼 클릭 -> Add local
6. 새로 열린 창에서 Virtualenv Environment탭이 선택되어있는지 확인
7. Exisiting environment 라디오버튼 클릭
8. Interpreter: 항목의 가장 우측에 있는 ... 버튼 클릭
9. 인터프리터로 사용될 파이썬 경로 선택

- Mac은 /user/local/var/pyenv/versions/sample-env/bin/python
- ubuntu는  `/Users/<자신의 홈폴더명>/.pyenv/versions/sample-env/bin/python`선택

10. 추가된 인터프리터 선택 후 OK클릭
11. 나온 창에서 OK클릭

