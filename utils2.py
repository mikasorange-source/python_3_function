def show_question(questions, options_shuffled):
    for i in range(len(questions)):
        print('問題' + str(i + 1))
        print(questions[i])
        for j, option_shuffled_entry in enumerate(options_shuffled[i]):
            print(str(j + 1) + ':' + option_shuffled_entry)

def check_answer_and_count_score(
        questions, answers, options_shuffled, str_number_of_options
):
    score = 0
    for i in range(len(questions)):
        index = options_shuffled[i].index(answers[i])
        while True:
            input_answer = input('問題' + str(i + 1) 
                                 + 'の答えを入力してください：')
            if (
                input_answer == answers[i] 
                or input_answer == str(index + 1)
            ):
                print('問題' + str(i + 1) + '正解！')
                score += 1
                break
            elif (
                input_answer in options_shuffled[i] 
                or input_answer in str_number_of_options
            ):
                print(
                    '問題' + str(i + 1) + '不正解...正解は' 
                      + answers[i] + 'でした！'
                )
                break
            else:
                print('正しく入力してください')
    return score

def show_result(score, questions):
    print(str(len(questions)) + '問中' + str(score) + '問正解でした！')
    print('正答率' + str(round(score / len(questions) * 100)) + '%')
