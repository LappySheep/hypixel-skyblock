import json


def fileIO(filename, IO, data=None):
  if IO == "save" and data != None:
    with open(filename, encoding='utf-8', mode="w") as f:
      f.write(json.dumps(data,indent=4,sort_keys=True,separators=(',',': ')))
  elif IO == "load" and data == None:
    with open(filename, encoding='utf-8', mode="r") as f:
      return json.loads(f.read())
  elif IO == "check" and data == None:
    try:
      with open(filename, encoding='utf-8', mode="r") as f:
        return True
    except:
      return False
  else:
    raise("Invalid fileIO call.")


o=["st","nd","rd"];dw=lambda n:f"{n}th"if n in[*range(4,21),*range(24,31)]else f"{n}{o[n%10-1]}" # date wordify


def search(query):
  updates = fileIO("updates.json", "load")
  years = list(updates.keys())
  lm = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  months = [n[0:3].lower()for n in lm]
  results = []
  for year in years:
    for month in months:
      try:
        ups = updates[year][month]
      except: # no updates in this month
        continue
      for update in ups:
        u = ups[update]["content"]
        for line in u:
          if query in line:
            z = ups[update]
            results.append({
              "title": f"{z['title']}",
              "date": f"{z['date']}/{month}/{year}",
              "dword_us": f"{lm[months.index(month)]} {dw(z['date'])}, {year}",
              "id": update,
              "ref": line
            })
  return results


def variation(query):
  n = search(query)
  #
  # add more if needed
  t = search(query.title())
  n.extend(x for x in t if x not in n)
  t = search(query.lower())
  n.extend(x for x in t if x not in n)
  #
  n = sorted(n, key=lambda x:x["id"])
  return n


def copytext(lst):
  # list of references from search()
  for s in lst:
    d,i,r,t,v=s["dword_us"],s["id"],s["ref"],s["title"],"{{!}}"
    print(f"""{v}{d} {v}{v} [[patch:{i}{v}{t}]]
{v}{r}
{v}-""")



def main():
  o = input(f"Enter Query>> ")
  print("\n\n")
  copytext(variation(o))
  print("\n\n")
  return



while __name__ == "__main__":
  main()
