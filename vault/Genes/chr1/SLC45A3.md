---
symbol: "SLC45A3"
type: "gene"
col: 8184
ensembl_id: "ENSG00000158715"
name: "solute carrier family 45 member 3"
location: "1q32.1"
module: 158
arm: "+"
pooled_cpm: 2.75
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# SLC45A3

*solute carrier family 45 member 3* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.75× (z +16.5, q 0e+00, up in 20 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM: 0.584× (z -4.7, q 0.001, down in 13 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGA7B]] (+0.63, fdr 9e-06), [[HMGA1]] (+0.62, fdr 1e-05), [[PHLDA1]] (+0.62, fdr 1e-05); moves opposite to [[GAPVD1]] (-0.49, fdr 3e-05), [[LAMTOR2]] (-0.48, fdr 1e-04).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LEMD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8184.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.75×** | +16.5 | 0e+00 | 20/29 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.81×** | +9.1 | 2e-17 | 10/29 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.61×** | +7.8 | 1e-12 | 1/5 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +7.1 | 1e-10 | 1/3 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +5.3 | 1e-05 | 4/11 (SW1417, A498, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +4.0 | 0.007 | 1/15 (KATO III) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.007 | 5/28 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8184.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.584×** | -4.7 | 0.001 | 13/43 (HepG2/C3A, CFPAC-1, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.659×** | -4.5 | 0.002 | 19/40 (CFPAC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.657×** | -3.7 | 0.030 | 9/44 (SW 900, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.448×** | -3.7 | 0.030 | 11/34 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.710×** | -3.6 | 0.036 | 12/42 (CFPAC-1, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.652×** | -3.5 | 0.045 | 11/43 (HepG2/C3A, PANC-1, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.691×** | -3.3 | 0.073 | 12/38 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM |  | **0.671×** | -3.3 | 0.073 | 6/39 (A549, A-427, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.495×** | -3.2 | 0.073 | 8/28 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | 0.738× | -3.1 | 0.12 | 11/43 (CFPAC-1, SW48, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8184. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1.34 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +10.3) | [[Bimatoprost (drug)]] 0.05 µM 0.0553× (z -8.9) |
| [[A-172 (line)]] | wt | 2.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +12.0) | — |
| [[HEC-1-A (line)]] | alt | 6.50 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0701× (z -11.1) |
| [[HOP62 (line)]] | alt | 2.57 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0521× (z -9.5) |
| [[LoVo (line)]] | wt | 2.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.46× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 1.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +8.6) | — |
| [[SW480 (line)]] | alt | 4.21 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0849× (z -10.5) |
| [[A-427 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.938 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.909 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8184), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA7B]] | +0.63 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[HMGA1]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[PHLDA1]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[MYEOV]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[CYB5R2]] | +0.61 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[BCAN-AS2]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[EPHA2]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ADAP1]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[FOSL1]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[LTBP2]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[PADI1]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[HLA-K]] | +0.59 | +0.53 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GAPVD1]] | -0.49 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[LAMTOR2]] | -0.48 | -0.57 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LEMD1]] | B | LEMD1 activity raises SLC45A3's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 1.57× lower at baseline in the lines without LEMD1 | 0.029 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[MIR4280HG]] | B | MIR4280HG activity raises SLC45A3's level | lines that do not express MIR4280HG (21) vs lines expressing it (29) | 1.34× lower at baseline in the lines without MIR4280HG | 0.050 | ⚠ within organs, on part of the lines; also absent: EVA1A, MILR1, LNX1; maybe low, not absent |
| [[TINAGL1]] | B | TINAGL1 activity raises SLC45A3's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.45× lower at baseline in the lines without TINAGL1 | 0.084 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[VAV1]] | B | VAV1 activity raises SLC45A3's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 1.24× lower at baseline in the lines without VAV1 | 0.089 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity raises SLC45A3's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.2, 1.4); signed map (8.0, 39.0). **Vector** length 62.0, 9.56% of its response variance represented; |z| ≥ 3 in 1,106 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +16.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.3 | +0.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.4 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -4.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.6 | -4.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.5 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 45 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:205,657,851-205,680,509 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IPCA-6, prostein, IPCA-2, IPCA-8; previously PCANAP6, PCANAP2, PCANAP8 |
| Gene groups (HGNC) | Solute carrier family 45 |
| Reactome | 3 pathways, smallest: Cellular hexose transport; SLC-mediated transmembrane transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JT2](https://www.uniprot.org/uniprotkb/Q96JT2) (Solute carrier family 45 member 3):

> Proton-associated sucrose transporter. May be able to transport also glucose and fructose.

**Summary**, from NCBI Gene [85414](https://www.ncbi.nlm.nih.gov/gene/85414):

> Predicted to enable sucrose:proton symporter activity. Predicted to be involved in several processes, including positive regulation of fatty acid biosynthetic process; positive regulation of glucose metabolic process; and regulation of oligodendrocyte differentiation. Predicted to be located in plasma membrane. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:8642](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8642) · Entrez [85414](https://www.ncbi.nlm.nih.gov/gene/85414) · UniProt [Q96JT2](https://www.uniprot.org/uniprotkb/Q96JT2) · Ensembl [ENSG00000158715](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158715)

## Data

Gene col 8184: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8184); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8184, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8184]; `tensor/DDL_lfc|DDL_z.npy` [8184]; `embed/gene_vectors.npy` [8184]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8184 or target_col == 8184). Every well: [[SLC45A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC45A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
