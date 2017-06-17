import urllib

def read_text():
    quotes = open("/home/srishti/Downloads/movie_quotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_read):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_read)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("No curse words found.")
    else:
        print("Could not scan the document.")

read_text()
