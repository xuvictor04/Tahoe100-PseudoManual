---
symbol: "RPAIN"
type: "gene"
col: 4955
ensembl_id: "ENSG00000129197"
name: "RPA interacting protein"
location: "17p13.2"
module: 24
arm: "+"
pooled_cpm: 35.18
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# RPAIN

*RPA interacting protein* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.52× (z +7.0, q 7e-10, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.404× (z -5.1, q 2e-04, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM26]] (+0.74, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[EPB41L4A-AS1]] (+0.70, fdr 7e-06), [[UBE2B]] (+0.70, fdr 7e-06), [[SNHG7]] (+0.70, fdr 7e-06); moves opposite to [[MAPRE1]] (-0.67, fdr 6e-05), [[TARDBP]] (-0.65, fdr 6e-05), [[IPO5]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4955.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +7.0 | 7e-10 | 37/48 (BT-474, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.76×** | +7.0 | 7e-10 | 34/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +6.6 | 9e-09 | 34/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.64×** | +6.1 | 1e-07 | 36/47 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.24×** | +3.7 | 0.024 | 22/48 (A-172, HS-578T, …) | top dose only | composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.70×** | +3.6 | 0.029 | 24/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.65×** | +3.4 | 0.057 | 18/48 (SW480, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.60×** | +3.2 | 0.086 | 16/48 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.29×** | +3.2 | 0.086 | 23/46 (PANC-1, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.56× | +3.0 | 0.15 | 12/48 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4955.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.404×** | -5.1 | 2e-04 | 33/47 (SNU-1, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.672×** | -4.9 | 2e-04 | 31/47 (PANC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.722×** | -4.1 | 0.009 | 21/48 (PANC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.728×** | -4.0 | 0.011 | 26/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.537×** | -3.5 | 0.052 | 23/49 (HT-29, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4955. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 27.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.97× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[C-33 A (line)]] | alt | 63.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 42.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 29.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +8.6) | — |
| [[C32 (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 33.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 55.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 33.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -12.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SW48 (line)]] | wt | 56.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0865× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 70.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.10× (z +8.5) | — |
| [[A498 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4955), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | +0.74 | +0.59 / +0.75 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[EPB41L4A-AS1]] | +0.70 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[UBE2B]] | +0.70 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[SNHG7]] | +0.70 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[PCGF1]] ⚠ | +0.68 | +0.44 / +0.71 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SAT2]] | +0.67 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[TMEM258]] | +0.66 | +0.34 / +0.76 | both halves | 1e-04 |  |
| [[ZFAND2B]] | +0.66 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[INAFM1]] | +0.66 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[CHCHD5]] | +0.65 | +0.31 / +0.69 | both halves | 2e-04 |  |
| [[LAMTOR5]] | +0.65 | +0.21 / +0.76 | both halves | 6e-04 |  |
| [[SNHG32]] | +0.64 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[NKAP]] | +0.64 | +0.47 / +0.72 | both halves | 2e-05 |  |
| [[RAB24]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE1]] | -0.67 | -0.38 / -0.71 | both halves | 6e-05 |  |
| [[TARDBP]] | -0.65 | -0.38 / -0.73 | both halves | 6e-05 |  |
| [[IPO5]] | -0.65 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[PSME3]] | -0.64 | -0.40 / -0.70 | both halves | 5e-05 |  |
| [[MOB1A]] | -0.62 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[STMP1]] | -0.62 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[VMA21]] | -0.61 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[EIF5A]] | -0.61 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[BTBD1]] | -0.60 | -0.34 / -0.66 | both halves | 1e-04 |  |
| [[LAMC1]] | -0.60 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[TMX1]] | -0.59 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[EMC1]] | -0.59 | -0.45 / -0.64 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.738). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.5, -27.8); signed map (-15.8, -1.6). **Vector** length 90.8, 24.3% of its response variance represented; |z| ≥ 3 in 618 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +3.2 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.4 | +1.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.3 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +2.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.1 | +3.2 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.5 | -0.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.1 | -1.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.3 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | +0.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -2.9 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -5.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | RPA interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:5,419,641-5,432,877 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4189, RIP, hRIP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UA6](https://www.uniprot.org/uniprotkb/Q86UA6) (RPA-interacting protein):

> Mediates the import of RPA complex into the nucleus, possibly via some interaction with importin beta. Isoform 2 is sumoylated and mediates the localization of RPA complex into the PML body of the nucleus, thereby participating in RPA function in DNA metabolism.

**Summary**, from NCBI Gene [84268](https://www.ncbi.nlm.nih.gov/gene/84268):

> Predicted to enable zinc ion binding activity. Acts upstream of or within protein import into nucleus and response to UV. Located in PML body and cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28641](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28641) · Entrez [84268](https://www.ncbi.nlm.nih.gov/gene/84268) · UniProt [Q86UA6](https://www.uniprot.org/uniprotkb/Q86UA6) · Ensembl [ENSG00000129197](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129197)

## Data

Gene col 4955: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4955); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4955, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4955]; `tensor/DDL_lfc|DDL_z.npy` [4955]; `embed/gene_vectors.npy` [4955]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4955 or target_col == 4955). Every well: [[RPAIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPAIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
