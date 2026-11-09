---
symbol: "GRIP2"
type: "gene"
col: 6902
ensembl_id: "ENSG00000144596"
name: "glutamate receptor interacting protein 2"
location: "3p25.1"
module: 61
arm: "+"
pooled_cpm: 3.12
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# GRIP2

*glutamate receptor interacting protein 2* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.65× (z +11.6, q 1e-28, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.19× (z +10.4, q 1e-22, up in 27 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.621× (z -4.3, q 0.008, down in 13 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (PANC-1 0.251×, SW480 0.287×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (A-172 0.0509×; ⚠ cell-cycle shift, explains <1% of this change).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRA2]] (+0.64, fdr 4e-05), [[ZNF423]] (+0.59, fdr 1e-04), [[CDH23]] (+0.58, fdr 4e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PDZD4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6902.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.65×** | +11.6 | 1e-28 | 1/4 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.19×** | +10.4 | 1e-22 | 27/42 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +9.2 | 1e-17 | 17/27 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +8.1 | 9e-14 | 4/11 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +6.8 | 1e-09 | 1/7 (MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.80×** | +5.5 | 4e-06 | 1/10 (NCI-H2030) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +5.4 | 6e-06 | 10/33 (LoVo, HOP62, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.48×** | +4.4 | 6e-04 | 2/6 (PANC-1, SW1417) | rises with dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +4.2 | 0.002 | 12/30 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.12×** | +3.7 | 0.014 | 1/6 (PANC-1) | top dose only | noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.5 | 0.022 | 5/45 (HOP62, LoVo, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.030 | 4/29 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.046 | 1/27 (A-172) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.43×** | +3.0 | 0.096 | 2/17 (NCI-H460, A549) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +3.0 | 0.100 | 9/44 (HOP62, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6902.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (PANC-1 0.251×, SW480 0.287×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (A-172 0.0509×; ⚠ cell-cycle shift, explains <1% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.621×** | -4.3 | 0.008 | 13/37 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.696× | -3.4 | 0.14 | 11/42 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.702× | -3.4 | 0.14 | 5/31 (NCI-H23, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Hexylresorcinol (drug)]] 5 µM |  | 0.788× | -3.2 | 0.19 | 10/45 (PANC-1, A-427, …) | top dose only | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | 0.721× | -3.1 | 0.22 | 8/44 (PANC-1, Hs 766T, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6902. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1.96 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.11× (z +8.7) | — |
| [[SW480 (line)]] | alt | 10.6 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.65× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.59 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0509× (z -8.7) ⚠ cell-cycle shift, explains <1% of this change |
| [[PANC-1 (line)]] | alt | 8.14 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.838 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.998 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.967 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.917 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.965 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.948 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.808 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.829 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.852 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.000 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6902), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 19 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRA2]] | +0.64 | +0.42 / +0.70 | both halves | 4e-05 | **novel candidate** |
| [[ZNF423]] | +0.59 | +0.36 / +0.70 | both halves | 1e-04 |  |
| [[CDH23]] | +0.58 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[DACH2]] | +0.57 | +0.38 / +0.70 | both halves | 7e-05 |  |
| [[KCNG3]] | +0.57 | +0.35 / +0.68 | both halves | 1e-04 | pathway: Neuronal System |
| [[ADAMTS19]] | +0.56 | +0.38 / +0.62 | both halves | 7e-05 |  |
| [[HES2]] | +0.56 | +0.36 / +0.63 | both halves | 1e-04 |  |
| [[LINC02384]] | +0.56 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[PLD5]] | +0.54 | +0.32 / +0.64 | both halves | 2e-04 |  |
| [[NTN1]] | +0.54 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[NKAIN1]] | +0.53 | +0.38 / +0.60 | both halves | 7e-05 | STRING 504 |
| [[LINC02511]] | +0.53 | +0.16 / +0.65 | ⚠ one half (not replicated) | 0.001 |  |
| [[ISM1]] | +0.53 | +0.27 / +0.64 | both halves | 3e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDZD4]] | B | PDZD4 activity raises GRIP2's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 1.87× lower at baseline in the lines without PDZD4 | 0.001 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[KCNIP4]] | B | KCNIP4 activity lowers GRIP2's level | lines that do not express KCNIP4 (6) vs lines expressing it (44) | 2.18× higher at baseline in the lines without KCNIP4 | 0.008 | ⚠ within organs, on part of the lines; also absent: MLLT3, TEX9, MAMDC2-AS1; maybe low, not absent |
| [[SPOCK3]] | B | SPOCK3 activity lowers GRIP2's level | lines that do not express SPOCK3 (22) vs lines expressing it (28) | 1.26× higher at baseline in the lines without SPOCK3 | 0.036 | ⚠ within organs, on part of the lines; also absent: CTSF, NCAM2, LRP1B; maybe low, not absent |
| [[CCDC69]] | B | CCDC69 activity lowers GRIP2's level | lines that do not express CCDC69 (11) vs lines expressing it (39) | 1.60× higher at baseline in the lines without CCDC69 | 0.049 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ADAMTS19]] | B | ADAMTS19 activity lowers GRIP2's level | lines that do not express ADAMTS19 (11) vs lines expressing it (39) | 1.62× higher at baseline in the lines without ADAMTS19 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000287943, FAM13C, ABCA12; maybe low, not absent |
| [[GBX1]] | B | GBX1 activity raises GRIP2's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 1.57× lower at baseline in the lines without GBX1 | 0.090 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.505). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.1, 34.8); signed map (28.5, 22.0). **Vector** length 50.3, 6.97% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +10.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +11.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +3.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.5 | -4.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | +3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains <1% of this change | -1.4 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -3.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | glutamate receptor interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:14,489,107-14,556,075 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1719 |
| Gene groups (HGNC) | PDZ domain containing |
| Reactome | 6 pathways, smallest: Trafficking of GluR2-containing AMPA receptors; Glutamate binding, activation of AMPA receptors and synaptic plasticity; Trafficking of AMPA receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0E4](https://www.uniprot.org/uniprotkb/Q9C0E4) (Glutamate receptor-interacting protein 2):

> May play a role as a localized scaffold for the assembly of a multiprotein signaling complex and as mediator of the trafficking of its binding partners at specific subcellular location in neurons.

**Summary**, from NCBI Gene [80852](https://www.ncbi.nlm.nih.gov/gene/80852):

> Predicted to enable glutamate receptor binding activity. Predicted to be involved in several processes, including neurotransmitter receptor transport, endosome to postsynaptic membrane; positive regulation of AMPA glutamate receptor clustering; and positive regulation of excitatory postsynaptic potential. Predicted to act upstream of or within Notch signaling pathway; artery smooth muscle contraction; and positive regulation of blood pressure. Predicted to be located in dendritic shaft; neuron …

**Accessions** — [HGNC:23841](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23841) · Entrez [80852](https://www.ncbi.nlm.nih.gov/gene/80852) · UniProt [Q9C0E4](https://www.uniprot.org/uniprotkb/Q9C0E4) · Ensembl [ENSG00000144596](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144596)

## Data

Gene col 6902: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6902); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6902, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6902]; `tensor/DDL_lfc|DDL_z.npy` [6902]; `embed/gene_vectors.npy` [6902]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6902 or target_col == 6902). Every well: [[GRIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
