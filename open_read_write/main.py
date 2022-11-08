# test = open('test.txt', 'rt')
test = open('test.txt')

# with open('test.txt', 'rt') as test:

# Print all file in one str
# result = test.read()
# print(f'Содержание файла: {result}')

# Read one str. с каждым вызовом readline печатается следующая строка
# result = test.readline()
# result1 = test.readline()
# result2 = test.readline()
# result3 = test.readline()
# print(f'You results: {result3}')

# Readlines выводит список, можно обращатсья по индексу [..]
# result = test.readlines()
# print(f'вывод инфы: {result}')
# print(result[1])

# for line in test:
#     print(line)
#
#
# test.close()

# with open('new/file2.txt', 'wt') as test:
    # при записи первой строки и после по новой выполняя вторую строку, происходит перезапись в файле
    # test.write('what are you doing?')
    # test.write('everything clear\n')
    # test.write('the good result')

    # Запись нескольких строчек
    # test.writelines(['line1\n', 'line2\n'])

#режим at позволяет сохранять и дописывать в файл
# with open('new/file2.txt', 'at') as test:
#     test.writelines(['new1\n', 'new2\n'])

try:
    with open('new/file2.txt', 'rt') as test:
        num = test.read()
except FileExistsError:
    num = ''