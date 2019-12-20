### Models

모델은 데이터에 대한 정보를 나타내는 최종 소스이다. 그것은 갖고있는 데이터의 필수 필드와 행동(함수)을 포합한다.

기본사항 

- 각각의 모델은  ```djnago.db.models.Model``` 의 서브클래스이다.
- 모델의 각 속성은 데이터베이스의 필드를 나타낸다.
- 이것들을 이용해서, 장고는 데이터베이스 액세스 API를 제공 

#### Quick example

이 샘플 모델은 `first_name`과 `last_name`을 가진 `Person`을 정의함

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

`first_name`과 `last_name`은 모델의 필드. 각각의 필드는 클래스의 속성을 나타내며, 데이터베이스의 컬럽에 매핑됨

위의 `Person`모델은 아래와 같은 데이터테이블을 만듦

```python
CREATE TABLE myapp_person (
"id" serial NOT NULL PRIMARY KEY,
"first_name" varchar(30) NOT NULL,
"last_name" varchar(30) NOT NULL
);
```

몇가지 기술적 정보:

- 테이블 이름은 `myapp_person`으로 만들어지지만, 재정의할 수 있음
- `id`필드는 자동으로 추가되지만, 오버라이드할 수 있음
- 이 예제에서 쓰인 `CREATE TABLE` SQL은 `PostgreSQL` 문법이지만 장고에서는 지정된 데이터베이스에 맞는 SQL을 사용

#### Using models

모델을 정의하면, 장고에게 이 모델을 사용할 것임을 알려야함. 설정파일에서 `INSTALLED_APPS` 설정에 `models.py`를 포함하고 있는 모듈의 이름을 추가해줌.

```python
INSTALLED_APPS = [
#...
'myapp,
#...
]
```

새로운 애플리케이션을 `INSTALLED_APPS`에 추가했다면, `manage.py migrate` 명령어를 실행. 선택적으로는 `manage.py makemigrations`를 사용해서 먼저 마이그레이션을 만들어줄 수 있음

#### Fields

모델에서 가장 중요한 부분이며, 반드시 필요한 부분. 필드는 데이터베이스의 필드를 정의함. 또한, 필드는 클래스 속성으로 사용됨. clean, save, delete와 같은 models API와 중복되지 않도록 함

예제:

```python
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    
class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
```

#### Field types

각각의 필드는 적절한 필드 클래스의 인스턴스여야 함.

필드 클래스는 아래의 몇가지 사항을 정의함

- 데이터베이서 컬럼의 데이터 형
- form field를 렌더링 할 때 사용할 기본 HTML위젯
- Django admin에서 자동으로 만들어지는 form 의 검증 형태

장고는 매우 다양한 내장 필드 타입을 제공. 장고에서 제공하지 않는 자신만의 필드를 쉽게 만들 수도 있음



#### Field options

각 필드는 고유의 인수를 가짐. 예를 들어 `CharField`는 `max_length`인수를 반드시 가져야하며, 데이터베이스에서 VARCHAR 필드의 사이즈를 지정

모든 필드에서 사용 가능한 공통 인수도 있음. 이들은 모두 선택사항.

##### null

True일 경우, 장고는 빈 값을 NULL로 데이터베이스에 저장. 기본값은 False

##### blank

True일 경우, 필드는 빈 값을 허용. 기본값은 False

nulldms epdlxjqpdltmdp NULL값이 들어가는 것을 허용하는 것이며 blank는 데이터베이스에 빈 문자열 값("")을 허용하는 것. from validation은 blank=True일 경우 공백값을 허용. 만약 blank=False라면 해당 필드는 반드시 채워져야함

##### choices

반복 가능한(예를 들면, 리스트나 튜플) 튜플의 묶음을 선택목록으로 사용. 이 인수가 주어지면, 기본 폼 위젯은 select box로 대체되어 선택값을 제한함.

choices는 다음과 같이 나타냄

```python
YEAR_IN_SCHOOL_CHOICES = (
	('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR'. 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
)
```

각 튜플의 첫번째 요소는 데이터베이스에 저장되는 값이며, 두번째 요소는 기본 양식이나 위젯에 표시되는 값이다.

모델 인스턴스에서 표시되는 값을 액세스하기 위해서는 get_FOO_distpay() 함수를 이용한다. 예제는 다음과 같다.

```python
from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
    ('S', 'Small')
    ('M', 'Medium'),
    ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
```

```python
>>> p = Person(name="Fred Flintstone", shirt_size="L")\
>>> p.save()
>>> p.shirt_size
'L'
>>> p.get_shirt_size_display()
'Large'
```

##### default

필드에 기본값으로 설정된다

##### help_text

폼 위젯에서 추가적으로 보여줄 도움말 텍스트. 폼을 사용하지 않아도 문서화에 많은 도움이 된다.

##### primary_key

True일 경우, 해당 필드는 모델의 primary key로 사용된다

어떤 필드에서도 `primary_key=True`를 설정하지 않으면, 장고는 자동으로 `IntegerField`를 생성해 primary key로 사용한다. 그러므로 반드시 `primary_key=True`를 어떤 필드에 추가할 필요는 없다.

primary key필드는 읽기전용이다. 기존의 개체의 primary key값을 변경한 후 저장하면, 이전 객체와는 별개의 새로운 객체가 생성된다.

##### unique

True일 경우, 이 필드의 값ㄷ은 테이블 전체에서 고유해야한다.

이것들은 많이 사용되는 공통 필드 옵션들의 짧은 설명이다.



#### Automatic primary key field

기본적으로 장고는 각 모델에 다음 필드를 제공한다.

``` python
id = models.AutoField(primary_key=True)
```

이것은 auto-increment primary key이다.

만약 임의의 primary key를 지정하고 싶다면, 필드 중 하나에 `primary_key=True`를 지정하면 된다. 장고는 당신이 primary key필드를 추가했을 경우 `id` 컬럼을 추가하지 않는다.

각각의 모델은 정확히 하나의 `primary_key=Ture` 필드를 가져야한다.



#### Verbose field names

`ForeingKey`, `ManyToManyField`, `OneToOneField`를 제외한 모든 필드에서, 자세한 필드명은 첫번째 인수이다. 만약 Verbose name이 주어지지 않을 경우, 장고는 자동으로 해당 필드의 이름을 사용해서 Verbose name 을 만들어 사용한다.

아래의 예에서, verbose name은 `person's first name`이다.

```python
first_name = models.CharField("person's first name", max_length=30)
```

아래의 예에서는 verbose name은 `first name`이다.

```python
first_name = models.CharField(max_lenght=30)
```

`ForeignKey`, `ManyToManyField`, `OneToOneField`는 첫번째 인자로 모델 클래스를 가져야 하므로, `verbose_name` 인수를 사용한다.

```python
poll = models.ForeignKey(
Poll,
on_delete=models.CASCADE,
verbose_name="the related poll",
)
sites = models.ManyToManyField(Site, verbose_name="list of sites")
placee = models.OneToOneField(
	Place,
    on_delete=models.CASCADE,
    verbose_name="related place",
)
```

첫 글자는 대문자로 지정하지 않는다. 장고는 자동으로 첫번째 글자를 대문자화한다.



#### Relationship

관계형 데이터베이스의 강력함은 테이블간의 관계에 있다. 장고는 데이터베이스의 관계 유형 중 가장 일반적인 3가지를 제공한다. `many-to-one`, `many-to-many`, `one-to-one`

##### Many-to-one relationship

Many-to-one 관계를 정의하기 위해, `djnago.db.models.ForeignKey`를 사용한다. 다른 필드 타입과 비슷하게, 모델의 클래스 속성으로 정의한다. `ForeignKey`는 관계를 정의할 모델 클래스를 인수로 가져야한다.

예를 들어, `Car` 모델은 `Manufacturer`를  `ForeignKey`로 갖는다. `Manufacturer`는 여러개의 `Car`를 가질 수 있지만, `Car`는 오직 하나의 `Manufacturer`만을 갖는다.

```python
from django.db import models

class Manufacturer(models.Model):
    #...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    #...
```

또한 recoursive relationships와 relationships to models not yet defined를 만들 수 있다. 자세한 사항은 the modle field reference를 참조한다.(https://docs.djangoproject.com/en/1.10/ref/models/fields/#ref-foreignkey)

`ForeignKey`필드의 이름은 해당 모델의 lowercase를 추천하지만 필수는 아니다.



##### Many-to-many relationships

many-to-many 관계를 정의하기 위해서는, `ManyToNManyField`를 사용한다. `ManyToManyField`는 관계를 정의할 모델 클래스를 인수로 가져야한다.

예를 들어,  `Pizza`모델은 여러 개의 `Topping` 객체를 가질 수 있다. `Topping`은 여러개의 `Pizza`에 올라갈 수 있으며, `Pizza`역시 여러개의 `Topping`을 가질 수 있다. 이것은 다음과 같이 나타낼 수 있다. 

```python
from django.db import models

class Topping(models.Model):
    # ...
    pass

class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyFielfd(Topping)
```

`ForeignKey`와 마찬가지로, 여기서도 recursive relationships와 relationships to models not yet defined를 만들 수 있다.

일반적으로 필드명은 관계된 모델 객체의 복수형을 추천하지만 필수는 아니다. 

어떤 모델이 `ManyToManyField`를 갖는지는 중요하지 않지만, 오직 관계되는 둘 중 하나의 모델에만 존재해야 한다. 

일반적으로 `ManyToManyField` 인스턴스는 form에서 수정할 객체에 가까워야 한다. 위의 예제에서는 `toppings`가 `Pizza`에 있는 것이 `Topping`이 `pizzas`를 갖는 것보다는 자연스럽기 때문에, `Pizza` 래그 에서 사용자는 `toppings`를 선택할 가능성이 높다.

 ##### Extra fields on many-to-many relationships

피자와 토핑같은 간단한 many-to-many 관계를 만들 때, `ManyToManyField`는 필요로 하는 모든 것을 제공한다. 하지만, 때때로 두 모델 사이의 관계와 데이터를 연결해야 할 수도 있다.

예를 들어, 음악가가 속한 음악 그룹을 트래킹(추적)하는 경우를 고려핸본다. 사람과 그룹으로 멤버를 이루는 관계에서, `ManyToManyField`로 이 관계를 나타내고자 한다. 하지만, 어떤 사람이 그룹으로 가입할 때 가입하는 날짜와 같은 세부사항들이 추가로 존재한다. 

이런 경우, 장고에서는 many-to-many 관계를 관리하는 데 사용되는 모델을 지정할 수 있다. 그리고 중간 모델에 추가 피드를 넣을 수 있다. `ManyToManyField`의 `through` 인수에 중간 모델을 가리키도록 하여 연결할 수 있다. 음악가 예제에서는, 다음과 같이 나타낸다.

```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name
   
class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')
    
    def __str__(self):
        return self.name
    
    
class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
```

중간 모델을 설정할 때, 명시적으로 many-to-many관계에 참여하는 모델들의 `ForeignKey`를 지정한다. 이 명시적 선언은 두 모델이 관련되는 법을 정의한다.

중간 모델에는 몇가지 제한 사항이 있다.

- 중간모델은 원본모델(위의 예에서 Group모델)에 대해 단 하나의 `ForeignKey`필드를 가져야 한다. 여러개여도 안되며, 없어서도 안된다. 아니면 반드시 `ManyToMany` 필드에서 `through_fields` 옵션으로 관계에 사용될 필드 이름을 지정해 주어야 한다. 둘 중 하나가 아니면 Validation 에러가 발생한다. 타겟 모델(위 예제에서 Person)의 경우에도 동일하다.
- 자기 자신에게 many-to-many 관계를 가지는 모델의 경우에는 중간 모델에 동일한 모델에 대한 `ForeignKey` 필드를 2개 선언할 수 있다. 3개 이상의 `ForeignKey` 필드를 선언할 경우에는 앞에서 언급한 것과 같이 through_fields 옵션을 설정해주어야 한다.
- 자기자신에게 many-to-many 관계를 가지고 중간모델을 직접 선언하는 경우에는 `ManyToMany`필드의 `symmetrical`옵션을 `False`로 설정해주어야 한다.

이제 `ManyToManyField`에서 중간 모델( 이 경우, `Membership`)을 사용할 준비가 되었다. 중간 모델 인스턴스를 만들어보자

```python
ringo = Person.objects.create(name="Ringo Starr")
paul = Perosn.objects.create(name="Paul McCartney")
beatles = Group.objects.create(name="The Beatles")
m1 = Membership(Person=ringo, group=beatles,
     date_joined=date(1962, 8, 16),
     invite_reason="Needed a new drummer.")
mi.save()
beatles.members.all()
<QuerySet [<Person: Ringo Starr>]>
ringo.group_set.all()
<QuerySet [<Group: The Beatles>]>
m2 = Membership.objects.create(person=paul, group=beatles,
     date_joined=date(1960, 8, 1),
     invite_reason="Wanted to form a band")
neatles.members.all()
<QuerySet [<Person: Ringo Starr>, <Person: Paul McCartney>]>
```

일반적인 many-to-many 필드와는 달리,add()., create(), set()(직접 할당) 명령어를 사용할 수 없다.

```python
# THIS WILL NOT WORK
beatles.members.add(join)
# NEITHER WILL THIS
beatles.members.carete(name="George Harrison")
# AND NEITHER WILL THIS
beatles.member.set([john, paul, ringo, george])
```

왜냐하면 `Person`과 `Group` 관계를 설정할 때 중간 모델의 필드값들을 명시해주어야 하기 때문이다. 즉, 위의 예와 같이 단순히 add/create/set 하는 경우에는 중간 모델에서 person과 group필드값은 알 수 있지만, date_joined와 invite_reason 필드값은 알 수 없기 때문이다.

그러므로 중간모델을 직접 지정한 경우에는 중간 모델을 직접 생성하는 방법밖에는 없다.

```python
Membership.objects.create(person=ringo, grou=beatles,
	date_joined=date(1968, 9, 4),
	invite_reason="You've been gone for a month and we miss you")
beatles.members.all()
<QuerySet [<Person: Ringo Starr>, <Person: Paul McCartney>, <Person: Ringo Starr>]>
# THIS WILL NOT WORK BECAUSE IT CANNOT TELL WHICH MEMBERSHIP TO REMOVE
beatles.members.remove(ringo)
```

하지만 clear() 함수는 사용 가능하다.

```python
# Beatles have broken up
beatles.mombers.clear()
# Note that this deletes the intermediate model instances
Membership.objects.all()
<QuerySet []>
```

관계를 생성할 때는 위와 같은 제약이 있지만, 쿼리시에는 일반적인 many-to-many 관계와 동일하게 사용할 수 있다.

```python
# Find all the groups with a member whose name starts with 'Paul'
Group.objects.filter(members__name__startswith='Paul')
<QuerySet [<Group: The Beatles>]>
```

중간 모델을 사용하고 있기 때문에 아래와 같은 쿼리도 가능하다.

아래의 예제는 비틀즈 멤버 중 1961년 1월 1일 이후에 합류한 멤버를 찾는다.

```python
# Find all the members of the Beatles that joined after 1 Jan 1961
Person.objects.filter(
	group_-name='The Beatles',
	membership__date_joined__gt=date(1961,1,1))
<QuerySet [<Person: Ringo Starr>]>
```

`Membership`모델 (중간모델)에 직접 쿼리할 수도 있다.

```python
ringos_membership = Membership.objects.get(group=beatles, person=ringo)
ringos_membership.date_joined
datetime.date(1962, 8, 16)
ringos_membership.invite_reason
'Needed a new drummer.'
```

`Person` 객체로부터 many-to-many 역참조를 이용해도 위와 동일한 결과를 얻을 수 있다.

````python
ringos_membership = ringo.membership_set.get(group=beatles)
ringos_membership.date_joined
datetime.date(1962, 8, 16)
ringos_membership.invite_reason
'Needed a new drummer.'
````



##### One-to-one relationships

one-to-one 관계를 정의하려면, `OneToOneField`를 이용하면 된다. 다른 관계 필드와 마찬가지로 모델 클래스의 어트리뷰트로 선언하면 된다.

일대일 관계는 다른 모델을 확장하여 새로운 모델을 만드는 경우 유용하게 사용할 수 있다.

예를 들어, 가게(Places) 정보가 담긴 데이터베이스를 구축한다고 한다. 아마 데이터베이스에 주소, 전화번호 등의 정보가 들어갈 것이다. 그런데 맛집 데이터베이스를 추가적으로 구축할 경우, 새로 Restaurant 모델을 만들 수도 있지만, 반복을 피하기 위해 Restaurant 모델에 Place 모델만 `OneToOneField`로 선언해줄 수 있다.

`ForeignKeyField`와 마찬가지로 자기자신이나 아직 선언되지 않은 모델에 대해서도 관계를 가질 수 있다.

`OneToOneFiled`는 `parent_link`라는 옵션을 제공한다

`OneToOneField` 클래스가 자동적으로 모델의 primary key가 있었던 적이 있으나 지금은 더 이상 그렇게 사용하지 않는다. 물론, 직접 `primary_key=True`를 지정하여 primary key로 만들 수는 있다. 어쨌든, 결과적으로 하나의 모델이 여러개의 `OneToOneField`를 가질 수 있게 되었다.

##### Models across files

다른 앱에 선언된 모델과 관계를 가질 수 있다. 그렇게 하려면, 다른 앱의 모델을 import해서 아래와 같이 관계 필드를 선언하면 된다.

```python
from django.db import models
from geography.models import ZipCode

class Restaurant(models.Model):
    #...
    zip_code = models.ForeignKey(
    ZipCode,
    on_delete=models.Set_NULL,
    blank=True,
    null=True,
    )
```



##### Field name restcirtions

장고는 모델 필드명에 2가지 제약을 두고 있다.

1. 파이썬 예약어는 필드명으로 사용할 수 없다. 이 경우, 파이썬 구문 에러가 발생한다.

   ```python
   class Example(models.Model):
   pass = models.IntegerField() # 'pass' is a reserverd word!
   ```

2.  필드 이름에 밑줄 두개를 연속으로 사용할 수 없다. 이는 장고에서 특별한 문법으로 사용되기 때문이다.

   ```python
   class Example(models.Model):
   	foo__bar = models.IntegerField() # 'foo__bar' has two underscores!
   ```

데이터베이스 컬럼명에 밑줄 두개 넣어야만 하는 상황이라면, db_column 옵션을 사용해서 제약을 우회할 수 있다.

SQL 예약어의 경우(join, where, select)에는 필드 이름으로 허용된다. 장고에서 쿼리문을 만들 때, 모든 컬럼명과 테이블명은 이스케이프  처리하기 때문이다 .



##### Meta options

아래와 같이 모델 클래스 내부에 Meta라는 이름의 클래스를 선언해서 모델에 메타데이터를 추가할 수 있다.

```python
from django.db import models

class Ox(models.Model):
	horn_length = models.IntegerField()

	class Meta:
		ordering = ["horn_length"]
		verbose_name_plural = "oxen"
```

모델 메타데이터는 앞에서 보았던 필드의 옵션과 달리, 모델 단위의 옵셥이라고 볼 수 있다. 예들 들어, 정렬 옵션, 데이터베이스 테이블 이름, 또는 읽기좋은 이름(verbose_name) 이나 복수(verbose_name_plural)이름을 지정해줄 수 있다.

모델클래스에 Meta클래스를 반드시 선언해야 하는 것은 아니며, 또한 모든 옵션을 설정해야 하는 것도 아니다.



##### Model Attributes

<strong> objects </strong>

모델 클래스에서 가장 중요한 속성은 `Manager`이다. `Manager` 객체는 모델클래스를 기반으로 데이터베이스에 대한 쿼리 인터페이스를 제공하며, 데이터베이스 레코드를 모델 객체로 인스턴스화 하는데 사용된다. 특별히 `Manager`를 할당하지 않으면 장고는 기본 Manager를 클래스 속성으로 자동 할당한다. 이때, 속성의 이름이 objects이다.

Manager는 모델 클래스를 통해 접근할 수 있으며, 모델 인스턴스(객체)를 통해서는 접근할 수 없다.

##### Model methods

모델 객체(row) 다누이의 기능을 구현하려면 모델 클래스에 메서드를 구현해주면 된다. 테이블 단위의 기능은 Manager에 구현한다.

이러한 규칙은 비즈니스 로직을 모델에서 관리하는데 있어 중요한 테크닉이다.

예를 들어, 다음과 같이 커스텀 메서드를 추가할 수 있다.

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    
    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post_boomer"
        
def _get_full_name(self):
    "Returns the person's full name"
    return '%s %s' % (self.first_name, self.last_name)
full_name = property(_get_full_name)
```

이 예제에서, 마지막 메서드는 property.

model instance reference에는 모델 클래스에 자동적으로 주어지는 메서드들이 나와있다. 이러한 메서드를 여러분이 오버라이드해서 사용할 수 있는데, 자세한 내용은 다음 절애서 셜명.

###### \_\_str\_\_() (python3)

모델 객체가 문자열로 표현되어야 하는 경우에 호출. admin이나 console에서 많이 쓰이게 됨

기본 구현은 아무 도움이 되지 않는 문자열을 리턴하기 때문에, 모든 모델에 대해 오버라이드 해서 알맞게 구현해주는게 좋음

###### get_absolute_url()

이 메서드는 장고가 해당 모델 객체의 URL을 계산할 수 있도록 함. 장고는 이 메서드를 모델 객체를 URL로 표현하는 경우에 사용. admin 사이트에서 사용..

모델 객체가 유일한 URL을 가지는 경우에는 이 메서드를 구현해주어야 함.



##### Overriding predefined model methods

커스터마이징 할 데이터베이스 동작을 캡슐화하는 또 다른 모델 메서드 집합이 있음. 특히 `save()` 및 `delete()` 의 작업방식을 바꾸는 경우가 많음. 동작을 바꾸기위해 이 메서드들을 마음껏 오버라이드할 수 있음.

내장된 메서드를 재정의하는 일반적인 사용 사례는 객체를 저장할 때마다 어떤 작업을 수행하기를 원할 때. 

받아들이는 매개변수에 대해서는 save() 문서 참조(https://docs.djangoproject.com/en/1.11/ref/models/instances/#django.db.models.Model.save)

```python
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    
    def save(self, *args, **kwargs):
        do_something()
        super(Blog, self).save(*args, **kwargs) # Call the "real" save() method
```

저장을 막을 수도 있다.

```python
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    
    def save(self, *args, **kwargs):
        if self.name == "Yoko Ono's blog":
            retrun # Yoko shall never have her own blog!
        else:
            super(Blog, self).save(*srg, **kwargs) # Call the "real" save() method.
```

슈퍼 클래스 메서드를 호출하는 것을 기억하는 것이 중요 

super(Blog, self).save(*args, **kwargs)를 말한다.

이는 객체가 데이터베이스에 저장되도록 한다.

수퍼 클래스 메서드를 호출하는 것을 잊어버리면 기본 동작이 실행되지 않으며 데이터베이스에 저장하지 않는다.

또한 모델 메서드에 전달할 수 있는 인수를 전달하는 것이 중요하다. 이는 `*args`와 `**kwargs` 를 사용하면 코드가 추가될 때 해당 인수를 자동으로 지원한다는 보장을 받는다

오버라이드된 모델 메서드는 `bulk operations`에서는 동작하지 않는다.

QuerySet을 사용하여 대량으로 객체를 삭제할 때 또는 계단식 삭제의 결과로 객체의 delete() 메서드가 반드시 호출되지 않을 수 있다. 사용자 정의 삭제 논리를 실행하려면 `pre_delete`와 `post_delete` 시그널을 사용할 수 있다. 

불행하게도 `bulk operations`에서는 `save()` 메서드와 `pre_save` 및 `post_save` 시그널이 호출되지 않기 때문에 객체를 대량으로 만들거나 업데이트할 때 해결방법이 없다.

##### Executing custom SQL

또 다른 공통 패턴은 모델 메서드 및 모듈 수준 메서드에서 사용자 지정 SQL 문을 작성하는 것이다. 원시 SQL 사용에 대한 자세한 정보는 using raw SQL 문서를 참조.(https://docs.djangoproject.com/en/2.0/topics/db/sql/)



#### Model inheritance

`Django`의 모델 상속은 파이썬에서 일반적인 클래스 상속이 작동하는 방식과 거의 동일하게 작동하지만 반드시 따라야하는 기본 사항이 있다. 기본 클래스가 `djnago.db.models.Model`을 상속받아야 한다.

부모 모델이 자체 데이터베이스 테이블을 가지는 모델이 될지, 또는 부모가 자식 모델에게 전달할 정보만을 가지고 있는지 여부만 결정하면 된다.

`Django`에서는 세가지 스타일의 상속을 제공한다.

1. 흔히 부모 클래스를 사용하여 각 하위 모델에 대히 일일이 입력하지 않으려는 정보를 제공하는 경우이다. 이 클래스는 따로 분리하여 사용하지 않으므로 추상 기본 클래스(Abstract base classes).를 사용한다.
2. 기존 모델을 하위 클래스화(다른 애플리케이션의 모델이어도 무관)하고, 각 모델이 자체 데이터베이스 테이블을 가지기 원한다면 다중 테이블 상속(Multi table inheritance)이 필요하다.
3. 마지막으로 모델 필드를 변경하지 않고 모델의 파이썬 수준 동작만 수정하려는 경우 `Proxy` 모델을 사용할 수 있다.

##### Abstact base classes

추상 기본 클래스는 몇가지 공통된 정보를 여러 다른 모델에 넣으려 할 때 유용하다. 기본 클래스를 작성하고 `Meta` class에 `abstract = True`를 넣는다. 이 모델은 데이터베이스 테이블을 만드는 데 사용되지 않는다. 대신 다른 모델의 기본 클래스로 사용될 때 해당 필드는 자식 클래스의 필드에 추가된다. 자식의 이름과 같은 이름(상속받은 클래스의 이름과 같은 이름의 필드)을 가진 추상 기본 클래스의 필드를 갖는 것은 오류이며, `Django`는 이에 대해 오류를 발생시킨다.

예시

``` python
from django.db import models

class CommonInfo(models.Model):
    name = models.Charfield(max_length=100)
    age = models.PositiveIntegerField()
    
    class Meta:
        abstract = True
        
class Student(commonInfo):
    home_group = models.CharField(max_length=5)
```

`Student` 모델에는 `name`, `age` 및 `home_group`의 세가지 필드가 있다. `CommonInfo` 모델은 `abstract base class`이기 때문에 일반 `Django` 모델로 사용할 수 없다. 이 모델은 데이터베이스 테이블을 생성하지 않으며 `Manager`을 가지지 않으므로 직접 인스턴스화하거나 저장할 수 없다

많은 경우, 이 유형의 모델 상속이 일반적이다. 그것은 파이썬 레벨에서 공통 정보를 제외시키는 방법을 제공하면서 데이터베이스 레벨에서 하위 모델 당 하나의 데이터베이스 테이블만 생성한다.

##### Meta inheritance

추상 기본 클래스가 생성되면 Django는 기본 클래스에서 선언한 `Meta` 내부 클래스를 속성으로 사용할 수 있게 한다. 자식 클래스가 자신의 메타 클래스를 선언하지 않으면 부모 클래스의 메타를 상속받는다. 자식이 부모의 `Meta`클래스를 확장하려고 하면 해당 클래스를 서브 클래스로 사용할 수 있다.

예시

```python
from django.db import models

class CommonInfo(models.Model):
    #...
    class Meta:
        abstract = True
        ordering = ['name']
        
class Student(CommonInfo):
    #...
    class Meta(CommonInfo.Meta):
        db_table = 'student_info'
```

`Django`는 추상 기본 클래스의 `Meta`클래스를 조정한다. `Meta` 속성을 적용하기 전에 `abstract` 속성 값을 `False`로 설정한다. 즉, 추상 기본 클래스의 자식은 자동으로 추상클래스가 되지 않는다. 물론 다른 추상 기본 클래스에서 상속받은 추상 기본 클래스를 만들 수 있다. 매번 `abstract = True`를 명시적으로 설정하는 것을 기억하면 된다.

일부 속성은 추상 기본 클래스의 `Meta`클래스에 포함하는 것이 타당하지 않다. 예를 들어, `db_table`을 포함하는 것은 모든 자식 클래스(자신의 메타를 지정하지 않은 클래스)가 동일한 데이터베이스 테이블을 사용한다는 것을 의미한다. 이는 대부분의 경우 원하지 않는 동작이다.

##### Be careful with related_name and related_query_name

ForeignKey 또는 ManyToManyField에서 related_name 또는 related_query_name을 사용하는 경우 필드의 고유한 역 이름(reverse name)과 쿼리 이름(query name)을 항상 지정해야 합니다. 이 필드들(ForeignKey, ManyToManyField)을 가진 추상 기본 클래스를 상속받은 경우 매번 해당 속성(rlated_name 또는 related_query_name)에 대해 정확히 동일한 값이 사용되므로 일반적으로 문제가 발생합니다.

이 문제를 해결하려면 추상 기본 클래스에서 related_name 또는 related_query_name을 사용할 때 값의 일부에 '%(app_label)s' 및 '%(class)s'를 포함해야 합니다.

- '%(class)s'는 필드가 사용되는 하위 클래스의 lower-cased 이름으로 대체된다.
- '%(app_label)s'는 하위 클래스가 포함된 애플리케이션 이름의 lower-cased 이름으로 바뀐다. 설치된 각 응용 프로그램 이름은 고유해야하며 각 응용 프로그램 내의 모델 클래스 이름도 고유해야하므로 결과 이름이 달라진다.

모델 예제 `common/models,py`

```python
from django.db import models

class Base(models.Model):
    m2m = models.ManyToManyField(
    OtherModel,
    related_name="%(app_label)s_%(class)s_related",
    related_query_name="%(app_label)s_%(class)ss",
    )
    
    class Meta:
        abstract = True
     
class ChildA(Base):
    pass

class ChildB(Base):
    pass
```

다른 모델 예제 `rare/models.py`:

```python
from common.models import Base

class Childb(Base):
pass
```

<strong>common.ChildA.m2m</strong> 필드의 <strong>reverse name</strong>은 <strong>common_childa_related</strong>이고,  <strong>reverse query name</strong>은 <strong>common_childas</strong>이다.

<strong>common.ChildB.m2m</strong> 필드의 <strong>reverse name</strong>은 <strong>common_childb_related</strong>이고,  <strong>reverse query name</strong>은 <strong>common_childbs</strong>이다.

마지막으로 <strong>rare.ChildB.m2m</strong> 필드의 <strong>reverse name</strong>은 <strong>rare_childb_related</strong>이고,  <strong>reverse query name</strong>은 <strong>rare_childbs</strong>이다. <strong>'%(class)s'</strong> 및 <strong>'%(app_lab)s'</strong>를 사용하여 관련 이름 또는 관련 검색어 이름을 작성하는 방법은 사용자에게 달렸지만, 사용하는 것을 잊을 경우 Django는 시스템 검사를 수행할 때 오류를 발생시킨다.(또는 마이크레이션을 실행할때)

추상 기본 클래스 필드에 <strong>related_name</strong> 속성을 지정하지 않으면 상속받은 자식 클래스의 기본 <strong>reverse name</strong>은 필드를 직접 선언한 경우와 마찬가지로 <strong>'_set'</strong>이 뒤에 오는 자식 클래스의 이름이 된다. 예를 들어, 위 코드에서 <strong>related_name</strong> 속성을 생략하면 <strong>m2m</strong> 필드의 <strong>reverse name</strong>은 <strong>ChildA</strong>의 경우 <strong>childa_set</strong>이 되고 <strong>ChildB</strong> 필드의 경우 <strong>childeb_set</strong>이 된다.



#### Multi-table inheritance

Django가 지원하는 모델 상속의 두번째 유형은 계층 구조의 각 모델이 모두 각각 자신을 나타내는 모델이다. 각 모델은 자체 데이터베이스 테이블에 해당하며 개별적으로 쿼리하고 생성할 수 있다. 상속관계는 자동으로 생성된 OneToOneField를 통해 자신 모델과 부모 간의 링크를 만든다.

예시

```python
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    
class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
```

Place의 모든 필드는 Restaurant에서 사용할 수 있지만 데이터는 다른 데이터베이스 테이블에 있다. 그래서 아래 두 명령 모두 가능하다.

```python
Place.objects.filter(name="Bob's Cafe")
Restaurant.objects.filter(name="Bob's Cafe")
```

Restaurant 이면서 Place가 있는 경우, 모델 이름의 소문자 버전을 사용하여 Place객체에서 Restaurant 객체를 가져올 수 있다.

```python
p = Place.objects.get(id=12)
# If p is a Restaurant object, this will give the child class:
p.restaurant
<Restaurant: ...>
```

그러나 위 예제의 p가 Restaurant이 아닌 경우(즉, Place 객체로 직접 작성되었거나 다른 클래스의 부모인 경우) p.restaurant를 참조하면 Restaurant.DoesNotExist 예외가 발생한다.

Restaurant에 자동으로 생성된 OneToPneField는 다음과 같은 형태를 가진다.

```python
place_ptr = models.OneToOneField(
	Place, on_delete=models.CASCADE,
	parent_link=True,
)
```

Restaurant 에서 parent_link=True를 사용해 자신의 OneToOneField를 선언하여 해당 필드를 재정의할 수 있다.

##### Meta and multi-table inheritance

다중 테이블 상속 상황에서 자식 클래스가 부모의 <eta 클래스에서 상속받는 것은 의미가 없다. 모든 메타 옵션은 이미 상위 클래스에 적용되었고 다시 적용하면 모순된 행동만 발생한다.(기본 클래스가 자체적으로 존재하지 않는 추상 기본 클래스의 경우와 대조적이다.)

따라서 자식 모델은 부모의 메타 클래스에 액세스할 수 없다. 그러나 자식이 부모로부터 동작을 상속하는 몇 가지 제한된 경우가 있다. 자식이 ordering 특성이나 get_latest_by 특성을 지정하지 않으면 해당 특성을 부모로부터 상속한다.

부모가 ordering되어 있고 이를 해제하려면 명시적으로 사용을 중지할 수 있다.

```python
class ChildModel(ParentModel):
	#...
	class Meta:
	# Remove parent's ordering effect
	ordering = []
```

##### Inheritance and reverse relations

다중 테이블 상속은 암시적으로 OneToOneField를 사용하여 부모와 자식을 연결하기 때문에 위의 예와 같이 상위에서 하위로 이동할 수 있다. 그러나 이 경우 related-name의 값으로 ForeignKey 및 ManyToManyField 관계에 대한 기본 값을 사용한다. 이러한 과계 유형들을 부모 모델의 하위 클래스에 배치하는 경우 해당 필드 각각에 반드시 related_name속성을 지정해야 한다. 이를 잊어버리면 Django는 유효성 검사 오류를 발생시킨다.

예를 들어 위의 Place 클래스에서 ManyToManyField를 사용하는 다른 하위 클래스를 만들어보자.

 ```python
class Supplier(Place):
	customers = models.ManyToManyField(Place)
 ```

결과는 다음과 같은 에러를 나타낸다.

```python
Reverse query name for 'Supplier.customers' clashes with reverse query
name for 'Supplier.place_ptr'.

HINT: Add or change a related_name argument to the definitionfor
'Supplier.customers' or 'Supplier.place_ptr'.
```

customers_name 필드에 related_name을 추가하면 models.ManyToManyField(Place, related_name='provider'에서 발생한 오류가 해결된다.

##### Specifying the parent link field

앞서 언급했든이 Django는 자동적으로 자식 클래스를 임의의 추상이 아닌 부모 모델에 연결하는 OneToOneField를 만든다. 부모에게 다시 연결되는 속성의 이름을 제어하려는 경우 고유한 OneToOneField를 만들고 parent_link=True로 설정하여 해당 필드가 부모 클래스에 대한 링크임을 나타낼 수 있다.

