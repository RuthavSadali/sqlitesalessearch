import sqlite3


class Search:

        
    def department_total(self, dept):
        """
        Returns the sum of all sales within a department
        """
        cconn = sqlite3.connect('sales.sqlite')
        conn = cconn.cursor()
        conn.execute('''SELECT department FROM sales''')
        deptart = conn.fetchall()
        conn.execute('''SELECT amount FROM sales''')
        moneys = conn.fetchall()
        tot = 0.0
        ext = []
        stringg = ""

        for x in range(0, len(deptart)):
            if str(deptart[x]) == "('" + dept + "',)":
                stringg = str(moneys[x])
                stringg = stringg[1: len(stringg)-2]
                tot = tot + float(stringg)
        tot = round(tot, 2)
        
        return tot

    def department_total_bydate(self, dept, date):
        """
        Returns the sum of all sales within a department on a specific date
        """
        cconn = sqlite3.connect('sales.sqlite')
        conn = cconn.cursor()
        conn.execute('''SELECT department FROM sales''')
        deptart = conn.fetchall()
        conn.execute('''SELECT amount FROM sales''')
        moneys = conn.fetchall()
        conn.execute('''SELECT sale_date FROM sales''')
        dates = conn.fetchall()
        tot = 0.0
        ext = []
        stringg = ""

        for x in range(0, len(deptart)):
            if str(deptart[x]) == "('" + dept + "',)" and str(dates[x]) == "('" + date + "',)":
                stringg = str(moneys[x])
                stringg = stringg[1: len(stringg)-2]
                tot = tot + float(stringg)
        
        ##print('IT IS ' + str(tot))
        return tot


    def country_count_date_range(self, country, start_date, end_date):
        """
        Returns the number of sales to buyers in a specific country between 2 dates, inclusive
        """
        
        cconn = sqlite3.connect('sales.sqlite')
        conn = cconn.cursor()
        conn.execute('''SELECT country, id FROM buyers''')
        deptart = conn.fetchall()
        conn.execute("""SELECT buyer_id, amount FROM sales WHERE sale_date >= '""" + start_date + """' AND sale_date <= '"""+ end_date + """'""")
        buyers = conn.fetchall()
        tot = 0

        for x in range(0, len(deptart)):
            temp = str(deptart[x]).split(',')
            county = temp[0][2:-1]
            idofbuyer = temp[1][1:-1]
            for x in range(0, len(buyers)):
                buyandmon = str(buyers[x]).split(',')
                idofperson = buyandmon[0][1:]
                moneys = buyandmon[1][:-1]
                if idofperson == idofbuyer:
                    if county == country:
                        tot = tot + float(moneys)
        return tot

    def biggest_spender(self):
        """
        Returns a tuple with the first and last name of the buyer who spent the most money
        """
        cconn = sqlite3.connect('sales.sqlite')
        conn = cconn.cursor()
        conn.execute('''SELECT buyer_id, amount FROM sales''')
        deptart = conn.fetchall()
        arr = []
        for x in range(0, 1001):
            arr.append(0.0)
        
        for x in range(0, len(deptart)):
            temp = str(deptart[x]).split(',')
            idofbuyer = temp[0][1:]
            cost = temp[1][1:-1]
            arr[int(idofbuyer)] = arr[int(idofbuyer)] + float(cost)
        
        max = 0.0
        biggest = ""
        for x in range(0, len(arr)):
            if arr[x] > max:
                max = arr[x]
                biggest = str(x)
            
        conn.execute('''SELECT id, first_name, last_name FROM buyers''')
        deptart = conn.fetchall()

        tup = ("", "")

        for x in range(0, len(deptart)):
            temp = str(deptart[x]).split(',')
            idofper = temp[0][1:]
            firstName = temp[1][2:-1]
            lastName = temp[2][2:-2]
            if idofper == biggest:
                tup = (firstName, lastName)

        return tup

    def biggest_spenders(self, how_many, department):
        """
        Returns the how_many highest spenders in a specific department
        """
        cconn = sqlite3.connect('sales.sqlite')
        conn = cconn.cursor()
        conn.execute('''SELECT buyer_id, amount, department FROM sales''')
        deptart = conn.fetchall()
        arr = []
        for x in range(0, 1001):
            arr.append(0.0)

        for x in range(0, len(deptart)):
            temp = str(deptart).split(',')
            idofper = temp[0][1:]
            money = temp[1][1:]
            depart = temp[2][1:-1][2:-2]
            if depart == department:
                arr[int(idofper)] == float(money)
        s = ""
        arr.sort(reverse = True)
        for x in range(0, how_many):
            if x == how_many - 1:
                s = s + str(arr[x])
            else:
                s = s + str(arr[x]) + ","
        arrOfNames = s.split(',')
        returnArr = []

        conn.execute('''SELECT id, first_name, last_name FROM buyers''')
        deptart = conn.fetchall()

        for x in range(0, len(deptart)):
            temp = str(deptart[x]).split(',')
            idofper = temp[0][1:]
            firstName = temp[1][2:-1]
            lastName = temp[2][2:-2]
            for x in range(0, len(arrOfNames)):
                if str(x) == idofper:
                    returnArr.append((firstName, lastName, float(arrOfNames[x])))
        print (returnArr)
        return returnArr
