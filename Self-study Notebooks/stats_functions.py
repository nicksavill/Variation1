import numpy as np

def t_statistic(S1, S2):
    xbar1 = S1.mean(axis=0)
    xbar2 = S2.mean(axis=0)
    var1 = S1.var(axis=0)
    var2 = S2.var(axis=0)
    n1 = np.sum(~np.isnan(S1), axis=0)
    n2 = np.sum(~np.isnan(S2), axis=0)
    if isinstance(n1, np.ndarray):
        n1 = n1[0]
        n2 = n2[0]
    df1 = n1 - 1
    df2 = n2 - 1
    var_p = (df1*var1 + df2*var2)/(df1 + df2)
    se_p = np.sqrt(var_p*(1/n1 + 1/n2))
    return (xbar1-xbar2)/se_p