skills_data = [
  {
    "name": "Python",
    "icon": "code",
    "level": "advanced"
  },
  {
    "name": "Power BI",
    "icon": "bar_chart",
    "level": "expert"
  },
  {
    "name": "Excel",
    "icon": "table",
    "level": "expert"
  },
]

markdown_list = []

skills_data = sorted(skills_data, key=lambda item: item.get("name", "zzz"))

for skill in skills_data:
    name = skill.get("name", "Skill")
    icon = skill.get("icon", "")
    level = skill.get("level", "intermediate")
    
    if level == "beginner":
        color = "gray"
    elif level == "intermediate":
        color = "blue"
    elif level == "advanced":
        color = "violet"
    elif level == "expert":
        color = "green"
    else:
        pass

    markdown_list.append(f":{color}-badge[:material/{icon}: {name}]")

print(" ".join(sorted(markdown_list)))