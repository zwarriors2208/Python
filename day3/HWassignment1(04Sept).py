math_student = {'charlie', 'alice', 'bob', 'david'}
science_student = {'charlie', 'david', 'eve', 'frank'}
#student who are enrolled in both math and science
s = math_student.intersection(science_student)
print("student who are enrolled in both math and science: ", s)
#student who are enrolled in both math but not in science
s1 = math_student - science_student
print("student who are enrolled in  math but not in science: ", s1)
##student who are enrolled in either of the subject math and science
s2 = math_student.union(science_student)
print("student who are enrolled in either of the subject math and science", s2)
#student who are enrolled in science but not in math
s3 = science_student - math_student
print("student who are enrolled in both science but not in math: ", s3)