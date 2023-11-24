import csv
import matplotlib.pyplot as plt


def get_file_to_lines(filename, header_line_count):
    csv_file = open(filename, 'r', encoding='utf-8-sig')
    csv_data = csv.reader(csv_file)

    header = []
    for i in range(header_line_count):
        header.append(next(csv_data))

    data = []
    for line in csv_data:
        data.append(line)

    csv_file.close()

    if header_line_count < 2:
        return {
            'header': header[0],
            'data': data
        }
    else:
        return {
            'header': header,
            'data': data
        }
#end-def


def text_full(text, max_length):
    text_length = 0
    for x in text:
        #print(x, ord(x))
        if ord('가') <= ord(x) <= ord('힝'):
            text_length += 2
        else:
            text_length += 1

    add_text = ''
    for i in range(max_length - text_length):
        add_text += ' '

    return text + add_text
#end-def





