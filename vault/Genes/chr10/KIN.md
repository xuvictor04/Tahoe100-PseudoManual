---
symbol: "KIN"
type: "gene"
col: 7547
ensembl_id: "ENSG00000151657"
name: "Kin17 DNA and RNA binding protein"
location: "10p14"
module: 149
arm: "+"
pooled_cpm: 33.4
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# KIN

*Kin17 DNA and RNA binding protein* — 10p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.67× (z +18.5, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.679× (z -9.3, q 1e-17, down in 24 of 36 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (AsPC-1 0.0857×, LoVo 0.154×, HEC-1-A 0.129×, LS 180 0.149×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.200×, NCI-H2347 0.344×, A498 0.466×, A549 0.382×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H1573 0.252×, hTERT-HPNE 0.256×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM32A]] (+0.69, fdr 1e-05), [[ZNF791]] (+0.66, fdr 1e-05), [[TRIM4]] (+0.65, fdr 1e-05); moves opposite to [[AHCY]] (-0.55, fdr 5e-05), [[INPP4A]] (-0.52, fdr 1e-04), [[SMAD2]] (-0.52, fdr 1e-05).
> It is in [[Module 149]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7547.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +18.5 | 0e+00 | 42/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.14×** | +17.8 | 0e+00 | 44/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.91×** | +14.2 | 9e-44 | 40/49 (PANC-1, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +12.5 | 2e-33 | 35/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +11.6 | 5e-29 | 29/48 (RKO, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +11.5 | 1e-28 | 35/48 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +11.1 | 2e-26 | 37/48 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +10.7 | 1e-24 | 31/48 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +10.5 | 3e-24 | 33/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +8.0 | 6e-14 | 30/42 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +8.0 | 9e-14 | 32/47 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +6.8 | 4e-10 | 23/48 (LoVo, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +6.6 | 2e-09 | 26/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.61×** | +6.3 | 1e-08 | 22/48 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.28×** | +5.8 | 3e-07 | 21/47 (RKO, NCI-H460, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +5.6 | 9e-07 | 17/48 (HOP62, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.8 | 4e-05 | 15/48 (HOP62, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7547.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (AsPC-1 0.0857×, LoVo 0.154×, HEC-1-A 0.129×, LS 180 0.149×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.200×, NCI-H2347 0.344×, A498 0.466×, A549 0.382×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H1573 0.252×, hTERT-HPNE 0.256×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.679×** | -9.3 | 1e-17 | 24/36 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.785×** | -6.2 | 1e-07 | 23/46 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.837× | -4.3 | 0.004 | 16/42 (NCI-H1573, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.875× | -3.2 | 0.19 | 16/47 (NCI-H2347, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7547. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +14.3) | — |
| [[SW480 (line)]] | alt | 37.0 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +10.3) | — |
| [[A498 (line)]] | wt | 46.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.466× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 27.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 47.1 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.88× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 25.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -17.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 32.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 31.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 27.8 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.63× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 55.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.9) | — |
| [[A-172 (line)]] | wt | 37.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.0) | — |
| [[A-427 (line)]] | wt | 30.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -14.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 43.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -9.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0857× (z -20.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 45.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 26.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.3) | — |
| [[hTERT-HPNE (line)]] | wt | 34.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -18.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 30.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -15.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 40.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -11.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 48.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.84× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 38.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -11.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7547), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM32A]] | +0.69 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[ZNF791]] | +0.66 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[TRIM4]] | +0.65 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[ZNF557]] | +0.65 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[SLC4A1AP]] | +0.65 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[TTF1]] | +0.64 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[SNRPB2]] | +0.63 | +0.66 / +0.54 | both halves | 1e-05 | STRING 814 |
| [[USP8]] | +0.63 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[NRBF2]] | +0.63 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[ALKBH1]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[MON1B]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[BRAP]] | +0.59 | +0.68 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHCY]] | -0.55 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[INPP4A]] | -0.52 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[SMAD2]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[NME4]] | -0.51 | -0.56 / -0.27 | both halves | 3e-04 |  |
| [[SMG1P3]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[POLD2]] | -0.51 | -0.53 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.665). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.7, 4.3); signed map (-4.2, -12.6). **Vector** length 73.8, 13.6% of its response variance represented; |z| ≥ 3 in 941 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.4 | +11.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +17.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +14.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +18.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.6 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +5.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.2 | +0.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | -0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +6.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -4.5 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.7 | -9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.3 | -6.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.2 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.0 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.7 | -1.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Lapatinib ditosylate (drug)]] 0.5 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | Kin17 DNA and RNA binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p14 — chr10:7,750,962-7,787,993 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIN17, Rts2 |
| Reactome | 1 pathways, smallest: Protein methylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O60870](https://www.uniprot.org/uniprotkb/O60870) (DNA/RNA-binding protein KIN17):

> Involved in DNA replication and the cellular response to DNA damage. May participate in DNA replication factories and create a bridge between DNA replication and repair mediated by high molecular weight complexes. May play a role in illegitimate recombination and regulation of gene expression. May participate in mRNA processing. Binds, in vitro, to double-stranded DNA. Also shown to bind preferentially to curved DNA in vitro and in vivo (By similarity). Binds via its C-terminal domain to RNA in …

**Summary**, from NCBI Gene [22944](https://www.ncbi.nlm.nih.gov/gene/22944):

> The protein encoded by this gene is a nuclear protein that forms intranuclear foci during proliferation and is redistributed in the nucleoplasm during the cell cycle. Short-wave ultraviolet light provokes the relocalization of the protein, suggesting its participation in the cellular response to DNA damage. Originally selected based on protein-binding with RecA antibodies, the mouse protein presents a limited similarity with a functional domain of the bacterial RecA protein, a characteristic …

**Accessions** — [HGNC:6327](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6327) · Entrez [22944](https://www.ncbi.nlm.nih.gov/gene/22944) · UniProt [O60870](https://www.uniprot.org/uniprotkb/O60870) · Ensembl [ENSG00000151657](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151657)

## Data

Gene col 7547: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7547); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7547, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7547]; `tensor/DDL_lfc|DDL_z.npy` [7547]; `embed/gene_vectors.npy` [7547]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7547 or target_col == 7547). Every well: [[KIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
