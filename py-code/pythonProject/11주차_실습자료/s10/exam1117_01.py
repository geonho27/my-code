from exam1117_function import get_file_to_lines, text_full

file_name = '2023년 10월  교통카드 통계자료.csv'
result = get_file_to_lines(file_name)

header = result['header']
data = result['data']

# 데이터 초기 가공!!!
for data_row in data:
    for i in range(4, 8):
        data_row[i] = int(data_row[i])

#유무임 승하차 인원이 가장 많은 역?

# 유임승차가 가장 많은 역?
max_type = ['유임승차', '유임하차', '무임승차', '무임하차']
max_length = len(max_type)
max_val = [0] * max_length
max_line = [''] * max_length
max_station = [''] * max_length

for data_row in data:
    line = data_row[1]
    station = data_row[3]
    val = data_row[4:8] #유임승차수,유임하차수,무임승차수,무임하차수

    for i in range(max_length):
        if val[i] > max_val[i]:
            max_val[i] = val[i]
            max_line[i] = line
            max_station[i] = station

for i in range(max_length):
    print(f'{max_type[i]} {max_line[i]:10} {text_full(max_station[i], 20)} {max_val[i]:>15,}')









