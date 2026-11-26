price = 15000
seats = [    
  [0, 0, 0, 0, 0, 0],    
  [0, 0, 0, 0, 0, 0],    
  [0, 0, 0, 0, 0, 0],    
  [0, 0, 0, 0, 0, 0],    
  [0, 0, 0, 0, 0, 0]
]

# 좌석 상태 출력
def show_seats(seats):
  for rows in seats:
    for col in rows:
      print(col, end=' ')
    print()

# 좌석 예약 확인
def check_seat(seats, row, col):
  # try:
  #   seat = seats[row-1][col-1]
  # except IndexError:
  #   print('존재하지 않은 자리입니다.')
  #   return False

  # 좌석 범위 바깥을 접근할 수 없다.
  if (row < 1 or row > 5) or (col < 1 or col > 6):
    print('존재하지 않은 자리입니다.')
    return False

  seat = seats[row-1][col-1]
    
  if seat == 0:
    print("이용가능한 자리입니다.")
    return True
  else:
    print("이미 예약된 자리입니다.")
    return False

# 예약 처리
def reserve_seat(seats, row, col):
  try:
      seats[row-1][col-1] = 1
  except IndexError:
    print('존재하지 않은 자리입니다.')


# 금액 계산
def calculate_price(row, col, age):
  ticket_price = price

  # 나이 13세 이하, 30% 할인
  if age <= 13:
    ticket_price = ticket_price * (1 - 0.3)

  # 나이 65세 이상, 20% 할인
  if age >= 65:
    ticket_price = ticket_price * (1 - 0.2)

  # 자리 첫행, 마지막
  if row == 1 or row == len(seats):
    ticket_price = ticket_price - 2000

  return ticket_price

def make_reservation(seats, row, col, age):
  # 좌석확인
  if not check_seat(seats, row, col):
    return None

  # 예약처리
  reserve_seat(seats, row, col)

  # 요금계산
  ticket_price = calculate_price(row, col, age)

  return ticket_price


show_seats(seats)

row = int( input('행 : ') )
col = int( input('열 : ') )
age = int( input('나이 : ') )

price = make_reservation(seats, row, col, age)

if price is not None:    
  print(f"결제 금액: {price:,}원")
  show_seats(seats)