library('ggplot2')
library('forecast')
library('tseries')

setwd('/Users/shelbyjennings/Desktop')
daily_data = read.csv('Bike-Sharing-Dataset/day.csv', header=TRUE, stringsAsFactors=FALSE)

#examine data
#peaks during summer
daily_data$Date = as.Date(daily_data$dteday)
ggplot(daily_data, aes(Date, cnt)) + geom_line() + scale_x_date('month') + 
  ylab("Daily Bike Checkouts") + xlab("")

#removing outliers that could lead to bias
count_ts = ts(daily_data[, c('cnt')])
daily_data$clean_cnt = tsclean(count_ts)
ggplot() + geom_line(data = daily_data, aes(x=Date, y=clean_cnt)) +
  ylab("Cleaned Bicycle Count")

#smoothing the series by using moving average
daily_data$cnt_ma = ma(daily_data$clean_cnt, order=7)
daily_data$cnt_ma30 = ma(daily_data$clean_cnt, order=30)
ggplot() +
  geom_line(data=daily_data, aes(x=Date, y=clean_cnt, colour="Counts")) +
  geom_line(data=daily_data, aes(x=Date, y=cnt_ma, colour="Weekly Moving Average")) +
  geom_line(data=daily_data, aes(x=Date, y=cnt_ma30, colour="Monthly Moving Average")) +
  ylab("Bicylce Count")
#eventually would want to additionally specify multiple levels of seasonality
#paying attention to seasonality, trend, cycle

#calculating seasonal component of series
count_ma = ts(na.omit(daily_data$cnt_ma), frequency=30)
decomp = stl(count_ma, s.window="periodic")
deseasonal_cnt <- seasadj(decomp)
plot(decomp)

#is series stationary?
adf.test(count_ma, alternative="stationary")
#data:  count_ma
#Dickey-Fuller = -0.2557, Lag order = 8, p-value = 0.99
#alternative hypothesis: stationary


