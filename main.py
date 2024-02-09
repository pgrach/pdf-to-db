import camelot
import pandas as pd

def extract_data_from_pdf(pdf_path):
  """Extracts data from a PDF file and converts it into a pandas DataFrame.

  Args:
    pdf_path: The path to the PDF file.

  Returns:
    A pandas DataFrame containing the extracted data.
  """

  tables = camelot.read_pdf(pdf_path, flavor='stream', pages='all')

  # Extract data from each table
  data = []
  for table in tables:
    df = table.df.iloc[:-1]  # Remove the last row (total)
    if df.shape[1] > 2:  # Check if there are more than 2 columns
      taxonomy = df.iloc[0, 0]
      companies = df.iloc[1:, 0].tolist()
      data.extend([(taxonomy, company) for company in companies])

  # Create a pandas DataFrame
  df = pd.DataFrame(data, columns=['taxonomy', 'company'])

  return df

# Save the extracted data to a CSV file
data = extract_data_from_pdf('path/to/your/pdf.pdf')
data.to_csv('data.csv', index=False)
