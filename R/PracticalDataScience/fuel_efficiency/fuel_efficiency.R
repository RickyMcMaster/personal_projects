library(plyr)
library(ggplot2)
library(reshape2)

getwd()
setwd('/Users/richard.mcmaster/Documents/analysis_projects/R/PracticalDataScience/fuel_efficiency')
getwd()

vehicles <- read.csv(unz("vehicles.csv.zip", "vehicles.csv"),
                     stringsAsFactors = F)
head(vehicles)
