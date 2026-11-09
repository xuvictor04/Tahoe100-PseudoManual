---
symbol: "NEDD9"
type: "gene"
col: 3294
ensembl_id: "ENSG00000111859"
name: "neural precursor cell expressed, developmentally down-regulated 9"
location: "6p24.2"
module: 123
arm: "+"
pooled_cpm: 67.17
n_lines_expressing: 34
n_dd_up: 19
n_dd_down: 15
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 18
direction_downstream: 33
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# NEDD9

*neural precursor cell expressed, developmentally down-regulated 9* — 6p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.30× (z +15.5, q 0e+00, up in 29 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.506× (z -12.5, q 8e-33, down in 26 of 33 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTGER4]] (+0.74, fdr 7e-06), [[ADRB2]] (+0.66, fdr 7e-06), [[LMCD1]] (+0.65, fdr 1e-05); moves opposite to [[STX16-NPEPL1]] (-0.57, fdr 3e-05), [[DVL3]] (-0.55, fdr 3e-05), [[LY6G5B]] (-0.55, fdr 3e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[ELF3]] → it (grade B ⚠); 33 go from it, the strongest it → [[PLD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3294.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.30×** | +15.5 | 0e+00 | 29/32 (SNU-423, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.23×** | +14.7 | 0e+00 | 23/32 (hTERT-HPNE, A498, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.02×** | +12.9 | 5e-36 | 31/32 (SNU-423, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.47×** | +11.7 | 2e-29 | 27/32 (SNU-423, SW1417, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.44×** | +10.1 | 1e-21 | 27/32 (SW1417, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.90×** | +8.0 | 9e-14 | 20/32 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.94×** | +7.3 | 2e-11 | 26/33 (LoVo, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +7.2 | 4e-11 | 25/33 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +6.2 | 3e-08 | 23/32 (SW1417, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +5.6 | 2e-06 | 19/32 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.002 | 19/33 (Hs 766T, HS-578T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.35×** | +3.9 | 0.004 | 15/32 (BT-474, KATO III, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.76×** | +3.8 | 0.006 | 18/33 (SNU-423, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.33×** | +3.7 | 0.009 | 14/32 (NCI-H2347, KATO III, …) | inconsistent across doses | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +3.6 | 0.012 | 15/32 (BT-474, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.023 | 14/33 (HOP62, LS 180, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.041 | 11/32 (A549, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3294.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.506×** | -12.5 | 8e-33 | 26/33 (HepG2/C3A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.370×** | -12.4 | 1e-32 | 22/27 (A-172, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.405×** | -11.7 | 3e-29 | 25/32 (HepG2/C3A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.496×** | -9.1 | 2e-17 | 26/32 (SW480, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.502×** | -8.2 | 2e-14 | 26/29 (HepG2/C3A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -6.4 | 2e-08 | 22/31 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.691×** | -4.5 | 5e-04 | 19/32 (A549, HepG2/C3A, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.718×** | -4.3 | 0.001 | 17/32 (LoVo, A549, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.732×** | -3.8 | 0.009 | 17/32 (LoVo, COLO 205, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.758×** | -3.6 | 0.021 | 16/31 (LoVo, C32, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.601×** | -3.4 | 0.031 | 16/32 (NCI-H2030, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.609×** | -3.3 | 0.039 | 13/32 (BT-474, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.775×** | -3.2 | 0.069 | 16/31 (COLO 205, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.783×** | -3.1 | 0.069 | 16/31 (HT-29, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.846× | -3.0 | 0.088 | 10/33 (NCI-H2030, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.763×** | -3.0 | 0.088 | 15/32 (HepG2/C3A, SW480, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3294. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 117 | 3 | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.80× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.155× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 100.0 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -20.3) |
| [[A-172 (line)]] | wt | 47.1 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.0501× (z -21.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 95.8 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 556 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -25.3) |
| [[Hs 766T (line)]] | wt | 118 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -15.3) |
| [[KATO III (line)]] | alt | 316 | 2 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.73× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.148× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -12.6) |
| [[SW1417 (line)]] | alt | 34.0 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 6.17× (z +12.6) | — |
| [[SW480 (line)]] | alt | 56.5 | 0 | 6 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.253× (z -12.4) |
| [[BT-474 (line)]] | alt | 124 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -10.3) |
| [[HOP62 (line)]] | alt | 21.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.10× (z +13.8) | — |
| [[J82 (line)]] | alt | 62.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -10.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 74.1 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.7× (z +10.9) | [[Auranofin (drug)]] 5 µM 0.291× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 71.9 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.60× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -15.2) |
| [[NCI-H2347 (line)]] | alt | 62.8 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +11.4) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -9.0) |
| [[COLO 205 (line)]] | alt | 245 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0919× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -13.0) |
| [[A498 (line)]] | wt | 50.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -10.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 46.6 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +10.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -10.3) |
| [[LS 180 (line)]] | wt | 136 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -17.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 153 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -19.1) |
| [[HS-578T (line)]] | alt | 28.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +11.4) | — |
| [[hTERT-HPNE (line)]] | wt | 22.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +15.3) | — |
| [[CHP-212 (line)]] | wt | 36.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0867× (z -9.1) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 44.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -9.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 126 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 22.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.34× (z +10.3) | — |
| [[NCI-H596 (line)]] | alt | 63.9 | 0 | 1 | — | [[Oxaprozin (drug)]] 5 µM 0.206× (z -14.5) |
| [[Panc 03.27 (line)]] | alt | 165 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 46.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.76× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 48.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -9.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 4.55 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.06 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.22 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.92 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 8.85 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.65 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.63 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.31 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.81 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.74 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3294), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTGER4]] | +0.74 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[ADRB2]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[LMCD1]] | +0.65 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[KLF4]] | +0.63 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[MYLIP]] | +0.61 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[FRMD4B]] | +0.61 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[STARD5]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ARL4A]] | +0.58 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[TIPARP]] | +0.58 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[AHR]] | +0.58 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[TNFAIP3]] | +0.57 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[SGK1]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX16-NPEPL1]] | -0.57 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[DVL3]] | -0.55 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[LY6G5B]] | -0.55 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[GTF3C2-AS2]] | -0.54 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[ANXA2R-OT1]] | -0.53 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[FUBP3]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[ERVK13-1]] | -0.52 | -0.32 / -0.50 | both halves | 1e-04 |  |
| [[DCTN5]] | -0.52 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[CTC-338M12.4]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[PTPN9]] | -0.51 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[PEX6]] | -0.51 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[NDOR1]] | -0.51 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 15, C 3. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3]] | B | ELF3 activity raises NEDD9's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 3.30× lower at baseline in the lines without ELF3 | 0.003 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[KLF5]] | B | KLF5 activity raises NEDD9's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 2.79× lower at baseline in the lines without KLF5 | 0.005 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[CCL20]] | B | CCL20 activity raises NEDD9's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 3.40× lower at baseline in the lines without CCL20 | 0.007 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[ATP1B1]] | B | ATP1B1 activity raises NEDD9's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 4.91× lower at baseline in the lines without ATP1B1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[KLF4]] | B | KLF4 activity raises NEDD9's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 4.39× lower at baseline in the lines without KLF4 | 0.027 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |
| [[PLD1]] | B | PLD1 activity raises NEDD9's level | lines that do not express PLD1 (7) vs lines expressing it (43) | 4.64× lower at baseline in the lines without PLD1 | 0.038 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |
| [[RNF144B]] | B | RNF144B activity raises NEDD9's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 3.16× lower at baseline in the lines without RNF144B | 0.048 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |
| [[EFNA1]] | B | EFNA1 activity raises NEDD9's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 3.02× lower at baseline in the lines without EFNA1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[TLE4]] | B | TLE4 activity raises NEDD9's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 3.45× lower at baseline in the lines without TLE4 | 0.056 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |
| [[GATA6]] | B | GATA6 activity raises NEDD9's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 3.04× lower at baseline in the lines without GATA6 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[TRIB1]] | B | TRIB1 activity raises NEDD9's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 4.67× lower at baseline in the lines without TRIB1 | 0.064 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[BIK]] | B | BIK activity raises NEDD9's level | lines that do not express BIK (15) vs lines expressing it (35) | 2.36× lower at baseline in the lines without BIK | 0.064 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 30, C 3. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLD1]] | B | NEDD9 activity raises PLD1's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 2.45× lower at baseline in the lines without NEDD9 | 0.007 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[ATP1B1]] | B | NEDD9 activity raises ATP1B1's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 2.65× lower at baseline in the lines without NEDD9 | 0.008 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[EPS8]] | B | NEDD9 activity raises EPS8's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 2.43× lower at baseline in the lines without NEDD9 | 0.009 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[ARL4D]] | B | NEDD9 activity raises ARL4D's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 2.10× lower at baseline in the lines without NEDD9 | 0.010 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[TNFAIP3]] | B | NEDD9 activity raises TNFAIP3's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 2.12× lower at baseline in the lines without NEDD9 | 0.020 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[UGCG]] | B | NEDD9 activity raises UGCG's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 1.71× lower at baseline in the lines without NEDD9 | 0.033 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[KCTD15]] | B | NEDD9 activity lowers KCTD15's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 1.92× higher at baseline in the lines without NEDD9 | 0.037 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[PAG1]] | B | NEDD9 activity raises PAG1's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 3.21× lower at baseline in the lines without NEDD9 | 0.040 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[GATA6]] | B | NEDD9 activity raises GATA6's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 2.50× lower at baseline in the lines without NEDD9 | 0.044 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[KLF4]] | B | NEDD9 activity raises KLF4's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 1.96× lower at baseline in the lines without NEDD9 | 0.046 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[BTG1]] | B | NEDD9 activity raises BTG1's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 1.62× lower at baseline in the lines without NEDD9 | 0.049 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[SENP3]] | B | NEDD9 activity lowers SENP3's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 1.33× higher at baseline in the lines without NEDD9 | 0.055 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.0, 8.4); signed map (1.7, 23.6). **Vector** length 121, 36.6% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.50 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.0 | +12.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +7.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +15.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +14.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.4 | +4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +2.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.5 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +1.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.3 | -9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -12.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -6.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -1.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.7 | -3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | neural precursor cell expressed, developmentally down-regulated 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.2 — chr6:11,183,298-11,382,348 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HEF1, CAS-L, CASS2 |
| Gene groups (HGNC) | Cas scaffold protein family; SH3 domain containing |
| Hallmark sets | APOPTOSIS, MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14511](https://www.uniprot.org/uniprotkb/Q14511) (Enhancer of filamentation 1):

> Scaffolding protein which plays a central coordinating role for tyrosine-kinase-based signaling related to cell adhesion. As a focal adhesion protein, plays a role in embryonic fibroblast migration (By similarity). May play an important role in integrin beta-1 or B cell antigen receptor (BCR) mediated signaling in B- and T-cells. Integrin beta-1 stimulation leads to recruitment of various proteins including CRKL and SHPTP2 to the tyrosine phosphorylated form. Promotes adhesion and migration of …

**Summary**, from NCBI Gene [4739](https://www.ncbi.nlm.nih.gov/gene/4739):

> The protein encoded by this gene is a member of the CRK-associated substrates family. Members of this family are adhesion docking molecules that mediate protein-protein interactions for signal transduction pathways. This protein is a focal adhesion protein that acts as a scaffold to regulate signaling complexes important in cell attachment, migration and invasion as well as apoptosis and the cell cycle. This protein has also been reported to have a role in cancer metastasis. Alternative …

**Accessions** — [HGNC:7733](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7733) · Entrez [4739](https://www.ncbi.nlm.nih.gov/gene/4739) · UniProt [Q14511](https://www.uniprot.org/uniprotkb/Q14511) · Ensembl [ENSG00000111859](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111859)

## Data

Gene col 3294: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3294); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3294, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3294]; `tensor/DDL_lfc|DDL_z.npy` [3294]; `embed/gene_vectors.npy` [3294]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3294 or target_col == 3294). Every well: [[NEDD9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEDD9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
