import pandas as pd
def analyze_salaries(file_path, output_path):
    try:
        df = pd.read_csv(file_path)
        if 'Department' not in df.columns or 'Salary' not in df.columns:
            raise ValueError("Missing required columns: 'Department' or 'Salary'")
        df = df.dropna(subset=['Department', 'Salary'])
        df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
        df = df.dropna(subset=['Salary'])
        result = df.groupby('Department').agg(total_salary=('Salary', 'sum'),average_salary=('Salary', 'mean')).reset_index()
        result.to_csv(output_path, index=False)
        print(f"Analysis saved to {output_path}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

input_file = 'employee.csv'
output_file = 'salary_analysis.csv'
analyze_salaries(input_file, output_file)

