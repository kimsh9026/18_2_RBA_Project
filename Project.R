install.packages('KoNLP')
install.packages('SnowballC')
install.packages('wordcloud')
install.packages('RColorBrewer')
install.packages('plyr')
install.packages('stringr')
install.packages('ggplot2')

library(KoNLP)
library(SnowballC)
library(RColorBrewer)
library(wordcloud) 
library(plyr)
library(stringr)
library(ggplot2)
useSejongDic()
getwd()
txt <- readLines("./Project/R_Project/crawl/data/all_rank.txt", encoding = "EUC-KR")
#띄어쓰기를 지움
actual_keyword <- str_replace_all(txt, " ", "")

#띄어쓰기를 뉴라인캐릭터로 바꾼 버전을 로드함
word_by_word <- readLines("./Project/R_Project/crawl/data/all_rank_without_blank.txt")
View(word_by_word)

wordcount_whole_keyword <- table(unlist(actual_keyword))
wordcount_seperated_keyword <- table(unlist(word_by_word))

View(wordcount_whole_keyword)
View(wordcount_seperated_keyword)

df_wordcount_whole_keyword <- as.data.frame(wordcount_whole_keyword, stringsAsFactors = F)
df_wordcount_seperated_keyword <- as.data.frame(wordcount_seperated_keyword, stringsAsFactors = F)

View(df_wordcount_whole_keyword)
View(df_wordcount_seperated_keyword)

df_wordcount_whole_keyword <- df_wordcount_whole_keyword %>% arrange(desc(Freq))
df_wordcount_seperated_keyword <- df_wordcount_seperated_keyword %>% arrange(desc(Freq))

df_wordcount_whole_keyword <- rename(df_wordcount_whole_keyword, word=Var1, freq=Freq) #변수이름 바꿔주고
View(df_wordcount_whole_keyword)
df_wordcount_seperated_keyword <- rename(df_wordcount_seperated_keyword, word=Var1, freq=Freq) #변수이름 바꿔주고
View(df_wordcount_seperated_keyword)
View(df_wordcount_whole_keyword)

require(devtools)
library(wordcloud2)
View(df_wordcount_whole_keyword)

wordcloud2(data = df_wordcount_whole_keyword, figPath = "./Project/R_Project/naver.png", color="green", backgroundColor="white")


set.seed(9999)
wordcloud(
  words = df_wordcount_whole_keyword$word,
  freq = df_wordcount_whole_keyword$freq,
  min.freq = 2,
  max.words = 500, #표현단어수 200개까지
  random.order = F, #고빈도단어 중앙 배치
  rot.per = 0.35, # 회전단어 비율
  colors = brewer.pal(8, "Dark2"), #단어색깔.....,
  family="AppleGothic"
)

set.seed(9999)
wordcloud(
  words = df_wordcount_seperated_keyword$word,
  freq = df_wordcount_seperated_keyword$freq,
  min.freq = 2,
  max.words = 500, #표현단어수 200개까지
  random.order = F, #고빈도단어 중앙 배치
  rot.per = 0.35, # 회전단어 비율
  colors = brewer.pal(8, "Dark2"), #단어색깔.....,
  family="AppleGothic"
)
        
















          
require(devtools)
#install_github("lchiffon/wordcloud2")
library(wordcloud2)

wordcloud2(data = txt_df, color="random-light", backgroundColor="black")
wordcloud2(data = txt_df, minRotation = -pi/6, maxRotation = -pi/6, minSize = 10, rotateRatio = 1)
wordcloud2(data = txt_df, color="random-light", shape = 'star')
wordcloud2(data = txt_df, figPath = "twitter.png", size=1.5, color = "skyblue")