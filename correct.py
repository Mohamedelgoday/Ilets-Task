import language_check
lang_tool = language_check.LanguageTool("en-US")
text = "A sentence with a error in the Hitchhiker’s Guide tot he Galaxy"
matches = lang_tool.check(text)
print(matches)
print("gogooooooooooooooooooooooo")