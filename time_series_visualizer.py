import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import calendar
# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates = ["date"],index_col='date')

# Clean data
df = df[(df['value'] >= (df['value'].quantile(0.025))) & 
    (df['value'] <= (df['value'].quantile(0.975)))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20, 6.3))
    plt.plot(df['value'], color="darkred")
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df_bar.index.month
    month_list = list(set(df_bar.index.month.tolist()))
    month_list = [calendar.month_name[i] for i in month_list]
    df_bar['year'] = df_bar.index.year
    df_bar = (df_bar.groupby(['year', 'month'])['value'].mean()).unstack()
    # Draw bar plot
    fig = df_bar.plot(figsize=(20,16), legend=True, kind='bar').figure
    plt.legend(title = 'Months', labels = month_list, fontsize=20)
    plt.xlabel('Years', fontsize=20)
    plt.ylabel('Average Page Views', fontsize=20)



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    months_list = list(calendar.month_abbr)[1:]
    
    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(20,8))
    
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0]).set(xlabel = "Year", ylabel = "Page Views", title = "Year-wise Box Plot (Trend)")
    sns.boxplot(x='month',y='value',data=df_box,order=months_list,ax=axes[1]).set(xlabel = "Month", ylabel = "Page Views", title = "Month-wise Box Plot (Seasonality)")
    fig.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
