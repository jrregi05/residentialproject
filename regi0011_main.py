import arcpy, pprint
from arcpy import env
from pprint import pprint
sys.path.append("D:\\OU\\Summer2022\\SpatialProgramming\\Term Project\\Final_Test_Shapefiles")
import regi0011_module as mod

env.workspace = "D:\\OU\\Summer2022\\SpatialProgramming\\Term Project\\Final_Test_Shapefiles"
env.overwriteOutput = True

print("Hello and welcome to the OKC Metro ideal neighborhood finding software. Before we begin we need to gather information.")

hasKids = input("Do you have any children? Please answer with 'Yes' or 'No'.")
kidsAges = []

if hasKids == "Yes":
      privPub = input("Do you want to live near a private or public school? Please answer with 'Private' or 'Public'.")
      privPubSchools = mod.findPrivPub(privPub)
      numKids = int(input("How many kids do you have who are in school? Please enter with a number only."))
      if numKids > 1:
          kidsAges = input("What are their ages? Please answer with the ages separated by a space. EX: '7 9 13' to indicate their ages are 7 years, 9 years, and 13 years old.").split(" ")
          kidsSchools = mod.findSchools(kidsAges)
      else:
          kidsAges.append(int(input("How old is your child? Please answer with a number.")))
          kidsSchools = mod.findSchools(kidsAges)

householdIncome = int(input("Please enter your household income, rounded to the nearest thousand. EX: if your income is $52,568, please input $52,500"))
housholdSchools = mod.bgIncome(householdIncome)


mod.finalOutput()
