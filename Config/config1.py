import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("config.ini")
print Config.sections()
print Config.get('SectionOne', 'Status')
print Config.get('SectionOne', 'Does not exist')
