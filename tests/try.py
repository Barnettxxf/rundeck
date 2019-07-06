import signal
import sys
import time

a = {'defaultTab': 'summary', 'description': 'simple', 'executionEnabled': True, 'group': 'simple',
     'id': 'c5aa2e58-1342-42c4-9350-2493f90a8728', 'loglevel': 'INFO', 'loglimit': '100MB', 'loglimitAction': 'halt',
     'maxMultipleExecutions': '2', 'name': 'simple', 'nodeFilterEditable': False, 'notification': {'onfailure': {
        'email': {'attachLog': True, 'attachLogInFile': True, 'recipients': 'xuxiongfeng@yimian.com.cn',
                  'subject': 'simple'}}}, 'notifyAvgDurationThreshold': None, 'retry': {'delay': '2m', 'retry': '3'},
     'schedule': {'dayofmonth': {'day': '1,12'}, 'month': '1,3,5',
                  'time': {'hour': '2', 'minute': '0/5', 'seconds': '0'}, 'year': '*'}, 'scheduleEnabled': True,
     'sequence': {'commands': [{'description': 'spider', 'exec': 'ls && sleep 10'}], 'keepgoing': False,
                  'strategy': 'node-first'}, 'timeout': '1h', 'uuid': 'c5aa2e58-1342-42c4-9350-2493f90a8728'}

for k in a.keys():
    print(f'{k} = Field()')