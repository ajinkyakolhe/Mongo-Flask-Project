from pymongo import MongoClient

client = MongoClient()
db = client['test-database']
if __name__ == '__main__':
    with open("api.txt", 'r', encoding='latin-1') as f:
        lll = []
        for line in f:
            line = line.split("$#$")
            print(line)
            # print("id = " + line[0])
            description = ['id', 'title', 'summary', 'rating', 'name', 'label', 'author', 'description', 'type',
                           'downloads', 'useCount', 'sampleURL', 'downloadURL', 'dateModified', 'remoteFeed',
                           'numComments', 'commentsURL', 'Tags', 'category', 'protocols', 'serviceEndpoint', 'version',
                           'wsdl', 'dataFormats', 'api groups', 'example', 'clientInstall', 'authentication', 'ssl',
                           'readonly', 'VendorAPIKits', 'CommunityAPIKits', 'blog', 'forum', 'support', 'accountReq',
                           'commercial', 'provider', 'managedBy', 'nonCommercial', 'dataLicensing', 'fees', 'limits',
                           'terms', 'company', 'updated']
            list_dict = {}
            for i in range(len(description)):
                list_dict[description[i]] = line[i]
            # list_dict = {k: v for k, v in enumerate(line)}
            #list_dict = {str(k): str(v) for k, v in list_dict.items()}
            print(list_dict, '\n')
            info = db.info
            info.insert_one(list_dict)
        print(info)
