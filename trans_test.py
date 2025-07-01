from deep_translator import GoogleTranslator


text = """If you spend any time working in a team of software developers, you’ll notice onething: people
 make mistakes. Have you ever heard the old joke about asking 10 econ-omists a question and
 getting 11 different answers? It’s like that when you have a list ofthings to do: if you have 10 things
 to do, you’ll make 11 mistakes doing them.Another thing you’ll notice is that people are different.
 Bob isn’t the same personas Ted. When we look at Bob’s workstation, everything is organized and
 tidy. Every-thing is where it should be."""



result = GoogleTranslator(source='en', target='ru').translate(text)



print(result)
