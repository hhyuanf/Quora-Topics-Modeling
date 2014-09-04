clear;
clc;

% import data from u.data file and store it in data matrix where userids
% are on rows and itemids are on columns
imported_data = importdata('u.data');
data = zeros(943, 1682);
for i = 1: 1: 100000
    userid = imported_data(i, 1);
    itemid = imported_data(i, 2);
    rating = imported_data(i, 3);
    data(userid, itemid) = rating;
end
%% problem 1
% define R to be a rating matrix
R = data;
% define W to be a 0-1 matrix
W = data;
for i = 1: 1: 943
    for j = 1: 1: 1682
        if W(i, j) ~= 0
            W(i, j) = 1;
        end
    end
end
k = 10;
[A,Y,numIter,tElapsed,finalResidual_10] = wnmfrule(R, W, k);
result = A * Y;
total_error = sum(sum(W.*((R - result).^2)));
k = 50;
[A,Y,numIter,tElapsed,finalResidual_50] = wnmfrule(R, W, k);
result = A * Y;
total_error = sum(sum(W.*((R - result).^2)));
k = 100;
[A,Y,numIter,tElapsed,finalResidual_100] = wnmfrule(R, W, k);
result = A * Y;
total_error = sum(sum(W.*((R - result).^2)));
%% problem 2
% define W to be a rating matrix
W = data;
% define R to be a 0-1 matrix
R = data;
for i = 1: 1: 943
    for j = 1: 1: 1682
        if R(i, j) ~= 0
            R(i, j) = 1;
        end
    end
end
k = 10;
[A,Y,numIter,tElapsed,finalResidual_10] = wnmfrule(R, W, k);
result = A * Y;
total_error = sum(sum(W.*((R - result).^2)));
k = 50;
[A,Y,numIter,tElapsed,finalResidual_50] = wnmfrule(R, W, k);
result = A * Y;
total_error = sum(sum(W.*((R - result).^2)));
k = 100;
[A,Y,numIter,tElapsed,finalResidual_100] = wnmfrule(R, W, k);
result = A * Y;
total_error = sum(sum(W.*((R - result).^2)));
%% problem 3 & problem 4
% shuffle the index from 1 to 100k to randomly generate 10 parts
array = zeros(1, 100000);
for i = 1: 1: 100000
    array(i) = i;
end
shuffle = randperm(100000);
% record this random sequence
dlmwrite('random_number.txt', shuffle);
% create an array to record the average error for 10 cases
avg_error = zeros(1, 10);
% create an array to record the precision for 10 cases
precision = zeros(1, 10);
% create an array to record the recall for 10 cases
recall = zeros(1, 10);
for t = 1: 1: 10
    % create an array to record the index of testing set
    test = zeros(1, 10000);
    test(1: 10000) = shuffle((t - 1) * 10000 + 1: t * 10000);
    % define R and W to be rating matrices
    R = data;
    W = data;
    % define W to be a 0-1 matrix
%     for i = 1: 1: 943
%         for j = 1: 1: 1682
%             if W(i, j) ~= 0
%                W(i, j) = 1;
%             end
%         end
%     end
    % define R to be a 0-1 matrix
    for i = 1: 1: 943
        for j = 1: 1: 1682
            if R(i, j) ~= 0
               R(i, j) = 1;
            end
        end
    end
    % set the kth testing set to be 0 in R and W
    for i = 1: 1: length(test)
        R(imported_data(test(i), 1), imported_data(test(i), 2)) = 0;
        W(imported_data(test(i), 1), imported_data(test(i), 2)) = 0;
    end
    k = 100; %k=10, 50, 100
    [A,Y,numIter,tElapsed,finalResidual_100] = wnmfrule(R, W, k);
    result = A * Y;

    % problem 3 part
    sum_error = 0;
    for i = 1: 1: 10000
        cur_error = abs(data(imported_data(test(i), 1), imported_data(test(i), 2)) - result(imported_data(test(i), 1), imported_data(test(i), 2)));
        sum_error = sum_error + cur_error;
    end
    avg_error(t) = sum_error/10000;
    
    % problem 4 part
    num_predict_like = 0;
    num_actually_like = 0;
    % create an array to record the index of entries in the testing set that
    % users are predicted to like movies
    predict_like = zeros(1, 10000);
    % find out how many entries in testing set are predicted to larger than
    % 3.5
    for i = 1: 1: 10000
        if (result(imported_data(test(i), 1), imported_data(test(i), 2)) >= 3.5)
            num_predict_like = num_predict_like + 1;
            predict_like(num_predict_like) = test(i);
        end
    end
    % out of the predict_like terms, find out how many entries are actually
    % larger than or equal to 4
    for i = 1: 1: 10000
        if(predict_like(i) == 0)
            break; 
        end
        if (data(imported_data(predict_like(i), 1), imported_data(predict_like(i), 2)) >= 4)
            num_actually_like = num_actually_like + 1;
        end
    end
    precision(t) = num_actually_like/num_predict_like;

    num_predict_like = 0;
    num_actually_like = 0;
    % create an array to record the index of entries in the testing set that
    % users actually like movies
    actually_like = zeros(1, 10000);
    % find out how many entries in testing set are actually to larger than or
    % equal to 4
    for i = 1: 1: 10000
        if (data(imported_data(test(i), 1), imported_data(test(i), 2)) >= 4)
            num_actually_like = num_actually_like + 1;
            actually_like(num_actually_like) = test(i);
        end
    end
    % out of the actually_like terms, how many entries are actually larger than
    % or equal to 4
    for i = 1: 1: 10000
        if(actually_like(i) == 0)
            break; 
        end
        if (result(imported_data(actually_like(i), 1), imported_data(actually_like(i), 2)) >= 3.5)
            num_predict_like = num_predict_like + 1;
        end
    end
    recall(t) = num_predict_like/num_actually_like;
end
%% problem 5
lambda  = 1;
% define R to be a rating matrix
R = data;
% define W to be a 0-1 matrix
W = data;
for i = 1: 1: 943
    for j = 1: 1: 1682
        if W(i, j) ~= 0
            W(i, j) = 1;
        end
    end
end
% for i = 1: 1: 943
%     for j = 1: 1: 1682
%         if R(i, j) ~= 0
%             R(i, j) = 1;
%         end
%     end
% end
k = 10;
[A,Y,numIter,tElapsed,finalResidual_10] = wnmfrule_regularizer(R, W, k, lambda);