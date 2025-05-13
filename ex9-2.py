class person:
  def _init_(self, name, age):
    self.name = name
    self.age = age
    
  def myfunc(self):
      print ("Hello my name is"+ self.name" my age is" +str (self.age))
      #print("Hello my name is"+ self.name" my age is" , (self.age)

p1 = person("John",36)
print (p1)    
p1.myfunc()
