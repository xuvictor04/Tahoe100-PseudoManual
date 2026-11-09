---
symbol: "PSMC2"
type: "gene"
col: 8415
ensembl_id: "ENSG00000161057"
name: "proteasome 26S subunit, ATPase 2"
location: "7q22.1"
module: 7
arm: "+"
pooled_cpm: 51.05
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# PSMC2

*proteasome 26S subunit, ATPase 2* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (12 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.75× (z +20.8, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.723× (z -6.7, q 9e-09, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HIKESHI]] (+0.70, fdr 1e-05), [[NSUN3]] (+0.67, fdr 3e-05), [[PSMC1]] (+0.67, fdr 7e-06); moves opposite to [[EML4]] (-0.57, fdr 4e-05), [[PPM1G]] (-0.57, fdr 4e-05), [[SNX25]] (-0.56, fdr 2e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8415.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.75×** | +20.8 | 0e+00 | 48/49 (PANC-1, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.44×** | +18.5 | 0e+00 | 46/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.41×** | +18.2 | 0e+00 | 48/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.97×** | +15.0 | 0e+00 | 43/48 (SW480, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.06×** | +14.2 | 8e-44 | 46/48 (LOX-IMVI, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.61×** | +14.0 | 9e-43 | 41/48 (NCI-H23, NCI-H460, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +11.8 | 2e-30 | 37/47 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +10.8 | 4e-25 | 37/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +9.5 | 2e-19 | 39/48 (SW480, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.47×** | +8.0 | 7e-14 | 29/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +7.7 | 6e-13 | 32/48 (MIA PaCa-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.46×** | +7.5 | 2e-12 | 36/48 (NCI-H460, NCI-H23, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.42×** | +6.7 | 1e-09 | 26/44 (A-427, Panc 03.27, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.37×** | +6.5 | 2e-09 | 33/48 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +6.5 | 4e-09 | 26/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.9 | 1e-07 | 25/48 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.44×** | +5.5 | 1e-06 | 34/49 (LOX-IMVI, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +5.4 | 2e-06 | 25/48 (NCI-H2347, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.8 | 5e-05 | 21/48 (A-172, COLO 205, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.002 | 17/48 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.005 | 16/48 (PANC-1, SW480, …) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8415.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.723×** | -6.7 | 9e-09 | 27/48 (NCI-H2347, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.816×** | -6.0 | 4e-07 | 27/48 (A-172, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.750×** | -6.0 | 4e-07 | 26/48 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -5.3 | 1e-05 | 1/49 (NCI-H2122) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.774×** | -5.3 | 1e-05 | 27/48 (LS 180, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.793×** | -4.8 | 1e-04 | 24/48 (LoVo, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.832×** | -3.8 | 0.010 | 22/48 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -3.6 | 0.020 | 19/48 (NCI-H2347, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8415. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 59.1 | 11 (5 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.89× (z +14.3) | — |
| [[NCI-H460 (line)]] | wt | 44.6 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.59× (z +12.1) | — |
| [[PANC-1 (line)]] | alt | 44.1 | 8 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.8× (z +15.1) | — |
| [[LoVo (line)]] | wt | 48.7 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +13.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.13× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 50.7 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.52× (z +12.9) | — |
| [[KATO III (line)]] | alt | 65.5 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.98× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LOX-IMVI (line)]] | wt | 26.6 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.72× (z +11.8) | — |
| [[NCI-H2347 (line)]] | alt | 70.8 | 4 | 1 | [[TAK-901 (drug)]] 5 µM 4.88× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.505× (z -8.8) |
| [[RKO (line)]] | wt | 62.5 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.2× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW48 (line)]] | wt | 79.1 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 4.07× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 40.9 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.06× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 34.3 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.74× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 37.4 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 9.50× (z +11.6) | — |
| [[LS 180 (line)]] | wt | 50.0 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.6× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 53.1 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 9.80× (z +11.7) | — |
| [[A-172 (line)]] | wt | 63.4 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.96× (z +10.6) | — |
| [[A498 (line)]] | wt | 84.2 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.91× (z +11.6) | — |
| [[HT-29 (line)]] | alt | 48.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.97× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 46.9 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.78× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 45.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +14.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.95× (z +11.4) | — |
| [[RPMI-7951 (line)]] | alt | 57.2 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.85× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 46.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.75× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 66.4 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.87× (z +10.6) | — |
| [[A-427 (line)]] | wt | 52.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.76× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.87× (z +8.5) | — |
| [[A549 (line)]] | wt | 36.8 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.92× (z +9.5) | — |
| [[AsPC-1 (line)]] | alt | 37.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.12× (z +10.1) | — |
| [[COLO 205 (line)]] | alt | 36.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.83× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 46.0 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.96× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 50.6 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.75× (z +8.9) | — |
| [[SW 1088 (line)]] | alt | 87.3 | 0 | 2 | — | [[Thymopentin (drug)]] 5 µM 0.0806× (z -9.1) |
| [[C32 (line)]] | wt | 105 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.70× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 55.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.00× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 62.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.81× (z +11.0) | — |
| [[J82 (line)]] | alt | 47.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.14× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +8.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SHP-77 (line)]] | alt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.14× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | — |
| [[SW 900 (line)]] | alt | 57.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.75× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 101 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8415), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIKESHI]] | +0.70 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[NSUN3]] | +0.67 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[PSMC1]] | +0.67 | +0.72 / +0.64 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[AP5M1]] | +0.66 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[RAE1]] | +0.66 | +0.59 / +0.53 | both halves | 1e-05 | pathway: Disorders of transmembrane transporters |
| [[SUPT7L]] | +0.66 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[MOB4]] | +0.66 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[MAIP1]] | +0.65 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[HTATIP2]] | +0.65 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[TACO1]] | +0.64 | +0.66 / +0.35 | both halves | 1e-04 |  |
| [[PSMA6]] | +0.64 | +0.67 / +0.64 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[BLOC1S2]] | +0.64 | +0.70 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EML4]] | -0.57 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[PPM1G]] | -0.57 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[SNX25]] | -0.56 | -0.59 / -0.29 | both halves | 2e-04 |  |
| [[GRK6]] | -0.54 | -0.59 / -0.26 | both halves | 4e-04 |  |
| [[R3HDM4]] | -0.54 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[LLGL2]] | -0.54 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[OSBPL8]] | -0.53 | -0.57 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PSMC2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PSMC2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CD9]] | B | CD9 activity raises PSMC2's level | lines that do not express CD9 (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without CD9 | 0.099 | ⚠ within organs, on part of the lines; also absent: ALS2CL, CARD10, MSX2; maybe low, not absent |
| [[EPM2AIP1]] | C | EPM2AIP1 activity lowers PSMC2's level | lines that do not express EPM2AIP1 (3) vs lines expressing it (47) | 1.62× higher at baseline in the lines without EPM2AIP1 | 0.092 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MLF1, ADAL, TTC30A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.519). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-16.2, 9.0); signed map (13.9, -24.7). **Vector** length 96.1, 26.3% of its response variance represented; |z| ≥ 3 in 1,169 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.1 | +14.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.5 | +18.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.5 | +18.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.7 | +20.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.7 | +5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +15.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +9.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +1.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | -3.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -6.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.8 | -6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.5 | -5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -0.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.0 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit, ATPase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:103,328,570-103,370,346 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MSS1, S7, Nbla10058, RPT1 |
| Gene groups (HGNC) | AAA ATPases; Proteasome |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 170 pathways, smallest: Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC); Cross-presentation of soluble exogenous antigens (endosomes) |
| Matched by | ensembl_id |

**Function**, from UniProt [P35998](https://www.uniprot.org/uniprotkb/P35998) (26S proteasome regulatory subunit 7):

> Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair. PSMC2 belongs to …

**Summary**, from NCBI Gene [5701](https://www.ncbi.nlm.nih.gov/gene/5701):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9548](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9548) · Entrez [5701](https://www.ncbi.nlm.nih.gov/gene/5701) · UniProt [P35998](https://www.uniprot.org/uniprotkb/P35998) · Ensembl [ENSG00000161057](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161057)

## Data

Gene col 8415: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8415); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8415, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8415]; `tensor/DDL_lfc|DDL_z.npy` [8415]; `embed/gene_vectors.npy` [8415]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8415 or target_col == 8415). Every well: [[PSMC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
