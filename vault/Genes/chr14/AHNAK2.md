---
symbol: "AHNAK2"
type: "gene"
col: 11698
ensembl_id: "ENSG00000185567"
name: "AHNAK nucleoprotein 2"
location: "14q32.33"
module: 111
arm: "+"
pooled_cpm: 120.85
n_lines_expressing: 38
n_dd_up: 26
n_dd_down: 21
n_dd_up_clean: 18
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# AHNAK2

*AHNAK nucleoprotein 2* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.06× (z +8.6, q 5e-15, up in 20 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.362× (z -17.2, q 0e+00, down in 32 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIDINS220]] (+0.65, fdr 1e-05), [[PLEC]] (+0.56, fdr 2e-05), [[VAT1]] (+0.56, fdr 1e-05); moves opposite to [[TRAPPC13]] (-0.51, fdr 6e-05), [[LRR1]] (-0.49, fdr 4e-05), [[C2orf42]] (-0.49, fdr 7e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ELFN2]] → it (grade B ⚠); 4 go from it, the strongest it → [[ABTB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11698.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.06×** | +8.6 | 5e-15 | 20/36 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.82×** | +7.1 | 4e-10 | 21/36 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +6.4 | 2e-08 | 21/37 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +6.4 | 3e-08 | 21/34 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +5.4 | 8e-06 | 18/36 (A498, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.47×** | +4.6 | 4e-04 | 29/36 (HEC-1-A, NCI-H460, …) | two highest doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.48×** | +4.5 | 6e-04 | 22/36 (SW480, KATO III, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.30×** | +4.3 | 1e-03 | 23/36 (A-172, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.002 | 14/36 (LS 180, SW480, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.45×** | +4.2 | 0.002 | 23/36 (HEC-1-A, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.42×** | +4.0 | 0.004 | 19/35 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.81×** | +3.7 | 0.010 | 18/38 (NCI-H460, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.010 | 23/35 (SW480, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[4EGI-1 (drug)]] 5 µM |  | **1.77×** | +3.6 | 0.015 | 22/36 (SW480, NCI-H460, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +3.5 | 0.015 | 14/34 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD-8055 (drug)]] 5 µM |  | **1.69×** | +3.2 | 0.041 | 21/37 (NCI-H460, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.044 | 18/36 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.049 | 18/36 (NCI-H460, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.050 | 21/36 (NCI-H1792, A549, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.050 | 19/37 (Panc 03.27, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11698.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.362×** | -17.2 | 0e+00 | 32/36 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.503×** | -11.7 | 5e-29 | 29/37 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.417×** | -10.5 | 2e-23 | 33/36 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.446×** | -9.7 | 5e-20 | 27/36 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.454×** | -9.5 | 3e-19 | 33/36 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.455×** | -9.1 | 9e-18 | 28/36 (MIA PaCa-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.473×** | -9.0 | 2e-17 | 32/36 (SW 900, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.506×** | -8.2 | 2e-14 | 33/36 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.528×** | -7.7 | 1e-12 | 31/36 (NCI-H661, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.524×** | -7.3 | 1e-11 | 34/36 (A549, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.580×** | -6.5 | 3e-09 | 27/35 (SW 900, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.608×** | -5.8 | 4e-07 | 23/36 (PANC-1, CFPAC-1, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.620×** | -5.7 | 4e-07 | 30/36 (SW 900, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.633×** | -5.5 | 2e-06 | 23/36 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.670×** | -4.8 | 5e-05 | 26/36 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.513×** | -4.2 | 9e-04 | 24/37 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.547×** | -3.8 | 0.004 | 22/36 (NCI-H2347, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.711×** | -2.9 | 0.090 | 15/36 (MIA PaCa-2, NCI-H23, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11698. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 206 | 0 | 19 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0697× (z -19.5) |
| [[PANC-1 (line)]] | alt | 297 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -22.0) |
| [[Panc 03.27 (line)]] | alt | 144 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -18.6) |
| [[NCI-H23 (line)]] | alt | 105 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -17.0) |
| [[CFPAC-1 (line)]] | alt | 410 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -24.6) |
| [[SW 900 (line)]] | alt | 182 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -16.0) |
| [[A498 (line)]] | wt | 46.1 | 6 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.29× (z +12.4) | — |
| [[A549 (line)]] | wt | 278 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0878× (z -35.0) |
| [[HEC-1-A (line)]] | alt | 165 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -22.6) |
| [[LoVo (line)]] | wt | 107 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.230× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.260× (z -11.0) |
| [[SNU-423 (line)]] | alt | 108 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -16.4) |
| [[NCI-H1573 (line)]] | alt | 145 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -17.5) |
| [[LS 180 (line)]] | wt | 49.4 | 3 (2 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 2.83× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 103 | 2 (1 ⚠) | 2 | [[Panobinostat (drug)]] 0.5 µM 2.84× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -19.0) |
| [[A-427 (line)]] | wt | 43.9 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 4.06× (z +10.3) | [[Digitoxin (drug)]] 0.5 µM 0.274× (z -9.5) |
| [[KATO III (line)]] | alt | 163 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -16.0) |
| [[NCI-H2030 (line)]] | alt | 123 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 2.97× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -12.8) |
| [[NCI-H2347 (line)]] | alt | 206 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -17.8) |
| [[NCI-H460 (line)]] | wt | 82.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -14.0) |
| [[NCI-H661 (line)]] | alt | 71.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -12.1) |
| [[A-172 (line)]] | wt | 363 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 221 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -12.6) |
| [[Hs 766T (line)]] | wt | 198 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -11.3) |
| [[J82 (line)]] | alt | 37.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 77.2 | 1 (1 ⚠) | 1 | [[Selinexor (drug)]] 5 µM 2.38× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | [[Ixazomib citrate (drug)]] 5 µM 0.292× (z -8.5) |
| [[SW480 (line)]] | alt | 66.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.96× (z +8.7) | — |
| [[H4 (line)]] | wt | 59.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -10.0) |
| [[HCT15 (line)]] | alt | 47.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 45.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 187 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -11.4) |
| [[SW48 (line)]] | wt | 74.6 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.204× (z -8.6) ⚠ toxic; unreliable plate only |
| [[AN3 CA (line)]] | alt | 27.6 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 19.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.5 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 15.2 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 26.2 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.9 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.1 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 29.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 30.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 75.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11698), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIDINS220]] | +0.65 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[PLEC]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[VAT1]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[AHNAK]] | +0.55 | +0.55 / +0.64 | both halves | 1e-05 | same gene group; STRING 944 |
| [[CAST]] | +0.55 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[SNX15]] | +0.53 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[SPTAN1]] | +0.53 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[CDC42BPB]] | +0.53 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[EZR]] | +0.52 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[PPL]] | +0.51 | +0.39 / +0.45 | both halves | 5e-05 |  |
| [[IL17RD]] | +0.51 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[ANXA2]] | +0.50 | +0.44 / +0.47 | both halves | 3e-05 | STRING 971 |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC13]] | -0.51 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[LRR1]] | -0.49 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[C2orf42]] | -0.49 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[HSPA14]] | -0.49 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[MEIS2]] | -0.47 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[PLEKHS1]] | -0.45 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[DHRS7B]] | -0.45 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[LSM8]] | -0.44 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[LINC02068]] | -0.44 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[PDSS2]] | -0.44 | -0.32 / -0.44 | both halves | 1e-04 |  |
| [[PSMB5]] | -0.44 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[CADPS2]] | -0.43 | -0.40 / -0.33 | both halves | 1e-04 | STRING 410 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELFN2]] | B | ELFN2 activity raises AHNAK2's level | lines that do not express ELFN2 (19) vs lines expressing it (31) | 2.92× lower at baseline in the lines without ELFN2 | 0.009 | ⚠ within organs, on part of the lines; also absent: IL31RA, LHX1, TMEM92 |
| [[MTOR]] | B | MTOR activity lowers AHNAK2's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 5.0% of all compounds | 0.024 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ZNF185]] | B | ZNF185 activity raises AHNAK2's level | lines that do not express ZNF185 (15) vs lines expressing it (35) | 2.19× lower at baseline in the lines without ZNF185 | 0.064 | ⚠ within organs, on part of the lines; also absent: HTR1D, KLF5, IL18 |
| [[CAPG]] | B | CAPG activity raises AHNAK2's level | lines that do not express CAPG (17) vs lines expressing it (33) | 2.10× lower at baseline in the lines without CAPG | 0.068 | ⚠ within organs, on part of the lines; also absent: MALL, LINC02086, SH3RF2 |
| [[A4GALT]] | B | A4GALT activity raises AHNAK2's level | lines that do not express A4GALT (14) vs lines expressing it (36) | 2.15× lower at baseline in the lines without A4GALT | 0.092 | ⚠ within organs, on part of the lines; also absent: HTR1D, PAPSS2, NT5E |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABTB1]] | B | AHNAK2 activity raises ABTB1's level | lines that do not express AHNAK2 (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without AHNAK2 | 0.033 | ⚠ within organs, on part of the lines; also absent: CAV1, CAV2, ITGA2; maybe low, not absent |
| [[SPAG9]] | B | AHNAK2 activity raises SPAG9's level | lines that do not express AHNAK2 (12) vs lines expressing it (38) | 1.56× lower at baseline in the lines without AHNAK2 | 0.064 | ⚠ within organs, on part of the lines; also absent: CAV1, CAV2, ITGA2; maybe low, not absent |
| [[GJB3]] | B | AHNAK2 activity raises GJB3's level | lines that do not express AHNAK2 (12) vs lines expressing it (38) | 2.25× lower at baseline in the lines without AHNAK2 | 0.074 | ⚠ within organs, on part of the lines; also absent: CAV1, CAV2, ITGA2; maybe low, not absent |
| [[MEGF6]] | B | AHNAK2 activity raises MEGF6's level | lines that do not express AHNAK2 (12) vs lines expressing it (38) | 2.27× lower at baseline in the lines without AHNAK2 | 0.080 | ⚠ within organs, on part of the lines; also absent: CAV1, CAV2, ITGA2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.2, 8.7); signed map (-9.2, 32.6). **Vector** length 118, 37.0% of its response variance represented; |z| ≥ 3 in 1,454 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.2 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +2.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +8.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.9 | +3.7 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.8 | +4.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.5 | +4.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +4.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -11.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.1 | -2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -17.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.3 | -5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.8 | -7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | AHNAK nucleoprotein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:104,937,244-104,978,374 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C14orf78 |
| Gene groups (HGNC) | PDZ domain containing |
| Matched by | ensembl_id |

UniProt [Q8IVF2](https://www.uniprot.org/uniprotkb/Q8IVF2) carries no function annotation.

**Summary**, from NCBI Gene [113146](https://www.ncbi.nlm.nih.gov/gene/113146):

> This gene encodes a large nucleoprotein. The encoded protein has a tripartite domain structure with a relatively short N-terminus and a long C-terminus, separated by a large body of repeats. The N-terminal PSD-95/Discs-large/ZO-1 (PDZ)-like domain is thought to function in the formation of stable homodimers. The encoded protein may play a role in calcium signaling by associating with calcium channel proteins. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr …

**Accessions** — [HGNC:20125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20125) · Entrez [113146](https://www.ncbi.nlm.nih.gov/gene/113146) · UniProt [Q8IVF2](https://www.uniprot.org/uniprotkb/Q8IVF2) · Ensembl [ENSG00000185567](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185567)

## Data

Gene col 11698: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11698); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11698, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11698]; `tensor/DDL_lfc|DDL_z.npy` [11698]; `embed/gene_vectors.npy` [11698]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11698 or target_col == 11698). Every well: [[AHNAK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AHNAK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
