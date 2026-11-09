---
symbol: "NPL"
type: "gene"
col: 5765
ensembl_id: "ENSG00000135838"
name: "N-acetylneuraminate pyruvate lyase"
location: "1q25.3"
module: 125
arm: "+"
pooled_cpm: 5.87
n_lines_expressing: 43
n_dd_up: 44
n_dd_down: 5
n_dd_up_clean: 26
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# NPL

*N-acetylneuraminate pyruvate lyase* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.06× (z +25.2, q 0e+00, up in 32 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.467× (z -9.7, q 2e-19, down in 20 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.551× (z -7.6, q 8e-12, down in 19 of 40 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALOXE3]] (+0.62, fdr 7e-06), [[LACC1]] (+0.59, fdr 2e-05), [[GLRX2]] (+0.55, fdr 1e-05); moves opposite to [[CEP43]] (-0.63, fdr 7e-06), [[TCTN3]] (-0.58, fdr 5e-05), [[SIN3A]] (-0.57, fdr 2e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[EML5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5765.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.06×** | +25.2 | 0e+00 | 32/35 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **5.86×** | +22.5 | 0e+00 | 38/40 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.34×** | +21.3 | 0e+00 | 36/38 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.12×** | +20.5 | 0e+00 | 36/38 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **3.79×** | +16.9 | 0e+00 | 34/39 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.07×** | +14.3 | 3e-44 | 32/37 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.19×** | +14.2 | 8e-44 | 32/38 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **2.85×** | +12.8 | 1e-35 | 20/25 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.63×** | +12.3 | 6e-33 | 25/34 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.59×** | +12.0 | 2e-31 | 33/40 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.40×** | +11.1 | 5e-27 | 29/39 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.48×** | +11.1 | 7e-27 | 23/31 (NCI-H460, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.37×** | +11.0 | 2e-26 | 27/38 (SW480, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.82×** | +10.7 | 4e-25 | 19/34 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +8.6 | 2e-16 | 3/9 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.92×** | +8.3 | 4e-15 | 24/39 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.7 | 8e-10 | 16/40 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.55×** | +5.6 | 6e-07 | 10/38 (A498, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.55×** | +5.5 | 8e-07 | 14/38 (A-172, A-427, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.21×** | +5.3 | 3e-06 | 10/37 (PANC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5765.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.467×** | -9.7 | 2e-19 | 20/30 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.551×** | -7.6 | 8e-12 | 19/40 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.601×** | -6.5 | 1e-08 | 17/38 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.639×** | -5.7 | 1e-06 | 18/38 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.569×** | -3.8 | 0.019 | 12/36 (A-427, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Rutin (trihydrate) (drug)]] 5 µM |  | 0.775× | -3.1 | 0.16 | 8/38 (SW 900, SW1417, …) | top dose only |  |
| [[Fluvoxamine (drug)]] 0.05 µM |  | 0.772× | -3.1 | 0.17 | 1/38 (CFPAC-1) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.63 per unit of S-phase module lfc, -0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5765. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.80 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +14.5) | — |
| [[NCI-H460 (line)]] | wt | 11.8 | 5 (1 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.40× (z +11.5) | [[Digitoxin (drug)]] 5 µM 0.154× (z -12.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 12.5 | 2 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.74× (z +9.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -11.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -9.3) |
| [[PANC-1 (line)]] | alt | 3.51 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 11.9× (z +11.6) | — |
| [[A-172 (line)]] | wt | 3.60 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 23.9× (z +9.9) | [[Carbamazepine (drug)]] 5 µM 0.0661× (z -8.8) |
| [[A498 (line)]] | wt | 7.89 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 9.46× (z +11.8) | — |
| [[C32 (line)]] | wt | 15.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +9.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0950× (z -10.6) |
| [[COLO 205 (line)]] | alt | 12.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +8.5) | [[Sacubitril_Valsartan (drug)]] 0.05 µM 0.0558× (z -10.2) |
| [[HT-29 (line)]] | alt | 15.0 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.25× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[LS 180 (line)]] | wt | 6.69 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +10.5) | [[Digitoxin (drug)]] 5 µM 0.104× (z -9.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 2.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 3.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +12.3) | — |
| [[HEC-1-A (line)]] | alt | 1.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 7.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +9.3) | — |
| [[hTERT-HPNE (line)]] | wt | 6.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +11.2) | — |
| [[J82 (line)]] | alt | 8.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +12.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.04 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.97× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 6.57 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.108× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 17.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +11.3) | — |
| [[NCI-H23 (line)]] | alt | 5.66 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0828× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 3.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.57× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 6.05 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.46× (z +8.9) | — |
| [[A549 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.756 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.599 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5765), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALOXE3]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[LACC1]] | +0.59 | +0.75 / +0.47 | both halves | 2e-05 |  |
| [[GLRX2]] | +0.55 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[RPLP0P2]] | +0.54 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[CD22]] | +0.53 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[GLIPR2]] | +0.53 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[PTER]] | +0.52 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[TTPAL]] | +0.51 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CCDC136]] | +0.51 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[GADD45A]] | +0.51 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[NEDD4]] | +0.51 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[GALNT9]] | +0.50 | +0.44 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP43]] | -0.63 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[TCTN3]] | -0.58 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[SIN3A]] | -0.57 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[ATF6B]] | -0.56 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[PIGN]] | -0.55 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[PIGS]] | -0.53 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[TCTN2]] | -0.53 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[ULK4]] | -0.53 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[ZNF487]] | -0.52 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[CD46]] | -0.51 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[DCAF11]] | -0.51 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[CMC2]] | -0.51 | -0.56 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NPL's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.3% of all compounds | 0.010 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[SUGCT]] | C | SUGCT activity lowers NPL's level | lines that do not express SUGCT (4) vs lines expressing it (46) | 1.38× higher at baseline in the lines without SUGCT | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, CABYR, HHAT; maybe low, not absent; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EML5]] | B | NPL activity raises EML5's level | lines that do not express NPL (7) vs lines expressing it (43) | 2.77× lower at baseline in the lines without NPL | 0.060 | ⚠ within organs, on part of the lines; also absent: IQCJ-SCHIP1, NPR2, CAPS2; maybe low, not absent; its own permutation p |
| [[LRIF1]] | B | NPL activity raises LRIF1's level | lines that do not express NPL (7) vs lines expressing it (43) | 2.57× lower at baseline in the lines without NPL | 0.060 | ⚠ within organs, on part of the lines; also absent: IQCJ-SCHIP1, NPR2, CAPS2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.438). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.9, 4.8); signed map (22.9, 17.5). **Vector** length 63.2, 10.2% of its response variance represented; |z| ≥ 3 in 1,248 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +20.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +14.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +14.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +25.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.6 | +12.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +11.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +5.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.9 | -5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -7.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +2.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.8 | -9.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -0.9 | +1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -0.9 | +1.3 |
|  | [[Sodium Salicylate (drug)]] 5 µM |  | -0.9 | -0.3 |
|  | [[Ixazomib (drug)]] 5 µM |  | -0.9 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | N-acetylneuraminate pyruvate lyase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:182,789,293-182,830,384 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NPL1, DHDPS1; previously C1orf13 |
| Gene groups (HGNC) | Oxo-acid lyases |
| Reactome | 4 pathways, smallest: Sialic acid metabolism; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXD5](https://www.uniprot.org/uniprotkb/Q9BXD5) (N-acetylneuraminate lyase):

> Catalyzes the cleavage of N-acetylneuraminic acid (sialic acid) to form pyruvate and N-acetylmannosamine via a Schiff base intermediate. It prevents sialic acids from being recycled and returning to the cell surface. Involved in the N-glycolylneuraminic acid (Neu5Gc) degradation pathway. Although human is not able to catalyze formation of Neu5Gc due to the inactive CMAHP enzyme, Neu5Gc is present in food and must be degraded (Probable).

**Summary**, from NCBI Gene [80896](https://www.ncbi.nlm.nih.gov/gene/80896):

> This gene encodes a member of the N-acetylneuraminate lyase sub-family of (beta/alpha)(8)-barrel enzymes. N-acetylneuraminate lyases regulate cellular concentrations of N-acetyl-neuraminic acid (sialic acid) by mediating the reversible conversion of sialic acid into N-acetylmannosamine and pyruvate. A pseudogene of this gene is located on the short arm of chromosome 2. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jan …

**Accessions** — [HGNC:16781](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16781) · Entrez [80896](https://www.ncbi.nlm.nih.gov/gene/80896) · UniProt [Q9BXD5](https://www.uniprot.org/uniprotkb/Q9BXD5) · Ensembl [ENSG00000135838](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135838)

## Data

Gene col 5765: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5765); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5765, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5765]; `tensor/DDL_lfc|DDL_z.npy` [5765]; `embed/gene_vectors.npy` [5765]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5765 or target_col == 5765). Every well: [[NPL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
