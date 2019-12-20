from dataclasses import dataclass

@dataclass
class Webtoon:
    # 이 클래스에서 공통적으로 사용할 변수는 클래스 변수로 선언
    URL_WEBTOON_LIST = 'http://comic.naver.com/webtoon/weekday.nhn'
    URL_EPISODE_LIST = 'https://comic.naver.com/webtoon/list.nhn?titleId={id}'
    WEBTOON_LIST_HTML = None

    id: str
    url_thumbnail: str
    title: str

    def __post_init__(self):
        self.author = None
        self.description = None
        self.genres = None
        self.age = None

    def __repr__(self):
        # 객체의 표현값
        return f'Webtoon({self.title}, {self.id})'

    def get_detail_info(self):
        # 자신의 author, description, genres, age 값을 채운다.
        url = self.link
        response = requests.get(url)                                                    l.....................,, ,,,,,,,,,,,