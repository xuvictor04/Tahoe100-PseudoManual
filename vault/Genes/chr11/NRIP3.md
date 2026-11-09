---
symbol: "NRIP3"
type: "gene"
col: 10600
ensembl_id: "ENSG00000175352"
name: "nuclear receptor interacting protein 3"
location: "11p15.4"
module: 81
arm: "+"
pooled_cpm: 21.93
n_lines_expressing: 35
n_dd_up: 44
n_dd_down: 29
n_dd_up_clean: 33
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# NRIP3

*nuclear receptor interacting protein 3* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.27× (z +23.8, q 0e+00, up in 31 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (2 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 0.678× (z -5.6, q 1e-05, down in 15 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKIA]] (+0.67, fdr 7e-06), [[KBTBD8]] (+0.64, fdr 1e-05), [[C3orf52]] (+0.64, fdr 1e-05); moves opposite to [[LUC7L2]] (-0.59, fdr 3e-05), [[ARMC8]] (-0.56, fdr 1e-05), [[PPP4R3A]] (-0.53, fdr 3e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[OR4F15]] → it (grade B ⚠); 3 go from it, the strongest it → [[CNGA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10600.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.27×** | +23.8 | 0e+00 | 31/32 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.64×** | +22.0 | 0e+00 | 31/32 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.77×** | +20.6 | 0e+00 | 31/32 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.72×** | +20.2 | 0e+00 | 25/31 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **4.01×** | +19.9 | 0e+00 | 31/32 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.64×** | +18.5 | 0e+00 | 31/32 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.15×** | +15.5 | 0e+00 | 28/33 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.91×** | +15.3 | 0e+00 | 30/31 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.90×** | +15.2 | 0e+00 | 30/31 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.71×** | +14.3 | 2e-44 | 31/32 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.85×** | +14.2 | 9e-44 | 29/30 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.88×** | +9.0 | 9e-18 | 25/31 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +8.3 | 5e-15 | 18/30 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.72×** | +7.8 | 4e-13 | 23/29 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **1.64×** | +7.1 | 6e-11 | 14/26 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.98×** | +7.0 | 1e-10 | 23/32 (SW480, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10600.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.678×** | -5.6 | 1e-05 | 15/32 (LOX-IMVI, H4, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.768×** | -5.2 | 6e-05 | 20/32 (A549, PANC-1, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.708×** | -4.9 | 1e-04 | 14/31 (A549, H4, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.713×** | -4.8 | 2e-04 | 15/30 (LOX-IMVI, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.725×** | -4.6 | 4e-04 | 19/31 (LOX-IMVI, NCI-H2347, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.728×** | -4.4 | 0.001 | 12/27 (HS-578T, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.743×** | -4.3 | 0.002 | 15/32 (NCI-H2347, HOP62, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.748×** | -4.2 | 0.002 | 11/32 (HOP62, H4, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.748×** | -4.2 | 0.002 | 16/31 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.739×** | -4.2 | 0.002 | 15/30 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.726×** | -4.0 | 0.003 | 14/32 (NCI-H460, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.760×** | -3.9 | 0.004 | 9/32 (H4, HOP62, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.748×** | -3.9 | 0.005 | 14/30 (A549, H4, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.802×** | -3.8 | 0.006 | 14/33 (SK-MEL-2, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.831×** | -3.8 | 0.006 | 14/32 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.770×** | -3.8 | 0.006 | 14/31 (A549, SW1417, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.760×** | -3.6 | 0.009 | 10/32 (NCI-H1573, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10600. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 66.5 | 14 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.58× (z +14.6) | — |
| [[SW480 (line)]] | alt | 13.9 | 12 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.03× (z +18.5) | — |
| [[HOP62 (line)]] | alt | 38.4 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +17.0) | — |
| [[NCI-H460 (line)]] | wt | 23.3 | 8 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.67× (z +12.6) | — |
| [[SW1417 (line)]] | alt | 6.34 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 23.1× (z +13.0) | — |
| [[BT-474 (line)]] | alt | 8.78 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.7× (z +15.7) | — |
| [[J82 (line)]] | alt | 19.1 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +15.8) | — |
| [[NCI-H1792 (line)]] | alt | 17.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +13.4) | — |
| [[NCI-H23 (line)]] | alt | 11.7 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +9.2) | [[XRK3F2 (drug)]] 0.5 µM 0.0775× (z -8.9) |
| [[A-172 (line)]] | wt | 37.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.22× (z +11.9) | — |
| [[A549 (line)]] | wt | 16.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.32× (z +12.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 20.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 61.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.61× (z +9.6) | — |
| [[A-427 (line)]] | wt | 13.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.20× (z +11.0) | — |
| [[H4 (line)]] | wt | 72.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.24× (z +10.5) | — |
| [[HS-578T (line)]] | alt | 48.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 41.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 27.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.66× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 14.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +11.9) | — |
| [[C32 (line)]] | wt | 30.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.48× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 7.80 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.38× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 7.65 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.71× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 50.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.37× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 5.99 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.76× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 23.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +12.4) | — |
| [[A498 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.53 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.42 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 120 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.75 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.47 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10600), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKIA]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[KBTBD8]] | +0.64 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[C3orf52]] | +0.64 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[GALNT12]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[PLAUR]] | +0.61 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[HBEGF]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[CALB2]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[RAB3B]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[KHDRBS3]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[BCL2A1]] | +0.59 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[PNP]] | +0.58 | +0.48 / +0.65 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LUC7L2]] | -0.59 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[ARMC8]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[PPP4R3A]] | -0.53 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[RAF1]] | -0.51 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[RPRD1B]] | -0.51 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[RNF115]] | -0.50 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[WTAP]] | -0.49 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[SCAF8]] | -0.49 | -0.37 / -0.47 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OR4F15]] | B | OR4F15 activity raises NRIP3's level | lines that do not express OR4F15 (32) vs lines expressing it (18) | 3.18× lower at baseline in the lines without OR4F15 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, PHACTR1, ITGA4 |
| [[NR3C1]] | B | NR3C1 activity lowers NRIP3's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[MAP2K1]] | B | MAP2K1 activity raises NRIP3's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ADAMTS16]] | B | ADAMTS16 activity raises NRIP3's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 2.27× lower at baseline in the lines without ADAMTS16 | 0.093 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5 |
| [[SDK2]] | C | SDK2 activity raises NRIP3's level | lines that do not express SDK2 (16) vs lines expressing it (34) | 4.30× lower at baseline in the lines without SDK2 | 0.019 | ⚠ within organs, on part of the lines; also absent: NRIP3, ZNF549, MGAT5B; maybe low, not absent; co-absent with the target |
| [[KIAA1671]] | C | KIAA1671 activity lowers NRIP3's level | lines that do not express KIAA1671 (3) vs lines expressing it (47) | 6.67× higher at baseline in the lines without KIAA1671 | 0.030 | ⚠ few lines (3 vs 47); across organs; also absent: SOX13, FZD5, PDCD6P1; maybe low, not absent |
| [[HSPA12A]] | C | HSPA12A activity lowers NRIP3's level | lines that do not express HSPA12A (4) vs lines expressing it (46) | 1.53× higher at baseline in the lines without HSPA12A | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR3659HG, ENSG00000287400; maybe low, not absent; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNGA1]] | B | NRIP3 activity lowers CNGA1's level | lines that do not express NRIP3 (15) vs lines expressing it (35) | 1.81× higher at baseline in the lines without NRIP3 | 0.022 | ⚠ within organs, on part of the lines; also absent: SDK2, DTX3, MCTP1 |
| [[NIPAL1]] | B | NRIP3 activity lowers NIPAL1's level | lines that do not express NRIP3 (15) vs lines expressing it (35) | 1.94× higher at baseline in the lines without NRIP3 | 0.052 | ⚠ within organs, on part of the lines; also absent: SDK2, DTX3, MCTP1 |
| [[OBSL1]] | B | NRIP3 activity raises OBSL1's level | lines that do not express NRIP3 (15) vs lines expressing it (35) | 1.74× lower at baseline in the lines without NRIP3 | 0.098 | ⚠ within organs, on part of the lines; also absent: SDK2, DTX3, MCTP1 |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.6, 0.6); signed map (3.5, 46.8). **Vector** length 106, 29.0% of its response variance represented; |z| ≥ 3 in 1,136 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.7 | +15.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.3 | +9.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.9 | +18.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.2 | +14.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.1 | +15.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +15.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.4 | +6.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +7.0 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -4.9 | -2.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.5 | -3.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.7 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.7 | -3.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.4 | -5.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.3 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor interacting protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:8,965,682-9,005,288 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C11orf14 |
| Gene groups (HGNC) | Peptidase family A28 |
| Matched by | ensembl_id |

UniProt [Q9NQ35](https://www.uniprot.org/uniprotkb/Q9NQ35) carries no function annotation.

**Summary**, from NCBI Gene [56675](https://www.ncbi.nlm.nih.gov/gene/56675):

> Predicted to enable aspartic-type endopeptidase activity. Predicted to be involved in proteolysis. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:1167](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1167) · Entrez [56675](https://www.ncbi.nlm.nih.gov/gene/56675) · UniProt [Q9NQ35](https://www.uniprot.org/uniprotkb/Q9NQ35) · Ensembl [ENSG00000175352](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175352)

## Data

Gene col 10600: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10600); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10600, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10600]; `tensor/DDL_lfc|DDL_z.npy` [10600]; `embed/gene_vectors.npy` [10600]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10600 or target_col == 10600). Every well: [[NRIP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRIP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
