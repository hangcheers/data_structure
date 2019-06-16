import json
from collections import defaultdict

import numpy as np
import pandas as pd
import seaborn as sns

path = '/Users/helena/Downloads/pydata-notebook-master/datasets/bitly_usagov/example.txt'
records = [json.loads(line) for line in open(path, encoding='utf-8')]
time_zone = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zone[:10])


def get_count(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts


counts = get_count(time_zone)


def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]


print(top_counts(counts))

frame = pd.DataFrame(records)
tz_counts = frame['tz'].value_counts()
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Uknown'
tz_counts = clean_tz.value_counts()

results = pd.Series([x.split()[0] for x in frame.a.dropna()])
print(results.value_counts()[:8])  # value_counts() is a series method rather than a DataFrame method
# 有的agent缺失，所以先将他们从数据中移除
cframe = frame[frame.a.notnull()]
cframe['os'] = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
by_tz_os = cframe.groupby(['tz', 'os'])
# print(by_tz_os.size())  # dataframe df.size()
agg_counts = by_tz_os.size().unstack().fillna(0)
indexer = agg_counts.sum(1).argsort()
count_subset = agg_counts.take(indexer)[-10:]
print(count_subset)
count_subset = count_subset.stack()  # stack a dataframe with a single level column axis return a Series
count_subset.name = 'total'
count_subset = count_subset.reset_index()
print(count_subset[:10])


def norm_total(group):
    group['normed_total'] = group.total / group.total.sum()
    return group


results = count_subset.groupby('tz').apply(norm_total)
sns.barplot(x='normed_total', y='tz', hue='os', data=results)
