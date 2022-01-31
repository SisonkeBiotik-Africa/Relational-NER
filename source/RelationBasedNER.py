from langdetect import detect
from wikibaseintegrator import wbi_functions

#Extract the recognized drug Wikidata ID and the title
drugs = {}
with open("drugNER.txt", "r", encoding="utf-8") as f:
    for line in f:
        title = line[:line.find(";")]
        drug_wid = line[line.find(";")+1:-1]
        lang = detect(title)
        #Extracting the related entities from Wikidata
        verif = wbi_functions.execute_sparql_query('SELECT * WHERE {wd:'+drug_wid+' ?prop ?object. {?object rdfs:label ?label} UNION {?object skos:altLabel ?label} FILTER(LANG(?label)="'+lang+'")}')
        related_entities = {}
        properties = {}
        for entity in verif["results"]["bindings"]:
            related_entities[entity["label"]["value"]] = entity["object"]["value"]
            properties[entity["label"]["value"]] = entity["prop"]["value"]
        #Named Entity Recognition of Related Entities
        for term in related_entities:
            if (title.find(term)>=0) and (len(term) >= 4): 
                with open("relatedNER.txt", "a", encoding="utf-8") as f1:
                    f1.write(title+";"+drug_wid+";"+properties[term][36:]+";"+related_entities[term][31:]+"\n")
