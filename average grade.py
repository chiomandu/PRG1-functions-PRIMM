def final_score(homework_score, test_score, test_weighting=0.70, homework_weighting=0.3):
    final_homework=(homework_score *homework_weighting) 
    final_test= (test_score*test_weighting)
    final_grade= final_test + final_homework
    return final_grade
#print(final_score(390,6890))
    
user_test_score=int(input("What is your test scores? "))
user_homework_score=int(input("What is your homework score? "))
#print(user_test_score)
#print(user_homework_score)
#final_score= user_
print(final_score(user_test_score, user_homework_score))
