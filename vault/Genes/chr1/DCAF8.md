---
symbol: "DCAF8"
type: "gene"
col: 5363
ensembl_id: "ENSG00000132716"
name: "DDB1 and CUL4 associated factor 8"
location: "1q23.2"
module: 77
arm: "-"
pooled_cpm: 99.93
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 18
n_dd_up_clean: 6
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# DCAF8

*DDB1 and CUL4 associated factor 8* — 1q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.06× (z +24.7, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.456× (z -19.1, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIA1]] (+0.72, fdr 7e-06), [[MEPCE]] (+0.70, fdr 1e-05), [[AKT1S1]] (+0.70, fdr 4e-05); moves opposite to [[LPCAT4]] (-0.71, fdr 7e-06), [[GRB2]] (-0.70, fdr 7e-06), [[SPTLC2]] (-0.68, fdr 2e-05).
> It sits in the **-** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DDX43]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5363.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.06×** | +24.7 | 0e+00 | 44/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.92×** | +15.2 | 0e+00 | 41/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +11.8 | 1e-29 | 4/50 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +9.6 | 1e-19 | 36/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +7.9 | 3e-13 | 32/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.24×** | +5.1 | 3e-05 | 25/48 (NCI-H460, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +4.8 | 2e-04 | 25/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +3.8 | 0.010 | 22/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.7 | 0.012 | 15/47 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[crizotinib (drug)]] 5 µM |  | 1.16× | +3.5 | 0.022 | 13/48 (HOP62, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.022 | 20/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5363.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.456×** | -19.1 | 0e+00 | 48/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.479×** | -17.9 | 0e+00 | 47/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.506×** | -16.5 | 0e+00 | 47/48 (NCI-H2030, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.691×** | -9.0 | 3e-17 | 37/48 (NCI-H1792, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.703×** | -8.6 | 1e-15 | 39/48 (SW 900, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.731×** | -7.6 | 2e-12 | 36/48 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.805×** | -7.5 | 6e-12 | 26/49 (A549, NCI-H460, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.613×** | -6.2 | 4e-08 | 35/49 (NCI-H23, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.665×** | -5.2 | 1e-05 | 27/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.801×** | -5.2 | 1e-05 | 29/48 (AN3 CA, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.868× | -4.9 | 5e-05 | 18/48 (LOX-IMVI, NCI-H23, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.823×** | -4.6 | 2e-04 | 25/50 (C-33 A, NCI-H23, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.836× | -4.4 | 5e-04 | 21/49 (hTERT-HPNE, AsPC-1, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.716×** | -4.3 | 9e-04 | 22/48 (A498, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.891× | -4.0 | 0.002 | 10/48 (RKO, NCI-H2030, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.749×** | -3.7 | 0.007 | 19/48 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.865× | -3.5 | 0.012 | 21/48 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.760×** | -3.5 | 0.014 | 18/48 (RKO, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.814×** | -3.3 | 0.023 | 12/49 (A498, SW 1271, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.817×** | -3.3 | 0.024 | 15/48 (A498, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5363. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 133 | 8 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +24.2) | [[Panobinostat (drug)]] 0.5 µM 0.382× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 105 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -13.4) |
| [[LoVo (line)]] | wt | 84.1 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +17.4) | [[Panobinostat (drug)]] 0.5 µM 0.440× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 126 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +19.8) | [[Panobinostat (drug)]] 5 µM 0.373× (z -14.1) |
| [[NCI-H23 (line)]] | alt | 250 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.482× (z -10.5) |
| [[A498 (line)]] | wt | 104 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +16.7) | [[Belinostat (drug)]] 5 µM 0.503× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 122 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +15.2) | [[Panobinostat (drug)]] 0.5 µM 0.393× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 207 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +18.1) | [[Belinostat (drug)]] 5 µM 0.403× (z -12.9) |
| [[PANC-1 (line)]] | alt | 112 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +17.7) | [[Panobinostat (drug)]] 5 µM 0.415× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 109 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.417× (z -10.5) |
| [[A-172 (line)]] | wt | 114 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +18.9) | — |
| [[A549 (line)]] | wt | 83.2 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +19.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -10.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.469× (z -8.6) |
| [[KATO III (line)]] | alt | 76.3 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.363× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 90.9 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.389× (z -12.3) |
| [[Panc 03.27 (line)]] | alt | 83.2 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.427× (z -9.8) |
| [[RKO (line)]] | wt | 132 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.391× (z -10.9) |
| [[SW 900 (line)]] | alt | 110 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +13.4) | [[Belinostat (drug)]] 5 µM 0.400× (z -10.7) |
| [[SW480 (line)]] | alt | 87.6 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.427× (z -12.4) |
| [[C-33 A (line)]] | alt | 122 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.386× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.429× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 84.8 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.278× (z -11.8) |
| [[HOP62 (line)]] | alt | 65.3 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +15.3) | [[Panobinostat (drug)]] 0.5 µM 0.446× (z -9.5) |
| [[Hs 766T (line)]] | wt | 89.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +14.1) | — |
| [[RPMI-7951 (line)]] | alt | 81.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +14.7) | [[Panobinostat (drug)]] 5 µM 0.433× (z -8.6) |
| [[SW1417 (line)]] | alt | 83.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.441× (z -10.8) |
| [[A-427 (line)]] | wt | 144 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.488× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.518× (z -8.8) |
| [[C32 (line)]] | wt | 203 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.8) | [[Ponatinib (drug)]] 5 µM 0.458× (z -11.1) |
| [[COLO 205 (line)]] | alt | 103 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.446× (z -8.7) |
| [[HT-29 (line)]] | alt | 85.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +17.3) | [[Panobinostat (drug)]] 5 µM 0.433× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 60.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +16.7) | — |
| [[SNU-1 (line)]] | wt | 118 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 81.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.4) | [[Panobinostat (drug)]] 0.5 µM 0.407× (z -10.3) |
| [[BT-474 (line)]] | alt | 64.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.6) | — |
| [[CFPAC-1 (line)]] | alt | 55.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.8) | — |
| [[CHP-212 (line)]] | wt | 130 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -9.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[H4 (line)]] | wt | 79.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 68.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 49.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +16.3) | — |
| [[hTERT-HPNE (line)]] | wt | 77.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.7) | — |
| [[J82 (line)]] | alt | 64.8 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.486× (z -8.6) ⚠ cell-cycle shift, explains ~44% of this change |
| [[LS 180 (line)]] | wt | 64.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.6) | — |
| [[SW48 (line)]] | wt | 84.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +10.8) | — |
| [[AN3 CA (line)]] | alt | 101 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 94.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5363), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIA1]] | +0.72 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[MEPCE]] | +0.70 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[AKT1S1]] | +0.70 | +0.72 / +0.41 | both halves | 4e-05 |  |
| [[PMF1]] | +0.70 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MED12]] | +0.70 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[SRRM2]] | +0.69 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[FKRP]] | +0.69 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[BAZ2B]] | +0.69 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[ZNF764]] | +0.69 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[NEK9]] | +0.67 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[ZC3H11A]] | +0.67 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[ST7L]] | +0.67 | +0.62 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPCAT4]] | -0.71 | -0.67 / -0.61 | both halves | 7e-06 |  |
| [[GRB2]] | -0.70 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[SPTLC2]] | -0.68 | -0.67 / -0.48 | both halves | 2e-05 |  |
| [[ANKRD27]] | -0.67 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[MPZL1]] | -0.67 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[SEC11A]] | -0.66 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[TMEM120B]] | -0.66 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[RNF4]] | -0.66 | -0.67 / -0.58 | both halves | 8e-06 |  |
| [[TAF5L]] | -0.65 | -0.60 / -0.49 | both halves | 1e-05 | same gene group |
| [[PDCD10]] | -0.65 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[MFSD14CP]] | -0.65 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[SLC15A4]] | -0.64 | -0.61 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDX43]] | B | DDX43 activity lowers DCAF8's level | lines that do not express DDX43 (34) vs lines expressing it (16) | 1.20× higher at baseline in the lines without DDX43 | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC34A2, LINC02377, RNF17 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **-** arm (projection on the module's main direction -0.763). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-8.9, 4.6); signed map (16.3, -23.1). **Vector** length 120, 35.7% of its response variance represented; |z| ≥ 3 in 1,084 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.1 | +24.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.3 | +15.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.7 | +9.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | -0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +0.3 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.5 | +1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -7.7 | -16.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.3 | -19.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.1 | -8.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.9 | -17.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.1 | -9.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.1 | -5.2 |
|  | [[EX229 (drug)]] 5 µM |  | -3.8 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -6.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | DDB1 and CUL4 associated factor 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.2 — chr1:160,215,715-160,262,549 (-) |
| Ensembl biotype | protein_coding |
| Also known as | H326, FLJ35857; previously WDR42A |
| Gene groups (HGNC) | WD repeat domain containing; DDB1 and CUL4 associated factors |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TAQ9](https://www.uniprot.org/uniprotkb/Q5TAQ9) (DDB1- and CUL4-associated factor 8):

> May function as a substrate receptor for CUL4-DDB1 E3 ubiquitin-protein ligase complex.

**Summary**, from NCBI Gene [50717](https://www.ncbi.nlm.nih.gov/gene/50717):

> This gene encodes a WD repeat-containing protein that interacts with the Cul4-Ddb1 E3 ligase macromolecular complex. Multiple alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jul 2009]

**Accessions** — [HGNC:24891](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24891) · Entrez [50717](https://www.ncbi.nlm.nih.gov/gene/50717) · UniProt [Q5TAQ9](https://www.uniprot.org/uniprotkb/Q5TAQ9) · Ensembl [ENSG00000132716](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132716)

## Data

Gene col 5363: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5363); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5363, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5363]; `tensor/DDL_lfc|DDL_z.npy` [5363]; `embed/gene_vectors.npy` [5363]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5363 or target_col == 5363). Every well: [[DCAF8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCAF8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
