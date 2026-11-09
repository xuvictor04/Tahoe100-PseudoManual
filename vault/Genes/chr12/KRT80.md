---
symbol: "KRT80"
type: "gene"
col: 9535
ensembl_id: "ENSG00000167767"
name: "keratin 80"
location: "12q13.13"
module: 123
arm: "+"
pooled_cpm: 22.02
n_lines_expressing: 28
n_dd_up: 51
n_dd_down: 12
n_dd_up_clean: 40
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 28
direction_downstream: 32
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# KRT80

*keratin 80* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 51 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.80× (z +17.8, q 0e+00, up in 14 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.09× (z +13.9, q 1e-41, up in 15 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.628× (z -8.8, q 6e-16, down in 21 of 26 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00592]] (+0.67, fdr 7e-06, ⚠ same locus), [[ANXA3]] (+0.61, fdr 1e-05), [[IL18]] (+0.59, fdr 1e-05), [[AJUBA]] (+0.59, fdr 1e-05); moves opposite to [[SENP5]] (-0.55, fdr 1e-05), [[QPCTL]] (-0.49, fdr 3e-05), [[SMG1P5]] (-0.49, fdr 3e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[CXADR]] → it (grade B ⚠); 32 go from it, the strongest it → [[LINC00592]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 51 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9535.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.80×** | +17.8 | 0e+00 | 14/24 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.16×** | +14.7 | 0e+00 | 11/19 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +13.9 | 1e-41 | 15/26 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.07×** | +13.7 | 3e-40 | 23/26 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.97×** | +9.0 | 2e-17 | 19/26 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.02×** | +8.6 | 6e-16 | 11/21 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.84×** | +7.8 | 6e-13 | 17/26 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.50×** | +7.6 | 2e-12 | 13/26 (PANC-1, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +7.5 | 4e-12 | 16/26 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.53×** | +6.7 | 1e-09 | 15/26 (NCI-H1573, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +6.5 | 5e-09 | 14/26 (SW480, A549, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.60×** | +6.2 | 2e-08 | 15/25 (LS 180, COLO 205, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.66×** | +6.2 | 2e-08 | 19/27 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled); position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.66×** | +6.1 | 3e-08 | 15/26 (SW480, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.59×** | +6.1 | 5e-08 | 14/27 (NCI-H1573, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.38×** | +5.7 | 5e-07 | 18/26 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +5.6 | 5e-07 | 17/26 (PANC-1, A549, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.52×** | +5.5 | 1e-06 | 14/26 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9535.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.628×** | -8.8 | 6e-16 | 21/26 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.555×** | -7.9 | 8e-13 | 17/26 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.573×** | -7.5 | 2e-11 | 20/26 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.632×** | -6.1 | 1e-07 | 14/26 (HEC-1-A, SW1417, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.677×** | -5.2 | 2e-05 | 15/25 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.686×** | -5.1 | 4e-05 | 12/26 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.671×** | -4.9 | 9e-05 | 16/26 (HT-29, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.720×** | -4.3 | 0.002 | 11/25 (SW480, HEC-1-A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.733×** | -4.2 | 0.002 | 16/26 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[BAY1125976 (drug)]] 5 µM |  | **0.546×** | -3.6 | 0.018 | 3/26 (MIA PaCa-2, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | 0.840× | -3.3 | 0.042 | 7/27 (A498, CFPAC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.781×** | -3.3 | 0.042 | 14/26 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.783×** | -3.3 | 0.044 | 11/25 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -3.2 | 0.051 | 2/27 (HCT15, HepG2/C3A) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9535. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 89.7 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -15.1) |
| [[HEC-1-A (line)]] | alt | 84.8 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -21.5) |
| [[KATO III (line)]] | alt | 53.7 | 2 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.52× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.190× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -10.9) |
| [[LoVo (line)]] | wt | 47.3 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -16.1) |
| [[SW1417 (line)]] | alt | 96.9 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -22.1) |
| [[COLO 205 (line)]] | alt | 23.3 | 4 (2 ⚠) | 0 | [[Daptomycin (drug)]] 0.5 µM 7.20× (z +9.6) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 7.69× (z +9.6) | — |
| [[SW480 (line)]] | alt | 42.9 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -23.4) |
| [[A-172 (line)]] | wt | 30.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.65× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 6.49× (z +9.4) | — |
| [[A498 (line)]] | wt | 10.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.02× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.36× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 35.5 | 1 | 2 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 3.49× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 9.30 | 1 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 2.19× (z +11.1) ⚠ position not correctable | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 17.6 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.254× (z -9.4) |
| [[A549 (line)]] | wt | 8.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 33.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 19.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.51× (z +10.2) | — |
| [[J82 (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 41.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0852× (z -17.0) |
| [[A-427 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.48 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.69 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.69 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9535), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00592]] | +0.67 | +0.66 / +0.70 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ANXA3]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[IL18]] | +0.59 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[AJUBA]] | +0.59 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[LINC00857]] | +0.59 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[SH3RF2]] | +0.59 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[LGALSL]] | +0.58 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[KRTAP5-AS1]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[CFL2]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[CLDN1]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[AMOTL2]] | +0.58 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[RBMS2]] | +0.57 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[TRIM58]] | +0.57 | +0.42 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SENP5]] | -0.55 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[QPCTL]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[SMG1P5]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[SNHG30]] | -0.48 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ANKRD13D]] | -0.47 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[ZNF487]] | -0.47 | -0.26 / -0.54 | both halves | 3e-04 |  |
| [[MED31]] | -0.46 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[TNPO3]] | -0.46 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[RABEP2]] | -0.45 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[NFATC2IP]] | -0.45 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[SDF2]] | -0.44 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[FBXL12]] | -0.44 | -0.32 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 6, C 22. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXADR]] | B | CXADR activity raises KRT80's level | lines that do not express CXADR (16) vs lines expressing it (34) | 2.68× lower at baseline in the lines without CXADR | 0.020 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[GPR87]] | B | GPR87 activity raises KRT80's level | lines that do not express GPR87 (36) vs lines expressing it (14) | 2.62× lower at baseline in the lines without GPR87 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1 |
| [[COL16A1]] | B | COL16A1 activity raises KRT80's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 2.16× lower at baseline in the lines without COL16A1 | 0.025 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers KRT80's level | compounds that target MAP2K1: 4 of 4 raise it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 8.7% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds |
| [[WWC1]] | B | WWC1 activity raises KRT80's level | lines that do not express WWC1 (13) vs lines expressing it (37) | 3.27× lower at baseline in the lines without WWC1 | 0.079 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CHMP4C, LSR; maybe low, not absent |
| [[SAMD12]] | B | SAMD12 activity raises KRT80's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 2.94× lower at baseline in the lines without SAMD12 | 0.082 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[ARHGEF38]] | C | ARHGEF38 activity raises KRT80's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 7.18× lower at baseline in the lines without ARHGEF38 | 8e-05 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1; co-absent with the target |
| [[ANXA3]] | C | ANXA3 activity raises KRT80's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 5.45× lower at baseline in the lines without ANXA3 | 1e-04 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132; co-absent with the target |
| [[TRIM29]] | C | TRIM29 activity raises KRT80's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 5.48× lower at baseline in the lines without TRIM29 | 3e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2; co-absent with the target |
| [[MACC1]] | C | MACC1 activity raises KRT80's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 6.76× lower at baseline in the lines without MACC1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2; co-absent with the target |
| [[MISP]] | C | MISP activity raises KRT80's level | lines that do not express MISP (23) vs lines expressing it (27) | 5.04× lower at baseline in the lines without MISP | 0.001 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B; co-absent with the target |
| [[ELF3-AS1]] | C | ELF3-AS1 activity raises KRT80's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 4.38× lower at baseline in the lines without ELF3-AS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 13, C 19. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00592]] | B | KRT80 activity raises LINC00592's level | lines that do not express KRT80 (22) vs lines expressing it (28) | 1.80× lower at baseline in the lines without KRT80 | 0.003 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2 |
| [[TMEM184A]] | B | KRT80 activity raises TMEM184A's level | lines that do not express KRT80 (22) vs lines expressing it (28) | 2.39× lower at baseline in the lines without KRT80 | 0.014 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2 |
| [[LINC01186]] | B | KRT80 activity raises LINC01186's level | lines that do not express KRT80 (22) vs lines expressing it (28) | 2.19× lower at baseline in the lines without KRT80 | 0.031 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2 |
| [[TUFT1]] | B | KRT80 activity raises TUFT1's level | lines that do not express KRT80 (22) vs lines expressing it (28) | 2.49× lower at baseline in the lines without KRT80 | 0.032 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2 |
| [[KRTAP5-AS1]] | B | KRT80 activity raises KRTAP5-AS1's level | lines that do not express KRT80 (22) vs lines expressing it (28) | 2.09× lower at baseline in the lines without KRT80 | 0.039 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2 |
| [[PLXNB2]] | B | KRT80 activity raises PLXNB2's level | lines that do not express KRT80 (22) vs lines expressing it (28) | 1.62× lower at baseline in the lines without KRT80 | 0.050 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2 |
| [[WWC1]] | B | KRT80 activity raises WWC1's level | lines that do not express KRT80 (22) vs lines expressing it (28) | 2.85× lower at baseline in the lines without KRT80 | 0.064 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2 |
| [[C4orf19]] | B | KRT80 activity raises C4orf19's level | lines that do not express KRT80 (22) vs lines expressing it (28) | 2.16× lower at baseline in the lines without KRT80 | 0.077 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2 |
| [[COL12A1]] | B | KRT80 activity lowers COL12A1's level | lines that do not express KRT80 (22) vs lines expressing it (28) | 3.13× higher at baseline in the lines without KRT80 | 0.093 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2 |
| [[TAF5]] | B | KRT80 activity lowers TAF5's level | lines that do not express KRT80 (22) vs lines expressing it (28) | 1.19× higher at baseline in the lines without KRT80 | 0.094 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2 |
| [[PLXNB2]] | B | KRT80 activity strengthens PLXNB2's drug response | lines that do not express KRT80 (20) vs lines expressing it (27) | the lines without KRT80 respond 0.70× as strongly (z diff +1.00); strongest at Panobinostat 0.5 µM: 0.55x vs 0.41x (z diff +2.7) | 0.097 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2; target measured in part of the lines; artifact flags |
| [[TES]] | B | KRT80 activity raises TES's level | lines that do not express KRT80 (22) vs lines expressing it (28) | 2.59× lower at baseline in the lines without KRT80 | 0.099 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2 |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.583). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.3, 12.0); signed map (48.6, 15.9). **Vector** length 94.5, 27.3% of its response variance represented; |z| ≥ 3 in 828 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Signaling by Hippo* (reactome, mean cos +0.51 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +17.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +14.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +9.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.6 | +5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.9 | +6.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.8 | +4.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.8 | +5.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -8.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.4 | -7.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -2.3 | -5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -2.1 | -4.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.0 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -7.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.5 | -3.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.3 | -1.7 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | keratin 80 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:52,168,996-52,192,014 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KB20 |
| Gene groups (HGNC) | Keratins, type II |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

UniProt [Q6KB66](https://www.uniprot.org/uniprotkb/Q6KB66) carries no function annotation.

**Summary**, from NCBI Gene [144501](https://www.ncbi.nlm.nih.gov/gene/144501):

> Keratins are intermediate filament proteins responsible for the structural integrity of epithelial cells and are subdivided into epithelial keratins and hair keratins. This gene's expression profile shows that it encodes a type II epithelial keratin, although structurally the encoded protein is more like a type II hair keratin. This protein is involved in cell differentiation, localizing near desmosomal plaques in earlier stages of differentiation but then dispersing throughout the cytoplasm in …

**Accessions** — [HGNC:27056](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27056) · Entrez [144501](https://www.ncbi.nlm.nih.gov/gene/144501) · UniProt [Q6KB66](https://www.uniprot.org/uniprotkb/Q6KB66) · Ensembl [ENSG00000167767](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167767)

## Data

Gene col 9535: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9535); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9535, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9535]; `tensor/DDL_lfc|DDL_z.npy` [9535]; `embed/gene_vectors.npy` [9535]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9535 or target_col == 9535). Every well: [[KRT80 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRT80.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
