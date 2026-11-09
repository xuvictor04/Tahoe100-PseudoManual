---
symbol: "MAVS"
type: "gene"
col: 1552
ensembl_id: "ENSG00000088888"
name: "mitochondrial antiviral signaling protein"
location: "20p13"
module: 118
arm: "+"
pooled_cpm: 57.75
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 25
n_dd_up_clean: 6
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# MAVS

*mitochondrial antiviral signaling protein* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 1.34× (z +4.6, q 0.003, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.308× (z -25.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOC7]] (+0.56, fdr 1e-05), [[APH1A]] (+0.56, fdr 3e-05), [[KPNA6]] (+0.55, fdr 2e-05); moves opposite to [[RFESD]] (-0.47, fdr 2e-04), [[NR1D1]] (-0.47, fdr 2e-05), [[CCDC28B]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BHLHE41]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1552.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.34×** | +4.6 | 0.003 | 34/48 (SK-MEL-2, Hs 766T, …) | all doses, flat |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.045 | 18/48 (J82, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +3.7 | 0.045 | 17/40 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.055 | 23/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.061 | 16/49 (HOP62, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.089 | 18/49 (HepG2/C3A, J82, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.089 | 20/49 (NCI-H2347, LS 180, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.18 | 13/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1552.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.308×** | -25.8 | 0e+00 | 48/48 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.330×** | -16.5 | 0e+00 | 46/48 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.363×** | -15.7 | 0e+00 | 47/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.410×** | -13.8 | 3e-41 | 44/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.460×** | -12.0 | 2e-31 | 43/48 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.498×** | -10.0 | 1e-21 | 43/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.322×** | -9.2 | 3e-18 | 44/49 (SW480, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.567×** | -8.8 | 1e-16 | 33/48 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.548×** | -8.6 | 4e-16 | 40/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.383×** | -7.8 | 4e-13 | 39/48 (SW480, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.617×** | -7.2 | 3e-11 | 35/47 (COLO 205, SNU-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.671×** | -5.9 | 1e-07 | 31/47 (HepG2/C3A, SW 900, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.714×** | -5.2 | 8e-06 | 31/48 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.734×** | -4.8 | 7e-05 | 27/48 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.566×** | -4.6 | 2e-04 | 23/38 (SW480, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.819×** | -4.3 | 5e-04 | 22/48 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.772×** | -3.7 | 0.007 | 23/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.807×** | -3.3 | 0.027 | 16/48 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.810×** | -3.3 | 0.031 | 15/47 (SNU-1, BT-474, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.695×** | -2.9 | 0.077 | 17/48 (HS-578T, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1552. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 95.0 | 0 | 11 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -22.9) |
| [[SNU-1 (line)]] | wt | 97.8 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -19.9) |
| [[COLO 205 (line)]] | alt | 134 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -27.9) |
| [[BT-474 (line)]] | alt | 78.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -21.9) |
| [[HOP62 (line)]] | alt | 75.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -14.8) |
| [[LoVo (line)]] | wt | 70.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -16.8) |
| [[MIA PaCa-2 (line)]] | alt | 76.5 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -19.9) |
| [[A-172 (line)]] | wt | 60.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -23.8) |
| [[NCI-H460 (line)]] | wt | 63.9 | 0 | 5 | — | [[Harringtonine (drug)]] 5 µM 0.219× (z -14.9) |
| [[RKO (line)]] | wt | 58.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -16.3) |
| [[SNU-423 (line)]] | alt | 97.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -23.7) |
| [[CFPAC-1 (line)]] | alt | 62.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -26.0) |
| [[HEC-1-A (line)]] | alt | 63.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -19.6) |
| [[HepG2_C3A (line)]] | wt | 84.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -13.0) |
| [[HT-29 (line)]] | alt | 71.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -19.3) |
| [[J82 (line)]] | alt | 63.5 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.180× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.299× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 52.9 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.249× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.293× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 64.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -18.8) |
| [[PANC-1 (line)]] | alt | 40.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -21.1) |
| [[RPMI-7951 (line)]] | alt | 98.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -15.1) |
| [[A549 (line)]] | wt | 59.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -18.7) |
| [[Hs 766T (line)]] | wt | 65.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 27.9 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.182× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 41.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -18.3) |
| [[SK-MEL-2 (line)]] | alt | 49.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -15.2) |
| [[A-427 (line)]] | wt | 22.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -15.1) |
| [[AsPC-1 (line)]] | alt | 40.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -17.1) |
| [[H4 (line)]] | wt | 50.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.4) |
| [[HCT15 (line)]] | alt | 89.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -9.9) |
| [[HS-578T (line)]] | alt | 50.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.273× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 48.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -17.1) |
| [[KATO III (line)]] | alt | 71.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -22.5) |
| [[LS 180 (line)]] | wt | 59.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 35.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.178× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 39.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.186× (z -13.1) |
| [[SHP-77 (line)]] | alt | 41.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0720× (z -22.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -10.3) |
| [[SW 1271 (line)]] | alt | 84.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -11.1) |
| [[SW 900 (line)]] | alt | 44.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -14.3) |
| [[SW1417 (line)]] | alt | 41.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -14.0) |
| [[NCI-H661 (line)]] | alt | 41.3 | 0 | 1 | — | [[Saquinavir (drug)]] 5 µM 0.175× (z -8.7) |
| [[A498 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1552), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC7]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[APH1A]] | +0.56 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[KPNA6]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[PHYKPL]] | +0.52 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[LARP4B]] | +0.52 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[ERVK13-1]] | +0.51 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[FBXL19]] | +0.50 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[TMEM127]] | +0.49 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[HMGA1P4]] | +0.48 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[PRR14L]] | +0.48 | +0.35 / +0.62 | both halves | 1e-04 |  |
| [[MFSD14CP-1]] | +0.46 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[PCGF3]] | +0.46 | +0.42 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFESD]] | -0.47 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[NR1D1]] | -0.47 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[CCDC28B]] | -0.45 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[N4BP3]] | -0.45 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[CYTH4]] | -0.44 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[WIPF3]] | -0.44 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[CD83]] | -0.43 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[PER2]] | -0.42 | -0.37 / -0.46 | both halves | 9e-05 |  |
| [[TLE6]] | -0.42 | -0.36 / -0.37 | both halves | 9e-05 |  |
| [[BIK]] | -0.42 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[SNPH]] | -0.41 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[MIDEAS]] | -0.41 | -0.39 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BHLHE41]] | B | BHLHE41 activity raises MAVS's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 1.19× lower at baseline in the lines without BHLHE41 | 0.069 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.288). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-13.8, -16.4); signed map (-10.4, -21.9). **Vector** length 75.3, 20.2% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.4 | -5.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +2.3 | +1.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | -1.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.2 | +3.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.7 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.5 | -3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.7 | -25.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -15.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.4 | -1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -2.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial antiviral signaling protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:3,846,799-3,876,123 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VISA, KIAA1271, IPS-1, Cardif |
| Gene groups (HGNC) | Caspase recruitment domain containing |
| Reactome | 27 pathways, smallest: NF-kB activation through FADD/RIP-1 pathway mediated by caspase-8 and -10; TRAF3-dependent IRF activation pathway; TRAF6 mediated IRF7 activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z434](https://www.uniprot.org/uniprotkb/Q7Z434) (Mitochondrial antiviral-signaling protein):

> Adapter required for innate immune defense against viruses. Acts downstream of DHX33, RIGI and IFIH1/MDA5, which detect intracellular dsRNA produced during viral replication, to coordinate pathways leading to the activation of NF-kappa-B, IRF3 and IRF7, and to the subsequent induction of antiviral cytokines such as IFNB and RANTES (CCL5). Peroxisomal and mitochondrial MAVS act sequentially to create an antiviral cellular state. Upon viral infection, peroxisomal MAVS induces the rapid …

**Summary**, from NCBI Gene [57506](https://www.ncbi.nlm.nih.gov/gene/57506):

> This gene encodes an intermediary protein necessary in the virus-triggered beta interferon signaling pathways. It is required for activation of transcription factors which regulate expression of beta interferon and contributes to antiviral innate immunity. [provided by RefSeq, Jul 2020]

**Accessions** — [HGNC:29233](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29233) · Entrez [57506](https://www.ncbi.nlm.nih.gov/gene/57506) · UniProt [Q7Z434](https://www.uniprot.org/uniprotkb/Q7Z434) · Ensembl [ENSG00000088888](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088888)

## Data

Gene col 1552: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1552); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1552, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1552]; `tensor/DDL_lfc|DDL_z.npy` [1552]; `embed/gene_vectors.npy` [1552]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1552 or target_col == 1552). Every well: [[MAVS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAVS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
