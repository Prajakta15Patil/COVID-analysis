import json
import glob


# function to extract the contents of each json file
# and store them in a list format to pre-process it later.
def get_paper(paths):
    data = []
    for path in paths:
        with open(path) as json_file:
            data.append(json.load(json_file))
    return data


def merge_abstracts(paper):
    merge_abstract = ''
    # assigns a default value to the papers that don't have any abstract
    if 'abstract' in paper:
        for abstract in paper['abstract']:
            # change logic
            merge_abstract = ' '.join([merge_abstract, abstract['text']])
    return merge_abstract


# get body text from papers
# to combine multiple body text paragraphs into a single text
def merge_sections(paper):
    sections = {}  # change the logic
    for bodytext in paper['body_text']:
        section = bodytext['section']
        text = bodytext['text']
        if section in sections:
            sections[section].append(text)
        else:
            sections[section] = [text]
    for keys, value in sections.items():
        sections[keys] = ' '.join(value)
    # print(sections)
    return sections


def merge_bodytexts(paper):
    merge_text = ''
    for text in paper['body_text']:
        merge_text = ' '.join([merge_text, text['text']])
    return merge_text


def process_paper(paper):
    single_paper = {}
    single_paper['paper_id'] = paper['paper_id']
    single_paper['title'] = paper['metadata']['title']
    single_paper['abstract'] = merge_abstracts(paper)
    single_paper['section_bodytext'] = merge_sections(paper)
    single_paper['bodytext'] = merge_bodytexts(paper)
    return single_paper


# print(len(data)) # 19458

# don't export all files into one large file. break it up.
def exportdata(data, path):
    with open(path+data['paper_id']+'.json', 'w') as data_file:
        json.dump(data, data_file)
        #print(len(data))


if __name__ == '__main__':
    directory = "/home/prajakta/Documents/SharpestMinds/COVID-analysis"
    data_loc = '/'.join([directory, "papers/*/*.json"])
    final_data_loc = '/'.join([directory, "data/"])

    files = glob.glob(data_loc)
    raw_data = get_paper(files)
    # data = []
    for paper in raw_data:
        # data.append(process_paper(paper))
        exportdata(process_paper(paper), final_data_loc)
