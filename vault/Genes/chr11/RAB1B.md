---
symbol: "RAB1B"
type: "gene"
col: 10540
ensembl_id: "ENSG00000174903"
name: "RAB1B, member RAS oncogene family"
location: "11q13.2"
module: 153
arm: "+"
pooled_cpm: 34.09
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# RAB1B

*RAB1B, member RAS oncogene family* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.76× (z +18.5, q 0e+00, up in 39 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (PANC-1 3.78×, A498 4.78×, NCI-H2030 3.78×, HEC-1-A 3.25×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (PANC-1 3.16×, SW480 2.93×, A-172 4.65×, MIA PaCa-2 4.24×, …; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 2.55×, NCI-H1573 2.92×; ⚠ cell-cycle shift, explains ~31% of this change).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.514× (z -12.2, q 2e-31, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAG6]] (+0.76, fdr 7e-06), [[LIN7C]] (+0.72, fdr 1e-05), [[PPP2R1A]] (+0.71, fdr 2e-05); moves opposite to [[CAMLG]] (-0.65, fdr 8e-05), [[GAS5]] (-0.64, fdr 1e-05), [[SNHG7]] (-0.63, fdr 4e-05).
> It is in [[Module 153]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 11 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10540.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (PANC-1 3.78×, A498 4.78×, NCI-H2030 3.78×, HEC-1-A 3.25×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (PANC-1 3.16×, SW480 2.93×, A-172 4.65×, MIA PaCa-2 4.24×, …; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 2.55×, NCI-H1573 2.92×; ⚠ cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.76×** | +18.5 | 0e+00 | 39/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.73×** | +17.6 | 0e+00 | 37/37 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +10.9 | 3e-25 | 31/38 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.48×** | +7.2 | 1e-10 | 39/48 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.43×** | +6.5 | 1e-08 | 35/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.40×** | +6.2 | 6e-08 | 31/47 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.33×** | +5.2 | 1e-05 | 25/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.7 | 2e-04 | 16/35 (HEC-1-A, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.29×** | +4.6 | 3e-04 | 21/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.19× | +4.5 | 4e-04 | 17/48 (SNU-423, HEC-1-A, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.22×** | +3.5 | 0.021 | 18/47 (NCI-H23, hTERT-HPNE, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.18× | +3.0 | 0.12 | 11/48 (NCI-H1573, PANC-1, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10540.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.514×** | -12.2 | 2e-31 | 46/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.558×** | -10.7 | 3e-24 | 45/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.559×** | -10.7 | 3e-24 | 42/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.642×** | -8.1 | 6e-14 | 42/48 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -8.1 | 8e-14 | 32/47 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.784×** | -6.3 | 2e-08 | 29/48 (RPMI-7951, BT-474, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -5.4 | 6e-06 | 24/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -5.0 | 4e-05 | 2/48 (SHP-77, SW 1271) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.620×** | -4.6 | 3e-04 | 23/48 (HT-29, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.784×** | -4.5 | 5e-04 | 22/48 (C32, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.846× | -3.1 | 0.10 | 13/48 (LOX-IMVI, NCI-H1573, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.891× | -3.0 | 0.11 | 16/48 (SW 1271, SW 900, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.849× | -3.0 | 0.11 | 12/47 (hTERT-HPNE, KATO III, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10540. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 42.3 | 5 (5 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.78× (z +14.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.452× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 38.8 | 2 (2 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +10.6) ⚠ cell-cycle shift, explains ~31% of this change | [[Panobinostat (drug)]] 0.5 µM 0.365× (z -10.0) |
| [[A498 (line)]] | wt | 19.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.78× (z +13.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 27.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +10.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.355× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 33.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.71× (z +10.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.358× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 22.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.24× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 27.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +12.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 26.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.32× (z +9.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 31.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 39.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +10.3) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 30.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 20.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +10.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 35.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +10.3) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 39.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +9.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 45.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 36.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.78× (z +12.3) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 50.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.74× (z +8.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 44.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +9.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -10.0) |
| [[SW480 (line)]] | alt | 35.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +12.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 38.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +10.3) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 42.1 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0937× (z -11.4) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 40.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.16× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 52.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +8.7) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 36.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 50.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.32× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 36.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 44.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +10.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10540), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAG6]] | +0.76 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.72 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[PPP2R1A]] | +0.71 | +0.48 / +0.75 | both halves | 2e-05 | pathway: Mitotic Prophase |
| [[SRP9]] | +0.70 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[RAB11B]] | +0.69 | +0.58 / +0.72 | both halves | 7e-06 | same gene group; pathway: RAB geranylgeranylation; STRING 916 |
| [[MED12]] | +0.69 | +0.52 / +0.73 | both halves | 1e-05 |  |
| [[SF3B4]] | +0.69 | +0.51 / +0.74 | both halves | 1e-05 |  |
| [[CBX5]] | +0.69 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SF3A1]] | +0.68 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[ARAF]] | +0.68 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[PIGT]] | +0.68 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[SZRD1]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 8 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMLG]] | -0.65 | -0.37 / -0.71 | both halves | 8e-05 |  |
| [[GAS5]] | -0.64 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[SNHG7]] | -0.63 | -0.42 / -0.68 | both halves | 4e-05 |  |
| [[SNHG6]] | -0.62 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[RPL18]] ⚠ | -0.61 | -0.32 / -0.68 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS13]] ⚠ | -0.61 | -0.37 / -0.66 | both halves | 8e-05 | same gene group; ⚠ in the vector space only through flagged drug-doses |
| [[PDCD5]] | -0.61 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[NSUN5P2-1]] ⚠ | -0.60 | -0.47 / -0.64 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS26]] | -0.60 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[RPL36AL]] ⚠ | -0.60 | -0.22 / -0.65 | both halves | 6e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS8]] | -0.60 | -0.36 / -0.65 | both halves | 9e-05 | same gene group |
| [[RPL23]] | -0.60 | -0.33 / -0.66 | both halves | 1e-04 | same gene group |
| [[ADGRL3-AS1]] | -0.60 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[RPL26]] | -0.60 | -0.34 / -0.66 | both halves | 1e-04 |  |
| [[COMMD6]] | -0.60 | -0.22 / -0.68 | both halves | 6e-04 |  |
| [[RPL36]] | -0.59 | -0.37 / -0.64 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises RAB1B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises RAB1B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.760). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.3, -23.6); signed map (-14.8, -34.4). **Vector** length 80.6, 16.5% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +17.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +18.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +10.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +5.2 | +6.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.8 | +4.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.8 | +1.2 |
|  | [[Folic acid (drug)]] 5 µM |  | +1.5 | +2.1 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -6.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.1 | -3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.0 | -8.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | +0.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | RAB1B, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,268,590-66,277,492 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases; Small nucleolar RNA protein coding host genes |
| Reactome | 18 pathways, smallest: Golgi Cisternae Pericentriolar Stack Reorganization; RAB geranylgeranylation; COPII-mediated vesicle transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0U4](https://www.uniprot.org/uniprotkb/Q9H0U4) (Ras-related protein Rab-1B):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different set of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. Plays a role in the initial events of the autophagic vacuole development which take place at specialized regions of the …

**Summary**, from NCBI Gene [81876](https://www.ncbi.nlm.nih.gov/gene/81876):

> Members of the RAB protein family, such as RAB1B, are low molecular mass monomeric GTPases localized on the cytoplasmic surfaces of distinct membrane-bound organelles. RAB1B functions in the early secretory pathway and is essential for vesicle transport between the endoplasmic reticulum (ER) and Golgi (Chen et al., 1997 [PubMed 9030196]; Alvarez et al., 2003 [PubMed 12802079]).[supplied by OMIM, Jan 2009]

**Accessions** — [HGNC:18370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18370) · Entrez [81876](https://www.ncbi.nlm.nih.gov/gene/81876) · UniProt [Q9H0U4](https://www.uniprot.org/uniprotkb/Q9H0U4) · Ensembl [ENSG00000174903](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174903)

## Data

Gene col 10540: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10540); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10540, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10540]; `tensor/DDL_lfc|DDL_z.npy` [10540]; `embed/gene_vectors.npy` [10540]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10540 or target_col == 10540). Every well: [[RAB1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
