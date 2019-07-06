from string import Template

tmpl = Template("""
- description: ${description}
  executionEnabled: true
  group: ${group}
  loglevel: INFO
  name: ${name}
  nodeFilterEditable: false
  nodefilters:
    dispatch:
      excludePrecedence: true
      keepgoing: false
      rankOrder: ascending
      successOnEmptyNodeFilter: false
      threadcount: 1
    filter: '${filter}'
  nodesSelectedByDefault: true
  notification:
    onfailure:
      email:
        recipients: ${recipients}
        subject: ${subject}
  retry:
    delay: ${delay}
    retry: '${retry}'
  schedule:
    month: '${month}'
    time:
      hour: '${hour}'
      minute: '${minute}'
      seconds: '${seconds}'
    weekday:
      day: '${day}'
    year: '${year}'
  scheduleEnabled: true
  sequence:
    commands:
    - description: ${command_description}
      exec: ${exec}
    keepgoing: true
    strategy: ${strategy}
  timeZone: Asia/Shanghai
  timeout: ${timeout}
""")
