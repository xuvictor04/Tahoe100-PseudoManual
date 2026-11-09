---
symbol: "HDAC6"
type: "gene"
col: 1724
ensembl_id: "ENSG00000094631"
name: "histone deacetylase 6"
location: "Xp11.23"
module: 40
arm: "+"
pooled_cpm: 29.91
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 27
n_dd_up_clean: 0
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 0
direction_downstream: 1739
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# HDAC6

*histone deacetylase 6* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 1.24× (z +4.6, q 0.003, up in 13 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 3.00×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.417× (z -18.2, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OS9]] (+0.63, fdr 9e-06), [[SEPTIN2]] (+0.63, fdr 1e-05), [[ALDH6A1]] (+0.61, fdr 8e-06); moves opposite to [[RPF1]] (-0.60, fdr 1e-05), [[RRS1]] (-0.59, fdr 1e-05), [[TRMT10C]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1,739 go from it, the strongest it → [[ABRACL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1724.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 3.00×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.24×** | +4.6 | 0.003 | 13/48 (A-427, HOP62, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.23×** | +4.3 | 0.004 | 21/44 (A-427, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.2 | 0.004 | 15/47 (RKO, SK-MEL-2, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.19× | +3.7 | 0.027 | 13/48 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.5 | 0.045 | 13/35 (A-172, AsPC-1, …) | two highest doses | composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.12× | +3.3 | 0.10 | 6/48 (SW480, KATO III, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.15 | 11/48 (CHP-212, HCT15, …) | inconsistent across doses |  |
| [[BI-3406 (drug)]] 5 µM |  | 1.32× | +3.0 | 0.19 | 8/47 (SK-MEL-2, HOP62, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1724.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.417×** | -18.2 | 0e+00 | 41/47 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.609×** | -14.6 | 1e-45 | 31/47 (HT-29, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.560×** | -12.0 | 4e-31 | 38/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.562×** | -11.5 | 1e-28 | 37/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.591×** | -10.9 | 1e-25 | 41/48 (C-33 A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.616×** | -10.1 | 8e-22 | 35/48 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.626×** | -9.7 | 2e-20 | 32/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.433×** | -9.1 | 5e-18 | 36/48 (H4, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.653×** | -8.9 | 5e-17 | 37/48 (A-427, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.666×** | -8.4 | 2e-15 | 30/48 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.667×** | -8.4 | 2e-15 | 30/48 (SW480, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.723×** | -6.7 | 8e-10 | 27/48 (KATO III, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.546×** | -6.6 | 2e-09 | 30/46 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.733×** | -6.5 | 4e-09 | 25/48 (HCT15, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.809×** | -6.2 | 2e-08 | 26/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.729×** | -6.2 | 2e-08 | 24/48 (KATO III, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1724. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 47.2 | 0 | 5 | — | [[Harringtonine (drug)]] 0.5 µM 0.378× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 34.7 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.342× (z -9.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.489× (z -9.1) |
| [[H4 (line)]] | wt | 45.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0801× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 24.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -11.5) |
| [[SNU-423 (line)]] | alt | 52.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -12.3) |
| [[A-172 (line)]] | wt | 26.8 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.355× (z -8.8) |
| [[HOP62 (line)]] | alt | 27.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -17.5) |
| [[HS-578T (line)]] | alt | 34.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -9.9) |
| [[HT-29 (line)]] | alt | 39.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -18.5) |
| [[KATO III (line)]] | alt | 42.0 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.363× (z -8.6) |
| [[LoVo (line)]] | wt | 21.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.326× (z -9.8) |
| [[LS 180 (line)]] | wt | 24.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.2) |
| [[SNU-1 (line)]] | wt | 26.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -10.2) |
| [[A-427 (line)]] | wt | 31.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.380× (z -8.9) |
| [[A498 (line)]] | wt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -10.7) |
| [[A549 (line)]] | wt | 31.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -10.4) |
| [[C-33 A (line)]] | alt | 34.9 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.214× (z -10.2) |
| [[COLO 205 (line)]] | alt | 32.6 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.230× (z -9.4) |
| [[HCT15 (line)]] | alt | 49.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 22.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.00× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 42.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.340× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 26.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -10.4) |
| [[J82 (line)]] | alt | 27.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 13.3 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.264× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 42.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.339× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 20.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -12.6) |
| [[NCI-H23 (line)]] | alt | 25.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -13.0) |
| [[RPMI-7951 (line)]] | alt | 37.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.243× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.185× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[SW 900 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.277× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW48 (line)]] | wt | 13.3 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0819× (z -9.7) |
| [[AN3 CA (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1724), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OS9]] | +0.63 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[SEPTIN2]] | +0.63 | +0.67 / +0.56 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium |
| [[ALDH6A1]] | +0.61 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[DCAF11]] | +0.61 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[AP2A1]] | +0.60 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[LMAN2]] | +0.59 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[RAB5B]] | +0.58 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[TMEM50B]] | +0.58 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[KDELR1]] | +0.58 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[TULP3]] | +0.57 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[CALR]] | +0.56 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[ODF2]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPF1]] | -0.60 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[RRS1]] | -0.59 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[TRMT10C]] | -0.58 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[NDUFAF4]] | -0.57 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[BICD1]] | -0.56 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[PCNX2]] | -0.56 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[BRIX1]] | -0.55 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[PAK1IP1]] | -0.55 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[REXO4]] | -0.55 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[ADO]] | -0.55 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[IRS1]] | -0.53 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[FADD]] | -0.52 | -0.49 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1,739 arrows, 1,739 of them with an alert ⚠; grade A 0, B 1,739, C 0. Shown: the 12 strongest; 1,727 more arrows (1,727 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABRACL]] | B | HDAC6 activity raises ABRACL's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ACTR5]] | B | HDAC6 activity lowers ACTR5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ANKRD10]] | B | HDAC6 activity raises ANKRD10's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ANKS3]] | B | HDAC6 activity lowers ANKS3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ARAP2]] | B | HDAC6 activity raises ARAP2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ARF1]] | B | HDAC6 activity raises ARF1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ARPP19]] | B | HDAC6 activity raises ARPP19's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[BAIAP2L2]] | B | HDAC6 activity raises BAIAP2L2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[BTG3]] | B | HDAC6 activity raises BTG3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CABIN1]] | B | HDAC6 activity lowers CABIN1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CARD19]] | B | HDAC6 activity lowers CARD19's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CD63]] | B | HDAC6 activity raises CD63's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.451). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-13.9, -19.1); signed map (-58.1, 6.7). **Vector** length 92.5, 20.6% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +3.1 | -3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.0 | +3.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +4.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.0 | +2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -18.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.9 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -8.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.9 | -5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -6.6 |

## What is on record

|  |  |
|---|---|
| Name | histone deacetylase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:48,801,377-48,824,982 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0901, JM21, HD6, FLJ16239, PPP1R90, KDAC6 |
| Gene groups (HGNC) | Ring finger proteins; Protein phosphatase 1 regulatory subunits; Histone deacetylases, class IIB |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 31 pathways, smallest: Chaperone Mediated Autophagy; RUNX2 regulates osteoblast differentiation; HSF1 activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBN7](https://www.uniprot.org/uniprotkb/Q9UBN7) (Protein deacetylase HDAC6):

> Deacetylates a wide range of non-histone substrates. Plays a central role in microtubule-dependent cell motility by mediating deacetylation of tubulin. Required for cilia disassembly via deacetylation of alpha-tubulin. Alpha-tubulin deacetylation results in destabilization of dynamic microtubules (By similarity). Promotes deacetylation of CTTN, leading to actin polymerization, promotion of autophagosome-lysosome fusion and completion of autophagy. Deacetylates SQSTM1. Deacetylates …

**Summary**, from NCBI Gene [10013](https://www.ncbi.nlm.nih.gov/gene/10013):

> Histones play a critical role in transcriptional regulation, cell cycle progression, and developmental events. Histone acetylation/deacetylation alters chromosome structure and affects transcription factor access to DNA. The protein encoded by this gene belongs to class II of the histone deacetylase/acuc/apha family. It contains an internal duplication of two catalytic domains which appear to function independently of each other. This protein possesses histone deacetylase activity and represses …

**Accessions** — [HGNC:14064](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14064) · Entrez [10013](https://www.ncbi.nlm.nih.gov/gene/10013) · UniProt [Q9UBN7](https://www.uniprot.org/uniprotkb/Q9UBN7) · Ensembl [ENSG00000094631](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000094631)

## Data

Gene col 1724: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1724); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1724, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1724]; `tensor/DDL_lfc|DDL_z.npy` [1724]; `embed/gene_vectors.npy` [1724]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1724 or target_col == 1724). Every well: [[HDAC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDAC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
