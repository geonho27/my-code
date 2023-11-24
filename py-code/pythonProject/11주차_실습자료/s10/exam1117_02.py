from exam1117_function import get_file_to_lines, text_full
import matplotlib.pyplot as plt

file_name = '2023년 10월  교통카드 통계자료.csv'
result = get_file_to_lines(file_name)

header = result['header']
data = result['data']

# 데이터 초기 가공!!!
for data_row in data:
    for i in range(4, 8):
        data_row[i] = int(data_row[i])

#모든 역의 유무임 승하차 비율
max_type = ['유임승차', '유임하차', '무임승차', '무임하차']
colors = ['#ff0000', '#00ff00', '#0000ff', '#ff00ff']

plt.rc('font', family='Malgun Gothic')

for data_row in data:
    line = data_row[1]
    station = data_row[3]
    val_data = data_row[4:8] #유임승차수,유임하차수,무임승차수,무임하차수

    save_file_name = f'./pie/{line}-{station}.png'
    
    plt.title(f'{line} - {station} 유무임 승하차 비율')
    plt.pie(val_data, labels=max_type, colors=colors, autopct='%1.f%%')
    plt.legend()
    plt.savefig(save_file_name)
    plt.show()





