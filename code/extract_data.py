import json
import os
# data = []  # list of dictionaries to store cleaned data


# function to extract the contents of each json file
# and store them in a list format to pre-process it later.
def getrawdata(path):
    raw_data = []  # to store the contents from raw files
    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file = dirname + '/' + filename

            with open(file) as json_file:
                raw_data.append(json.load(json_file))
    return raw_data


# print(raw_data[5])
# print(len(raw_data))  # 19458 files


def cleancontent(raw_data):
    single_paper = {}
    for each_paper in raw_data:
        # if each_paper['paper_id'] == 'PMC3091733':
        single_paper['paper_id'] = each_paper['paper_id']
        single_paper['title'] = each_paper['metadata']['title']

        # get abstracts from papers
        # to combine multiple abstract paragraphs into a single paragraph
        merge_abstract = ""
        # assigns a default value to the papers that don't have any abstract
        if 'abstract' in each_paper:
            for each_abstract in each_paper['abstract']:
                merge_abstract = ''.join(each_abstract['text'])
                # change this logic

        single_paper['abstract'] = merge_abstract

        # get body text from papers
        # to combine multiple body text paragraphs into a single text
        merge_bodytext = []
        sections = {}  # change the logic
        for each_bodytext in each_paper['body_text']:
            if each_bodytext['section'] in sections:
                merge_bodytext.append(each_bodytext['text'])
            else:
                section_text = 'SECTION:' + each_bodytext['section']
                body_text = each_bodytext['text']
                whole_text = ' '.join([section_text, body_text])
                merge_bodytext.append(whole_text)
                sections.append(each_bodytext['section'])

        merge_bodytext = ''.join(merge_bodytext)
        single_paper['body_text'] = merge_bodytext

        data.append(single_paper)

    return data


# print(len(data)) # 19458


def exportdata(data, path):
    with open(data_loc+'covid_papers.json', 'w') as data_file:
        json.dump(data, data_file)
        print("File written")


if __name__ == '__main__':
    data_loc = "/home/prajakta/Documents/SharpestMinds/COVID-analysis/papers/"
    raw_data = getrawdata(data_loc)
    data = cleancontent(raw_data)
    data_loc = "/home/prajakta/Documents/SharpestMinds/COVID-analysis/data/"
    exportdata(data, data_loc)
