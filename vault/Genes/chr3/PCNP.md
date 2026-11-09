---
symbol: "PCNP"
type: "gene"
col: 1310
ensembl_id: "ENSG00000081154"
name: "PEST proteolytic signal containing nuclear protein"
location: "3q12.3"
module: 148
arm: "+"
pooled_cpm: 124.41
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 7
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# PCNP

*PEST proteolytic signal containing nuclear protein* — 3q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.76× (z +15.5, q 0e+00, up in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.27× (z +6.6, q 5e-09, up in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (Panc 03.27 3.03×, SW480 2.31×, NCI-H460 2.37×, HOP62 2.21×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 1.99×, NCI-H460 2.15×, PANC-1 1.89×, NCI-H2347 2.01×, …; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 2 lines (A498 3.83×, NCI-H460 2.61×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 1.65×).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.614× (z -13.4, q 4e-38, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPY19L4]] (+0.65, fdr 1e-04), [[SLC30A9]] (+0.64, fdr 1e-05), [[RRM2B]] (+0.64, fdr 2e-05); moves opposite to [[HMGB1P5]] (-0.58, fdr 2e-05, ⚠ HMGB1P5 in the vector space only through flagged drug-doses), [[NR2F6]] (-0.56, fdr 1e-04), [[PTMAP2]] (-0.54, fdr 2e-04, ⚠ PTMAP2 in the vector space only through flagged drug-doses), [[C4orf48]] (-0.52, fdr 5e-04), [[UBE2G1]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1310.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (Panc 03.27 3.03×, SW480 2.31×, NCI-H460 2.37×, HOP62 2.21×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 1.99×, NCI-H460 2.15×, PANC-1 1.89×, NCI-H2347 2.01×, …; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 2 lines (A498 3.83×, NCI-H460 2.61×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 1.65×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +15.5 | 0e+00 | 44/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +15.0 | 0e+00 | 37/44 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +10.5 | 2e-23 | 35/45 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +7.8 | 1e-12 | 0/50 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +6.6 | 5e-09 | 31/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.38×** | +4.7 | 3e-04 | 23/49 (A498, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.15× | +3.7 | 0.015 | 9/49 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.10× | +3.7 | 0.018 | 16/48 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~13% of this change | 1.14× | +3.6 | 0.020 | 13/48 (NCI-H23, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.14× | +3.6 | 0.020 | 17/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.15× | +3.5 | 0.022 | 18/47 (RKO, NCI-H460, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1310.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.614×** | -13.4 | 4e-38 | 45/48 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.644×** | -12.1 | 4e-31 | 43/48 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.680×** | -10.6 | 7e-24 | 43/48 (LOX-IMVI, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.730×** | -8.7 | 7e-16 | 40/48 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.820×** | -7.7 | 1e-12 | 29/48 (SW1417, LOX-IMVI, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.866× | -5.6 | 2e-06 | 21/49 (SW480, HEC-1-A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.825×** | -5.3 | 1e-05 | 24/48 (Panc 03.27, A-172, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.758×** | -4.0 | 0.005 | 25/49 (A549, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.900× | -3.9 | 0.006 | 5/48 (NCI-H23, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Elagolix sodium (drug)]] 0.5 µM |  | 0.884× | -3.4 | 0.035 | 10/48 (CHP-212, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.884× | -3.4 | 0.035 | 11/49 (A498, A-427, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.884× | -3.3 | 0.052 | 17/48 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.889× | -3.1 | 0.097 | 15/47 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | 0.925× | -3.0 | 0.10 | 1/48 (SNU-1) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1310. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 97.7 | 4 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.37× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.65× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.519× (z -11.2) |
| [[HOP62 (line)]] | alt | 136 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.21× (z +12.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.548× (z -10.0) |
| [[SW480 (line)]] | alt | 110 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.31× (z +15.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -13.2) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.579× (z -10.7) |
| [[A549 (line)]] | wt | 150 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +11.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.398× (z -12.3) |
| [[A-427 (line)]] | wt | 232 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.563× (z -9.5) |
| [[J82 (line)]] | alt | 153 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 1.77× (z +8.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.515× (z -10.8) |
| [[LoVo (line)]] | wt | 137 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 1.82× (z +9.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.511× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 124 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.484× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 78.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.61× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -11.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 137 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +11.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 142 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.97× (z +12.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 112 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.05× (z +10.1) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.561× (z -8.6) |
| [[SW1417 (line)]] | alt | 117 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.508× (z -11.1) |
| [[HT-29 (line)]] | alt | 113 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.04× (z +10.5) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 135 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.405× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.472× (z -9.1) |
| [[KATO III (line)]] | alt | 117 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.07× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 143 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.476× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 112 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.19× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 119 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.3) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H2030 (line)]] | alt | 84.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.29× (z +11.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 124 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +10.5) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.448× (z -9.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 112 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.72× (z +12.2) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 99.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 154 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.450× (z -10.3) |
| [[A498 (line)]] | wt | 115 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.83× (z +11.4) | — |
| [[AN3 CA (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.309× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[C32 (line)]] | wt | 118 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +9.2) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 147 | 0 | 1 | — | [[palbociclib (drug)]] 5 µM 0.0928× (z -9.1) |
| [[H4 (line)]] | wt | 129 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.399× (z -9.2) |
| [[Hs 766T (line)]] | wt | 89.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 156 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.81× (z +8.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 129 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +15.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 136 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.482× (z -10.2) |
| [[SW48 (line)]] | wt | 133 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.47× (z +9.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 121 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 134 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 101 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 133 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1310), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY19L4]] | +0.65 | +0.33 / +0.70 | both halves | 1e-04 |  |
| [[SLC30A9]] | +0.64 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[RRM2B]] | +0.64 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[CHMP3]] | +0.62 | +0.30 / +0.66 | both halves | 2e-04 |  |
| [[AMZ2]] | +0.55 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[TAF9]] | +0.55 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[BAX]] | +0.55 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[PRKAR1A]] | +0.55 | +0.27 / +0.59 | both halves | 3e-04 |  |
| [[LIN7C]] | +0.54 | +0.27 / +0.56 | both halves | 3e-04 |  |
| [[NEK9]] | +0.54 | +0.32 / +0.39 | both halves | 2e-04 |  |
| [[SF3A1]] | +0.54 | +0.33 / +0.56 | both halves | 1e-04 |  |
| [[GUF1]] | +0.54 | +0.26 / +0.52 | both halves | 4e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 11 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGB1P5]] ⚠ | -0.58 | -0.47 / -0.54 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NR2F6]] | -0.56 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[PTMAP2]] ⚠ | -0.54 | -0.32 / -0.53 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[POP7]] | -0.53 | -0.12 / -0.54 | ⚠ one half (not replicated) | 0.002 |  |
| [[C4orf48]] | -0.52 | -0.23 / -0.52 | both halves | 5e-04 |  |
| [[UBE2G1]] | -0.51 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[CARHSP1]] | -0.50 | -0.21 / -0.52 | both halves | 7e-04 |  |
| [[MRPL14]] | -0.50 | -0.23 / -0.53 | both halves | 5e-04 |  |
| [[POLR3K]] | -0.48 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[EXOSC4]] | -0.48 | -0.25 / -0.50 | both halves | 4e-04 |  |
| [[RPL36AL]] ⚠ | -0.48 | -0.12 / -0.49 | ⚠ not reproduced | 0.002 | ⚠ in the vector space only through flagged drug-doses |
| [[EMC6]] | -0.47 | -0.14 / -0.51 | ⚠ one half (not replicated) | 0.002 |  |
| [[AMD1]] | -0.47 | -0.24 / -0.49 | both halves | 5e-04 |  |
| [[PAQR4]] | -0.47 | -0.23 / -0.48 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PCNP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PCNP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.520). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-7.6, 2.2); signed map (16.4, -29.1). **Vector** length 111, 30.2% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.7 | +15.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.2 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.5 | +2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +2.0 | +1.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -7.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.6 | -13.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.6 | -10.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -3.5 | +0.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.9 | -8.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.2 | -1.2 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.1 | -0.9 |
|  | [[Flutamide (drug)]] 0.5 µM |  | -2.0 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | PEST proteolytic signal containing nuclear protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.3 — chr3:101,574,180-101,594,465 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WW12](https://www.uniprot.org/uniprotkb/Q8WW12) (PEST proteolytic signal-containing nuclear protein):

> May be involved in cell cycle regulation.

**Summary**, from NCBI Gene [57092](https://www.ncbi.nlm.nih.gov/gene/57092):

> Involved in proteasome-mediated ubiquitin-dependent protein catabolic process and protein ubiquitination. Located in nuclear body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30023](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30023) · Entrez [57092](https://www.ncbi.nlm.nih.gov/gene/57092) · UniProt [Q8WW12](https://www.uniprot.org/uniprotkb/Q8WW12) · Ensembl [ENSG00000081154](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081154)

## Data

Gene col 1310: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1310); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1310, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1310]; `tensor/DDL_lfc|DDL_z.npy` [1310]; `embed/gene_vectors.npy` [1310]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1310 or target_col == 1310). Every well: [[PCNP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCNP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
