# Graph sqlite query result


## dataset prep
- data download link:https://www.kaggle.com/imdevskp/sars-outbreak-2003-complete-dataset
- csv data I use: sars_2003_complete_dataset_clean.csv

## import csv into xx

- import via SQLiteStudio (I use win10)
- tools -> import
- In this case, tick "fist line represent CSV col name"


# create view

- In this step, the csv is imported in the sqlite
- let's create two views

```sql
create view v_sars 
as
select 
    date, 
    country, 
    `Cumulative number of case(s)` as cases, 
    `Number of deaths` as deaths,
    `Number recovered` as recovered
from sars_2013_02;

```


```sql
create view v_month
as
select
    strftime('%m', date) as n_month,
    case strftime('%m', date) 
    when '01' then 'Jan' 
    when '02' then 'Feb'
    when '03' then 'Mar'
    when '04' then 'Apr'
    when '05' then 'Jul'
    when '06' then 'Aug'
    when '07' then 'Sep'
    when '08' then 'Oct'
    when '09' then 'Sep'
    when '10' then 'Oct'
    when '11' then 'Nov'
    when '12' then 'Dec'
    else '' end
    as s_month,
    date,
    cases,
    deaths,
    recovered
from v_sars

```

## time to query and graph them in python
- setup your python env
- in my case, I currently use MiniConda and need to use Conda Prmompt terminal (could integrated into VSCODE, but this way is no IDE setup/config required)
- Have a new conda env: `conda create --name sqlite3 python=3.9 -y`
- Install needed packages: `conda install sqlite3, pandas, matplotlib`


## run code! 

- run a1.py  


## ref
ref: https://funprojects.blog/2021/12/27/6-lines-of-python-to-plot-sqlite-data/

