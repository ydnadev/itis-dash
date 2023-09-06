# ITIS Data Dash

Simple dashboard of taxonomic data sourced from ITIS [[1]](#1).
Dashboard: https://itis-taxonomy-search.streamlit.app/

## Usage

### Dashboard
![Name Search](data/name_search.png)
![Scientific Name Search](data/sci_name_search.png)

### Data
*Note - ITIS database does not exist in this repository, download ITIS data from source below.* 

Extract data from ITIS SQLite db  
    - run src/script1-species.sql to dump data for all species as tsv to *itisdata/species.txt*  
    - run src/script1-subspecies.sql to dump data for all species as tsv to *itisdata/subspecies.txt*  
    - run src/script2-species.sql to dump data for all taxa hierarchy as csv to *itisdata/taxa-species.csv*  
    - run src/script2-subspecies.sql to dump data for all taxa hierarchy as csv to *itisdata/taxa-subspecies.csv*  

Parsing assumes 2 files above- 
```bash
perl src/itis_parser.pl 
```

Dashboard -
```bash
streamlit run itis_dash.py
```
## References
<a id="1">[1]</a> 
Retrieved from the Integrated Taxonomic Information System (ITIS) on-line database, www.itis.gov, CC0
https://doi.org/10.5066/F7KH0KBK  
<a id="2">[2]</a> Built on Streamlit - https://streamlit.io/

## Maintainers
The Conservation Technology Lab at the San Diego Zoo Wildlife Alliance
