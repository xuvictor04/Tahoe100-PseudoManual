---
symbol: "NTPCR"
type: "gene"
col: 5757
ensembl_id: "ENSG00000135778"
name: "nucleoside-triphosphatase, cancer-related"
location: "1q42.2"
module: 220
arm: "+"
pooled_cpm: 23.57
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 21
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/220"]
generated_by: "tahoemap"
---

# NTPCR

*nucleoside-triphosphatase, cancer-related* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.37× (z +7.5, q 4e-11, up in 26 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.38× (z +5.5, q 6e-06, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.407× (z -21.5, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DTWD1]] (+0.69, fdr 7e-06), [[TP53TG1]] (+0.67, fdr 1e-05), [[TM7SF3]] (+0.62, fdr 1e-05); moves opposite to [[RIPK1]] (-0.56, fdr 1e-05), [[MYH15]] (-0.54, fdr 1e-05), [[LINC02798]] (-0.52, fdr 2e-05).
> It is in [[Module 220]], a single-armed module (Respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TP53]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5757.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.37×** | +7.5 | 4e-11 | 26/48 (A-427, C32, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +5.6 | 6e-06 | 19/33 (SNU-423, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +5.5 | 6e-06 | 25/48 (LoVo, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.8 | 3e-04 | 21/42 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.28×** | +4.2 | 0.003 | 18/42 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.26×** | +3.9 | 0.007 | 13/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.015 | 10/45 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.042 | 12/47 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.11 | 10/48 (A549, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | 1.42× | +3.0 | 0.11 | 3/45 (SW480, H4, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.19× | +3.0 | 0.11 | 8/47 (RKO, HT-29, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.19× | +3.0 | 0.11 | 3/47 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.11 | 10/48 (SK-MEL-2, SW480, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.0 | 0.11 | 19/48 (NCI-H460, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5757.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.407×** | -21.5 | 0e+00 | 44/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.564×** | -9.7 | 1e-19 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -8.6 | 1e-15 | 30/48 (NCI-H2030, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.626×** | -7.9 | 3e-13 | 33/47 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.652×** | -7.2 | 5e-11 | 30/47 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.670×** | -6.8 | 1e-09 | 27/46 (NCI-H460, RKO, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.680×** | -6.5 | 6e-09 | 25/47 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.720×** | -5.3 | 7e-06 | 23/47 (NCI-H460, COLO 205, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.764×** | -4.6 | 3e-04 | 18/47 (HCT15, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.768×** | -4.5 | 5e-04 | 19/47 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.607×** | -4.3 | 8e-04 | 18/45 (MIA PaCa-2, A498, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.775×** | -4.3 | 8e-04 | 20/47 (AN3 CA, SW480, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.794×** | -3.9 | 0.004 | 17/47 (NCI-H2030, A549, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.785×** | -3.9 | 0.005 | 17/48 (AN3 CA, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -3.6 | 0.013 | 16/46 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.768×** | -3.2 | 0.043 | 10/48 (MIA PaCa-2, PANC-1, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5757. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 39.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -13.9) |
| [[NCI-H460 (line)]] | wt | 40.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -22.9) |
| [[PANC-1 (line)]] | alt | 29.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -23.3) |
| [[NCI-H1573 (line)]] | alt | 32.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -16.2) |
| [[NCI-H2030 (line)]] | alt | 32.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -13.8) |
| [[SW480 (line)]] | alt | 21.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -16.5) |
| [[KATO III (line)]] | alt | 11.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 29.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -14.9) |
| [[SW 900 (line)]] | alt | 24.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -16.5) |
| [[A-427 (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -11.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 38.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -11.3) |
| [[C32 (line)]] | wt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 24.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -16.6) |
| [[HEC-1-A (line)]] | alt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -10.9) |
| [[HOP62 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -13.7) |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 22.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -12.8) |
| [[LS 180 (line)]] | wt | 30.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.307× (z -8.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[Panc 03.27 (line)]] | alt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -12.3) |
| [[RKO (line)]] | wt | 26.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -10.6) ⚠ cell-cycle shift, explains ~9% of this change |
| [[SNU-423 (line)]] | alt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -9.7) |
| [[SW1417 (line)]] | alt | 17.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -10.2) |
| [[A-172 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5757), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTWD1]] | +0.69 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[TP53TG1]] | +0.67 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[TM7SF3]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[TRIAP1]] | +0.60 | +0.37 / +0.72 | both halves | 8e-05 |  |
| [[EDA2R]] | +0.58 | +0.38 / +0.70 | both halves | 6e-05 |  |
| [[MRPL39]] | +0.57 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[CYFIP2]] | +0.57 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[PEX2]] | +0.56 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[ZMAT3]] | +0.55 | +0.38 / +0.67 | both halves | 7e-05 |  |
| [[TRIM32]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[PINCR]] | +0.54 | +0.39 / +0.65 | both halves | 6e-05 |  |
| [[NDUFAF8]] | +0.54 | +0.42 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIPK1]] | -0.56 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[MYH15]] | -0.54 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[LINC02798]] | -0.52 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[MYLK2]] | -0.51 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[BCL2L12]] | -0.51 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[IQCJ-SCHIP1]] | -0.51 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[TUBA1C]] | -0.50 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[MPP4]] | -0.50 | -0.50 / -0.43 | both halves | 4e-05 |  |
| [[POLG]] | -0.49 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[CHRNA10]] | -0.48 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[ZCCHC24]] | -0.47 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[CCDC18]] | -0.47 | -0.40 / -0.47 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | C | TP53 activity strengthens NTPCR's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 1.08× as strongly (z diff -0.32); strongest at Selinexor 5 µM: 1.19x vs 1.56x (z diff +2.5) | 0.873 over the table, 0.070 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 220]] — Respiratory electron transport; 11 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-4.0, -8.4); signed map (-25.6, -9.1). **Vector** length 87.2, 19.0% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +6.2 | +7.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | -2.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.9 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +4.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.3 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | -1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +0.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.0 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -21.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -4.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -0.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -0.2 |
|  | [[Cinacalcet (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | nucleoside-triphosphatase, cancer-related |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.2 — chr1:232,950,605-232,983,882 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13186, HCR-NTPase, THEP1; previously C1orf57 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSD7](https://www.uniprot.org/uniprotkb/Q9BSD7) (Cancer-related nucleoside-triphosphatase):

> Has nucleotide phosphatase activity towards ATP, GTP, CTP, TTP and UTP. Hydrolyzes nucleoside diphosphates with lower efficiency.

**Summary**, from NCBI Gene [84284](https://www.ncbi.nlm.nih.gov/gene/84284):

> The protein encoded by this gene is a non-specific nucleoside triphosphatase that is slow-acting in vitro. This gene is overexpressed in many tumor tissues, and while it is not essential for the cell, overexpression is cytotoxic. However, the cytotoxicity is not related to its triphosphatase activity. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:28204](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28204) · Entrez [84284](https://www.ncbi.nlm.nih.gov/gene/84284) · UniProt [Q9BSD7](https://www.uniprot.org/uniprotkb/Q9BSD7) · Ensembl [ENSG00000135778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135778)

## Data

Gene col 5757: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5757); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5757, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5757]; `tensor/DDL_lfc|DDL_z.npy` [5757]; `embed/gene_vectors.npy` [5757]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5757 or target_col == 5757). Every well: [[NTPCR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NTPCR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
