# Imports
from tkinter import *
from tkcalendar import DateEntry
import datetime as dt
import yfinance as yf
import mplfinance as mpf

def visualize():
    try:
        # Get Dates From DateEntry and Convert To Datetime
        from_date = cal_from.get_date()
        to_date = cal_to.get_date()

        start = dt.datetime(from_date.year, from_date.month, from_date.day)
        end = dt.datetime(to_date.year, to_date.month, to_date.day)

        # Load Ticker From Entry And Download Data
        ticker = text_ticker.get()
        data = yf.download(ticker, start=start, end=end)

        if data.empty:
            raise ValueError("No data found for the given ticker or date range.")

        # Restructure Data Into OHLC Format
        data = data[['Open', 'High', 'Low', 'Close']]

        # Plot The Candlestick Chart
        mpf.plot(data, type='candle', style='charles', title=f"{ticker} Share Price",
                 ylabel='Price', volume=False)

    except Exception as e:
        print(f"Error: {e}")

# Define Main Window
root = Tk()
root.title("Stock Visualizer")

# Add Components And Link Function
label_from = Label(root, text="From:")
label_from.pack()
cal_from = DateEntry(root, width=50, year=2010, month=1, day=1)
cal_from.pack(padx=10, pady=10)

label_to = Label(root, text="To:")
label_to.pack()
cal_to = DateEntry(root, width=50)
cal_to.pack(padx=10, pady=10)

label_ticker = Label(root, text="Ticker Symbol:")
label_ticker.pack()
text_ticker = Entry(root)
text_ticker.pack()

btn_visualize = Button(root, text="Visualize", command=visualize)
btn_visualize.pack()

root.mainloop()
