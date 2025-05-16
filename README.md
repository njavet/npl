# npl
Noe's pydantic language

Purpose:
To provide a clean, standardized input format for LLMs processing 
semi-structured texts (e.g. journals, config files), 
focusing on semantic clarity rather than visual markup.

## Syntax Rules
0. Sections 
<<Section name>>
* must begin at start of line
* Acts as hard semantic boundary
* No closing tags

1. Paragraphs
<Paragraph name>
* must begin at start of line
* Acts as hard semantic boundary
* No closing tags

2. Separation
* Two newlines \n\n -> paragraph break
* single newline -> for <= 79 chars per line, no semantic meaning

3. Bullet lists
start with an asterics and a newline which has semantic meaning

4. Whitespaces
everything except two newlines or single newlines in bullet point lists
will be parsed to one single whitespace. 

