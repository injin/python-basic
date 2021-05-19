#import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조할인 영화 보러 갔을 때
# theater_module.price_solder(5) # 5명의 군인이 영화 보러 갔을 때

import theater_module as mv
mv.price(3)
mv.price_morning(4)

from theater_module import *
price(3)
price_soldier(5)


from theater_module import price, price_morning
price(5)


from theater_module import price_soldier as price
price(4)