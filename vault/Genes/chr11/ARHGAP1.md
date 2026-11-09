---
symbol: "ARHGAP1"
type: "gene"
col: 10584
ensembl_id: "ENSG00000175220"
name: "Rho GTPase activating protein 1"
location: "11p11.2"
module: 222
arm: "+"
pooled_cpm: 39.43
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 31
n_dd_up_clean: 2
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/222"]
generated_by: "tahoemap"
---

# ARHGAP1

*Rho GTPase activating protein 1* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.37× (z +7.2, q 3e-10, up in 30 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H2030 2.50×, SW480 1.97×, NCI-H460 2.38×).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.502× (z -11.1, q 6e-26, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMUT]] (+0.69, fdr 7e-06), [[RARS2]] (+0.63, fdr 1e-05), [[KLHL28]] (+0.63, fdr 1e-05); moves opposite to [[DTNB]] (-0.57, fdr 1e-05), [[ATF7IP]] (-0.56, fdr 1e-05), [[PSMA4]] (-0.55, fdr 1e-05).
> It is in [[Module 222]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[SWI5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10584.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H2030 2.50×, SW480 1.97×, NCI-H460 2.38×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.2 | 3e-10 | 30/47 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.050 | 15/47 (NCI-H1792, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.25×** | +3.6 | 0.050 | 20/45 (A498, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.23× | +3.2 | 0.20 | 19/48 (NCI-H2030, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10584.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.502×** | -11.1 | 6e-26 | 37/48 (HOP62, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.615×** | -11.0 | 6e-26 | 31/47 (AsPC-1, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.563×** | -9.3 | 4e-18 | 34/48 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.595×** | -8.4 | 9e-15 | 38/48 (HS-578T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.598×** | -8.3 | 1e-14 | 36/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.608×** | -8.0 | 1e-13 | 36/48 (A-172, HS-578T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.626×** | -7.3 | 3e-11 | 31/46 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.737×** | -6.9 | 3e-10 | 31/48 (RPMI-7951, NCI-H2347, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.659×** | -6.7 | 1e-09 | 31/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.662×** | -6.4 | 1e-08 | 33/47 (AsPC-1, PANC-1, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.681×** | -6.2 | 3e-08 | 32/48 (AsPC-1, HOP62, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.681×** | -5.8 | 2e-07 | 26/48 (H4, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.699×** | -5.8 | 4e-07 | 26/48 (C32, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.571×** | -4.7 | 1e-04 | 25/43 (HepG2/C3A, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.764×** | -4.3 | 6e-04 | 22/48 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.758×** | -4.3 | 6e-04 | 21/47 (AsPC-1, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.822×** | -4.0 | 0.002 | 17/48 (AsPC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.824×** | -4.0 | 0.002 | 17/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.766×** | -4.0 | 0.002 | 17/48 (A-427, PANC-1, …) | all doses, flat |  |
| [[Gefitinib (drug)]] 5 µM |  | **0.795×** | -3.7 | 0.007 | 14/48 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.665×** | -3.4 | 0.014 | 19/47 (AsPC-1, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.809×** | -3.4 | 0.015 | 18/48 (Hs 766T, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10584. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 46.1 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.196× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -12.6) |
| [[SW480 (line)]] | alt | 39.4 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.6) | [[Digitoxin (drug)]] 0.5 µM 0.363× (z -10.1) |
| [[A-172 (line)]] | wt | 67.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -14.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.426× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 68.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -19.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.348× (z -10.2) |
| [[HS-578T (line)]] | alt | 61.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -16.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.377× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 53.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.162× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.289× (z -9.2) |
| [[A498 (line)]] | wt | 115 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -10.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 40.3 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.341× (z -9.1) |
| [[COLO 205 (line)]] | alt | 31.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.186× (z -9.6) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 25.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -12.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 45.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.322× (z -10.3) |
| [[A549 (line)]] | wt | 41.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[H4 (line)]] | wt | 45.3 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.143× (z -10.5) |
| [[Hs 766T (line)]] | wt | 52.1 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.303× (z -9.5) |
| [[J82 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.277× (z -9.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 30.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.197× (z -10.6) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 13.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 36.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -11.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.128× (z -10.0) ⚠ transcription drop; cell-cycle shift, explains ~63% of this change |
| [[A-427 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10584), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMUT]] | +0.69 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[RARS2]] | +0.63 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[KLHL28]] | +0.63 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[DPY19L3]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[USP20]] | +0.62 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[ZBTB49]] | +0.62 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[CRLS1]] | +0.61 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[TBCCD1]] | +0.60 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[CWF19L1]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[MTMR14]] | +0.59 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[DIS3]] | +0.59 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[ARPC3]] | +0.58 | +0.61 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTNB]] | -0.57 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[ATF7IP]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[PSMA4]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[STAU2]] | -0.54 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[NUTM2B-AS1]] | -0.53 | -0.61 / -0.40 | both halves | 4e-05 |  |
| [[PLEKHA5]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[DST]] | -0.52 | -0.61 / -0.46 | both halves | 2e-05 | pathway: RND2 GTPase cycle |
| [[TBL1X]] | -0.52 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[TENM3]] | -0.52 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[GKAP1]] | -0.52 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[TTC28]] | -0.51 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[MID1]] | -0.51 | -0.49 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SWI5]] | C | ARHGAP1's natural level strengthens SWI5's drug response | ARHGAP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.17; direction not clear | 0.039 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 222]]; 10 genes; every member is in the + arm (projection on the module's main direction -0.722). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.8, -31.7); signed map (-47.0, 4.9). **Vector** length 120, 33.0% of its response variance represented; |z| ≥ 3 in 1,006 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +7.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +3.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.5 | +2.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | +2.2 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -6.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.4 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.0 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.0 | -8.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.5 | -8.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.9 | -2.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -3.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:46,677,080-46,700,619 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RhoGAP, p50rhoGAP, CDC42GAP, Cdc42GAP |
| Gene groups (HGNC) | Rho GTPase activating proteins; BCH domain containing ; CRAL-TRIO lipid binding domain containing |
| Reactome | 16 pathways, smallest: RND2 GTPase cycle; RHOF GTPase cycle; RHOD GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07960](https://www.uniprot.org/uniprotkb/Q07960) (Rho GTPase-activating protein 1):

> GTPase activator for the Rho, Rac and Cdc42 proteins, converting them to the putatively inactive GDP-bound state. Cdc42 seems to be the preferred substrate.

**Summary**, from NCBI Gene [392](https://www.ncbi.nlm.nih.gov/gene/392):

> This gene encodes a member of a large family of proteins that activate Rho-type guanosine triphosphate (GTP) metabolizing enzymes. The encoded protein contains a SRC homology 3 domain and interacts with Bcl-2-associated protein family members. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:673](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:673) · Entrez [392](https://www.ncbi.nlm.nih.gov/gene/392) · UniProt [Q07960](https://www.uniprot.org/uniprotkb/Q07960) · Ensembl [ENSG00000175220](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175220)

## Data

Gene col 10584: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10584); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10584, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10584]; `tensor/DDL_lfc|DDL_z.npy` [10584]; `embed/gene_vectors.npy` [10584]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10584 or target_col == 10584). Every well: [[ARHGAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
