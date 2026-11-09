---
symbol: "VSIR"
type: "gene"
col: 2873
ensembl_id: "ENSG00000107738"
name: "V-set immunoregulatory receptor"
location: "10q22.1"
module: 31
arm: "+"
pooled_cpm: 7.38
n_lines_expressing: 36
n_dd_up: 19
n_dd_down: 20
n_dd_up_clean: 15
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 14
direction_downstream: 18
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# VSIR

*V-set immunoregulatory receptor* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.03× (z +13.5, q 1e-38, up in 27 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.561× (z -7.7, q 8e-12, down in 18 of 32 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.404× (z -6.3, q 8e-08, down in 14 of 24 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP2]] (+0.59, fdr 2e-05), [[PCDH1]] (+0.58, fdr 2e-05), [[FCHO1]] (+0.57, fdr 6e-05); moves opposite to [[EFCAB2]] (-0.50, fdr 9e-05), [[NHSL1]] (-0.49, fdr 1e-04), [[PCBP1-AS1]] (-0.48, fdr 4e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[CAPG]] → it (grade B ⚠); 18 go from it, the strongest it → [[RIOK3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2873.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.03×** | +13.5 | 1e-38 | 27/33 (HOP62, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.24×** | +10.8 | 8e-25 | 22/32 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.13×** | +10.2 | 5e-22 | 20/32 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.10×** | +10.0 | 2e-21 | 21/31 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.04×** | +9.6 | 9e-20 | 24/32 (A549, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +7.6 | 3e-12 | 18/30 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +7.3 | 3e-11 | 4/13 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.21×** | +5.6 | 2e-06 | 13/30 (J82, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +5.1 | 2e-05 | 9/26 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.0 | 0.003 | 1/17 (LoVo) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.76×** | +4.0 | 0.003 | 11/26 (KATO III, J82, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.006 | 3/31 (PANC-1, A549, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.014 | 13/32 (J82, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.020 | 2/28 (Panc 03.27, SW1417) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +3.4 | 0.024 | 4/32 (SW 900, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.024 | 3/30 (KATO III, NCI-H460, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.066 | 4/32 (A498, SW 900, …) | inconsistent across doses | position effect removed |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.071 | 7/31 (J82, HEC-1-A, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2873.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.561×** | -7.7 | 8e-12 | 18/32 (SW1417, AsPC-1, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.404×** | -6.3 | 8e-08 | 14/24 (Hs 766T, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.427×** | -5.9 | 6e-07 | 14/27 (A498, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.650×** | -5.7 | 1e-06 | 14/32 (SNU-423, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -5.3 | 2e-05 | 15/27 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.499×** | -4.8 | 1e-04 | 12/29 (NCI-H1792, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.899× | -4.7 | 2e-04 | 6/33 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.697×** | -4.5 | 4e-04 | 6/32 (KATO III, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.716×** | -4.4 | 5e-04 | 9/31 (SW480, SW 900, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.716×** | -4.4 | 5e-04 | 8/32 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.715×** | -4.3 | 0.001 | 10/29 (HEC-1-A, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.735×** | -4.1 | 0.002 | 11/31 (Hs 766T, SW1417, …) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.746×** | -3.9 | 0.005 | 8/31 (SW 900, HOP62, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.594×** | -3.6 | 0.012 | 10/25 (Hs 766T, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.771×** | -3.4 | 0.023 | 11/27 (HOP62, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.618×** | -3.3 | 0.029 | 4/30 (SW1417, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.769×** | -3.3 | 0.036 | 9/31 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2873. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 36.1 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.167× (z -12.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 52.5 | 0 | 2 (1 ⚠) | — | [[EX229 (drug)]] 5 µM 0.0590× (z -8.9) |
| [[SW1417 (line)]] | alt | 20.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -13.8) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.351× (z -9.9) |
| [[A498 (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0960× (z -9.7) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -11.0) ⚠ cell-cycle shift, explains ~10% of this change |
| [[HEC-1-A (line)]] | alt | 14.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -9.1) |
| [[KATO III (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -10.8) ⚠ cell-cycle shift, explains ~10% of this change |
| [[NCI-H1792 (line)]] | alt | 5.81 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -8.8) ⚠ cell-cycle shift, explains ~10% of this change |
| [[Panc 03.27 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -8.8) ⚠ cell-cycle shift, explains ~10% of this change |
| [[SW 900 (line)]] | alt | 7.21 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0806× (z -9.3) |
| [[SW480 (line)]] | alt | 8.06 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.571 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.482 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.862 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.587 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.776 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.23 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2873), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP2]] | +0.59 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[PCDH1]] | +0.58 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[FCHO1]] | +0.57 | +0.39 / +0.45 | both halves | 6e-05 |  |
| [[DENND3]] | +0.56 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[HDAC11]] | +0.56 | +0.50 / +0.36 | both halves | 9e-05 |  |
| [[ABLIM2]] | +0.55 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[RASAL1]] | +0.55 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[FOXO6]] | +0.55 | +0.34 / +0.45 | both halves | 1e-04 |  |
| [[FKBP1B]] | +0.55 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[MAST3]] | +0.54 | +0.35 / +0.43 | both halves | 1e-04 |  |
| [[PTK2B]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[P2RY2]] | +0.53 | +0.43 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB2]] | -0.50 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[NHSL1]] | -0.49 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[PCBP1-AS1]] | -0.48 | -0.26 / -0.33 | both halves | 4e-04 |  |
| [[ZFP91]] | -0.47 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[MFF-DT]] | -0.46 | -0.25 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[METTL4]] | -0.46 | -0.20 / -0.39 | ⚠ not reproduced | 8e-04 |  |
| [[TTC6]] | -0.46 | -0.36 / -0.27 | both halves | 3e-04 |  |
| [[NMNAT1]] | -0.46 | -0.29 / -0.31 | both halves | 2e-04 |  |
| [[ATF5]] | -0.46 | -0.19 / -0.33 | ⚠ not reproduced | 8e-04 |  |
| [[DNAAF10]] | -0.45 | -0.29 / -0.24 | both halves | 4e-04 |  |
| [[PYCR2]] | -0.45 | -0.26 / -0.33 | both halves | 4e-04 |  |
| [[ZNF785]] | -0.45 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[PRKAR1B]] | -0.45 | -0.34 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAPG]] | B | CAPG activity raises VSIR's level | lines that do not express CAPG (17) vs lines expressing it (33) | 2.54× lower at baseline in the lines without CAPG | 0.003 | ⚠ within organs, on part of the lines; also absent: MALL, LINC02086, SH3RF2 |
| [[AFAP1L2]] | B | AFAP1L2 activity raises VSIR's level | lines that do not express AFAP1L2 (27) vs lines expressing it (23) | 2.04× lower at baseline in the lines without AFAP1L2 | 0.007 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH |
| [[ADRB2]] | B | ADRB2 activity raises VSIR's level | lines that do not express ADRB2 (23) vs lines expressing it (27) | 2.08× lower at baseline in the lines without ADRB2 | 0.008 | ⚠ within organs, on part of the lines; also absent: GBP5, ADAMTS16, ENSG00000271933 |
| [[ALS2CL]] | B | ALS2CL activity raises VSIR's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 2.39× lower at baseline in the lines without ALS2CL | 0.010 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[PCDH1]] | B | PCDH1 activity raises VSIR's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.12× lower at baseline in the lines without PCDH1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[PTK2B]] | B | PTK2B activity raises VSIR's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 2.28× lower at baseline in the lines without PTK2B | 0.051 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[P2RY2]] | B | P2RY2 activity raises VSIR's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.19× lower at baseline in the lines without P2RY2 | 0.054 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[RASSF4]] | B | RASSF4 activity raises VSIR's level | lines that do not express RASSF4 (11) vs lines expressing it (39) | 2.66× lower at baseline in the lines without RASSF4 | 0.059 | ⚠ within organs, on part of the lines; also absent: CTSS, SLC15A3, MX2; maybe low, not absent |
| [[LINC00482]] | B | LINC00482 activity raises VSIR's level | lines that do not express LINC00482 (8) vs lines expressing it (42) | 2.38× lower at baseline in the lines without LINC00482 | 0.060 | ⚠ within organs, on part of the lines; also absent: SOX13, SEPTIN9-DT |
| [[EEPD1]] | B | EEPD1 activity raises VSIR's level | lines that do not express EEPD1 (14) vs lines expressing it (36) | 1.96× lower at baseline in the lines without EEPD1 | 0.062 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent |
| [[CCDC120]] | B | CCDC120 activity raises VSIR's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 1.93× lower at baseline in the lines without CCDC120 | 0.063 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[JUP]] | B | JUP activity raises VSIR's level | lines that do not express JUP (16) vs lines expressing it (34) | 1.82× lower at baseline in the lines without JUP | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 18, C 0. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIOK3]] | B | VSIR activity raises RIOK3's level | lines that do not express VSIR (14) vs lines expressing it (36) | 1.67× lower at baseline in the lines without VSIR | 0.001 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[AFAP1L2]] | B | VSIR activity raises AFAP1L2's level | lines that do not express VSIR (14) vs lines expressing it (36) | 2.95× lower at baseline in the lines without VSIR | 0.002 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[BAIAP3]] | B | VSIR activity raises BAIAP3's level | lines that do not express VSIR (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without VSIR | 0.005 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[MAPK11]] | B | VSIR activity lowers MAPK11's level | lines that do not express VSIR (14) vs lines expressing it (36) | 1.53× higher at baseline in the lines without VSIR | 0.006 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[DENND3]] | B | VSIR activity raises DENND3's level | lines that do not express VSIR (14) vs lines expressing it (36) | 1.85× lower at baseline in the lines without VSIR | 0.013 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[CORO2A]] | B | VSIR activity raises CORO2A's level | lines that do not express VSIR (14) vs lines expressing it (36) | 1.97× lower at baseline in the lines without VSIR | 0.013 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[PCDH1]] | B | VSIR activity raises PCDH1's level | lines that do not express VSIR (14) vs lines expressing it (36) | 3.35× lower at baseline in the lines without VSIR | 0.020 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[PTK2B]] | B | VSIR activity raises PTK2B's level | lines that do not express VSIR (14) vs lines expressing it (36) | 2.24× lower at baseline in the lines without VSIR | 0.025 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[PDLIM1]] | B | VSIR activity raises PDLIM1's level | lines that do not express VSIR (14) vs lines expressing it (36) | 2.48× lower at baseline in the lines without VSIR | 0.030 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[JUP]] | B | VSIR activity raises JUP's level | lines that do not express VSIR (14) vs lines expressing it (36) | 2.49× lower at baseline in the lines without VSIR | 0.040 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[AHDC1]] | B | VSIR activity raises AHDC1's level | lines that do not express VSIR (14) vs lines expressing it (36) | 1.43× lower at baseline in the lines without VSIR | 0.041 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[ANXA11]] | B | VSIR activity raises ANXA11's level | lines that do not express VSIR (14) vs lines expressing it (36) | 1.91× lower at baseline in the lines without VSIR | 0.044 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.522). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.6, 33.9); signed map (-21.7, 33.0). **Vector** length 64.2, 13.2% of its response variance represented; |z| ≥ 3 in 741 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +13.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +7.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.6 | +9.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.6 | +10.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.4 | +10.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +2.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +1.2 | +1.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.7 | -7.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -5.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -5.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.9 | -4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.7 | -3.6 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -6.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | V-set immunoregulatory receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:71,747,556-71,773,520 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SISP1, GI24, B7-H5, B7H5, VISTA, PD-1H, Dies1; previously C10orf54 |
| Gene groups (HGNC) | V-set domain containing; B7 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7M9](https://www.uniprot.org/uniprotkb/Q9H7M9) (V-type immunoglobulin domain-containing suppressor of T-cell activation):

> Immunoregulatory receptor which inhibits the T-cell response. May promote differentiation of embryonic stem cells, by inhibiting BMP4 signaling (By similarity). May stimulate MMP14-mediated MMP2 activation.

**Summary**, from NCBI Gene [64115](https://www.ncbi.nlm.nih.gov/gene/64115):

> Enables endopeptidase activator activity; enzyme binding activity; and identical protein binding activity. Involved in several processes, including negative regulation of cytokine production; positive regulation of collagen catabolic process; and regulation of T cell activation. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30085](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30085) · Entrez [64115](https://www.ncbi.nlm.nih.gov/gene/64115) · UniProt [Q9H7M9](https://www.uniprot.org/uniprotkb/Q9H7M9) · Ensembl [ENSG00000107738](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107738)

## Data

Gene col 2873: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2873); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2873, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2873]; `tensor/DDL_lfc|DDL_z.npy` [2873]; `embed/gene_vectors.npy` [2873]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2873 or target_col == 2873). Every well: [[VSIR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VSIR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
