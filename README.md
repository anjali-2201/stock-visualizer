# Stock Visualizer  

A simple Python application that allows users to visualize historical stock data as candlestick charts. The user-friendly interface is built using `Tkinter`, and the application leverages `yfinance` to fetch stock data and `mplfinance` to create the candlestick charts.  

---

## Features  

- Input stock ticker symbols to retrieve historical stock data.  
- Select a date range using an interactive calendar widget.  
- Visualize the data as candlestick charts for better insights into stock performance.  

---

## Installation  

1. **Clone the Repository**  
   ```bash  
   git clone https://github.com/your-username/stock-visualizer.git  
   cd stock-visualizer  
   ```  

2. **Set Up the Environment**  
   Install the required Python libraries using `pip`:  
   ```bash  
   pip install tkcalendar yfinance mplfinance  
   ```  

3. **Run the Application**  
   Execute the script:  
   ```bash  
   python stock_visualizer.py  
   ```  

---

## Usage  

1. Launch the application.  
2. Select the start and end dates using the calendar widgets.  
3. Enter a valid stock ticker symbol (e.g., `AAPL` for Apple or `GOOGL` for Google).  
4. Click on the **Visualize** button to view the candlestick chart for the selected date range.  

---

## Example  

- **Input**: Ticker Symbol: `AAPL`, Date Range: `01-01-2020` to `01-01-2022`  
- **Output**: A candlestick chart showing Apple's stock prices within the selected range.  

---

## Dependencies  

- `tkinter` - For building the graphical user interface.  
- `tkcalendar` - For date selection widgets.  
- `yfinance` - For fetching historical stock data.  
- `mplfinance` - For plotting candlestick charts.  
