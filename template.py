import time

debug = True
file = 'sample' if debug else 'input'

# Part 1
def part_1():
    with open(file, 'r') as f:
        while line := f.readline():
            pass
    return

# Part 2
def part_2():
    with open(file, 'r') as f:
        while line := f.readline():
            pass
    return


print("Running part 1...")
part_1_start_time = time.perf_counter_ns()
answer_part_1 = part_1()
part_1_end_time = time.perf_counter_ns()

print("Running part 2...")
part_2_start_time = time.perf_counter_ns()
answer_part_2 = part_2()
part_2_end_time = time.perf_counter_ns()

time_part_1 = part_1_end_time - part_1_start_time
time_part_2 = part_2_end_time - part_2_start_time

print('-'*20)
print(f"""
Results:
    Part 1: {answer_part_1} \t\t took {time_part_1/1000}μs
    Part 2: {answer_part_2} \t\t took {time_part_2/1000}μs
""")