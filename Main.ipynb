import pandas as pd
import datetime

# Load the dataset and handle the case where the file might not be found.
try:
    file = pd.read_csv('romanianearthquakes.csv')
except FileNotFoundError:
    print("Error: The file 'romanianearthquakes.csv' was not found.")
    exit()

# Function to display the top N sorted rows of a given column with a custom label.
def display_sorted_data(column, ascending=True, top_n=10, label="results"):
    try:
        sorted_data = file.sort_values(by=column, ascending=ascending).head(top_n)
        print(f"\nTop {top_n} {label} ({'Ascending' if ascending else 'Descending'}):")
        print(sorted_data.to_string(index=False))
    except KeyError:
        print(f"Column '{column}' not found in the dataset.")

# Function to display statistical analysis for a specific column.
def display_stat(column, stat_func, stat_name):
    try:
        result = stat_func(file[column])
        print(f"\n{stat_name} {column}: {result}")
    except KeyError:
        print(f"Column '{column}' not found in the dataset.")
    except Exception as e:
        print(f"Error calculating {stat_name}: {e}")

# Display the top 10 earthquakes by magnitude in descending order.
def greatest10magnitude():
    display_sorted_data('magnitude', ascending=False, label="earthquakes by magnitude")

# Display the lowest 10 earthquakes by magnitude in ascending order.
def lowest10magnitude():
    display_sorted_data('magnitude', ascending=True, label="earthquakes by magnitude")

# Search for earthquakes based on a user-provided magnitude.
def usermagnitude():
    try:
        usermag = float(input("Enter a magnitude: "))
        result = file[file['magnitude'] == usermag]
        if result.empty:
            print(f"No earthquakes found with magnitude == {usermag}.")
        else:
            print(f"\nEarthquakes with magnitude == {usermag}:")
            print(result.to_string(index=False))
    except ValueError:
        print("Invalid magnitude input. Please enter a numeric value.")

# Display the top 10 zones with the most earthquake occurrences.
def top10zone():
    print("\nTop 10 zones by earthquake count:")
    print(file['zone description'].value_counts().head(10).to_string())

# Display zones with the fewest earthquake occurrences.
def lowest10zone():
    print("\nZones with the fewest earthquake occurrences:")
    print(file['zone description'].value_counts(ascending=True).head(10).to_string())

# Display the top 10 earthquakes by depth in descending order.
def top10depth():
    display_sorted_data('depth', ascending=False, label="earthquakes by depth")

# Display the lowest 10 earthquakes by depth in ascending order.
def lowest10depth():
    display_sorted_data('depth', ascending=True, label="earthquakes by depth")

# Display the earliest 10 earthquakes by date.
def earliest10():
    display_sorted_data('dateTime', ascending=True, label="earthquakes by date")

# Display the latest 10 earthquakes by date.
def latest10():
    display_sorted_data('dateTime', ascending=False, label="earthquakes by date")

# Display the average of the earthquake magnitude.
def average():
    display_stat('magnitude', pd.Series.mean, "Average")

# Display the average latitude.
def averagelatitude():
    display_stat('latitude', pd.Series.mean, "Average")

# Display the average longitude.
def averagelongitude():
    display_stat('longitude', pd.Series.mean, "Average")

# Display the median of the latitude values.
def medianlatitude():
    display_stat('latitude', pd.Series.median, "Median")

# Display the median of the longitude values.
def medianlongitude():
    display_stat('longitude', pd.Series.median, "Median")

# Filter earthquakes based on a date range provided by the user.
def filter_by_date():
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    try:
        file['dateTime'] = pd.to_datetime(file['dateTime'])
        filtered = file[(file['dateTime'] >= start_date) & (file['dateTime'] <= end_date)]
        if filtered.empty:
            print(f"No earthquakes found between {start_date} and {end_date}.")
        else:
            print(f"\nEarthquakes between {start_date} and {end_date}:")
            print(filtered.to_string(index=False))
    except Exception as e:
        print("Error filtering by date. Ensure the dates are in YYYY-MM-DD format.", e)

# Search for earthquakes based on a specific depth.
def searchfordepth():
    try:
        userinput = float(input("Enter a depth: "))
        result = file[file['depth'] == userinput]
        if result.empty:
            print(f"No earthquakes found with depth == {userinput}.")
        else:
            print(f"\nEarthquakes with depth == {userinput}:")
            print(result.to_string(index=False))
    except ValueError:
        print("Invalid depth input. Please enter a numeric value.")

# Analyze the correlation between magnitude and depth.
def correlation_magnitude_depth():
    try:
        correlation = file['magnitude'].corr(file['depth'])
        print(f"\nCorrelation between magnitude and depth: {correlation}")
        if correlation > 0:
            print("A positive correlation indicates that earthquakes with greater depth tend to have higher magnitudes.")
        elif correlation < 0:
            print("A negative correlation indicates that deeper earthquakes tend to have lower magnitudes.")
        else:
            print("No correlation between magnitude and depth.")
    except KeyError:
        print("Columns 'magnitude' or 'depth' not found in the dataset.")
    except Exception as e:
        print(f"Error calculating correlation: {e}")

# Main function to display the menu and execute user-selected options.
def main():
    # Menu options
    options = [
        "Greatest 10 Magnitude",
        "Lowest 10 Magnitude",
        "Search for a Magnitude",
        "Greatest 10 Zones",
        "Lowest 10 Zones",
        "Greatest 10 Depth",
        "Lowest 10 Depth",
        "Earliest 10",
        "Latest 10",
        "Average Magnitude",
        "Average Latitude",
        "Average Longitude",
        "Median Latitude",
        "Median Longitude",
        "Filter by Date Range",
        "Search for Depth",
        "Correlation Between Magnitude and Depth",
        "Exit"]

    while True:
        print("\nWelcome to Romania Earthquake Analysis")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(options):
                if choice == 1:
                    greatest10magnitude()
                elif choice == 2:
                    lowest10magnitude()
                elif choice == 3:
                    usermagnitude()
                elif choice == 4:
                    top10zone()
                elif choice == 5:
                    lowest10zone()
                elif choice == 6:
                    top10depth()
                elif choice == 7:
                    lowest10depth()
                elif choice == 8:
                    earliest10()
                elif choice == 9:
                    latest10()
                elif choice == 10:
                    average()
                elif choice == 11:
                    averagelatitude()
                elif choice == 12:
                    averagelongitude()
                elif choice == 13:
                    medianlatitude()
                elif choice == 14:
                    medianlongitude()
                elif choice == 15:
                    filter_by_date()
                elif choice == 16:
                    searchfordepth()
                elif choice == 17:
                    correlation_magnitude_depth()
                elif choice == 18:
                    print("Thank you for using Romania Earthquake Analysis!")
                    break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 18.")

if __name__ == "__main__":
    main()

