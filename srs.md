# Software Requirements Specification Document

This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/) and be sure that your group has a `main` branch with this document and the entire [template repository codebase](https://github.com/david-gary/onlineStoreTemplate) either forked or downloaded and copied into your group's repository. If you have arranged to use a different codebase as a template, you do not need to have the original template included, but a `main` branch is still required.

## Group Members

* [Alec](mmailto:asteene@uncc.edu)
* [Jack](mmailto:jdougl39@uncc.edu)
<<<<<<< HEAD
* [Nick](mmailto:nmatherl@uncc.edu)
* [Mansoor](mmailto:mmoham18@uncc.edu)
=======
* [Name](mmailto:email@uncc.edu)
* [Name](mmailto:email@uncc.edu)
>>>>>>> origin/main

## Revisions

When a change is made to the document, a new revision should be created. The revision should be added to the table below with all information filled out.

| Version | Date | Description | Author | Reviewed By |
| --- | --- | --- | --- | --- |
| 1.0 | 03/22/23 | Initial draft | [David Gary](mailto:dgary9@uncc.edu) | [David Gary](mailto:dgary@uncc.edu) |

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Constraints](#constraints)
4. [Use Cases](#use-cases)
5. [User Stories](#user-stories)
6. [Glossary](#glossary)

## Introduction

In this section, you should give a brief overview of what your project will be. Describe the software system you are building and what problems it solves. You should also give a short description of the stakeholders (users of the system) and what their needs are. There is no set formatting requirement, but you should maintain a consistent structure across future sections. Not all members must contribute to this section.

## Requirements

Each group member must supply at least three functional requirements for the project. Each requirement should be written in the following format:

- **REQ-1**: the user should be able to create orders.
    - **description**: the user should be able to put multiple food items into an order, the the order gets created when the user is finished adding items
    - **type**: functional
    - **priority**: 1
    - **rationale**: the user needs to be able to create orders in order for the kitchen to complete them
    - **testing**: we could test this by showing the contents of the completed order once the order is completed
- **REQ-2**: the orders should get stored in a database
    - **description**: once the orders are completed, they should get stored in a database so they can get acessed lated when needed
    - **type**: functional
    - **priority**: 1
    - **rationale**: the kitchen should be able to access the orders so they can fulfill them
    - **testing**: we could show a list of completed orders whenever a new order is completed
- **REQ-3**: be able to make changes to completed orders
    - **description**: once the orders are completed, a user should be able to change the order in case a mistake is made
    - **type**: functional
    - **priority**: 2
    - **rationale**: in case a customer changes their mind, or a user makes a mistake, the completed orders need to be changable
    - **testing**: we could create an order, then change it to see if the corresponding order on the order list is changed.
- **REQ-4** : track sales and customer data
    - **description**: keep a record of sales data that can be put into a report that would help a user make business decisions
    - **type**: functional
    - **rationale**: a user would be able to make business decisions based on this data, so it would be useful to track and report.
- **REQ-5**: manager login with increased authorization
    - **description**: allow for two different types of accounts, with different levels of authorization
    - **type**: functional
    - **rationale**: only managers should have the authorization to perform certain tasks, such as take items of an order after it has ben placed, and create accounts for new users.
- **REQ-6**: print receipt to .txt file
    - **description**: similate printing a receipt to a printer by printing an itemized reciept to a .txt file
    - **type**: functional
    - **rationale**: there needs to be a physical record of purchases, so the software should be able to provide that 
- **REQ-7:**
  - **Description:** There should be an interface that shows the layout of the dining room, where employees can select a table to open up the table's active tab or open up a blank tab if one is not already open for the table
  - **Type:** Functioal
  - **Priority:** 2
  - **Rationale:** The employees should be able to easily access the tabs for their tables. Displaying it this way could easily help keep track of the 'ole "what goes where" conundrum
  - **Testing:** We can interact with each table set up, with or without a tab currently set up, and see if the current tab is displayed properly/a blank one is set up. We need to make sure that the tab created is properly stored in the database and accessed 
- **REQ-8:**
  - **Description:** The system should keep track of the total number of tickets made that day
  - **Type:** Functional
  - **Priority:** 4
  - **Rationale:** The managers and people using the system to decide staffing could use this information to better determine how many servers are needed.
  - **Testing:** We create and close out different sets of tickets and verify that the "total" number output matches the number created
- **REQ-9:**
  - **Description:** The system should keep track of when an employee arrives to work (clocks in) and when they end their shift (clocks out)
  - **Type:** Functional
  - **Priority:** 3
  - **Rationale:** The restaraunt needs to know the time an employee works in order to properly compensate them
  - **Testing:** We can have a number of employees clock in and ensure that the time on shift is being displayed propeerly


* **ID:** A unique identifier for the requirement. This should be a number that is unique across the entire document (something like REQ-1, REQ-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Description:** A short description of the requirement. This should be a single sentence that describes the requirement. Do not replace the word `Description` with the actual description. Put the description in the space where these instructions are written. Maintain that practice for all future sections.
  * **Type:** The type of requirement. Should be either `Functional` or `Non-Functional`.
  * **Priority:** The priority of the requirement. This should be a number between 1 and 5, with 1 being the highest priority and 5 being the lowest priority.
  * **Rationale:** A short description of why the requirement is important. This should be a single sentence that describes why the requirement is important.
  * **Testing:** A short description of how the requirement can be tested. This should be a single sentence that describes how the requirement can be tested.
* **ID:** A unique identifier for the requirement. This should be a number that is unique across the entire document (something like REQ-1, REQ-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Description:** A short description of the requirement. This should be a single sentence that describes the requirement.
  * **Type:** The type of requirement. Should be either `Functional` or `Non-Functional`.
  * **Priority:** The priority of the requirement. This should be a number between 1 and 5, with 1 being the highest priority and 5 being the lowest priority.
  * **Rationale:** A short description of why the requirement is important. This should be a single sentence that describes why the requirement is important.
  * **Testing:** A short description of how the requirement can be tested. This should be a single sentence that describes how the requirement can be tested.

## Constraints

In this section, you should list any constraints that you have for the project. Each group member must supply at least two constraints. These can be constraints on the project itself, the software system, or the stakeholders. Constraints can be anything that limits the scope of the project. For example, that this project's template code is written using Flask and Python constitutes a constraint on the backend of the project. Constraints can also be things like the required timeline of the project. Be creative.
- CONST-1: user should only be able to create orders if they have a server account
- CONST-2: only users with proper permissions should be able to view sales and user data
- CONST-3:
    All functions written by all team members must have proper documentation strings and commenting in order to ensure readability by all team members.
- CONST-4:
    The Database must be organized in terms of the table. A check must be attributed to a table, which a user can then access the table to open a check on that table, and close the check on that table. Additionally, only one check can be open on one table. 
- **CONST-5**: the software should be able to run on a simple, inexpensive computer or tablet
- **CONST-6**: the software must be produced before the end of the semester

CONST-1:
    All functions written by all team members must have proper documentation strings and commenting in order to ensure readability by all team members.
CONST-2:
    The Database must be organized in terms of the table. A check must be attributed to a table, which a user can then access the table to open a check on that table, and close the check on that table. Additionally, only one check can be open on one table. 

## Use Cases

In this section, you should list use cases for the project. Use cases are a thorough description of how the system will be used. Each group member must supply at least two use cases. Each use case should be written in the following format:

- **UC-1**: create and index orders for completion
    * **description**: the user will click on the food that will be added to the order, and then click complete order when the order is completed, it will then go back to the main screen where there is a create order button for each table, and a list of all current orders on the side
    * **actors**: servers, who will make the orders, and chefs, who will prepare the orders from the list
    * **preconditions**: code needs to have a button for each table, a way to create an order, and a list to the side of the tables with the orders on it.
    * **postconditions**: order must be listed on the side of the tables part of the software
- **UC-2**: create sales data for the owner to look at
    * **description: the owner of the store will be able to look at sales data for the day, with a number of each item sold
    * **actors: the owner of the store
    * **preconditions: the number of each item sold during the day will need to be tracked and put into a database
    * **postconditions: the database will be printed onto a page that only the manager can access
- **UC-3**:
    * **Description**: A system that allows a restaurant to manage customer sales.
    * **Actors**: Server, Customer
    * **Preconditions**: The customer must be in the brick and mortar store with money and place an order(s), and the server/cashier at the restaurant must take the order.
    * **Postconditions**: The restaurant gets paid and the customer gets their food. 
- **UC-4**:
    * **Description**: A system that allows someone to place an order at a restaurant.
    * **Actors**: Customer
    * **Preconditions**: Customer has money and wants to place an order.
    * **Postconditions**: Customer gets food and restaurant gets paid.
* **UC-5:**
  * **Description:** The employee will use the system to clock in and out for their shift
  * **Actors:** Employee
  * **Preconditions:**
    * Employee with a setup account
    * An interface to clock in
    * An interface to clock out
  * **Postconditions:**
    * The time needs to be accurately computed and stored so that the employee can receive pay

* **UC-6:**
  * **Description:** A manager will use the system to see sales for the day, displayed with information on hows much of each item is sold
  * **Actors:** Manager
  * **Preconditions:** A manager account set up, tickets being created properly, tickets beign closed out with their information being recorded, number of a certain item sold being increased as tickets are closed out, an interface to display the items sold
  * **Postconditions:** Manager has access to the sales for specific days and how many items were sold

* **ID:** A unique identifier for the use case. This should be a number that is unique across the entire document (something like UC-1, UC-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Description:** A description of the use case that gives the user a high-level overview of how the system is interacted with.
  * **Actors:** A list of the actors that are involved in the use case. Only include the actors that are directly involved. Actors are the people or things that interact with the system. For example, when ordering at a fast food restaurant, one might have the following actors: the customer, the cashier, and the cook. But only the customer and the cashier are directly involved in the use case of ordering food. The cook is not directly involved in the use case of ordering food.
  * **Preconditions:** A list of the preconditions for the use case. This should be a list of the preconditions for the use case, which are the conditions that must be met before the use case can be executed. Continuing with the restaurant example, the customer must have money in their wallet and the cashier must be logged in to the system before the use case of ordering food can be executed.
  * **Postconditions:** A list of the postconditions for the use case. This should be a list of the postconditions for the use case, which are the conditions that must be met after the use case has been executed. Continuing with the restaurant example, the customer must have their food and the cashier must have the customer's money after the use case of ordering food has been executed.

## User Stories

In this section, you should list user stories for the project. User stories are a short description of how a user will be interacting with the system. Each group member must supply at least two user stories. Each user story should be written in the following format:

- **US-1**:
    * **type of user**: server
    * **description**: the server will click on the table that they are currently serving, and fill out the order that the customer wants, then clicks complete order
- **US-2**:
    * **type of user**: manager
    * **description**: the manager will log on to his admin account to make changes to orders, he can also access the sales and customer data, he can use this information to pay taxes and see what items are the most popular.
-**US-3**:
  **Type**: Manager/Admin account
  **Description**: Create accounts, give account manager authorization, take items off of check, authorize discounts, plus all lower level permissions.
- **US-4**:
  * **Type**: Wait Staff level account
  * **Description**: Open tab, accept payment, close tab, add to tab, assign tab to table, make notes on the tab, submit order ticke* 
* **US-Alpha:**
  * **Type of User:** `Server`
  * **Description:** A server comes in for their shift at _le restaraunt_, opens the work computer, accesses the system, and clocks in. Once customers come in and are seated by a `Hostess`, the `Server` will visit and take their drink orders. After this, they will go to the computer/tablet with access to the system, sign in with their credentials, click on the corresponding table on the restaraunt model, and add their drinks to the tab. After this, they will do the same process for the customer's food orders. At the end of the meal, the server will "print out" a ticket for the customer, and use the POS to collect payment and tip. At the end of their shift, they will use the POS to clock out.
* **US-Beta**
  * **Type of User:** `Hostess`
  * **Description:** Hostess will use the POS to clock in. When a customer comes in, a hostess will sign in with their credentials, view open tables on the POS, and determine where to seat the customers. They will also use the POS to clock out at the end of their shift.

* **ID:** A unique identifier for the user story. This should be a number that is unique across the entire document (something like US-1, US-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Type of User:** The type of user that the user story is for. This should be a single word that describes the type of user. For example, a user story for a customer might be `Customer` and a user story for an administrator might be `Admin`.
  * **Description:** A description of the user story that gives a narrative from that user's perspective. This can be any length, but it must paint the picture of what the user wants to do, how they intend to do it, why they want to, and what they expect to happen.

## Glossary

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:

* **Term:** The term that is being defined. This should be a single word or phrase that is being defined.
  * **Definition:** A definition of the term. This should be a short description of the term that is being defined. This should be a single sentence that describes the term.
  * 
* **Term:** POS
  * **Definition** Acronym for Point Of Sale, a system that facilitates the sale of goods and collecting of compensation
* **Term:**
