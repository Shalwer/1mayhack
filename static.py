start_text = 'Начнём с /maths'
maths = 'Для значения тригонометрической функции пиши: ' \
        'функция-(пробел)-значения\n Пример: \n sin 145 \n acos 54'


def default_answer(message):
    answer = f'Мы можем поболтать, но только как бот с человеком.\n' \
             f'То есть: \n- {message} \n- Увы, я не знаю этой команды Т_Т '
    return answer
