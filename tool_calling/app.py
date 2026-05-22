import os
from dotenv import load_dotenv
from tools.weather_tools import WeatherTool
from tools.file_tools import FileManagementTool
from tools.system_tools import SystemManagementTool

load_dotenv()
# Weather Tool
API_KEY = os.getenv("OPEN_WEATHER_API_KEY")

weather_tool = WeatherTool(API_KEY)
weather_result = weather_tool.invoke(city="Hyderabad", country="IN")

print("\nWeather Result:")
print(weather_result)

# File Tool
file_tool = FileManagementTool()
# Create file
print(file_tool.create_file("sample.txt", "Hello from AI Tool Calling"))
# Update file
print(file_tool.update_file("sample.txt", "New content added"))


# System Tool
system_tool = SystemManagementTool()

print("\nSystem Stats:")
print(system_tool.get_system_stats())

print("\nOpen Ports:")
print(system_tool.get_open_ports()[:5])

print("\nRunning Services:")
print(system_tool.get_running_services())