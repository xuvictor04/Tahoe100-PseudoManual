---
symbol: "TPTE2"
type: "gene"
col: 5396
ensembl_id: "ENSG00000132958"
name: "transmembrane phosphoinositide 3-phosphatase and tensin homolog 2"
location: "13q12.11"
module: 26
arm: "+"
pooled_cpm: 6.43
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 9
n_dd_up_clean: 28
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# TPTE2

*transmembrane phosphoinositide 3-phosphatase and tensin homolog 2* — 13q12.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 4.07× (z +18.9, q 0e+00, up in 42 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.483× (z -9.8, q 5e-20, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAALC-AS1]] (+0.75, fdr 7e-06), [[SLC26A7]] (+0.74, fdr 7e-06), [[LINC02641]] (+0.73, fdr 7e-06); moves opposite to [[TAF5L]] (-0.59, fdr 2e-05), [[POMGNT2]] (-0.58, fdr 4e-05), [[REPS1]] (-0.53, fdr 1e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[CASC20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5396.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **4.07×** | +18.9 | 0e+00 | 42/45 (HT-29, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.55×** | +17.8 | 0e+00 | 29/42 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.63×** | +17.4 | 0e+00 | 38/47 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +16.1 | 0e+00 | 34/41 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.03×** | +14.9 | 0e+00 | 35/41 (COLO 205, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.57×** | +12.7 | 6e-35 | 35/47 (SHP-77, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.55×** | +12.1 | 1e-31 | 30/40 (NCI-H460, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +11.6 | 4e-29 | 24/37 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +8.6 | 5e-16 | 20/43 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.89×** | +8.6 | 6e-16 | 27/47 (SHP-77, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +8.1 | 4e-14 | 21/48 (A-172, Hs 766T, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +7.8 | 4e-13 | 24/48 (PANC-1, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +7.5 | 3e-12 | 4/13 (RPMI-7951, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +7.2 | 2e-11 | 20/44 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +6.8 | 5e-10 | 13/34 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.64×** | +6.7 | 9e-10 | 19/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.59×** | +6.3 | 1e-08 | 16/45 (SHP-77, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +6.0 | 5e-08 | 17/48 (LoVo, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5396.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.483×** | -9.8 | 5e-20 | 25/47 (C32, LoVo, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.495×** | -9.2 | 2e-17 | 24/32 (NCI-H1573, C32, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.355×** | -7.3 | 5e-11 | 22/45 (NCI-H1573, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.610×** | -6.7 | 3e-09 | 22/42 (LoVo, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.789×** | -4.6 | 6e-04 | 12/48 (HEC-1-A, NCI-H1573, …) | top dose only |  |
| [[5-Fluorouracil (drug)]] 5 µM |  | **0.768×** | -3.6 | 0.031 | 6/47 (C32, HEC-1-A, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.614×** | -3.5 | 0.045 | 4/36 (LS 180, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **0.779×** | -3.4 | 0.049 | 3/45 (PANC-1, HOP62, …) | two highest doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.840× | -3.4 | 0.049 | 4/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[5-Fluorouracil (drug)]] 0.5 µM |  | **0.784×** | -3.3 | 0.054 | 11/46 (BT-474, SW48, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -3.0 | 0.14 | 9/48 (SK-MEL-2, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5396. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 11.2 | 3 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.96× (z +11.6) | [[Belinostat (drug)]] 0.5 µM 0.102× (z -12.2) |
| [[SHP-77 (line)]] | alt | 7.73 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 16.9× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 14.6× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 24.8 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.47× (z +10.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.135× (z -9.3) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 10.7 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 45.9× (z +13.8) | — |
| [[NCI-H1573 (line)]] | alt | 27.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0537× (z -17.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 6.57 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.31× (z +10.2) | — |
| [[A498 (line)]] | wt | 3.80 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.06× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 13.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +10.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.135× (z -10.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 5.35 | 1 | 1 | [[Auranofin (drug)]] 5 µM 11.6× (z +9.1) | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0837× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 4.64 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.83× (z +8.6) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.106× (z -9.4) |
| [[A-172 (line)]] | wt | 8.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +8.7) | — |
| [[C32 (line)]] | wt | 17.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0871× (z -11.0) ⚠ toxic |
| [[LS 180 (line)]] | wt | 5.52 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 14.5× (z +9.5) | — |
| [[A-427 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5396), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAALC-AS1]] | +0.75 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[SLC26A7]] | +0.74 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[LINC02641]] | +0.73 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[SNX31]] | +0.69 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[CCDC13]] | +0.67 | +0.69 / +0.43 | both halves | 4e-05 |  |
| [[COLQ]] | +0.67 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[C1QTNF7-AS1]] | +0.67 | +0.60 / +0.77 | both halves | 7e-06 |  |
| [[LVRN]] | +0.67 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[CXCL13]] | +0.67 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[CMYA5]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[MCF2]] | +0.65 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TBCE-1]] | +0.65 | +0.60 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF5L]] | -0.59 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[POMGNT2]] | -0.58 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[REPS1]] | -0.53 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[ABHD10]] | -0.53 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[BBS5]] | -0.53 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[THYN1]] | -0.53 | -0.56 / -0.20 | both halves | 7e-04 |  |
| [[SCAP]] | -0.53 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ARHGAP44]] | -0.51 | -0.49 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASC20]] | B | CASC20 activity raises TPTE2's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 1.95× lower at baseline in the lines without CASC20 | 0.029 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[LINC02641]] | B | LINC02641 activity raises TPTE2's level | lines that do not express LINC02641 (14) vs lines expressing it (36) | 1.81× lower at baseline in the lines without LINC02641 | 0.031 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent |
| [[IGSF11]] | B | IGSF11 activity raises TPTE2's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.64× lower at baseline in the lines without IGSF11 | 0.044 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[LINC01917]] | B | LINC01917 activity raises TPTE2's level | lines that do not express LINC01917 (19) vs lines expressing it (31) | 1.71× lower at baseline in the lines without LINC01917 | 0.054 | ⚠ within organs, on part of the lines; also absent: LINC00504, RMEL3, TEK; maybe low, not absent |
| [[LINC01482]] | B | LINC01482 activity raises TPTE2's level | lines that do not express LINC01482 (5) vs lines expressing it (45) | 2.31× lower at baseline in the lines without LINC01482 | 0.057 | ⚠ within organs, on part of the lines; also absent: MAP7D2, SLC35F4, ENSG00000226965; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers TPTE2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CORIN]] | B | CORIN activity raises TPTE2's level | lines that do not express CORIN (5) vs lines expressing it (45) | 2.08× lower at baseline in the lines without CORIN | 0.060 | ⚠ within organs, on part of the lines; also absent: TNNI3K, WDR49, ENSG00000229195; maybe low, not absent; its own permutation p |
| [[TMEM225B]] | B | TMEM225B activity raises TPTE2's level | lines that do not express TMEM225B (7) vs lines expressing it (43) | 1.75× lower at baseline in the lines without TMEM225B | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SRSF12 |
| [[RAPGEF4]] | B | RAPGEF4 activity raises TPTE2's level | lines that do not express RAPGEF4 (5) vs lines expressing it (45) | 1.80× lower at baseline in the lines without RAPGEF4 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000286739, BIVM, CLIP3; maybe low, not absent |
| [[ANKRD7]] | B | ANKRD7 activity raises TPTE2's level | lines that do not express ANKRD7 (11) vs lines expressing it (39) | 1.58× lower at baseline in the lines without ANKRD7 | 0.080 | ⚠ within organs, on part of the lines; also absent: PCDH15, LINC02398, ABCA12; maybe low, not absent |
| [[LINC01505]] | B | LINC01505 activity raises TPTE2's level | lines that do not express LINC01505 (5) vs lines expressing it (45) | 2.41× lower at baseline in the lines without LINC01505 | 0.087 | ⚠ within organs, on part of the lines; also absent: EID2, CENPP, ENSG00000223727; maybe low, not absent |
| [[WDR49]] | C | WDR49 activity raises TPTE2's level | lines that do not express WDR49 (3) vs lines expressing it (47) | 2.43× lower at baseline in the lines without WDR49 | 0.065 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FOXP1, ENSG00000286952, CORIN; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.655). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (13.7, 16.8); signed map (22.5, 1.1). **Vector** length 90.9, 18.4% of its response variance represented; |z| ≥ 3 in 1,214 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.0 | +18.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.0 | +12.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +11.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +14.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +12.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +6.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +5.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.1 | +3.9 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.0 | -6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.9 | -9.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.6 | -7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -1.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -1.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.8 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -4.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane phosphoinositide 3-phosphatase and tensin homolog 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.11 — chr13:19,422,876-19,561,625 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TPIP |
| Gene groups (HGNC) | C2 tensin-type domain containing; PTEN protein phosphatases |
| Reactome | 4 pathways, smallest: Synthesis of PIPs at the Golgi membrane; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6XPS3](https://www.uniprot.org/uniprotkb/Q6XPS3) (Phosphatidylinositol 3,4,5-trisphosphate 3-phosphatase TPTE2):

> Acts as a lipid phosphatase, removing the phosphate in the D3 position of the inositol ring from phosphatidylinositol 3,4,5-trisphosphate.; [Isoform 4]: Shows no phosphoinositide phosphatase activity.

**Summary**, from NCBI Gene [93492](https://www.ncbi.nlm.nih.gov/gene/93492):

> TPIP is a member of a large class of membrane-associated phosphatases with substrate specificity for the 3-position phosphate of inositol phospholipids.[supplied by OMIM, Jul 2002]

**Accessions** — [HGNC:17299](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17299) · Entrez [93492](https://www.ncbi.nlm.nih.gov/gene/93492) · UniProt [Q6XPS3](https://www.uniprot.org/uniprotkb/Q6XPS3) · Ensembl [ENSG00000132958](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132958)

## Data

Gene col 5396: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5396); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5396, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5396]; `tensor/DDL_lfc|DDL_z.npy` [5396]; `embed/gene_vectors.npy` [5396]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5396 or target_col == 5396). Every well: [[TPTE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPTE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
