---
symbol: "RGS2"
type: "gene"
col: 3831
ensembl_id: "ENSG00000116741"
name: "regulator of G protein signaling 2"
location: "1q31.2"
module: 235
arm: "+"
pooled_cpm: 42.21
n_lines_expressing: 33
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 9
tags: ["gene", "module/235"]
generated_by: "tahoemap"
---

# RGS2

*regulator of G protein signaling 2* — 1q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.18× (z +10.9, q 5e-25, up in 25 of 31 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.04× (z +9.5, q 3e-19, up in 26 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.574× (z -4.8, q 9e-04, down in 21 of 32 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Trametinib (drug)]] 0.05 µM: 0.699× (z -4.7, q 9e-04, down in 16 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP6]] (+0.61, fdr 1e-05), [[KCNMB4]] (+0.59, fdr 1e-05), [[EFNB2]] (+0.58, fdr 1e-05); moves opposite to [[RUFY3]] (-0.46, fdr 6e-05), [[TBC1D22B]] (-0.46, fdr 1e-04), [[ANXA4]] (-0.46, fdr 8e-05).
> It is in [[Module 235]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[DPP10]] → it (grade B ⚠); 9 go from it, the strongest it → [[ST3GAL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3831.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **3.18×** | +10.9 | 5e-25 | 25/31 (A498, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.92×** | +10.1 | 1e-21 | 27/31 (NCI-H2030, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.04×** | +9.5 | 3e-19 | 26/31 (NCI-H2347, C32, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +9.1 | 8e-18 | 11/31 (HOP62, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.86×** | +8.3 | 2e-14 | 16/31 (A498, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.35×** | +8.1 | 8e-14 | 18/30 (HT-29, SK-MEL-2, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.19×** | +7.4 | 9e-12 | 24/30 (NCI-H2030, A498, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.16×** | +7.3 | 2e-11 | 21/30 (A498, NCI-H2347, …) | two highest doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +6.9 | 3e-10 | 14/28 (NCI-H2347, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.03×** | +6.7 | 1e-09 | 17/30 (NCI-H2347, A498, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.95×** | +6.0 | 8e-08 | 18/31 (CFPAC-1, SK-MEL-2, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.84×** | +5.7 | 4e-07 | 18/30 (NCI-H2030, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +5.2 | 8e-06 | 19/31 (C32, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.68×** | +4.6 | 1e-04 | 10/30 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.65×** | +4.6 | 2e-04 | 15/25 (RKO, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.70×** | +3.6 | 0.011 | 8/32 (NCI-H2347, RKO, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **1.42×** | +3.3 | 0.026 | 12/30 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3831.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.574×** | -4.8 | 9e-04 | 21/32 (NCI-H460, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.699×** | -4.7 | 9e-04 | 16/31 (LoVo, NCI-H460, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.633×** | -4.3 | 0.003 | 16/30 (LoVo, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.626×** | -4.1 | 0.006 | 14/30 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.678×** | -3.5 | 0.043 | 13/30 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.669×** | -3.5 | 0.043 | 12/29 (H4, Hs 766T, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.701×** | -3.2 | 0.090 | 13/29 (NCI-H460, SW 900, …) | all doses, flat |  |
| [[Erlotinib (drug)]] 5 µM |  | **0.701×** | -3.2 | 0.090 | 10/30 (A498, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.779× | -3.1 | 0.10 | 12/31 (NCI-H460, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.517× | -3.1 | 0.10 | 12/33 (NCI-H460, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3831. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 411 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0730× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -15.2) |
| [[LoVo (line)]] | wt | 37.7 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Cobimetinib (drug)]] 0.5 µM 0.163× (z -10.2) |
| [[C32 (line)]] | wt | 115 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +9.5) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.86× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 10.8 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +11.2) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[NCI-H2030 (line)]] | alt | 42.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 6.71× (z +10.5) ⚠ cell-cycle shift, explains ~33% of this change | [[Adagrasib (drug)]] 0.05 µM 0.490× (z -13.9) ⚠ position not correctable |
| [[NCI-H2347 (line)]] | alt | 18.4 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.20× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 52.7 | 1 (1 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.99× (z +8.5) ⚠ toxic; cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.156× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 121 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.194× (z -10.0) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 0.5 µM 0.243× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 66.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.48× (z +9.3) ⚠ cell-cycle shift, explains ~39% of this change | [[Dinaciclib (drug)]] 5 µM 0.0487× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0696× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 46.0 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0578× (z -11.2) |
| [[HOP62 (line)]] | alt | 12.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 46.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0699× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 23.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +9.5) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 40.1 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.181× (z -8.5) |
| [[A-172 (line)]] | wt | 8.03 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.82 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.34 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.67 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.93 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.51 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.92 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.36 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.83 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.43 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.45 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.71 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.31 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.43 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3831), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP6]] | +0.61 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[KCNMB4]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[EFNB2]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[DOCK4]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[TLE6]] | +0.57 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[RTN1]] | +0.56 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SERPIND1]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[GLRX]] | +0.54 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[ISM2]] | +0.54 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[RIMKLA]] | +0.52 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[GTF2IP7]] | +0.52 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[SLC2A3]] | +0.52 | +0.39 / +0.49 | both halves | 6e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RUFY3]] | -0.46 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[TBC1D22B]] | -0.46 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[ANXA4]] | -0.46 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[SLC35B3]] | -0.45 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[GALNT7]] | -0.44 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[MSTO1]] | -0.44 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[TM9SF5P]] | -0.44 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[SARM1]] | -0.43 | -0.36 / -0.30 | both halves | 2e-04 |  |
| [[C8orf44-SGK3]] | -0.43 | -0.26 / -0.42 | both halves | 4e-04 |  |
| [[CDKN2B-AS1]] | -0.43 | -0.36 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPP10]] | B | DPP10 activity raises RGS2's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 2.41× lower at baseline in the lines without DPP10 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent |
| [[GLRX]] | B | GLRX activity raises RGS2's level | lines that do not express GLRX (10) vs lines expressing it (40) | 2.50× lower at baseline in the lines without GLRX | 0.031 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[PLAC4]] | B | PLAC4 activity raises RGS2's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 1.91× lower at baseline in the lines without PLAC4 | 0.059 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[AADACP1]] | B | AADACP1 activity raises RGS2's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 2.01× lower at baseline in the lines without AADACP1 | 0.082 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1 |
| [[SERPINB11]] | B | SERPINB11 activity raises RGS2's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 2.98× lower at baseline in the lines without SERPINB11 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX |
| [[MAP2K1]] | B | MAP2K1 activity raises RGS2's level | compounds that target MAP2K1: 2 of 4 lower it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST3GAL1]] | B | RGS2 activity raises ST3GAL1's level | lines that do not express RGS2 (17) vs lines expressing it (33) | 2.73× lower at baseline in the lines without RGS2 | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC01393, P2RY1, MEF2C-AS1; maybe low, not absent |
| [[MARCHF3]] | B | RGS2 activity raises MARCHF3's level | lines that do not express RGS2 (17) vs lines expressing it (33) | 1.63× lower at baseline in the lines without RGS2 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC01393, P2RY1, MEF2C-AS1; maybe low, not absent |
| [[PAG1]] | B | RGS2 activity raises PAG1's level | lines that do not express RGS2 (17) vs lines expressing it (33) | 2.91× lower at baseline in the lines without RGS2 | 0.049 | ⚠ within organs, on part of the lines; also absent: LINC01393, P2RY1, MEF2C-AS1; maybe low, not absent |
| [[MSTO1]] | B | RGS2 activity lowers MSTO1's level | lines that do not express RGS2 (17) vs lines expressing it (33) | 1.05× higher at baseline in the lines without RGS2 | 0.064 | ⚠ within organs, on part of the lines; also absent: LINC01393, P2RY1, MEF2C-AS1; maybe low, not absent |
| [[MFSD2A]] | B | RGS2 activity raises MFSD2A's level | lines that do not express RGS2 (17) vs lines expressing it (33) | 1.12× lower at baseline in the lines without RGS2 | 0.069 | ⚠ within organs, on part of the lines; also absent: LINC01393, P2RY1, MEF2C-AS1; maybe low, not absent |
| [[GLRX]] | B | RGS2 activity raises GLRX's level | lines that do not express RGS2 (17) vs lines expressing it (33) | 2.03× lower at baseline in the lines without RGS2 | 0.071 | ⚠ within organs, on part of the lines; also absent: LINC01393, P2RY1, MEF2C-AS1; maybe low, not absent |
| [[ATP2B1]] | B | RGS2 activity raises ATP2B1's level | lines that do not express RGS2 (17) vs lines expressing it (33) | 1.96× lower at baseline in the lines without RGS2 | 0.078 | ⚠ within organs, on part of the lines; also absent: LINC01393, P2RY1, MEF2C-AS1; maybe low, not absent |
| [[MLKL]] | B | RGS2 activity raises MLKL's level | lines that do not express RGS2 (17) vs lines expressing it (33) | 1.97× lower at baseline in the lines without RGS2 | 0.087 | ⚠ within organs, on part of the lines; also absent: LINC01393, P2RY1, MEF2C-AS1; maybe low, not absent |
| [[PTPRM]] | C | RGS2 activity raises PTPRM's level | lines that do not express RGS2 (17) vs lines expressing it (33) | 3.48× lower at baseline in the lines without RGS2 | 0.078 | ⚠ within organs, on part of the lines; also absent: LINC01393, P2RY1, MEF2C-AS1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 235]]; 5 genes; every member is in the + arm (projection on the module's main direction 0.565). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.1, 7.8); signed map (2.0, 53.3). **Vector** length 95.1, 25.0% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +8.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +2.4 | +4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.4 | +10.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +7.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +1.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.7 | +1.8 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.1 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.1 | -4.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.9 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | regulator of G protein signaling 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q31.2 — chr1:192,809,039-192,812,275 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously G0S8 |
| Gene groups (HGNC) | Receptor ligands; Regulators of G-protein signaling |
| Reactome | 3 pathways, smallest: G alpha (q) signalling events; GPCR downstream signalling; Signaling by GPCR |
| Matched by | ensembl_id |

**Function**, from UniProt [P41220](https://www.uniprot.org/uniprotkb/P41220) (Regulator of G protein signaling 2):

> Regulates G protein-coupled receptor signaling cascades. Inhibits signal transduction by increasing the GTPase activity of G protein alpha subunits, thereby driving them into their inactive GDP-bound form. It is involved in the negative regulation of the angiotensin-activated signaling pathway. Plays a role in the regulation of blood pressure in response to signaling via G protein-coupled receptors and GNAQ. Plays a role in regulating the constriction and relaxation of vascular smooth muscle …

**Summary**, from NCBI Gene [5997](https://www.ncbi.nlm.nih.gov/gene/5997):

> Regulator of G protein signaling (RGS) family members are regulatory molecules that act as GTPase activating proteins (GAPs) for G alpha subunits of heterotrimeric G proteins. RGS proteins are able to deactivate G protein subunits of the Gi alpha, Go alpha and Gq alpha subtypes. They drive G proteins into their inactive GDP-bound forms. Regulator of G protein signaling 2 belongs to this family. The protein acts as a mediator of myeloid differentiation and may play a role in leukemogenesis. …

**Accessions** — [HGNC:9998](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9998) · Entrez [5997](https://www.ncbi.nlm.nih.gov/gene/5997) · UniProt [P41220](https://www.uniprot.org/uniprotkb/P41220) · Ensembl [ENSG00000116741](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116741)

## Data

Gene col 3831: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3831); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3831, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3831]; `tensor/DDL_lfc|DDL_z.npy` [3831]; `embed/gene_vectors.npy` [3831]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3831 or target_col == 3831). Every well: [[RGS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
