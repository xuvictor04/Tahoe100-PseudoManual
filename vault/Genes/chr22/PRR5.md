---
symbol: "PRR5"
type: "gene"
col: 11841
ensembl_id: "ENSG00000186654"
name: "proline rich 5"
location: "22q13.31"
module: 159
arm: "+"
pooled_cpm: 8.92
n_lines_expressing: 46
n_dd_up: 13
n_dd_down: 17
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 8
direction_downstream: 18
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# PRR5

*proline rich 5* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.89× (z +9.1, q 3e-17, up in 23 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.348× (z -21.4, q 0e+00, down in 29 of 40 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.429× (z -12.1, q 2e-31, down in 26 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRR5-ARHGAP8]] (+0.81, fdr 7e-06, ⚠ same locus), [[ARHGAP8]] (+0.73, fdr 1e-05, ⚠ same locus), [[TPST2]] (+0.70, fdr 9e-06), [[ANKRD27]] (+0.67, fdr 1e-05), [[LIMK1]] (+0.67, fdr 1e-05); moves opposite to [[DNAI4]] (-0.67, fdr 3e-05), [[CREBBP]] (-0.64, fdr 1e-05), [[EP300]] (-0.64, fdr 2e-05).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 18 go from it, the strongest it → [[KIAA1671]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11841.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.89×** | +9.1 | 3e-17 | 23/43 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.81×** | +8.6 | 2e-15 | 26/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +7.5 | 9e-12 | 25/43 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +6.6 | 6e-09 | 17/43 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +6.0 | 2e-07 | 20/43 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +5.4 | 5e-06 | 15/43 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.44×** | +5.0 | 4e-05 | 13/40 (NCI-H1573, HEC-1-A, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +4.7 | 2e-04 | 16/41 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +4.4 | 8e-04 | 5/18 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.57×** | +3.4 | 0.037 | 4/29 (PANC-1, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.040 | 6/40 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.040 | 7/43 (NCI-H1573, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.047 | 2/38 (SW480, HOP62) | top dose only | noisy plate (z scaled); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 1.16× | +3.0 | 0.11 | 10/43 (NCI-H23, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11841.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.348×** | -21.4 | 0e+00 | 29/40 (A-172, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.429×** | -12.1 | 2e-31 | 26/38 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.463×** | -10.6 | 5e-24 | 28/43 (LoVo, NCI-H2030, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.536×** | -8.6 | 1e-15 | 23/40 (A-172, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.550×** | -8.6 | 1e-15 | 27/43 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.659×** | -8.4 | 3e-15 | 25/44 (RPMI-7951, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -7.1 | 1e-10 | 23/41 (HOP62, C-33 A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.615×** | -7.0 | 2e-10 | 21/43 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.666×** | -5.8 | 4e-07 | 16/32 (A-172, SW48, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.473×** | -5.6 | 1e-06 | 21/41 (LoVo, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.691×** | -5.3 | 7e-06 | 20/42 (LoVo, RKO, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.782×** | -5.0 | 3e-05 | 16/38 (HOP62, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.805×** | -4.4 | 6e-04 | 15/43 (KATO III, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.763×** | -3.9 | 0.005 | 16/42 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.783×** | -3.5 | 0.018 | 15/42 (LoVo, A-172, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.804×** | -3.1 | 0.062 | 9/43 (LoVo, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11841. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 9.40 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -13.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -9.8) |
| [[A-172 (line)]] | wt | 12.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0524× (z -21.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -10.5) |
| [[LoVo (line)]] | wt | 20.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -21.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 9.56 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.100× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -8.6) |
| [[SW480 (line)]] | alt | 10.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -11.2) |
| [[A498 (line)]] | wt | 20.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -15.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[C-33 A (line)]] | alt | 18.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -12.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -9.8) |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0470× (z -10.6) |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -10.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 9.37 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.109× (z -11.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H460 (line)]] | wt | 7.26 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -12.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -9.0) |
| [[SW48 (line)]] | wt | 30.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -11.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -11.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AsPC-1 (line)]] | alt | 6.24 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0583× (z -11.7) |
| [[Hs 766T (line)]] | wt | 4.39 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0802× (z -11.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[KATO III (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 9.18 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -14.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 8.38 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -12.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 900 (line)]] | alt | 7.13 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0618× (z -10.5) |
| [[SW1417 (line)]] | alt | 9.24 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.173× (z -8.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.984 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.961 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11841), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR5-ARHGAP8]] | +0.81 | +0.77 / +0.81 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ARHGAP8]] | +0.73 | +0.74 / +0.52 | both halves | 1e-05 | STRING 932; ⚠ same locus (14.9 kb, same strand: neighbours can correlate without regulation) |
| [[TPST2]] | +0.70 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[ANKRD27]] | +0.67 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[LIMK1]] | +0.67 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[WASF3]] | +0.67 | +0.64 / +0.48 | both halves | 2e-05 | pathway: Signaling by VEGF |
| [[PACC1]] | +0.66 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[GNAZ]] | +0.66 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[BRSK2]] | +0.65 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[FAM118A]] | +0.64 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SHANK3]] | +0.64 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[FGFR4]] | +0.64 | +0.46 / +0.55 | both halves | 2e-05 | pathway: Intracellular signaling by second messengers |
| [[AIF1L]] | +0.64 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[IMPDH1]] | +0.64 | +0.62 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAI4]] | -0.67 | -0.69 / -0.45 | both halves | 3e-05 |  |
| [[CREBBP]] | -0.64 | -0.56 / -0.51 | both halves | 1e-05 | pathway: Regulation of T cell activation by CD28 family |
| [[EP300]] | -0.64 | -0.46 / -0.50 | both halves | 2e-05 | pathway: Regulation of T cell activation by CD28 family |
| [[BAZ2B]] | -0.63 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[METTL6]] | -0.63 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[SLC38A4-AS1]] | -0.62 | -0.71 / -0.42 | both halves | 4e-05 |  |
| [[PCNX4-DT]] | -0.62 | -0.66 / -0.33 | both halves | 1e-04 |  |
| [[RC3H2]] | -0.61 | -0.62 / -0.39 | both halves | 6e-05 |  |
| [[ZNF429]] | -0.61 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[CGGBP1]] | -0.61 | -0.64 / -0.36 | both halves | 9e-05 |  |
| [[HHLA3]] | -0.61 | -0.65 / -0.30 | both halves | 2e-04 |  |
| [[BPTF]] | -0.61 | -0.64 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PRR5's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLCG2]] | B | PLCG2 activity raises PRR5's level | lines that do not express PLCG2 (10) vs lines expressing it (40) | 1.89× lower at baseline in the lines without PLCG2 | 0.026 | ⚠ within organs, on part of the lines; also absent: CRACD; maybe low, not absent |
| [[AIF1L]] | B | AIF1L activity raises PRR5's level | lines that do not express AIF1L (12) vs lines expressing it (38) | 1.56× lower at baseline in the lines without AIF1L | 0.074 | ⚠ within organs, on part of the lines; also absent: FAM169A, NUP210, PRR36; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PRR5's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers PRR5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers PRR5's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MIR583HG]] | B | MIR583HG activity lowers PRR5's level | lines that do not express MIR583HG (10) vs lines expressing it (40) | 1.95× higher at baseline in the lines without MIR583HG | 0.095 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RGS17, GNAI1, KLF12; maybe low, not absent |
| [[GARNL3]] | C | GARNL3 activity raises PRR5's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 2.10× lower at baseline in the lines without GARNL3 | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 0, C 18. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA1671]] | C | PRR5 activity raises KIAA1671's level | lines that do not express PRR5 (4) vs lines expressing it (46) | 3.70× lower at baseline in the lines without PRR5 | 0.002 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: NECTIN1, PLEKHG3, SNED1 |
| [[PBX4]] | C | PRR5 activity raises PBX4's level | lines that do not express PRR5 (4) vs lines expressing it (46) | 3.00× lower at baseline in the lines without PRR5 | 0.029 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: NECTIN1, PLEKHG3, SNED1 |
| [[THAP9]] | C | PRR5 activity raises THAP9's level | lines that do not express PRR5 (4) vs lines expressing it (46) | 1.64× lower at baseline in the lines without PRR5 | 0.036 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: NECTIN1, PLEKHG3, SNED1 |
| cells under [[Doxycycline (monohydrate) (drug)]] 5 µM | C | PRR5, [[PRR5-ARHGAP8]] activity raises the cells' numbers under Doxycycline (monohydrate) 5 µM (protects the cells) | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (44) | the lines without PRR5, PRR5-ARHGAP8: 0.68× the cells of the other lines | 0.040 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |
| cells under [[EX229 (drug)]] 0.05 µM | C | PRR5, [[PRR5-ARHGAP8]] activity raises the cells' numbers under EX229 0.05 µM (protects the cells) | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (44) | the lines without PRR5, PRR5-ARHGAP8: 0.77× the cells of the other lines | 0.057 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |
| cells under [[Glycyrrhizic acid (drug)]] 0.5 µM | C | PRR5, [[PRR5-ARHGAP8]] activity raises the cells' numbers under Glycyrrhizic acid 0.5 µM (protects the cells) | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (44) | the lines without PRR5, PRR5-ARHGAP8: 0.73× the cells of the other lines | 0.057 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |
| cells under [[Vinblastine (sulfate) (drug)]] 0.5 µM | C | PRR5, [[PRR5-ARHGAP8]] activity raises the cells' numbers under Vinblastine (sulfate) 0.5 µM (protects the cells) | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (44) | the lines without PRR5, PRR5-ARHGAP8: 0.71× the cells of the other lines | 0.059 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | PRR5, [[PRR5-ARHGAP8]] activity raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (44) | the lines without PRR5, PRR5-ARHGAP8: 0.75× the cells of the other lines | 0.063 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |
| cells under [[Apalutamide (drug)]] 0.5 µM | C | PRR5, [[PRR5-ARHGAP8]] activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (44) | the lines without PRR5, PRR5-ARHGAP8: 1.26× the cells of the other lines | 0.065 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |
| [[CGREF1]] | C | PRR5, [[PRR5-ARHGAP8]] activity raises CGREF1's level | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (46) | 2.92× lower at baseline in the lines without PRR5, PRR5-ARHGAP8 | 0.072 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |
| [[RO60]] | C | PRR5 activity strengthens RO60's drug response | lines that do not express PRR5 (4) vs lines expressing it (46) | the lines without PRR5 respond 0.96× as strongly (z diff +1.05); strongest at Ouabain (Octahydrate) 5 µM: 1.16x vs 1.55x (z diff +4.7) | 0.075 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: NECTIN1, PLEKHG3, SNED1; artifact flags |
| cells under [[Procainamide (hydrochloride) (drug)]] 0.5 µM | C | PRR5, [[PRR5-ARHGAP8]] activity raises the cells' numbers under Procainamide (hydrochloride) 0.5 µM (protects the cells) | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (44) | the lines without PRR5, PRR5-ARHGAP8: 0.77× the cells of the other lines | 0.082 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.0, 4.1); signed map (-20.8, 36.3). **Vector** length 84.8, 16.5% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +7.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.1 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +4.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.6 | +9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.7 | -10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -12.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.1 | -21.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.4 | -8.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -8.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | proline rich 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:44,668,547-44,737,681 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PP610, FLJ20185k, Protor-1., PROTOR1 |
| Gene groups (HGNC) | MTOR complex 2 |
| Reactome | 25 pathways, smallest: Dengue virus modulates apoptosis; CD28 dependent PI3K/Akt signaling; Constitutive Signaling by AKT1 E17K in Cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [P85299](https://www.uniprot.org/uniprotkb/P85299) (Proline-rich protein 5):

> Associated subunit of mTORC2, which regulates cell growth and survival in response to hormonal signals. mTORC2 is activated by growth factors, but, in contrast to mTORC1, seems to be nutrient-insensitive. mTORC2 seems to function upstream of Rho GTPases to regulate the actin cytoskeleton, probably by activating one or more Rho-type guanine nucleotide exchange factors. PRR5 plays an important role in regulation of PDGFRB expression and in modulation of platelet-derived growth factor signaling. …

**Summary**, from NCBI Gene [55615](https://www.ncbi.nlm.nih.gov/gene/55615):

> This gene encodes a protein with a proline-rich domain. This gene is located in a region of chromosome 22 reported to contain a tumor suppressor gene that may be involved in breast and colorectal tumorigenesis. The protein is a component of the mammalian target of rapamycin complex 2 (mTORC2), and it regulates platelet-derived growth factor (PDGF) receptor beta expression and PDGF signaling to Akt and S6K1. Alternative splicing and the use of alternative promoters results in transcripts …

**Accessions** — [HGNC:31682](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31682) · Entrez [55615](https://www.ncbi.nlm.nih.gov/gene/55615) · UniProt [P85299](https://www.uniprot.org/uniprotkb/P85299) · Ensembl [ENSG00000186654](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186654)

## Data

Gene col 11841: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11841); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11841, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11841]; `tensor/DDL_lfc|DDL_z.npy` [11841]; `embed/gene_vectors.npy` [11841]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11841 or target_col == 11841). Every well: [[PRR5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRR5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
