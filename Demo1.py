import numpy as np
import scipy.linalg as la

# def gaussian(x, mu, sig):
#     return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
#
# x_values = np.linspace(-3, 3, 120)
# for mu, sig in [(-1, 1), (0, 2), (2, 3)]:
#     mp.plot(x_values, gaussian(x_values, mu, sig))
#
# mp.show()

def mat_guassianelimination(A):
    R = numpy.lu(A, permute_l=True)
    return R

def matrix_mul(A,B):
    R = A.dot(B)
    return R

def matrix_inverse(A):
   R = np.linalg.inv(A)
   return  R

def matrix_eigenvals(A) :
    R= np.linalg.eigvals(A)
    return  R

def matrix_eigenvector(A) :
    R= np.linalg.eig(A)
    return  R

def matrix_rank(B):
    R= np.linalg.matrix_rank(B)
    return

def matrix_det(A):
    R= np.linalg.det(A)
    return R

def matrix_columnspace(A):
    R= np.linalg.qr(A)
    return R


if __name__ == '__main__':
 input = '2F(K+2) = 6F(k+1)+ 4F(K)'
 splitinput=[item.strip() for item in input.split('=')]
rhs=splitinput[1]
print(rhs)
# split rhs and get find min value of k.
splitrhs=[item.strip() for item in rhs.split(')+')]
print(len(splitrhs))


 # A = [1, -3, 3, 4, 5, 6, 7, 8, 5]
 # B = [6, 1, 1, 4, -2, 5, 2, 8, 7]
 # A = np.array(A).reshape((3, 3))
 # B = np.array(B).reshape((3, 3))
 #
 # _inverse = matrix_inverse(A)
 # _product = matrix_mul(A, B)
 #
 # _rank = matrix_rank(A)
 # _determinant=matrix_det(A)
 #
 # _eignVal = matrix_eigenvals(A)
 # _eignenvector= matrix_eigenvector(A)
 #
 # _columnspace= matrix_columnspace(B)
 #
 #
 # print  ('Matrix')
 # print(A)
 # print ('Eigen Values')
 # print (_eignVal)
 # print ('Inverse of Matrix A')
 # print (_inverse)
 # print ('Product of Matrix -- here A*B')
 # print (_product)
 # print ('Rank  of Matrix A')
 # print (_rank)
 # print('Determinant of Matrix A')
 # print(_determinant)
 # print('Eignen Vector of A')
 # print(_eignenvector)
 # print ('Column Space of A')
 # print (_columnspace)