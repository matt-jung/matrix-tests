def matrix_multiplication(A,B):
    """
    Multiplies two matrices inputed as nested arrays

    Args:
        A,B (array): Matrices given as nested arrays

    Returns:
        AB (array): Matrix product of A and B

    Raises:
        ValueError: If dimensions of A and B are incompatible for matrix multiplication.

    Notes:
        -AB does not necessarily equal BA
    """
    if len(A[0])!=len(B):
        raise ValueError('Matrix dimensions are incompatible. Number of columns in A must equal number of rows in B.')

    AB = [[0 for x in range(len(B[0]))] for x in range(len(A))]

    for j in range(len(B[0])):    
        for i in range(len(A)):
            for k in range(len(B)):
                AB[i][j]+=A[i][k]*B[k][j]
    return AB



def hermitian_conjugate(A):
    """
    Outputs the hermitian conjugate of a matrix

    Args:
        A (array): Matrix given as nested arrays

    Returns:
        A_dagger (array): Hermitian conjugate of matrix A

    """
    rows=len(A)
    columns=len(A[0])

    #Create blank matrix of opposite dimensions:

    A_dagger=[[0 for x in range(rows)] for x in range(columns)]

    for i in range(rows):
        for j in range(columns):
            A_dagger[j][i]=complex(A[i][j].real,-A[i][j].imag)
    
    return A_dagger



def is_unitary(A):
    """
    Determines whether a given square matrix is unitary.

    Args:
        A (array): Matrix given as a nested array

    Returns:
        unitary (bool): Truth statues of whether the given matrix is unitary

    Raises:
        TypeError: If input matrix is not square.

    """
    if len(A)!=len(A[0]):
        raise TypeError('Input must be a square matrix. Only square matrices can be unitary.')

    import numpy as np  
    unitary=True
    identity_matrix=np.identity(len(A))

    for i in range(len(A)):
        for j in range(len(A[0])):
            if matrix_multiplication(A,hermitian_conjugate(A))[i][j]!=identity_matrix[i][j]:
                unitary=False
    return unitary