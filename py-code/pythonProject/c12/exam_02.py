from c12.data_helper import DataHelper

data_helper = DataHelper('지하철_시간대별_이용현황.csv', 2)

#header = data_helper.get_header()
#for h_row in header:
#   print(h_row)

#data = data_helper.get_data()
#for d_row in data:
#    print(d_row)


header = data_helper.get_header()
print(header[0][4:-1:2])

station_list = []
for time in header[0][4:-1:2]:
    station = Station()
    station.time = time
    station_list.append(station)


for station in station_list:
    station.show()


