
def my_fun1(year):
  return 1911 + year


def my_fun2(year):
  return  year - 1911
  
year = int(input("please input 民國"))
print("西元=",my_fun1(year))

year = int(input("please input 西元"))
print("民國=",my_un2(year))
