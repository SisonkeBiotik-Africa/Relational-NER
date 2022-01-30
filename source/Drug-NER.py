from langdetect import detect

#Generating the Dict for Drug NER
drugs = {}
with open("drugs.tsv", "r", encoding="utf-8") as f:
    for line in f:
        drug = line[:-1].split("\t")
        print(drug)
        wid = drug[0][31:]
        label = drug[1]
        lang = drug[2]
        drugs[label+"-"+lang] = wid

#Identifying drugs in dataset
with open("dataset.csv", "r", encoding="utf-8") as f1:
    for line01 in f1:
        title = line01[line01.find(',')+1:-1]
        title = title[title.find(',')+1:-1]
        lang_title = detect(title)
        considered_entities = [x[:-3] for x in drugs if x.find("-"+lang_title) == len(x)-3]
        for item in considered_entities:
            if (title.find(item)>=0):
                with open("drugNER.txt", "a", encoding="utf-8") as f2:
                    f2.write(title+";"+drugs[item+"-"+lang_title]+"\n")
