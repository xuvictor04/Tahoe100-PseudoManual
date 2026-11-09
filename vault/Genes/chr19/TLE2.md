---
symbol: "TLE2"
type: "gene"
col: 803
ensembl_id: "ENSG00000065717"
name: "TLE family member 2, transcriptional corepressor"
location: "19p13.3"
module: 100
arm: "+"
pooled_cpm: 5.6
n_lines_expressing: 40
n_dd_up: 12
n_dd_down: 16
n_dd_up_clean: 9
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 6
direction_downstream: 4
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# TLE2

*TLE family member 2, transcriptional corepressor* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.10× (z +20.1, q 0e+00, up in 18 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.496× (z -8.8, q 8e-16, down in 22 of 32 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CECR2]] (+0.62, fdr 1e-05), [[CDH23]] (+0.61, fdr 4e-05), [[ITGA7]] (+0.59, fdr 6e-05); moves opposite to [[THADA]] (-0.56, fdr 6e-05), [[CIAO1]] (-0.54, fdr 3e-05), [[WDR70]] (-0.52, fdr 3e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MSI1]] → it (grade B ⚠); 4 go from it, the strongest it → [[ADGRL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 803.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.10×** | +20.1 | 0e+00 | 18/32 (BT-474, A-172, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.86×** | +12.3 | 2e-32 | 3/6 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +10.9 | 2e-25 | 11/18 (HS-578T, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +10.6 | 5e-24 | 21/37 (PANC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +7.1 | 2e-10 | 6/11 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +7.0 | 2e-10 | 20/34 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +6.2 | 3e-08 | 13/30 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +6.1 | 6e-08 | 8/37 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.53×** | +5.4 | 5e-06 | 10/36 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +4.5 | 4e-04 | 6/32 (PANC-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.4 | 5e-04 | 13/34 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.012 | 11/36 (HCT15, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 803.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.496×** | -8.8 | 8e-16 | 22/32 (MIA PaCa-2, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.582×** | -6.8 | 3e-09 | 19/37 (NCI-H23, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.609×** | -6.2 | 1e-07 | 15/37 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.622×** | -6.0 | 4e-07 | 15/37 (MIA PaCa-2, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.636×** | -5.7 | 2e-06 | 18/36 (MIA PaCa-2, NCI-H1573, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.729×** | -5.6 | 2e-06 | 18/31 (LoVo, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.686×** | -4.7 | 2e-04 | 12/36 (NCI-H2030, A549, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.693×** | -4.6 | 3e-04 | 11/37 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.704×** | -4.4 | 7e-04 | 15/36 (HCT15, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.718×** | -4.2 | 0.002 | 9/36 (NCI-H1573, MIA PaCa-2, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.731×** | -3.9 | 0.005 | 7/37 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.716×** | -3.9 | 0.005 | 14/30 (NCI-H1573, HOP62, …) | all doses, flat | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | **0.742×** | -3.5 | 0.021 | 5/36 (MIA PaCa-2, C-33 A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.749×** | -3.4 | 0.028 | 13/36 (MIA PaCa-2, RKO, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.764×** | -3.4 | 0.028 | 11/37 (MIA PaCa-2, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.771×** | -3.1 | 0.074 | 9/32 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 803. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -10.9) |
| [[A-172 (line)]] | wt | 4.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +12.2) | — |
| [[BT-474 (line)]] | alt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.96× (z +12.4) | — |
| [[HOP62 (line)]] | alt | 4.12 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 9.12× (z +8.6) | — |
| [[LoVo (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -12.6) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.4) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H23 (line)]] | alt | 9.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 4.09 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0552× (z -9.2) |
| [[PANC-1 (line)]] | alt | 2.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.94× (z +8.7) | — |
| [[SW480 (line)]] | alt | 2.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.65× (z +9.8) | — |
| [[A-427 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.961 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.883 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.982 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 803), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CECR2]] | +0.62 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[CDH23]] | +0.61 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[ITGA7]] | +0.59 | +0.39 / +0.70 | both halves | 6e-05 |  |
| [[TMEM266]] | +0.58 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[RHBDL3]] | +0.57 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[SYNGR1]] | +0.56 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[SEMA6B]] | +0.56 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[SPTBN4]] | +0.56 | +0.36 / +0.66 | both halves | 9e-05 |  |
| [[CRLF1]] | +0.55 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[FRMPD3]] | +0.55 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[CHMP3-AS1]] | +0.54 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[CIB2]] | +0.53 | +0.45 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THADA]] | -0.56 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[CIAO1]] | -0.54 | -0.44 / -0.50 | both halves | 3e-05 | same gene group |
| [[WDR70]] | -0.52 | -0.46 / -0.49 | both halves | 3e-05 | same gene group |
| [[PRMT5]] | -0.51 | -0.36 / -0.58 | both halves | 9e-05 |  |
| [[EEFSEC]] | -0.48 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[SRRD]] | -0.48 | -0.32 / -0.47 | both halves | 1e-04 |  |
| [[PWP1]] | -0.46 | -0.36 / -0.49 | both halves | 9e-05 | same gene group |
| [[PTCD2]] | -0.46 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[ZNF22]] | -0.45 | -0.37 / -0.43 | both halves | 7e-05 |  |
| [[NOL11]] | -0.45 | -0.29 / -0.56 | both halves | 2e-04 |  |
| [[FASTKD2]] | -0.45 | -0.28 / -0.60 | both halves | 3e-04 |  |
| [[FAN1]] | -0.45 | -0.32 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSI1]] | B | MSI1 activity raises TLE2's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.08× lower at baseline in the lines without MSI1 | 0.011 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[FAM184A]] | B | FAM184A activity raises TLE2's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 1.65× lower at baseline in the lines without FAM184A | 0.055 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers TLE2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PTK7]] | B | PTK7 activity raises TLE2's level | lines that do not express PTK7 (9) vs lines expressing it (41) | 2.00× lower at baseline in the lines without PTK7 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000289985, ZNF433, ENSG00000269755 |
| [[KREMEN2]] | B | KREMEN2 activity raises TLE2's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.43× lower at baseline in the lines without KREMEN2 | 0.073 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[RHBDL3]] | B | RHBDL3 activity raises TLE2's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 2.04× lower at baseline in the lines without RHBDL3 | 0.074 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRL1]] | B | TLE2 activity raises ADGRL1's level | lines that do not express TLE2 (10) vs lines expressing it (40) | 3.00× lower at baseline in the lines without TLE2 | 0.037 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SEMA6B]] | B | TLE2 activity raises SEMA6B's level | lines that do not express TLE2 (10) vs lines expressing it (40) | 2.29× lower at baseline in the lines without TLE2 | 0.044 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MAST1]] | B | TLE2 activity raises MAST1's level | lines that do not express TLE2 (10) vs lines expressing it (40) | 2.10× lower at baseline in the lines without TLE2 | 0.067 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TMCC2]] | B | TLE2 activity raises TMCC2's level | lines that do not express TLE2 (10) vs lines expressing it (40) | 1.68× lower at baseline in the lines without TLE2 | 0.096 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.656). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.1, 34.1); signed map (27.3, 21.6). **Vector** length 57.5, 9.44% of its response variance represented; |z| ≥ 3 in 783 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +20.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +10.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.5 | +6.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +0.8 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.3 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -8.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -3.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | TLE family member 2, transcriptional corepressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,997,639-3,047,635 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ESG2, GRG2, ESG, FLJ41188 |
| Gene groups (HGNC) | WD repeat domain containing; Wnt enhanceosome complex; TLE family |
| Reactome | 9 pathways, smallest: Repression of WNT target genes; Deactivation of the beta-catenin transactivating complex; NOTCH1 Intracellular Domain Regulates Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04725](https://www.uniprot.org/uniprotkb/Q04725) (Transducin-like enhancer protein 2):

> Transcriptional corepressor that binds to a number of transcription factors. Inhibits the transcriptional activation mediated by CTNNB1 and TCF family members in Wnt signaling. The effects of full-length TLE family members may be modulated by association with dominant-negative AES (By similarity).

**Summary**, from NCBI Gene [7089](https://www.ncbi.nlm.nih.gov/gene/7089):

> Enables transcription corepressor activity. Involved in negative regulation of DNA-templated transcription and negative regulation of canonical Wnt signaling pathway. Located in nuclear body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11838](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11838) · Entrez [7089](https://www.ncbi.nlm.nih.gov/gene/7089) · UniProt [Q04725](https://www.uniprot.org/uniprotkb/Q04725) · Ensembl [ENSG00000065717](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065717)

## Data

Gene col 803: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 803); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 803, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 803]; `tensor/DDL_lfc|DDL_z.npy` [803]; `embed/gene_vectors.npy` [803]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 803 or target_col == 803). Every well: [[TLE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
