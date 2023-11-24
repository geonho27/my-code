
def calc_data(value):
    return value * 2 + 1
#end-def

list_1 = ['1', '2', '3', '4']
#각각의 데이터에 특정함수(값에 2배를 하고 1을 더하는 함수)를 호출한 결과의 값으로

#list_2 = [1, 2, 3, 4]
#list_3 = [3, 5, 7, 9]
'''
list_3 = []
for i in list_1:
    tmp = int(i)
    tmp_2 = calc_data(tmp)
    list_3.append(tmp_2)
print(list_3)
'''

list_3 = list(map(calc_data, list(map(int, list_1))))
print(list_3)