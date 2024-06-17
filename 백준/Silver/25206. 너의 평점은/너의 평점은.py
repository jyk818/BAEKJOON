# 과목 학점 등급(과목평점)
# ObjectOrientedProgramming1 3.0 A+
# (전체 학점 * 등급) / 총 학점의 합

gpa_score = {
    "A+":4.5, 
    "A0":4.0, 
    "B+":3.5, 
    "B0":3.0, 
    "C+":2.5,
    "C0":2.0, 
    "D+":1.5, 
    "D0":1.0, 
    "F":0.0
}
score = 0
total_credit = 0

for i in range(20):
  subject, credit, gpa = input().split()

  if gpa in gpa_score :
    score += float(credit) * gpa_score[gpa]      # getting the value from dictionary with key. (ex. dictionary[key])
    total_credit += float(credit)

print(score/total_credit)