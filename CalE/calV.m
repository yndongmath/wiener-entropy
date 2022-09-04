function [result] = calV(n, k, j)
% calulate the value of 
% input: n, k, j
%

A = -2/3*k^3 + (3*n-6)/3*k^2 + (3*n+2-6*j)*k/3 + n^2 - n;
B = (k^2 - k + 2*n -2) / 2;
C = (k^2 + k + 2*n -2) /2;
D = calD(n, k, j);
result = log2(A)- 1/A * (j*B*log2(B)+(n-k-j)*C*log2(C) + D);
end


 