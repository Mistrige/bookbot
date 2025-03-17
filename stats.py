def get_book_text(path):
    with open(path) as f:
            return f.read()

def get_num_words(path):
     text = get_book_text(path)
     count = len(text.split())
     return count
     

def get_letter_count(path):
     dict1 = {}
     text = get_book_text(path)
     lowercase = text.lower()
     seperate = list(lowercase)
     for o in range(len(seperate)):
          if seperate[o] in dict1:
               dict1[seperate[o]] += 1
          else:
               dict1[seperate[o]] = 1
     return dict1

def sorting(dict2):
     return dict2[1]

def sorted1(path):
     dict2 = get_letter_count(path)
     lest = list(dict2.items())
     lest.sort(reverse=True, key=sorting)
     lest2 = []
     for i in range (len(lest)):
          stringy = str(lest[i][0])
          if stringy.isalpha():
               lest2.append(lest[i])
     lest3 = []
     for o in range (len(lest2)):
        stringer = str(lest2[o][0] + ": " + str(lest2[o][1]))
        lest3.append(stringer)
     return lest3
