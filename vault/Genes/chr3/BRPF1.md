---
symbol: "BRPF1"
type: "gene"
col: 8033
ensembl_id: "ENSG00000156983"
name: "bromodomain and PHD finger containing 1"
location: "3p25.3"
module: 119
arm: "+"
pooled_cpm: 20.42
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 6
n_dd_up_clean: 19
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# BRPF1

*bromodomain and PHD finger containing 1* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +11.5, q 8e-28, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.590× (z -8.9, q 5e-16, down in 29 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.756× (z -6.6, q 6e-09, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM11]] (+0.72, fdr 1e-05), [[MTF1]] (+0.67, fdr 1e-05), [[ZNF324]] (+0.65, fdr 1e-05); moves opposite to [[GLS]] (-0.57, fdr 1e-05), [[ABLIM1]] (-0.55, fdr 1e-04), [[EFR3A]] (-0.53, fdr 1e-04).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8033.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +11.5 | 8e-28 | 38/47 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.42×** | +10.7 | 2e-24 | 42/48 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.46×** | +8.9 | 9e-17 | 32/47 (NCI-H1792, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.67×** | +8.6 | 1e-15 | 33/48 (LOX-IMVI, SW480, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +7.1 | 2e-10 | 27/43 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.21×** | +6.9 | 5e-10 | 27/46 (SW480, A-427, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +6.6 | 2e-09 | 30/46 (A-172, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.45×** | +6.2 | 5e-08 | 26/48 (SW480, HEC-1-A, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.43×** | +6.0 | 2e-07 | 24/47 (LS 180, SW480, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +5.5 | 2e-06 | 23/47 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +5.3 | 5e-06 | 23/47 (A498, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +4.9 | 5e-05 | 22/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +4.5 | 3e-04 | 18/45 (A-427, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.30×** | +4.3 | 6e-04 | 16/48 (SW480, AsPC-1, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.29×** | +4.2 | 8e-04 | 21/45 (J82, A498, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.001 | 12/47 (NCI-H460, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +3.9 | 0.003 | 18/48 (MIA PaCa-2, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.022 | 8/44 (MIA PaCa-2, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.022 | 5/47 (SW1417, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.041 | 8/46 (LOX-IMVI, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.049 | 4/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.049 | 9/45 (LoVo, RKO, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.052 | 16/48 (MIA PaCa-2, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8033.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.590×** | -8.9 | 5e-16 | 29/41 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.640×** | -7.2 | 2e-10 | 23/33 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.756×** | -6.6 | 6e-09 | 31/48 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.729×** | -4.9 | 1e-04 | 18/37 (SHP-77, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.704×** | -4.8 | 2e-04 | 15/48 (SW48, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.800×** | -3.6 | 0.029 | 16/47 (SW480, BT-474, …) | rises with dose |  |
| [[Pyridoxine (drug)]] 5 µM |  | 0.882× | -3.0 | 0.21 | 6/48 (MIA PaCa-2, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8033. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 24.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0350× (z -27.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 10.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -10.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 14.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -11.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 20.5 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.95× (z +9.2) | — |
| [[A-427 (line)]] | wt | 24.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -13.8) |
| [[A498 (line)]] | wt | 24.6 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.197× (z -9.9) ⚠ toxic |
| [[A549 (line)]] | wt | 19.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +12.3) | — |
| [[C-33 A (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -9.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -11.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -13.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 18.5 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0929× (z -11.3) ⚠ toxic |
| [[KATO III (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -9.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -11.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -10.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -10.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8033), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM11]] | +0.72 | +0.52 / +0.76 | both halves | 1e-05 |  |
| [[MTF1]] | +0.67 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[ZNF324]] | +0.65 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[TPRN]] | +0.64 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[TRIM11]] | +0.64 | +0.42 / +0.71 | both halves | 4e-05 |  |
| [[NCBP2AS2]] | +0.63 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[CHERP]] | +0.63 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[YRDC]] | +0.63 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[FBXL18]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[ENKD1]] | +0.62 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[PHRF1]] | +0.62 | +0.37 / +0.63 | both halves | 7e-05 | same gene group |
| [[TBC1D10B]] | +0.61 | +0.52 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLS]] | -0.57 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[ABLIM1]] | -0.55 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[EFR3A]] | -0.53 | -0.36 / -0.61 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.726). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-31.8, -11.0); signed map (-11.5, -9.4). **Vector** length 84.0, 17.3% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +11.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | +4.1 | +4.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.9 | +6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +7.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.5 | +10.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +6.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.0 | +3.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.5 | +2.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.5 | +3.1 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.7 | -8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.5 | -4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.4 | -4.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.7 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -3.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | bromodomain and PHD finger containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:9,731,729-9,748,019 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BR140 |
| Gene groups (HGNC) | PHD finger proteins; PWWP domain containing; Bromodomain containing |
| Reactome | 6 pathways, smallest: Regulation of TP53 Activity through Acetylation; HATs acetylate histones; Regulation of TP53 Activity |
| Matched by | ensembl_id |

**Function**, from UniProt [P55201](https://www.uniprot.org/uniprotkb/P55201) (Peregrin):

> Scaffold subunit of various histone acetyltransferase (HAT) complexes, such as the MOZ/MORF and HBO1 complexes, which have a histone H3 acetyltransferase activity. Plays a key role in HBO1 complex by directing KAT7/HBO1 specificity towards histone H3 'Lys-14' acetylation (H3K14ac). Some HAT complexes preferentially mediate histone H3 'Lys-23' (H3K23ac) acetylation. Positively regulates the transcription of RUNX1 and RUNX2.

**Summary**, from NCBI Gene [7862](https://www.ncbi.nlm.nih.gov/gene/7862):

> This gene encodes a bromodomain, PHD finger and chromo/Tudor-related Pro-Trp-Trp-Pro (PWWP) domain containing protein. The encoded protein is a component of the MOZ/MORF histone acetyltransferase complexes which function as a transcriptional regulators. This protein binds to the catalytic MYST domains of the MOZ and MORF proteins and may play a role in stimulating acetyltransferase and transcriptional activity of the complex. Alternative splicing results in multiple transcript variants. …

**Accessions** — [HGNC:14255](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14255) · Entrez [7862](https://www.ncbi.nlm.nih.gov/gene/7862) · UniProt [P55201](https://www.uniprot.org/uniprotkb/P55201) · Ensembl [ENSG00000156983](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156983)

## Data

Gene col 8033: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8033); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8033, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8033]; `tensor/DDL_lfc|DDL_z.npy` [8033]; `embed/gene_vectors.npy` [8033]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8033 or target_col == 8033). Every well: [[BRPF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRPF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
