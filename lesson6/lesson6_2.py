import random
def get_names(nums:int=2)->list[str]:
    with open('names.txt',mode='r',encoding='utf-8') as file:
        names_str = file.read()         #將讀取的資料放進一個變數
                           
    names:list = names_str.split(sep='\n')   #切割資料，放入變數names
    names = random.choices(names,k=nums)
    return names


def generate_students(names:list[str])->list[dict]:
    students:list[dict]=[]                              #建立一個lsit
    for name in names:
        chinese = random.randint(50,100)
        english = random.randint(50,100)
        math = random.randint(50,100)
        student = {'name':name,'chinese':chinese,'english':english,'math':math}
        students.append(student)
    # print(students)
    return students

nums = int(input('請輸入學生數量(最多10位):'))
student_names:list[str] = get_names(nums=nums)
students:list[dict] = generate_students(names=student_names)
print(students)