questions=[
    {"question":'Как зовут главного героя из фильма "Гарри Поттер и тайная комната"?',
     "answers":["Рон Уизли", "Дамболдор", "Гарри Поттер", "Волан-де-Морт"],
     "right_answer": 3},
     
     {"question":"Сколько кристражей нужно было собрать героям фильма?",
     "answers":["5", "6", "7", "нет правильного ответа"],
     "right_answer": 3},
      
      {"question":"Как звали кота Гермионы?",
     "answers":["Живоглот", "Пушок", "Кароста", "Правильного ответа нет"],
     "right_answer": 1},
       
       {"question":"Кому не выпала честь уничтожить крестраж?",
     "answers":["Невилу Долгопупсу", "Сириусу Блэку", "Волан-де-Морту", "Гарри Поттеру"],  
     "right_answer": 2},
        
        {"question":"На каком факультете нужно отгадать загадку, чтобы попасть в гостиную?",
     "answers":["Слизерин", "Пуффендуй","Когтевран", "Грифиндор"],
     "right_answer": 3}
         ]
score=0
print("очес пройти тест по Гарри Поттеру?")
print("1.Да")
print("2.Нет")
print("Ваш выбор: ")
user_choice=int(input())
if user_choice == 1:
   for question in questions:    
       print(question.get("question")) # вывод вопроса
       answer_number=0
       for answer in question["answers"]:
           answer_number+=1
           print(answer_number, ".", answer) # вывод вариантов
       user_answer=int(input("ваш ответ: ")) 
       if user_answer == question.get("right_answer"): # вывод состояния ответа
          score=score+20
          print("Верно!!!")
       else:
            print("Не Верно :(")
   if score == 100:
       print("Ты победитель!!!!!!!!!!!!!!!!!!!")
   else:
       print("Главное не победа а участие") 
   print(str(score) + "/100")
else:
     print(":(")
nume=input("Ваше имя: ")
file_result=open("result.txt", "a")
file_result.write("Игрок: " + nume + " Набрал(а) очков: " + str(score) + "/n") 
file_result.close()
