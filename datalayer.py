import pyodbc
from components import Product
from components import Distributor
from tkinter.ttk import Treeview

class DalHelper:
    def __init__(self):
        self.con = pyodbc.connect("driver={SQL Server};server=ANURAGOMEN\\SQLEXPRESS;database=projectdb;uid=sa;pwd=anurag")

    def __del__(self):
        if self.con!=None:
            self.con.close()
            self.con = None

class DALProduct(DalHelper):
    def Add_Product(self, Pro):
        flag = False
        try:
            cur = self.con.cursor()
            tup = (Pro.ProductName, Pro.Category)
            cur.execute("Insert into Products values(?,?)", tup)
            self.con.commit()
            flag = True
        except:
            self.con.rollback()

        return flag

    def Show_Product(self):

        cur= self.con.cursor()
        cur.execute("select * from Products")
        records = cur.fetchall()
        return records


class DALDistributor(DalHelper):
    def Add_Distributor(self, Dis):

        try:
            flag = False
            cur=self.con.cursor()
            tup= (Dis.DistributorName, Dis.Address, Dis.City, Dis.Contact)
            cur.execute("Insert into distributor values(?,?,?,?)",tup)
            self.con.commit()
            flag = True
        except:
            self.con.rollback()

        return flag

    def show_Distributor(self):

        cur = self.con.cursor()
        cur.execute("select * from distributor")
        records = cur.fetchall()
        return records


