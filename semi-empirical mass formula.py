

import pandas as pd
import plotly
import plotly.graph_objs as go




def I_have_both():
    A = float(input("What is your A value?:   "))
    Z = float(input("What is your Z value?:    "))
    B= find_binding_energy(A, Z)
    print("Your binding energy per nucleon is: " + str(B / A) + "MeV \n" + "Your binding energy is: " + str(B) + "MeV")


def I_have_z():
    Z = int(input("Please put in your Z:        "))
    find_the_largest_B_for_Z(Z)


def find_binding_energy(A, Z):
    a_1 = 15.67
    a_2 = 17.23
    a_3 = 0.75
    a_4 = 93.2
    if (A % 2 != 0):
        a_5 = 0
    elif (A % 2 == 0 and Z % 2 == 0):
        a_5 = 12.0
    elif (Z % 2 != 0):
        a_5 = -12.0
    first = a_1 * A
    second = a_2 * (A ** (2 / 3))
    third = a_3 * ((Z ** 2) / A ** (1 / 3))
    fourth = a_4 * (((A - 2 * Z) ** 2) / A)
    fifth = a_5 / (A ** (1 / 2))
    B = first - second - third - fourth + fifth
    print()
    print()
    return B


def find_the_largest_B_for_Z(Z):
    answer = [0.0, 0.0]
    for A in range(Z, (3 * Z + 1)):
        B = find_binding_energy(A, Z)
        if B > answer[0]:
            answer[0] = B
            answer[1] = A
    print("The largest binding energy for Z is " + str(answer[0])+ " MeV at A = "+str(answer[1]))
    return answer



def find__B_for_all_Z():
    output = []
    for Z in range(1,101):
        answer = [0.0, 0.0,0.0,0.0]
        for A in range(Z, (3 * Z + 1)):
            B = find_binding_energy(A, Z)
            if B > answer[0]:
                answer[0] = B
                answer[1] = A
                answer[2] = Z
                answer[3] = B/A
        output.append(answer)
    output_df = pd.DataFrame(output, columns=["B","A","Z","B/A"])

    trace = go.Scatter(
        x = output_df['Z'],
        y = output_df["B/A"]
    )
    layout = dict(title = "The Semi-Empirical Mass Formula",
                  xaxis = dict(title = "Atomic Number: Z"),
                  yaxis = dict(title = "Binding Energy per Nucleon"))
    fig = dict(data=[trace], layout=layout)
    plotly.offline.plot(fig)
    return



choose = input("Part A: find binding energy of A,Z pair \n Part B: find largest binding energy for Z?     \n or C for "
               "highest B from Z= 0-100:         ")
if choose == "A":
    I_have_both()
elif choose == "B":
    I_have_z()
elif choose == "C":
    print(find__B_for_all_Z())
else:
    print("you must choose A or B")
    choose = input("Part A: find binding energy of A,Z pair or Part B: find largest binding energy for Z?     ")