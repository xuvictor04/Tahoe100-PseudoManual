---
symbol: "SMIM29"
type: "gene"
col: 11832
ensembl_id: "ENSG00000186577"
name: "small integral membrane protein 29"
location: "6p21.31"
module: 20
arm: "-"
pooled_cpm: 7.91
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# SMIM29

*small integral membrane protein 29* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.86× (z +7.8, q 3e-12, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.271× (z -5.3, q 7e-05, down in 29 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[N4BP3]] (+0.71, fdr 7e-06), [[POLD4]] (+0.66, fdr 3e-05), [[EML2]] (+0.61, fdr 1e-05); moves opposite to [[ATP2A2]] (-0.62, fdr 1e-05), [[TARDBP]] (-0.61, fdr 4e-05), [[HNRNPA3]] (-0.59, fdr 3e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HES6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11832.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **2.86×** | +7.8 | 3e-12 | 38/46 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.86×** | +6.8 | 3e-09 | 25/42 (A-172, HOP62, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.90×** | +5.0 | 1e-04 | 25/37 (A498, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.011 | 20/47 (SW480, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.081 | 19/47 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.51× | +3.1 | 0.18 | 15/34 (A-172, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11832.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.271×** | -5.3 | 7e-05 | 29/46 (AsPC-1, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.317×** | -4.7 | 9e-04 | 26/40 (NCI-H2030, SNU-423, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.586×** | -4.2 | 0.006 | 23/46 (H4, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM |  | **0.694×** | -4.0 | 0.007 | 26/47 (H4, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.598×** | -4.0 | 0.007 | 18/45 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.579×** | -3.9 | 0.008 | 23/48 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.626×** | -3.4 | 0.042 | 15/46 (BT-474, NCI-H2347, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.643×** | -3.4 | 0.042 | 21/47 (SW480, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.647×** | -3.4 | 0.044 | 15/48 (SW480, Hs 766T, …) | all doses, flat | position effect removed |
| [[Anethole trithione (drug)]] 0.05 µM |  | **0.658×** | -3.3 | 0.064 | 14/47 (HT-29, SNU-423, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.638×** | -3.2 | 0.065 | 16/46 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Minodronic acid (drug)]] 0.05 µM |  | **0.656×** | -3.1 | 0.094 | 13/47 (SW 1271, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[RMC-6236 (drug)]] 5 µM |  | **0.470×** | -3.1 | 0.094 | 17/47 (SHP-77, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.666×** | -3.0 | 0.097 | 18/45 (HepG2/C3A, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11832. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 14.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +11.6) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A-427 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.144× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~62% of this change |
| [[HT-29 (line)]] | alt | 4.60 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0631× (z -8.7) |
| [[KATO III (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.217× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11832), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N4BP3]] | +0.71 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[POLD4]] | +0.66 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[EML2]] | +0.61 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[TIPRL]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ADPRM]] | +0.61 | +0.58 / +0.64 | both halves | 7e-06 | STRING 622 |
| [[SNHG8]] | +0.61 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[FBXW5]] | +0.61 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[UPP1]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[RIN1]] | +0.60 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[SNHG7]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SURF2]] | +0.60 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[SNHG32]] | +0.60 | +0.60 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP2A2]] | -0.62 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[TARDBP]] | -0.61 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[HNRNPA3]] | -0.59 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[FUCA2]] | -0.59 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[CMPK1]] | -0.59 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[TMX1]] | -0.59 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[GTF2I]] | -0.58 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[HNRNPM]] | -0.57 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[MOB1A]] | -0.57 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[RBBP4]] | -0.57 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[SMU1]] | -0.57 | -0.34 / -0.63 | both halves | 1e-04 |  |
| [[EMC1]] | -0.57 | -0.45 / -0.61 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES6]] | B | HES6 activity raises SMIM29's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.38× lower at baseline in the lines without HES6 | 0.072 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HOMER3]] | C | HOMER3 activity raises SMIM29's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without HOMER3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.603). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (6.8, 2.3); signed map (-22.3, 20.3). **Vector** length 87.5, 20.9% of its response variance represented; |z| ≥ 3 in 702 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.5 | +6.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.8 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +1.9 | +2.6 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.0 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.8 | -3.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.6 | -5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.2 | +1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | small integral membrane protein 29 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:34,246,381-34,249,108 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LBH, MGC57858; previously C6orf1 |
| Matched by | ensembl_id |

UniProt [Q86T20](https://www.uniprot.org/uniprotkb/Q86T20) carries no function annotation.

**Summary**, from NCBI Gene [221491](https://www.ncbi.nlm.nih.gov/gene/221491):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1340](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1340) · Entrez [221491](https://www.ncbi.nlm.nih.gov/gene/221491) · UniProt [Q86T20](https://www.uniprot.org/uniprotkb/Q86T20) · Ensembl [ENSG00000186577](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186577)

## Data

Gene col 11832: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11832); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11832, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11832]; `tensor/DDL_lfc|DDL_z.npy` [11832]; `embed/gene_vectors.npy` [11832]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11832 or target_col == 11832). Every well: [[SMIM29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMIM29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
