import re

class Calculus(object):
    def __init__(self, equation):
        self.equation = equation

    def __validator(self):
        return self.sequence_has_only_valid_characters(self.equation, "0123456789x^+-*/().")

    def __find_symbol_x(self, chain_of_str):
        return self.sequence_has_only_valid_characters(chain_of_str, "0123456789x")
    
    def sequence_has_only_valid_characters(self, sequence, valid_characters):
        valid_characters = "0123456789x"
        for char in sequence.lower():
            if char not in valid_characters:
                return False
        return True

    def separate_equation(self):
        return re.split("([+-])", self.equation.replace(" ", ""))

    def separate_equation_product_rule(self):
        return re.split("([*])", self.equation.replace(" ", ""))
    
    def power_rule(self):
        derivative_equation = []
        derivative_sign = []
        pre_derivative_equation = []
        final_result = []
        equation_list = self.separate_equation()
        for item in equation_list:
            if ((item != "+") & (item != "-") & (item != None)):
                hasX = self.__find_symbol_x(item)
                if (hasX == True):
                    derivative_equation.append([str(item), "^", "1"])
                else:
                    derivative_equation.append(re.split("(['^'])", item.replace(" ", "")))
            else:
                derivative_sign.append(item)
        for item in derivative_equation:
            exp = float(item[2])
            main_num = float(re.split("(['x'])", item[0])[0])
            main_num = main_num * float(exp)
            exp = exp - 1
            if (exp == 1):
                final = str(str(main_num) + "x")
                pre_derivative_equation.append(final)
            else:
                final = str(str(main_num) + "x^" + str(exp))
                pre_derivative_equation.append(final)
        sign_pos = 0
        for item in pre_derivative_equation:
            if (sign_pos < len(derivative_sign)):
                sign = str(derivative_sign[sign_pos])
                sign_pos = sign_pos + 1
            else:
                sign = ""
            final_result.append(str(item) + " " + sign + " ")
        result = ""
        for item in final_result:
            result = result + item
        return result

    def product_rule(self):
        derivative_equation = []
        derivative_sign = []
        equation_list = self.separate_equation_product_rule()
        
        for item in equation_list:
            if ((item != "*") & (item != None)):
                hasX = self.__find_symbol_x(item)
                if (hasX == True):
                    derivative_equation.append([str(item), "^", "1"])
                else:
                    derivative_equation.append(re.split("(['^'])", item.replace(" ", "")))
                
        print(derivative_equation)


    # def quotient_rule(self):

    # def chain_rule(self):

    # def find_derivative(self):
    #     equation_list = self.separate_equation()

equation = input("Enter your equation >>> ")
Calculus = Calculus(equation)
# print(Calculus.separate_equation())
print(Calculus.product_rule())
