from pages.basepage import *
from config.credential import *

input_email = (By.CSS_SELECTOR, "input[type='email']")
input_password = (By.CSS_SELECTOR, "input[type='password']")
email_address = userEmail
password = userPassword
form_input_name = userName
form_input_phone_number = userPhone
form_input_email = userEmail
form_input_cnic = userCnic
next_btn = (By.CSS_SELECTOR, "#identifierNext > div > button > span")
pass_next_btn = (By.CSS_SELECTOR, "#passwordNext > div > button > span")
page_title = (By.CSS_SELECTOR,
              ".freebirdFormviewerViewHeaderTitle.exportFormTitle")
all_input_title_selectors = ".freebirdFormviewerComponentsQuestionBaseTitleDescContainer > div.freebirdFormviewerComponentsQuestionBaseTitle"
all_input_values_selectors = ".quantumWizTextinputPaperinputInputArea input"
all_ques = []
corr_ans = []
random_ans = []
all_input_title = []
all_input_values = []
errors = []
a1 = ""
a2 = ""
a3 = ""
input_title_selectors_key = (By.CSS_SELECTOR,
                             ".freebirdFormviewerComponentsQuestionBaseTitleDescContainer > div.freebirdFormviewerComponentsQuestionBaseTitle")
input_values_selectors_key = (
    By.CSS_SELECTOR, ".quantumWizTextinputPaperinputInputArea input")

first_page_next_btn = (
    By.CSS_SELECTOR, "div.freebirdFormviewerViewNavigationLeftButtons > div > span > span")
second_page_next_btn = (
    By.CSS_SELECTOR, "div.freebirdFormviewerViewNavigationLeftButtons > div:nth-child(2) > span > span")
third_page_next_btn = ".appsMaterialWizButtonPaperbuttonLabel"
page2_ans_opt_selector = ".freebirdFormviewerComponentsQuestionRadioLabel"
page3_ans_opt_selector = ".freebirdFormviewerComponentsQuestionCheckboxCheckbox"
page4_drop_down_punjab = ".quantumWizMenuPaperselectOptionList"  # [0] Button
page4_drop_down_pakistan = (
    By.CSS_SELECTOR, ".quantumWizMenuPaperselectOptionList")  # [1] Button
page4_punjab_ans_input_city = "Multan"
page4_pakistan_ans_input_city = "Lahore"
page4_punjab_ans = (
    By.CSS_SELECTOR, ".exportSelectPopup .quantumWizMenuPaperselectOption[data-value='Multan']")
page4_pakistan_ans = (
    By.CSS_SELECTOR,
    f".exportSelectPopup .quantumWizMenuPaperselectOption[data-value='{page4_pakistan_ans_input_city}']")


all_error_msg = (".freebirdFormviewerComponentsQuestionBaseValidationError")
error_of = []
page_3_error_msg = []
ele = []
title = (By.CSS_SELECTOR, ".freebirdFormviewerViewHeaderTitle")
file_ele = ".appsMaterialWizButtonEl"
page5_add_btn = ".appsMaterialWizButtonEl"
page5_iframes = ".modal-dialog-content > iframe"
page5_titles_btn = (By.CSS_SELECTOR, '#\:6 > div')
page5_pdf_file = (By.CSS_SELECTOR, "[data-id='DoclistBlob.0.1aw6PyJ2zZTUlw1YRuDmR0LX2ZXTaLNh3']")
page5_img = (By.CSS_SELECTOR, "[aria-label='20689953_1437301106338452_2985474890754807218_o.jpg']")
page5_select_btn = (By.CSS_SELECTOR, "#picker\:ap\:2")
page5_img_title_btn = (By.CSS_SELECTOR, "#\:6 > div")
used_frames = []
page6_input_date_selector = (By.CSS_SELECTOR, "input[type='date']")
page6_input_time_selector = (By.CSS_SELECTOR, "input[type='number']")
page6_input_time_min_selector = (By.CSS_SELECTOR, "input[aria-label='Minute']")
page6_input_time_hour_selector = (By.CSS_SELECTOR, "input[aria-label='Hour']")
title_head = (By.CSS_SELECTOR, ".freebirdFormviewerViewHeaderTitle")
view_score_btn = (By.CSS_SELECTOR, ".appsMaterialWizButtonPaperbuttonLabel")
correct_ans_ques = ".freebirdFormviewerViewItemsItemItemTitle"
incorrect_ques = ".freebirdFormviewerViewItemsItemIncorrect"
correct_ans_list = ".freebirdFormviewerViewItemsItemGradingCorrectAnswerBox"
correct_divs = ".freebirdFormviewerViewItemsItemHasSectionBanner"
all_correct_ans = []
div1_ans = ".freebirdFormviewerViewItemsTextTextItem"
all_q_a_ = ".freebirdFormviewerViewItemsItemItem"
correct_q = ".freebirdFormviewerViewItemsItemCorrect"
wrong_questions_list = []
correct_ans_list = []

incorrect_ques = ".freebirdFormviewerViewItemsItemIncorrect"
correct_ans = ".freebirdFormviewerViewItemsItemGradingCorrectAnswerBox"
submitted_questions = []
submitted_ans = []
matched_ques = []

score_incorrect_ques = ".freebirdFormviewerViewItemsItemIncorrect"
score_correct_ans = ".freebirdFormviewerViewItemsItemGradingCorrectAnswerBox"
score_correct_ques = ".freebirdFormviewerViewItemsItemCorrect"
web_total_marks = (By.CSS_SELECTOR, "div.freebirdFormviewerViewHeaderGradeContainer > span")
score_all_incorrect_qes_list = []
score_total_marks = []
score_obtain_marks_list = []
score_total_marks_list = []


score_all_correct_qes_list = []
score_all_ques_marks = []
