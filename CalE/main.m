clc;
clear;
close all;

k = 67;
n_low = 1004;
n_up=2540;

y = [];

List_M = [];
List_I = [];
List_K = [];

for n = n_low:n_up
    idx0 = 1;
    idx1 = 1;
    idx2 = 1;
    idx3 = 1;
    idx4 = 1;
    n 
    min1 = vpa(calV(n, k-1, 1), 20);
    min2 = vpa(calV(n, k, 1), 20);
    min3 = vpa(calV(n, k+1, 1), 20);
    min4 = vpa(calV(n, k+2, 1), 20);
    min0 = vpa(calV(n, k-2, 1), 20);
    
    for j0 = 1:(n-k+2-1)
        v0 = vpa(calV(n, k-2, j0), 20);
        if v0 < min0
            idx0 = j0;
            min0 = v0;
        end
    end

    for j1 = 1:(n-k+1-1)
        v1 = vpa(calV(n, k-1, j1), 20);
        if v1 < min1
            idx1 = j1;
            min1 = v1;
        end
    end

    for j2 = 1:(n-k-1)
        v2 = vpa(calV(n, k, j2), 20);   
        if v2 < min2
            idx2 = j2;
            min2 = v2;
        end
    end

    for j3 = 1:(n-(k+1)-1)
        v3 = vpa(calV(n, k+1, j3), 20);
        if v3 < min3
            idx3 = j3;
            min3 = v3;
        end
    end

    for j4 = 1:(n-(k+2)-1)
        v4 = vpa(calV(n, k+2, j4), 20);
        if v4 < min4
            idx4 = j4;
            min4 = v4;
        end
    end

    idx_v = [idx0, idx1, idx2, idx3,idx4];
    min_v = [min0,min1, min2, min3,min4];
    [M,I] = min(min_v);
    List_M = [List_M, M];
    List_I = [List_I, idx_v(I)];

    idx_v(I)
    if I == 1
        k = k-2;
    elseif I == 2
        k = k - 1;
    elseif I == 4
        k = k + 1;
    elseif I == 5
        k = k + 2;
    end
    List_K = [List_K, k];
    k
end 
List_n = n_low:n_up;
title={'n','k','j'};
result_table=table(List_n',List_K',List_I','VariableNames',title);
writetable(result_table, 'Iw.csv');
