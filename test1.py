import g4f
import os
import subprocess
from g4f.Provider import (
    Phind
)
import art
from fp.fp import FreeProxy
from art import *
import colorama
import pyfiglet
import rich
from rich import *
from colorama import *

title = pyfiglet.figlet_format('Hacknet', font="dos_rebel")
print(f'[red]{title}[/red]')
colorama.init()
messages = [{"role" : "system", "content" : "You are 'Hacknet'"}]
proxy = FreeProxy().get()
print(proxy)
while True:
    subprocess.run(['tput', 'cup', '999', '999'])
    for i in range(2):
        print(" ")
    #input = rich.console.Console.input("[red]Question: [/red]")
    input = input(Fore.RED + Style.BRIGHT + "Question: ")
    messages.append({"role" : "user", "content" : f"{input}"})
    response = g4f.ChatCompletion.create(
        model=g4f.models.default,
        provider=g4f.Provider.Phind,
        messages=messages,
        stream=True,
    )
    answer = ''
    for i in response:
        answer += i
        os.system("cls")
        print(f'[red]{title}[/red]')
        for message in messages:
            if message == messages[-1] or messages[-2]:
                if message["role"] != "system":
                    print("[red]" + message["role"] + ": [/red]" + message["content"])
                    print("")
                    subprocess.run(['tput', 'cup', '999', '999'])
        print("[red]assistant: [/red]" + answer)
        subprocess.run(['tput', 'cup', '999', '999'])
    messages.append({"role" : "assistant", "content" : f"{answer}"})
    print(" ")
    del input
