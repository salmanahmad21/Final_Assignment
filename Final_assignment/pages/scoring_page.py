from pages.locators_page import *


class ScoringMethods(BaseMethods):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def scoring(self):
        obtain = 0
        total = 0
        obj = BaseMethods(self.driver)
        all_incorrect_ques = obj.get_all_elements(score_incorrect_ques)
        all_correct_ques = obj.get_all_elements(score_correct_ques)
        web_score_value = obj.get_text(web_total_marks)

        for i in range(len(all_incorrect_ques)):
            score_all_ques_marks.append(obj.clean_questions_tail(all_incorrect_ques[i].text))

        for i in range(len(all_correct_ques)):
            score_all_ques_marks.append(obj.clean_questions_tail(all_correct_ques[i].text))

        print("Marks of all original Ans >>> : ", score_all_ques_marks)

        for i in range(len(score_all_ques_marks)):
            score_obtain_marks_list.append(obj.clean_head(score_all_ques_marks[i]))
            score_total_marks_list.append(obj.clean_tail(score_all_ques_marks[i]))

        for ele in range(0, len(score_obtain_marks_list)):
            obtain += int(score_obtain_marks_list[ele])
            total += int(score_total_marks_list[ele])

        # print(obtain_marks_list)
        # print(total_marks_list)

        result = obtain, "/", total
        score_value = ''.join(''.join(map(str, result)))
        if score_value == web_score_value:
            print("Calculated Score >>> : ", score_value, " - Web Score >>> : ", web_score_value)
            print("Web Score Verified")
        return score_value, web_score_value
