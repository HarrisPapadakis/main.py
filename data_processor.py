import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    DataFrame: The loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return None

def process_data(data):
    """
    Process the data to compute basic statistics.
    
    Parameters:
    data (DataFrame): The data to process.
    
    Returns:
    dict: A dictionary with basic statistics.
    """
    if data is None:
        print("No data to process.")
        return {}

    stats = {
        'mean': data.mean().to_dict(),
        'median': data.median().to_dict(),
        'std_dev': data.std().to_dict()
    }
    return stats

def save_stats(stats, output_file):
    """
    Save statistics to a JSON file.
    
    Parameters:
    stats (dict): The statistics to save.
    output_file (str): The path to the output JSON file.
    """
    try:
        pd.DataFrame(stats).to_json(output_file, orient='index')
        print(f"Statistics saved to {output_file}")
    except Exception as e:
        print(f"Error saving statistics to {output_file}: {e}")

def main():
    input_file = 'data.csv'  # Replace with your CSV file path
    output_file = 'stats.json'  # Replace with your desired output file path

    data = load_data(input_file)
    stats = process_data(data)
    save_stats(stats, output_file)

if __name__ == "__main__":
    main()

