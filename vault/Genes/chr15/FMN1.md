---
symbol: "FMN1"
type: "gene"
col: 14578
ensembl_id: "ENSG00000248905"
name: "formin 1"
location: "15q13.3"
module: 106
arm: "+"
pooled_cpm: 195.29
n_lines_expressing: 33
n_dd_up: 3
n_dd_down: 29
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 6
direction_downstream: 6
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# FMN1

*formin 1* — 15q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.43× (z +8.0, q 7e-13, up in 19 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.559× (z -13.0, q 1e-35, down in 26 of 31 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.449× (z -12.6, q 7e-34, down in 28 of 31 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00511]] (+0.54, fdr 4e-05), [[TRIB1]] (+0.52, fdr 3e-05), [[CERS6]] (+0.52, fdr 8e-05); moves opposite to [[MFSD8]] (-0.53, fdr 7e-05), [[TSTD3]] (-0.51, fdr 4e-05), [[MACROH2A2]] (-0.49, fdr 1e-04).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[FKBP9P1-1]] → it (grade B ⚠); 6 go from it, the strongest it → [[C1QTNF3-AMACR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14578.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +8.0 | 7e-13 | 19/31 (A549, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +5.4 | 2e-05 | 20/32 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +4.5 | 0.001 | 14/31 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.18× | +3.7 | 0.032 | 10/31 (NCI-H23, HOP62, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.30× | +3.2 | 0.14 | 14/31 (SHP-77, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.22× | +3.2 | 0.14 | 11/31 (hTERT-HPNE, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 16 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14578.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.559×** | -13.0 | 1e-35 | 26/31 (COLO 205, CHP-212, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.449×** | -12.6 | 7e-34 | 28/31 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.468×** | -11.5 | 3e-28 | 26/30 (CHP-212, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.523×** | -10.2 | 3e-22 | 27/31 (SW480, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.652×** | -9.5 | 2e-19 | 27/32 (CHP-212, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.577×** | -8.7 | 4e-16 | 26/31 (CHP-212, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.574×** | -8.4 | 4e-15 | 23/31 (SW 900, SNU-423, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.652×** | -6.7 | 1e-09 | 25/31 (SW480, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.653×** | -6.7 | 1e-09 | 23/31 (SW480, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.521×** | -5.4 | 5e-06 | 19/32 (COLO 205, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.722×** | -5.1 | 2e-05 | 17/31 (PANC-1, SW1417, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.817×** | -4.5 | 4e-04 | 18/32 (CFPAC-1, C32, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.588×** | -4.4 | 5e-04 | 15/26 (Panc 03.27, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | **0.757×** | -4.4 | 5e-04 | 19/31 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.727×** | -4.3 | 6e-04 | 16/31 (SW480, SW 900, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.593×** | -4.3 | 6e-04 | 17/31 (PANC-1, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.594×** | -4.3 | 6e-04 | 17/31 (COLO 205, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.699×** | -4.0 | 0.002 | 17/31 (PANC-1, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.781×** | -3.9 | 0.003 | 17/31 (PANC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 5 µM |  | 0.844× | -3.8 | 0.005 | 14/32 (LOX-IMVI, SW 900, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.801×** | -3.5 | 0.012 | 16/31 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.801×** | -3.4 | 0.019 | 15/31 (A498, KATO III, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -3.3 | 0.020 | 21/31 (A-427, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.823×** | -3.0 | 0.047 | 15/31 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.694×** | -3.0 | 0.052 | 17/31 (PANC-1, COLO 205, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14578. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 455 | 0 | 14 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -13.9) |
| [[PANC-1 (line)]] | alt | 150 | 0 | 11 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.336× (z -12.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.351× (z -12.1) |
| [[SW480 (line)]] | alt | 178 | 3 (2 ⚠) | 8 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 5.01× (z +20.2) | [[Digitoxin (drug)]] 5 µM 0.223× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -18.3) |
| [[COLO 205 (line)]] | alt | 438 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -25.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -15.3) |
| [[SK-MEL-2 (line)]] | alt | 3,079 | 2 (1 ⚠) | 8 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.58× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -19.5) |
| [[CHP-212 (line)]] | wt | 1,856 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -22.1) |
| [[C32 (line)]] | wt | 1,825 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 6.81× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 153 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -15.8) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -14.2) |
| [[NCI-H1573 (line)]] | alt | 118 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -19.8) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -13.3) |
| [[A549 (line)]] | wt | 50.4 | 3 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.57× (z +11.7) | [[Digitoxin (drug)]] 0.5 µM 0.267× (z -10.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -9.2) |
| [[H4 (line)]] | wt | 135 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.153× (z -13.1) |
| [[SNU-423 (line)]] | alt | 222 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -16.1) |
| [[SW 900 (line)]] | alt | 178 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -18.6) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.330× (z -9.7) |
| [[SW1417 (line)]] | alt | 217 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.07× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -12.8) |
| [[A-427 (line)]] | wt | 85.9 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 105 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.79× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -12.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -10.6) |
| [[SHP-77 (line)]] | alt | 178 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -13.2) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -11.7) |
| [[SW48 (line)]] | wt | 158 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -11.3) |
| [[HT-29 (line)]] | alt | 152 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -11.4) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.313× (z -9.6) |
| [[KATO III (line)]] | alt | 104 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -11.9) |
| [[LoVo (line)]] | wt | 164 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.326× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 94.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -10.6) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.243× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 244 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.279× (z -11.3) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 79.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -10.6) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A-172 (line)]] | wt | 40.7 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.7 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 38.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 44.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 22.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 30.4 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 21.1 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 38.6 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.9 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 43.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.9 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 37.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 278 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.6 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 21.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 272 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.3 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 17.0 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 153 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 343 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14578), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00511]] | +0.54 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[TRIB1]] | +0.52 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[CERS6]] | +0.52 | +0.37 / +0.50 | both halves | 8e-05 |  |
| [[NRG3]] | +0.50 | +0.17 / +0.54 | ⚠ one half (not replicated) | 0.001 |  |
| [[RAPGEF5]] | +0.49 | +0.44 / +0.40 | both halves | 5e-05 |  |
| [[VMP1]] | +0.48 | +0.40 / +0.41 | both halves | 5e-05 |  |
| [[AKAP13]] | +0.48 | +0.44 / +0.37 | both halves | 9e-05 |  |
| [[DUSP2]] | +0.47 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[LINC00540]] | +0.47 | +0.38 / +0.37 | both halves | 8e-05 |  |
| [[SNED1]] | +0.47 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[HEY1]] | +0.47 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[DNAJB1]] | +0.46 | +0.27 / +0.46 | both halves | 3e-04 |  |
| [[CACNA1D]] | +0.46 | +0.38 / +0.48 | both halves | 6e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD8]] | -0.53 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[TSTD3]] | -0.51 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[MACROH2A2]] | -0.49 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[KLHL22]] | -0.48 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[INTS8]] | -0.48 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[ZNF563]] | -0.46 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[DDX59]] | -0.46 | -0.23 / -0.51 | both halves | 5e-04 |  |
| [[LRRC27]] | -0.45 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[POMT1]] | -0.45 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[ZNF25]] | -0.44 | -0.32 / -0.41 | both halves | 1e-04 |  |
| [[B4GALT4]] | -0.44 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[TRAPPC13]] | -0.44 | -0.38 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FKBP9P1-1]] | B | FKBP9P1-1 activity raises FMN1's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 2.63× lower at baseline in the lines without FKBP9P1-1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers FMN1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CACNA1D]] | B | CACNA1D activity raises FMN1's level | lines that do not express CACNA1D (23) vs lines expressing it (27) | 1.82× lower at baseline in the lines without CACNA1D | 0.062 | ⚠ within organs, on part of the lines; also absent: TESC, ENSG00000291189, CDX2; maybe low, not absent |
| [[MAML3]] | B | MAML3 activity raises FMN1's level | lines that do not express MAML3 (9) vs lines expressing it (41) | 3.23× lower at baseline in the lines without MAML3 | 0.068 | ⚠ within organs, on part of the lines; also absent: SOX4, GOLGA7B-DT, STEAP2-AS1 |
| [[RNF17]] | B | RNF17 activity raises FMN1's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 2.27× lower at baseline in the lines without RNF17 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD |
| [[SHROOM4]] | B | SHROOM4 activity raises FMN1's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 2.00× lower at baseline in the lines without SHROOM4 | 0.097 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1QTNF3-AMACR]] | B | FMN1 activity raises C1QTNF3-AMACR's level | lines that do not express FMN1 (17) vs lines expressing it (33) | 1.41× lower at baseline in the lines without FMN1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000278266, LINC02405, ENSG00000286016; maybe low, not absent |
| [[LINC00511]] | B | FMN1 activity raises LINC00511's level | lines that do not express FMN1 (17) vs lines expressing it (33) | 2.63× lower at baseline in the lines without FMN1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000278266, LINC02405, ENSG00000286016; maybe low, not absent |
| [[ADGRE2]] | B | FMN1 activity raises ADGRE2's level | lines that do not express FMN1 (17) vs lines expressing it (33) | 2.39× lower at baseline in the lines without FMN1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000278266, LINC02405, ENSG00000286016; maybe low, not absent |
| [[CACNA1D]] | B | FMN1 activity raises CACNA1D's level | lines that do not express FMN1 (17) vs lines expressing it (33) | 2.43× lower at baseline in the lines without FMN1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000278266, LINC02405, ENSG00000286016; maybe low, not absent |
| [[C1QTNF3]] | B | FMN1 activity raises C1QTNF3's level | lines that do not express FMN1 (17) vs lines expressing it (33) | 1.26× lower at baseline in the lines without FMN1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000278266, LINC02405, ENSG00000286016; maybe low, not absent |
| [[VMP1]] | B | FMN1 activity raises VMP1's level | lines that do not express FMN1 (17) vs lines expressing it (33) | 1.09× lower at baseline in the lines without FMN1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000278266, LINC02405, ENSG00000286016; maybe low, not absent |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.371). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.6, 36.2); signed map (9.7, 29.5). **Vector** length 82.8, 19.7% of its response variance represented; |z| ≥ 3 in 1,086 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | +5.8 | -3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +5.6 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | +5.0 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.7 | +3.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +0.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -0.1 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | formin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q13.3 — chr15:32,765,544-33,194,714 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP686C2281, FLJ45135, MGC125288, MGC125289; previously LD, FMN |
| Gene groups (HGNC) | Formins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68DA7](https://www.uniprot.org/uniprotkb/Q68DA7) (Formin-1):

> Plays a role in the formation of adherens junction and the polymerization of linear actin cables.

**Summary**, from NCBI Gene [342184](https://www.ncbi.nlm.nih.gov/gene/342184):

> This gene belongs to the formin homology family and encodes a protein that has a role in the formation of adherens junction and the polymerization of linear actin cables. The homologous gene in mouse is associated with limb deformity. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Sep 2015]

**Accessions** — [HGNC:3768](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3768) · Entrez [342184](https://www.ncbi.nlm.nih.gov/gene/342184) · UniProt [Q68DA7](https://www.uniprot.org/uniprotkb/Q68DA7) · Ensembl [ENSG00000248905](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248905)

## Data

Gene col 14578: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14578); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14578, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14578]; `tensor/DDL_lfc|DDL_z.npy` [14578]; `embed/gene_vectors.npy` [14578]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14578 or target_col == 14578). Every well: [[FMN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FMN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
