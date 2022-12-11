import numpy as np
import Models


def Solve(systems):
    result = Models.Solutions()
    for system in systems:
        if not SingularCO(system):
            co = SolvingForCO(system)
            result.CO.append(co)
        if not SingularNO(system):
            no = SolvingForNO(system)
            result.NO.append(no)
        if not SingularNO2(system):
            no2 = SolvingForNO2(system)
            result.NO2.append(no2)
        if not SingularO3(system):
            o3 = SolvingForO3(system)
            result.O3.append(o3)
        if not SingularO3NO2(system):
            o3no2 = SolvingForO3NO2(system)
            result.O3NO2.append(o3no2)

    return result


def Solve15(systems):
    result = Models.Solutions()
    for system in systems:
        if not SingularCO15(system):
            co = SolvingForCO15(system)
            result.CO.append(co)
        if not SingularNO15(system):
            no = SolvingForNO15(system)
            result.NO.append(no)
        if not SingularNO215(system):
            no2 = SolvingForNO215(system)
            result.NO2.append(no2)
        if not SingularO315(system):
            o3 = SolvingForO315(system)
            result.O3.append(o3)
        if not SingularO3NO215(system):
            o3no2 = SolvingForO3NO215(system)
            result.O3NO2.append(o3no2)

    return result


def SingularCO(vector):
    matrix = np.array([[vector[0].CO, vector[1].CO, vector[2].CO],
                       [vector[3].CO, vector[4].CO, vector[5].CO],
                       [vector[6].CO, vector[7].CO, vector[8].CO]])
    if np.linalg.det(matrix) == 0:
        return True
    return False


def SingularNO(vector):
    matrix = np.array([[vector[0].NO, vector[1].NO, vector[2].NO],
                       [vector[3].NO, vector[4].NO, vector[5].NO],
                       [vector[6].NO, vector[7].NO, vector[8].NO]])
    if np.linalg.det(matrix) == 0:
        return True
    return False


def SingularNO2(vector):
    matrix = np.array([[vector[0].NO2, vector[1].NO2, vector[2].NO2],
                       [vector[3].NO2, vector[4].NO2, vector[5].NO2],
                       [vector[6].NO2, vector[7].NO2, vector[8].NO2]])
    if np.linalg.det(matrix) == 0:
        return True
    return False


def SingularO3(vector):
    matrix = np.array([[vector[0].O3, vector[1].O3, vector[2].O3],
                       [vector[3].O3, vector[4].O3, vector[5].O3],
                       [vector[6].O3, vector[7].O3, vector[8].O3]])
    if np.linalg.det(matrix) == 0:
        return True
    return False


def SingularO3NO2(vector):
    matrix = np.array([[vector[0].O3NO2, vector[1].O3NO2, vector[2].O3NO2],
                       [vector[3].O3NO2, vector[4].O3NO2, vector[5].O3NO2],
                       [vector[6].O3NO2, vector[7].O3NO2, vector[8].O3NO2]])
    if np.linalg.det(matrix) == 0:
        return True
    return False


def SolvingForCO(vector):
    matrix = np.array([[vector[0].CO, vector[1].CO, vector[2].CO],
                       [vector[3].CO, vector[4].CO, vector[5].CO],
                       [vector[6].CO, vector[7].CO, vector[8].CO]])
    b = np.array([[vector[9].CO], [vector[9].CO], [vector[9].CO]])
    solution = np.linalg.solve(matrix, b)
    return solution[0][0], solution[1][0], solution[2][0]


def SolvingForNO(vector):
    matrix = np.array([[vector[0].NO, vector[1].NO, vector[2].NO],
                       [vector[3].NO, vector[4].NO, vector[5].NO],
                       [vector[6].NO, vector[7].NO, vector[8].NO]])
    b = np.array([[vector[9].NO], [vector[9].NO], [vector[9].NO]])
    solution = np.linalg.solve(matrix, b)
    return solution[0][0], solution[1][0], solution[2][0]


def SolvingForNO2(vector):
    matrix = np.array([[vector[0].NO2, vector[1].NO2, vector[2].NO2],
                       [vector[3].NO2, vector[4].NO2, vector[5].NO2],
                       [vector[6].NO2, vector[7].NO2, vector[8].NO2]])
    b = np.array([[vector[9].NO2], [vector[9].NO2], [vector[9].NO2]])
    solution = np.linalg.solve(matrix, b)
    return solution[0][0], solution[1][0], solution[2][0]


def SolvingForO3(vector):
    matrix = np.array([[vector[0].O3, vector[1].O3, vector[2].O3],
                       [vector[3].O3, vector[4].O3, vector[5].O3],
                       [vector[6].O3, vector[7].O3, vector[8].O3]])
    b = np.array([[vector[9].O3], [vector[9].O3], [vector[9].O3]])
    solution = np.linalg.solve(matrix, b)
    return solution[0][0], solution[1][0], solution[2][0]


def SolvingForO3NO2(vector):
    matrix = np.array([[vector[0].O3NO2, vector[1].O3NO2, vector[2].O3NO2],
                       [vector[3].O3NO2, vector[4].O3NO2, vector[5].O3NO2],
                       [vector[6].O3NO2, vector[7].O3NO2, vector[8].O3NO2]])
    b = np.array([[vector[9].O3NO2], [vector[9].O3NO2], [vector[9].O3NO2]])
    solution = np.linalg.solve(matrix, b)
    return solution[0][0], solution[1][0], solution[2][0]


def SingularCO15(vector):
    matrix = np.array([[vector[0].CO, vector[1].CO],
                       [vector[2].CO, vector[3].CO]])
    if np.linalg.det(matrix) == 0:
        return True
    return False


def SingularNO15(vector):
    matrix = np.array([[vector[0].NO, vector[1].NO],
                       [vector[2].NO, vector[3].NO]])
    if np.linalg.det(matrix) == 0:
        return True
    return False


def SingularNO215(vector):
    matrix = np.array([[vector[0].NO2, vector[1].NO2],
                       [vector[2].NO2, vector[3].NO2]])
    if np.linalg.det(matrix) == 0:
        return True
    return False


def SingularO315(vector):
    matrix = np.array([[vector[0].O3, vector[1].O3],
                       [vector[2].O3, vector[3].O3]])
    if np.linalg.det(matrix) == 0:
        return True
    return False


def SingularO3NO215(vector):
    matrix = np.array([[vector[0].O3NO2, vector[1].O3NO2],
                       [vector[2].O3NO2, vector[3].O3NO2]])
    if np.linalg.det(matrix) == 0:
        return True
    return False


def SolvingForCO15(vector):
    matrix = np.array([[vector[0].CO, vector[1].CO],
                       [vector[2].CO, vector[3].CO]])
    b = np.array([[vector[4].CO], [vector[4].CO]])
    solution = np.linalg.solve(matrix, b)
    return solution[0][0], solution[1][0]


def SolvingForNO15(vector):
    matrix = np.array([[vector[0].NO, vector[1].NO],
                       [vector[2].NO, vector[3].NO]])
    b = np.array([[vector[4].NO], [vector[4].NO]])
    solution = np.linalg.solve(matrix, b)
    return solution[0][0], solution[1][0]


def SolvingForNO215(vector):
    matrix = np.array([[vector[0].NO2, vector[1].NO2],
                       [vector[2].NO2, vector[3].NO2]])
    b = np.array([[vector[4].NO2], [vector[4].NO2]])
    solution = np.linalg.solve(matrix, b)
    return solution[0][0], solution[1][0]


def SolvingForO315(vector):
    matrix = np.array([[vector[0].O3, vector[1].O3],
                       [vector[2].O3, vector[3].O3]])
    b = np.array([[vector[4].O3], [vector[4].O3]])
    solution = np.linalg.solve(matrix, b)
    return solution[0][0], solution[1][0]


def SolvingForO3NO215(vector):
    matrix = np.array([[vector[0].O3NO2, vector[1].O3NO2],
                       [vector[2].O3NO2, vector[3].O3NO2]])
    b = np.array([[vector[4].O3NO2], [vector[4].O3NO2]])
    solution = np.linalg.solve(matrix, b)
    return solution[0][0], solution[1][0]
