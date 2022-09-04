function [D] = calD(n, k, j)
D = 0;
for i = 1 : k
    val = (i*j + (i+1)*(n-k-j) + i*(i-1)/2 + (k-i)*(k-i+1)/2);
    D = D + val*log2(val); 
end
end