class Station:
    def __init__(self):
        self.line_name = ''
        self.name = ''
        self.time = ''
        self.in_count = 0
        self.out_count = 0

    def set_data(self, line_name, name, time, in_cnt, out_cnt):
        self.line_name = line_name
        self.name = name
        self.time = time
        self.in_count = in_cnt
        self.out_count = out_cnt

    def show(self):
        print(
            f'{self.time} : {self.line_name} : {self.name}, 승차:{self.in_count}, 하차:{self.out_count}')


station1 = Station()
station1.line_name = '1호선'
station1.name = '구로'
station1.time = '04:00 ~ 04:59:59'
station1.in_count = 100
station1.out_count = 200

print(f'{station1.time} : {station1.line_name} : {station1.name}, 승차:{station1.in_count}, 하차:{station1.out_count}')

line_name = '1호선'
name = '구로'
time = '04:00 ~ 04:59:59'
in_count = 100
out_count = 200

print(line_name)

