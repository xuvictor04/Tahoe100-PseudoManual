---
symbol: "RIMOC1"
type: "gene"
col: 13010
ensembl_id: "ENSG00000205765"
name: "RAB7A interacting MON1-CCZ1 complex subunit 1"
location: "5p13.1"
module: 7
arm: "+"
pooled_cpm: 33.5
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 12
n_dd_up_clean: 19
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# RIMOC1

*RAB7A interacting MON1-CCZ1 complex subunit 1* — 5p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.26× (z +25.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.537× (z -9.8, q 7e-20, down in 33 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.645× (z -9.0, q 4e-17, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZXDB]] (+0.75, fdr 7e-06), [[BROX]] (+0.73, fdr 7e-06), [[ZXDA]] (+0.72, fdr 7e-06); moves opposite to [[TOMM5]] (-0.66, fdr 7e-06), [[FAM118A]] (-0.61, fdr 4e-05), [[SLC29A4]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13010.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.26×** | +25.0 | 0e+00 | 47/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.77×** | +15.4 | 0e+00 | 45/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.62×** | +13.7 | 3e-40 | 46/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.10×** | +11.7 | 3e-29 | 42/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +9.7 | 3e-20 | 41/48 (A-172, RKO, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +8.9 | 4e-17 | 42/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.55×** | +6.9 | 4e-10 | 35/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +6.6 | 3e-09 | 35/48 (PANC-1, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.95×** | +5.5 | 3e-06 | 28/48 (NCI-H1573, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +4.7 | 1e-04 | 24/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.6 | 2e-04 | 25/48 (NCI-H2030, J82, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +4.5 | 3e-04 | 21/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.3 | 7e-04 | 24/48 (A-427, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.35×** | +4.3 | 8e-04 | 22/48 (NCI-H460, A-427, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.35×** | +4.2 | 0.001 | 20/48 (A-427, PANC-1, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.001 | 21/48 (LoVo, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13010.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.537×** | -9.8 | 7e-20 | 33/47 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.645×** | -9.0 | 4e-17 | 44/48 (SW480, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.632×** | -7.2 | 8e-11 | 39/48 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.687×** | -5.9 | 5e-07 | 31/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.732×** | -4.9 | 9e-05 | 26/48 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.727×** | -4.5 | 5e-04 | 26/48 (CHP-212, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.673×** | -4.5 | 7e-04 | 23/48 (SW 1271, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.734×** | -3.5 | 0.035 | 20/48 (HepG2/C3A, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.739×** | -3.4 | 0.040 | 16/48 (Panc 03.27, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM |  | **0.793×** | -3.4 | 0.040 | 11/48 (BT-474, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.676×** | -3.2 | 0.063 | 15/43 (SHP-77, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.757×** | -3.1 | 0.081 | 14/48 (AsPC-1, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.826× | -3.0 | 0.11 | 17/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.827× | -3.0 | 0.11 | 15/47 (SNU-1, SW480, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13010. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 37.5 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.1) | [[Digitoxin (drug)]] 5 µM 0.235× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.308× (z -12.3) |
| [[A-427 (line)]] | wt | 50.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.70× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 31.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.84× (z +29.5) | — |
| [[PANC-1 (line)]] | alt | 28.1 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +18.7) | [[Digitoxin (drug)]] 5 µM 0.360× (z -10.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 39.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +20.9) | — |
| [[NCI-H1573 (line)]] | alt | 44.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +26.5) | — |
| [[NCI-H23 (line)]] | alt | 66.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +20.0) | — |
| [[NCI-H2347 (line)]] | alt | 32.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +17.7) | — |
| [[J82 (line)]] | alt | 51.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +17.9) | — |
| [[NCI-H2030 (line)]] | alt | 38.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +12.7) | — |
| [[SNU-423 (line)]] | alt | 46.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +18.4) | [[Digitoxin (drug)]] 5 µM 0.354× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 44.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +18.6) | — |
| [[AsPC-1 (line)]] | alt | 18.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +17.2) | — |
| [[C32 (line)]] | wt | 23.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +13.6) | — |
| [[COLO 205 (line)]] | alt | 26.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +11.4) | [[Digitoxin (drug)]] 5 µM 0.196× (z -9.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 23.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +9.6) | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0898× (z -10.5) |
| [[HCT15 (line)]] | alt | 37.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +11.0) | [[Digitoxin (drug)]] 5 µM 0.153× (z -12.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 23.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 50.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +17.4) | — |
| [[LoVo (line)]] | wt | 31.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +12.7) | [[Tucidinostat (drug)]] 5 µM 0.460× (z -9.0) |
| [[LS 180 (line)]] | wt | 25.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.322× (z -8.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 23.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +11.7) | — |
| [[BT-474 (line)]] | alt | 34.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +11.0) | — |
| [[C-33 A (line)]] | alt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 30.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +11.1) | — |
| [[HT-29 (line)]] | alt | 31.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.55× (z +15.2) | — |
| [[KATO III (line)]] | alt | 30.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 17.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +12.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 44.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +11.8) | — |
| [[RPMI-7951 (line)]] | alt | 32.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +12.0) | — |
| [[SHP-77 (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.233× (z -11.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 23.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 39.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +10.9) | — |
| [[SW1417 (line)]] | alt | 33.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +10.6) | — |
| [[SW48 (line)]] | wt | 24.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.131× (z -10.1) |
| [[AN3 CA (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13010), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDB]] | +0.75 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[BROX]] | +0.73 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[ZXDA]] | +0.72 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[ZNF252P]] | +0.71 | +0.77 / +0.58 | both halves | 7e-06 |  |
| [[DARS1]] | +0.71 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[ZNF252P-1]] | +0.70 | +0.77 / +0.57 | both halves | 1e-05 |  |
| [[RNF6]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[METTL6]] | +0.68 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[ARMT1]] | +0.68 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[GIN1]] | +0.68 | +0.75 / +0.44 | both halves | 3e-05 |  |
| [[TDP2]] | +0.67 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[TMEM184C]] | +0.67 | +0.78 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOMM5]] | -0.66 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[FAM118A]] | -0.61 | -0.68 / -0.41 | both halves | 4e-05 |  |
| [[SLC29A4]] | -0.61 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[PTMA]] | -0.60 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[SLC23A2]] | -0.60 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[UQCRH]] | -0.60 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[ATOX1]] | -0.59 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[COX6C]] | -0.59 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[UBE2G1]] | -0.59 | -0.67 / -0.49 | both halves | 1e-05 |  |
| [[UBL5]] | -0.58 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[CD81]] | -0.58 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[PTMAP2]] ⚠ | -0.58 | -0.65 / -0.44 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.571). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-19.8, 7.3); signed map (8.2, -28.4). **Vector** length 124, 35.4% of its response variance represented; |z| ≥ 3 in 1,133 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +10.5 | +11.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.5 | +13.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.3 | +15.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.9 | +25.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.6 | +6.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +4.1 | +4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +2.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.6 | -9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.7 | -4.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.5 | -9.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.5 | -0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.0 | -5.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -3.5 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.9 | -4.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.8 | -3.4 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -2.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | RAB7A interacting MON1-CCZ1 complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.1 — chr5:41,904,188-41,921,636 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LOC285636; previously C5orf51 |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NDU8](https://www.uniprot.org/uniprotkb/A6NDU8) (RAB7A-interacting MON1-CCZ1 complex subunit 1):

> Plays an important role in the removal of damaged mitochondria via mitophagy by controlling the stability and localization of RAB7A. Required for the recruitment of RAB7A and ATG9A vesicles to damaged mitochondria and promotes the stability of RAB7A by inhibiting its proteasomal degradation during mitophagy.

**Summary**, from NCBI Gene [285636](https://www.ncbi.nlm.nih.gov/gene/285636):

> Involved in mitophagy. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27750](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27750) · Entrez [285636](https://www.ncbi.nlm.nih.gov/gene/285636) · UniProt [A6NDU8](https://www.uniprot.org/uniprotkb/A6NDU8) · Ensembl [ENSG00000205765](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205765)

## Data

Gene col 13010: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13010); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13010, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13010]; `tensor/DDL_lfc|DDL_z.npy` [13010]; `embed/gene_vectors.npy` [13010]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13010 or target_col == 13010). Every well: [[RIMOC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIMOC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
