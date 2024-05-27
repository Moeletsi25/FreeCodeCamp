import numpy as np

#Define a function called statistics 
#if the length of the function does not contain 9 numbers it shall return 'List must contain nine numbers'
def matrix_statistics(numbers):
    if len(numbers) != 9:
        return "List must contain  nine numbers."
    
    # Convert list to a 3x3 NumPy array
    matrix = np.array(numbers).reshape(3, 3)
    
    # Calculate statistics function
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]
    }
    
    return calculations


input_list = [0,1,2,3,4,5,6,7,8]
print(matrix_statistics(input_list))
