import numpy as np
import scipy.linalg as la


def parseInput(inputStr):
    splitinput = []
    splitinput = [item.strip() for item in inputStr.split('=')]
    lhs = splitinput[0]
    rhs = splitinput[1]
    print(lhs)
    print(rhs)
    # get co-efficient and K state value in LHS

    LhsCoff = [item.strip() for item in lhs.split('F')]
    print(LhsCoff[1][1:4])
    if LhsCoff[0] == '':
        LCoff = int(1)
    else:
        LCoff = LhsCoff[0]
    print(LCoff)

    # split rhs and get find min value of k.
    splitrhs = []
    splitrhs = [item.strip() for item in rhs.split(' + ')]

    print(splitrhs)
    RHSCoef = []
    RHSPow = []
    for eq in splitrhs:
        coef = eq.split("F")[0]
        if coef == '':
            RHSCoef.append(1)
        else:
            RHSCoef.append(int(coef))

        pow = eq.split("F")[1][1:-1]
        print(eq)
        print(pow)

        # print(int(pow.split("+")[0]))
        # print(int(pow.split("+")[1][0]))
        if pow == 'K':
         RHSPow.append(0)
         RHSCoef = [int(x / LCoff) for x in RHSCoef]
        else:
          RHSPow.append(int(pow.split("+")[1][0]))

    # RHSCoef and RHS differential equation order.
    print(RHSCoef)
    print(RHSPow)
    # Construct the Array
    # Uk+1 = AUk
    # Creating A in the differential system.
    Matrix = np.identity(len(RHSCoef))
    # Swap Row 1 with row 2.
    # swap row 2 with row 3.
    Matrix[[0, 1]] = Matrix[[1, 0]]
    Matrix[[1, 2]] = Matrix[[2, 1]]
    # put RHSCoef to row 3 on Matrix.
    Matrix[2] = RHSCoef

    # find Eigen Values of Matrix.
    eigVal, eigVec = la.eig(Matrix)
    eigVal = eigVal.real

    for x in eigVal:
        if x > 1 or x < -1:
            return False
    return True

if __name__ == "__main__":
 inputStr = "F(K+3)=2F(K+2) + 3F(K+1) + 4F(K)"
 if parseInput(inputStr):
      print("Stable")
 else:
      print("Unstable")
