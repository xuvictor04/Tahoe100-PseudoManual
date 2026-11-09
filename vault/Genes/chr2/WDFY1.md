---
symbol: "WDFY1"
type: "gene"
col: 1427
ensembl_id: "ENSG00000085449"
name: "WD repeat and FYVE domain containing 1"
location: "2q36.1"
module: 30
arm: "+"
pooled_cpm: 132.81
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# WDFY1

*WD repeat and FYVE domain containing 1* — 2q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.39× (z +9.9, q 2e-20, up in 43 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 5 lines (SW480 3.35×, NCI-H2030 4.36×, RPMI-7951 7.56×, PANC-1 2.68×, …); [[PH-797804 (drug)]] 5 µM in 1 line (C32 4.68×); [[Trametinib (drug)]] 5 µM in 1 line (C32 2.08×; ⚠ cell-cycle shift, explains ~58% of this change); [[Binimetinib (drug)]] 5 µM in 1 line (C32 2.00×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.557× (z -18.0, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LDAF1]] (+0.62, fdr 1e-05), [[BCAS4]] (+0.61, fdr 1e-05), [[CYRIA]] (+0.61, fdr 3e-05); moves opposite to [[DDX5]] (-0.58, fdr 4e-05), [[SPRY3]] (-0.57, fdr 6e-05), [[MSANTD2]] (-0.54, fdr 6e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1427.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 5 lines (SW480 3.35×, NCI-H2030 4.36×, RPMI-7951 7.56×, PANC-1 2.68×, …); [[PH-797804 (drug)]] 5 µM in 1 line (C32 4.68×); [[Trametinib (drug)]] 5 µM in 1 line (C32 2.08×; ⚠ cell-cycle shift, explains ~58% of this change); [[Binimetinib (drug)]] 5 µM in 1 line (C32 2.00×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.39×** | +9.9 | 2e-20 | 43/49 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +5.8 | 2e-06 | 32/48 (C32, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.24×** | +4.6 | 7e-04 | 23/48 (A498, CFPAC-1, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.6 | 0.043 | 9/49 (A498, NCI-H1792, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.6 | 0.043 | 11/48 (C32, AsPC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.21 | 14/48 (HT-29, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1427.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.557×** | -18.0 | 0e+00 | 44/49 (LS 180, AsPC-1, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.602×** | -10.6 | 8e-24 | 38/48 (SNU-423, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.610×** | -10.3 | 1e-22 | 39/50 (LS 180, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.794×** | -7.1 | 2e-10 | 27/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.711×** | -6.8 | 8e-10 | 30/45 (NCI-H460, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.734×** | -6.7 | 2e-09 | 32/48 (A498, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.739×** | -6.6 | 4e-09 | 30/48 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.781×** | -5.4 | 6e-06 | 30/48 (A498, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.783×** | -5.3 | 7e-06 | 24/49 (A-172, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.858× | -4.7 | 2e-04 | 25/48 (LoVo, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.826×** | -4.1 | 0.002 | 21/48 (RPMI-7951, AsPC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.827×** | -4.0 | 0.003 | 22/48 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.845× | -3.7 | 0.011 | 20/48 (NCI-H1573, LoVo, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 0.841× | -3.6 | 0.012 | 21/44 (SNU-1, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.847× | -3.6 | 0.012 | 22/48 (A498, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.848× | -3.6 | 0.013 | 18/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.852× | -3.4 | 0.018 | 19/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.856× | -3.4 | 0.023 | 11/49 (NCI-H460, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1427. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 197 | 4 (1 ⚠) | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.68× (z +9.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -12.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -11.3) |
| [[A-172 (line)]] | wt | 262 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.7) ⚠ cell-cycle shift, explains ~52% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -12.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -10.8) |
| [[HOP62 (line)]] | alt | 165 | 0 | 5 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.492× (z -14.2) |
| [[hTERT-HPNE (line)]] | wt | 247 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -12.6) |
| [[LS 180 (line)]] | wt | 139 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -16.6) |
| [[SNU-423 (line)]] | alt | 417 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 92.5 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -10.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -9.5) |
| [[A498 (line)]] | wt | 179 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.455× (z -10.9) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 123 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -16.2) |
| [[HEC-1-A (line)]] | alt | 118 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -15.4) |
| [[LoVo (line)]] | wt | 81.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -15.4) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.655× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 194 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.415× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.476× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 119 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -10.5) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 108 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 152 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.56× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -10.0) |
| [[SW 900 (line)]] | alt | 185 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -11.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -10.5) |
| [[SW480 (line)]] | alt | 90.4 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.35× (z +10.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Hs 766T (line)]] | wt | 176 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -12.2) |
| [[HT-29 (line)]] | alt | 107 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -13.5) |
| [[MIA PaCa-2 (line)]] | alt | 86.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 88.5 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.36× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -9.8) |
| [[PANC-1 (line)]] | alt | 106 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 2.68× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -15.0) |
| [[A549 (line)]] | wt | 181 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -15.0) |
| [[AN3 CA (line)]] | alt | 155 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -8.7) |
| [[C-33 A (line)]] | alt | 98.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -10.2) ⚠ cell-cycle shift, explains ~52% of this change |
| [[CFPAC-1 (line)]] | alt | 125 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -10.0) |
| [[HCT15 (line)]] | alt | 118 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 174 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -12.5) |
| [[HS-578T (line)]] | alt | 144 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.42× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 102 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -15.7) |
| [[NCI-H661 (line)]] | alt | 98.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 115 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -13.7) |
| [[SNU-1 (line)]] | wt | 72.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 96.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 82.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 83.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1427), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDAF1]] | +0.62 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[BCAS4]] | +0.61 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[CYRIA]] | +0.61 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[RRAGD]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[STX7]] | +0.59 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[ARL8B]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[TSPAN33]] | +0.57 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[RAD17]] | +0.56 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[TMEM185A]] | +0.56 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[MAPK3]] | +0.55 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[SDHB]] | +0.55 | +0.56 / +0.38 | both halves | 6e-05 |  |
| [[RTN4RL2]] | +0.54 | +0.49 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX5]] | -0.58 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[SPRY3]] | -0.57 | -0.63 / -0.39 | both halves | 6e-05 |  |
| [[MSANTD2]] | -0.54 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[SATB2]] | -0.51 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[HNRNPAB]] | -0.51 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[SNRPB]] | -0.50 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[P2RY11]] | -0.50 | -0.56 / -0.40 | both halves | 4e-05 |  |
| [[HNRNPA2B1]] | -0.50 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[RAB11B-AS1]] | -0.49 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[ERCC6L2]] | -0.48 | -0.57 / -0.29 | both halves | 2e-04 |  |
| [[STXBP5-AS1]] | -0.48 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[ATR]] | -0.48 | -0.50 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises WDFY1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ENTHD1]] | B | ENTHD1 activity raises WDFY1's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 1.47× lower at baseline in the lines without ENTHD1 | 0.022 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.524). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (8.1, -10.5); signed map (-26.8, -5.0). **Vector** length 118, 34.7% of its response variance represented; |z| ≥ 3 in 1,168 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.6 | +9.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.7 | +3.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +4.7 | +4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.6 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +5.8 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.9 | -7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -18.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.5 | -10.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.3 | -10.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -2.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.6 | -2.8 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -2.6 | -1.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.5 | -3.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat and FYVE domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.1 — chr2:223,855,716-223,945,357 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1435, FENS-1, WDF1, ZFYVE17 |
| Gene groups (HGNC) | Zinc fingers FYVE-type; WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWB7](https://www.uniprot.org/uniprotkb/Q8IWB7) (WD repeat and FYVE domain-containing protein 1):

> Positively regulates TLR3- and TLR4-mediated signaling pathways by bridging the interaction between TLR3 or TLR4 and TICAM1. Promotes TLR3/4 ligand-induced activation of transcription factors IRF3 and NF-kappa-B, as well as the production of IFN-beta and inflammatory cytokines.

**Summary**, from NCBI Gene [57590](https://www.ncbi.nlm.nih.gov/gene/57590):

> The protein encoded by this gene is a phosphatidylinositol 3-phosphate binding protein, which contains a FYVE zinc finger domain and multiple WD-40 repeat domains. When exogenously expressed, it localizes to early endosomes. Mutagenesis analysis demonstrates that this endosomal localization is mediated by the FYVE domain. [provided by RefSeq, Jan 2015]

**Accessions** — [HGNC:20451](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20451) · Entrez [57590](https://www.ncbi.nlm.nih.gov/gene/57590) · UniProt [Q8IWB7](https://www.uniprot.org/uniprotkb/Q8IWB7) · Ensembl [ENSG00000085449](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085449)

## Data

Gene col 1427: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1427); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1427, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1427]; `tensor/DDL_lfc|DDL_z.npy` [1427]; `embed/gene_vectors.npy` [1427]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1427 or target_col == 1427). Every well: [[WDFY1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDFY1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
