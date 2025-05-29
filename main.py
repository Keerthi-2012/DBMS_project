import pymysql.cursors
from datetime import datetime

while True:
    username = input("Username: ")
    password = input("Password: ")
    try:
        con = pymysql.connect(host='localhost',
                              user="root",
                              password="Anjan@123",
                              db='ICC',
                              cursorclass=pymysql.cursors.DictCursor)
        if con.open:
            print("Connected")
        else:
            print("Failed to connect")

        with con.cursor() as cur:
            while True:
                if username == "admin" and password == "admin":
                    print("1.  Insert Season")
                    print("2.  Insert Match")
                    print("3.  Insert Team")
                    print("4.  Insert Player")
                    print("5.  Insert Toss")
                    print("6.  Insert Venue")
                    print("7.  Insert Batsman Score")
                    print("8.  Insert Bowler Stat")
                    print("9.  Update Match")
                    print("10. Update Team")
                    print("11. Update Player")
                    print("12. Update Venue")
                    print("13. Update Batsman Score")
                    print("14. Update Bowler Stat")
                    print("15. Delete Team")
                    print("16. Archive Player Records")
                    print("17. Delete Venue")
                    print("18. Search Champion")
                    print("19. Search Match")
                    print("20. Search Venue")
                    print("21. Search Team")
                    print("22. Search Player")
                    print("23. Search Season")
                    print("24. Aggregate Venue Data")
                    print("25. Count Match Results of a Team")
                    print("26. Team Statistics")
                    print("27. List Current Teams")
                    print("28. List Matches By Date")
                    print("29. List Match Results of a Season")
                    print("30. List Venues Available")
                    print("31. Display Points Table")
                    print("-1. Logout")

                    ch = int(input("Enter choice> "))

                    if ch == -1:
                        print("Bye!")
                        exit()
                    # else:
                    #     dispatchAdmin(ch)
                else:
                    print("1.  Search Champion")
                    print("2.  Search Match")
                    print("3.  Search Venue")
                    print("4.  Search Team")
                    print("5.  Search Player")
                    print("6.  Search Season")
                    print("7.  Aggregate Venue Data")
                    print("8.  Count Match Results of a Team")
                    print("9.  Team Statistics")
                    print("10. List Current Teams")
                    print("11. List Matches By Date")
                    print("12. List Match Results of a Season")
                    print("13. List Venues Available")
                    print("14. Display Points Table")
                    print("-1. Logout")

                    ch = int(input("Enter choice> "))

                    if ch == -1:
                        print("Bye!")
                        exit()
                    # else:
                    #     dispatchUser(ch)
    except Exception as e:
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
