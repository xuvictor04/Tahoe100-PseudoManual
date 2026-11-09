---
symbol: "ACSS1"
type: "gene"
col: 7856
ensembl_id: "ENSG00000154930"
name: "acyl-CoA synthetase short chain family member 1"
location: "20p11.21"
module: 190
arm: "+"
pooled_cpm: 7.59
n_lines_expressing: 42
n_dd_up: 22
n_dd_down: 15
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/190"]
generated_by: "tahoemap"
---

# ACSS1

*acyl-CoA synthetase short chain family member 1* — 20p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.61× (z +10.4, q 2e-22, up in 19 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.629× (z -10.1, q 2e-21, down in 21 of 34 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.412× (z -7.2, q 1e-10, down in 19 of 38 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC43A1]] (+0.59, fdr 1e-05), [[TPD52L1]] (+0.51, fdr 3e-05), [[EEF2K]] (+0.50, fdr 3e-05); moves opposite to [[DNAAF11]] (-0.47, fdr 5e-04), [[GUSBP1-1]] (-0.47, fdr 3e-04), [[SCAPER]] (-0.45, fdr 1e-04).
> It is in [[Module 190]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SORL1]] → it (grade B ⚠); 2 go from it, the strongest it → [[CCND2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7856.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +10.4 | 2e-22 | 19/38 (LS 180, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.55×** | +9.6 | 3e-19 | 15/38 (KATO III, SW 900, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +8.3 | 2e-14 | 5/15 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +8.1 | 9e-14 | 11/27 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +7.2 | 9e-11 | 19/38 (PANC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +7.0 | 3e-10 | 17/36 (NCI-H460, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.31×** | +5.9 | 2e-07 | 12/38 (BT-474, NCI-H1792, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +5.3 | 8e-06 | 11/37 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +4.3 | 9e-04 | 7/38 (LS 180, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 9e-04 | 11/36 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.34×** | +4.2 | 0.001 | 5/37 (LoVo, SW1417, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +4.2 | 0.001 | 7/19 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.002 | 3/39 (PANC-1, C32, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.002 | 9/34 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.8 | 0.006 | 5/38 (COLO 205, CFPAC-1, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.007 | 3/32 (SW480, SW48, …) | all doses, flat | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Regorafenib (drug)]] 5 µM |  | **1.56×** | +3.6 | 0.012 | 0/35 | rises with dose | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.17× | +3.4 | 0.018 | 4/38 (SNU-423, PANC-1, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.018 | 6/38 (PANC-1, A549, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7856.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.629×** | -10.1 | 2e-21 | 21/34 (LoVo, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.560×** | -9.0 | 8e-17 | 19/39 (HT-29, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.558×** | -8.7 | 8e-16 | 22/37 (hTERT-HPNE, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.412×** | -7.2 | 1e-10 | 19/38 (A549, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.639×** | -6.9 | 5e-10 | 17/34 (HOP62, HT-29, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.658×** | -6.5 | 1e-08 | 16/32 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.705×** | -5.4 | 5e-06 | 12/36 (AsPC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.741×** | -4.6 | 3e-04 | 14/37 (PANC-1, HT-29, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.756×** | -4.3 | 1e-03 | 11/37 (SHP-77, HT-29, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.761×** | -4.2 | 0.001 | 16/38 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.593×** | -4.2 | 0.001 | 5/36 (HT-29, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.775×** | -3.9 | 0.004 | 16/37 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.798×** | -3.5 | 0.020 | 10/38 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.856× | -3.4 | 0.026 | 8/38 (Hs 766T, SNU-423, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.676×** | -3.2 | 0.059 | 6/32 (SW 900, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.871× | -3.0 | 0.083 | 6/38 (SHP-77, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7856. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 26.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -12.9) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A549 (line)]] | wt | 13.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -14.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[Hs 766T (line)]] | wt | 12.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -9.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 8.59 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0673× (z -9.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Monocrotaline (drug)]] 5 µM 0.0811× (z -8.6) |
| [[KATO III (line)]] | alt | 33.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -12.1) ⚠ cell-cycle shift, explains ~44% of this change |
| [[LoVo (line)]] | wt | 21.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0865× (z -25.4) ⚠ cell-cycle shift, explains ~44% of this change |
| [[PANC-1 (line)]] | alt | 9.72 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 6.53 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0572× (z -12.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HOP62 (line)]] | alt | 3.85 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0669× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[MIA PaCa-2 (line)]] | alt | 2.98 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0694× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 5.08 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0828× (z -9.1) |
| [[SNU-423 (line)]] | alt | 4.68 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0733× (z -9.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.751 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.688 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7856), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC43A1]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[TPD52L1]] | +0.51 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[EEF2K]] | +0.50 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[PIK3C2B]] | +0.50 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[SLC22A5]] | +0.48 | +0.55 / +0.40 | both halves | 5e-05 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[CD276]] | +0.48 | +0.38 / +0.45 | both halves | 6e-05 |  |
| [[PPARGC1B]] | +0.48 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[ATP7B]] | +0.47 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[SEMA4G]] | +0.47 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[ARHGEF16]] | +0.46 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[EPB41L4B]] | +0.46 | +0.37 / +0.48 | both halves | 7e-05 |  |
| [[THRA]] | +0.46 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF11]] | -0.47 | -0.53 / -0.23 | both halves | 5e-04 |  |
| [[GUSBP1-1]] | -0.47 | -0.52 / -0.27 | both halves | 3e-04 |  |
| [[SCAPER]] | -0.45 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[OSMR]] | -0.44 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[GMDS-DT]] | -0.44 | -0.44 / -0.37 | both halves | 9e-05 |  |
| [[NRIP1]] | -0.43 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[UBAP1]] | -0.42 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[MAP3K20]] | -0.42 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[GPATCH8]] | -0.41 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[TAOK1]] | -0.41 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[SRSF4]] | -0.41 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[IQCH]] | -0.40 | -0.39 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SORL1]] | B | SORL1 activity raises ACSS1's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 1.73× lower at baseline in the lines without SORL1 | 0.050 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCND2]] | B | ACSS1 activity lowers CCND2's level | lines that do not express ACSS1 (8) vs lines expressing it (42) | 2.40× higher at baseline in the lines without ACSS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PRXL2A, STAT5A, MGST2; maybe low, not absent; its own permutation p |
| [[THRA]] | B | ACSS1 activity raises THRA's level | lines that do not express ACSS1 (8) vs lines expressing it (42) | 1.40× lower at baseline in the lines without ACSS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: PRXL2A, STAT5A, MGST2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 190]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.423). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.1, 13.1); signed map (0.6, 13.2). **Vector** length 60.3, 9.55% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +10.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +7.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.6 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +7.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +3.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +5.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.6 | -4.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.2 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -6.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -3.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Thymol (drug)]] 5 µM |  | -1.3 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA synthetase short chain family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.21 — chr20:25,006,230-25,058,980 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ568C11.3, AceCS2L, MGC33843; previously ACAS2L |
| Gene groups (HGNC) | Acyl-CoA synthetase family |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 3 pathways, smallest: Ethanol oxidation; Phase I - Functionalization of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUB1](https://www.uniprot.org/uniprotkb/Q9NUB1) (Acetyl-coenzyme A synthetase 2-like, mitochondrial):

> Catalyzes the synthesis of acetyl-CoA from short-chain fatty acids. Acetate is the preferred substrate. Can also utilize propionate with a much lower affinity (By similarity). Provides acetyl-CoA that is utilized mainly for oxidation under ketogenic conditions (By similarity). Involved in thermogenesis under ketogenic conditions, using acetate as a vital fuel when carbohydrate availability is insufficient (By similarity).

**Summary**, from NCBI Gene [84532](https://www.ncbi.nlm.nih.gov/gene/84532):

> This gene encodes a mitochondrial acetyl-CoA synthetase enzyme. A similar protein in mice plays an important role in the tricarboxylic acid cycle by catalyzing the conversion of acetate to acetyl CoA. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:16091](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16091) · Entrez [84532](https://www.ncbi.nlm.nih.gov/gene/84532) · UniProt [Q9NUB1](https://www.uniprot.org/uniprotkb/Q9NUB1) · Ensembl [ENSG00000154930](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154930)

## Data

Gene col 7856: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7856); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7856, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7856]; `tensor/DDL_lfc|DDL_z.npy` [7856]; `embed/gene_vectors.npy` [7856]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7856 or target_col == 7856). Every well: [[ACSS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACSS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
