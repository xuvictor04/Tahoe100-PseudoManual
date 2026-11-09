---
symbol: "SPTAN1"
type: "gene"
col: 12441
ensembl_id: "ENSG00000197694"
name: "spectrin alpha, non-erythrocytic 1"
location: "9q34.11"
module: 111
arm: "+"
pooled_cpm: 215.56
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# SPTAN1

*spectrin alpha, non-erythrocytic 1* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.49× (z +21.7, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.800× (z -5.3, q 6e-05, down in 33 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (HEC-1-A 0.540×, SNU-1 0.457×, LS 180 0.518×, SW480 0.630×, …); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.381×, SNU-1 0.401×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.362×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.619×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DYNC1H1]] (+0.66, fdr 1e-05), [[FLII]] (+0.63, fdr 7e-06), [[EZR]] (+0.61, fdr 2e-05); moves opposite to [[MIR762HG]] (-0.63, fdr 1e-05), [[SPATA5L1]] (-0.59, fdr 2e-05), [[RNF145]] (-0.59, fdr 1e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12441.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.49×** | +21.7 | 0e+00 | 44/48 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.34×** | +14.3 | 6e-44 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.10×** | +12.5 | 2e-33 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.00×** | +11.7 | 2e-29 | 46/48 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +9.5 | 2e-19 | 42/48 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +6.5 | 8e-09 | 38/48 (COLO 205, NCI-H460, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +6.4 | 1e-08 | 37/48 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +5.5 | 3e-06 | 29/49 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +5.3 | 6e-06 | 38/48 (NCI-H460, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +5.2 | 9e-06 | 37/48 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +5.0 | 3e-05 | 32/44 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +4.9 | 6e-05 | 34/48 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.72×** | +4.7 | 9e-05 | 39/48 (LOX-IMVI, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +4.6 | 2e-04 | 26/48 (A498, C-33 A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +4.3 | 5e-04 | 29/48 (COLO 205, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.005 | 34/48 (LoVo, SNU-1, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.005 | 29/49 (LOX-IMVI, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12441.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (HEC-1-A 0.540×, SNU-1 0.457×, LS 180 0.518×, SW480 0.630×, …); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.381×, SNU-1 0.401×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.362×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.619×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.800×** | -5.3 | 6e-05 | 33/49 (HEC-1-A, SNU-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.639×** | -3.9 | 0.023 | 32/49 (RKO, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.826× | -3.2 | 0.24 | 23/48 (Hs 766T, AsPC-1, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.833× | -3.1 | 0.31 | 19/49 (HEC-1-A, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12441. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 175 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +24.2) | — |
| [[NCI-H460 (line)]] | wt | 221 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +23.7) | — |
| [[COLO 205 (line)]] | alt | 218 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +20.5) | — |
| [[SW480 (line)]] | alt | 271 | 7 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +25.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.630× (z -10.2) |
| [[HOP62 (line)]] | alt | 201 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +25.3) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.619× (z -8.6) |
| [[PANC-1 (line)]] | alt | 138 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +13.6) | — |
| [[RKO (line)]] | wt | 395 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -12.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 345 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -12.2) |
| [[C-33 A (line)]] | alt | 211 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.61× (z +10.8) | — |
| [[J82 (line)]] | alt | 265 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +17.8) | — |
| [[LOX-IMVI (line)]] | wt | 162 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +25.4) | — |
| [[BT-474 (line)]] | alt | 339 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.26× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.4) | — |
| [[C32 (line)]] | wt | 107 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +22.1) | — |
| [[H4 (line)]] | wt | 122 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +13.7) | — |
| [[HEC-1-A (line)]] | alt | 398 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -12.3) |
| [[Hs 766T (line)]] | wt | 187 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.3) | — |
| [[hTERT-HPNE (line)]] | wt | 183 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +19.3) | — |
| [[LoVo (line)]] | wt | 199 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.1) | — |
| [[RPMI-7951 (line)]] | alt | 145 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +13.8) | — |
| [[SK-MEL-2 (line)]] | alt | 123 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +16.9) | — |
| [[A-172 (line)]] | wt | 409 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.36× (z +10.5) | — |
| [[A-427 (line)]] | wt | 138 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +16.8) | — |
| [[A549 (line)]] | wt | 211 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.52× (z +11.0) | — |
| [[AsPC-1 (line)]] | alt | 205 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +16.8) | — |
| [[HS-578T (line)]] | alt | 135 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.85× (z +10.9) | — |
| [[HT-29 (line)]] | alt | 229 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.7) | — |
| [[KATO III (line)]] | alt | 262 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.49× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 302 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 293 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +16.9) | — |
| [[NCI-H1792 (line)]] | alt | 100 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +20.5) | — |
| [[NCI-H2030 (line)]] | alt | 118 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +15.9) | — |
| [[Panc 03.27 (line)]] | alt | 241 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +14.1) | [[Lonafarnib (drug)]] 5 µM 0.190× (z -10.8) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 183 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +16.4) | — |
| [[CHP-212 (line)]] | wt | 159 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.65× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 365 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 102 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +19.5) | — |
| [[NCI-H23 (line)]] | alt | 161 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +17.5) | — |
| [[SNU-423 (line)]] | alt | 227 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 217 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -8.7) |
| [[AN3 CA (line)]] | alt | 228 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 176 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.28× (z +9.7) | — |
| [[SW 1271 (line)]] | alt | 379 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 174 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +14.7) | — |
| [[SW48 (line)]] | wt | 262 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +13.6) | — |
| [[HepG2_C3A (line)]] | wt | 183 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 176 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12441), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNC1H1]] | +0.66 | +0.49 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 562 |
| [[FLII]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_MYOGENESIS |
| [[EZR]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 655 |
| [[DSG2]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 | pathway: Apoptosis |
| [[UBA1]] | +0.60 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[IQGAP1]] | +0.59 | +0.39 / +0.54 | both halves | 5e-05 | pathway: Cell-Cell communication; STRING 753 |
| [[TFE3]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[HUWE1]] | +0.58 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[MYH9]] | +0.58 | +0.40 / +0.59 | both halves | 5e-05 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 848 |
| [[JUN]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS |
| [[YWHAH]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 | pathway: Apoptosis |
| [[FLNC]] | +0.57 | +0.45 / +0.53 | both halves | 3e-05 | pathway: Cell-Cell communication |

## Genes that move opposite

*51 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR762HG]] | -0.63 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[SPATA5L1]] | -0.59 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[RNF145]] | -0.59 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[SELENOH]] | -0.56 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[MFSD14CP]] | -0.56 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[NUP54]] | -0.56 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[PGS1]] | -0.55 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[DHRS7B]] | -0.55 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[NCBP2AS2]] | -0.54 | -0.38 / -0.58 | both halves | 7e-05 |  |
| [[PANK1]] | -0.54 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[CAPN10-DT]] | -0.54 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[SUZ12P1]] | -0.54 | -0.46 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.7, 8.7); signed map (-9.6, 32.8). **Vector** length 138, 47.7% of its response variance represented; |z| ≥ 3 in 1,172 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.8 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.5 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +21.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.1 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +2.9 |
|  | [[RMC-6236 (drug)]] 5 µM |  | +3.6 | +2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.3 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.9 | -5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.3 | -1.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -7.1 | -3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~4% of this change | -5.1 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.6 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.1 | -1.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.4 | -2.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | spectrin alpha, non-erythrocytic 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,552,558-128,633,662 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | EF-hand domain containing; Spectrins; SH3 domain containing |
| Hallmark sets | MYOGENESIS, APOPTOSIS, MITOTIC_SPINDLE |
| Reactome | 32 pathways, smallest: Caspase-mediated cleavage of cytoskeletal proteins; Nephrin family interactions; Interaction between L1 and Ankyrins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13813](https://www.uniprot.org/uniprotkb/Q13813) (Spectrin alpha chain, non-erythrocytic 1):

> Fodrin, which seems to be involved in secretion, interacts with calmodulin in a calcium-dependent manner and is thus candidate for the calcium-dependent movement of the cytoskeleton at the membrane.

**Summary**, from NCBI Gene [6709](https://www.ncbi.nlm.nih.gov/gene/6709):

> Spectrins are a family of filamentous cytoskeletal proteins that function as essential scaffold proteins that stabilize the plasma membrane and organize intracellular organelles. Spectrins are composed of alpha and beta dimers that associate to form tetramers linked in a head-to-head arrangement. This gene encodes an alpha spectrin that is specifically expressed in nonerythrocytic cells. The encoded protein has been implicated in other cellular functions including DNA repair and cell cycle …

**Accessions** — [HGNC:11273](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11273) · Entrez [6709](https://www.ncbi.nlm.nih.gov/gene/6709) · UniProt [Q13813](https://www.uniprot.org/uniprotkb/Q13813) · Ensembl [ENSG00000197694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197694)

## Data

Gene col 12441: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12441); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12441, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12441]; `tensor/DDL_lfc|DDL_z.npy` [12441]; `embed/gene_vectors.npy` [12441]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12441 or target_col == 12441). Every well: [[SPTAN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPTAN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
