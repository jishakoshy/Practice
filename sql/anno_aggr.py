# Aggregation is the process of summarizing data by calculating a single value from
# a group of values. For example, you could use aggregation to calculate the total 
# sales for a product or the average age of customers.

# Annotation is the process of adding new columns to a table based on the 
# values in existing columns. For example, you could use annotation to add a column
# that calculates the discount for each product or a column that indicates the customer's region.

# eg:
# SELECT SUM(sales) AS total_sales
# FROM products;

# eg:
# SELECT product_name, price * 0.1 AS discount
# FROM products;

# group by 
# select company, count(*) from games group by company;