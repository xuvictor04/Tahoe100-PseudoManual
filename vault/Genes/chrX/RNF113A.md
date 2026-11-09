---
symbol: "RNF113A"
type: "gene"
col: 4604
ensembl_id: "ENSG00000125352"
name: "ring finger protein 113A"
location: "Xq24"
module: 12
arm: "+"
pooled_cpm: 10.38
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 4
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# RNF113A

*ring finger protein 113A* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.92× (z +6.0, q 1e-06, up in 26 of 39 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.81× (z +5.7, q 4e-06, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.632× (z -4.4, q 0.007, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCEAL8]] (+0.77, fdr 7e-06), [[ZNF622]] (+0.77, fdr 7e-06), [[MTIF3]] (+0.75, fdr 7e-06); moves opposite to [[MOB1A]] (-0.65, fdr 1e-05), [[TARDBP]] (-0.64, fdr 2e-05), [[VMA21]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4604.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +6.0 | 1e-06 | 26/39 (MIA PaCa-2, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +5.7 | 4e-06 | 33/46 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~15% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +5.3 | 3e-05 | 25/44 (LS 180, HOP62, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.55×** | +4.2 | 0.004 | 23/41 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.037 | 22/44 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.28×** | +3.3 | 0.082 | 14/43 (MIA PaCa-2, LS 180, …) | all doses, flat | composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.40× | +3.2 | 0.11 | 15/45 (SNU-423, KATO III, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 1.39× | +3.0 | 0.16 | 14/46 (LS 180, SW480, …) | all doses, flat | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4604.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.632×** | -4.4 | 0.007 | 21/47 (SNU-423, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.682×** | -3.6 | 0.079 | 9/48 (A498, Hs 766T, …) | two highest doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.682×** | -3.4 | 0.095 | 14/46 (C32, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.699×** | -3.4 | 0.095 | 17/46 (HS-578T, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.708× | -3.3 | 0.11 | 16/46 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.711× | -3.2 | 0.11 | 18/47 (SNU-423, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4604. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 6.54 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0458× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0831× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4604), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCEAL8]] | +0.77 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[ZNF622]] | +0.77 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[MTIF3]] | +0.75 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.74 | +0.58 / +0.78 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[LEO1]] | +0.73 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[RIOK2]] | +0.73 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[RP9]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[ZNHIT3]] | +0.72 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[C1orf35]] | +0.72 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[C18orf21]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[PCGF1]] ⚠ | +0.71 | +0.59 / +0.71 | both halves | 7e-06 | same gene group; ⚠ in the vector space only through flagged drug-doses |
| [[NRBF2]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.71 | +0.69 / +0.67 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 995 |
| [[SUGP1]] | +0.70 | +0.68 / +0.67 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | -0.65 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[TARDBP]] | -0.64 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[VMA21]] | -0.64 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[HNRNPA3]] | -0.63 | -0.50 / -0.66 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[IPO5]] | -0.62 | -0.45 / -0.71 | both halves | 3e-05 |  |
| [[NUP188]] | -0.61 | -0.42 / -0.65 | both halves | 4e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[PSME3]] | -0.61 | -0.41 / -0.67 | both halves | 4e-05 |  |
| [[MMGT1]] | -0.60 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[GNG12]] | -0.60 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[DHFR]] | -0.60 | -0.37 / -0.67 | both halves | 8e-05 |  |
| [[FGD5-AS1]] | -0.59 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[UBE2V1]] | -0.59 | -0.51 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.748). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-38.9, -11.0); signed map (-14.5, -7.2). **Vector** length 74.6, 15.9% of its response variance represented; |z| ≥ 3 in 592 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +2.7 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.1 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +2.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +1.8 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -0.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +2.4 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -7.9 | -1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.8 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.3 | +0.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.7 | -1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -0.8 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -1.0 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 113A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:119,870,475-119,871,733 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNF113, Cwc24; previously ZNF183 |
| Gene groups (HGNC) | Ring finger proteins; Zinc fingers CCCH-type; NTC associated proteins; Spliceosomal Bact complex; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O15541](https://www.uniprot.org/uniprotkb/O15541) (E3 ubiquitin-protein ligase RNF113A):

> Required for pre-mRNA splicing as component of the spliceosome. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs (Probable). E3 ubiquitin-protein ligase that catalyzes the transfer of ubiquitin onto target proteins. Catalyzes polyubiquitination of SNRNP200/BRR2 with non-canonical 'Lys-63'-linked polyubiquitin chains. Plays a role in DNA repair via its role in the synthesis of 'Lys-63'-linked polyubiquitin chains that recruit ALKBH3 and the ASCC …

**Summary**, from NCBI Gene [7737](https://www.ncbi.nlm.nih.gov/gene/7737):

> This intronless gene encodes a protein which contains a C3H1-type zinc finger domain and a C3HC4 Ring-type (Really Interesting New Gene-type) zinc finger domain. The Ring-type zinc finger domain is identified in various tumor suppressors, DNA repair genes and cytokine receptor-associated molecules, and is probably involved in mediating protein-protein interactions. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:12974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12974) · Entrez [7737](https://www.ncbi.nlm.nih.gov/gene/7737) · UniProt [O15541](https://www.uniprot.org/uniprotkb/O15541) · Ensembl [ENSG00000125352](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125352)

## Data

Gene col 4604: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4604); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4604, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4604]; `tensor/DDL_lfc|DDL_z.npy` [4604]; `embed/gene_vectors.npy` [4604]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4604 or target_col == 4604). Every well: [[RNF113A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF113A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
