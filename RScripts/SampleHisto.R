library(DBI)
library(RSQLite)
con = dbConnect(SQLite(), "C:/Users/velu3/Documents/GitHub/ProjectCDEMCA/db.sqlite3")
alltables = dbListTables(con)
customer_data = dbGetQuery( con,'select * from Web_App_customer' )

png(file = "C:/Users/velu3/Documents/GitHub/ProjectCDEMCA/Web_App/static/Web_App/RGraphs/AgeOfClass.png")

hist(customer_data$Age,
     col="blue",
     main="Histogram to Show Count of Age Class",
     xlab="Age Class",
     ylab="Frequency",
     labels=TRUE)

dev.off()
