# import tools   #注意下方要使用時的時候加入tools.
# import gear
# import gear.widget
# from gear import widget
from gear.widget import get_name , generate_bmi

if __name__ == '__main__':      #此為主程式
    nums = int(input('請輸入人數:'))
    # # names:list[str]=tools.get_name(nums=nums)
    # students =tools.generate_bmi(tools.get_name(nums=nums))                   #tools模組中的方法
    # students =gear.widget.generate_bmi(gear.widget.get_name(nums=nums))       #gear資料夾(package)中的模組(module)
    # students =widget.generate_bmi(widget.get_name(nums=nums))     
    students =generate_bmi(get_name(nums=nums))
    # print(students)
    for student in students:
        for key,value in student.items():
            print(f'{key}:{value}')
        print('=========================')