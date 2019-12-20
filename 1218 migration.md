### Migration

- 모델 변경내역 히스토리 관리

- 모델의 변경 내역을 DB Schema(데이터베이스 데이터 구조)로 반영시키는 효율적인 방법을 제공

- migration 옵션을 끌 수도 있음

  ```python
  # 마이그레이션 파일 생성
  python manage.py makemigrations 앱이름 
  # 마이그레이션 적용
  python manage.py migrate 앱이름
  # 마이그레이션 적용 현황
  python manage.py showmigrations 앱이름
  # 지정 마이그레이션의 SQL 내역
  python manage.py sqlmigrate 앱이름 마이그레이션이름
  ```

  

  