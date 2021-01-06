# Information

- 최초 작성: 최진혁
- 최초 작성일: 2020-01-04
- [참고 문서](https://b.luavis.kr/python/python-convention)

# Coding Convention

1. 들여쓰기
   - 공백 4개
   - Tab 사용 금지
   - Python 실행 시 -tt 옵션 사용

1. Import
   - Import 순서
     1. 표준 라이브러리
     1. 관련 서드파티 라이브러리
     1. 로컬 어플리케이션 / 자체 라이브러리
   - Import 구분
     - 권장: import os import sys
     - 라이브러리 분류 별 개행
   - 예시

     ```
     # Std Library
     import os
     import sys

     # 3rd Library
     import numpy
     import pandas

     # Project Library
     import test
     import cuostom_agent
     ```

1. Pet Peeves
   1. 괄호, 중괄호, 대괄호 내부에 연결되는 부분
      - 권장: spam(ham[1], {eggs: 2})
   1. 콤마, 세미콜론, 콜론의 이전 위치
      - 권장: if x == 4: print x, y; x, y = y, x
   1. 함수 호출시 인수 목록이 시작되는 괄호의 바로 이전 위치
      - 권장: spam(1)
   1. 인덱싱 혹은 슬라이싱이 시작되는 괄호의 바로 이전 위치
      - 권장: dict['key'] = list[index]
   1. 할당(혹은 기타 다른) 연산자 주변에 한 개를 초과하는 공백 문자가 있는 경우
      - 권장
        ```
        x = 1
        y = 2
        long_variable = 3
        ```

1. 명명 규칙
   1. 패키지와 모듈명
      - lower_case_with_underscores #ex: test_file
   1. Class명
      - CamelCase (ex: TestClass)
   1. 함수명
      - lower_case_with_underscores #ex: test_function()
   1. 함수 선언
      - 인스턴스 메서드는 첫 번째 인수 self 사용
      - 클래스 메서드는 @classmethod를 위에 붙인 뒤<br>첫 번째 인수 cls 사용
      - 정적 메서드는 @staticmethod를 위에 붙인 뒤<br>첫 번째 인수 없음
   1. 변수명
      - lower_case_with_underscores #ex: car_handle = 1
   1. 내부 패키지, 내부 모듈 , private
      - 맨 앞에 \_ 언더스코어 문자를 붙힘 #ex: \_check
   1. 전역 변수
      - 전체 대문자 사용 필요시 \_ 언더스코어 사용 #ex: MAX_COUNT

1. 기타 권고
   - 항상 이진 연산자의 주위에는 한 개의 공백을 넣는다: 할당 (=), 증감 할당 ( +=, -= 등.), 비교 (==, <, >, !=, <>, <=, >=, in, not in, is, is not), 부울 연산 (and, or, not)
   - 우선 순위가 서로 다른 연산자를 함께 사용할 경우, 우선 순위가 낮은 연산자 주위에 공백을 넣을지 고려해보자. 하지만 이 경우에도 한 개 를 초과하는 공백 문자를 사용하면 안 되며, 이진 연산자의 양쪽을 똑 같은 방식으로 기술하도록 한다.
   - 권장
     ```
     i = i + 1
     submitted += 1
     x = x*2 - 1
     hypot2 = x*x + y*y
     c = (a+b) * (a-b)
     ```
    - 데이터 비교시 소문자 권장

# 로그 규칙

1. 로그 레벨
    - DEBUG < INFO < WARNING < ERROR < CRITICAL

# 버전 관리

- 각 프로젝트 별 README 참고
