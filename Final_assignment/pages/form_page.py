from pages.locators_page import *


class Csv(BaseMethods):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def write_data(self):
        with open('Records.csv', 'a') as file:
            headers = ["questions", "random ans", "correct ans"]
            writer = csv.writer(file, delimiter=',')
            writer.writerow(headers)
            for i in range(len(all_ques)):
                writer.writerow([all_ques[i], random_ans[i]])
        print("All Questions >>> ", all_ques, "All Ans >>>", random_ans)





