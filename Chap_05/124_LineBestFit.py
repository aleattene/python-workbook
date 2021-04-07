"""
The program receives a COLLECTION of POINTS (x, y) from the USER,
UNTIL for the X COORDINATE a BLANK LINE is ENTERED.
After that, the program displays the EQUATION of the STRAIGHT LINE
that best approximates the LINE that connects all of the POINTS entered.
For example (1, 1) (2, 2.1) (3, 2.9) -> Y = 0.95 X + 0.1
"""


# START Definition of the FUNCTIONS


def checkEntry(number):            # Possible evolution -> IMPORT module
    # Check Entry -> FLOAT
    return True


def angularCoefficient(x_coordinates, y_coordinates):
    product_XY = 0
    sum_XX = 0
    n = len(x_coordinates)
    for i in range(n):
        product_XY += x_coordinates[i]*y_coordinates[i]
        sum_XX += x_coordinates[i] ** 2
    sum_X = sum(x_coordinates)
    sum_Y = sum(y_coordinates)
    product_sumXsumY = sum_X * sum_Y
    sumXsumX = sum_X ** 2
    m_numerator = (product_XY - ((sum_X * sum_Y)) / n)
    m_denominator = sum_XX - (sumXsumX / n)
    m = m_numerator / m_denominator     # possible evolution -> chek division by zero
    return m


def yIntercept(x_coordinates, y_coordinates):
    n = len(x_coordinates)
    X_average = sum(x_coordinates) / n
    Y_average = sum(y_coordinates) / n
    m = angularCoefficient(x_coordinates, y_coordinates)
    y_intercept = Y_average - (m * X_average)
    return y_intercept


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # EMPTY LISTS (to store the coordinates X and Y)
    x_coordinates = []
    y_coordinates = []

    # Declaration of the VARIABLES
    point = 1

    # Acquisition and Control of the POINTS entered by the USER
    while True:
        print("Enter the coordinates (x,y) of the point n.{}.".format(point))
        x = input("x coordinate: ")
        y = input("y coordinate: ")
        if x == "" or y == "":
            continue
        else:
            break

    while True:
        x_coordinates.append(float(x))
        y_coordinates.append(float(y))
        point += 1
        print("Enter the coordinates (x,y) of the point n.{}.".format(point))
        x = input("x coordinate (blanck line to quit): ")
        if x == "":
            break
        y = input("y coordinate: ")

    # Calculation of the ANGULAR COEFFICIENT (m) of the STRAIGHT LINE
    m = angularCoefficient(x_coordinates, y_coordinates)

    # Calculation of the Y-INTERCEPT (b) of the STRAIGHT LINE
    b = yIntercept(x_coordinates, y_coordinates)

    # Displaying the EQUATION of the STRAIGHT LINE
    print("THE EQUATION of the STRAIGHT LINE that best representing the POINTS ENTERED is",
          " Y = {:.2f} X + {:.1f}".format(m, b))


if __name__ == "__main__":
    main()
