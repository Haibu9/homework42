import multiprocessing
import time

def read_info(name):
    all_data = []
    with open(name, 'r') as file_:
        line = file_.readline()
        all_data.append(line)

filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

# Линейный вызов

start = time.time()

for file in filenames:
    read_info(file)

finish = time.time()
print(f'Результат линейного вызова {(finish - start) * 10000}')

# Многопроцессный
# start = time.time()
# with multiprocessing.Pool():
#     map(read_info, filenames)
#
# finish = time.time()
# print(f'Результат Многопроцессного вызова {(finish - start) * 10000}')
