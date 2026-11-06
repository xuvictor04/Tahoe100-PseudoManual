---
symbol: SLC30A1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [ZRC1]
gene_name: solute carrier family 30 member 1
locus: 1q32.3
locus_type: gene with protein product
gene_family: [Solute carrier family 30]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 40.5
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# SLC30A1

*solute carrier family 30 member 1* — 1q32.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/SLC30A1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | solute carrier family 30 member 1 |
| Also known as | ZRC1, zinc resistance conferring homolog (S. cerevisiae) |
| Locus | 1q32.3 — gene with protein product |
| Gene families | Solute carrier family 30 |
| Previously named | solute carrier family 30 (zinc transporter), member 1 |

**Function**, from UniProt [Q9Y6M5](https://www.uniprot.org/uniprotkb/Q9Y6M5) (reviewed):

> Zinc ion:proton antiporter that could function at the plasma membrane mediating zinc efflux from cells against its electrochemical gradient protecting them from intracellular zinc accumulation and toxicity (PubMed:31471319, PubMed:33996761, PubMed:39422023, PubMed:39111308, PubMed:39390258). Alternatively, could prevent the transport to the plasma membrane of CACNB2, the L-type calcium channels regulatory subunit, through a yet to be defined mechanism. By modulating the expression of these channels at the plasma membrane, could prevent calcium and zinc influx into cells. By the same mechanism, could also prevent L-type calcium channels-mediated heavy metal influx into cells (By similarity). In some cells, could also function as a zinc ion:proton antiporter mediating zinc entry into the lumen of cytoplasmic vesicles. In macrophages, can increase zinc ions concentration into the lumen of cytoplasmic vesicles containing engulfed bacteria and could help inactivate them (PubMed:32441444). Forms a complex with TMC6/EVER1 and TMC8/EVER2 at the ER membrane of keratynocytes which facilitates zinc uptake into the ER (PubMed:18158319). Down-regulates the activity of transcription factors induced by zinc and cytokines (PubMed:18158319). Also functions as a copper transporter, facilitating the entry of copper into cells, which is crucial for copper-induced cell death (cuproptosis) (PubMed:39111308). Acts as a Zn(2+)/Ca(2+) exchanger, exporting zinc in exchange for calcium influx (PubMed:38669333)

**Summary**, from NCBI Gene [7779](https://www.ncbi.nlm.nih.gov/gene/7779):

> Enables calcium:monoatomic cation antiporter activity and zinc:proton antiporter activity. Involved in defense response to bacterium; intracellular zinc ion homeostasis; and transition metal ion transport. Located in several cellular components, including Golgi apparatus; basolateral plasma membrane; and nuclear membrane. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:11012](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11012) · Entrez [7779](https://www.ncbi.nlm.nih.gov/gene/7779) · UniProt [Q9Y6M5](https://www.uniprot.org/uniprotkb/Q9Y6M5) · Ensembl [ENSG00000170385](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170385) · OMIM [609521](https://www.omim.org/entry/609521)

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 40.50 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 54 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.089× |
| Wild-type minus altered | 1.069× |
| Compounds moving it up in WT lines | 64 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00947 |
| As a percentage | +0.66% |
| FDR, exposure-shuffle null | 0.0167 |
| In TP53-wild-type lines / altered lines | 0.00625 / 0.01143 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.394 raw, 0.092 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
