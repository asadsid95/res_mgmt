# res_mgmt

Client wants resident's directory and parcel management feature for residents, to be used by Concierge.

Product requirement:

 - Add/remove residents into unit; shows on main page
 - Add/remove packages for resident/unit; shows on main page

 - unit occupied by one resident 

 - 3 types of parcels; no limit on unit; reminder sent to user after 24h of no-pickup 

 - Able to add package(s) received for each unit
 - Unit numbers who have picked the parcel today
 - Who has picked the parcel for unit xxx (eg: 201)
 - Check the unit numbers who didn't pick the parcel in 24 hours.
 - How many parcels were delivered by Amazon today.
 - How many parcels were delivered by Purolator last week.
 - How many items were not picked after 2 days.
 - What was the heaviest package and for which unit today?


    
Analyzing client requirements for software requirements:

1.  Storing data of resident and packages in DB:

    Residents directory:
    - add resident with various details 
    - - Name, unit # 
    - remove resident
    
    Parcel management feature:
    - add package
    - - assign resident name, unit number, courier, weight, checked time

2.  Make GUI (tkinter) to show management features