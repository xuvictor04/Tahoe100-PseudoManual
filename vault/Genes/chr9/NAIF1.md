---
symbol: "NAIF1"
type: "gene"
col: 10067
ensembl_id: "ENSG00000171169"
name: "nuclear apoptosis inducing factor 1"
location: "9q34.11"
module: 11
arm: "+"
pooled_cpm: 4.11
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# NAIF1

*nuclear apoptosis inducing factor 1* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.69× (z +17.0, q 0e+00, up in 33 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.481× (z -8.8, q 5e-16, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF764]] (+0.84, fdr 7e-06), [[FAM200A]] (+0.84, fdr 7e-06), [[ZNF689]] (+0.83, fdr 7e-06); moves opposite to [[STRN]] (-0.69, fdr 2e-04), [[METAP1]] (-0.66, fdr 6e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10067.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.69×** | +17.0 | 0e+00 | 33/38 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.46×** | +10.9 | 3e-25 | 29/37 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.47×** | +10.6 | 9e-24 | 32/43 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.99×** | +8.4 | 9e-15 | 26/45 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +8.3 | 2e-14 | 18/39 (Hs 766T, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +4.7 | 2e-04 | 12/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.5 | 6e-04 | 11/27 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.39×** | +4.0 | 0.005 | 6/25 (SW480, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.82×** | +3.8 | 0.009 | 10/42 (SW480, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.34×** | +3.5 | 0.024 | 5/44 (SW 900, AsPC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.1 | 0.093 | 6/45 (KATO III, AsPC-1, …) | top dose only | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.31× | +3.0 | 0.13 | 4/37 (LoVo, A-172, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10067.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.481×** | -8.8 | 5e-16 | 26/46 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.648×** | -5.2 | 5e-05 | 16/46 (HEC-1-A, A-172, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.667×** | -4.9 | 2e-04 | 14/46 (A-172, SW1417, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.696×** | -4.4 | 0.002 | 13/39 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.507×** | -4.3 | 0.002 | 9/42 (SHP-77, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.707×** | -4.2 | 0.003 | 14/46 (LOX-IMVI, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Trimetrexate (drug)]] 5 µM |  | 0.829× | -3.2 | 0.11 | 7/44 (HT-29, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10067. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 4.36 | 0 | 2 | — | [[Radotinib (drug)]] 0.5 µM 0.0692× (z -10.2) |
| [[A-427 (line)]] | wt | 5.18 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.0934× (z -9.8) |
| [[A498 (line)]] | wt | 3.22 | 0 | 1 | — | [[Ixazomib (drug)]] 0.05 µM 0.0902× (z -9.5) |
| [[HS-578T (line)]] | alt | 3.51 | 0 | 1 | — | [[Gallic acid (drug)]] 0.05 µM 0.0739× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 3.63 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.05 µM 0.0788× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 3.42 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0776× (z -9.4) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 4.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +10.4) | — |
| [[A-172 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10067), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF764]] | +0.84 | +0.84 / +0.71 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.84 | +0.84 / +0.72 | both halves | 7e-06 |  |
| [[ZNF689]] | +0.83 | +0.82 / +0.71 | both halves | 7e-06 |  |
| [[METTL18]] | +0.81 | +0.82 / +0.68 | both halves | 7e-06 |  |
| [[ZNF181]] | +0.80 | +0.81 / +0.63 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.80 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[MAD2L1BP]] | +0.78 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[ZBTB6]] | +0.77 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[HELQ]] | +0.77 | +0.79 / +0.60 | both halves | 7e-06 |  |
| [[PEX12]] | +0.77 | +0.80 / +0.69 | both halves | 7e-06 |  |
| [[ZNF75A]] | +0.77 | +0.82 / +0.66 | both halves | 7e-06 |  |
| [[FIZ1]] | +0.77 | +0.81 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRN]] | -0.69 | -0.77 / -0.31 | both halves | 2e-04 |  |
| [[METAP1]] | -0.66 | -0.71 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises NAIF1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF155]] | B | ZNF155 activity raises NAIF1's level | lines that do not express ZNF155 (5) vs lines expressing it (45) | 1.05× lower at baseline in the lines without ZNF155 | 0.079 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF540, ZNF529-AS1, AGK |
| [[NRIP1]] | B | NRIP1 activity lowers NAIF1's level | lines that do not express NRIP1 (8) vs lines expressing it (42) | 1.18× higher at baseline in the lines without NRIP1 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |
| [[EID2]] | C | EID2 activity raises NAIF1's level | lines that do not express EID2 (3) vs lines expressing it (47) | 1.42× lower at baseline in the lines without EID2 | 0.069 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.847). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.8, 6.9); signed map (4.1, -20.3). **Vector** length 62.3, 8.84% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +17.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +10.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +8.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.7 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.3 | +1.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.1 | -8.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.7 | -4.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.5 | -5.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.2 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.1 | -4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -4.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -0.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -1.4 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -0.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | nuclear apoptosis inducing factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,061,233-128,068,206 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp762G199, bA379C10.2; previously C9orf90 |
| Gene groups (HGNC) | Harbinger transposase derived genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q69YI7](https://www.uniprot.org/uniprotkb/Q69YI7) (Nuclear apoptosis-inducing factor 1):

> Induces apoptosis.

**Summary**, from NCBI Gene [203245](https://www.ncbi.nlm.nih.gov/gene/203245):

> Involved in negative regulation of cell growth and regulation of mitochondrial membrane permeability involved in apoptotic process. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25446](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25446) · Entrez [203245](https://www.ncbi.nlm.nih.gov/gene/203245) · UniProt [Q69YI7](https://www.uniprot.org/uniprotkb/Q69YI7) · Ensembl [ENSG00000171169](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171169)

## Data

Gene col 10067: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10067); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10067, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10067]; `tensor/DDL_lfc|DDL_z.npy` [10067]; `embed/gene_vectors.npy` [10067]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10067 or target_col == 10067). Every well: [[NAIF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAIF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
