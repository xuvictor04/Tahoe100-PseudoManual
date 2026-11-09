---
symbol: "PCBD2"
type: "gene"
col: 5340
ensembl_id: "ENSG00000132570"
name: "pterin-4 alpha-carbinolamine dehydratase 2"
location: "5q31.1"
module: 124
arm: "+"
pooled_cpm: 52.38
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# PCBD2

*pterin-4 alpha-carbinolamine dehydratase 2* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.67× (z +6.9, q 3e-09, up in 29 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.58× (z +5.6, q 4e-06, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.433× (z -11.8, q 1e-29, down in 44 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.465× (z -10.8, q 4e-25, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AVEN]] (+0.73, fdr 7e-06), [[LINC01355]] (+0.70, fdr 7e-06), [[EPM2A]] (+0.70, fdr 7e-06); moves opposite to [[RNF24]] (-0.68, fdr 1e-05), [[PLEKHH3]] (-0.66, fdr 1e-05), [[RNF114]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SMIM15-AS1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5340.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +6.9 | 3e-09 | 29/42 (HT-29, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +6.3 | 7e-08 | 32/49 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +5.6 | 4e-06 | 38/48 (RKO, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.0 | 1e-04 | 25/48 (HS-578T, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +4.9 | 1e-04 | 22/43 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.6 | 4e-04 | 27/47 (Panc 03.27, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.37×** | +4.5 | 6e-04 | 31/48 (HOP62, A549, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.4 | 6e-04 | 0/49 | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.005 | 22/48 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.30×** | +3.6 | 0.016 | 22/48 (HEC-1-A, HOP62, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.078 | 20/47 (A-172, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5340.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.433×** | -11.8 | 1e-29 | 44/47 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.434×** | -11.8 | 1e-29 | 45/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.465×** | -10.8 | 4e-25 | 41/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.484×** | -10.3 | 1e-22 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.623×** | -9.5 | 3e-19 | 35/48 (NCI-H1573, A498, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.539×** | -8.7 | 2e-16 | 35/48 (SW 900, SW 1271, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.532×** | -8.6 | 7e-16 | 33/48 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.547×** | -8.6 | 8e-16 | 37/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.550×** | -8.5 | 2e-15 | 45/48 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.568×** | -7.7 | 7e-13 | 34/47 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.375×** | -7.3 | 2e-11 | 42/49 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.617×** | -6.8 | 4e-10 | 32/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.654×** | -6.0 | 7e-08 | 32/48 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.470×** | -5.6 | 1e-06 | 30/48 (NCI-H1573, AN3 CA, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.691×** | -5.2 | 6e-06 | 28/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.721×** | -4.6 | 2e-04 | 27/48 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.602×** | -3.8 | 0.005 | 19/48 (NCI-H2030, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.742×** | -3.6 | 0.010 | 17/48 (BT-474, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.841× | -3.5 | 0.014 | 17/48 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |
| [[Ritonavir (drug)]] 0.5 µM |  | **0.813×** | -3.0 | 0.081 | 10/48 (MIA PaCa-2, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5340. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 84.6 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.180× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.117× (z -10.9) |
| [[PANC-1 (line)]] | alt | 61.0 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.192× (z -18.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.450× (z -8.8) |
| [[LoVo (line)]] | wt | 96.8 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.259× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 62.6 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.293× (z -11.6) |
| [[SW480 (line)]] | alt | 80.3 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -14.7) |
| [[KATO III (line)]] | alt | 55.1 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.242× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 64.9 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -18.1) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H2030 (line)]] | alt | 84.2 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.305× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 94.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -14.3) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.341× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 55.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -11.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[C-33 A (line)]] | alt | 70.6 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.215× (z -10.6) |
| [[LS 180 (line)]] | wt | 60.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.358× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 43.7 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -14.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 43.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -15.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A549 (line)]] | wt | 63.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -13.0) ⚠ cell-cycle shift, explains ~47% of this change |
| [[AN3 CA (line)]] | alt | 66.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 81.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -11.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SW 900 (line)]] | alt | 34.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -12.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.254× (z -9.3) |
| [[SW48 (line)]] | wt | 62.5 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.172× (z -10.6) |
| [[A-172 (line)]] | wt | 30.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -8.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[CFPAC-1 (line)]] | alt | 37.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.332× (z -8.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 42.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -8.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SNU-1 (line)]] | wt | 51.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -10.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW 1271 (line)]] | alt | 55.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0632× (z -9.1) |
| [[SW1417 (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.347× (z -8.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5340), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVEN]] | +0.73 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[LINC01355]] | +0.70 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[EPM2A]] | +0.70 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[PCBP1-AS1]] | +0.70 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[SMIM15-AS1]] | +0.68 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[DPH5-DT]] | +0.67 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[GNL3L]] | +0.67 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[EXOSC6]] | +0.67 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[HCG18]] | +0.67 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[RCBTB2]] | +0.66 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ANKAR]] | +0.66 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[EFCAB8]] | +0.65 | +0.60 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF24]] | -0.68 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.66 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[RNF114]] | -0.64 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[BLVRB]] | -0.64 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[TMEM256]] | -0.63 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[TNNI3]] | -0.63 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[KBTBD3]] | -0.62 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[PEX3]] | -0.61 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[HILPDA]] | -0.61 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[TUBG2]] | -0.61 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[RFX2]] | -0.60 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[MXI1]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMIM15-AS1]] | C | SMIM15-AS1's natural level strengthens PCBD2's drug response | SMIM15-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.13; direction not clear | 0.034 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.704). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (8.9, -8.6); signed map (22.8, -28.0). **Vector** length 106, 31.5% of its response variance represented; |z| ≥ 3 in 1,100 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | -1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.0 | +4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.9 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.9 | +5.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.3 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.7 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | -0.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.1 | -8.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.8 | -10.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.4 | -10.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.2 | -4.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -8.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.9 | -3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.7 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -1.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | pterin-4 alpha-carbinolamine dehydratase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:134,905,120-135,007,959 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DCOHM, DCOH2 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Pterin-4 alpha-carbinolamine dehydratases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0N5](https://www.uniprot.org/uniprotkb/Q9H0N5) (Pterin-4-alpha-carbinolamine dehydratase 2):

> Plays a role in tetrahydrobiopterin biosynthesis which is a cofactor for amino acid hydroxylases. May prevent both the formation of 7-pterins and accelerate the formation of quinonoid-BH2 (By similarity). Regulates the dimerization of homeodomain protein HNF1A and enhances its transcriptional activity. Also acts as a coactivator for HNF1B-dependent transcription.

**Summary**, from NCBI Gene [84105](https://www.ncbi.nlm.nih.gov/gene/84105):

> Predicted to enable 4-alpha-hydroxytetrahydrobiopterin dehydratase activity; identical protein binding activity; and phenylalanine 4-monooxygenase activity. Involved in positive regulation of DNA-templated transcription. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24474](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24474) · Entrez [84105](https://www.ncbi.nlm.nih.gov/gene/84105) · UniProt [Q9H0N5](https://www.uniprot.org/uniprotkb/Q9H0N5) · Ensembl [ENSG00000132570](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132570)

## Data

Gene col 5340: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5340); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5340, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5340]; `tensor/DDL_lfc|DDL_z.npy` [5340]; `embed/gene_vectors.npy` [5340]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5340 or target_col == 5340). Every well: [[PCBD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCBD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
