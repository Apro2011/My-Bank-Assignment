# My-Bank-Assignment

## Project Setup
1. Created and ran a virtual environment called "env".
2. Installed Django, graphene-django, django-extensions
3. Completed the usual setup for Django and graphene with "url for graphiql is 'gql/'"
4. "mysite" is my project root and "myapp" is my application

## Working with the CSV data
1. Created models according to the CSV file headings (bank_data/bank_branches.csv) with "ifsc" as the primary key
2. Created a "scripts" folder inside there is "load_data.py" file which includes the script for uploading csv data to the database through models.
3. "csv" package has been used to read the csv file and "django-extensions" has been used to run the script -> "python manage.py runscript load_data" (This will take some time)
4. After that graphene schema has been made in the "mysite/schema.py" with the "Query" class inside the same file.
5. Two queries have been made which you can use in "graphiql" browser
    1 -> ```
    
          query {
              detailsByBankBranch(bankBranch: "MOBILE BANK") {
                ifsc
                city
                bankId
                branch
                bankName
                state
                district
                address
              }
            }

         ```
         For Bank Details by branch
         
   2 -> ```
   
        query {
            details {
              ifsc
              city
              bankId
              branch
              bankName
              state
              district
              address
            }
          }
       ```
       For All Bank Details
       
 6. Tests are written for the first query in "tests/test_schema.py" file.
 7. I have added the Database db.sqlite3 so that no one needs to upload the data from csv file.
 
 ### So that's how the above problem is solved which took some hours to complete as I was using CSV for first time.
