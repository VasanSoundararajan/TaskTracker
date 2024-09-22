import click
import json
import os

@click.command()
@click.argument('name', default='list')
@click.option('--index', '-i', default="", help='Index of the item')
@click.option('--update', '-u', default="", help='Updated value of the item')

def main(name, index=0, update=""):
    # Check if the file exists
    if os.path.exists('Data.json'):
        with open('Data.json', 'r') as file:
            data = json.load(file)
            # If the data is a dictionary, turn it into a list for task management
            if isinstance(data, dict):
                data = [data]
    else:
        # Initialize data as an empty list if the file doesn't exist
        data = []
    
    if name == "add":
        corup = {
                 "Task": update,
                 "Status":"Undone"
                }
        data.append(corup)  # Append the new task to the list
        
        # Write the updated list back to the file
        with open('Data.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Item added successfully")

    elif name=="delete":
        if index.isdigit() and 1<=int(index)<=len(data):
            del data[int(index)-1]
            with open('Data.json', 'w') as f:
                json.dump(data, f, indent=4)
            print("Item deleted successfully")

    elif name == "list":
        if data:
            for i, item in enumerate(data, start=1):
                print(f"{i}. {item['Task']}")
        else:
            print("No tasks available")

    elif name=="update":
        if index.isdigit() and 1<=int(index)<=len(data):
            data[int(index)-1]["Status"] = update
            with open('Data.json', 'w') as f:
                json.dump(data, f, indent=4)
            print("Item updated successfully")
    
    elif name=="listdone":
        if data:
            for i, item in enumerate(data, start=1):
                if item["Status"]=="Done":
                    print(f"{i}. {item['Task']}")

    elif name=="listundone":
        if data:
            for i, item in enumerate(data, start=1):
                if item["Status"]=="Undone":
                    print(f"{i}. {item['Task']}")

    elif name=="listdo":
        if data:
            for i, item in enumerate(data, start=1):
                if item["Status"]=="Todo":
                    print(f"{i}. {item['Task']}")

if __name__ == '__main__':
    main()
