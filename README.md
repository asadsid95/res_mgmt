# res_mgmt

### Goal of this program:

This program is a building management system. The following are **client's requirements**:
This system, operated by building's concierge (staff), will allow assigning residents to units, adding/removing parcel upon receiving/picking up.

**Product requirements:**
1. This system must keep record of all residents that have ever lived in a specific unit. This means keeping history of all residents.
2. This system must keep record of all parcels received by the resident. This means keeping history of all parcels.
3. This system must be able to send reminders via email to residents who haven't picked up their parcels after 48 hours.
4. This system should be able to send reminders via email to resident whose residence is coming to an end within 7 days.
5. This system should be operated by different staff members (different work shifts) while giving each member access to all info about residents, units and parcels.
6. This sytem should have login capabilities for different staff members
7. This system should be a web application
8. This system should provide reports (different frequencies) on units occupied, parcels picked-up/received in a duration.

- Must have(s): 1,2,3
- Nice to have(s) AKA focus on these once 'Must have(s)' are completed: 4,5,6,7,8

**Technical requirements**

- Storage: SQLite3  

- When creating units for building, number of units <= max capacity 
- When assigning residents to suites, suite # must be part of building and be vacant. Resident also get added into history list (of all residents to occupy that suite)
- When removing residents from suites, suite must be part of building and occupied by that resident
* assume one resident per suite. Resident become deactivated but remain in the history list 

- When assigning a parcel, it must match suite # and name of resident, add onto list of other parcels
- When removing parcels, all parcels get removed
- For parcels reminders, it should be include list of all parcels needing to be picked up

**User types**

- Concierge staff
- Residents

**User Journey:**
[link](https://miro.com/app/board/uXjVOY5yft8=/?invite_link_id=737696554129)

**Data model & ERD:**

- Table: Building
- - building_id INT (PK)
- - number_of_units INT

- Table: Suites
- - suite_id INT (PK)
- - building_id (FK)
- - suite_number INT
- - is_vacant BOOLEAN

- Table: Residents
- - resident_id INT (PK)
- - unit_id (FK)
- - name TEXT
- - email TEXT
- - lease_start_date DATETIME/TEXT
- - lease_END_date DATETIME/TEXT
- - is_active BOOLEAN

- Table: Parcels
- - parcel_id INT (PK)
- - resident_id INT (FK)
- - courier TEXT
- - time_check_in DATETIME/TEXT
- - time_check_out DATETIME/TEXT
- - picked_up BOOLEAN


~~Client wants resident's directory and parcel management feature for residents, to be used by Concierge.~~
 
 ~~- Add/remove residents into unit; shows on main page~~
 ~~- Add/remove packages for resident/unit; shows on main page~~

 ~~- unit occupied by one resident~~

 ~~- 3 types of parcels; no limit on unit; reminder sent to user after 2 days of no-pickup~~

Product requirement:

 - Able to add package(s) received for each unit
 - Unit numbers who have picked the parcel today
 - Who has picked the parcel for unit xxx (eg: 201)
 - Check the unit numbers who didn't pick the parcel in 24 hours.
 - How many parcels were delivered by Amazon today.
 - How many parcels were delivered by Purolator last week.
 - How many items were not picked after 2 days.
 - What was the heaviest package and for which unit today?


~~List all features and entities:~~
~~Features (E - essential & NE - Non-essential):~~
~~- - Add residents to Unit (E)~~
~~- - Remove residents to Unit (E)~~
~~- - Add parcels to unit (E)~~
~~- - Add parcels to Unit (E)~~
~~- - Email resident if parcel not picked up after 2days(NE)~~

~~- Entities:~~
~~-GUI~~
~~- Database~~