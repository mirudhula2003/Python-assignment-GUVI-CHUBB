import pandas as pd

try:
    df = pd.read_csv('code11.csv')

    if 'Product_ID' in df.columns and 'Name' in df.columns and 'Quantity' in df.columns:
        low_stock = df[df['Quantity'] < 10]

        if not low_stock.empty:
            print(low_stock)
        else:
            print("No products with low stock.")
    else:
        print("Error: Missing required columns in the CSV file.")
    
except FileNotFoundError:
    print("Error: The CSV file was not found.")
except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty.")
except pd.errors.ParserError:
    print("Error: The CSV file is malformed.")
except Exception as e:
    print(e)

