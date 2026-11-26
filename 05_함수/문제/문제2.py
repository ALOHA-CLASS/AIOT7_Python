products = {    
  "사과": {"price": 1500, "stock": 10},
  "우유": {"price": 2500, "stock": 5},
  "라면": {"price": 1200, "stock": 20},
  "빵": {"price": 2000, "stock": 8},
  "콜라": {"price": 1800, "stock": 12}
}

order = {    
  "사과": 3,    
  "우유": 2,    
  "라면": 5,    
  "콜라": 2
}

# 상품 출력
def show_products(products):
  print('상품명\t| 가격\t| 재고')
  print('-----------------------')
  for name, info in products.items():
    print(' {} \t'.format(name), end='')
    print(" {} \t".format(info['price']), end='')
    print(" {} \t".format(info['stock']))

# 상품명으로 상품이 등록되었는지 확인
def check_product(products, name):
  if products[name] is None:
    print('해당 상품은 존재하지 않습니다.')
    return False

  print('상품 확인!')
  return True

# 요청한 수량 만큼 재고있는지 확인
def check_stock(products, name, quantity):
  if not check_product(products, name):
    return False

  product = products[name]
  stock = product['stock']
  # 재고 < 요청수량
  if stock < quantity:
    print('요청한 수량보다 재고가 부족합니다.')
    print('부족한 수량 : {}'.format( quantity - stock ))
    return False
  else:
    print('요청한 수량이상 재고가 존재합니다.')
    print('재고 : {}'.format( stock ))
    return True

  
# 재고 차감
def update_stock(products, name, quantity):
  if not check_product(products, name):
    return

  product = products[name]
  product['stock'] -= quantity
  print('재고를 {}건 차감하고, {}건 남았습니다.'.format(quantity, product['stock']))


 # 총 주문 금액 계산
def calculate_total(products, order):
  total = 0
  for name, quantity in order.items():
    # 단가 x 개수 = 가격
    product = products[name]
    # 사과 1000원 x 3개 = 3000
    price = product['price'] * quantity
    # 총 주문 금액에 누적
    total += price

  return total
  
# 구매 금액에 따라 지정된 할인율을 반환
def calculate_discount(total):
  if total >= 50000:
    return 0.1
  elif total >= 30000:
    return 0.05
  elif total >= 10000:
    return 0.02
  else:
    return 0
  
# 주문 전체 처리
def process_order(products, order):
  for name, quantity in order.items():
    result1 = check_product(products, name)
    result2 = check_stock(products, name, quantity)
    if not result1 or  not result2:
      print('주문을 진행할 수 없습니다.')
      return

  # 주문 진행 가능
  total = calculate_total(products, order)
  rate = calculate_discount(total)
  discount = total * rate
  payment = total - discount

  # 재고 차감
  for name, quantity in order.items():
    update_stock(products, name, quantity)

  # 주문 결과
  result = { 
    'total' : total, 
    'discount' : discount, 
    'payment' : payment 
  }
  return result



### 
result = process_order(products, order)

if result:    
  print("주문이 완료되었습니다.")    
  print(f"주문 금액: {result['total']:,}원")    
  print(f"할인 금액: {result['discount']:,}원")    
  print(f"최종 결제 금액: {result['payment']:,}원")
  show_products(products)