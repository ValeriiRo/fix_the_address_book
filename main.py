from pprint import pprint
import csv

if __name__ == '__main__':
  with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    pprint(rows)
    contacts_list = list(rows)
  pprint(contacts_list)

  import re

  keys = []
  for lines in contacts_list:
    there_are_changes = False
    lines_str = ",".join(lines)
    pattern = re.compile(
      r'''(\w+)\,?\s*(\w+)\,?\s*(\w+)?\,?\,?\,\s*(\w+)?\,\s?(\w[А-Яа-я –]+)?[\s,]((\+7|8)?\s?\(?(\d{3})\)?\s?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})\s?\(?(доб.)?\(?\s?(\d+)?)?[\s,](\w[a-zA-Z1-9@.]+)?''')
    words_list = pattern.sub(r"\1,\2,\3,\4,\5,+7(\8)\9-\10-\11\12\13,\14", lines_str)
    words_list = words_list.split(',')
    step = 0
    for contacts in keys:
      if words_list[0] in contacts:
        if words_list[1] in contacts:
          if keys[step][2] == '':
            keys[step][2] = words_list[2]
          if keys[step][3] == '':
            keys[step][3] = words_list[3]
          if keys[step][4] == '':
            keys[step][4] = words_list[4]
          if keys[step][5] == r'+7\\()--':
            keys[step][5] = words_list[5]
          if keys[step][6] == '':
            keys[step][6] = words_list[6]
          there_are_changes = True
      step += 1
    if there_are_changes == False:
      keys += [words_list]

  with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(keys)