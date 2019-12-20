MVC

Model

​	DB

View (Django: Template)

​	사용자가 보는 화면

Controller (Djanggo: View)

​	DB의 데이터를 사용자가 보는 화면으로 전달

​	사용자의 데이터를 적절히 가공해서 DB에 변경사항을 전달

urls.py -> URLResolver

요청의 URL을 판단해서 특정 Controller(View함수)로 연결

request -> runserver -> urls.py -> view function -> Response(HTTP 규격)

 

 