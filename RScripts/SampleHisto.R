
customer_data=read.csv("C:/Users/velu3/Documents/GitHub/ProjectCDEMCA/Data/Mall_Customers.csv")

png(file = "C:/Users/velu3/Documents/GitHub/ProjectCDEMCA/Web_App/static/Web_App/RGraphs/barchart_months_revenue.png")

hist(customer_data$Age,
     col="blue",
     main="Histogram to Show Count of Age Class",
     xlab="Age Class",
     ylab="Frequency",
     labels=TRUE)

dev.off()
