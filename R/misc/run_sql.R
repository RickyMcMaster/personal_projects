library(yaml)
library(tidyverse)

yaml_loc = "plista_da_config.yml"

setwd("/Users/richard.mcmaster/plista_git/dataeng/da/da-tools/deployR/preprocessing/")

creds <- yaml.load_file(yaml_loc)

USERNAME = creds$mysql_680$user
PASSWORD = creds$mysql_680$password
DBNAME = creds$mysql_680$database
HOST = creds$mysql_680$host
PORT = creds$mysql_680$port
FILE = "/Users/richard.mcmaster/plista_git/dataeng/da/da-tools/deployR/preprocessing/sql_test.sql"

dum_cmd <- glue::glue("mysql -u {USERNAME} -p {PASSWORD} --host {HOST} --port {PORT} {DBNAME}  < \"{FILE}\"")
print(cmd)

cmd <- "/usr/local/mysql/bin/mysql --login-path=plista680 insights -e 'select * from dummy'"

# system("export")
system2(cmd)
