#multithreding example
import threading
import time
#function to calculate squares
def calculate_squares(numbers):
    for number in numbers:
        print(f"Squares of {number} : {number * number }")

def main():

    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    start_time = time.time()

    thread = threading.Thread(target=calculate_squares, args=(numbers, ))

    thread.start()

    thread.join()
    end_time = time.time()
    print("Multithreding Performance time is :", end_time - start_time, "seconds")

if __name__ == "__main__":
    main()

