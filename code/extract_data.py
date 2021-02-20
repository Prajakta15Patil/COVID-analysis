import json
import glob


def get_paper(paths):
    """
    Extract the contents from json files.
        
        Parameters:
                paths (list): Paths for all json files
                
        Returns:
                data (list): Contents from all json files
    """
    data = []
    for path in paths:
        with open(path) as json_file:
            data.append(json.load(json_file))
    return data


def merge_abstracts(paper):
    """
    Concatenate multiple paragraphs of an abstract into a single text seperated by space.
        
        Parameters:
                paper (dictionary): Contents of a json file
        Returns:
                merge_abstract (string): Single abstract
    """
    merge_abstract = ''

    if 'abstract' in paper:
        for abstract in paper['abstract']:
            merge_abstract = ' '.join([merge_abstract, abstract['text']])
    return merge_abstract



def merge_sections(paper):
    """
    Extract multiple sections within a body text and store it in a dictionary. Merge sections with
    multiple paragraphs.
        
        Parameters:
                paper (dictionary): Contents of a json file
        Returns:
                sections (dictionary): Single bodytext 
    """
    sections = {}
    for bodytext in paper['body_text']:
        section = bodytext['section']
        text = bodytext['text']
        if section in sections:
            sections[section].append(text)
        else:
            sections[section] = [text]
    for keys, value in sections.items():
        sections[keys] = ' '.join(value)
    return sections


def merge_bodytexts(paper):
    """
    Concatenate multiple paragraphs of body text into a single text seperated by space.
        
        Parameters:
                paper (dictionary): Contents of a json file
        Returns:
                merge_text (string): Single bodytext 
    """
    merge_text = ''
    for text in paper['body_text']:
        merge_text = ' '.join([merge_text, text['text']])
    return merge_text


def process_paper(paper):
    """
    Load contents from a json file into a dictionary 
        
        Parameters:
                paper (dictionary): Contents of a json file
        Returns:
                single_paper (dictionary): contents of a paper 
    """
    single_paper = {}
    single_paper['paper_id'] = paper['paper_id']
    single_paper['title'] = paper['metadata']['title']
    single_paper['abstract'] = merge_abstracts(paper)
    single_paper['section_bodytext'] = merge_sections(paper)
    single_paper['bodytext'] = merge_bodytexts(paper)
    return single_paper



def exportdata(data, path):
    """
    Store the pre-processed data as json file
        
        Parameters:
                data (list): Contents of json files
                path (list): Paths of json files
        Returns:
                single_paper (dictionary): contents of a paper 
    """
    with open(path+data['paper_id']+'.json', 'w') as data_file:
        json.dump(data, data_file)


if __name__ == '__main__':
    directory = "/home/prajakta/Documents/SharpestMinds/COVID-analysis"
    data_loc = '/'.join([directory, "papers/*/*.json"])
    final_data_loc = '/'.join([directory, "data/"])

    files = glob.glob(data_loc)
    raw_data = get_paper(files)

    for paper in raw_data:
        exportdata(process_paper(paper), final_data_loc)
