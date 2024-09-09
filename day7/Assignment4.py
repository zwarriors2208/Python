from win32con import PAN_STRAIGHT_ARMS_SINGLE_SERIF


class bank_interst_calculator:
    __interest_rate=8.6
    __interest_rate_SeniorCitizen=8.4
    Principle_amount=55
    Time_duration=4
    senior=False
    def __init__(self,p_amount,Duration,seniorCitizen_flag):
        self.Principle_amount=p_amount
        self.Time_duration=Duration
        self.senior=seniorCitizen_flag

    def simple_interest_calculator(self):
        if self.senior:
            SI = (self.Time_duration * self.Principle_amount *self.__interest_rate_SeniorCitizen)/100
        else:
            SI = self.Time_duration * self.Principle_amount * self.__interest_rate / 100

        print(f"The simple interest is {SI}")

    def Monthly_installment(self):



cc = bank_interst_calculator(78000, (12 + 7)/12, True)
cc.simple_interest_calculator()

ankit = bank_interst_calculator(1000000, 10, 0)
ankit.simple_interest_calculator()
