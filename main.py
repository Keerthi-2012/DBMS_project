import pymysql.cursors
from datetime import datetime

# Insert Functions
def seasonInsert(): pass
def matchInsert(): pass
def teamInsert(): pass
def playerInsert(): pass
def tossInsert(): pass
def venueInsert(): pass
def batsmanScoreInsert(): pass
def bowlerStatInsert(): pass

# Update Functions
def updateMatch(): pass
def updateTeam(): pass
def updatePlayer(): pass
def updateVenue(): pass
def updateBatsmanScore(): pass
def updateBowlerStat(): pass

# Delete / Archive Functions
def deleteTeams(): pass
def archivePlayerRecord(): pass
def deleteVenue(): pass

# Search Functions
def searchChampion(): pass
def searchMatch(): pass
def searchVenue(): pass
def searchTeam(): pass
def searchPlayer(): pass
def searchSeason(): pass

# Aggregate / Stats / List Functions
def aggregateVenueData(): pass
def matchResultofaTeam(): pass
def teamStatistics(): pass
def listCurrentTeams(): pass
def listMatchesbyDate(): pass
def listMatchResults(): pass
def venuesAvailable(): pass
def pointsTable(): pass


def dispatchAdmin(ch):
    """
    Function that maps helper functions to admin options entered
    """
    if ch == 1:
        seasonInsert()
    elif ch == 2:
        matchInsert()
    elif ch == 3:
        teamInsert()
    elif ch == 4:
        playerInsert()
    elif ch == 5:
        tossInsert()
    elif ch == 6:
        venueInsert()
    elif ch == 7:
        batsmanScoreInsert()
    elif ch == 8:
        bowlerStatInsert()
    elif ch == 9:
        updateMatch()
    elif ch == 10:
        updateTeam()
    elif ch == 11:
        updatePlayer()
    elif ch == 12:
        updateVenue()
    elif ch == 13:
        updateBatsmanScore()
    elif ch == 14:
        updateBowlerStat()
    elif ch == 15:
        deleteTeams()
    elif ch == 16:
        archivePlayerRecord()
    elif ch == 17:
        deleteVenue()
    elif ch == 18:
        searchChampion()
    elif ch == 19:
        searchMatch()
    elif ch == 20:
        searchVenue()
    elif ch == 21:
        searchTeam()
    elif ch == 22:
        searchPlayer()
    elif ch == 23:
        searchSeason()
    elif ch == 24:
        aggregateVenueData()
    elif ch == 25:
        matchResultofaTeam()
    elif ch == 26:
        teamStatistics()
    elif ch == 27:
        listCurrentTeams()
    elif ch == 28:
        listMatchesbyDate()
    elif ch == 29:
        listMatchResults()
    elif ch == 30:
        venuesAvailable()
    elif ch == 31:
        pointsTable()

def dispatchUser(ch):
    """
    Function that maps helper functions to regular user options entered
    """
    if ch == 1:
        searchChampion()
    elif ch == 2:
        searchMatch()
    elif ch == 3:
        searchVenue()
    elif ch == 4:
        searchTeam()
    elif ch == 5:
        searchPlayer()
    elif ch == 6:
        searchSeason()
    elif ch == 7:
        aggregateVenueData()
    elif ch == 8:
        matchResultofaTeam()
    elif ch == 9:
        teamStatistics()
    elif ch == 10:
        listCurrentTeams()
    elif ch == 11:
        listMatchesbyDate()
    elif ch == 12:
        listMatchResults()
    elif ch == 13:
        venuesAvailable()
    elif ch == 14:
        pointsTable()

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
