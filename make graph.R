
library(ggplot2)
library(tidyverse)
library(reshape)

fold <- 'C:\\Users\\jseyhun\\OneDrive - Coherent Economics LLC\\atp project\\betting market graphs'
x <- read.csv(paste0(fold, '/out/data.csv'), as.is=T)
x <- x[,-1]
vars <- c('B365','EX','PS','LB')
names(x)[names(x) %in% vars] <- paste0(vars, ".val")
names(x)[names(x) %in% paste0(vars,'n')] <- paste0(vars, '.n')

x2 <- reshape(x, idvar = c('brac', 'brac_lab', 'brac_lab2'), varying = list(c(3,5,7,9),c(4,6,8,10)), v.names = c('val', 'n'), direction = 'long', timevar = 'var', times = vars)
row.names(x2) <- NULL

x2$shape1 <- 16
nas <- which(is.na(x2$n))
x2$shape1[nas] <- 0
x2$n[nas] <- 0 #for hollow size missing ones
x2$val[nas] <- x2$brac[nas] #same
x2$size1[x2$n == 0] <- 3 
x2$size1[x2$n > 0 & x2$n < 100] <- 1.5
x2$size1[x2$n >= 100 & x2$n < 1000] <- 3
x2$size1[x2$n >= 1000] <- 4.5

x2$var[x2$var == "B365"] <- 'Bet365'
x2$var[x2$var == "EX"] <- 'Expekt'
x2$var[x2$var == "LB"] <- 'Ladbrokes'
x2$var[x2$var == "PS"] <- 'Pinnacles Sports'

l <- c('0%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%')
l2 <- c('0%', '20%', '40%', '60%', '80%', '100%')
mycols <- c('#2176B9', '#1FB3B6', '#90353B', '#6E8E84')
sizes <- c("0" = 5, "10" = 2, "100" = 3, "1000" = 4)

p <- ggplot(x2, aes(x = brac, y = val, group = var, color = var)) + 
  geom_point(aes(shape = shape1, size = size1)) + geom_line(size = 1) + facet_wrap(vars(var), ncol = 2) +
  geom_abline(slope = 1, intercept = 0, size = 1) +
  xlab('Predicted Chance of Victory') + ylab('Actual Chance of Victory') + 
  scale_y_continuous(breaks = seq(0,1,0.1), labels = l) + scale_x_continuous(breaks = seq(0,1,0.1), labels = l) +
  labs(color = 'Bookie', size = '# Matches') + theme_minimal() + 
  ggtitle(paste('Tennis Betting Market: Predicted vs Actual Probabilities of Win', "Men's ATP Tour", '2010 - 2019', sep = '\n')) +
  scale_color_manual(values = mycols, labels = c('B365', 'EX', 'LB', 'PS')) + 
  theme(plot.title = element_text(hjust = 0.5, face = 'bold', size = 20), legend.title = element_text(face = 'bold', size = 14), 
        axis.line = element_line(color = 'black'), strip.text = element_text(face = 'bold', size = 14), axis.title = element_text(size = 14),
        axis.ticks = element_line(size = 1), axis.text = element_text(size = 14)) +
  scale_shape_identity() +
  scale_size_continuous(range = c(1.5,4.5), breaks = c(4,1.5,3,4.5), labels = c('0', '[1,100)', '[100,1000)', '[1000,)')) +
  guides(size = guide_legend(override.aes = list(shape = c(0, 16, 16, 16))))
  #scale_size_manual(values = x2$size1, breaks = c("0","10","100","500"), labels = 1:4)
  
  
  
p

