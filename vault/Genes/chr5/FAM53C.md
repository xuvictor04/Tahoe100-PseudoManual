---
symbol: "FAM53C"
type: "gene"
col: 4213
ensembl_id: "ENSG00000120709"
name: "family with sequence similarity 53 member C"
location: "5q31.2"
module: 93
arm: "+"
pooled_cpm: 51.88
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# FAM53C

*family with sequence similarity 53 member C* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.47× (z +11.5, q 4e-28, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.359× (z -9.3, q 1e-17, down in 40 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.585× (z -4.6, q 5e-04, down in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SW1417 0.128×, CFPAC-1 0.161×, NCI-H1573 0.131×, SK-MEL-2 0.190×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (SW480 0.222×, NCI-H2030 0.146×, RKO 0.174×, SK-MEL-2 0.206×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (Panc 03.27 0.0305×, SW1417 0.0986×, SNU-423 0.183×, HepG2/C3A 0.199×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2B]] (+0.85, fdr 7e-06), [[IFRD1]] (+0.78, fdr 7e-06), [[POR]] (+0.76, fdr 7e-06); moves opposite to [[BTBD1]] (-0.68, fdr 1e-05), [[TMEM33]] (-0.68, fdr 1e-05), [[GFM1]] (-0.61, fdr 5e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4213.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.47×** | +11.5 | 4e-28 | 44/48 (AsPC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +10.7 | 5e-24 | 46/49 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.37×** | +7.8 | 1e-12 | 46/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +5.2 | 3e-05 | 42/48 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.83×** | +5.0 | 4e-05 | 38/48 (SW480, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.75×** | +5.0 | 4e-05 | 36/48 (SW480, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.60×** | +4.2 | 0.002 | 28/48 (AsPC-1, KATO III, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +3.9 | 0.008 | 29/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.012 | 30/48 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.51×** | +3.6 | 0.018 | 32/50 (PANC-1, KATO III, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.51×** | +3.6 | 0.019 | 28/48 (SW48, J82, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.2 | 0.063 | 26/47 (NCI-H1573, RKO, …) | rises with dose | cell-cycle shift (explains ~24% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4213.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SW1417 0.128×, CFPAC-1 0.161×, NCI-H1573 0.131×, SK-MEL-2 0.190×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (SW480 0.222×, NCI-H2030 0.146×, RKO 0.174×, SK-MEL-2 0.206×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (Panc 03.27 0.0305×, SW1417 0.0986×, SNU-423 0.183×, HepG2/C3A 0.199×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.359×** | -9.3 | 1e-17 | 40/49 (Panc 03.27, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.405×** | -7.5 | 1e-11 | 40/45 (SW480, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.421×** | -7.5 | 1e-11 | 37/40 (SW1417, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.585×** | -4.6 | 5e-04 | 40/48 (SK-MEL-2, NCI-H1573, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.699× | -3.2 | 0.14 | 26/47 (SW 900, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4213. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 48.7 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -11.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 54.8 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.201× (z -10.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 55.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -11.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 47.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +18.0) | — |
| [[CFPAC-1 (line)]] | alt | 72.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -13.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 59.3 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -9.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 30.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +14.1) | — |
| [[LS 180 (line)]] | wt | 25.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -9.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 80.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 64.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 57.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 45.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -8.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 40.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +12.2) | — |
| [[COLO 205 (line)]] | alt | 54.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -10.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 61.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -10.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 39.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +12.9) | — |
| [[Hs 766T (line)]] | wt | 35.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 36.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +10.4) | — |
| [[J82 (line)]] | alt | 43.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +11.3) | — |
| [[LoVo (line)]] | wt | 63.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 48.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -9.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 71.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0305× (z -19.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 49.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -11.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 69.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -11.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 76.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0986× (z -15.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 51.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -11.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 41.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 65.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -10.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 70.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 67.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 48.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +11.9) | — |
| [[PANC-1 (line)]] | alt | 47.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +14.1) | — |
| [[RPMI-7951 (line)]] | alt | 66.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +8.6) | — |
| [[SW 1271 (line)]] | alt | 79.5 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0808× (z -9.0) ⚠ cell-cycle shift, explains ~75% of this change |
| [[SW 900 (line)]] | alt | 45.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.5) | — |
| [[SW48 (line)]] | wt | 43.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 74.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 86.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4213), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2B]] | +0.85 | +0.81 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[IFRD1]] | +0.78 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[POR]] | +0.76 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[PIM2]] | +0.71 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[POLR2A]] | +0.70 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[SLC9A1]] | +0.69 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[LRRC23]] | +0.69 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[DHDH]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[CNNM4]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[WDR47]] | +0.68 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[MYLIP]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[TRA2A]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTBD1]] | -0.68 | -0.55 / -0.72 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.68 | -0.54 / -0.71 | both halves | 1e-05 |  |
| [[GFM1]] | -0.61 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[EFTUD2]] | -0.60 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[FARSB]] | -0.60 | -0.42 / -0.67 | both halves | 4e-05 |  |
| [[CAPRIN1]] | -0.59 | -0.46 / -0.65 | both halves | 3e-05 |  |
| [[MRPL42]] | -0.58 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[AIFM1]] | -0.58 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[ABHD13]] | -0.58 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[NUP155]] | -0.58 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[NUP42]] | -0.58 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ZC3H14]] | -0.57 | -0.34 / -0.63 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FAM53C's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.843). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.5, -26.1); signed map (3.1, 16.8). **Vector** length 137, 48.0% of its response variance represented; |z| ≥ 3 in 840 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +10.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +2.1 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +3.2 | +2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +3.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.9 | +2.7 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +2.9 | +2.2 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.6 | -7.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.3 | -7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.3 | -9.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -6.3 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.9 | -0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.9 | -4.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.9 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -0.7 |
|  | [[Benztropine (mesylate) (drug)]] 0.5 µM |  | -2.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 53 member C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:138,331,935-138,349,729 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C5orf6 |
| Matched by | ensembl_id |

UniProt [Q9NYF3](https://www.uniprot.org/uniprotkb/Q9NYF3) carries no function annotation.

**Summary**, from NCBI Gene [51307](https://www.ncbi.nlm.nih.gov/gene/51307):

> The protein encoded by this gene belongs to the FAM53 protein family. FAM53 protein family members bind to a transcriptional regulator that modulates cell proliferation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:1336](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1336) · Entrez [51307](https://www.ncbi.nlm.nih.gov/gene/51307) · UniProt [Q9NYF3](https://www.uniprot.org/uniprotkb/Q9NYF3) · Ensembl [ENSG00000120709](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120709)

## Data

Gene col 4213: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4213); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4213, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4213]; `tensor/DDL_lfc|DDL_z.npy` [4213]; `embed/gene_vectors.npy` [4213]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4213 or target_col == 4213). Every well: [[FAM53C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM53C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
