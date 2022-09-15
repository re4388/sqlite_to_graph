
import sqlite3, pandas , matplotlib.pyplot as plt

# replace this link to your local db file location
link = "C:\\projects\wits-active\\ts-aws-playground\\sqlite3\\starred.db"
conn = sqlite3.connect(link)


def runCode1():
    sql = """
    select sum(deaths) sum_deaths, country 
    from v_sars 
    group by Country 
    having sum_deaths > 0 
    order by sum_deaths desc 
    limit 5"""
    
    data = pandas.read_sql(sql, conn)

    xVal = data.Country
    yVal = data.sum_deaths
    plt.bar(xVal,yVal)
    plt.title("SARS Death in 2003")
    plt.show()

def runCode2():
    sql = """
    select 
        s_month, sum(deaths) as sum_deaths, sum(cases) as sum_cases 
    from v_month 
        group by n_month
    """

    data = pandas.read_sql(sql, conn) 

    x_val= data.s_month
    y1_val= data.sum_deaths
    y2_val= data.sum_cases
    
    plt.plot(x_val,y1_val, label = "Deaths")
    plt.plot(x_val,y2_val, label = "Cases")
    plt.legend()
    plt.title("SARS Death in 2003")
    plt.show()


# runCode1()
runCode2()