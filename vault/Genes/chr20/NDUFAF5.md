---
symbol: "NDUFAF5"
type: "gene"
col: 2104
ensembl_id: "ENSG00000101247"
name: "NADH:ubiquinone oxidoreductase complex assembly factor 5"
location: "20p12.1"
module: 17
arm: "+"
pooled_cpm: 23.66
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# NDUFAF5

*NADH:ubiquinone oxidoreductase complex assembly factor 5* — 20p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.50× (z +13.8, q 8e-41, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.596× (z -7.3, q 1e-10, down in 22 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.724× (z -6.5, q 2e-08, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SHP-77 0.236×, C-33 A 0.120×, PANC-1 0.348×, HEC-1-A 0.254×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (CFPAC-1 0.0688×; ⚠ transcription drop; cell-cycle shift, explains ~58% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.0939×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.308×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.413×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IRAK1BP1]] (+0.69, fdr 7e-06), [[PCGF6]] (+0.69, fdr 7e-06), [[SNX4]] (+0.68, fdr 7e-06); moves opposite to [[LINC00910]] (-0.63, fdr 1e-05), [[SLC9A1]] (-0.63, fdr 7e-06), [[CCNYL1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2104.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.50×** | +13.8 | 8e-41 | 45/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **5.21×** | +12.2 | 8e-32 | 44/47 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.58×** | +6.5 | 2e-08 | 28/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +6.2 | 6e-08 | 31/47 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +5.8 | 7e-07 | 27/47 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.51×** | +5.8 | 7e-07 | 25/47 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.49×** | +5.6 | 2e-06 | 24/47 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +5.5 | 2e-06 | 29/48 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +5.5 | 3e-06 | 26/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.41×** | +4.6 | 3e-04 | 22/47 (LOX-IMVI, BT-474, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +4.5 | 3e-04 | 22/48 (SNU-423, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +4.5 | 4e-04 | 23/48 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +4.2 | 0.001 | 22/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.0 | 0.003 | 21/47 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +4.0 | 0.003 | 22/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.041 | 16/47 (SK-MEL-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.54×** | +3.2 | 0.041 | 8/47 (C32, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.041 | 15/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2104.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SHP-77 0.236×, C-33 A 0.120×, PANC-1 0.348×, HEC-1-A 0.254×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (CFPAC-1 0.0688×; ⚠ transcription drop; cell-cycle shift, explains ~58% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.0939×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.308×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.413×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.596×** | -7.3 | 1e-10 | 22/42 (SHP-77, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -6.5 | 2e-08 | 32/48 (NCI-H2347, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.623×** | -6.4 | 2e-08 | 22/35 (HEC-1-A, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.741×** | -4.1 | 0.006 | 22/48 (NCI-H2347, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | 0.794× | -3.3 | 0.12 | 12/48 (HOP62, SK-MEL-2, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 0.651× | -3.2 | 0.14 | 13/47 (HS-578T, HOP62, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2104. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 20.7 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.40× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.0939× (z -14.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 19.8 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.50× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 20.4 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 9.98× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -9.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 44.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +11.8) | — |
| [[SW480 (line)]] | alt | 38.0 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 8.03× (z +11.3) | — |
| [[KATO III (line)]] | alt | 26.3 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 14.2× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 27.8 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 13.6× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 61.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.308× (z -10.4) |
| [[A-427 (line)]] | wt | 16.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +9.9) | — |
| [[A498 (line)]] | wt | 21.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.57× (z +9.5) | — |
| [[A549 (line)]] | wt | 33.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 28.9 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.43× (z +8.8) | — |
| [[C-33 A (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -12.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 23.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0688× (z -17.4) ⚠ transcription drop; cell-cycle shift, explains ~58% of this change |
| [[LOX-IMVI (line)]] | wt | 21.3 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.12× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 19.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -9.7) |
| [[SHP-77 (line)]] | alt | 77.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -12.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2104), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRAK1BP1]] | +0.69 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[PCGF6]] | +0.69 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[SNX4]] | +0.68 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[NDUFA9]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 707 |
| [[SAAL1]] | +0.65 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[RPP30]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[RBM45]] | +0.65 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[MRPS35]] | +0.64 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[HARS2]] | +0.64 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[SLC25A12]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport |
| [[MRPL16]] | +0.63 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[NDUFS6]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 841 |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00910]] | -0.63 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[SLC9A1]] | -0.63 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[CCNYL1]] | -0.61 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[ZSWIM6]] | -0.61 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[FOSB]] | -0.61 | -0.57 / -0.58 | both halves | 8e-06 |  |
| [[C6orf62]] | -0.58 | -0.49 / -0.68 | both halves | 1e-05 |  |
| [[TRIM72]] | -0.58 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[CATSPERG]] | -0.57 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[TEX14]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[MIR9-1HG]] | -0.56 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[ARF4]] | -0.56 | -0.46 / -0.66 | both halves | 2e-05 |  |
| [[HAP1]] | -0.56 | -0.54 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.571). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-21.8, -2.0); signed map (-25.8, -17.7). **Vector** length 83.5, 18.0% of its response variance represented; |z| ≥ 3 in 889 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.1 | +2.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +13.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +12.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.9 | -0.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +0.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -6.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -4.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.1 | -2.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.0 | -0.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.8 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase complex assembly factor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.1 — chr20:13,785,007-13,821,580 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ842G6.1; previously C20orf7 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors; 7BS non-methyltransferases |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TEU4](https://www.uniprot.org/uniprotkb/Q5TEU4) (Arginine-hydroxylase NDUFAF5, mitochondrial):

> Arginine hydroxylase that mediates hydroxylation of 'Arg-111' of NDUFS7 and is involved in the assembly of mitochondrial NADH:ubiquinone oxidoreductase complex (complex I, MT-ND1) at early stages. May also have methyltransferase activity (Probable).

**Summary**, from NCBI Gene [79133](https://www.ncbi.nlm.nih.gov/gene/79133):

> The NADH-ubiquinone oxidoreductase complex (complex I) of the mitochondrial respiratory chain catalyzes the transfer of electrons from NADH to ubiquinone, and consists of at least 43 subunits. The complex is located in the inner mitochondrial membrane. This gene encodes a mitochondrial protein that is associated with the matrix face of the mitochondrial inner membrane and is required for complex I assembly. A mutation in this gene results in mitochondrial complex I deficiency. Multiple …

**Accessions** — [HGNC:15899](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15899) · Entrez [79133](https://www.ncbi.nlm.nih.gov/gene/79133) · UniProt [Q5TEU4](https://www.uniprot.org/uniprotkb/Q5TEU4) · Ensembl [ENSG00000101247](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101247)

## Data

Gene col 2104: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2104); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2104, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2104]; `tensor/DDL_lfc|DDL_z.npy` [2104]; `embed/gene_vectors.npy` [2104]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2104 or target_col == 2104). Every well: [[NDUFAF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFAF5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
