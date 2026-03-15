# varroc_noida.py

# Optimized script with enhancements

# 1. Production count resets on new date
from datetime import datetime
import pandas as pd

class ProductionCounter:
    def __init__(self):
        self.production_count = 0
        self.current_date = self.get_today_date()

    def get_today_date(self):
        return datetime.now().date()

    def reset_count_if_new_day(self):
        today = self.get_today_date()
        if today != self.current_date:
            self.production_count = 0
            self.current_date = today

# 2. Export popup closes on any button click
class ExportPopup:
    def close_popup(self):
        print("Popup closed")  # Placeholder for GUI functionality

# 3. Excel exports only filtered data from table
class ExcelExporter:
    def export_filtered_data(self, filtered_data):
        filtered_data.to_excel('filtered_data.xlsx', index=False)

# 4. Sensor debouncing to prevent fast counting
class Sensor:
    def __init__(self):
        self.last_trigger_time = 0
        self.debounce_delay = 0.5  # seconds

    def read_sensor(self):
        current_time = self.get_current_time()
        if current_time - self.last_trigger_time > self.debounce_delay:
            self.last_trigger_time = current_time
            return True  # Count production
        return False  # Debounce trigger

# 5. Model count display
class ModelCountDisplay:
    def display_count(self, model_name, count):
        print(f"{model_name} count: {count}")

# 6. Grid background color change
GRID_BACKGROUND_COLOR = '#f0f0f0'  # light grey

# 7. Yellow slider buttons and white slider track
SLIDER_BUTTON_COLOR = 'yellow'
SLIDER_TRACK_COLOR = 'white'

# 8. Dropdown styling with yellow hover
DROPDOWN_HOVER_COLOR = 'yellow'

# 9. Calendar date selection with yellow circles
CALENDAR_DATE_SELECTION_COLOR = 'yellow'

# 10. Reset button spacing
RESET_BUTTON_SPACING = '10px'

# 11. Date column in table
class DataFrameWithDate:
    def __init__(self):
        self.df = pd.DataFrame(columns=['Date', 'Value'])

# 12. Column width adjustments
COLUMN_WIDTHS = {'Date': '100px', 'Value': '200px'}

# Main execution would go here if this were a script.

