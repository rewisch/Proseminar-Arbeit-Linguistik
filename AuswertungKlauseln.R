#install.packages('dplyr')
#install.packages('sjPlot')
#install.packages('summarytools')
#install.packages('RColorBrewer')
#install.packages('gcookbook')
library(ggplot2)
library(dplyr)
library(sjPlot)
library(summarytools)
library(RColorBrewer)
library(gcookbook) 


data <- read.csv("C:\\Users\\rwiet\\PycharmProjects\\clausulae\\Caesar_clausulae.csv", header=TRUE, stringsAsFactors=FALSE, encoding="UTF-8")
data1 <- read.csv("C:\\Users\\rwiet\\PycharmProjects\\clausulae\\1_Caesar_clausulae.csv", header=TRUE, stringsAsFactors=FALSE, encoding="UTF-8")
View(data)

#table(data$Klauselname)
#table(data$Satzlänge)
#table(data$Rede)
#table(data$KategorieKlausel)
#table(data$Artistisch)
#table(data$KategorieKlausel)
#table(data$KategorieKlausel,data$Buch)



#-------------------------------------- #
#-------------------------------------- #
#---> Klauselgebrauch in den Reden <---#
#-------------------------------------- #
#-------------------------------------- #

chisq.test(table(data$Rede, data$KategorieKlausel))
chisq.test(table(data$Artistisch, data$Rede))

data$Rede[data$Rede== 1]<- 'Ja'
data$Rede[data$Rede == 0]<- 'Nein'
data$Artistisch[data$Artistisch == 1]<- 'Ja'
data$Artistisch[data$Artistisch == 0]<- 'Nein'

tab_xtab(var.row = data$Rede, var.col = data$Artistisch, show.col.prc = TRUE, show.obs = TRUE )
tab_xtab(var.row = data$Rede, var.col = data$KategorieKlausel, show.col.prc = TRUE, show.obs = TRUE )



#------------------------------------ #
#------------------------------------ #
#---> Artistisch/Nicht-Artistisch <---#
#------------------------------------ #
#------------------------------------ #

data$Artistisch[data$Artistisch == 1]<- 'Ja'
data$Artistisch[data$Artistisch == 0]<- 'Nein'

chisq.test(table(data$Buch, data$Artistisch))

barplot(table(data$Artistisch,data$Buch), beside =T, col = c("deepskyblue", "tomato"), xlab = 'Buch', ylab = 'Artistisch', main = 'Artistisch/Nicht-Artistisch pro Buch')
legend('top', fill=c("deepskyblue", "tomato"), legend=c("Nicht-Artistisch", 'Artistisch'), horiz =T)

barplot(table(data$Artistisch,data$Buch), col = c("deepskyblue", "tomato"), xlab = 'Buch', ylab = 'Artistisch', main = 'Artistisch/Nicht-Artistisch pro Buch')
legend('top', fill=c("deepskyblue", "tomato"), legend=c("Nicht-Artistisch", 'Artistisch'), horiz =T)

tab_xtab(var.row = data$Artistisch, var.col = data$Buch, show.col.prc = TRUE, show.obs = TRUE )

View(data)


ggplot(data, aes(x= Artistisch,  group=Buch)) + 
  geom_bar(aes(y = ..prop.., fill = factor(..x..)), stat="count") +
  geom_text(aes( label = scales::percent(..prop..),
                 y= ..prop.. ), stat= "count", vjust = -.5) +
  labs(y = "Prozent", fill="Artistisch") +
  facet_grid(~Buch) +
  scale_y_continuous(labels = scales::percent)

#--------------------------#
#--------------------------#
#---> Klauselkategorie <---#
#--------------------------#
#--------------------------#

chisq.test(table(data$Buch, data$KategorieKlausel))

barplot(table(data$KategorieKlausel,data$Buch), beside =T, col = c('green','orange','blue','limegreen','darkgreen','royalblue','red'), xlab = 'Buch', ylab = 'Klausel', main = 'Klauseln pro Buch')
legend('top', fill=c('green','orange','blue','limegreen','darkgreen','royalblue','red'), legend=c("Cretic-Trochaic", 'Double cretic/molossus cretic', 'Double trochee', 'Hypodochmiac', 'Spondaic', 'Heroic', 'Miscellaneous'), horiz =F)

tab_xtab(var.row = data$KategorieKlausel, var.col = data$Buch, show.col.prc = TRUE, show.obs = TRUE )

ggplot(data, aes(x= KategorieKlausel,  group=Buch)) + 
  geom_bar(aes(y = ..prop.., fill = factor(..x..)), stat="count") +
  geom_text(aes( label = scales::percent(..prop..),
                 y= ..prop.. ), stat= "count", vjust = 0.5, hjust = 1, angle = 90) +
  labs(y = "Prozent", fill="Klausel Kategorie") +
  facet_grid(~Buch) +
  scale_y_continuous( labels = scales::percent) + 
  scale_x_continuous(breaks=c(1,2,3,4,5,6,7))


freq(data$KategorieKlausel)
freq(data$Artistisch)




#------------------------------------#
#------------------------------------#
#---> Heroisch in Rede insgesamt <---#
#------------------------------------#
#------------------------------------#



data$Heroisch <- data$KategorieKlausel
data$Heroisch[data$Heroisch != 6]<- 'Nein'
data$Heroisch[data$Heroisch ==6]<- 'Ja'

tab_xtab(var.row = data$Heroisch, var.col = data$Rede, show.col.prc = TRUE, show.obs = TRUE )
tab_xtab(var.row = data$Heroisch, var.col = data$Buch, show.col.prc = TRUE, show.obs = TRUE )

#------------------------------------#
#------------------------------------#
#---> Heroisch in Buch 1-------  <---#
#------------------------------------#
#------------------------------------#


data1$Heroisch <- data1$KategorieKlausel
data1$Heroisch[data1$Heroisch != 6]<- 'Nein'
data1$Heroisch[data1$Heroisch ==6]<- 'Ja'
View(data1)

tab_xtab(var.row = data1$Heroisch, var.col = data1$Rede, show.col.prc = TRUE, show.obs = TRUE )


#Heroische Klauseln über das ganze Werk
tab_xtab(var.row = data$Heroisch, var.col = data$Buch, show.col.prc = TRUE, show.obs = TRUE )

