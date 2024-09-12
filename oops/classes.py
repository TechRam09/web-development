# class MyClass:
#     variable="some text"
#     def myFunction(self):
#         print("nishanth is",self.variable)
    
#     def my2Function(self,name):
#         print("My coderFriend is", name)
        
        

# myobjectX = MyClass()
# myobjectX.myFunction()
# myobjectX.my2Function("Nishanth")

class Movie:
    def movie_name(self,mname):
        print("Movie Name is:",mname)
    def movie_language(self,mlanguage):
        print("Movie Language is:",mlanguage)
    def movie_rating(self,rating):
        print("Movie rating is:",rating)
        
        
m = Movie()
m.movie_name("Kantara")
m.movie_language("Kannada")
m.movie_rating(8.7)
