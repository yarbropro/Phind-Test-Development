response = g4f.ChatCompletion.create(
    model=g4f.models.default,
    provider=g4f.Provider.Phind,
    messages=[{"role": "user", "content": "What Can you do?"}],
    stream=True,
)
answer = ''
for i in response:
    answer += i
    os.system("clear")
    print(answer)