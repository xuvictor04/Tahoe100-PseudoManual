---
symbol: "EHMT1"
type: "gene"
col: 11166
ensembl_id: "ENSG00000181090"
name: "euchromatic histone lysine methyltransferase 1"
location: "9q34.3"
module: 36
arm: "+"
pooled_cpm: 175.19
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# EHMT1

*euchromatic histone lysine methyltransferase 1* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.58× (z +4.9, q 5e-04, up in 28 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H1573 2.39×, SW48 2.28×, COLO 205 1.73×; ⚠ cell-cycle shift, explains ~93% of this change); [[TAK-901 (drug)]] 5 µM in 3 lines (COLO 205 7.30×, LS 180 3.99×, SW480 2.85×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (COLO 205 2.57×; ⚠ cell-cycle shift, explains ~0% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (LS 180 3.65×).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.494× (z -13.8, q 1e-40, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.635× (z -9.3, q 3e-18, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS13D]] (+0.67, fdr 7e-06), [[TRAPPC10]] (+0.66, fdr 7e-06), [[UBE3C]] (+0.64, fdr 7e-06); moves opposite to [[BTN2A2]] (-0.56, fdr 9e-06), [[SDCBP]] (-0.56, fdr 1e-05), [[FAM117A]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MTHFD1L]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11166.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H1573 2.39×, SW48 2.28×, COLO 205 1.73×; ⚠ cell-cycle shift, explains ~93% of this change); [[TAK-901 (drug)]] 5 µM in 3 lines (COLO 205 7.30×, LS 180 3.99×, SW480 2.85×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (COLO 205 2.57×; ⚠ cell-cycle shift, explains ~0% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (LS 180 3.65×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.58×** | +4.9 | 5e-04 | 28/49 (COLO 205, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +4.7 | 6e-04 | 31/48 (LS 180, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 1.18× | +3.4 | 0.11 | 19/48 (AsPC-1, SNU-423, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.16× | +3.0 | 0.29 | 15/48 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.29 | 21/47 (C32, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11166.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.494×** | -13.8 | 1e-40 | 39/44 (SHP-77, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.548×** | -12.3 | 4e-32 | 42/49 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.575×** | -10.4 | 3e-23 | 38/45 (C-33 A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.635×** | -9.3 | 3e-18 | 34/48 (C32, RKO, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.736×** | -8.8 | 1e-16 | 40/48 (Panc 03.27, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.672×** | -7.8 | 7e-13 | 33/48 (NCI-H460, A498, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.707×** | -6.8 | 1e-09 | 36/47 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.802×** | -6.3 | 2e-08 | 31/48 (LOX-IMVI, J82, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.754×** | -5.7 | 6e-07 | 35/48 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.756×** | -5.7 | 7e-07 | 30/48 (SW1417, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.769×** | -5.4 | 4e-06 | 35/49 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | 0.854× | -4.5 | 3e-04 | 25/48 (A498, A-172, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.798×** | -4.4 | 5e-04 | 26/50 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.810×** | -4.3 | 7e-04 | 28/48 (Hs 766T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.814×** | -4.2 | 0.001 | 24/48 (SW1417, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.850× | -3.3 | 0.028 | 17/48 (AsPC-1, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11166. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 198 | 0 | 9 (9 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.302× (z -18.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 203 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -21.9) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.531× (z -8.9) |
| [[HS-578T (line)]] | alt | 122 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -19.2) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.424× (z -11.4) |
| [[A549 (line)]] | wt | 218 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -14.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 149 | 0 | 7 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.360× (z -13.2) |
| [[SK-MEL-2 (line)]] | alt | 148 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.495× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 206 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -11.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 215 | 0 | 6 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.296× (z -16.0) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 163 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.563× (z -11.1) |
| [[A498 (line)]] | wt | 160 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -23.7) ⚠ cell-cycle shift, explains ~93% of this change |
| [[J82 (line)]] | alt | 238 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -15.4) ⚠ cell-cycle shift, explains ~93% of this change |
| [[NCI-H1573 (line)]] | alt | 157 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +17.4) ⚠ cell-cycle shift, explains ~93% of this change | [[Dinaciclib (drug)]] 5 µM 0.350× (z -14.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 188 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 2.85× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.514× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.653× (z -10.0) |
| [[COLO 205 (line)]] | alt | 152 | 4 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.30× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 151 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.413× (z -11.9) |
| [[HT-29 (line)]] | alt | 207 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -11.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 122 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -14.3) ⚠ cell-cycle shift, explains ~93% of this change |
| [[LoVo (line)]] | wt | 192 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.661× (z -8.7) |
| [[SNU-1 (line)]] | wt | 216 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.511× (z -11.3) |
| [[SW1417 (line)]] | alt | 201 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -12.6) ⚠ cell-cycle shift, explains ~93% of this change |
| [[AN3 CA (line)]] | alt | 249 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -11.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 294 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -20.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 130 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.241× (z -17.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 284 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.287× (z -15.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.368× (z -13.2) |
| [[SHP-77 (line)]] | alt | 196 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.517× (z -9.1) |
| [[A-427 (line)]] | wt | 137 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.240× (z -19.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[AsPC-1 (line)]] | alt | 208 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.457× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.581× (z -9.0) |
| [[Hs 766T (line)]] | wt | 132 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.524× (z -10.1) |
| [[LS 180 (line)]] | wt | 190 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.99× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 119 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.437× (z -10.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.565× (z -10.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 158 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.3) ⚠ cell-cycle shift, explains ~93% of this change | [[Dinaciclib (drug)]] 5 µM 0.409× (z -9.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 214 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -16.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 212 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -11.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 247 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.549× (z -8.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 134 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.440× (z -8.6) ⚠ toxic |
| [[KATO III (line)]] | alt | 184 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.454× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 182 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.538× (z -8.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 105 | 0 | 1 | — | [[Aprepitant (drug)]] 5 µM 0.0541× (z -10.8) |
| [[BT-474 (line)]] | alt | 471 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 166 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 121 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11166), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS13D]] | +0.67 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[TRAPPC10]] | +0.66 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[UBE3C]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[HIRA]] | +0.63 | +0.65 / +0.66 | both halves | 7e-06 | pathway: Cellular Senescence |
| [[LETM1]] | +0.63 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[EMC8]] | +0.63 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[MTOR]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 | pathway: Regulation of TP53 Activity |
| [[SPECC1L]] | +0.61 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[MFSD14CP-1]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[HERC2]] | +0.59 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[POLR3E]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[KIAA0232]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN2A2]] | -0.56 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[SDCBP]] | -0.56 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[FAM117A]] | -0.55 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.55 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[BTN2A3P]] | -0.53 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[BPNT1]] | -0.53 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[KLHL32]] | -0.53 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[PREPL]] | -0.53 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[CGNL1]] | -0.50 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[ARMCX3]] | -0.49 | -0.47 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTHFD1L]] | C | MTHFD1L activity raises EHMT1's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 1.87× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.689). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-6.8, -32.5); signed map (-17.7, -52.7). **Vector** length 120, 41.8% of its response variance represented; |z| ≥ 3 in 1,174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +1.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.5 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.8 | -8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.4 | -5.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -7.3 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.9 | -6.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -6.8 | -7.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.1 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -9.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -2.3 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | euchromatic histone lysine methyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,618,992-137,870,016 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Eu-HMTase1, FLJ12879, KIAA1876, bA188C12.1, KMT1D, FLJ40292, GLP; previously EHMT1-IT1 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Histone lysine methyltransferases; SET domain containing |
| Reactome | 15 pathways, smallest: Regulation of TP53 Activity through Methylation; Regulation of endogenous retroelements by the Human Silencing Hub (HUSH) complex; Transcriptional Regulation by E2F6 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9B1](https://www.uniprot.org/uniprotkb/Q9H9B1) (Histone-lysine N-methyltransferase EHMT1):

> Histone methyltransferase that specifically mono-, di- and trimethylates 'Lys-9' of histone H3 (H3K9me1, H3K9me2 and H3K9me3, respectively) in euchromatin. H3K9me represents a specific tag for epigenetic transcriptional repression by recruiting HP1 proteins to methylated histones. Also weakly methylates 'Lys-27' of histone H3 (H3K27me). Also required for DNA methylation, the histone methyltransferase activity is not required for DNA methylation, suggesting that these 2 activities function …

**Summary**, from NCBI Gene [79813](https://www.ncbi.nlm.nih.gov/gene/79813):

> The protein encoded by this gene is a histone methyltransferase that methylates the lysine-9 position of histone H3. This action marks the genomic region packaged with these methylated histones for transcriptional repression. This protein may be involved in the silencing of MYC- and E2F-responsive genes and therefore could play a role in the G0/G1 cell cycle transition. Defects in this gene are a cause of chromosome 9q subtelomeric deletion syndrome (9q-syndrome, also known as Kleefstra …

**Accessions** — [HGNC:24650](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24650) · Entrez [79813](https://www.ncbi.nlm.nih.gov/gene/79813) · UniProt [Q9H9B1](https://www.uniprot.org/uniprotkb/Q9H9B1) · Ensembl [ENSG00000181090](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181090)

## Data

Gene col 11166: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11166); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11166, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11166]; `tensor/DDL_lfc|DDL_z.npy` [11166]; `embed/gene_vectors.npy` [11166]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11166 or target_col == 11166). Every well: [[EHMT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EHMT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
