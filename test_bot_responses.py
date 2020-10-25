from helper import *


def test_bot_responses():
   response = get_bot_response_to('привет')
   assert response[0] == 'Привет!'
   response = get_bot_response_to('запусти сценарий')
   assert response[0] == 'Хорошо. Давайте выберем подходящую еду.'
   assert response[1] == 'Что вы хотите?'
   response = get_bot_response_to('Пельмени')
   assert response[0] == 'Неправильный выбор. Давайте попробуем еще раз!))'
   assert response[1] == 'Что вы хотите?'
   response = get_bot_response_to('Блины')
   assert response[0] == 'Напоминаю твой вопрос: запусти сценарий'
   assert response[1] == 'Приятного аппетита, бро! :)'
