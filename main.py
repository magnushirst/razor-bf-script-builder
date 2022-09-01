import math
from string import Template

START_FILE = Template('''
<?xml version="1.0" encoding="utf-8"?>
<Macro xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <Name>BRUTE_FORCE_MO2_$script_number</Name>
  <Guid>513b01d0-26ca-4bc4-806d-734d94d4862$script_number</Guid>
  <MacroEvents>
''')

END_FILE = '''
  </MacroEvents>
  <IsFolder>false</IsFolder>
  <FolderGuid>00000000-0000-0000-0000-000000000000</FolderGuid>
</Macro>
'''
output_file_name = 'output/script'


split_files = int(input("How many files (default = 1): ") or 1)


with open('files/start-wrapper.txt') as f:
    start_wrapper = f.read()

with open('files/end-wrapper.txt') as f:
    end_wrapper = f.read()

with open('files/word-list.txt') as f:
    word_list = f.read().splitlines()

percentage_of_words_per_file = 1 / split_files
number_of_words_per_file = math.ceil((len(word_list) * percentage_of_words_per_file))

words_written = 0
for output_file_number in range(0, split_files):
    output_file_number += 1
    if output_file_number == split_files:
        file_word_limit = len(word_list)
    else:
        file_word_limit = words_written + number_of_words_per_file

    print(f'Creating macro for words {words_written} to {file_word_limit} in file {output_file_name}_{output_file_number}.xml')

    with open(f'{output_file_name}_{output_file_number}.xml', "w") as f:
        f.write(START_FILE.substitute(script_number=output_file_number))
        for i in range(words_written, file_word_limit):
            words_written += 1
            f.write('\n<!--START OF WORD LOOP-->\n')
            f.write(start_wrapper)
            f.write(word_list[i].lower())
            f.write(end_wrapper)
            f.write('\n<!--END OF WORD LOOP-->\n')
        f.write(END_FILE)

print('Finished')

