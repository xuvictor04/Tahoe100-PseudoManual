---
symbol: "CNBP"
type: "gene"
col: 9841
ensembl_id: "ENSG00000169714"
name: "CCHC-type zinc finger nucleic acid binding protein"
location: "3q21.3"
module: 25
arm: "+"
pooled_cpm: 146.56
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# CNBP

*CCHC-type zinc finger nucleic acid binding protein* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.02× (z +15.1, q 0e+00, up in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.61× (z +10.6, q 4e-24, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.820× (z -4.3, q 0.010, down in 26 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 0.574×, SK-MEL-2 0.594×; ⚠ cell-cycle shift, explains ~32% of this change); [[Selinexor (drug)]] 5 µM in 1 line (RKO 0.629×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLNS1A]] (+0.58, fdr 1e-05), [[EIF4B]] (+0.58, fdr 1e-05), [[SBDSP1]] (+0.57, fdr 3e-05); moves opposite to [[ULBP2]] (-0.53, fdr 3e-05), [[C19orf81]] (-0.51, fdr 4e-04), [[UBA6]] (-0.50, fdr 9e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ULBP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 19 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9841.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +15.1 | 0e+00 | 42/44 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.89×** | +13.1 | 2e-36 | 45/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.68×** | +11.6 | 5e-29 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +10.7 | 2e-24 | 38/45 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +10.6 | 4e-24 | 46/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +9.9 | 6e-21 | 0/50 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.55×** | +9.8 | 9e-21 | 41/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +9.0 | 2e-17 | 41/48 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.10×** | +8.7 | 3e-16 | 39/48 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.47×** | +8.7 | 3e-16 | 31/48 (NCI-H2030, HT-29, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +8.1 | 3e-14 | 36/47 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +8.1 | 3e-14 | 40/48 (NCI-H1792, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.40×** | +7.5 | 2e-12 | 38/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +7.4 | 4e-12 | 26/48 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.88×** | +7.4 | 5e-12 | 38/49 (KATO III, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +5.8 | 3e-07 | 29/48 (LOX-IMVI, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +5.1 | 1e-05 | 29/48 (H4, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.9 | 2e-05 | 28/48 (H4, SW480, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.20× | +4.0 | 0.001 | 22/48 (HT-29, HEC-1-A, …) | two highest doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.033 | 15/49 (NCI-H1573, C32, …) | top dose only | noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.10× | +3.0 | 0.046 | 3/49 (PANC-1, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9841.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 0.574×, SK-MEL-2 0.594×; ⚠ cell-cycle shift, explains ~32% of this change); [[Selinexor (drug)]] 5 µM in 1 line (RKO 0.629×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.820×** | -4.3 | 0.010 | 26/47 (LoVo, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.848× | -3.7 | 0.060 | 22/48 (SW 900, PANC-1, …) | all doses, stronger at high dose |  |
| [[Fusidic acid (drug)]] 5 µM |  | 0.900× | -3.4 | 0.14 | 4/48 (SW 1088, NCI-H661, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.869× | -3.2 | 0.22 | 17/48 (PANC-1, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9841. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 108 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.19× (z +9.4) | — |
| [[SW480 (line)]] | alt | 153 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.01× (z +16.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.18× (z +11.9) | — |
| [[H4 (line)]] | wt | 136 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +10.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.66× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 160 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.37× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.09× (z +11.0) | — |
| [[LoVo (line)]] | wt | 119 | 4 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +11.5) ⚠ cell-cycle shift, explains ~26% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -11.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1573 (line)]] | alt | 102 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +12.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 81.3 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.42× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.58× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 99.0 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +13.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 172 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +12.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 96.8 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.86× (z +17.1) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 204 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.91× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.96× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 217 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.67× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.56× (z +11.8) | — |
| [[HCT15 (line)]] | alt | 167 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 129 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +16.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LS 180 (line)]] | wt | 128 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +10.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2030 (line)]] | alt | 97.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +17.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 174 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.41× (z +11.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 163 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.31× (z +12.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 134 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.10× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 142 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HEC-1-A (line)]] | alt | 195 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.90× (z +10.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[Hs 766T (line)]] | wt | 102 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 177 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 107 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +13.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 185 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.04× (z +9.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -10.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-423 (line)]] | alt | 114 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +12.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 163 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.06× (z +9.4) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 130 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.04× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 155 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.19× (z +9.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 185 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.629× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 160 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 158 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 1.84× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 126 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 147 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 142 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 112 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 105 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 147 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9841), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLNS1A]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[EIF4B]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[SBDSP1]] | +0.57 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[LIN7C]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[RMND5A]] | +0.56 | +0.40 / +0.56 | both halves | 4e-05 |  |
| [[MRRF]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[BOD1]] | +0.55 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[EIF4H]] | +0.54 | +0.40 / +0.61 | both halves | 5e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 471 |
| [[MATR3]] | +0.54 | +0.38 / +0.60 | both halves | 7e-05 |  |
| [[DNAJA2]] | +0.54 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[SBDS]] | +0.53 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[EEF1A1]] | +0.53 | +0.41 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ULBP2]] | -0.53 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[C19orf81]] | -0.51 | -0.25 / -0.55 | both halves | 4e-04 |  |
| [[UBA6]] | -0.50 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[B3GAT3]] | -0.50 | -0.26 / -0.55 | both halves | 4e-04 |  |
| [[RNF122]] | -0.49 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[NUDT22]] | -0.49 | -0.21 / -0.52 | both halves | 6e-04 |  |
| [[PLAUR]] | -0.48 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[FBXO11]] | -0.48 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[NOG]] | -0.48 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[TPBG]] | -0.48 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[CCDC24]] | -0.47 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[MYO9B]] | -0.47 | -0.37 / -0.40 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ULBP2]] | B | ULBP2 activity lowers CNBP's level | lines that do not express ULBP2 (9) vs lines expressing it (41) | 1.20× higher at baseline in the lines without ULBP2 | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.520). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-31.0, -24.4); signed map (5.7, -34.0). **Vector** length 84.3, 25.0% of its response variance represented; |z| ≥ 3 in 1,175 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.1 | +10.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.4 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.1 | +8.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.0 | +0.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.7 | -1.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.6 | -0.6 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -2.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.1 | -0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.9 | -3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.8 | -1.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.7 | -1.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | CCHC-type zinc finger nucleic acid binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:129,167,827-129,183,922 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNF163, ZCCHC22, CNBP1; previously DM2, ZNF9 |
| Gene groups (HGNC) | Zinc fingers CCHC-type |
| Hallmark sets | PEROXISOME, MYC_TARGETS_V1 |
| Reactome | 5 pathways, smallest: SARS-CoV-2 activates/modulates innate and adaptive immune responses; SARS-CoV-2-host interactions; SARS-CoV-2 Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [P62633](https://www.uniprot.org/uniprotkb/P62633) (CCHC-type zinc finger nucleic acid binding protein):

> Single-stranded DNA-binding protein that preferentially binds to the sterol regulatory element (SRE) sequence 5'-GTGCGGTG-3', and thereby mediates transcriptional repression. Has a role as transactivator of the Myc promoter (By similarity). Binds single-stranded RNA in a sequence-specific manner (By similarity).; [Isoform 1]: Binds G-rich elements in target mRNA coding sequences. Prevents G-quadruplex structure formation in vitro, suggesting a role in supporting translation by resolving stable …

**Summary**, from NCBI Gene [7555](https://www.ncbi.nlm.nih.gov/gene/7555):

> This gene encodes a nucleic-acid binding protein with seven zinc-finger domains. The protein has a preference for binding single stranded DNA and RNA. The protein functions in cap-independent translation of ornithine decarboxylase mRNA, and may also function in sterol-mediated transcriptional regulation. A CCTG expansion from <30 repeats to 75-11000 repeats in the first intron of this gene results in myotonic dystrophy type 2. Multiple transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:13164](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13164) · Entrez [7555](https://www.ncbi.nlm.nih.gov/gene/7555) · UniProt [P62633](https://www.uniprot.org/uniprotkb/P62633) · Ensembl [ENSG00000169714](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169714)

## Data

Gene col 9841: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9841); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9841, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9841]; `tensor/DDL_lfc|DDL_z.npy` [9841]; `embed/gene_vectors.npy` [9841]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9841 or target_col == 9841). Every well: [[CNBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
