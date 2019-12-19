# 19.11.04 Python Class 05
"""
명시적 형 변환(Casting) : int(), float(), str()
"""
# print('3.1' + 1.2) # 에러. string과 float는 연산 불가.
print(float('3.1') + 1.2) # 정상 실행. float형으로 변환 후, 연산 실행. 결과 4.3
print('3.1' + str(1.2)) # 정상 실행. str형으로 변환 후, 문자열을 이어 붙힘. 결과 3.11.2

x = input('plz input number X >>>')
y = input('plz input number Y >>>')
print(x + y)
# 결과 1.22.3
# 1.2와 2.3을 이어 붙힐뿐, 산술 연산은 되지 않는다. (사용자에게 input 받은 것은 문자열 취급)

x = float(x)
y = float(y)
# 문자열을 실수형으로 변환
print(x + y)
# 결과 3.5
print(f'{x} + {y} = {x + y}')
print(f'{x} - {y} = {x - y}')
print(f'{x} * {y} = {x * y}')
print(f'{x} / {y} = {x / y}')

