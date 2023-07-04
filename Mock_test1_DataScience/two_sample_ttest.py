from scipy import stats

def perform_hypothesis_test(sample1, sample2):
    t_statistic, p_value = stats.ttest_ind(sample1, sample2)
    print(t_statistic)
    return p_value

sample1 = list(map(int, input("Enter sample1 list: ").split(' ')))
sample2 = list(map(int, input("Enter sample2 list: ").split(' ')))

p_value = perform_hypothesis_test(sample1, sample2)
print("P-value:", p_value)