---
symbol: "ETFDH"
type: "gene"
col: 10124
ensembl_id: "ENSG00000171503"
name: "electron transfer flavoprotein dehydrogenase"
location: "4q32.1"
module: 40
arm: "+"
pooled_cpm: 33.31
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 18
n_dd_up_clean: 16
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# ETFDH

*electron transfer flavoprotein dehydrogenase* — 4q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.58× (z +13.6, q 1e-39, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.606× (z -10.5, q 3e-23, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABHD18]] (+0.71, fdr 7e-06), [[APTR]] (+0.66, fdr 1e-05), [[DPM3]] (+0.64, fdr 1e-05); moves opposite to [[ZFP41]] (-0.61, fdr 1e-05), [[PURB]] (-0.60, fdr 1e-05), [[ZKSCAN2]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[APPAT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10124.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +13.6 | 1e-39 | 32/48 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +10.2 | 4e-22 | 34/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +10.2 | 6e-22 | 35/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +8.6 | 1e-15 | 32/48 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +7.7 | 2e-12 | 28/48 (NCI-H2347, KATO III, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.35×** | +6.3 | 2e-08 | 29/48 (NCI-H2347, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +5.3 | 7e-06 | 24/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.59×** | +5.1 | 2e-05 | 20/48 (A498, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +4.7 | 2e-04 | 17/48 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.6 | 2e-04 | 21/48 (C32, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Retinoic acid (drug)]] 5 µM |  | 1.15× | +4.2 | 0.001 | 7/48 (SW480, SNU-423, …) | top dose only |  |
| [[Mifepristone (drug)]] 5 µM |  | **1.23×** | +4.2 | 0.001 | 16/48 (SW480, KATO III, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.21×** | +4.1 | 0.002 | 15/48 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.21×** | +4.0 | 0.002 | 13/48 (A498, LS 180, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +4.0 | 0.003 | 10/48 (AsPC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.004 | 8/48 (LoVo, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10124.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.606×** | -10.5 | 3e-23 | 37/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.609×** | -10.5 | 4e-23 | 31/47 (H4, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.410×** | -9.8 | 2e-20 | 39/48 (SNU-1, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.670×** | -8.1 | 7e-14 | 32/48 (HCT15, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.687×** | -7.9 | 3e-13 | 30/48 (PANC-1, A-427, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.498×** | -7.7 | 1e-12 | 30/48 (PANC-1, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.814×** | -6.1 | 7e-08 | 26/47 (NCI-H1792, SW 900, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.748×** | -6.1 | 7e-08 | 23/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.748×** | -6.1 | 7e-08 | 23/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.795×** | -4.8 | 8e-05 | 21/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.805×** | -4.6 | 2e-04 | 22/48 (PANC-1, AsPC-1, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.791×** | -4.5 | 3e-04 | 19/43 (LS 180, SW480, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.807×** | -4.5 | 3e-04 | 17/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.810×** | -4.4 | 4e-04 | 22/48 (Hs 766T, NCI-H460, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.817×** | -4.0 | 0.002 | 18/47 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.820×** | -3.9 | 0.004 | 17/47 (BT-474, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Demeclocycline (drug)]] 5 µM |  | 0.893× | -3.4 | 0.026 | 9/48 (A498, SW 900, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.761×** | -3.0 | 0.071 | 9/48 (CFPAC-1, C32, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10124. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 69.2 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.442× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 33.6 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.302× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 59.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -14.5) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.283× (z -12.7) |
| [[H4 (line)]] | wt | 33.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0487× (z -18.0) |
| [[HCT15 (line)]] | alt | 54.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -10.0) |
| [[LS 180 (line)]] | wt | 57.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -15.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 44.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[SW48 (line)]] | wt | 39.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.100× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[SW480 (line)]] | alt | 29.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.418× (z -9.4) |
| [[A498 (line)]] | wt | 39.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.35× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 20.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.171× (z -10.8) |
| [[HOP62 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.410× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 51.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[HT-29 (line)]] | alt | 31.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.333× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 22.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +10.9) | — |
| [[RKO (line)]] | wt | 31.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +9.6) | — |
| [[SW 1088 (line)]] | alt | 58.3 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0716× (z -8.9) |
| [[SW1417 (line)]] | alt | 18.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +8.8) | — |
| [[A-172 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10124), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD18]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[APTR]] | +0.66 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[DPM3]] | +0.64 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[TULP3]] | +0.63 | +0.57 / +0.59 | both halves | 8e-06 |  |
| [[SEC22A]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[PIK3C2A]] | +0.61 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[RAB6A]] | +0.60 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[EAF2]] | +0.60 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[KIZ]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[IFT20]] | +0.59 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[DNAJC4]] | +0.59 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[SLC17A5]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFP41]] | -0.61 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[PURB]] | -0.60 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | -0.60 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[EBNA1BP2]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[CEP41]] | -0.60 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[TMEM185B]] | -0.59 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[COA7]] | -0.59 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[PUF60]] | -0.57 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[EIF4G1]] | -0.56 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[SFPQ]] | -0.56 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[RIF1]] | -0.56 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[GRWD1]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APPAT]] | B | APPAT activity raises ETFDH's level | lines that do not express APPAT (7) vs lines expressing it (43) | 1.44× lower at baseline in the lines without APPAT | 0.098 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.582). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-25.3, -37.1); signed map (-44.5, 13.7). **Vector** length 92.2, 20.4% of its response variance represented; |z| ≥ 3 in 1,062 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | +3.8 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +13.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +7.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.8 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +4.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.5 | +2.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.1 | +3.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.3 | -10.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -10.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -7.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -9.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | electron transfer flavoprotein dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.1 — chr4:158,671,968-158,710,742 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ETFQO |
| Gene groups (HGNC) | Flavoproteins; Oxidoreductases |
| Hallmark sets | FATTY_ACID_METABOLISM, XENOBIOTIC_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 2 pathways, smallest: Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16134](https://www.uniprot.org/uniprotkb/Q16134) (Electron transfer flavoprotein-ubiquinone oxidoreductase, mitochondrial):

> Links fatty acid beta-oxidation and amino acid catabolism to the respiratory chain by transferring electrons from the electron transfer flavoprotein (ETF) to ubiquinone.

**Summary**, from NCBI Gene [2110](https://www.ncbi.nlm.nih.gov/gene/2110):

> This gene encodes a component of the electron-transfer system in mitochondria and is essential for electron transfer from a number of mitochondrial flavin-containing dehydrogenases to the main respiratory chain. Mutations in this gene are associated with glutaric acidemia. Alternatively spliced transcript variants that encode distinct isoforms have been observed. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:3483](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3483) · Entrez [2110](https://www.ncbi.nlm.nih.gov/gene/2110) · UniProt [Q16134](https://www.uniprot.org/uniprotkb/Q16134) · Ensembl [ENSG00000171503](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171503)

## Data

Gene col 10124: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10124); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10124, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10124]; `tensor/DDL_lfc|DDL_z.npy` [10124]; `embed/gene_vectors.npy` [10124]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10124 or target_col == 10124). Every well: [[ETFDH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ETFDH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
