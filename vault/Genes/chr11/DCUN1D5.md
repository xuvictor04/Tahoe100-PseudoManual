---
symbol: "DCUN1D5"
type: "gene"
col: 6048
ensembl_id: "ENSG00000137692"
name: "defective in cullin neddylation 1 domain containing 5"
location: "11q22.3"
module: 54
arm: "+"
pooled_cpm: 59.45
n_lines_expressing: 50
n_dd_up: 44
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# DCUN1D5

*defective in cullin neddylation 1 domain containing 5* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (21 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.73× (z +8.8, q 6e-16, up in 41 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.42× (z +8.3, q 2e-14, up in 31 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.237×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.325×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNU13]] (+0.64, fdr 1e-05), [[PARGP1]] (+0.63, fdr 7e-06), [[RABEPK]] (+0.62, fdr 1e-05); moves opposite to [[SFR1]] (-0.60, fdr 1e-05), [[VEZF1]] (-0.57, fdr 3e-05), [[CHRAC1]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 22 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6048.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +8.8 | 6e-16 | 41/47 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.67×** | +8.6 | 2e-15 | 39/47 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +8.3 | 2e-14 | 31/48 (CFPAC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.60×** | +7.9 | 5e-13 | 37/48 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +7.5 | 8e-12 | 41/48 (SW480, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.51×** | +6.9 | 5e-10 | 37/48 (KATO III, C-33 A, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +6.8 | 7e-10 | 38/48 (HT-29, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.48×** | +6.5 | 5e-09 | 38/48 (SNU-423, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.10×** | +6.5 | 5e-09 | 34/49 (KATO III, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.09×** | +6.4 | 7e-09 | 34/48 (RKO, KATO III, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +6.3 | 2e-08 | 36/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.45×** | +6.1 | 4e-08 | 32/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +6.0 | 1e-07 | 33/47 (NCI-H1573, HT-29, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +5.9 | 2e-07 | 31/48 (Hs 766T, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.40×** | +5.5 | 1e-06 | 33/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +4.7 | 9e-05 | 27/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +4.4 | 3e-04 | 24/49 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.45×** | +4.4 | 3e-04 | 26/48 (A549, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +4.0 | 0.002 | 23/48 (RPMI-7951, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.002 | 25/48 (J82, NCI-H2347, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.56×** | +3.9 | 0.002 | 24/48 (NCI-H460, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.015 | 16/48 (NCI-H1792, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.019 | 15/48 (SW 900, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6048.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.237×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.325×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 5 µM |  | 0.666× | -3.6 | 0.19 | 16/50 (LoVo, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6048. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 88.6 | 5 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.67× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.06× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 63.8 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.58× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H460 (line)]] | wt | 56.0 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.32× (z +9.3) ⚠ toxic | — |
| [[C-33 A (line)]] | alt | 77.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 43.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 38.2 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +8.6) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 91.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.5) ⚠ cell-cycle shift, explains ~82% of this change | — |
| [[NCI-H2347 (line)]] | alt | 49.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 49.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +9.7) | — |
| [[RKO (line)]] | wt | 110 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +8.6) ⚠ cell-cycle shift, explains ~82% of this change | — |
| [[SNU-1 (line)]] | wt | 73.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 78.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 79.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 60.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 82.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6048), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNU13]] | +0.64 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[PARGP1]] | +0.63 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[RABEPK]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[ANKS3]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[NDUFAF7]] | +0.61 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[TOMM5]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[TRMU]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SLIRP]] | +0.61 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[MMS19]] | +0.60 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[B4GALT2]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[MIR4458HG]] | +0.59 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[PAM16]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFR1]] | -0.60 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.57 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[CHRAC1]] | -0.57 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[NCOA4]] | -0.56 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[LEPROT]] | -0.55 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[SKIL]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[PNRC2]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[YWHAZ]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[ATP7A]] | -0.53 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[MAPRE1]] | -0.53 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[C21orf91]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[JUNB]] | -0.52 | -0.46 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.542). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-8.5, -17.5); signed map (-53.8, -3.1). **Vector** length 82.0, 21.0% of its response variance represented; |z| ≥ 3 in 967 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | +5.0 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +2.7 | +3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.6 | +6.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.6 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +7.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +4.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | -4.1 | +4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | +0.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.0 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | +0.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.9 | -1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | defective in cullin neddylation 1 domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:103,050,686-103,092,194 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2714, FLJ32431 |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTE7](https://www.uniprot.org/uniprotkb/Q9BTE7) (DCN1-like protein 5):

> Contributes to the neddylation of all cullins by transferring NEDD8 from N-terminally acetylated NEDD8-conjugating E2s enzyme to different cullin C-terminal domain-RBX complexes which is necessary for the activation of cullin-RING E3 ubiquitin ligases (CRLs). May play a role in DNA damage response and may participate in cell proliferation and anchorage-independent cell growth.

**Summary**, from NCBI Gene [84259](https://www.ncbi.nlm.nih.gov/gene/84259):

> Enables cullin family protein binding activity. Involved in DNA damage response; positive regulation of protein neddylation; and regulation of cell growth. Located in nucleus and spindle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28409](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28409) · Entrez [84259](https://www.ncbi.nlm.nih.gov/gene/84259) · UniProt [Q9BTE7](https://www.uniprot.org/uniprotkb/Q9BTE7) · Ensembl [ENSG00000137692](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137692)

## Data

Gene col 6048: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6048); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6048, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6048]; `tensor/DDL_lfc|DDL_z.npy` [6048]; `embed/gene_vectors.npy` [6048]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6048 or target_col == 6048). Every well: [[DCUN1D5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCUN1D5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
