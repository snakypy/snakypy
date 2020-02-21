class BMI:
    """Class that will calculate the body mass index."""

    def __init__(self, sex, weight, height):
        self.sex = sex
        self.weight = weight
        self.height = height
        self.reg_male = {'V1': 20.7, 'V2': 26.4, 'V3': 27.8, 'V4': 31.1}
        self.reg_female = {'V1': 19.1, 'V2': 25.8, 'V3': 27.3, 'V4': 32.3}

    def calc_bmi(self):
        """
        This method will perform the body mass index calculation.
        Applied within the "calc_bmi" method.

        Returns:
            [float] -- The method returns a float after the calculation,
                       otherwise it falls into an Exception.
        """
        try:
            w = float(self.validate_hw(self.weight, 0, 350))
            h = float(self.validate_hw(self.height, 0, 3))
            return w / (h * h)
        except Exception:
            return False

    def validate_sex(self):
        """Method to validate the person's gender.

        Returns:
            [str] - Returns a one-character string, or "m" or "f", where "m" is
                    a male and "f" is a female. If neither, it returns a false Boolean.
        """
        if self.sex == 'm' or self.sex == 'f':
            return self.sex
        return False

    @staticmethod
    def validate_hw(hw, value1, value2):
        """
        This is a static method for validating weight and height.
        The height cannot be greater than 3 meters and neither the weight
        above 350, nor can both be zeroed or negative

        Arguments:
            hw {float} -- You will receive either height or weight
            value1 {float} -- Will receive a minimum height, which represents zero (0)
            value2 {float} -- Will receive a maximum weight, which represents 350.

        Returns:
            [float] -- Returns a "float" if it enters the imposed conditions.
                       If it does not return a false Boolean value.
        """
        if float(hw) <= value1 or float(hw) > value2:
            return False
        return hw

    @staticmethod
    def reply(result_bmi, reg):
        """
        The purpose of this statistical method is to receive the calculation
        of the body mass index already done, and to compare it with the
        statistical data informed in the initializer method of the class.

        Arguments:
            result_bmi {float} -- This arguments will receive the body mass index
                                  value already performed.
            reg {dict} -- Receive a dictionary containing the height and weight
                          of each category

        Returns:
            [str] -- Returns a string informing the result according to the
                     calculation obtained.
        """
        if result_bmi < reg['V1']:
            return 'Under weight.'
        elif reg['V1'] <= result_bmi < reg['V2']:
            return 'Normal weight.'
        elif reg['V2'] <= result_bmi < reg['V3']:
            return 'Marginally overweight.'
        elif reg['V3'] <= result_bmi < reg['V4']:
            return 'Overweight.'
        elif result_bmi > reg['V4']:
            return 'Obesity.'

    def main(self):
        if self.calc_bmi():
            if self.validate_sex() == 'm':
                return self.reply(self.calc_bmi(), self.reg_male)
            elif self.validate_sex() == 'f':
                return self.reply(self.calc_bmi(), self.reg_female)
        return False


def bmi(sex, weight, height):
    """
    This function is responsible for calling the class of body mass index (BMI).

    Example:

    import snakypy

    snakypy.calculation.bmi('m', 60.4, 1.73)

    Arguments:
        sex {str} -- You must receive a string with a single character.
                     The string must be either "m" for "male" or "f" for "female"
        weight {float} -- You should receive a float, this is where you put the
                          weight. E.g: 60.4
        height {float} -- You should receive a float, this is where you put the
                          height. E.g: 1.73

    Returns:
        [object] -- The return will be a string informing the result or a false Boolean,
                    if the arguments are wrong.
    """
    return BMI(sex, weight, height).main()


def percentage(per, whole, *, operation=None, log=False):
    """
    This function will calculate a whole with a certain percentage value.

    Example:

    import snakypy

    snakypy.calculation.percentage(8.5, 50)


    Arguments:
        per {float} -- Input argument that should receive a float representing
                       a certain percentage value.
        whole {float} -- Input argument that should receive a float representing
                         total value.

    Keyword Arguments:
        operation {str} -- This named parameter must receive two types of string
                           values. One is the plus sign ('+') that will add the total
                           to the imposed percentage. The other is the minus sign ('-'),
                           which subtracts the total value from the imposed percentage
                           value. (default: {None})
        log {bool} -- If this parameter is of the value True, then the return will be
                     a custom string with the percent signs and the operation.
                     (default: {False})

    Returns:
        [object] -- Returns the result of the calculation, either in string or a float
                    depending on whether the log is True or not.
    """
    option = {
        '+': lambda: whole + (whole * (per / 100)),
        '-': lambda: whole - (whole * (per / 100))
    }.get(operation, lambda: whole * (per / 100))()
    if log:
        if operation == '+':
            return f'>> {whole} + {per}% = {option:.2f}'
        elif operation == '-':
            return f'>> {whole} - {per}% = {option:.2f}'
        return f'>> {per}% of {whole} = {option:.2f}'
    return option


__all__ = ['bmi', 'percentage']
