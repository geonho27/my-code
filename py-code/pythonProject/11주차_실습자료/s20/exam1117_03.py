from c11.s10.exam1117_function import get_file_to_lines, text_full
import matplotlib.pyplot as plt

file_name = '지하철_시간대별_이용현황.csv'
result = get_file_to_lines(file_name, 2)

header = result['header']
data = result['data']

data_chart = []

for data_row in data:
    data_row[4:-1] = list(map(int, data_row[4:-1]))

    #data_row[10] #7시대의 승차인원수
    #data_row[12] #8시대의 승차인원수
    #data_row[14] #9시대의 승차인원수
    #data_sum = data_row[10] + data_row[12] + data_row[14]
    data_sum = sum(data_row[10:15:2])

    data_chart.append(data_sum)

data_chart_x = range(len(data_chart))

data_chart.sort()

plt.bar(data_chart_x, data_chart)
plt.show()








