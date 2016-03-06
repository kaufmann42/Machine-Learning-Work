from Bio import Entrez
from Bio import Medline
Entrez.email = "kaufmann42@ufl.edu"     # Always tell NCBI who you are

handle = Entrez.esearch(db="pubmed", term="2-(2-Aminophenyl)-1H-Benzimidazole", retmax=463)
record = Entrez.read(handle)
idlist = record["IdList"]
# print(idlist)

handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline",
                           retmode="text")
records = Medline.parse(handle)

for record in records:
    print("title:", record.get("TI", "?"))
    # print("authors:", record.get("AU", "?"))
    # print("source:", record.get("SO", "?"))
    print("Abstract:", record.get("AB", "?"))

# EXAMPLE RECORD
# {'LID': '10.12688/f1000research.2-238.v3 [doi]'
# 'STAT': 'PubMed-not-MEDLINE'
# 'DEP': '20131111'
# 'DA': '20140815'
# 'AID': ['10.12688/f1000research.2-238.v3 [doi]']
# 'DCOM': '20140815'
# 'DP': '2013'
# 'OWN': 'NLM'
# 'PT': ['Journal Article']
# 'LA': ['eng']
# 'CRDT': ['2014/08/16 06:00']
# 'FAU': ['Karthikeyan
# G'
# 'Paul-Satyaseela
# Maneesh'
# 'Dhatchana Moorthy
# Nachiappan'
# 'Gopalaswamy
# Radha'
# 'Narayanan
# Shridhar']
# 'JT': 'F1000Research'
# 'PG': '238'
# 'TI': 'Functional characterization of Candida albicans Hos2 histone deacetylase.'
# 'PL': 'England'
# 'TA': 'F1000Res'
# 'JID': '101594320'
# 'AB': 'Candida albicans is a mucosal commensal organism capable of causing superficial (oral and vaginal thrush) infections in immune normal hosts
# but is a major pathogen causing systemic and mucosal infections in immunocompromised individuals. Azoles have been very effective anti-fungal agents and the mainstay in treating opportunistic mold and yeast infections. Azole resistant strains have emerged compromising the utility of this class of drugs. It has been shown that azole resistance can be reversed by the co-administration of a histone deacetylase (HDAC) inhibitor
# suggesting that resistance is mediated by epigenetic mechanisms possibly involving Hos2
# a fungal deacetylase. We report here the cloning and functional characterization of HOS2 (High Osmolarity Sensitive)
# a gene coding for fungal histone deacetylase from C. albicans. Inhibition studies showed that Hos2 is susceptible to pan inhibitors such as trichostatin A (TSA) and suberoylanilide hydroxamic acid (SAHA)
# but is not inhibited by class I inhibitors such as MS-275. This in vitro enzymatic assay
# which is amenable to high throughput could be used for screening potent fungal Hos2 inhibitors that could be a potential anti-fungal adjuvant. Purified Hos2 protein consistently deacetylated tubulins
# rather than histones from TSA-treated cells. Hos2 has been reported to be a putative NAD+ dependent histone deacetylase
# a feature of sirtuins. We assayed for sirtuin activation with resveratrol and purified Hos2 protein and did not find any sirtuin activity.'
# 'AD': 'Drug Discovery Research
# Orchid Chemicals and Pharmaceuticals Limited
# Chennai
# 600 119
# India. Drug Discovery Research
# Orchid Chemicals and Pharmaceuticals Limited
# Chennai
# 600 119
# India ; Current address: Samrud Foundation for Health & Research
# Bangalore
# 560106
# India. Drug Discovery Research
# Orchid Chemicals and Pharmaceuticals Limited
# Chennai
# 600 119
# India. Drug Discovery Research
# Orchid Chemicals and Pharmaceuticals Limited
# Chennai
# 600 119
# India. Drug Discovery Research
# Orchid Chemicals and Pharmaceuticals Limited
# Chennai
# 600 119
# India ; Current address: AstraZeneca India Pvt. Ltd
# Bengaluru
# 560024
# India.'
# 'VI': '2'
# 'IS': '2046-1402 (Electronic) 2046-1402 (Linking)'
# 'PMC': 'PMC4111124'
# 'AU': ['Karthikeyan G'
# 'Paul-Satyaseela M'
# 'Dhatchana Moorthy N'
# 'Gopalaswamy R'
# 'Narayanan S']
# 'MHDA': '2013/01/01 00:01'
# 'PHST': ['2013 [ecollection]'
# '2014/07/18 [accepted]'
# '2014/07/22 [epublish]']
# 'EDAT': '2013/01/01 00:00'
# 'SO': 'F1000Res. 2013 Nov 11;2:238. doi: 10.12688/f1000research.2-238.v3. eCollection 2013.'
# 'PMID': '25110576'
# 'PST': 'epublish'}
