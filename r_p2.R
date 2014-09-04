library("tm")
library("topicmodels")

filesPath <- "/Users/yankanghe/Desktop/EE239/project_2/Answers"

#load the corpus of documents
corpus <- Corpus(DirSource(filesPath, encoding = "UTF-8") , readerControl = list(lange="english"))

#store length
len_corpus <- length(corpus)
len_document <- 1
for(p in 1:len_corpus)
{
  ##grab <- gregexpr("\\W+", corpus[p])
  len_document[p] <- sapply(gregexpr("\\W+", corpus[p]), length) + 1
  
}
#select 5 random documents
num_document <-1
sel_document<-1
while(num_document < 6)
{
  rand_index <- floor(len_corpus*runif(1)) + 1

  # length morn than 100
  if(len_document[rand_index] > 100)
    {
    sel_document[num_document] <- rand_index
    num_document <- num_document + 1
    }
}


#remove stop words from the text
corpus <- tm_map(corpus, removeWords, stopwords("english"))
#corpus <- tm_map(corpus, stripWhitespace)

#create document-term matrix
dtm <- DocumentTermMatrix(corpus)
#apply(dtm, 1, sum)


#train the model
k <- 21
lda_result <- LDA(dtm, k, method="VEM",estimate.alpha = FALSE,alpha = 50/k,estimate.beta = FALSE)

#get beta, logarithm of word distribution in topics
beta <- attr(lda_result,"beta")
plot(exp(beta[1,]))
plot(exp(beta[2,]))
plot(exp(beta[3,]))


#get gamma, containing topic distribution for each document
gamma <- attr(lda_result, "gamma")
plot(gamma[sel_document[1],])
plot(gamma[sel_document[2],])
plot(gamma[sel_document[3],])
plot(gamma[sel_document[4],])
plot(gamma[sel_document[5],])

#get alpha
alpha <- attr(lda_result, "alpha")

