library("tm")
library("wordcloud")
library("RColorBrewer")

setwd("/Users/tomasbalint/Documents/Tomba/PROJEKTY_osobne/Web_tomasbalint_com/web_pelikan/wordcloud")

#data<-Corpus (DirSource("corpus/"))
#inspect(data)
data<-read.csv("corpus/korpus.txt", header=F,stringsAsFactors=F)
f<-runif(dim(data)[1],0,0.7)
# increase frequency of keywords
f[which(data[,1]=="energy")]<-0.94
f[which(data[,1]=="climate")]<-0.97
f[which(data[,1]=="research")]<-0.98
f[which(data[,1]=="data analysis")]<-0.93
f[which(data[,1]=="crowdsourcing")]<-0.92
f[which(data[,1]=="complex systems")]<-0.96
f[which(data[,1]=="R")]<-0.90
f[which(data[,1]=="python")]<-0.91

pal2 <- brewer.pal(9,"Blues")
pal2<-pal2[-(1:4)]
png("tb_cloud.png", width=1150,height=800, bg='transparent')
wordcloud(words=data[,1],freq=f, scale=c(4,0.5), max.words=150, random.order=FALSE, rot.per=0.15, use.r.layout=FALSE, colors=pal2)
dev.off()
