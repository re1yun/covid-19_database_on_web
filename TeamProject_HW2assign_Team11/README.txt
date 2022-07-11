python에서 mysql에 접속하는 방법은 여러가지가 있지만, 저희는 to_sql이라는 함수를 쓰기 위해서 간단한 sqlalchemy를 이용해 create_engine을 활용하여 연결했습니다.

create_engine에 mysql root의 pw는 사용자마다 다르기때문에 현재 공백으로 비워뒀습니다. (실행시키기 전에 본인의 root의 pw를 입력해야합니다.)

pandas를 사용해 csv를 읽어와 데이터프레임에 저장하였으며, loc와 iloc를 사용해서 필요한 열을 가져왔습니다.
이후 dtype을 활용해 주어진 변수 타입으로 mysql에 입력을 진행하였습니다.

이러한 방식을 사용하여 patientinfo, region, weather와 case를 입력하였습니다.

timeinfo를 만들 때에는 mysql에서 patientinfo를 읽어와 역시 pandas를 사용해 데이터프레임에 저장하고, 여기서 데이터를 추출했습니다.
먼저 additional_timeinfo.csv파일에서는 date를 읽어왔으며, patientinfo에서는 groupby를 사용해 날짜와 추가적인 조건에 맞추어 데이터를 분류했습니다.
size를 사용해서 개수를 셌으며, series로 리턴된 값을 데이터프레임으로 변환 후, 컬럼 값을 지정해줌으로써 향후 있을 merge이 원활토록 했습니다.
또한 추출된 날짜 데이터 타입이 오브젝트로 설정되어있어 이 또한 date타입으로 변환해주었습니다.

후에 'date'를 기준으로 데이터프레임들을 합쳐주고, 누적합을 계산하고 난 뒤에 앞선 상황가 동일하게 to_sql를 활용해서 데이터베이스에 입력하였습니다.

 -- 실행순서
1. 데이터베이스 & 테이블 생성
2. 파이썬 파일들을 통해 데이터들을 입력
3. 외래키를 설정
 