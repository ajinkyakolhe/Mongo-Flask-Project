from pymongo import MongoClient

client = MongoClient()
db = client['mashup_db']
if __name__ == '__main__':
    with open("mashup.txt", 'r', encoding='latin-1') as f:
        lll = []
        for line in f:
            line = line.split("$#$")

            line[15] = (line[15]).split("###")

            line[16] = (line[16]).split("###")
            #print(line[16])
            line[16] = [w.replace('$$$', ': ') for w in line[16]]
            #print(line[16])
            print(line)
            description = ['id', 'title', 'summary', 'rating', 'name', 'label', 'author', 'description', 'type',
                           'downloads', 'useCount', 'sampleURL', 'dateModified', 'numComments', 'commentsURL', 'Tags',
                           'APIs', 'updated']
            # list_dict = {key: value for (description, line) in iterable}

            list_dict = {}
            for i in range(len(description)):
                list_dict[description[i]] = line[i]
            # list_dict = {k: v for k, v in enumerate(line)}
            # list_dict = {str(k): str(v) for k, v in list_dict.items()}
            #print(list_dict, '\n')
            info = db.info
            info.insert_one(list_dict)
        print(info)
