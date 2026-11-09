---
symbol: "EIF3I"
type: "gene"
col: 1401
ensembl_id: "ENSG00000084623"
name: "eukaryotic translation initiation factor 3 subunit I"
location: "1p35.2"
module: 60
arm: "+"
pooled_cpm: 67.08
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# EIF3I

*eukaryotic translation initiation factor 3 subunit I* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.01× (z +12.9, q 4e-35, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.01× (z +8.1, q 6e-14, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Rifaximin (drug)]] 5 µM in 1 line (SW 1271 0.0594×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD8]] (+0.63, fdr 7e-06), [[GPATCH2L]] (+0.59, fdr 1e-05), [[RPTOR]] (+0.57, fdr 1e-05); moves opposite to [[TXNDC16]] (-0.59, fdr 3e-05), [[HMGN3]] (-0.58, fdr 1e-05), [[RCOR3]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1401.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.01×** | +12.9 | 4e-35 | 48/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.58×** | +10.7 | 5e-24 | 41/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.25×** | +8.8 | 3e-16 | 44/45 (KATO III, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.01×** | +8.1 | 6e-14 | 47/48 (SW480, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.88×** | +7.3 | 2e-11 | 46/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +7.3 | 4e-11 | 41/48 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.86×** | +7.2 | 4e-11 | 45/48 (NCI-H1573, LoVo, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +6.4 | 1e-08 | 37/48 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.68×** | +6.0 | 1e-07 | 44/49 (NCI-H1573, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +5.2 | 1e-05 | 36/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.51×** | +4.8 | 9e-05 | 36/48 (NCI-H1573, NCI-H460, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +4.6 | 2e-04 | 39/48 (NCI-H1573, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.47×** | +4.5 | 3e-04 | 33/48 (SW480, COLO 205, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **1.46×** | +4.4 | 4e-04 | 37/47 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.94×** | +4.1 | 0.002 | 37/48 (HT-29, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.023 | 28/48 (A-172, HOP62, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.027 | 27/48 (NCI-H2030, SW480, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.035 | 24/48 (HOP62, SK-MEL-2, …) | all doses, flat |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.68×** | +3.2 | 0.037 | 28/48 (C32, SNU-423, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.61×** | +2.9 | 0.073 | 24/48 (NCI-H1792, HT-29, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +2.8 | 0.087 | 22/48 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **1.59×** | +2.8 | 0.087 | 22/48 (NCI-H1792, PANC-1, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1401.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Rifaximin (drug)]] 5 µM in 1 line (SW 1271 0.0594×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.751× | -3.4 | 0.32 | 32/48 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.759× | -3.1 | 0.32 | 24/47 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.771× | -3.1 | 0.32 | 24/48 (A-427, NCI-H2030, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1401. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 46.5 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.14× (z +12.1) | — |
| [[A498 (line)]] | wt | 52.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A549 (line)]] | wt | 56.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LoVo (line)]] | wt | 58.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.44× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 78.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW480 (line)]] | alt | 70.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.38× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.94× (z +10.1) | — |
| [[A-172 (line)]] | wt | 35.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HOP62 (line)]] | alt | 66.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HT-29 (line)]] | alt | 63.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[KATO III (line)]] | alt | 57.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.49× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 47.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.01× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H2347 (line)]] | alt | 63.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +12.8) | — |
| [[NCI-H460 (line)]] | wt | 52.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[PANC-1 (line)]] | alt | 91.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SNU-423 (line)]] | alt | 70.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW 900 (line)]] | alt | 43.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-427 (line)]] | wt | 87.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[C32 (line)]] | wt | 59.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[CFPAC-1 (line)]] | alt | 61.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[COLO 205 (line)]] | alt | 38.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.53× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[H4 (line)]] | wt | 75.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[Hs 766T (line)]] | wt | 71.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HS-578T (line)]] | alt | 98.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LOX-IMVI (line)]] | wt | 63.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LS 180 (line)]] | wt | 62.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RPMI-7951 (line)]] | alt | 70.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SNU-1 (line)]] | wt | 61.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW 1271 (line)]] | alt | 55.6 | 0 | 1 | — | [[Rifaximin (drug)]] 5 µM 0.0594× (z -9.0) |
| [[AN3 CA (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 90.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 71.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1401), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD8]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 | STRING 454 |
| [[GPATCH2L]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[RPTOR]] | +0.57 | +0.63 / +0.52 | both halves | 1e-05 | same gene group |
| [[CCT4]] | +0.56 | +0.63 / +0.50 | both halves | 1e-05 | STRING 819 |
| [[CCT6A]] | +0.56 | +0.57 / +0.50 | both halves | 1e-05 | STRING 629 |
| [[PSMC4]] | +0.55 | +0.57 / +0.40 | both halves | 5e-05 | STRING 466 |
| [[MAPKAP1]] | +0.55 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[PSMD12]] | +0.55 | +0.63 / +0.40 | both halves | 4e-05 | STRING 479 |
| [[RTF2]] | +0.54 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[PRR14L]] | +0.54 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[TAF13]] | +0.53 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[PSMB7]] | +0.53 | +0.46 / +0.46 | both halves | 3e-05 | STRING 999 |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC16]] | -0.59 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[HMGN3]] | -0.58 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[RCOR3]] | -0.57 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[MAZ]] | -0.56 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[GMNN]] | -0.55 | -0.37 / -0.57 | both halves | 9e-05 |  |
| [[RSBN1L]] | -0.55 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[ENY2]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[SAP30]] | -0.53 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[MIS18BP1]] | -0.53 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[ELF2]] | -0.52 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[LCORL]] | -0.52 | -0.59 / -0.36 | both halves | 9e-05 |  |
| [[KCTD3]] | -0.51 | -0.36 / -0.62 | both halves | 9e-05 | same gene group |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.508). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-2.0, -40.5); signed map (-24.1, -30.3). **Vector** length 61.3, 16.2% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.52 to 4); *proteasome* (control, mean cos +0.51 to 4); *Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.6 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.5 | +7.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.8 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | +4.1 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.9 | +2.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~76% of this change | -3.4 | +3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | -2.3 | +3.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | +0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.4 | -0.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 3 subunit I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:32,221,077-32,245,397 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRIP-1, eIF3-beta, eIF3-p36; previously EIF3S2 |
| Gene groups (HGNC) | WD repeat domain containing; Eukaryotic translation initiation factor 3 complex subunits |
| Reactome | 14 pathways, smallest: Formation of the ternary complex, and subsequently, the 43S complex; Ribosomal scanning and start codon recognition; Translation initiation complex formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13347](https://www.uniprot.org/uniprotkb/Q13347) (Eukaryotic translation initiation factor 3 subunit I):

> Component of the eukaryotic translation initiation factor 3 (eIF-3) complex, which is required for several steps in the initiation of protein synthesis. The eIF-3 complex associates with the 40S ribosome and facilitates the recruitment of eIF-1, eIF-1A, eIF-2:GTP:methionyl-tRNAi and eIF-5 to form the 43S pre-initiation complex (43S PIC). The eIF-3 complex stimulates mRNA recruitment to the 43S PIC and scanning of the mRNA for AUG recognition. The eIF-3 complex is also required for disassembly …

**Summary**, from NCBI Gene [8668](https://www.ncbi.nlm.nih.gov/gene/8668):

> Contributes to translation initiation factor activity. Involved in translational initiation. Located in extracellular exosome. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3272](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3272) · Entrez [8668](https://www.ncbi.nlm.nih.gov/gene/8668) · UniProt [Q13347](https://www.uniprot.org/uniprotkb/Q13347) · Ensembl [ENSG00000084623](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084623)

## Data

Gene col 1401: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1401); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1401, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1401]; `tensor/DDL_lfc|DDL_z.npy` [1401]; `embed/gene_vectors.npy` [1401]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1401 or target_col == 1401). Every well: [[EIF3I — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF3I.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
