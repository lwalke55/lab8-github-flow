from adventure.utils import read_events_from_file
from rich.console import Console
from rich import print
import random

default_message = "[bold red]You stand still, unsure what to do. The forest swallows you.[/bold red]"

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return default_message

def left_path(event):
    return "[yellow]You walk left. " + event + "[/yellow]"

def right_path(event):
    return "[magenta]You walk right. " + event + "[/magenta]"

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    print("You wake up in a dark forest. You can go left or right.")
    while True:
        console = Console()
        choice = console.input("[bold green]Which direction do you choose?[/bold green] ([yellow]left[/yellow]/[magenta]right[/magenta]/[red]exit[/red]): ")
        choice = choice.strip().lower()
        if choice == 'exit':
            print("goodbye")
            break
        
        print(step(choice, events))
