---
symbol: "ARHGEF11"
type: "gene"
col: 5361
ensembl_id: "ENSG00000132694"
name: "Rho guanine nucleotide exchange factor 11"
location: "1q23.1"
module: 18
arm: "+"
pooled_cpm: 97.44
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ARHGEF11

*Rho guanine nucleotide exchange factor 11* — 1q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.60× (z +11.6, q 4e-28, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.623× (z -11.6, q 3e-28, down in 34 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.650× (z -10.6, q 7e-24, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SFMBT1]] (+0.71, fdr 1e-05), [[ATAD2B]] (+0.70, fdr 7e-06), [[MACROH2A2]] (+0.69, fdr 7e-06); moves opposite to [[SPAG9]] (-0.56, fdr 3e-05), [[GNAI3]] (-0.54, fdr 4e-05), [[ZMYM6]] (-0.53, fdr 1e-04).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[FAM135A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5361.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +11.6 | 4e-28 | 43/48 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +9.0 | 5e-17 | 36/48 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +8.7 | 4e-16 | 36/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +8.7 | 4e-16 | 30/49 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +7.5 | 7e-12 | 31/47 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +6.8 | 7e-10 | 29/48 (SW480, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.9 | 3e-07 | 29/47 (HEC-1-A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +5.6 | 1e-06 | 29/47 (H4, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +4.4 | 7e-04 | 21/47 (C32, SW48, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +4.2 | 0.001 | 21/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +4.0 | 0.003 | 17/48 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.18× | +3.9 | 0.004 | 18/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.9 | 0.004 | 22/48 (HS-578T, CFPAC-1, …) | top dose only | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.15× | +3.4 | 0.028 | 16/48 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.28×** | +3.2 | 0.048 | 14/43 (AsPC-1, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.048 | 16/49 (SW480, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.066 | 12/48 (NCI-H2347, SNU-423, …) | inconsistent across doses |  |
| [[Penfluridol (drug)]] 5 µM |  | 1.14× | +3.1 | 0.066 | 9/47 (A498, KATO III, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.13× | +3.1 | 0.066 | 11/48 (NCI-H2347, Hs 766T, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.26×** | +2.9 | 0.095 | 11/49 (NCI-H2347, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5361.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.623×** | -11.6 | 3e-28 | 34/49 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.620×** | -11.3 | 4e-27 | 32/44 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.650×** | -10.6 | 7e-24 | 35/48 (A-427, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.682×** | -9.4 | 9e-19 | 31/48 (SW480, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.710×** | -8.4 | 6e-15 | 30/48 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.702×** | -8.0 | 9e-14 | 33/45 (Panc 03.27, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.735×** | -7.5 | 4e-12 | 29/48 (NCI-H1573, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -4.3 | 0.001 | 22/48 (SW480, SHP-77, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.773×** | -3.3 | 0.062 | 13/38 (BT-474, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.917× | -3.0 | 0.15 | 10/48 (NCI-H2030, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5361. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 96.1 | 3 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.545× (z -9.3) |
| [[SW480 (line)]] | alt | 83.2 | 2 | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.464× (z -12.5) |
| [[PANC-1 (line)]] | alt | 109 | 2 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.441× (z -13.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 247 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.26× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.293× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.409× (z -12.4) |
| [[A-427 (line)]] | wt | 181 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -24.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.334× (z -16.4) |
| [[NCI-H23 (line)]] | alt | 236 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0939× (z -33.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.519× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 122 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -20.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 157 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.463× (z -10.8) |
| [[SW1417 (line)]] | alt | 101 | 2 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.490× (z -10.0) |
| [[C-33 A (line)]] | alt | 183 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.500× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 77.7 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.553× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 72.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 192 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -17.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 139 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.432× (z -10.9) |
| [[KATO III (line)]] | alt | 79.5 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.472× (z -9.5) |
| [[LS 180 (line)]] | wt | 93.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.483× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 96.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +14.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.496× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~57% of this change |
| [[NCI-H1573 (line)]] | alt | 111 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -17.1) |
| [[Panc 03.27 (line)]] | alt | 91.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -24.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 157 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -23.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 75.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.473× (z -8.9) |
| [[A498 (line)]] | wt | 88.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -13.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 153 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -9.7) |
| [[BT-474 (line)]] | alt | 59.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 27.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 88.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.251× (z -12.7) ⚠ toxic; cell-cycle shift, explains ~57% of this change |
| [[J82 (line)]] | alt | 50.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.391× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 44.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 277 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.178× (z -15.9) |
| [[SNU-423 (line)]] | alt | 46.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 89.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +8.9) | — |
| [[A549 (line)]] | wt | 80.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 78.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 63.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5361), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFMBT1]] | +0.71 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[ATAD2B]] | +0.70 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[MACROH2A2]] | +0.69 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[PKD2]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[ARID2]] | +0.63 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[DPY19L1P1]] | +0.63 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SPECC1L]] | +0.62 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[PAXBP1]] | +0.62 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[NR2C2]] | +0.61 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[CRTC3]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[TOR3A]] | +0.60 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[ZNRF2P2]] | +0.60 | +0.56 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG9]] | -0.56 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[GNAI3]] | -0.54 | -0.46 / -0.41 | both halves | 4e-05 | same gene group |
| [[ZMYM6]] | -0.53 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[UFM1]] | -0.52 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[LTN1]] | -0.52 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[CAST]] | -0.51 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[NBEAL1]] | -0.51 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[TVP23C]] | -0.50 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[PLXNA3]] | -0.49 | -0.37 / -0.45 | both halves | 8e-05 | pathway: Semaphorin interactions |
| [[TBC1D23]] | -0.49 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[NELFE]] | -0.49 | -0.55 / -0.28 | both halves | 3e-04 | same gene group |
| [[APBB3]] | -0.49 | -0.43 / -0.32 | both halves | 2e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM135A]] | C | ARHGEF11's natural level strengthens FAM135A's drug response | ARHGEF11's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.12; direction clear | 0.060 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.470). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.3, 13.8); signed map (7.4, -4.3). **Vector** length 123, 35.6% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +8.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +7.1 | +6.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +7.0 | +8.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.1 | +11.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +7.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +4.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.2 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +4.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.4 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +1.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.3 | -10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | -7.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.5 | -8.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.0 | -9.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -4.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.1 — chr1:156,934,840-157,046,903 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0380, GTRAP48, PDZ-RHOGEF |
| Gene groups (HGNC) | Dbl family Rho GEFs; PDZ domain containing; MicroRNA protein coding host genes |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 20 pathways, smallest: Sema4D induced cell migration and growth-cone collapse; Sema4D in semaphorin signaling; NRAGE signals death through JNK |
| Matched by | ensembl_id |

**Function**, from UniProt [O15085](https://www.uniprot.org/uniprotkb/O15085) (Rho guanine nucleotide exchange factor 11):

> May play a role in the regulation of RhoA GTPase by guanine nucleotide-binding alpha-12 (GNA12) and alpha-13 (GNA13). Acts as guanine nucleotide exchange factor (GEF) for RhoA GTPase and may act as GTPase-activating protein (GAP) for GNA12 and GNA13. Involved in neurotrophin-induced neurite outgrowth.

**Summary**, from NCBI Gene [9826](https://www.ncbi.nlm.nih.gov/gene/9826):

> Rho GTPases play a fundamental role in numerous cellular processes that are initiated by extracellular stimuli that work through G protein coupled receptors. The encoded protein may form a complex with G proteins and stimulate Rho-dependent signals. A similar protein in rat interacts with glutamate transporter EAAT4 and modulates its glutamate transport activity. Expression of the rat protein induces the reorganization of the actin cytoskeleton and its overexpression induces the formation of …

**Accessions** — [HGNC:14580](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14580) · Entrez [9826](https://www.ncbi.nlm.nih.gov/gene/9826) · UniProt [O15085](https://www.uniprot.org/uniprotkb/O15085) · Ensembl [ENSG00000132694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132694)

## Data

Gene col 5361: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5361); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5361, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5361]; `tensor/DDL_lfc|DDL_z.npy` [5361]; `embed/gene_vectors.npy` [5361]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5361 or target_col == 5361). Every well: [[ARHGEF11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
