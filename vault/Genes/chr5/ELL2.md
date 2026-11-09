---
symbol: "ELL2"
type: "gene"
col: 4033
ensembl_id: "ENSG00000118985"
name: "elongation factor for RNA polymerase II 2"
location: "5q15"
module: 113
arm: "+"
pooled_cpm: 477.91
n_lines_expressing: 38
n_dd_up: 10
n_dd_down: 45
n_dd_up_clean: 9
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 11
direction_downstream: 13
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# ELL2

*elongation factor for RNA polymerase II 2* — 5q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 1.42× (z +5.4, q 3e-05, up in 23 of 36 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.36× (z +4.7, q 6e-04, up in 24 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 45 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.375× (z -21.0, q 0e+00, down in 29 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINE1]] (+0.63, fdr 1e-05), [[ERRFI1]] (+0.63, fdr 1e-05), [[EPAS1]] (+0.60, fdr 1e-05); moves opposite to [[HNF4G]] (-0.51, fdr 4e-05), [[SH2D4A]] (-0.49, fdr 4e-05), [[TRIM2]] (-0.49, fdr 4e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[MARCHF3]] → it (grade B ⚠); 13 go from it, the strongest it → [[IL1RAP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4033.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.42×** | +5.4 | 3e-05 | 23/36 (C32, COLO 205, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +4.7 | 6e-04 | 24/37 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +4.2 | 0.004 | 21/37 (SK-MEL-2, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +4.2 | 0.004 | 16/36 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.009 | 24/36 (LOX-IMVI, NCI-H460, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.009 | 23/37 (NCI-H1573, H4, …) | top dose only | plate-row cell shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.009 | 17/36 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.012 | 19/36 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +3.4 | 0.043 | 14/37 (C32, CHP-212, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.072 | 20/36 (SK-MEL-2, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.079 | 18/36 (C32, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 45 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4033.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.375×** | -21.0 | 0e+00 | 29/37 (NCI-H1792, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.326×** | -17.0 | 0e+00 | 30/37 (HepG2/C3A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.339×** | -15.8 | 0e+00 | 27/32 (HepG2/C3A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.422×** | -12.6 | 3e-34 | 32/35 (HepG2/C3A, RKO, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.560×** | -8.8 | 2e-16 | 32/36 (RKO, HS-578T, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.548×** | -8.8 | 2e-16 | 25/36 (SNU-423, HS-578T, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.605×** | -7.3 | 2e-11 | 24/38 (SNU-423, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.656×** | -6.4 | 1e-08 | 24/36 (HepG2/C3A, hTERT-HPNE, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.669×** | -6.1 | 8e-08 | 26/36 (RKO, hTERT-HPNE, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.649×** | -6.0 | 8e-08 | 22/33 (HepG2/C3A, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.762×** | -5.8 | 3e-07 | 25/36 (RKO, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.692×** | -5.6 | 1e-06 | 21/36 (A-172, SNU-423, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.696×** | -5.3 | 6e-06 | 29/36 (NCI-H2347, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.721×** | -4.9 | 3e-05 | 22/36 (NCI-H1792, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.724×** | -4.9 | 4e-05 | 27/36 (RKO, HS-578T, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.796×** | -4.9 | 4e-05 | 20/36 (A-172, SNU-423, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **0.804×** | -4.6 | 1e-04 | 24/36 (RKO, NCI-H23, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.613×** | -3.9 | 0.003 | 23/36 (RKO, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.773×** | -3.9 | 0.003 | 23/35 (BT-474, RKO, …) | all doses, flat |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.613×** | -3.9 | 0.003 | 23/37 (NCI-H2347, J82, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.780×** | -3.7 | 0.004 | 20/36 (HS-578T, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4033. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 1,040 | 0 | 18 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -22.0) |
| [[BT-474 (line)]] | alt | 188 | 0 | 15 (3 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.225× (z -12.0) |
| [[SNU-423 (line)]] | alt | 943 | 0 | 11 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -23.4) |
| [[A-172 (line)]] | wt | 633 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -17.5) |
| [[HepG2_C3A (line)]] | wt | 1,198 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -20.8) |
| [[J82 (line)]] | alt | 684 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -24.0) |
| [[hTERT-HPNE (line)]] | wt | 1,055 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -20.1) |
| [[HS-578T (line)]] | alt | 721 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -23.8) |
| [[LoVo (line)]] | wt | 148 | 8 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.94× (z +17.0) | — |
| [[NCI-H2030 (line)]] | alt | 727 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -20.4) |
| [[NCI-H2347 (line)]] | alt | 1,076 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -16.1) |
| [[NCI-H460 (line)]] | wt | 1,027 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -22.0) |
| [[C32 (line)]] | wt | 183 | 7 (3 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 3.22× (z +13.7) | — |
| [[LOX-IMVI (line)]] | wt | 753 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -16.8) |
| [[NCI-H1573 (line)]] | alt | 861 | 2 (1 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.204× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 905 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -24.8) |
| [[SW 900 (line)]] | alt | 644 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -22.2) |
| [[CFPAC-1 (line)]] | alt | 753 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -13.8) |
| [[HOP62 (line)]] | alt | 1,153 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -13.0) |
| [[SHP-77 (line)]] | alt | 520 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -22.8) |
| [[RPMI-7951 (line)]] | alt | 500 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -12.9) |
| [[SW480 (line)]] | alt | 140 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.79× (z +9.6) | — |
| [[A549 (line)]] | wt | 542 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -18.5) |
| [[H4 (line)]] | wt | 438 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.366× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 283 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +24.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +9.5) | — |
| [[AsPC-1 (line)]] | alt | 132 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.60× (z +12.8) | — |
| [[COLO 205 (line)]] | alt | 149 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 193 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +17.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.37× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 380 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 369 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.00× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -10.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 232 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 1088 (line)]] | alt | 1,127 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -14.2) |
| [[Hs 766T (line)]] | wt | 178 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +17.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 403 | 0 | 1 | — | [[Radotinib (drug)]] 5 µM 0.396× (z -9.1) |
| [[SW 1271 (line)]] | alt | 542 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -8.6) |
| [[A-427 (line)]] | wt | 85.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 85.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 69.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 214 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 113 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 70.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 65.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 115 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 48.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 779 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 564 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 118 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 56.2 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 69.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 113 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4033), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINE1]] | +0.63 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[ERRFI1]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[EPAS1]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[STC1]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[IL1RAP]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[OSMR]] | +0.57 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[FERMT2]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ANGPTL4]] | +0.56 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[EBF2]] | +0.56 | +0.39 / +0.44 | both halves | 6e-05 |  |
| [[MARCHF3]] | +0.55 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[TREM1]] | +0.55 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[WDFY2]] | +0.55 | +0.59 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNF4G]] | -0.51 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[SH2D4A]] | -0.49 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[TRIM2]] | -0.49 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[CTPS2]] | -0.48 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[DIS3L]] | -0.47 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[ARFGEF2]] | -0.47 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[SLC37A1]] | -0.47 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[ACTR3C]] | -0.46 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[ITGA9-AS1]] | -0.46 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[TNFRSF14-AS1]] | -0.45 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[ITPKB]] | -0.45 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[TMCO4]] | -0.44 | -0.41 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MARCHF3]] | B | MARCHF3 activity raises ELL2's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 4.82× lower at baseline in the lines without MARCHF3 | 0.004 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[GLRX]] | B | GLRX activity raises ELL2's level | lines that do not express GLRX (10) vs lines expressing it (40) | 3.42× lower at baseline in the lines without GLRX | 0.008 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[GLIS3]] | B | GLIS3 activity raises ELL2's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 3.02× lower at baseline in the lines without GLIS3 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| [[SGIP1]] | B | SGIP1 activity raises ELL2's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 2.69× lower at baseline in the lines without SGIP1 | 0.015 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG |
| [[SMOX]] | B | SMOX activity raises ELL2's level | lines that do not express SMOX (6) vs lines expressing it (44) | 2.43× lower at baseline in the lines without SMOX | 0.026 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[CLMP]] | B | CLMP activity raises ELL2's level | lines that do not express CLMP (25) vs lines expressing it (25) | 2.91× lower at baseline in the lines without CLMP | 0.034 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10 |
| [[NDNF]] | B | NDNF activity raises ELL2's level | lines that do not express NDNF (25) vs lines expressing it (25) | 2.70× lower at baseline in the lines without NDNF | 0.073 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1 |
| [[STC1]] | C | STC1 activity raises ELL2's level | lines that do not express STC1 (24) vs lines expressing it (26) | 3.76× lower at baseline in the lines without STC1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP; co-absent with the target |
| [[RGS17]] | C | RGS17 activity raises ELL2's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 3.36× lower at baseline in the lines without RGS17 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1; co-absent with the target |
| [[EPAS1]] | C | EPAS1 activity raises ELL2's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 3.22× lower at baseline in the lines without EPAS1 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS; co-absent with the target |
| [[APC]] | C | APC activity strengthens ELL2's drug response | recorded loss-of-function mutation of APC in 5 lines vs 32 not recorded | the APC-altered lines respond 0.08× as strongly (z diff +6.41); strongest at Idarubicin (hydrochloride) 5 µM: 1.06x vs 0.36x (z diff +9.9) | 0.300 over the table, 0.079 within its group | ⚠ within its group only (a lead); tissue-confounded; across organs; target measured in part of the lines; lower baseline (lost expression?); artifact flags |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 11, C 2. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL1RAP]] | B | ELL2 activity raises IL1RAP's level | lines that do not express ELL2 (12) vs lines expressing it (38) | 3.35× lower at baseline in the lines without ELL2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent |
| [[GLRX]] | B | ELL2 activity raises GLRX's level | lines that do not express ELL2 (12) vs lines expressing it (38) | 3.40× lower at baseline in the lines without ELL2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent |
| [[SMOX]] | B | ELL2 activity raises SMOX's level | lines that do not express ELL2 (12) vs lines expressing it (38) | 2.82× lower at baseline in the lines without ELL2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent |
| [[MAP2K1]] | B | ELL2 activity raises MAP2K1's level | lines that do not express ELL2 (12) vs lines expressing it (38) | 1.35× lower at baseline in the lines without ELL2 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent |
| [[WDFY2]] | B | ELL2 activity raises WDFY2's level | lines that do not express ELL2 (12) vs lines expressing it (38) | 2.17× lower at baseline in the lines without ELL2 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent |
| [[MARCHF3]] | B | ELL2 activity raises MARCHF3's level | lines that do not express ELL2 (12) vs lines expressing it (38) | 2.30× lower at baseline in the lines without ELL2 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent |
| [[MCL1]] | B | ELL2 activity raises MCL1's level | lines that do not express ELL2 (12) vs lines expressing it (38) | 1.79× lower at baseline in the lines without ELL2 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent |
| cells under [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM | B | ELL2 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express ELL2 (12) vs lines expressing it (36) | the lines without ELL2: 1.17× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent |
| [[OSMR]] | B | ELL2 activity raises OSMR's level | lines that do not express ELL2 (12) vs lines expressing it (38) | 4.12× lower at baseline in the lines without ELL2 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent |
| [[RAI14]] | B | ELL2 activity raises RAI14's level | lines that do not express ELL2 (12) vs lines expressing it (38) | 3.50× lower at baseline in the lines without ELL2 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent |
| [[GLIS3]] | B | ELL2 activity raises GLIS3's level | lines that do not express ELL2 (12) vs lines expressing it (38) | 3.76× lower at baseline in the lines without ELL2 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent |
| [[EPAS1]] | C | ELL2 activity raises EPAS1's level | lines that do not express ELL2 (12) vs lines expressing it (38) | 4.74× lower at baseline in the lines without ELL2 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.5, 10.3); signed map (14.1, 36.6). **Vector** length 130, 47.4% of its response variance represented; |z| ≥ 3 in 1,549 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.2 | +4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +6.5 | -4.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | +6.4 | -2.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +6.4 | -6.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.6 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.1 | +3.9 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -7.2 | -8.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -4.3 | -4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.3 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~58% of this change | -4.3 | -1.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -3.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.8 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | elongation factor for RNA polymerase II 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q15 — chr5:95,885,098-95,961,851 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRCCAT1 |
| Gene groups (HGNC) | Super elongation complex |
| Hallmark sets | ANDROGEN_RESPONSE, HEME_METABOLISM |
| Reactome | 3 pathways, smallest: M-decay: degradation of maternal mRNAs by maternally stored factors; Maternal to zygotic transition (MZT); RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O00472](https://www.uniprot.org/uniprotkb/O00472) (RNA polymerase II elongation factor ELL2):

> Elongation factor component of the super elongation complex (SEC), a complex required to increase the catalytic rate of RNA polymerase II transcription by suppressing transient pausing by the polymerase at multiple sites along the DNA. Component of the little elongation complex (LEC), a complex required to regulate small nuclear RNA (snRNA) gene transcription by RNA polymerase II and III. Plays a role in immunoglobulin secretion in plasma cells: directs efficient alternative mRNA processing, …

**Summary**, from NCBI Gene [22936](https://www.ncbi.nlm.nih.gov/gene/22936):

> Predicted to enable cis-regulatory region sequence-specific DNA binding activity. Involved in snRNA transcription by RNA polymerase II. Located in nucleoplasm. Part of transcription elongation factor complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17064](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17064) · Entrez [22936](https://www.ncbi.nlm.nih.gov/gene/22936) · UniProt [O00472](https://www.uniprot.org/uniprotkb/O00472) · Ensembl [ENSG00000118985](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118985)

## Data

Gene col 4033: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4033); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4033, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4033]; `tensor/DDL_lfc|DDL_z.npy` [4033]; `embed/gene_vectors.npy` [4033]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4033 or target_col == 4033). Every well: [[ELL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
