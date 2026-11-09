---
symbol: "WASF3"
type: "gene"
col: 5400
ensembl_id: "ENSG00000132970"
name: "WASP family member 3"
location: "13q12.13"
module: 95
arm: "-"
pooled_cpm: 24.39
n_lines_expressing: 29
n_dd_up: 14
n_dd_down: 15
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 6
direction_downstream: 6
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# WASF3

*WASP family member 3* — 13q12.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.77× (z +19.6, q 0e+00, up in 25 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.342× (z -19.8, q 0e+00, down in 24 of 26 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HACE1]] (+0.77, fdr 7e-06), [[FAM234B]] (+0.74, fdr 7e-06), [[JAM3]] (+0.73, fdr 7e-06); moves opposite to [[SLC9A8]] (-0.76, fdr 7e-06), [[BAZ2B]] (-0.75, fdr 1e-05), [[GGPS1]] (-0.75, fdr 1e-05).
> It sits in the **-** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[MMP17]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5400.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.77×** | +19.6 | 0e+00 | 25/26 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.48×** | +17.5 | 0e+00 | 24/26 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.13×** | +14.5 | 1e-45 | 24/26 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.09×** | +14.2 | 1e-43 | 22/26 (NCI-H2030, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +12.6 | 3e-34 | 21/27 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +9.2 | 2e-18 | 18/25 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +9.2 | 2e-18 | 19/25 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.59×** | +9.1 | 4e-18 | 21/27 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +5.0 | 3e-05 | 5/27 (SW 900, RPMI-7951, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.30×** | +4.7 | 1e-04 | 9/25 (LoVo, H4, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.9 | 0.006 | 12/26 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.7 | 0.009 | 10/23 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.21×** | +3.6 | 0.012 | 9/26 (HOP62, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.037 | 4/26 (SW480, A-427, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5400.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.342×** | -19.8 | 0e+00 | 24/26 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.489×** | -19.4 | 0e+00 | 24/27 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.468×** | -14.5 | 1e-45 | 23/26 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.471×** | -14.5 | 4e-45 | 25/26 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.534×** | -12.0 | 3e-31 | 20/25 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.570×** | -10.8 | 4e-25 | 20/26 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.575×** | -10.6 | 2e-24 | 21/26 (hTERT-HPNE, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.640×** | -8.6 | 8e-16 | 18/26 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.730×** | -8.5 | 1e-15 | 21/27 (SW480, SNU-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.824×** | -5.2 | 9e-06 | 14/26 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.753×** | -5.2 | 9e-06 | 15/24 (SNU-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.754×** | -5.2 | 9e-06 | 12/25 (C32, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.823×** | -3.7 | 0.008 | 11/27 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.829×** | -3.5 | 0.021 | 15/26 (C32, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | 0.835× | -3.4 | 0.021 | 0/27 | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.842× | -3.3 | 0.035 | 11/26 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.831×** | -3.3 | 0.035 | 6/25 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 0.855× | -3.0 | 0.077 | 14/26 (SW480, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5400. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.2 | 1 | 9 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.39× (z +8.9) | [[Harringtonine (drug)]] 5 µM 0.117× (z -21.2) |
| [[SNU-1 (line)]] | wt | 79.1 | 0 | 9 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.115× (z -16.6) |
| [[hTERT-HPNE (line)]] | wt | 71.8 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.188× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 19.0 | 3 (1 ⚠) | 5 | [[Panobinostat (drug)]] 5 µM 3.45× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -15.0) |
| [[C32 (line)]] | wt | 126 | 1 | 6 (1 ⚠) | [[Ponatinib (drug)]] 5 µM 3.00× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -17.5) |
| [[HEC-1-A (line)]] | alt | 46.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -14.7) |
| [[NCI-H23 (line)]] | alt | 34.3 | 2 | 4 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.05× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -17.8) |
| [[PANC-1 (line)]] | alt | 41.2 | 2 | 4 | [[Panobinostat (drug)]] 5 µM 2.63× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -20.5) |
| [[A-172 (line)]] | wt | 31.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -13.1) |
| [[J82 (line)]] | alt | 80.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -20.0) |
| [[Panc 03.27 (line)]] | alt | 17.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.73× (z +9.2) | — |
| [[SW480 (line)]] | alt | 61.5 | 0 | 4 | — | [[Auranofin (drug)]] 5 µM 0.467× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 19.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.223× (z -9.3) |
| [[HOP62 (line)]] | alt | 29.6 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.221× (z -12.6) |
| [[LoVo (line)]] | wt | 17.9 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 3.16× (z +9.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -9.4) |
| [[C-33 A (line)]] | alt | 98.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0818× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 7.47 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.11× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 33.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0827× (z -16.3) |
| [[SW 900 (line)]] | alt | 45.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.276× (z -9.3) |
| [[A-427 (line)]] | wt | 33.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 30.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.268× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~11% of this change |
| [[H4 (line)]] | wt | 27.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 20.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.0) |
| [[A498 (line)]] | wt | 4.87 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.38 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.03 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.65 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5400), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACE1]] | +0.77 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[FAM234B]] | +0.74 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[JAM3]] | +0.73 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[RAB6B]] | +0.73 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ARL6]] | +0.72 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[METAP1]] | +0.72 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[PACC1]] | +0.70 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[POMGNT2]] | +0.70 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.70 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[GRB2]] | +0.70 | +0.67 / +0.58 | both halves | 7e-06 | pathway: FCGR3A-mediated phagocytosis; STRING 543 |
| [[TPD52]] | +0.70 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[MAPT]] | +0.70 | +0.66 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A8]] | -0.76 | -0.70 / -0.62 | both halves | 7e-06 |  |
| [[BAZ2B]] | -0.75 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[GGPS1]] | -0.75 | -0.73 / -0.51 | both halves | 1e-05 |  |
| [[INO80D]] | -0.75 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[WARS2-AS1]] | -0.74 | -0.71 / -0.43 | both halves | 3e-05 |  |
| [[LINC01004]] | -0.74 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[C11orf58]] | -0.72 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[PATL2]] | -0.72 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[TAPBPL]] | -0.71 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[PCNX4-DT]] | -0.71 | -0.65 / -0.34 | both halves | 1e-04 |  |
| [[CREBBP]] | -0.71 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[UNK]] | -0.71 | -0.69 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises WASF3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GNAO1]] | B | GNAO1 activity raises WASF3's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 2.81× lower at baseline in the lines without GNAO1 | 0.089 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[FAM124A]] | B | FAM124A activity raises WASF3's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 3.17× lower at baseline in the lines without FAM124A | 0.099 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1 |
| [[IGF2BP1]] | C | IGF2BP1 activity raises WASF3's level | lines that do not express IGF2BP1 (23) vs lines expressing it (27) | 3.40× lower at baseline in the lines without IGF2BP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: SLFN11, RUNX3, DPY19L2; co-absent with the target |
| [[COL4A4]] | C | COL4A4 activity raises WASF3's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 2.89× lower at baseline in the lines without COL4A4 | 0.040 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A; co-absent with the target |
| [[EBF2]] | C | EBF2 activity raises WASF3's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 2.83× lower at baseline in the lines without EBF2 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP17]] | B | WASF3 activity raises MMP17's level | lines that do not express WASF3 (21) vs lines expressing it (29) | 2.28× lower at baseline in the lines without WASF3 | 0.017 | ⚠ within organs, on part of the lines; also absent: SDC2, COL4A4, IGF2BP1 |
| [[PBLD]] | B | WASF3 activity raises PBLD's level | lines that do not express WASF3 (21) vs lines expressing it (29) | 1.32× lower at baseline in the lines without WASF3 | 0.025 | ⚠ within organs, on part of the lines; also absent: SDC2, COL4A4, IGF2BP1 |
| [[ERMAP]] | B | WASF3 activity raises ERMAP's level | lines that do not express WASF3 (21) vs lines expressing it (29) | 1.17× lower at baseline in the lines without WASF3 | 0.048 | ⚠ within organs, on part of the lines; also absent: SDC2, COL4A4, IGF2BP1 |
| [[GPD1L]] | B | WASF3 activity lowers GPD1L's level | lines that do not express WASF3 (21) vs lines expressing it (29) | 1.68× higher at baseline in the lines without WASF3 | 0.057 | ⚠ within organs, on part of the lines; also absent: SDC2, COL4A4, IGF2BP1 |
| [[MMADHC-DT]] | B | WASF3 activity raises MMADHC-DT's level | lines that do not express WASF3 (21) vs lines expressing it (29) | 1.20× lower at baseline in the lines without WASF3 | 0.069 | ⚠ within organs, on part of the lines; also absent: SDC2, COL4A4, IGF2BP1 |
| [[COLQ]] | B | WASF3 activity raises COLQ's level | lines that do not express WASF3 (21) vs lines expressing it (29) | 1.49× lower at baseline in the lines without WASF3 | 0.076 | ⚠ within organs, on part of the lines; also absent: SDC2, COL4A4, IGF2BP1 |

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **-** arm (projection on the module's main direction -0.818). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (3.4, 7.1); signed map (-38.6, -7.3). **Vector** length 85.4, 22.6% of its response variance represented; |z| ≥ 3 in 741 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +12.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.2 | +17.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.1 | +14.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.4 | +19.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.3 | +14.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +9.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +5.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.2 | -19.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -14.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -19.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -8.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.3 | -14.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -3.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.7 | -0.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | WASP family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.13 — chr13:26,557,683-26,688,948 (+) |
| Ensembl biotype | protein_coding |
| Also known as | WAVE3, SCAR3, KIAA0900 |
| Gene groups (HGNC) | Wiskott-Aldrich Syndrome protein family |
| Reactome | 17 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; FCGR3A-mediated phagocytosis; Leishmania phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPY6](https://www.uniprot.org/uniprotkb/Q9UPY6) (Actin-binding protein WASF3):

> Downstream effector molecules involved in the transmission of signals from tyrosine kinase receptors and small GTPases to the actin cytoskeleton. Required for regulation of cell morphology and cytoskeletal organization.

**Summary**, from NCBI Gene [10810](https://www.ncbi.nlm.nih.gov/gene/10810):

> This gene encodes a member of the Wiskott-Aldrich syndrome protein family. The gene product is a protein that forms a multiprotein complex that links receptor kinases and actin. Binding to actin occurs through a C-terminal verprolin homology domain in all family members. The multiprotein complex serves to tranduce signals that involve changes in cell shape, motility or function. A pseudogene of this gene have been defined on chromosome 6. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:12734](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12734) · Entrez [10810](https://www.ncbi.nlm.nih.gov/gene/10810) · UniProt [Q9UPY6](https://www.uniprot.org/uniprotkb/Q9UPY6) · Ensembl [ENSG00000132970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132970)

## Data

Gene col 5400: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5400); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5400, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5400]; `tensor/DDL_lfc|DDL_z.npy` [5400]; `embed/gene_vectors.npy` [5400]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5400 or target_col == 5400). Every well: [[WASF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WASF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
