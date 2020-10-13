#!/bin/bash
# determine language 
language_of_file() {
    language=`file -b job_description.txt` 
    if [[ $language =~ "ASCII text" ]]
    then
    echo "ENGLISH"
    fill_english_template
    else 
    echo "GERMAN"
    fill_german_template
    fi
}
#fill_english_template() {

#}

#fill_german_template() {

#}

#extract_info() {
    
#}
language_of_file

python3 requirment
