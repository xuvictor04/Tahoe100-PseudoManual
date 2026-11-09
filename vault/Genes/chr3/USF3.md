---
symbol: "USF3"
type: "gene"
col: 10729
ensembl_id: "ENSG00000176542"
name: "upstream transcription factor family member 3"
location: "3q13.2"
module: 118
arm: "+"
pooled_cpm: 49.52
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 25
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# USF3

*upstream transcription factor family member 3* — 3q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.82× (z +8.0, q 6e-13, up in 32 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.510× (z -17.3, q 0e+00, down in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.623× (z -12.2, q 7e-32, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMUB2]] (+0.68, fdr 7e-06), [[PPP6C]] (+0.59, fdr 2e-05), [[KPNA6]] (+0.56, fdr 1e-05); moves opposite to [[GLS]] (-0.48, fdr 3e-05), [[DENND1A]] (-0.47, fdr 1e-04), [[POLR3G]] (-0.47, fdr 2e-04).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[MAP3K11]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10729.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.82×** | +8.0 | 6e-13 | 32/49 (NCI-H460, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.37×** | +4.3 | 0.006 | 20/48 (A-427, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +4.1 | 0.006 | 0/49 | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.18× | +4.1 | 0.006 | 15/47 (SK-MEL-2, J82, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.8 | 0.018 | 12/47 (LoVo, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.061 | 10/49 (NCI-H1573, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.079 | 11/48 (HEC-1-A, H4, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.12 | 6/48 (HOP62, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10729.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.510×** | -17.3 | 0e+00 | 44/48 (NCI-H1573, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.536×** | -16.0 | 0e+00 | 44/48 (NCI-H1573, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.559×** | -14.9 | 0e+00 | 41/48 (A498, SW 900, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.623×** | -12.2 | 7e-32 | 36/47 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.734×** | -11.2 | 3e-27 | 31/48 (HS-578T, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.667×** | -10.4 | 2e-23 | 37/48 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.761×** | -9.9 | 3e-21 | 36/48 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.673×** | -9.8 | 9e-21 | 35/48 (hTERT-HPNE, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.693×** | -9.4 | 3e-19 | 39/48 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.725×** | -8.3 | 7e-15 | 35/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.728×** | -7.8 | 2e-13 | 31/49 (LS 180, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.741×** | -7.4 | 6e-12 | 28/47 (J82, BT-474, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.753×** | -7.0 | 1e-10 | 30/48 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.597×** | -6.9 | 2e-10 | 29/49 (A498, NCI-H1573, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.767×** | -6.8 | 4e-10 | 30/48 (A-172, RPMI-7951, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.824×** | -5.0 | 2e-05 | 22/48 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.698×** | -4.8 | 3e-05 | 21/48 (HOP62, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.861× | -3.6 | 0.008 | 16/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trimetrexate (drug)]] 5 µM |  | 0.908× | -3.5 | 0.009 | 7/49 (CHP-212, LoVo, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.915× | -3.2 | 0.023 | 12/48 (A-427, NCI-H1573, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.794×** | -3.1 | 0.035 | 11/48 (MIA PaCa-2, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.885× | -3.0 | 0.042 | 9/47 (A549, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10729. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 63.8 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -16.4) |
| [[AsPC-1 (line)]] | alt | 38.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -13.9) |
| [[CFPAC-1 (line)]] | alt | 48.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -12.1) |
| [[hTERT-HPNE (line)]] | wt | 44.7 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0769× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.330× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 71.8 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.628× (z -8.7) |
| [[SW480 (line)]] | alt | 55.9 | 0 | 5 (5 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.146× (z -15.2) ⚠ toxic |
| [[A498 (line)]] | wt | 35.4 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.362× (z -12.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.480× (z -9.1) |
| [[J82 (line)]] | alt | 42.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -15.4) |
| [[NCI-H460 (line)]] | wt | 32.4 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.16× (z +8.9) | [[Homoharringtonine (drug)]] 0.05 µM 0.469× (z -9.0) |
| [[A-172 (line)]] | wt | 42.4 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.275× (z -13.5) ⚠ cell-cycle shift, explains ~20% of this change |
| [[COLO 205 (line)]] | alt | 64.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -16.2) |
| [[HT-29 (line)]] | alt | 75.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.421× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.438× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 61.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -12.3) |
| [[PANC-1 (line)]] | alt | 58.7 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.481× (z -10.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW 900 (line)]] | alt | 45.5 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.324× (z -10.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.370× (z -8.7) |
| [[HCT15 (line)]] | alt | 67.9 | 0 | 2 | — | [[Sonidegib (drug)]] 5 µM 0.0918× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 41.0 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.385× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~68% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.531× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 51.5 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.290× (z -11.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW48 (line)]] | wt | 35.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.377× (z -8.7) |
| [[BT-474 (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.402× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 55.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.448× (z -9.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 50.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.440× (z -8.6) |
| [[LoVo (line)]] | wt | 36.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -22.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[LOX-IMVI (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.364× (z -9.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LS 180 (line)]] | wt | 44.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -9.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H23 (line)]] | alt | 76.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.450× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 61.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.500× (z -9.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-1 (line)]] | wt | 37.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -8.7) |
| [[SW 1271 (line)]] | alt | 52.8 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0966× (z -8.6) |
| [[A-427 (line)]] | wt | 70.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 60.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10729), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMUB2]] | +0.68 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[PPP6C]] | +0.59 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[KPNA6]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ZBTB3]] | +0.53 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[WDR83]] | +0.53 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[KBTBD4]] | +0.52 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[PRCC]] | +0.52 | +0.43 / +0.50 | both halves | 4e-05 |  |
| [[EMC3]] | +0.52 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[SUPT4H1]] | +0.52 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[NRL]] | +0.51 | +0.21 / +0.56 | both halves | 6e-04 |  |
| [[NAA60]] | +0.51 | +0.37 / +0.45 | both halves | 9e-05 |  |
| [[APPBP2]] | +0.51 | +0.48 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLS]] | -0.48 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[DENND1A]] | -0.47 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[POLR3G]] | -0.47 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[CEP83]] | -0.44 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[RELT]] | -0.43 | -0.34 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP3K11]] | C | USF3's natural level strengthens MAP3K11's drug response | USF3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.27; direction not clear | 0.013 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-26.4, -10.0); signed map (-6.7, -11.6). **Vector** length 78.9, 16.1% of its response variance represented; |z| ≥ 3 in 1,149 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.4 | +0.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.2 | +8.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~68% of this change | +2.9 | -3.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | -0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | -1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.2 | +3.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.6 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -9.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.3 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -8.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -6.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | upstream transcription factor family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.2 — chr3:113,648,385-113,696,646 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA2018 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68DE3](https://www.uniprot.org/uniprotkb/Q68DE3) (Basic helix-loop-helix domain-containing protein USF3):

> Involved in the negative regulation of epithelial-mesenchymal transition, the process by which epithelial cells lose their polarity and adhesion properties to become mesenchymal cells with enhanced migration and invasive properties.

**Summary**, from NCBI Gene [205717](https://www.ncbi.nlm.nih.gov/gene/205717):

> This gene encodes a large protein that contains a helix-loop-helix domain and a polyglutamine region. A deletion in the polyglutamine region was associated with risk for thyroid carcinoma. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:30494](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30494) · Entrez [205717](https://www.ncbi.nlm.nih.gov/gene/205717) · UniProt [Q68DE3](https://www.uniprot.org/uniprotkb/Q68DE3) · Ensembl [ENSG00000176542](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176542)

## Data

Gene col 10729: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10729); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10729, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10729]; `tensor/DDL_lfc|DDL_z.npy` [10729]; `embed/gene_vectors.npy` [10729]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10729 or target_col == 10729). Every well: [[USF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
