import multiprocessing
from timed import timed

# Define a function to be executed by each process
@timed
def worker(item):
    # Process the item
    result = item * 2
    return result

@timed
def operate():
    # Create a pool of worker processes
    with multiprocessing.Pool(processes=4) as pool:
        # Apply the worker function to a list of input values
        input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        output_values = pool.map(worker, input_values)

    # Print the results
    print("Input values:", input_values)
    print("Output values:", output_values)

if __name__ == '__main__':
    operate()