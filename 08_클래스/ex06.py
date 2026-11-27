import math

class Circle:

    # @property : 해당 변수를 데코레이터 기능을 사용할 변수로 지정
    #           - getter, setter 로 사용 가능
    #           - @property 로 지정한 변수는 객체.변수 형태로 접근 가능
    #           - 실제 데이터는 __radius 와 같은 형태의 private 변수에 저장

    @property
    def radius(self):
        return self.__radius

    # @변수.setter : 해당 메소드를 setter 메소드로 지정
    #               - 객체.변수 = 값 형태로 값을 대입할 때 실행
    #               - 전달받은 값(value)이 유효한지 검사 가능
    #               - 반지름이 0 이하인 경우 0을 저장하도록 처리

    @radius.setter
    def radius(self, value):

        # 반지름은 양수이어야 하므로 0 이하인지 검사
        if value <= 0:
            print('반지름은 양수이어야합니다.')

            # 잘못된 값이 전달되면 반지름을 0으로 설정
            self.__radius = 0
            return

        # 유효한 값이면 private 변수에 저장
        self.__radius = value

    # @변수.getter : 해당 메소드를 getter 메소드로 지정
    #               - 객체.변수 형태로 접근할 때 실행
    #               - 지정한 getter 메소드가 호출되어 값을 반환
    #               - 여기서는 __radius 에 저장된 반지름 값을 반환

    @radius.getter
    def radius(self):
        return self.__radius


# Circle 클래스의 객체 생성
circle = Circle()

# setter 메소드를 통해 반지름 값 지정
# - 전달한 값이 -10이므로 setter 내부의 유효성 검사 실행
# - 0 이하이므로 __radius 에 0 저장
circle.radius = -10

# getter 메소드를 통해 반지름 값에 접근
# - 객체.radius 형태로 접근하면 getter 메소드 실행
print('circle - radius : {}'.format(circle.radius))