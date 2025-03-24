#multiprocessing example
from multiprocessing import Process
import time

def calculate_squares(numbers):
    for number in numbers:
        print(f"Square of {number} : {number * number }")
        
def main():
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    processes = []
    start_time = time.time()

    for i in range(0, len(numbers), 2):
        process = Process(target=calculate_squares, args=(numbers[i:i+2],))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    print("Multiprocess Performance time :", end_time-start_time, "seconds")

if __name__ == "__main__":
    main()
