---
symbol: "GTF3C1"
type: "gene"
col: 1179
ensembl_id: "ENSG00000077235"
name: "general transcription factor IIIC subunit 1"
location: "16p12.1"
module: 127
arm: "+"
pooled_cpm: 62.64
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# GTF3C1

*general transcription factor IIIC subunit 1* — 16p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.11× (z +14.1, q 2e-42, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.806× (z -3.9, q 0.049, down in 23 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 0.758× (z -3.7, q 0.051, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (AsPC-1 0.238×, LS 180 0.323×, NCI-H1573 0.382×, Panc 03.27 0.367×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.132×, LoVo 0.355×, NCI-H1573 0.345×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.115×, HCT15 0.180×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[XRK3F2 (drug)]] 0.5 µM in 1 line (Hs 766T 0.189×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.277×); [[Auranofin (drug)]] 5 µM in 1 line (SW 1088 0.0786×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAF6]] (+0.72, fdr 7e-06), [[TGOLN2]] (+0.68, fdr 7e-06), [[SNRNP200]] (+0.67, fdr 7e-06); moves opposite to [[EIF3J-DT]] (-0.61, fdr 1e-05), [[SNHG8]] (-0.60, fdr 1e-05), [[OOEP]] (-0.57, fdr 2e-05).
> It is in [[Module 127]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1179.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.11×** | +14.1 | 2e-42 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.00×** | +13.1 | 1e-36 | 45/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +13.0 | 1e-36 | 46/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.63×** | +9.5 | 2e-19 | 40/49 (LoVo, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.31×** | +8.3 | 2e-14 | 40/48 (MIA PaCa-2, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +7.6 | 3e-12 | 40/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +6.1 | 9e-08 | 23/48 (HT-29, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +5.1 | 2e-05 | 32/48 (C-33 A, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +5.0 | 3e-05 | 32/48 (SK-MEL-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +4.8 | 1e-04 | 36/49 (AsPC-1, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.24×** | +4.1 | 0.002 | 25/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.23×** | +3.9 | 0.005 | 22/48 (C-33 A, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **1.22×** | +3.7 | 0.008 | 20/48 (LoVo, SW480, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.20×** | +3.5 | 0.021 | 22/48 (A-172, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.20×** | +3.3 | 0.035 | 20/48 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tadalafil (drug)]] 5 µM |  | 1.19× | +3.2 | 0.046 | 20/48 (NCI-H2030, A-172, …) | top dose only | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.086 | 12/47 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1179.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (AsPC-1 0.238×, LS 180 0.323×, NCI-H1573 0.382×, Panc 03.27 0.367×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.132×, LoVo 0.355×, NCI-H1573 0.345×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.115×, HCT15 0.180×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[XRK3F2 (drug)]] 0.5 µM in 1 line (Hs 766T 0.189×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.277×); [[Auranofin (drug)]] 5 µM in 1 line (SW 1088 0.0786×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.806×** | -3.9 | 0.049 | 23/47 (hTERT-HPNE, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.758×** | -3.7 | 0.051 | 27/48 (SNU-1, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.787× | -3.2 | 0.23 | 17/48 (LoVo, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1179. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 55.1 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.53× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 71.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.29× (z +10.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 76.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 62.2 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.47× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.345× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 54.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.31× (z +11.6) | — |
| [[RKO (line)]] | wt | 89.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -22.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 54.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.80× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 58.3 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.21× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 50.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.53× (z +8.6) | — |
| [[SW 1088 (line)]] | alt | 73.6 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0786× (z -9.2) |
| [[A549 (line)]] | wt | 63.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 92.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -11.9) |
| [[BT-474 (line)]] | alt | 60.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.61× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 45.8 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.48× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 78.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 51.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.22× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 70.0 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.189× (z -12.6) |
| [[HT-29 (line)]] | alt | 52.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.8) | — |
| [[hTERT-HPNE (line)]] | wt | 57.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.317× (z -9.6) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 50.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.29× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 60.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 49.1 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.51× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 43.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.367× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 102 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.13× (z +8.7) | — |
| [[A-172 (line)]] | wt | 79.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 86.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 63.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 97.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 80.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 75.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 78.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1179), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF6]] | +0.72 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[TGOLN2]] | +0.68 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SNRNP200]] | +0.67 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[PCNX3]] | +0.64 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[AP2M1]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[UGGT1]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PRPF31]] | +0.63 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[DHX16]] | +0.62 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[BAP1]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[PRPF8]] | +0.62 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[BLTP2]] | +0.61 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[EMC1]] | +0.61 | +0.59 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF3J-DT]] | -0.61 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[SNHG8]] | -0.60 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[OOEP]] | -0.57 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[MSX1]] | -0.54 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[BTG3]] | -0.54 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[HRK]] | -0.53 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[GAS5]] | -0.52 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[EIF1]] | -0.52 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ZFAS1]] | -0.52 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[SPATC1]] | -0.51 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[MIR17HG]] | -0.51 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[ABHD5]] | -0.50 | -0.48 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-27.8, -22.7); signed map (-21.2, -37.0). **Vector** length 84.3, 19.7% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.0 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.7 | -2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +13.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +14.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +9.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +8.3 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | +1.6 | +1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +1.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.5 | +1.1 |
|  | [[Riluzole hydrochloride (drug)]] 0.5 µM |  | +1.5 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.4 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIIC subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.1 — chr16:27,459,555-27,549,913 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TFIIIC220 |
| Gene groups (HGNC) | General transcription factor IIIC complex subunits |
| Reactome | 5 pathways, smallest: RNA Polymerase III Transcription Initiation From Type 2 Promoter; RNA Polymerase III Transcription Initiation From Type 1 Promoter; RNA Polymerase III Transcription Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12789](https://www.uniprot.org/uniprotkb/Q12789) (General transcription factor 3C polypeptide 1):

> Required for RNA polymerase III-mediated transcription. Component of TFIIIC that initiates transcription complex assembly on tRNA and is required for transcription of 5S rRNA and other stable nuclear and cytoplasmic RNAs. Binds to the box B promoter element.

**Summary**, from NCBI Gene [2975](https://www.ncbi.nlm.nih.gov/gene/2975):

> Enables RNA polymerase III general transcription initiation factor activity. Involved in transcription initiation at RNA polymerase III promoter. Located in nucleoplasm. Part of transcription factor TFIIIC complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:4664](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4664) · Entrez [2975](https://www.ncbi.nlm.nih.gov/gene/2975) · UniProt [Q12789](https://www.uniprot.org/uniprotkb/Q12789) · Ensembl [ENSG00000077235](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077235)

## Data

Gene col 1179: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1179); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1179, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1179]; `tensor/DDL_lfc|DDL_z.npy` [1179]; `embed/gene_vectors.npy` [1179]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1179 or target_col == 1179). Every well: [[GTF3C1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF3C1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
