### virtualenv

- virtualenv(독립된 개발환경을 제공해주는 프로그램)를 활용하여 가상 개발환경을 구축
- 가상환경 위에서 원하는 버전의 django 및 패키지 설치

#### 가상환경 추가 및 실행

```python
pyenv virtualenv 버전 환경이름 #virtualenv 만들기
pyenv local 환경이름 #virtualenv 실행
```

#### 가상환경 위에djnago 및 패키지 설치

```python
pip install django~=버전 # pipsms Pip installs Package의 약자, 기본적으로 파이썬 설치시 같이 설치되는 package Manager. 외부 파이썬 패키지나 라이브러리를 대신 설치해줌
pip freeze #설치한 패키지 리스트 확인

pip install django_extensions notebook # setting.py 내 INSTALLED_APPS에 djnago_extesions 추가 필요
python manage.py shell_plus # 익스텐션 앱을 설치하면 shell_plus 사용 가능, 필요한 모델을 자동 import 해줘서 편리함
python manage.py shell_plus --notebook # jupyter notebook을 통해서 django shell을 사용 가능

```

#### requirement.txt

- 필요한 라이브러리를 설치하여 개발환경 세팅 후 requirements.txt를 만든다.
- requirements.txt가 있으면 다음 명령을 통해 동일한 파이썬 패키지들을 한번에 설치할 수 있다.
- 매 패키지마다 명령어를 치며 설치하기는 힘들기 때문에 requirements.txt 사용.
- 프로젝트 디렉토리 내에 requirements라는 디렉토리를 만든 뒤 그 디렉토리 내에서 명령어 실행.  ```pip freeze```는 현재 pip로 설치한 패키지 목록을 출력하는 명령어. >는 해당 출력 내용을 다음 인자로 오는 파일에 저장하는 명령어. 명령어 실행이 끝나면 requirements.txt라는 파일 생성. 

```python
pip3 freeze > requirements.txt # 패키지 목록을 txt 파일로 만들기
pip3 install -r requirements.txt # 한번에 패키지 설치
```

### django 프로젝트 생성

```python
django-admin startproject 프로젝트이름 . # .은 현재 디렉토리에 장고를 설치하라고 스크립트에게 알려줌
```

- setting.py 설정 수정

  ```python
  LANGUAGE_CODE = 'ko-kr'
  TIME_ZONE = 'Asia/Seoul'
  STATIC_ROOT = os.path.join(BASE_DIR, 'static')
  ```

### djnago 프로젝트 app 생성

```
python manage.py startapp 앱이름
```

- setting.py에 생성한 app 등록

  ```python
  INSTALL_APPS = [
  ...
  'myapp',
  ]
  ```

#### Python interpreter설정

- 이 프로젝트에서 사용하는 코드를 어떤 파이썬을 사용해서 해석할지 정해주는 과정.

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

##### reference

https://wayhome25.github.io/django/2017/04/29/python-dev-environments/