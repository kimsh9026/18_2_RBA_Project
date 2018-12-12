#Chapter 7
#감성분석
#함수 생성 방법
#plyr패키지 - 원본 데이터를 분석하기 쉬운 형태로 나누어 다시 새로운 형태로 만들어 주는 패키지, <Dataframe,List,Array>.. daply() (dataframe -> array)등으로 이용
#tidyverse패키지 - 일반 데이터 분석에 필요할 가능성이 있는 패키지를 포함,, ggplot2, tibble, tidyr, readr, purr, dplyr, stringr, forcats 패키지들을 포함
#tidytext패키지,, unnest_tokens() - text를 token화.
#glue패키지
#stringr패키지

#감성분석 코드 (코드단에서 text를 입력해야함...)
install.packages("tidyverse")
install.packages("plyr")
install.packages("glue")
install.packages("stringr")
install.packages("tidytext")

library(plyr)
library(glue)
library(stringr)
library(tidyverse)
library(tidytext)

sample <- c("you're awesome and I love you",
            "I hate and hate and hate. So angry, Die!",
            "impressed and amazed : you are peeriess in your achievement of unparalleled mediocrity",
            "oh how I love being ignored",
            "absolutely adore it when my bus is late")

pos.words <- scan('positive-words.txt', what='character', comment.char=';')
neg.words <- scan('negative-words.txt', what='character', comment.char=';')

score.sentiment <- function(sentences, pos.words, neg.words){
  scores <- laply(sentences,
                  function(sentence, pos.words, neg.words)
                          {
                            sentence <- gsub("[[:punct:]]", "", sentence) #;같은거 없애는거.. positive랑 negative 보면 왜 하는지 알 것 같긴 한데 이해는 안됨.. [[:punct]]가 구두점문자들이래..
                            sentence <- gsub("[[:cntrl:]]", "", sentence) #이거는 뉴라인캐릭터나 \n, \r같은거 없애준데... [[:cntrl:]]이 그런거 정규식이래
                            sentence <- gsub("\\d+", "", sentence) # 이거는 도저히 모르겠다.
                            tryTolower <- function(x)
                            {
                              y<-NA
                              try_error <- tryCatch(tolower(x), error=function(e)e)
                              if(!inherits(try_error, "error"))
                                y <- tolower(x)
                              return(y)
                            }
                            sentence <- sapply(sentence, tryTolower)#sapply : 벡터, 리스트, 표현식, 데이터 프레임 등에 함수를 적용하고 그 결과를 벡터 또는 행렬로 반환한다.
                            word.list <- str_split(sentence, "\\s+")
                            words <- unlist(word.list)#unlist : list를 vector로
                            
                            pos.matches <- match(words, pos.words)#뭔지 알지?
                            neg.matches <- match(words, neg.words)#이것도?
                            
                            pos.matches <- !is.na(pos.matches)#결측값..알지?
                            neg.matches <- !is.na(neg.matches)#당연히 알겠지
                            
                            score <- sum(pos.matches) - sum(neg.matches)#sum하면 그냥 숫자가 딱 나오나보네.. 신기..
                            return(score)#리턴알지? 함수종료 or 결과 전달.
                          }
                  , pos.words, neg.words)#아직 파라미터였어 격충;;
  scores.df <- data.frame(text = sentences, score=scores)
  return(scores.df)
}
#call
result <- score.sentiment(sample, pos.words, neg.words)
result
hist(result$score)
qplot(result$score) #가로축 : 감성점수(score), 세로축 : 갯수(count)

#In tidytext, unnest_tokens(), 텍스트를 토큰화
ex <- c("because he could not stop for death",
        "HE kindly stopped or me")
ex_df <- data_frame(text=ex) %>% unnest_tokens(word, text)
ex_df

#In tidytext, 소문자 전환
(to_lower = FALSE)

#for(i in 1:10) <- 1부터 10까지, continue대신 next

#파일을 불러와서 감성점수 구하는 함수..
GetSentiment <- function(file){
  fileName <- glue("../input/", file, sep="") #현재 디렉토리 하위의 input 디렉토리에 file이라는 이름의 파일을 지정
  fileName <- trimws(fileName) #불필요한 space 제거
  fileText <- glue(read_file(fileName)) #파일 읽어서 fileText에 내용 저장
  fileText <- gsub("\\$", "", fileText) # 특수문자 제거
  tokens <- data_frame(text=fileText) %>% unnest_tokens(word, text) #unniest_tokens를 사용하여 text를 token화함
  
  sentiment <- tokens %>% 
    inner_join(get_sentiments("bing")) %>%  #sentiment word만..
    count(sentiment) %>% #postive & negative 단어 수 세기
    spread(sentiment, n, fill=0) %>%  #made data wide
    mutate(sentiment=positive-negative) %>% #감성점수 계산
    mutate(file=file) %>% #file명 추가
    mutate(year=as.numeric(str_match(file, "\\d{4}"))) %>% #숫자 4개로 년도를 추가
    mutate(president=str_match(file, "(.*?)_")[2]) #대통령이름 추가

  return(sentiment)
}

#각 파일의 감성점수 구하기..
files <- list.files("../input")
sentiments <- data_frame()
for(i in files){
  sentiments <- rbind(sentiments, GetSentiment(i))
}
View(sentiments)

#중복된 대통령 이름 수정
bushSr <- sentiments %>% 
  filter(president == "Bush") %>% 
  filter(year < 2000) %>% 
  mutate(president="Bush Sr.")

sentimets <- anti_join(sentiments,
                       sentiments[sentiments$president == "Bush" & sentiments$year < 2000,])

sentiments <- full_join(sentiments, bushSr)
View(sentiments)

#감성점수로 그래프 그리기
summary(sentiments)

ggplot(sentiments, aes(x=as.numeric(year), y=sentiment)) +
  geom_point(aes(color=president)) +
  geom_smooth(method = "auto")

ggplot(sentiments, aes(x=president, y=sentiment, color=president)) +
  geom_boxplot()

#공화당과 민주당 비교
democrats <- sentiments %>% 
  filter(president == c("Clinton", "Obama")) %>% 
  mutate(party="D")
republicans <- sentiments %>% 
  filter(president != "Clinton" & president != "Obama") %>% 
  mutate(party="R")

byParty <- full_join(democrats, republicans)
View(byParty)

#t검정 및 그래프
t.test(democrats$sentiment, republicans$sentiment)
# =는 귀무가설에 넣는다. ..1종오류... B일 확률(0이 아닌 평균값..으로 그린...)이 더 높아서 A에서 나왔는데, B에서 나왔다고 주장할 확률...???   P-value가.. 유효수준보다..낮으면.. 귀무가설,,(=이 들어가는 가설이야.....!!!!)을 기각한다... H0은 귀무가설, H1은 대립가설

ggplot(byParty, aes(x=party, y=sentiment, color=party)) + 
  geom_boxplot() +
  geom_point()

#Chapter 8
#지도그리기..
#maps패키지
#mapdata패키지
#mapproj패키지
#maptools패키지
#mapplots패키지
#ggiraphExtra패키지
#kormaps2014
#stringi패키지
#devtools
#단계 구분도를 그리기 위해서는 tidyverse와 ggiraphExtra, maps, mapproj 세가지를 이 순서로 설치해야 한다.
install.packages("tidyverse")
install.packages("ggiraphExtra")
install.packages("maps")
install.packages("mapproj")

library(tidyverse)
library(ggiraphExtra)
library(maps)
library(mapproj)

crime <- rownames_to_column(USArrests, var="state") #DF애 변수명 추가
crime$state <- tolower(crime$state) #소문자로 전환
states_map <- map_data("state") #위도, 경도 데이터를 DF형대로 전환,, state=미국, italy, france 등등..
str(states_map)
#지도 그리기
ggChoropleth(data=crime,
             aes(fill = Murder,
                 map_id = state),
             map = states_map)
#interactive 지도 만들기
ggChoropleth(data=crime,
             aes(fill = Murder,
                 map_id = state),
             map = states_map,
             interactive = T)
#Murder뿐만 아니라 Rape 변수도.. 지도가 두개가 생겨..
ggChoropleth(data=crime,
             aes(fill = c(Murder, Rape),
                 map_id = state),
             map = states_map,
             interactive = T)
#모든 변수에 대해, 지도가 네개가 생겨..
ggChoropleth(data=crime,
             aes(map_id = state),
             map = states_map,
             palette="OrRd",
             interactive = T)

#대한민국 지도는 kormaps..!
#대한민국지도에 필요한 패키지
install.packages("stringi") #kormaps2014쓸 때 필요..
install.packages("devtools")
devtools::install_github("cardiomoon/kormaps2014")

library(kormaps2014) #한글이 깨져보이면 str(changeCode())로 인코딩을 CP949로 변환하면 됨
str(korpop1)

#단계구분도를 위한패키지
install.packages("tidyverse")
install.packages("ggiraphExtra")
install.packages("maps")
install.packages("mapproj")

library(tidyverse)
library(ggiraphExtra)
library(maps)
library(mapproj)

korpop1_a <- rename(korpop1, pop=총인구_명, name=행정구역별_읍면동) #한글 변수명을 영어로..
str(korpop1_a)

ggChoropleth(data=korpop1_a,
             aes(fill=pop,
                 map_id=code,
                 tooltip=name),
             map=kormap1,
             interactive=T)

#ggplot으로 그리기..
theme_set(theme_gray(base_family="AppleGothic"))
ggplot(korpop1, aes(map_id = code, fill=총인구_명))+
  geom_map(map=kormap1, colour="black", size=0.1)+
  expand_limits(x=kormap1$long, y=kormap1$lat)+
  scale_fill_gradientn(colours=c("white", "skyblue", "blue"))+
  ggtitle("2015년도 시도별 인구분포도")+
  coord_map()

#ggChoropleth함수 사용
ggChoropleth(data=korpop1,
             aes(fill=총인구_명,
                 map_id=code,
                 tooltip=name1),
             map=kormap1,
             interactive=T)
ggChoropleth(data=korpop2,
             aes(fill=남자_명,
                 map_id=code),
             map=kormap2,
             interactive=T)

#Chapter 9
#인터랙티브 그래프,, 실시간으로 형태가 변하는 그래프, HTML포멧으로 저장 가능,, -> 웹브라우저를 이용해 그래프 조작 가능
#ploty패키지,, ggploty()함수를 적용하여 인터랙티브 그래프생성
#dygraphs패키지 - 인터랙티브 시계열 그래프
install.package("plotly")
library(plotly)

#mpg데이터로..
p<-ggplot(data=mpg, aes(x=displ, y=hwy, col=drv)) +
  geom_point()
ggplotly(p) #View창에서 Export -> Save as Web Page 를 이용해서 HTML로도 뽑아낼 수 있다 ㅇㅅㅇ
#diamonds데이터로..
p<-ggplot(data=diamonds,
          aes(x=cut, fill=clarity))+
  geom_bar(position="dodge")
ggplotly(p)
#random number생성하여 boxplot 그리기
set.seed(1234)
#rondom number generator
dat <- data.frame(cond=factor(rep(c("A","B"), each=200)),
                              rating=c(rnorm(200),rnorm(200, mean=8)))
#rep(1,3), rep(c(1,2), 3), rep(c(1,2), each=3), rep(c("a","b"), each=3)
summary(dat)
#1. basic boxplot
p <- ggplot(dat, aes(x=cond, y=rating)) +
  geom_boxplot()
ggplotly(p)
#2. colored boxplot
p <- ggplot(dat, aes(x=cond, y=rating, fill=cond)) +
  geom_boxplot()
ggplotly(p)
#3. flipped boxplot
p <- ggplot(dat, aes(x=cond, y=rating, fill=cond)) +
  geom_boxplot() +
  guides(fill=F) +
  coord_flip()
ggplotly(p)
#4. boxplot with stats
p <- ggplot(dat, aes(x=cond, y=rating)) +
  geom_boxplot() +
  stat_summary(fun.y=mean, geom='point', shape=5, size=4)
ggplotly(p)

#인터랙티브 시계열 그래프,, 시간순서로 정리되어있어야 타당한 자료!
install.packages("dygraphs")
library(dygraphs)
library(xts)
eco <- xts(economics$unemploy, order.by = economics$date)
head(eco)
dygraph(eco)
dygraph(eco) %>% dyRangeSelector() #날짜 범위 선택 가능
#여러 개 시계열 그래프 그리기
#저축률 psavert와 실업률 unemploy
#저축률
eco_1 <- xts(economics$psavert, order.by=economics$date)
#실업자수
eco_2 <- xts(economics$unemploy/1000, order.by = economics$date)

eco_a <- cbind(eco_1, eco_2)
colnames(eco_a) <- c("psavert", "unemploy")
head(eco_a)
dygraph(eco_a)
dygraph(eco_a) %>% dyRangeSelector()

#plotly가 제공하는 함수들을 좀 써볼까나~~

#plot_ly
#simple examples
plot_ly(economics, x=~pop)
plot_ly(economics, x=~date, y=~pop)
plot_ly(z=~volcano)
plot_ly(z=~volcano, type="surface")
#a functional interface
add_lines(plot_ly(economics, x=~date, y=~unemploy/pop))
#attributes defined via ploy_ly() set 'global'attributes
plot_ly(economics, x=~date, color = I("blue")) %>% 
  add_lines(y=~uempmed) %>% 
  add_lines(y=~psavert, color=I("red"))
#attributes : in the figure reference
library(RColorBrewer)
p <- plot_ly(iris, x=~Sepal.Width, y=~Sepal.Length)
add_markers(p, color=~Petal.Length, size=~Petal.Length)
add_markers(p, color=~Species)
add_markers(p, color=~Species, colors="Set2")
add_markers(p, symbol=~Species)
add_paths(p, linetype=~Species)
#함수연결
plot_ly(iris, x=~Sepal.Width, y=~Sepal.Length) %>% add_markers(color=Petal.Length, size=~Petal.Length) #이거랑 똑같은 문법으로 위에있는거 다 할 수 있다~

#add_data, add data to plotly visualization
plot_ly() %>% add_data(economics) %>% add_trace(x=~date,y=~pce)
#if no trace type is specified, it sets a sensible default
p <- plot_ly(economics, x=~date, y=~uempmed)
p
#add_*** : a specific case of a trace type,, ex) add_text(p, text="%") or add_paths(p), add_lines(p).. or..
add_trace(p, type="scatter", mode="marders+lines")
#mappings provided to ploy_ly
plot_ly(economics, x=~date, y=~uempmed, color="yellow", alpha=0.6, showlegend=FALSE) %>%
  add_lines() %>% add_markers(color=~pop)
#another parameters
plot_ly(economics, x=~date) %>% 
  add_ribbons(ymin=~pce-1e3, ymax=~pce+1e3)
#another parameters
txhousing %>% group_by(city) %>% 
  filter(year==2000) %>% #없어도 돼.. 필터자나
  plot_ly(x=~date, y=~median) %>% 
  add_lines(color=I("black"))
#univariate summary statistics
plot_ly(mtcars, x=~factor(vs), y=~mpg) %>% add_boxplot()
plot_ly(mtcars, x=~factor(vs), y=~mpg,
        box=list(visible=T)) %>% 
  add_trace(type="violin")
#the histogram
p <- plot_ly(alpha = 0.6) %>% 
  add_histogram(x = ~rnorm(500)) %>% 
  add_histogram(x = ~rnorm(500) + 1) %>% 
  layout(barmode = "overlay")
p
#the 2d analogy of add_histogram()
install.packages("MASS")
library(MASS)
p <- plot_ly(geyser, x=~waiting, y=~duration)
p
add_histogram2d(p)
add_histogram2dcontour(p)
#pie chart
ds <- data.frame(labels=c("A", "B", "C"), values=c(10, 40, 60))
plot_ly(ds, labels=~labels, values=~values) %>% 
  add_pie() %>% 
  layout(title="Basic Pie Chart using plotly")
#3D chart types
plot_ly(z=~volcano) %>% 
  add_surface()
plot_ly(x=c(0,0,1), y=c(0,1,0), z=c(0,0,0)) %>% 
  add_mesh

#animation_opts
if(interactive()){
  p <- ggplot(txhousing, aes(month, median)) +
    geom_line(aes(group=year), alpha = 0.3) +
    geom_smooth() +
    geom_line(aes(frame=year, ids=month), color="red") +
    facet_wrap(~city)
  
  ggplotly(p, width=1200, height=900) %>% 
    animation_opts(1000)
}

#어떤 새가 암컷일 확률이 48.8%, 400마리 중 암컷의 수는?
no_G <- rbinom(1, 400, 0.488)
no_G
#위의 문제를 1000번 실행..
no_sample <- 1000
no_G <- rbinom(no_sample, 400, 0.488)
hist(no_G)
mean(no_G)

#이란성 쌍둥이일 확률은 1/125, 둘 중 하나가 암컷일 확률은 49.5%
#일란성 쌍둥이일 확률은 1/300, 둘 다 암컷일 확률은 49.5
#single birth일 때 암컷일 확률은 48.8
#400마리 중 암컷의 수는?
no_sample <- 400
birth_type <- sample(c("이란성","일란성","single birth"),
                     no_sample,
                     replace = T,
                     prob=c(1/125, 1/300, 1-1/125-1/300))
girls <- rep(0, no_sample)
for(i in 1:no_sample){
  if(birth_type[i] == "single birth")
    girls[i] <- rbinom(1,1,0.488)
  
  else if(birth_type[i] == "일란성")
    girls[i] <- 2*rbinom(1,1,0.495)
  
  else if(birth_type[i] == "이란성")
    girls[i] <- rbinom(1,2,0/495)
}
no_G <- sum(girls)
no_G

#위 실험을 1000번 했을 때 암컷에 대한 분포는..?
no_sample <- 400
birth_type <- sample(c("이란성","일란성","single birth"),
                     no_sample,
                     replace = T,
                     prob=c(1/125, 1/300, 1-1/125-1/300))
no_rep <- 1000
no_G <- rep(0, no_rep)
for(n in 1:no_rep){
  girls <- rep(0,no_sample)
  for(i in 1:no_sample){
    if(birth_type[i] == "single birth")
      girls[i] <- rbinom(1,1,0.488)
    
    else if(birth_type[i] == "일란성")
      girls[i] <- 2*rbinom(1,1,0.495)
    
    else if(birth_type[i] == "이란성")
      girls[i] <- rbinom(1,2,0/495)
  }
  no_G[n] <- sum(girls)
}
title <- paste("평균: ", round(mean(no_G), 3), " sd:", round(sd(no_G),3))
hist(no_G, main=title, family = "AppleGothic")

#Monty Hall
#1회 실험..
car <- sample(3,1,replace = T)
door <- sample(3,1,replace = T)
stay_win <- car == door
switch_win <- car != door
c(stay_win, switch_win)

#10회 실험..
car <- sample(3,10,replace=T)
door <- sample(3,10,replace=T)
stay_win <- car==door
switch_win <- car!=door
c(sum(stay_win), sum(switch_win))

#10년간 진행한다면..?,, switch가 이길확률
sim_monty <- function(times){
  car <- sample(3,times,replace=T)
  door <- sample(3,times, replace=T)
  
  stay_win <- car==door
  switch_win <- car!=door
  
  switch_win_prob <- sum(switch_win)/times
  
  return(switch_win_prob)
}
sim_monty(520)

#10년간 진행한다면..?,, stay와 switch가 각각 이길확률
sim_monty <- function(times){
  car <- sample(3,times,replace=T)
  door <- sample(3,times, replace=T)
  
  stay_win <- car==door
  switch_win <- car!=door
  
  stay_win_prob <- sum(stay_win)/times
  switch_win_prob <- sum(switch_win)/times
  
  prob <- c(stay_win_prob, switch_win_prob)
  return(prob)
}
sim_monty(520)

#모의 실험 그래프
monty_MC_df <- data.frame()
for(i in 1:520){
  n_trials <- i
  prob <- sim_monty(i)
  monty_MC_df <- rbind(monty_MC_df, data.frame(n_trials, prob))
}

ggplot(monty_MC_df, aes(n_trials, prob)) +
  geom_line(size=1.0, color="lightblue", alpha=0.5)+
  labs(x="모의시험횟수", title="자동차를 차지할 확률",
       y="확률", subtitle="몬티홀 퀴즈쇼 처음 선택을 바꿨을 경우") +
  scale_y_continuous(labels = scales::percent) +
  scale_x_continuous(labels = scales::comma) +
  geom_hline(yintercept=2/3, color="red")