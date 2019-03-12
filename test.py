import json
import pandas
import csv

genelist = [
    "arsC",
    "arsM",
    "copA",
    "czcD",
    "arrA",
    "merA",
    "arsB",
    "czcA",
    "chrB",
    "nccA",
    "chrA",
    "copB",
    "czcB",
    "czcC",
    "merB",
    "pcoA",
    "acr3",
    "acrD",
    "aioA",
    "aioB",
    "arsA",
    "cadA",
    "copC",
    "smtA",
    "yvgW",
    "mco",
    "merE",
    "merF",
    "merP",
    "merT",
    "nirA",
    "tcrB",
    "zntA",
    "aoxB",
    "copZ",
    "dmeF",
    "actP",
    "aoxA",
    "arsD",
    "arsH",
    "cmeA",
    "cmeB",
    "cmeC",
    "ctpD",
    "cueO",
    "cusA",
    "cusC",
    "mdtA",
    "mdtB",
    "mrdH",
    "mreA",
    "pbrA",
    "pbrB",
    "rcnA",
    "zitB",
    "znuB",
    "znuC",
    "arxA",
    "cmtA",
    "ncrA",
    "nfsA",
    "nrsD",
    "srpC",
    "arrB",
    "arsP",
    "arxB1",
    "arxB2",
    "arxC",
    "cnrA",
    "arsI",
    "arsJ",
    "asoA",
    "asoB",
    "azoR",
    "cadB",
    "chrA1",
    "chrB1",
    "chrR",
    "cnrB",
    "cnrC",
    "ctpC",
    "ctpV",
    "cueA",
    "cueP",
    "cuiD",
    "cusB",
    "cutF",
    "cutO",
    "czcP",
    "cznA",
    "cznB",
    "cznC",
    "czrA",
    "czrB",
    "fieF",
    "mctB",
    "mdrL",
    "mdtC",
    "merG",
    "merH",
    "modA",
    "mymT",
    "nccB",
    "nccC",
    "nemA",
    "nia",
    "nirC",
    "nrsA",
    "nrsB",
    "pacS",
    "pfr",
    "yfmO",
    "zneB",
]


with open("results_kingdom_gene.json", "r") as read_file:
    data = json.load(read_file)

dictlist = []
for i in data:
    for key, value in i.items():
        temp = [key, value]
        dictlist.append(temp)

flat_list = [item for sublist in dictlist for item in sublist]


number = {}

for gene in genelist:
    number[gene] = flat_list.count(gene)

with open("output.csv", "w") as output:
    writer = csv.writer(output)
    for key, value in number.items():
        writer.writerow([key, value])
