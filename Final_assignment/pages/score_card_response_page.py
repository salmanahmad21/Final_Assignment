from pages.locators_page import *


class ScoreCardResponseMethods(BaseMethods):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def score_card_csv(self):
        obj = BaseMethods(self.driver)
        wrong_ques = obj.get_all_elements(incorrect_ques)
        right_ans = obj.get_all_elements(correct_ans)

        obj.wait_for_ele_invisible(title_head)

        for i in range(len(wrong_ques)):
            raw_ques = wrong_ques[i].text
            clean_ques = obj.clean_questions(raw_ques)
            wrong_questions_list.append(clean_ques)
            raw_ans = right_ans[i].text
            clean_ans = obj.clean_correct_ans(raw_ans)
            correct_ans_list.append(clean_ans)

        print("Wrong_ques >>> : ", wrong_questions_list)
        print("Correct_ans >>> : ", correct_ans_list)

        f = open('/Users/salmanahmad/Documents/output_csv.csv', encoding='UTF-8')
        csv_f = csv.reader(f)
        next(csv_f, None)

        for row in csv_f:
            submitted_questions.append(row[0])
            submitted_ans.append(row[1])

        print("CSV Ques >>> : ", submitted_questions)
        print("CSV Ans >>> : ", submitted_ans)

        csv_correct_answers_list = [None] * len(submitted_questions)

        for submitted_questions_index, csv_question in enumerate(submitted_questions):

            for web_question_index, web_question in enumerate(wrong_questions_list):
                is_matched_index = None
                is_matched_index = web_question_index if csv_question.strip(
                    '\t') == web_question else None
                if is_matched_index != None:
                    break

            if is_matched_index != None:
                csv_correct_answers_list[submitted_questions_index] = correct_ans_list[is_matched_index]
            else:
                csv_correct_answers_list[submitted_questions_index] = submitted_ans[submitted_questions_index]

        columns = {}

        columns['Questions'] = submitted_questions
        columns['Random Answer'] = submitted_ans
        columns['Correct Answer'] = csv_correct_answers_list

        data = list(zip(columns['Questions'],
                        columns['Random Answer'], columns['Correct Answer']))

        df = pd.DataFrame(data=data)
        df.columns = ['Questions', 'Random Answer', 'Correct Answer']

        df.to_csv('output_results.csv', index=False, header=True)
        f.close()
