# 교재 딕셔너리 예제
# 중괄호는 쉼표로 구분
# key : value

subjects = {
    '의사소통영어': 'A+',
    '오래된 미래': 'B+',
    '양자역학': 'A0'
}
student = '김도훈'
subject = '오래된 미래'
print(student, '학생의 ', subject, '과목 성적은', subjects[subject], '입니다.')
# old style
print("%s 학생의 %s 과목 성적은 %s입니다." % (student, subject, subjects[subject]))
# modern style (format 함수)
print("{0} 학생의 {1} 과목 성적은 {2}입니다.".format(student, subject, subjects[subject]))
print("{} 학생의 {} 과목 성적은 {}입니다.".format(student, subject, subjects[subject]))
# ultra modern style (f 스트링)
# f 스트링 - 홑따옴표 한 개만 필요
print(f'{student} 학생의 {subject} 과목 성적은 {subjects[subject]}입니다.')

# 1-4 예제: site가 앞에 %s로 들어가고 era가 뒤에 &s로 들어가
