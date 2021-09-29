class A:
    def feature1(self):
        print("Feature 1 working")

class B:
    def feature2(self):
        print("Feature 2 working")

class C(A, B):
    def featrue3(self):
        print("feature 3 Working")


a1=A()
c1=C()
