from c11.s10.exam1117_function import get_file_to_lines, text_full
import matplotlib.pyplot as plt

file_name = '지하철_시간대별_이용현황.csv'
result = get_file_to_lines(file_name, 2)

header = result['header']
data = result['data']

#출근시간대(7~9대)에 승차인원이 가장 많은 역은?

max_sum_val = 0
max_line = ''
max_station = ''

for data_row in data:
    data_row[4:-1] = list(map(int, data_row[4:-1]))
    data_sum = sum(data_row[10:15:2])
    line = data_row[1]
    station = data_row[3]

    if data_sum > max_sum_val:
        max_sum_val = data_sum
        max_line = line
        max_station = station

print(f'{max_line} {max_station} {max_sum_val:>15,}')








