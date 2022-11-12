numm = 0
carryy = 0



def andGate(int1, int2):
    equals = 0
    if int1 == 1 and int2 == 1:
        equals = 1
        return equals
    return equals


def notGate(int1):
    equals = 0
    if int1 == 1:
        equals = 0
    else:
        equals = 1
    return equals

def nandGate(int1, int2):
    equals = notGate(andGate(int1, int2))
    return equals

def orGate(int1, int2):
    int_1 = notGate(int1)
    int_2 = notGate(int2)
    equals = nandGate(int_1, int_2)
    return equals

def xorGate(int1, int2):
    int_1 = orGate(int1, int2)
    int_2 = nandGate(int1, int2)
    equals = andGate(int_1, int_2)
    return equals

def adder(int1, int2, int3):
    global numm
    global carryy
    int_1 = andGate(int1, int2)
    int_2 = xorGate(int1, int2)
    int_3 = andGate(int_2, int3)
    carryy = orGate(int_3, int_1)
    numm = xorGate(int3, int_2)
    return numm
    

def fourBit(int11, int12, int13, int14, int21, int22, int23, int24):
    global numm
    global carryy
    num1 = adder(int11, int21, carryy)
    num2 = adder(int12, int22, carryy)
    num3 = adder(int13, int23, carryy)
    num4 = adder(int14, int24, carryy)
    print(f'{num1} {num2} {num3} {num4} [{carryy}]')

    

# enter two numbers in binery 
fourBit(1,1,1,1     ,1,0,0,0)
