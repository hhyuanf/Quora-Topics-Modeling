library("tm")
library("topicmodels")

filesPath <- “/Users/yankanghe/Desktop/EE239/project_2/Answers_3”

#load the corpus of documents
corpus <- Corpus(DirSource(filesPath, encoding = "UTF-8") , readerControl = list(lange="english"))

#remove stop words from the text
funs <- list(stripWhitespace, tolower, removeNumbers, removePunctuation)
corpus <- tm_map(corpus, FUN = tm_reduce, tmFuns = funs)
corpus <- tm_map(corpus, removeWords, stopwords("english"))

#create document-term matrix
dtm <- DocumentTermMatrix(corpus)

#train the model
k <- 50
lda_result <- LDA(dtm, k, method="VEM")
terms(lda_result, 20)

#get beta, logarithm of word distribution in topics
beta <- attr(lda_result,"beta")
plot(beta[1,])
plot(exp(beta[1,]))

#get gamma, containing topic distribution for each document
gamma <- attr(lda_result, "gamma")
