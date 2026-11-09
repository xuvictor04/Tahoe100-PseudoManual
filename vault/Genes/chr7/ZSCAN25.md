---
symbol: "ZSCAN25"
type: "gene"
col: 12326
ensembl_id: "ENSG00000197037"
name: "zinc finger and SCAN domain containing 25"
location: "7q22.1"
module: 89
arm: "+"
pooled_cpm: 15.42
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# ZSCAN25

*zinc finger and SCAN domain containing 25* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 3.08× (z +8.7, q 1e-15, up in 34 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.412× (z -13.2, q 9e-37, down in 38 of 40 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (C32 0.0613×, NCI-H460 0.143×, MIA PaCa-2 0.116×, NCI-H2347 0.202×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (HEC-1-A 0.0916×, NCI-H1792 0.0814×, SNU-423 0.0970×, HS-578T 0.0945×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW1417 0.108×, AsPC-1 0.0567×, C32 0.162×, MIA PaCa-2 0.169×; ⚠ toxic; transcription drop); [[Saquinavir (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0840×); [[Allantoin (drug)]] 0.5 µM in 1 line (NCI-H460 0.313×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.175×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALKBH3]] (+0.68, fdr 7e-06), [[ALKBH1]] (+0.66, fdr 1e-05), [[MIEF1]] (+0.65, fdr 1e-05); moves opposite to [[CRY1]] (-0.61, fdr 8e-06), [[PEAK1]] (-0.58, fdr 1e-05), [[HYCC1]] (-0.56, fdr 4e-05).
> It is in [[Module 089]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12326.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **3.08×** | +8.7 | 1e-15 | 34/44 (KATO III, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **3.06×** | +8.7 | 1e-15 | 35/48 (A498, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +8.1 | 1e-13 | 31/47 (RKO, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +6.6 | 5e-09 | 33/48 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +6.2 | 5e-08 | 29/48 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +5.8 | 5e-07 | 21/47 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.32×** | +4.1 | 0.004 | 15/47 (LOX-IMVI, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.005 | 16/46 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.006 | 14/47 (PANC-1, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.30×** | +3.7 | 0.012 | 14/48 (SK-MEL-2, HT-29, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.055 | 9/47 (SK-MEL-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 1.17× | +3.2 | 0.057 | 14/48 (LOX-IMVI, A-427, …) | rises with dose | low cells (technical?) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.2 | 0.057 | 9/48 (KATO III, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.071 | 14/47 (SW1417, SW480, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.074 | 7/47 (A-172, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.074 | 12/45 (BT-474, NCI-H1573, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.078 | 3/48 (Panc 03.27, HOP62, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.090 | 12/48 (BT-474, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12326.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (C32 0.0613×, NCI-H460 0.143×, MIA PaCa-2 0.116×, NCI-H2347 0.202×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (HEC-1-A 0.0916×, NCI-H1792 0.0814×, SNU-423 0.0970×, HS-578T 0.0945×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW1417 0.108×, AsPC-1 0.0567×, C32 0.162×, MIA PaCa-2 0.169×; ⚠ toxic; transcription drop); [[Saquinavir (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0840×); [[Allantoin (drug)]] 0.5 µM in 1 line (NCI-H460 0.313×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.175×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.412×** | -13.2 | 9e-37 | 38/40 (SW1417, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.424×** | -12.3 | 5e-32 | 23/29 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.480×** | -10.1 | 1e-21 | 24/34 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.642×** | -6.3 | 3e-08 | 27/44 (SHP-77, PANC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12326. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 17.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -10.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 43.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0613× (z -20.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 2 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0823× (z -10.0) ⚠ toxic · without an alert: [[Saquinavir (drug)]] 0.5 µM 0.0840× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 18.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 15.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Allantoin (drug)]] 0.5 µM 0.313× (z -9.8) |
| [[SHP-77 (line)]] | alt | 14.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0891× (z -12.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 14.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -10.5) ⚠ cell-cycle shift, explains ~2% of this change |
| [[A498 (line)]] | wt | 14.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -8.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -9.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 9.73 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0567× (z -14.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -10.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 13.6 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.111× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0916× (z -16.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 12.3 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.175× (z -8.9) |
| [[HS-578T (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0945× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -9.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 9.40 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0814× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -10.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -8.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 24.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.40× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0970× (z -11.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -15.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -10.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12326), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALKBH3]] | +0.68 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[ALKBH1]] | +0.66 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[MIEF1]] | +0.65 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[ALKBH4]] | +0.65 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[TEFM]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[METTL22]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[MTERF4]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[GTPBP10]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[GTF3C2]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[RNF25]] | +0.62 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[PTCD1]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[ZNF223]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRY1]] | -0.61 | -0.58 / -0.61 | both halves | 8e-06 |  |
| [[PEAK1]] | -0.58 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[HYCC1]] | -0.56 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[EPB41L2]] | -0.50 | -0.51 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.768). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-44.1, 6.7); signed map (-9.9, -16.1). **Vector** length 64.8, 10.0% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.1 | +8.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +8.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +8.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | +1.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.9 | -0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +1.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.8 | -6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.8 | -13.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +1.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -0.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.8 | -12.3 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.4 | -2.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Artemether (drug)]] 0.05 µM |  | -1.3 | -0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and SCAN domain containing 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:99,616,946-99,632,408 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32468; previously ZNF498 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NSZ9](https://www.uniprot.org/uniprotkb/Q6NSZ9) (Zinc finger and SCAN domain-containing protein 25):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [221785](https://www.ncbi.nlm.nih.gov/gene/221785):

> This gene encodes a protein that bears some similarity to zinc finger proteins, which are involved in DNA binding and protein-protein interactions. Multiple alternatively spliced transcript variants have been identified, but the full-length nature for most of them has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:21961](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21961) · Entrez [221785](https://www.ncbi.nlm.nih.gov/gene/221785) · UniProt [Q6NSZ9](https://www.uniprot.org/uniprotkb/Q6NSZ9) · Ensembl [ENSG00000197037](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197037)

## Data

Gene col 12326: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12326); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12326, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12326]; `tensor/DDL_lfc|DDL_z.npy` [12326]; `embed/gene_vectors.npy` [12326]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12326 or target_col == 12326). Every well: [[ZSCAN25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSCAN25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
