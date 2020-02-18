class Imc:
    def __init__(self, sex, weight, height):
        self.sex = sex
        self.weight = weight
        self.height = height
        self.reg_male = {'V1': 20.7, 'V2': 26.4, 'V3': 27.8, 'V4': 31.1}
        self.reg_female = {'V1': 19.1, 'V2': 25.8, 'V3': 27.3, 'V4': 32.3}

    def calc_imc(self):
        try:
            w = float(self.validate_hw(self.weight, 0, 350))
            h = float(self.validate_hw(self.height, 0, 3))
            return w / (h * h)
        except Exception:
            return False

    def validate_sex(self):
        if self.sex == 'm' or self.sex == 'f':
            return self.sex
        return False

    @staticmethod
    def validate_hw(hw, value1, value2):
        if float(hw) <= value1 or float(hw) > value2:
            return False
        return hw

    @staticmethod
    def reply(result_imc, reg):
        if result_imc < reg['V1']:
            return 'Under weight.'
        elif reg['V1'] <= result_imc < reg['V2']:
            return 'Normal weight.'
        elif reg['V2'] <= result_imc < reg['V3']:
            return 'Marginally overweight.'
        elif reg['V3'] <= result_imc < reg['V4']:
            return 'Overweight.'
        elif result_imc > reg['V4']:
            return 'Obesity.'

    def main(self):
        if self.calc_imc():
            if self.validate_sex() == 'm':
                return self.reply(self.calc_imc(), self.reg_male)
            elif self.validate_sex() == 'f':
                return self.reply(self.calc_imc(), self.reg_female)
        return False


def imc(sex, weight, height):
    return Imc(sex, weight, height).main()


__all__ = ['imc']

if __name__ == '__main__':
    result = imc('m', 65, 1.75)
    print(result)
