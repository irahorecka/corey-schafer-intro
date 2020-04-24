library(ggplot2)

current_dir <- getwd()  # make sure you're in the R directory, or manually set to path with intro_count.csv
intros <- read.csv(paste0(current_dir, '/intro_count.csv'), sep=',', header=TRUE)
uniq_intro <- data.frame(table(intros$INTRO_COUNT))

# match letter keys to Corey's introductions
uniq_intro$Var1 <- as.character(uniq_intro$Var1)
uniq_intro$Var1[uniq_intro$Var1 == "a"] <- "Hey there how's it going, everybody."
uniq_intro$Var1[uniq_intro$Var1 == "b"] <- "Hey how's it going, everybody."
uniq_intro$Var1[uniq_intro$Var1 == "c"] <- "Hey everybody how's it going."
uniq_intro$Var1[uniq_intro$Var1 == "d"] <- "Hey what's going on everybody how's it going."
uniq_intro$Var1[uniq_intro$Var1 == "e"] <- "Hey guys how's it going."
uniq_intro$Var1[uniq_intro$Var1 == "f"] <- "Hey what's going on, everybody."

# create pie chart of Corey's video introductions
ggplot(uniq_intro, aes(x="", y=Freq, fill=reorder(Var1, Freq))) +
  geom_bar(stat="identity", width=1) +
  coord_polar("y", start=0) +
  scale_fill_brewer(name=NULL,
                    palette="Oranges",
                    direction=1) +
  labs(caption='   Source: "Python Tutorials" YouTube playlist\n(N=138)') +
  ggtitle("Corey Schafer's video introductions") +
  theme_void() +
  theme(axis.ticks = element_blank(),
        axis.text = element_blank(),
        axis.title = element_blank()) + 
  theme(plot.caption=element_text(size=10, hjust=0.05),
        plot.title=element_text(size=14, hjust=0.5, face='bold'),
        legend.title=element_text()) +
  theme(plot.margin=unit(c(.5, .5, .5, .5),"cm")) +
  guides(fill=guide_legend(reverse=T))
