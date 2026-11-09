---
symbol: "XPO5"
type: "gene"
col: 4543
ensembl_id: "ENSG00000124571"
name: "exportin 5"
location: "6p21.1"
module: 18
arm: "+"
pooled_cpm: 39.94
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 2
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# XPO5

*exportin 5* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.18× (z +16.7, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.812× (z -6.3, q 1e-07, down in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~24% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 0.759× (z -4.2, q 0.004, down in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 3 lines (NCI-H23 0.718×, HOP62 0.730×, MIA PaCa-2 0.753×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.308×, C32 0.234×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.378×, C32 0.373×; ⚠ cell-cycle shift, explains ~0% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (COLO 205 0.0770×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2G2]] (+0.76, fdr 7e-06), [[MDN1]] (+0.73, fdr 7e-06), [[TCOF1]] (+0.71, fdr 7e-06); moves opposite to [[SAP18]] (-0.61, fdr 1e-05), [[KDM5A]] (-0.58, fdr 1e-05), [[ZNF490]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ADCY3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 21 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4543.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.18×** | +16.7 | 0e+00 | 45/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.04×** | +15.3 | 0e+00 | 43/47 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.98×** | +14.7 | 0e+00 | 43/47 (CFPAC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +14.7 | 0e+00 | 42/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.92×** | +14.0 | 2e-42 | 44/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.87×** | +13.4 | 6e-39 | 43/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.83×** | +13.0 | 1e-36 | 40/48 (NCI-H1792, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.83×** | +13.0 | 1e-36 | 40/48 (NCI-H1792, HOP62, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.65×** | +10.9 | 5e-26 | 36/47 (A-427, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +8.2 | 1e-14 | 33/48 (LS 180, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.44×** | +7.9 | 2e-13 | 34/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +7.8 | 2e-13 | 32/47 (A-172, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.44×** | +7.5 | 2e-12 | 32/47 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.96×** | +7.5 | 2e-12 | 37/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.28×** | +7.4 | 4e-12 | 24/48 (NCI-H2347, NCI-H1792, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +6.6 | 2e-09 | 25/48 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +6.3 | 1e-08 | 27/48 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.73×** | +6.2 | 2e-08 | 31/47 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.70×** | +5.9 | 8e-08 | 25/47 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.43×** | +5.4 | 1e-06 | 22/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.57×** | +5.1 | 8e-06 | 23/47 (SW 900, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +4.9 | 2e-05 | 20/48 (CFPAC-1, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4543.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 3 lines (NCI-H23 0.718×, HOP62 0.730×, MIA PaCa-2 0.753×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.308×, C32 0.234×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.378×, C32 0.373×; ⚠ cell-cycle shift, explains ~0% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (COLO 205 0.0770×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.812×** | -6.3 | 1e-07 | 24/48 (LS 180, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -5.2 | 7e-05 | 6/48 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.759×** | -4.2 | 0.004 | 16/48 (LoVo, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.852× | -3.5 | 0.075 | 9/48 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.855× | -3.4 | 0.086 | 16/48 (A-427, SNU-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4543. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 35.7 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.05× (z +12.9) | — |
| [[NCI-H23 (line)]] | alt | 68.0 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.72× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.0966× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 32.0 | 5 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.04× (z +10.7) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.55× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 23.3 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.13× (z +9.3) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[PANC-1 (line)]] | alt | 60.3 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.95× (z +15.0) | — |
| [[SW480 (line)]] | alt | 44.9 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.41× (z +13.1) | — |
| [[CFPAC-1 (line)]] | alt | 16.6 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 26.5 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.76× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 6.49× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 80.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[C32 (line)]] | wt | 35.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.234× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 45.3 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.52× (z +8.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[SNU-423 (line)]] | alt | 33.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 54.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.308× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 13.6 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0770× (z -9.7) |
| [[Hs 766T (line)]] | wt | 22.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.22× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 32.9 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.88× (z +8.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[LoVo (line)]] | wt | 31.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 76.3 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.76× (z +9.6) ⚠ unreliable plate only | — |
| [[NCI-H2030 (line)]] | alt | 49.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +17.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 72.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 46.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 103 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 77.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4543), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2G2]] | +0.76 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[MDN1]] | +0.73 | +0.74 / +0.71 | both halves | 7e-06 | STRING 469 |
| [[TCOF1]] | +0.71 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[PUS7]] | +0.71 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[PTGES2]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[CAD]] | +0.70 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[LETM1]] | +0.69 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[UBE3C]] | +0.69 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[QSOX2]] | +0.68 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[TMTC4]] | +0.67 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[CHID1]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[TTC13]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAP18]] | -0.61 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[KDM5A]] | -0.58 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[ZNF490]] | -0.57 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[SNRNP27]] | -0.56 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[SLU7]] | -0.56 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[AKAP9]] | -0.56 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[CIR1]] | -0.55 | -0.52 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | B | ADCY3 activity raises XPO5's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.44× lower at baseline in the lines without ADCY3 | 0.024 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[NCS1]] | B | NCS1 activity raises XPO5's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 1.99× lower at baseline in the lines without NCS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[WNK2]] | B | WNK2 activity raises XPO5's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.57× lower at baseline in the lines without WNK2 | 0.036 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.773). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.6, -38.1); signed map (-5.0, -52.8). **Vector** length 99.1, 27.1% of its response variance represented; |z| ≥ 3 in 1,185 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.54 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.1 | +15.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.8 | +3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.5 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | +4.4 | +6.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.2 | +4.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.9 | +6.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.8 | +7.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.5 | +5.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.4 | +5.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.6 | -0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -6.7 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | +2.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -4.4 | -3.4 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.7 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | +1.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.7 | -4.2 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | exportin 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,522,334-43,576,038 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1291 |
| Gene groups (HGNC) | Exportins |
| Reactome | 2 pathways, smallest: MicroRNA (miRNA) biogenesis; Gene Silencing by RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAV4](https://www.uniprot.org/uniprotkb/Q9HAV4) (Exportin-5):

> Mediates the nuclear export of proteins bearing a double-stranded RNA binding domain (dsRBD) and double-stranded RNAs (cargos). XPO5 in the nucleus binds cooperatively to the RNA and to the GTPase Ran in its active GTP-bound form. Proteins containing dsRBDs can associate with this trimeric complex through the RNA. Docking of this complex to the nuclear pore complex (NPC) is mediated through binding to nucleoporins. Upon transit of a nuclear export complex into the cytoplasm, hydrolysis of …

**Summary**, from NCBI Gene [57510](https://www.ncbi.nlm.nih.gov/gene/57510):

> This gene encodes a member of the karyopherin family that is required for the transport of small RNAs and double-stranded RNA-binding proteins from the nucleus to the cytoplasm. The encoded protein translocates cargo through the nuclear pore complex in a RanGTP-dependent process. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:17675](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17675) · Entrez [57510](https://www.ncbi.nlm.nih.gov/gene/57510) · UniProt [Q9HAV4](https://www.uniprot.org/uniprotkb/Q9HAV4) · Ensembl [ENSG00000124571](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124571)

## Data

Gene col 4543: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4543); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4543, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4543]; `tensor/DDL_lfc|DDL_z.npy` [4543]; `embed/gene_vectors.npy` [4543]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4543 or target_col == 4543). Every well: [[XPO5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XPO5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
