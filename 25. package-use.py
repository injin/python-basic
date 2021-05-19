# import 뒤에는 모듈, 패키지만 가능. 함수 X
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


from travel import *
# trip_to = vietnam.VietnamPackage() #__init__에 없어서 안됨
trip_to = thailand.ThailandPackage()
trip_to.detail()


import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))

