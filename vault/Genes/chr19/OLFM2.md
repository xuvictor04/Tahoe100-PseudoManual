---
symbol: "OLFM2"
type: "gene"
col: 2547
ensembl_id: "ENSG00000105088"
name: "olfactomedin 2"
location: "19p13.2"
module: 61
arm: "+"
pooled_cpm: 12.29
n_lines_expressing: 36
n_dd_up: 31
n_dd_down: 9
n_dd_up_clean: 22
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# OLFM2

*olfactomedin 2* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.57× (z +37.9, q 0e+00, up in 24 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.738× (z -4.7, q 0.001, down in 10 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB46]] (+0.66, fdr 7e-06), [[OSBP2]] (+0.66, fdr 7e-06), [[WIPF3]] (+0.63, fdr 1e-05); moves opposite to [[ZDHHC7]] (-0.55, fdr 1e-05), [[TIMM21]] (-0.54, fdr 2e-05), [[PMS2]] (-0.53, fdr 6e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MED12L]] → it (grade B ⚠); 2 go from it, the strongest it → [[MED12L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2547.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.57×** | +37.9 | 0e+00 | 24/32 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **6.02×** | +26.9 | 0e+00 | 26/34 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.66×** | +21.6 | 0e+00 | 30/33 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **3.17×** | +18.0 | 0e+00 | 30/34 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.82×** | +16.2 | 0e+00 | 28/34 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.29×** | +12.9 | 3e-36 | 28/34 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.91×** | +12.9 | 3e-36 | 26/32 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **2.21×** | +12.4 | 3e-33 | 20/33 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +10.8 | 3e-25 | 9/17 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +9.5 | 1e-19 | 17/32 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +8.4 | 2e-15 | 19/33 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +8.3 | 7e-15 | 10/33 (SK-MEL-2, A549, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +6.7 | 1e-09 | 14/33 (A-172, SHP-77, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.52×** | +6.6 | 2e-09 | 14/33 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +6.4 | 8e-09 | 7/27 (SHP-77, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.13×** | +5.7 | 4e-07 | 11/33 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +5.7 | 5e-07 | 17/32 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +5.2 | 5e-06 | 11/32 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2547.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.738×** | -4.7 | 0.001 | 10/33 (SW 1271, LOX-IMVI, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.748×** | -4.5 | 0.002 | 10/32 (C32, H4, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.758×** | -4.3 | 0.003 | 9/33 (SHP-77, SW 900, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.773×** | -4.0 | 0.008 | 10/34 (H4, SW 900, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.792×** | -3.6 | 0.032 | 11/33 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.799×** | -3.5 | 0.044 | 7/32 (H4, SW 1271, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.642×** | -3.3 | 0.062 | 11/28 (C32, SHP-77, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.801×** | -3.3 | 0.062 | 8/32 (C32, NCI-H460, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.812×** | -3.2 | 0.074 | 12/33 (C32, SNU-423, …) | inconsistent across doses |  |
| [[Bexarotene (drug)]] 0.5 µM |  | 0.822× | -3.1 | 0.12 | 2/34 (CHP-212, A-172) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2547. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.40 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +16.9) | — |
| [[BT-474 (line)]] | alt | 39.4 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +17.0) | — |
| [[PANC-1 (line)]] | alt | 16.8 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +30.3) | [[Selinexor (drug)]] 5 µM 0.464× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 94.9 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[C-33 A (line)]] | alt | 86.0 | 0 | 5 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.107× (z -18.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -17.0) |
| [[NCI-H23 (line)]] | alt | 51.0 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +16.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 29.8 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -11.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 10.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.96× (z +19.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 4.88 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.8× (z +18.8) | — |
| [[HOP62 (line)]] | alt | 3.61 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +12.9) | — |
| [[LoVo (line)]] | wt | 22.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -9.9) |
| [[SNU-423 (line)]] | alt | 3.66 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 41.3× (z +15.3) | — |
| [[A-172 (line)]] | wt | 5.84 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.7× (z +16.2) | — |
| [[A549 (line)]] | wt | 12.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +13.0) | — |
| [[AN3 CA (line)]] | alt | 34.1 | 0 | 2 | — | [[Ponatinib (drug)]] 5 µM 0.0653× (z -10.9) |
| [[C32 (line)]] | wt | 18.4 | 0 | 2 (1 ⚠) | — | [[Cobimetinib (drug)]] 0.05 µM 0.164× (z -9.1) |
| [[HS-578T (line)]] | alt | 4.37 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +12.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.12× (z +15.2) | — |
| [[NCI-H1573 (line)]] | alt | 12.9 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 23.9× (z +16.2) | — |
| [[NCI-H2030 (line)]] | alt | 24.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +15.4) | — |
| [[SW 900 (line)]] | alt | 11.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +14.9) | — |
| [[H4 (line)]] | wt | 15.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +14.4) | — |
| [[SHP-77 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +10.5) | — |
| [[SW480 (line)]] | alt | 3.13 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.52× (z +11.1) | — |
| [[A498 (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.20 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2547), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB46]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[OSBP2]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[WIPF3]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[C11orf96]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[SHF]] | +0.59 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[NHSL2]] | +0.57 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SLC35F1]] | +0.57 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[IL3RA]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[ATP6V0A1]] | +0.57 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[GNG4]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[TICAM1]] | +0.56 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[TMEM40]] | +0.56 | +0.46 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC7]] | -0.55 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[TIMM21]] | -0.54 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[PMS2]] | -0.53 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[NUP133]] | -0.50 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[GLE1]] | -0.50 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[TSN]] | -0.48 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[SAMM50]] | -0.47 | -0.44 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MED12L]] | B | MED12L activity raises OLFM2's level | lines that do not express MED12L (18) vs lines expressing it (32) | 3.28× lower at baseline in the lines without MED12L | 0.004 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |
| [[NR3C1]] | B | NR3C1 activity lowers OLFM2's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 1.7% of all compounds | 0.014 | ⚠ off-target possible; 3 compounds |
| [[NTN1]] | B | NTN1 activity raises OLFM2's level | lines that do not express NTN1 (17) vs lines expressing it (33) | 2.62× lower at baseline in the lines without NTN1 | 0.023 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent |
| [[KCNQ2]] | B | KCNQ2 activity raises OLFM2's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 2.46× lower at baseline in the lines without KCNQ2 | 0.041 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |
| [[RPLP0P2]] | B | RPLP0P2 activity lowers OLFM2's level | lines that do not express RPLP0P2 (7) vs lines expressing it (43) | 3.30× higher at baseline in the lines without RPLP0P2 | 0.063 | ⚠ within organs, on part of the lines; also absent: CAMK2N1, ETS2, CSTB; maybe low, not absent |
| [[RASGEF1C]] | B | RASGEF1C activity raises OLFM2's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 3.18× lower at baseline in the lines without RASGEF1C | 0.089 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MED12L]] | B | OLFM2 activity raises MED12L's level | lines that do not express OLFM2 (14) vs lines expressing it (36) | 3.20× lower at baseline in the lines without OLFM2 | 0.056 | ⚠ within organs, on part of the lines; also absent: MGAT5B, JAM3, ANKS1B; maybe low, not absent |
| [[RHBDL3]] | B | OLFM2 activity raises RHBDL3's level | lines that do not express OLFM2 (14) vs lines expressing it (36) | 1.93× lower at baseline in the lines without OLFM2 | 0.068 | ⚠ within organs, on part of the lines; also absent: MGAT5B, JAM3, ANKS1B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.0, 10.6); signed map (30.5, 24.0). **Vector** length 83.7, 19.2% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +21.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.8 | +12.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +37.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.6 | +26.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.0 | +6.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +5.7 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.1 | +0.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -1.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -2.0 | -0.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.0 | -4.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | olfactomedin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:9,853,718-9,936,515 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OlfC, NOE2 |
| Gene groups (HGNC) | Olfactomedin domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O95897](https://www.uniprot.org/uniprotkb/O95897) (Noelin-2):

> Involved in transforming growth factor beta (TGF-beta)-induced smooth muscle differentiation. TGF-beta induces expression and translocation of OLFM2 to the nucleus where it binds to SRF, causing its dissociation from the transcriptional repressor HEY2/HERP1 and facilitating binding of SRF to target genes. Plays a role in AMPAR complex organization (By similarity). Is a regulator of vascular smooth-muscle cell (SMC) phenotypic switching, that acts by promoting RUNX2 and inhibiting MYOCD binding …

**Summary**, from NCBI Gene [93145](https://www.ncbi.nlm.nih.gov/gene/93145):

> Involved in positive regulation of smooth muscle cell differentiation. Acts upstream of or within protein secretion. Located in cytoplasm; extracellular region; and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17189](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17189) · Entrez [93145](https://www.ncbi.nlm.nih.gov/gene/93145) · UniProt [O95897](https://www.uniprot.org/uniprotkb/O95897) · Ensembl [ENSG00000105088](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105088)

## Data

Gene col 2547: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2547); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2547, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2547]; `tensor/DDL_lfc|DDL_z.npy` [2547]; `embed/gene_vectors.npy` [2547]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2547 or target_col == 2547). Every well: [[OLFM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OLFM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
