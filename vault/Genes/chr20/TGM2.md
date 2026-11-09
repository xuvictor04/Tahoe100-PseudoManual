---
symbol: "TGM2"
type: "gene"
col: 12756
ensembl_id: "ENSG00000198959"
name: "transglutaminase 2"
location: "20q11.23"
module: 174
arm: "+"
pooled_cpm: 128.69
n_lines_expressing: 34
n_dd_up: 6
n_dd_down: 64
n_dd_up_clean: 3
n_dd_down_clean: 58
in_vector_space: true
direction_upstream: 6
direction_downstream: 15
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# TGM2

*transglutaminase 2* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.38× (z +7.2, q 4e-10, up in 21 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.47× (z +6.1, q 2e-07, up in 23 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 64 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.148× (z -29.9, q 0e+00, down in 32 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NIBAN2]] (+0.69, fdr 7e-06), [[HPCAL1]] (+0.64, fdr 1e-05), [[ITGA3]] (+0.63, fdr 7e-06); moves opposite to [[ATP6V0D1-DT]] (-0.56, fdr 3e-05), [[GPRASP3]] (-0.54, fdr 2e-05), [[HOXD3]] (-0.54, fdr 5e-05).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 15 go from it, the strongest it → [[HPCAL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12756.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +7.2 | 4e-10 | 21/33 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +6.9 | 1e-09 | 16/28 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +6.1 | 2e-07 | 23/32 (PANC-1, hTERT-HPNE, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +5.5 | 5e-06 | 17/29 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.52×** | +4.7 | 3e-04 | 26/32 (LOX-IMVI, CFPAC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +4.4 | 0.001 | 23/33 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.32× | +3.1 | 0.18 | 13/32 (NCI-H1792, SW 900, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 66 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 64 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12756.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.148×** | -29.9 | 0e+00 | 32/32 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.190×** | -18.3 | 0e+00 | 31/32 (Hs 766T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.345×** | -16.6 | 0e+00 | 30/33 (Hs 766T, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.342×** | -11.9 | 3e-30 | 32/32 (HOP62, HT-29, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.385×** | -10.2 | 4e-22 | 29/32 (Hs 766T, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.534×** | -9.8 | 1e-20 | 26/32 (J82, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.421×** | -9.2 | 3e-18 | 24/31 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.437×** | -9.1 | 4e-18 | 29/32 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.456×** | -8.7 | 3e-16 | 28/32 (HOP62, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.495×** | -7.8 | 5e-13 | 27/32 (Hs 766T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.500×** | -7.2 | 2e-11 | 26/32 (SNU-423, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.530×** | -7.0 | 1e-10 | 27/32 (Hs 766T, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.530×** | -7.0 | 1e-10 | 26/32 (SW 900, RPMI-7951, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.527×** | -6.8 | 4e-10 | 25/32 (HT-29, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.587×** | -5.9 | 2e-07 | 23/32 (HS-578T, J82, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **0.629×** | -5.7 | 6e-07 | 19/34 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.699×** | -5.6 | 8e-07 | 22/33 (KATO III, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.607×** | -5.5 | 1e-06 | 22/32 (SW 900, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12756. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 81.0 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0901× (z -20.8) |
| [[SW480 (line)]] | alt | 148 | 3 (3 ⚠) | 10 | [[Dinaciclib (drug)]] 5 µM 5.86× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -16.0) |
| [[Hs 766T (line)]] | wt | 533 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0407× (z -45.9) |
| [[KATO III (line)]] | alt | 56.1 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -17.0) |
| [[HOP62 (line)]] | alt | 136 | 1 (1 ⚠) | 9 | [[Dinaciclib (drug)]] 5 µM 4.32× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -21.1) |
| [[SW 900 (line)]] | alt | 125 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0597× (z -26.9) |
| [[A549 (line)]] | wt | 295 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0543× (z -25.4) |
| [[BT-474 (line)]] | alt | 33.0 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0922× (z -17.5) |
| [[HS-578T (line)]] | alt | 44.0 | 0 | 7 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.120× (z -12.5) |
| [[HT-29 (line)]] | alt | 63.1 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0725× (z -21.7) |
| [[A498 (line)]] | wt | 197 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -19.8) |
| [[NCI-H2030 (line)]] | alt | 113 | 4 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.19× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -15.3) |
| [[COLO 205 (line)]] | alt | 34.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 39.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -16.4) |
| [[HepG2_C3A (line)]] | wt | 90.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -16.1) |
| [[NCI-H1792 (line)]] | alt | 407 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -16.0) |
| [[PANC-1 (line)]] | alt | 55.3 | 2 (1 ⚠) | 3 | [[Panobinostat (drug)]] 0.05 µM 4.06× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.33× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -20.0) |
| [[RPMI-7951 (line)]] | alt | 403 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.07× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -24.2) |
| [[MIA PaCa-2 (line)]] | alt | 202 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -16.4) |
| [[NCI-H2347 (line)]] | alt | 40.5 | 1 | 3 | [[Tucidinostat (drug)]] 5 µM 2.24× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -22.2) |
| [[Panc 03.27 (line)]] | alt | 523 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -25.2) |
| [[SNU-423 (line)]] | alt | 182 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0745× (z -17.9) |
| [[AsPC-1 (line)]] | alt | 368 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0866× (z -33.3) |
| [[CFPAC-1 (line)]] | alt | 660 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -29.0) |
| [[hTERT-HPNE (line)]] | wt | 91.2 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 2.66× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -9.7) |
| [[A-427 (line)]] | wt | 248 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 154 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 35.0 | 1 | 0 | [[Retinoic acid (drug)]] 5 µM 3.05× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 39.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -10.1) |
| [[SW1417 (line)]] | alt | 86.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -11.7) |
| [[A-172 (line)]] | wt | 30.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.12 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 24.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.1 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.94 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.52 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.84 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.39 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 99.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.7 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.79 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.47 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12756), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIBAN2]] | +0.69 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[HPCAL1]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ITGA3]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[SERPINE1]] | +0.61 | +0.60 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 410 |
| [[ADGRE2]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[MICAL2]] | +0.60 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[PTPN12]] | +0.59 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[MPRIP]] | +0.58 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[NDFIP2]] | +0.58 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[DIAPH1]] | +0.57 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[ITGB3]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[STK24]] | +0.56 | +0.59 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V0D1-DT]] | -0.56 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[GPRASP3]] | -0.54 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[HOXD3]] | -0.54 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[ZBED3]] | -0.54 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ZCCHC8]] | -0.54 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[RWDD3]] | -0.53 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ATF5]] | -0.52 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[UFC1]] | -0.52 | -0.36 / -0.36 | both halves | 9e-05 |  |
| [[TSTD3]] | -0.52 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[KIF13A]] | -0.52 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[TRPM7]] | -0.52 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[YBEY]] | -0.51 | -0.43 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises TGM2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 11.2% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PTPRE]] | B | PTPRE activity raises TGM2's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 1.79× lower at baseline in the lines without PTPRE | 0.073 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[ITGA3]] | B | ITGA3 activity raises TGM2's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 3.96× lower at baseline in the lines without ITGA3 | 0.079 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[TNFRSF6B]] | B | TNFRSF6B activity raises TGM2's level | lines that do not express TNFRSF6B (33) vs lines expressing it (17) | 3.32× lower at baseline in the lines without TNFRSF6B | 0.080 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19 |
| [[PLS3-AS1]] | B | PLS3-AS1 activity raises TGM2's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 3.13× lower at baseline in the lines without PLS3-AS1 | 0.091 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |
| [[ITGB3]] | C | ITGB3 activity raises TGM2's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 3.75× lower at baseline in the lines without ITGB3 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 14, C 1. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HPCAL1]] | B | TGM2 activity raises HPCAL1's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 2.47× lower at baseline in the lines without TGM2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[ITGA3]] | B | TGM2 activity raises ITGA3's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 2.63× lower at baseline in the lines without TGM2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[RALY]] | B | TGM2 activity raises RALY's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 1.38× lower at baseline in the lines without TGM2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[EHD4]] | B | TGM2 activity raises EHD4's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 1.51× lower at baseline in the lines without TGM2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[PTPRE]] | B | TGM2 activity raises PTPRE's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 2.32× lower at baseline in the lines without TGM2 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[MMD]] | B | TGM2 activity raises MMD's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 1.59× lower at baseline in the lines without TGM2 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[NRP1]] | B | TGM2 activity raises NRP1's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 3.72× lower at baseline in the lines without TGM2 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[TNFRSF6B]] | B | TGM2 activity raises TNFRSF6B's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 3.00× lower at baseline in the lines without TGM2 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[ENDOD1]] | B | TGM2 activity raises ENDOD1's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 1.64× lower at baseline in the lines without TGM2 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[ECE1]] | B | TGM2 activity raises ECE1's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 1.92× lower at baseline in the lines without TGM2 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[EFHD2]] | B | TGM2 activity raises EFHD2's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 1.81× lower at baseline in the lines without TGM2 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[RGS17]] | B | TGM2 activity raises RGS17's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 2.21× lower at baseline in the lines without TGM2 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.3, 4.6); signed map (4.8, 50.7). **Vector** length 125, 38.7% of its response variance represented; |z| ≥ 3 in 1,431 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +6.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | -0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.6 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +5.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.3 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.3 | +2.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | -0.5 |
|  | [[Econazole (drug)]] 5 µM |  | +2.1 | +2.8 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -7.6 | -11.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.3 | -9.8 |
|  | [[NG25 (drug)]] 5 µM |  | -4.7 | -4.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.6 | -5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.2 | -9.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -3.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.1 | -5.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.8 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.8 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | transglutaminase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:38,127,385-38,166,578 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TGC, TG2 |
| Gene groups (HGNC) | Transglutaminases |
| Hallmark sets | IL2_STAT5_SIGNALING, HYPOXIA, EPITHELIAL_MESENCHYMAL_TRANSITION, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [P21980](https://www.uniprot.org/uniprotkb/P21980) (Protein-glutamine gamma-glutamyltransferase 2):

> Calcium-dependent acyltransferase that catalyzes the formation of covalent bonds between peptide-bound glutamine and various primary amines, such as gamma-amino group of peptide-bound lysine, or mono- and polyamines, thereby producing cross-linked or aminated proteins, respectively. Involved in many biological processes, such as bone development, angiogenesis, wound healing, cellular differentiation, chromatin modification and apoptosis. Acts as a protein-glutamine gamma-glutamyltransferase by …

**Summary**, from NCBI Gene [7052](https://www.ncbi.nlm.nih.gov/gene/7052):

> Transglutaminases are enzymes that catalyze the crosslinking of proteins by epsilon-gamma glutamyl lysine isopeptide bonds. While the primary structure of transglutaminases is not conserved, they all have the same amino acid sequence at their active sites and their activity is calcium-dependent. The protein encoded by this gene acts as a monomer, is induced by retinoic acid, and appears to be involved in apoptosis. Finally, the encoded protein is the autoantigen implicated in celiac disease. …

**Accessions** — [HGNC:11778](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11778) · Entrez [7052](https://www.ncbi.nlm.nih.gov/gene/7052) · UniProt [P21980](https://www.uniprot.org/uniprotkb/P21980) · Ensembl [ENSG00000198959](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198959)

## Data

Gene col 12756: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12756); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12756, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12756]; `tensor/DDL_lfc|DDL_z.npy` [12756]; `embed/gene_vectors.npy` [12756]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12756 or target_col == 12756). Every well: [[TGM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TGM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
