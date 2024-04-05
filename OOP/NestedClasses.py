class Customer:
    def __init__(self, id, name, bno, bstreet, bcity, bcountry, bzipc, sno, sstreet, scity, scountry, szipc):
        self.cust_id = id
        self.name = name
        self.bill_add = self.Address(bno, bstreet, bcity, bcountry, bzipc, )
        self.shipp_add = self.Address(sno, sstreet, scity, scountry, szipc)

    class Address:
        def __init__(self, no, street, city, country, zipc):
            self.no = no
            self.street = street
            self.city = city
            self.country = country
            self.zipc = zipc

        def display(self):
            print(self.no),
            print(self.street)
            print(self.city)
            print(self.country)
            print(self.zipc)


c = Customer(10, 'John', 101, 'maple Avenue', 'baltimore', 'USA', 21215, 10, 'Maple', 'baltimore', 'USA', 21215)
c.bill_add.display()
c.shipp_add.display()
