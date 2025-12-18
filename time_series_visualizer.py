import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Importar y limpiar datos
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Filtrar el 2.5% inferior y superior
lower = df['value'].quantile(0.025)
upper = df['value'].quantile(0.975)
df = df[(df['value'] >= lower) & (df['value'] <= upper)]

# 2️⃣ Función gráfico de líneas
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(15,5))
    ax.plot(df.index, df['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    fig.savefig('line_plot.png')
    return fig

# 3️⃣ Función gráfico de barras
def draw_bar_plot():
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_bar = df_bar.groupby(['year','month'])['value'].mean().unstack()
    
    fig = df_bar.plot(kind='bar', figsize=(15,10)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=[
        'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'
    ])
    fig.savefig('bar_plot.png')
    return fig

# 4️⃣ Función gráficos de caja
def draw_box_plot():
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month
    df_box['month_name'] = df_box.index.strftime('%b')
    
    df_box['month_name'] = pd.Categorical(
        df_box['month_name'], 
        categories=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], 
        ordered=True
    )
    
    fig, axes = plt.subplots(1, 2, figsize=(20,6))
    
    # Year-wise
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Month-wise
    sns.box



