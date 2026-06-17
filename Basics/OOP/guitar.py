class Guitar:

    #attributes
    def __init__(self, model, brand, type) :
        self.model = model
        self.brand = brand
        self.type = type


    # methods
    def sound (self): # self refers to the object using this message
        print("your " +self.type +" " + self.model+ " " +self.brand+ " guitar sounds good")