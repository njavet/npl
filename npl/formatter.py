import re



def unify_small_sections(sections: list[str]) -> list[str]:
    new_sections = []
    curr = ''
    for section in sections:
        if len(curr) + len(section) <= conf.DOC_CHUNK_SIZE:
            curr = '\n\n'.join([curr, section])
        else:
            new_sections.append(curr)
            curr = ''
    return new_sections


def split_big_sections(sections: list[str]) -> list[str]:
    # TODO how to parse a docx file into desired llm input style ?
    #  TODO extract section header
    for section in sections:
        if len(section) > conf.DOC_CHUNK_SIZE:
            # TODO split
            pass
    return sections


# TODO if a section separated with '\n\n' contains too many characters,
#  split into two sections with same title
def raw_text_formatter(text: str) -> str:
    # remove leading and training ws
    text = '\n'.join(line.strip() for line in text.splitlines())
    # replace tabs
    text = re.sub(r'\t+', ' ', text)
    # replace multiple ws with one ws
    text = re.sub(r'[ ]{2,}', ' ', text)
    # replace 3+ newlines with 2
    text = re.sub(r'\n{3,}', '\n\n', text)
    # replace non semantic newlines
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
    # restore bullet point list
    text = re.sub(r'(?<!\n)\* ', r'\n* ', text)
    text = '\n'.join(line.strip() for line in text.splitlines())
    return text
