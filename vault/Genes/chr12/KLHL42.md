---
symbol: "KLHL42"
type: "gene"
col: 1504
ensembl_id: "ENSG00000087448"
name: "kelch like family member 42"
location: "12p11.22"
module: 137
arm: "+"
pooled_cpm: 36.71
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 8
n_dd_up_clean: 22
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# KLHL42

*kelch like family member 42* — 12p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +12.6, q 2e-33, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.263× (z -30.4, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAIM]] (+0.72, fdr 1e-04), [[ST7]] (+0.69, fdr 5e-05), [[SMAD1]] (+0.69, fdr 1e-05); moves opposite to [[DNAAF3]] (-0.67, fdr 1e-04), [[NBEAL1]] (-0.66, fdr 3e-05), [[GNAI2]] (-0.66, fdr 4e-04).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[BATF]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1504.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +12.6 | 2e-33 | 37/48 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +9.2 | 7e-18 | 26/48 (A-427, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +9.1 | 2e-17 | 28/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.50×** | +8.8 | 2e-16 | 33/48 (PANC-1, HS-578T, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +8.6 | 9e-16 | 33/47 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +8.2 | 2e-14 | 35/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +7.9 | 3e-13 | 28/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +7.5 | 6e-12 | 32/48 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +6.8 | 8e-10 | 26/48 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +6.7 | 1e-09 | 25/48 (HEC-1-A, SW 900, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +6.5 | 4e-09 | 26/47 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +6.3 | 2e-08 | 26/48 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +5.2 | 9e-06 | 21/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.24×** | +4.8 | 6e-05 | 16/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +4.7 | 1e-04 | 10/48 (BT-474, LoVo, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +4.6 | 2e-04 | 17/47 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.22×** | +4.5 | 2e-04 | 13/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1504.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.263×** | -30.4 | 0e+00 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.268×** | -30.0 | 0e+00 | 48/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.344×** | -24.3 | 0e+00 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.578×** | -12.5 | 1e-33 | 35/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.700×** | -8.2 | 4e-14 | 32/47 (AN3 CA, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.613×** | -5.8 | 5e-07 | 27/48 (SW480, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.851× | -5.2 | 1e-05 | 18/48 (SW48, HS-578T, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.674×** | -4.7 | 2e-04 | 18/48 (LoVo, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.815×** | -4.7 | 2e-04 | 18/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.856× | -3.6 | 0.020 | 18/47 (LoVo, HT-29, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.860× | -3.5 | 0.028 | 12/47 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.871× | -3.2 | 0.072 | 7/48 (HS-578T, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1504. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 62.6 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -22.3) |
| [[NCI-H2030 (line)]] | alt | 46.3 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -12.8) |
| [[SW480 (line)]] | alt | 58.8 | 1 (1 ⚠) | 4 | [[Topotecan (hydrochloride) (drug)]] 5 µM 1.82× (z +8.6) ⚠ toxic | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -25.2) |
| [[A-427 (line)]] | wt | 29.8 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -13.6) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.250× (z -12.2) |
| [[A498 (line)]] | wt | 27.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.166× (z -17.7) |
| [[J82 (line)]] | alt | 34.3 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.255× (z -13.1) |
| [[LOX-IMVI (line)]] | wt | 43.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -18.5) |
| [[MIA PaCa-2 (line)]] | alt | 35.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -16.8) |
| [[NCI-H1573 (line)]] | alt | 45.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -11.2) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 47.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -10.3) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.358× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 27.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.192× (z -17.1) |
| [[Panc 03.27 (line)]] | alt | 39.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -14.6) |
| [[PANC-1 (line)]] | alt | 42.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -17.1) |
| [[RKO (line)]] | wt | 55.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.201× (z -15.1) |
| [[SW1417 (line)]] | alt | 56.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.259× (z -15.0) |
| [[A-172 (line)]] | wt | 38.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -17.6) |
| [[A549 (line)]] | wt | 32.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.201× (z -14.8) |
| [[AN3 CA (line)]] | alt | 54.3 | 0 | 3 (1 ⚠) | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0681× (z -13.1) |
| [[C-33 A (line)]] | alt | 53.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.190× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 35.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -16.1) |
| [[HOP62 (line)]] | alt | 52.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -13.5) |
| [[KATO III (line)]] | alt | 28.0 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.151× (z -15.4) |
| [[LS 180 (line)]] | wt | 32.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -12.5) |
| [[SHP-77 (line)]] | alt | 72.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.142× (z -21.2) |
| [[SW48 (line)]] | wt | 61.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.107× (z -16.2) |
| [[C32 (line)]] | wt | 40.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.257× (z -11.3) |
| [[HS-578T (line)]] | alt | 23.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -10.5) |
| [[HT-29 (line)]] | alt | 24.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.213× (z -10.9) |
| [[SNU-1 (line)]] | wt | 50.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -13.4) |
| [[BT-474 (line)]] | alt | 31.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.234× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -8.6) |
| [[Hs 766T (line)]] | wt | 21.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 22.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.4) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 23.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.296× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1504), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAIM]] | +0.72 | +0.71 / +0.34 | both halves | 1e-04 |  |
| [[ST7]] | +0.69 | +0.55 / +0.39 | both halves | 5e-05 |  |
| [[SMAD1]] | +0.69 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[GABPB1]] | +0.67 | +0.48 / +0.40 | both halves | 4e-05 |  |
| [[GTF3C6]] | +0.67 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[ANGEL2]] | +0.66 | +0.59 / +0.39 | both halves | 6e-05 |  |
| [[NIPAL2]] | +0.66 | +0.47 / +0.37 | both halves | 8e-05 |  |
| [[FAM169A]] | +0.65 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[SLC16A14]] | +0.65 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[ADCK1]] | +0.65 | +0.60 / +0.28 | both halves | 3e-04 |  |
| [[CCNJ]] | +0.65 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[UBTF]] | +0.65 | +0.59 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF3]] | -0.67 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[NBEAL1]] | -0.66 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[GNAI2]] | -0.66 | -0.54 / -0.25 | both halves | 4e-04 |  |
| [[F11R]] | -0.65 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[ALDOA]] | -0.65 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[SUN1]] | -0.64 | -0.52 / -0.37 | both halves | 7e-05 |  |
| [[SPAG9]] | -0.64 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[LMTK3]] | -0.63 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[MAGT1]] | -0.61 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[SLC27A1]] | -0.61 | -0.46 / -0.21 | both halves | 6e-04 |  |
| [[CADM4]] | -0.60 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[ASMTL]] | -0.59 | -0.48 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BATF]] | B | BATF activity weakens KLHL42's drug response | lines that do not express BATF (33) vs lines expressing it (15) | the lines without BATF respond 0.96× as strongly (z diff +0.08); strongest at Belinostat 5 µM: 0.31x vs 0.44x (z diff -3.1) | 0.033 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2; target measured in part of the lines; both ways; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers KLHL42's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC16A1-AS1]] | B | SLC16A1-AS1 activity raises KLHL42's level | lines that do not express SLC16A1-AS1 (5) vs lines expressing it (45) | 1.52× lower at baseline in the lines without SLC16A1-AS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: P3H4, SLC16A1, DUSP19 |
| [[FAXC]] | B | FAXC activity raises KLHL42's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.49× lower at baseline in the lines without FAXC | 0.056 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[DLX1]] | B | DLX1 activity raises KLHL42's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 1.30× lower at baseline in the lines without DLX1 | 0.066 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |
| [[HDAC6]] | B | HDAC6 activity raises KLHL42's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LRP1]] | C | LRP1 activity lowers KLHL42's level | lines that do not express LRP1 (3) vs lines expressing it (47) | 1.37× higher at baseline in the lines without LRP1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OAF, TGFBR3, OSBPL3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.805). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-6.2, 9.8); signed map (24.8, -27.1). **Vector** length 121, 32.8% of its response variance represented; |z| ≥ 3 in 1,145 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +12.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +8.2 | +7.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +8.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.6 | +8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.2 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.4 | +6.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.1 | +5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.8 | +8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +6.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.8 | +4.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -8.4 | -30.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -8.1 | -30.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -8.0 | -24.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.2 | -12.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.4 | -8.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -5.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -5.2 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.9 | -1.5 |
|  | [[Daidzin (drug)]] 5 µM |  | -1.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 42 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.22 — chr12:27,780,048-27,803,040 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1340, Ctb9; previously KLHDC5 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2K6](https://www.uniprot.org/uniprotkb/Q9P2K6) (Kelch-like protein 42):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complex required for mitotic progression and cytokinesis. The BCR(KLHL42) E3 ubiquitin ligase complex mediates the ubiquitination and subsequent degradation of KATNA1. Involved in microtubule dynamics throughout mitosis.

**Summary**, from NCBI Gene [57542](https://www.ncbi.nlm.nih.gov/gene/57542):

> Contributes to ubiquitin-protein transferase activity. Involved in proteasome-mediated ubiquitin-dependent protein catabolic process; protein polyubiquitination; and regulation of microtubule-based process. Part of Cul3-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29252](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29252) · Entrez [57542](https://www.ncbi.nlm.nih.gov/gene/57542) · UniProt [Q9P2K6](https://www.uniprot.org/uniprotkb/Q9P2K6) · Ensembl [ENSG00000087448](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087448)

## Data

Gene col 1504: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1504); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1504, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1504]; `tensor/DDL_lfc|DDL_z.npy` [1504]; `embed/gene_vectors.npy` [1504]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1504 or target_col == 1504). Every well: [[KLHL42 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL42.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
