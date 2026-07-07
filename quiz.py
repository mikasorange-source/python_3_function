import random
import copy
import utils2

questions = [
    'Pythonで文字を表示するときに使うものはどれ？', 
    'Pythonで入力を受け取るときに使うものはどれ？', 
    'Pythonで「もし〜なら」という条件を書くときに使うものはどれ？'
]

options = [
    ['print', 'show', 'output'],
    ['input', 'scan', 'get'],
    ['if', 'when', 'check']
]
answers = ['print', 'input', 'if']
str_number_of_options = ['1', '2', '3']

options_shuffled = copy.deepcopy(options)
for option in options_shuffled:
    random.shuffle(option)

print('クイズゲームへようこそ！')

score = 0

utils2.show_question(questions, options_shuffled)

score = utils2.check_answer_and_count_score(
    questions, answers, options_shuffled, str_number_of_options
)
utils2.show_result(score, questions)
