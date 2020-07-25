import sqlite3




def set_default():
    conn = sqlite3.connect('tryjoin1.db')
    cur = conn.cursor()

    cur.executescript("""
    CREATE TABLE IF NOT EXISTS COMPANY (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, COMPANY_NAME TEXT NOT NULL);
    INSERT INTO COMPANY (COMPANY_NAME) VALUES ('AGAPPE') ;        
    INSERT INTO COMPANY (COMPANY_NAME) VALUES ('BIOMEURIEX') ;    
    INSERT INTO COMPANY (COMPANY_NAME) VALUES ('ARKRAY') ;        
    INSERT INTO COMPANY (COMPANY_NAME) VALUES ('NIHON KOHDEN') ;  
    INSERT INTO COMPANY (COMPANY_NAME) VALUES ('BIOLAB');         
    """)


    cur.executescript("""CREATE TABLE IF NOT EXISTS PRODUCT (ID INTEGER , PRODUCT_NAME TEXT,PRICE INTEGER, UNIT INTEGER);
    INSERT INTO PRODUCT (ID, PRODUCT_NAME, PRICE, UNIT) VALUES (?,?,?,?) , (1,'BIO-CHEMISTRY', 100, 100);
    INSERT INTO PRODUCT (ID, PRODUCT_NAME, PRICE, UNIT) VALUES (?,?,?,?) , (1,'CELL-COUNTER', 100, 100);
    INSERT INTO PRODUCT (ID, PRODUCT_NAME, PRICE, UNIT) VALUES (?,?,?,?) , (1,'MISPA NANO', 100, 100);
    INSERT INTO PRODUCT (ID, PRODUCT_NAME, PRICE, UNIT) VALUES (?,?,?,?) , (1,'MISPA NEO', 100, 100);
    INSERT INTO PRODUCT (ID , PRODUCT_NAME , PRICE , UNIT) VALUES (?,?,?,?) , (2 , 'MINI VIDAS' , 100 , 100);
    INSERT INTO PRODUCT (ID , PRODUCT_NAME , PRICE , UNIT) VALUES (?,?,?,?) , (2 , 'VIDAS' , 100 , 100);
    INSERT INTO PRODUCT (ID , PRODUCT_NAME , PRICE , UNIT) VALUES (?,?,?,?) , (3 , 'PPD 10TU' , 100 , 100);
    INSERT INTO PRODUCT (ID , PRODUCT_NAME , PRICE , UNIT) VALUES (?,?,?,?) , (3 , 'PPD 2TU' , 100 , 100);
    INSERT INTO PRODUCT (ID , PRODUCT_NAME , PRICE , UNIT) VALUES (?,?,?,?) , (3 , 'PPD 5TU' , 100 , 100);
    INSERT INTO PRODUCT (ID , PRODUCT_NAME , PRICE , UNIT) VALUES (?,?,?,?) , (4 , 'CELL COUNTER 3' , 100 , 100);
    INSERT INTO PRODUCT (ID , PRODUCT_NAME , PRICE , UNIT) VALUES (?,?,?,?) , (4 , 'CELL COUNTER 5' , 100 , 100);
    INSERT INTO PRODUCT (ID , PRODUCT_NAME , PRICE , UNIT) VALUES (?,?,?,?) , (4 , 'REAGENTS' , 100 , 100);
    INSERT INTO PRODUCT (ID , PRODUCT_NAME , PRICE , UNIT) VALUES (?,?,?,?) , (5 , 'GIMSA STAIN' , 100 , 100);
    INSERT INTO PRODUCT (ID , PRODUCT_NAME , PRICE , UNIT) VALUES (?,?,?,?) , (5 , 'RAPID PAP' , 100 , 100);
    INSERT INTO PRODUCT (ID , PRODUCT_NAME , PRICE , UNIT) VALUES (?,?,?,?) , (5 , 'LIQUID SOLUTION' , 100 , 100);
    """)

    conn.commit()
    conn.close()

def do_query():
    conn = sqlite3.connect('tryjoin1.db')
    cur = conn.cursor()
    cur.execute('select COMPANY_NAME,PRODUCT_NAME from COMPANY,PRODUCT where COMPANY.ID = PRODUCT.ID')
    print(cur.fetchall()) 
    conn.commit()
    conn.close()

#set_default()
do_query()
    
