# record i = argmax_over_i(P(Ti|doc)), doc_index = 1: 51625
associate_topic <- integer(51625)
for (i in 1: 51625){
	associate_topic[i] <- which.max(gamma[i, ])
}


# create an aray of length k = 21 and initialize to be all 0
stor <- integer(21)

# read MediHealth_index.txt and store as an array named MediHealth_index, which is of length 326
MediHealth_index <- t(read.table("MediHealth_index"))

for (i in 1:326){
	stor[associate_topic[MediHealth_index[i]]] <- stor[associate_topic[MediHealth_index[i]]] + 1
}
max1 <- which.max(stor)
num1 <- stor[max1]
stor[max1] <- -1
max2 <- which.max(stor)
num2 <- stor[max2]
stor[max2] <- -1
max3 <- which.max(stor)
num3 <- stor[max3]
stor[max3] <- -1
max4 <- which.max(stor)
num4 <- stor[max4]
stor[max4] <- -1
max5 <- which.max(stor)
num5 <- stor[max5]

# read GPS_index.txt and store it as an array named GPS_index, which is of length 228
GPS_index <- t(read.table("GPS_index"))

for (i in 1:228){
	stor[associate_topic[GPS_index[i]]] <- stor[associate_topic[GPS_index[i]]] + 1
}
max1 <- which.max(stor)
num1 <- stor[max1]
stor[max1] <- -1
max2 <- which.max(stor)
num2 <- stor[max2]
stor[max2] <- -1
max3 <- which.max(stor)
num3 <- stor[max3]
stor[max3] <- -1
max4 <- which.max(stor)
num4 <- stor[max4]
stor[max4] <- -1
max5 <- which.max(stor)
num5 <- stor[max5]

# read Cycling_index.txt and store it as an array named Cycling_index, which is of length 378
Cycling_index <- t(read.table("Cycling_index"))

for (i in 1:378){
	stor[associate_topic[Cycling_index[i]]] <- stor[associate_topic[Cycling_index[i]]] + 1
}
max1 <- which.max(stor)
num1 <- stor[max1]
stor[max1] <- -1
max2 <- which.max(stor)
num2 <- stor[max2]
stor[max2] <- -1
max3 <- which.max(stor)
num3 <- stor[max3]
stor[max3] <- -1
max4 <- which.max(stor)
num4 <- stor[max4]
stor[max4] <- -1
max5 <- which.max(stor)
num5 <- stor[max5]

# read Olympic_index.txt and store it as an array named Olympic_index, which is of length 215
Olympic_index <- t(read.table("Olympic_index"))

for (i in 1:215){
	stor[associate_topic[Olympic_index[i]]] <- stor[associate_topic[Olympic_index[i]]] + 1
}
max1 <- which.max(stor)
num1 <- stor[max1]
stor[max1] <- -1
max2 <- which.max(stor)
num2 <- stor[max2]
stor[max2] <- -1
max3 <- which.max(stor)
num3 <- stor[max3]
stor[max3] <- -1
max4 <- which.max(stor)
num4 <- stor[max4]
stor[max4] <- -1
max5 <- which.max(stor)
num5 <- stor[max5]

# read Acne_index.txt and store it as an array named Acne_index, which is of length 270
Acne_index <- t(read.table("Acne_index"))

for (i in 1:270){
	stor[associate_topic[Acne_index[i]]] <- stor[associate_topic[Acne_index[i]]] + 1
}
max1 <- which.max(stor)
num1 <- stor[max1]
stor[max1] <- -1
max2 <- which.max(stor)
num2 <- stor[max2]
stor[max2] <- -1
max3 <- which.max(stor)
num3 <- stor[max3]
stor[max3] <- -1
max4 <- which.max(stor)
num4 <- stor[max4]
stor[max4] <- -1
max5 <- which.max(stor)
num5 <- stor[max5]

# problem 4
# calculate prior probability P(Ti), and store in array P_T
record <- table(associate_topic)
P_T = c()
for(i in 1:21){
	P_T[i]	<- record[names(record) == i]/51625	
}
plot(P_T)

# problem 5
# record max_over_i(P(Ti|doc)), doc_index = 1: 51625
highest_prob <- apply(gamma, 1, max)

