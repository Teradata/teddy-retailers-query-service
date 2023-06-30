# Introduction

Learn how to use Teradata Query Service to query and access the Analytics Database through REST API. 

### Teradata Query Service

[Teradata Query Service](https://docs.teradata.com/r/Teradata-Query-Service-Installation-Configuration-and-Usage-Guide-for-Customers/April-2022/Overview/Teradata-Query-Service) is a REST API for Vantage to run standard SQL statements without managing client-side drivers.<br>
It lets developer query a Teradata-supported database from web pages, mobile devices, or scripting language using HTTP as the wire protocol and JSON as the data interchange format. 
<br>
Query Service provides APIs to:
*   Configure Teradata-supported systems
*   Submit SQL queries and access responses
*   Create database sessions
*   Access database and object metadata

## Prerequisites

- Code IDE
- Python 3.X (https://www.python.org/downloads/)
- ClearScape Analytics Experience Account (https://clearscape.teradata.com/register-user)

## About Project

<div align="center">

![Architecture](/img/about_project.PNG)

</div>

A Flask based web application that queries the Teradata database using Teradata Query Service.

## Steps

### Step 1: ClearScape Setup

Sign in to your [ClearScape Analytics Experience account](https://clearscape.teradata.com/sign-in) to create and access database with Query Service.  

<div align="center">

![Sign In](/img/sign_in.PNG)

</div>

Once you have signed in, click on **CREATE ENVIRONMENT**

<div align="center">

![Create Environment](/img/create_env.PNG)

</div>

Then, you need to provide -
* An _environment name_

  * A contextual name like 'Demo'       

* A _Database password_

  * A password of your choice
  * >Note it down for using it later in the code

* _Region_

  * Select one from the dropdown

<div align="center">

![environment values](/img/env_values.PNG)

</div>

It will open a new page showing your environment in Teradata Vantage on ClearScape Analytics Experience.

<div align="center">

![environment running](/img/final_page.PNG)

</div>

Congratulations you are all set to work with Teradata Query Service!


### Step 2: Create .env file

After you have cloned the project, create `.env` file inside it.

<div align="center" style="width:200px; height:200px">

![.env structure](/img/env_stru.PNG)

</div>

For connecting with the created ClearScape Analytics Experience environment, we need to provide -
* Host URL,
* User name, and
* Database password

Copy the _Host_ and _Username_ from the Step 1 and _Password_ is the database password we provided when created the environment.

Your .env file will look like this -

``` bash
# Environment Values
TD_HOST='HOST' # Host URL
TD_USER='demo_user' # default user name
TD_PASSWORD='DATABASE_PASSWORD' # your database pasword
```

> Replace **HOST** and **DATABASE_PASSWORD** with your values

### Step 3: Sample Data

The most important step is to upload the sample data to the environment.

There are two ways to do this -
1. Using a SQL client software, like [DBeaver](https://dbeaver.io/download/)
2. With the code (Python in our case)

We have incorporated the second option in the project. <br>

In the freshly cloned project, you will find [`data_load.sql`](/mock_data/data_load.sql) file containing SQL query to create a database and a table.

``` sql
CREATE DATABASE teddy_retailers_warehouse
AS PERMANENT = 110e6;
CREATE TABLE teddy_retailers_warehouse.customers_tvl AS
	(
		SELECT CAST(customer_id as CHAR(5)) as customer_id, email, bought_items, tlv, last_ordered  FROM 
		(
	    	LOCATION='/gs/storage.googleapis.com/clearscape_analytics_demo_data/DEMO_dbtAdvanced/customers_tlv.csv'
		) as d
)  WITH DATA;
```
The `customer_tlv.csv` file has following information -
* _customer_id_
* _email_
* _bought_items_
* _tlv_
* _last_ordered_

The CSV data is used here to calculate discount for customers based on their shopping habit. <br>

If you wish to check the SQL query separately, visit our [Query Service tutorial](https://quickstarts.teradata.com/query-service/send-queries-using-rest-api.html) page. <br>

> There is [`orders.json`](/mock_data/orders.json) file that contains product details and acts as Transactional DB.


### Step 4: Python virtual environment and requirements

Create a [Python virtual environment](https://docs.python.org/3/library/venv.html) and install the dependencies required for this project -


``` bash
$ pip install -r requirements.txt
```

You have everything required to run this project on your local machine.

### Step 5: Run the Project

The project is based on Flask, a micro web framework written in Python. <br>

Copy and paste below command to run the project -

``` bash
 flask --app .\teddy_qs.py run
 ```
Copy the address, http://127.0.0.1:5000 and paste it in your browser

 <div align="center">

![Flask run](/img/flask_run.PNG)

</div>

The browser should show "Teddy Retailers - Your Order" page. You can click on `Select a Customer` and get the information of different customers.

 <div align="center">

![Flask run](/img/result.PNG)

</div>
