CREATE TABLE IF NOT EXISTS Salesman (
 Salesman_id TEXT PRIMARY KEY,
 name TEXT,
 city TEXT,
 Comission REAL
);
INSERT INTO Salesman(Salesman_id,city,Comission)VALUES
   ("5001","James Hoog","New York","0.15"),
   ("5002","Nail Knite","Paris","0.13"),
   ("5005","Pit Alex","London","0.11"),
   ("5006","Mc Lyon","Paris","0.14"),
   ("5007","Paul Adam","Rome","0.13"),
   ("5003","Lauson Hen","San Jose","0.12");

CREATE TABLE IF NOT EXISTS Customer(
 customer_id TEXT,
 cust_name TEXT PRIMARY KEY,
 city TEXT,
 grade TEXT,
 Salesman_id TEXT
);

INSERT INTO Customer(customer_id,cust_name,city,grade)VALUES
 ("3002","HANNES ALFVEN", "SWEDEN","100"),
  ("3007","LOUIS NEEL", 'FRANCE',),
  ("3005","PAUL", "FRANCE",),
  ("3008",'HAMILTON', 'SWEDEN',),
  ("3004",'BERNARD KELSON', 'GREMANY',),
  ("3009", 'JOSEPH', 'RUSSIA',),
  ("3003",'PHILIPS', 'USA',),
  ("3001",'MARTIN', 'USA',);
  