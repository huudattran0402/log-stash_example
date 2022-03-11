from pygrok import Grok
import pandas as pd
import json

log_df = pd.DataFrame(columns=['Time','Level','Message'])

with open('Logstash Grok\sample.log', 'r') as file:
    logs = file.readlines()
pattern = '%{TIMESTAMP_ISO8601:time} %{LOGLEVEL:logLevel} %{GREEDYDATA:logMessage}'
grok = Grok(pattern)

log_array =  []
for log in logs:
    log_array.append(grok.match(log))

print(pd.DataFrame(log_array))