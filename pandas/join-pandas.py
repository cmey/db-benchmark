#!/usr/bin/env python

print("# join-pandas.py")

import os
import gc
import timeit
import pandas as pd
import pydoop.hdfs as hd

execfile("./helpers.py")

src_x = os.environ['SRC_X_LOCAL']
src_y = os.environ['SRC_Y_LOCAL']
# TODO skip for total row count > 2e9 as data volume cap due to pandas scalability, currently just comment out in run.sh

ver = pd.__version__
print(ver)
task = "join"
question = "inner join"
l = [os.path.basename(src_x), os.path.basename(src_y)]
data_name = '-'.join(l)
solution = "pandas"
fun = "merge"
cache = "TRUE"

print("loading datasets...")

with hd.open(src_x) as f:
   x = pd.read_csv(f)

with hd.open(src_y) as f:
   y = pd.read_csv(f)

print("joining...")

gc.collect()
t_start = timeit.default_timer()
ans = x.merge(y, how='inner', on='KEY')
print ans.shape[0]
t = timeit.default_timer() - t_start
m = float('NaN')
t_start = timeit.default_timer()
chk = [ans['X2'].sum(), ans['Y2'].sum()]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], solution=solution, version=ver, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_check(chk), chk_time_sec=chkt)
del ans

gc.collect()
t_start = timeit.default_timer()
ans = x.merge(y, how='inner', on='KEY')
print ans.shape[0]
t = timeit.default_timer() - t_start
m = float('NaN')
t_start = timeit.default_timer()
chk = [ans['X2'].sum(), ans['Y2'].sum()]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], solution=solution, version=ver, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_check(chk), chk_time_sec=chkt)
del ans

gc.collect()
t_start = timeit.default_timer()
ans = x.merge(y, how='inner', on='KEY')
print ans.shape[0]
t = timeit.default_timer() - t_start
m = float('NaN')
t_start = timeit.default_timer()
chk = [ans['X2'].sum(), ans['Y2'].sum()]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], solution=solution, version=ver, fun=fun, run=3, time_sec=t, mem_gb=m, cache=cache, chk=make_check(chk), chk_time_sec=chkt)
del ans

exit(0)
