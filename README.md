# Analysis_ENCODE_RNAseq
Analyze the expression level in RNA-seq deposited in ENCODE.  

ENCODE project has a lot of RNA-seq data. Here I use these resources for my research.

## RNA-seq of K562 cells
ENCSR620PUP : Control shRNA against no target in K562 cells followed by RNA-seq. (PE,100bp,strand-specific,Hi-seq 2000)
https://www.encodeproject.org/experiments/ENCSR620PUP/

ENCODE project mapped (STAR) and quantified the RNA-seq. We can obtain the data at GEO
(GSM2343937 https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343937)
(GSM2343938	https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343938)

By DL "GSM2343937_ENCFF834UXF_gene_quantifications_GRCh38.tsv.gz"
```
wget ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM2343nnn/GSM2343937/suppl/GSM2343937_ENCFF834UXF_gene_quantifications_GRCh38.tsv.gz
gzip -d GSM2343937_ENCFF834UXF_gene_quantifications_GRCh38.tsv.gz
```
I can get ensembl_id, transcript lengths, FPKM, etc.

As there is no gene_symbol, I made ensemblTOsymbol.py (written in python2).
It uses mygene (https://pypi.org/project/mygene/) to convert ensembl_id into gene_symbol.

### Input file
Input file is "ensembl.txt" which contains a ensembl_id in each line.

### output file
Output file will be "symbol.txt" ("ensembl_id" : "corresponding symbol")
