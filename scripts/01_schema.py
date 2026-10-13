
import psycopg2
import configuration

conn = None

try:
    # Step 1: Connect to PostgreSQL
    conn = psycopg2.connect(
        host=configuration.host,
        user=configuration.username,
        password=configuration.password,
        port=configuration.port,
        database=configuration.database_name
    )

    cur = conn.cursor()

    # Step 2: Create customers table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            Customer_ID SERIAL PRIMARY KEY,
            Customer_Name VARCHAR(100) NOT NULL,
            Gender VARCHAR(10) NOT NULL,
            Age INT NOT NULL,
            Age_Group VARCHAR(20),
            Date_of_Birth DATE,
            Email VARCHAR(100) UNIQUE NOT NULL,
            Phone VARCHAR(15) UNIQUE NOT NULL,
            City VARCHAR(50),
            State VARCHAR(50),
            Pincode VARCHAR(10),
            Registration_Date DATE,
            Customer_Tier VARCHAR(20),
            Total_Orders INT,
            Total_Spent DECIMAL(10, 2)
        );
    """)

    # Step 3: Create products table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            Product_ID SERIAL PRIMARY KEY,
            Product_Name VARCHAR(100) NOT NULL,
            Category VARCHAR(50),
            Brand VARCHAR(50),
            Original_Price DECIMAL(10, 2) NOT NULL,
            Discount_Percent DECIMAL(5, 2),
            Discount_Amount DECIMAL(10, 2),
            Selling_Price DECIMAL(10, 2),
            Stock_Quantity INT,
            Weight_kg DECIMAL(5, 2),
            Avg_Rating DECIMAL(3, 2),
            Total_Reviews INT
        );
    """)

    # Step 4: Create sales table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            Order_ID SERIAL PRIMARY KEY,
            Customer_ID INT REFERENCES customers(Customer_ID),
            Product_ID INT REFERENCES products(Product_ID),
            Order_Date DATE,
            Order_Time TIME,
            Delivery_Date DATE,
            Quantity INT,
            Unit_Price DECIMAL(10, 2),
            Order_Value DECIMAL(10, 2),
            Shipping_Cost DECIMAL(10, 2),
            Coupon_Code VARCHAR(20),
            Coupon_Discount DECIMAL(10, 2),
            Total_Amount DECIMAL(10, 2),
            Payment_Mode VARCHAR(20),
            Order_Status VARCHAR(20),
            Rating DECIMAL(3, 2),
            Review_Text TEXT,
            City VARCHAR(50),
            State VARCHAR(50),
            Customer_Age INT,
            Customer_Age_Group VARCHAR(20)
        );
    """)

    # Step 5: Save the changes
    conn.commit()

    print("All three tables created successfully!")

except psycopg2.Error as error:
    print("PostgreSQL error:", error)

finally:
    if conn is not None:
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")
