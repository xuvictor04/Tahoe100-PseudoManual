---
symbol: "DOCK7"
type: "gene"
col: 3811
ensembl_id: "ENSG00000116641"
name: "dedicator of cytokinesis 7"
location: "1p31.3"
module: 200
arm: "+"
pooled_cpm: 158.4
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/200"]
generated_by: "tahoemap"
---

# DOCK7

*dedicator of cytokinesis 7* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.58× (z +4.5, q 0.004, up in 32 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 1.82×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 2.08×; ⚠ cell-cycle shift, explains ~5% of this change).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.356× (z -21.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRSF1]] (+0.60, fdr 1e-05), [[DNAJC13]] (+0.58, fdr 1e-05), [[IARS2]] (+0.57, fdr 7e-06); moves opposite to [[TMEM104]] (-0.53, fdr 4e-05), [[RGP1]] (-0.52, fdr 3e-05), [[SLC25A44]] (-0.52, fdr 2e-05).
> It is in [[Module 200]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SUCLG2-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3811.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 1.82×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 2.08×; ⚠ cell-cycle shift, explains ~5% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.58×** | +4.5 | 0.004 | 32/49 (NCI-H460, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.054 | 24/47 (SW480, hTERT-HPNE, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 1.42× | +3.4 | 0.12 | 23/48 (NCI-H460, A-172, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.12 | 19/47 (RKO, SW480, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | 1.17× | +3.3 | 0.12 | 20/48 (PANC-1, NCI-H1573, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.17× | +3.1 | 0.17 | 13/47 (NCI-H23, RKO, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.16× | +3.1 | 0.17 | 16/49 (PANC-1, SW1417, …) | all doses, flat |  |
| [[Folic acid (drug)]] 5 µM |  | 1.11× | +3.0 | 0.17 | 0/48 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3811.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.356×** | -21.7 | 0e+00 | 47/48 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.360×** | -21.4 | 0e+00 | 47/48 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.512×** | -19.9 | 0e+00 | 41/48 (C32, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.431×** | -17.6 | 0e+00 | 47/48 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.534×** | -13.1 | 2e-37 | 45/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.617×** | -9.7 | 2e-20 | 43/47 (C32, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.654×** | -8.9 | 4e-17 | 45/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.678×** | -7.8 | 3e-13 | 32/48 (A-172, SK-MEL-2, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.691×** | -7.8 | 5e-13 | 41/48 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.791×** | -6.9 | 2e-10 | 29/49 (A549, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **0.743×** | -6.2 | 2e-08 | 30/49 (HEC-1-A, C32, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.744×** | -6.2 | 2e-08 | 32/48 (NCI-H661, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **0.764×** | -5.4 | 2e-06 | 25/44 (SNU-1, HEC-1-A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **0.769×** | -5.1 | 1e-05 | 28/45 (SNU-1, HEC-1-A, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.851× | -4.8 | 6e-05 | 20/48 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.795×** | -3.4 | 0.018 | 24/48 (hTERT-HPNE, HOP62, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.849× | -3.2 | 0.042 | 17/47 (C32, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.899× | -3.2 | 0.042 | 14/48 (A-172, SNU-1, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.904× | -3.0 | 0.069 | 3/49 (HT-29, Hs 766T, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.823×** | -2.9 | 0.085 | 13/49 (SW480, C32, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3811. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 361 | 0 | 18 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -28.6) |
| [[HEC-1-A (line)]] | alt | 261 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.323× (z -15.8) |
| [[RPMI-7951 (line)]] | alt | 276 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -17.8) |
| [[SK-MEL-2 (line)]] | alt | 285 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -23.4) |
| [[A-172 (line)]] | wt | 147 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -24.2) |
| [[NCI-H460 (line)]] | wt | 196 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -20.5) |
| [[SNU-423 (line)]] | alt | 251 | 0 | 9 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.355× (z -13.4) |
| [[A549 (line)]] | wt | 116 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -16.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.308× (z -15.6) |
| [[HCT15 (line)]] | alt | 255 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -15.4) |
| [[HS-578T (line)]] | alt | 302 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -22.4) |
| [[NCI-H1573 (line)]] | alt | 132 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -25.6) |
| [[SW480 (line)]] | alt | 109 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -20.4) |
| [[AN3 CA (line)]] | alt | 227 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0605× (z -22.6) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.303× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 145 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -20.0) |
| [[HOP62 (line)]] | alt | 176 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -22.3) |
| [[J82 (line)]] | alt | 177 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -23.9) |
| [[MIA PaCa-2 (line)]] | alt | 243 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -16.4) |
| [[A498 (line)]] | wt | 106 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -15.7) |
| [[LoVo (line)]] | wt | 118 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.422× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 173 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -23.0) |
| [[NCI-H23 (line)]] | alt | 177 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -27.6) |
| [[PANC-1 (line)]] | alt | 138 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -14.5) |
| [[SW 900 (line)]] | alt | 124 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.242× (z -17.1) |
| [[C-33 A (line)]] | alt | 197 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.314× (z -13.1) |
| [[H4 (line)]] | wt | 211 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.261× (z -12.4) |
| [[HepG2_C3A (line)]] | wt | 189 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.327× (z -13.1) |
| [[LS 180 (line)]] | wt | 148 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -15.3) |
| [[NCI-H2030 (line)]] | alt | 133 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.366× (z -13.1) |
| [[Panc 03.27 (line)]] | alt | 131 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.389× (z -12.5) |
| [[A-427 (line)]] | wt | 99.7 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.467× (z -9.8) |
| [[Hs 766T (line)]] | wt | 139 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.297× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 156 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.398× (z -10.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.421× (z -10.4) |
| [[RKO (line)]] | wt | 195 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.5) | [[Auranofin (drug)]] 5 µM 0.481× (z -9.1) |
| [[SHP-77 (line)]] | alt | 131 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.336× (z -14.7) |
| [[SNU-1 (line)]] | wt | 227 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[SW1417 (line)]] | alt | 171 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.439× (z -11.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.478× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 59.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.444× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 134 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.394× (z -9.3) |
| [[KATO III (line)]] | alt | 115 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.455× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 76.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.574× (z -9.9) |
| [[BT-474 (line)]] | alt | 76.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -14.2) |
| [[CHP-212 (line)]] | wt | 86.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.149× (z -10.8) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 81.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -9.2) |
| [[NCI-H661 (line)]] | alt | 168 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0994× (z -15.1) ⚠ transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW48 (line)]] | wt | 134 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.209× (z -15.7) |
| [[HT-29 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 113 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3811), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRSF1]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[DNAJC13]] | +0.58 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[IARS2]] | +0.57 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[PAM]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[BRCC3]] | +0.56 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[PARG]] | +0.56 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[TBC1D5]] | +0.55 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[ATG10]] | +0.55 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[ACAT1]] | +0.55 | +0.32 / +0.53 | both halves | 2e-04 |  |
| [[WDFY3]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[NT5DC1]] | +0.54 | +0.43 / +0.38 | both halves | 6e-05 |  |
| [[AK4]] | +0.54 | +0.57 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM104]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[RGP1]] | -0.52 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[SLC25A44]] | -0.52 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[TMEM243]] | -0.52 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[CCDC9]] | -0.52 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[BET1L]] | -0.52 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[WIPI1]] | -0.52 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[KIAA0513]] | -0.50 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[PDXDC2P-NPIPB14P]] | -0.50 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[YTHDF1]] | -0.49 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[ATG101]] | -0.49 | -0.29 / -0.52 | both halves | 2e-04 |  |
| [[NECTIN2]] | -0.49 | -0.31 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SUCLG2-DT]] | B | SUCLG2-DT activity raises DOCK7's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 1.92× lower at baseline in the lines without SUCLG2-DT | 0.008 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 200]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.438). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-24.3, -16.6); signed map (-4.2, -37.5). **Vector** length 101, 31.9% of its response variance represented; |z| ≥ 3 in 1,213 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.8 | +1.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.8 | +2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | +1.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.4 | +4.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +4.3 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | -3.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.3 | -13.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.0 | -7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.7 | -9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -19.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.2 | -8.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.0 | -3.2 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -2.0 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | dedicator of cytokinesis 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:62,454,298-62,688,386 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1771, ZIR2 |
| Gene groups (HGNC) | DOCK family Rho GEFs |
| Reactome | 11 pathways, smallest: MET activates RAP1 and RAC1; MET promotes cell motility; Signaling by MET |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96N67](https://www.uniprot.org/uniprotkb/Q96N67) (Dedicator of cytokinesis protein 7):

> Functions as a guanine nucleotide exchange factor (GEF), which activates Rac1 and Rac3 Rho small GTPases by exchanging bound GDP for free GTP. Does not have a GEF activity for CDC42. Required for STMN1 'Ser-15' phosphorylation during axon formation and consequently for neuronal polarization. As part of the DISP complex, may regulate the association of septins with actin and thereby regulate the actin cytoskeleton. Has a role in pigmentation (By similarity). Involved in the regulation of …

**Summary**, from NCBI Gene [85440](https://www.ncbi.nlm.nih.gov/gene/85440):

> The protein encoded by this gene is a guanine nucleotide exchange factor (GEF) that plays a role in axon formation and neuronal polarization. The encoded protein displays GEF activity toward RAC1 and RAC3 Rho small GTPases but not toward CDC42. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:19190](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19190) · Entrez [85440](https://www.ncbi.nlm.nih.gov/gene/85440) · UniProt [Q96N67](https://www.uniprot.org/uniprotkb/Q96N67) · Ensembl [ENSG00000116641](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116641)

## Data

Gene col 3811: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3811); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3811, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3811]; `tensor/DDL_lfc|DDL_z.npy` [3811]; `embed/gene_vectors.npy` [3811]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3811 or target_col == 3811). Every well: [[DOCK7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOCK7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
