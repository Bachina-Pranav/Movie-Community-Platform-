import subprocess as sp
import pymysql
import pymysql.cursors


def NewEpisode():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        # Takes episode details as input
        row = {}
        print("Enter new episode's details: ")
        row["Ename"] = input("Episode name: ")
        row["Season_and_number"] = input("Season and episode number(in the form of 'S_ E_'): ")
        row["Upload_date"] = input("Upload date(DD-MM-YYYY): ")
        
        ##################################################
        
        query = "INSERT INTO Episode (Epname, Season_and_number, Upload_date) VALUES('%s', '%s', '%s')" % (
            row["Ename"], row["Season_and_number"], row["Upload_date"])

        # print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return



def UpdateWW():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        # Takes character details as input
        row = {}
        print("Updating status of White Walkers: ")
        row["Wname"]=input("Name of the whitewalker:")
        row["WStatus"] = input("Status(Alive or Dead): ")
        
        ##########################################################
        
        query = "UPDATE White_Walker SET Wstatus='%s' WHERE Wname='%s'" % (
            row["WStatus"], row["Wname"])

        # print(query)
        cur.execute(query)
        con.commit()

        print("Updated in Database")

    except Exception as e:
        con.rollback()
        print("Failed to update in database")
        print(">>>>>>>>>>>>>", e)

    return



def UpdateCh():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        # Takes character details as input
        row = {}
        print("Updating status of Character: ")

        name = (input("Name of Character (Fname Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Lname"] = name[1]
        row["CStatus"] = input("Status(Alive or Dead): ")
        
        ##########################################################
        
        query = "UPDATE Character_info SET Cstatus='%s' WHERE Fname='%s' AND Lname='%s'" % (
            row["CStatus"], row["Fname"],row["Lname"])

        # print(query)
        cur.execute(query)
        con.commit()

        print("Updated In Database")

    except Exception as e:
        con.rollback()
        print("Failed to update in database")
        print(">>>>>>>>>>>>>", e)

    return
    
def UpdateLord():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        # Takes character details as input
        row = {}
        print("Updating status of Lord of a region: ")
        row["Place"]=input("Name of the region: ")
        row["Lord"] = input("Name of new Lord: ")
        
        ##########################################################
        
        query = "UPDATE Region SET Lord='%s' WHERE Place='%s'" % (
            row["Lord"], row["Place"])

        # print(query)
        cur.execute(query)
        con.commit()

        print("Updated In Database")

    except Exception as e:
        con.rollback()
        print("Failed to update into database")
        print(">>>>>>>>>>>>>", e)

    return

def deleteSub():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        ##########################################################
        # Takes character details as input
        row = {}
        print("Deleting subscriber info: ")
        row["Username"]=input("Username of the subscriber: ")
        query = "DELETE FROM Subscriber WHERE Username='%s'" % (
           row["Username"])

        # print(query)
        cur.execute(query)
        con.commit()

        print("Deleted from Database")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

    return

def displaych():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        # Takes character details as input
        row = {}
        print("Displaying characters of a particular house: ")
        #row["Status"] = input("Status(Alive or dead): ")
        row["house"] = input("Enter the house name: ")
        ##########################################################
        
        query = "SELECT Fname,Lname FROM Character_info AS C,House AS H WHERE C.Sigil=H.Sigil AND H.Hname='%s'" % (
            row["house"])

        # print(query)
        cur.execute(query)
        con.commit()
        
        output=cur.fetchall()
        for x in output:
            print(x)
        
        print("Retrieved from Database")

    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return

def displaylord():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        # Takes character details as input
        row = {}
        ##########################################################
        
        query = "SELECT Place,Lord FROM Region"

        # print(query)
        cur.execute(query)
        con.commit()

        output=cur.fetchall()
        for x in output:
            print(x)
        
        print("Retrieved from Database")
        
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    return

def displaymaxreign():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        # Takes character details as input
        row = {}
        # row["start_time"] = input("Start time: ")
        # row["end_time"] = input("End time: ")
        
        ##########################################################
        # find = "SELECT Ename,Start,End FROM Event WHERE Start LIKE '" + row["start_time"] + "' AND End LIKE '" + row["end_time"] + "'"
        final_query = "SELECT MAX(duration) FROM The_King"
        query = "%s" % (
            final_query)

        # print(query)
        cur.execute(query)
        con.commit()

        output=cur.fetchall()
        for x in output:
            print(x)
        
        print("Retrieved from Database")

    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return

def kingslastnm():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        # Takes character details as input
        row = {}
        row["compare_string"] = input("String to search for: ")
        
        ##########################################################
        find = "SELECT Tfname,Tlname FROM The_King WHERE Tlname LIKE '%"+row["compare_string"]+"%'"
        query = "%s" % (
            find)

        # print(query)
        cur.execute(query)
        con.commit()
        output=cur.fetchall()
        for x in output:
            print(x)
        
        print("Retrieved from Database")


    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return

def chval():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        # Takes character details as input
        row = {}
        ##########################################################
        
        query = "SELECT Fname,Lname FROM Character_info C ,Weapon W,Animal A WHERE A.Type='Dragon' AND W.Material='Valaryian Steel' AND A.Ownedby_Fname=C.Fname AND A.Ownedby_Lname=C.Lname AND W.Weildedby_Fname=C.Fname AND W.Weildedby_Lname=C.Lname" 
        # print(query)
        cur.execute(query)
        con.commit()

        output=cur.fetchall()
        for x in output:
            print(x)
        
        print("Retrieved from Database")


    except Exception as e:
        con.rollback()
        print("Failed to retireve from database")
        print(">>>>>>>>>>>>>", e)

    return


def NewCharacter():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        # Takes character details as input
        row = {}
        print("Enter new character's details: ")
        name = (input("Name (Fname Lname): ")).split(' ')
        row["Fname"] =name[0]
        row["Lname"] = name[1]
        row["Gender"] = input("Gender: ")
        row["cStatus"] =input("Status: ")
        row["Born"] = input("Born on: ")
        row["Died"] =input("Died on: ")
        row["Portrayed_By"] = input("Portayed by: ")
        row["Place"] = input("Place: ")
        row["Ename"] = input("Event name: ")
        kname = (input("Killed by (Fname Lname): "))
        if(kname==""):
            row["Kfname"] = ""
            row["Klname"] = ""
        else:
            kname=kname.split(' ')
            row["Kfname"] = kname[0]
            row["Klname"] =kname[1]
        row["Sigil"] = input("Sigil: ")
        row["Oname"] = input("Name of the organization: ")
        row["Gname"] = input("Worships: ")
        
        if(row["Died"] == ""):
            row["Died"] = "NULL"
        if(row["Kfname"]==""):
            row["Kfname"]="NULL"
        if(row["Klname"]==""):
            row["Klname"]="NULL"
        if(row["Oname"]==""):
            row["Oname"]="NULL"
        if(row["Gname"]==""):
            row["Gname"]="NULL"
        query = "INSERT INTO Character_info (Fname, Lname, Gender, Cstatus, Died, Born, Portrayed_by, Place, Ename, Kfname, Klname, Sigil, Oname, Gname) VALUES('%s', '%s', '%s', '%s' , '%s' , '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            row["Fname"], row["Lname"], row["Gender"], row["cStatus"], row["Died"], row["Born"], row["Portrayed_By"], row["Place"], row["Ename"], row["Kfname"], row["Klname"], row["Sigil"], row["Oname"], row["Gname"])

        # print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        NewCharacter()
    elif(ch == 2):
        NewEpisode()
    elif(ch == 3):
        UpdateWW()
    elif(ch == 4):
        UpdateCh()
    elif(ch == 5):
        UpdateLord()
    elif(ch == 6):
        deleteSub()
    elif(ch == 7):
        displaych()
    elif(ch == 8):
        displaylord()
    elif(ch == 9):
        displaymaxreign()
    elif(ch == 10):
        kingslastnm()
    elif(ch == 11):
        chval()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hardcode username and password
    username = "root"
    password = "11012004"

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              port=3306,
                              user="root",
                              password="11012004",
                              db='GOT',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of GOT Mini-world
                print("0. Logout")
                print("1. Add New Character")  # New charater is introduced
                print("2. Add New Episode")  # New episode is released
                print("3. Update status of white walker")  # White Walker just died
                print("4. Update status of character")  # Character just died
                print("5. Update Lord of region")  # New Lord takes over
                print("6. Delete Subscriber")  # Subscriber no longer uses service
                print("7. Display Characters belonging to a particular house")  # Display Characters belonging to a particular house
                print("8. Display Lords of all Regions")  # Display Lords of all Regions
                print("9. Display max reign of a King")  # Display max reign of a King
                print("10.Kings whose last name has xxxx ")  # Kings whose last name has xxxx
                print("11.Characters who wield Valyrian stell and have dragons")  # Characters who wield Valyrian stell and have dragons
                
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 0:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")