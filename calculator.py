import math


def taking_inputs_for_primitive_calculations():
    first_no = float(input('enter first value:'))
    second_no = float(input('enter second value:'))
    return (first_no, second_no)


def additon():
    first_no, second_no = taking_inputs_for_primitive_calculations()
    result = first_no + second_no
    return result


def subtraction():
    first_no, second_no = taking_inputs_for_primitive_calculations()
    result = first_no - second_no
    return result


def mulplication():
    first_no, second_no = taking_inputs_for_primitive_calculations()
    result = first_no * second_no
    return result


def division():
    first_no, second_no = taking_inputs_for_primitive_calculations()
    result = first_no / second_no
    return result


print('''
Options:
1. Addition
2. Subtraction
3. Muliplication
4. Division
5. More options
''')

SELECTED_OPTION = int(input('select option:'))

if SELECTED_OPTION == 1:
    ADDITION = additon()
    print(ADDITION)

elif SELECTED_OPTION == 2:
    SUBSTRACTION = subtraction()
    print(SUBSTRACTION)

elif SELECTED_OPTION == 3:
    MULTIPLY = mulplication()
    print(MULTIPLY)

elif SELECTED_OPTION == 4:
    DIVIDE = division()
    print(DIVIDE)

else:
    print('''
    More Options:
    6. Trignometric functions
    7. Other Mathematical Function
    8. Quadratic Equation
    ''')

    SELECTED_OPTION = int(input('Select Option:'))


    def taking_inputs_for_trignometric_calculations():
        angle = int(input('Enter angle respective to the function:'))
        return angle


    def sine():
        sin_input = taking_inputs_for_trignometric_calculations()
        sin_result = math.sin(math.radians(sin_input))
        return sin_result


    def cosine():
        cos_input = taking_inputs_for_trignometric_calculations()
        cos_result = math.cos(math.radians(cos_input))
        return cos_result


    def tan():
        tan_input = taking_inputs_for_trignometric_calculations()
        tan_result = math.tan(math.radians(tan_input))
        return tan_result


    def invsine():
        isin_input = taking_inputs_for_trignometric_calculations()
        isin_result = math.asin(isin_input)
        return isin_result


    def invcosine():
        icos_input = taking_inputs_for_trignometric_calculations()
        icos_result = math.acos(icos_input)
        return icos_result


    def invtan():
        itan_input = taking_inputs_for_trignometric_calculations()
        itan_result = math.atan(itan_input)
        return itan_result

    if SELECTED_OPTION == 6:
        print('''
        9. Sine, 9.1  InvSine
        10.Cose, 10.1 InvCosine
        11.Tan,  11.1 InvTan 
        ''')

        SELECTED_OPTION2 = float(input('Select Option:'))

        if SELECTED_OPTION2 == 9:
            SINE = sine()
            print(SINE, 'or', round(SINE))

        elif SELECTED_OPTION2 == 10:
            COSINE = cosine()
            print(round(COSINE))

        elif SELECTED_OPTION2 == 11:
            TAN = tan()
            print(round(TAN))

        elif SELECTED_OPTION2 == 9.1:
            INVERSE = invsine()
            print(math.degrees(INVERSE))

        elif SELECTED_OPTION2 == 10.1:
            INVERSE = invcosine()
            print(math.degrees(INVERSE))

        else:
            INVERSE = invtan()
            print(math.degrees(INVERSE))


    def input_for_exponent_sqrt_fact():
        value = int(input('Enter value for exponent/sqrt/factorial:'))
        return value


    def taking_inputs_for_log():
        log_input = float(input('Enter logarithmic value:'))
        return log_input


    def taking_inputs_for_different_logbase():
        log_input_1 = float(input('Enter value f_or log:'))
        log_input_2 = int(input('Enter base of log:'))
        return(log_input_1, log_input_2)


    def taking_inputs_for_power():
        power_input_1 = float(input('Enter value:'))
        power_input_2 = int(input('Enter power:'))
        return(power_input_1, power_input_2)


    if SELECTED_OPTION == 7:
        print('''
        Other Maths Functions:
        7.1 e power x
        7.2 ln/logarithmic with base e
        7.3 logarithmic for any base
        7.4 x ^ y
        7.5 Square root
        7.6 Factorial
        ''')


        SELECTED_OPTION = float(input('Choose Option:'))

        if SELECTED_OPTION == 7.1:
            INPUT = input_for_exponent_sqrt_fact()
            RESULT = math.exp(INPUT)
            print(RESULT)

        elif SELECTED_OPTION == 7.2:
            INPUT = taking_inputs_for_log()
            RESULT = math.log(INPUT)
            print('ln:', RESULT)


        elif SELECTED_OPTION == 7.3:
            INPUT_1, INPUT_2 = taking_inputs_for_different_logbase()
            RESULT = math.log(INPUT_1, INPUT_2)
            print('log of base:', INPUT_2, RESULT)

        elif SELECTED_OPTION == 7.4:
            INPUT_1, INPUT_2 = taking_inputs_for_power()
            RESULT = math.pow(INPUT_1, INPUT_2)
            print(RESULT)

        elif SELECTED_OPTION == 7.5:
            INPUT = input_for_exponent_sqrt_fact()
            RESULT = math.sqrt(INPUT)
            print('Sqrt of given no:', RESULT)


        else:
            INPUT = input_for_exponent_sqrt_fact()
            RESULT = math.factorial(INPUT)
            print('Factorial of number:', RESULT)

        coefficient_1 = float(input('Enter coefficient of x square / x2:'))
        coefficient_2 = float(input('Enter coefficient of x:'))
        coefficient_3 = float(input('Enter coefficient of c:'))

        DISCRIMINANT = coefficient_2**2 - 4 * coefficient_1 * coefficient_3 

        
        if SELECTED_OPTION == 8:



            def quadratic_formula():
                formula = (-coefficient_2+(DISCRIMINANT)**(1/2))/(2 * coefficient_1)
                return formula


            def quadratic_formula_2():
                formula_2 = (-coefficient_2-(DISCRIMINANT)**(1/2))/(2 * coefficient_1)
                return formula_2


            if DISCRIMINANT < 0:
                print('Roots are Complex Numbers.')
            else:
                root_1 = quadratic_formula()
                root_2 = quadratic_formula_2()
                print('Roots of equation are:', round(root_1), round(root_2))

            
