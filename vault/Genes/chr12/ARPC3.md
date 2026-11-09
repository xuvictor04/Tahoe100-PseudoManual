---
symbol: "ARPC3"
type: "gene"
col: 3204
ensembl_id: "ENSG00000111229"
name: "actin related protein 2/3 complex subunit 3"
location: "12q24.11"
module: 142
arm: "+"
pooled_cpm: 115.54
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# ARPC3

*actin related protein 2/3 complex subunit 3* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.35× (z +11.2, q 4e-26, up in 42 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 9 lines (SHP-77 4.23×, NCI-H460 3.08×, SW480 2.92×, HT-29 3.39×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (PANC-1 3.72×, A549 3.66×, C-33 A 5.63×, SNU-423 3.70×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.569× (z -10.8, q 1e-24, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RARS2]] (+0.73, fdr 7e-06), [[UBOX5]] (+0.63, fdr 1e-05), [[C1orf52]] (+0.62, fdr 1e-05); moves opposite to [[PRRC2A]] (-0.58, fdr 1e-05), [[SRSF2]] (-0.54, fdr 1e-05), [[BAHCC1]] (-0.54, fdr 1e-05).
> It is in [[Module 142]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3204.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 9 lines (SHP-77 4.23×, NCI-H460 3.08×, SW480 2.92×, HT-29 3.39×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (PANC-1 3.72×, A549 3.66×, C-33 A 5.63×, SNU-423 3.70×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +11.2 | 4e-26 | 42/44 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +11.1 | 6e-26 | 48/49 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +7.2 | 1e-10 | 36/45 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.31×** | +3.6 | 0.040 | 30/48 (RPMI-7951, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.4 | 0.073 | 29/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 5 µM |  | 1.27× | +3.2 | 0.14 | 28/48 (A498, A-172, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.1 | 0.14 | 0/50 | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.05 µM |  | 1.27× | +3.1 | 0.14 | 31/48 (HepG2/C3A, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3204.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.569×** | -10.8 | 1e-24 | 45/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.565×** | -7.8 | 2e-12 | 43/48 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.572×** | -7.6 | 6e-12 | 43/48 (H4, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.646×** | -5.9 | 4e-07 | 34/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.707×** | -4.7 | 3e-04 | 35/48 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.710×** | -4.6 | 3e-04 | 36/48 (NCI-H1792, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.719×** | -4.3 | 0.001 | 31/48 (AsPC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.559×** | -3.8 | 0.010 | 35/49 (AsPC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **0.824×** | -3.7 | 0.012 | 24/48 (A-427, SHP-77, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.773×** | -3.5 | 0.026 | 27/48 (hTERT-HPNE, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.843× | -3.3 | 0.050 | 25/48 (H4, SW1417, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.753×** | -3.3 | 0.050 | 25/50 (NCI-H23, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.800× | -3.0 | 0.11 | 25/48 (H4, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3204. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 245 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -17.1) |
| [[C-33 A (line)]] | alt | 53.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +10.7) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 144 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 85.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 96.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -12.3) |
| [[HT-29 (line)]] | alt | 119 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -15.4) |
| [[KATO III (line)]] | alt | 109 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -9.8) |
| [[PANC-1 (line)]] | alt | 148 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +12.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 160 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 129 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +11.2) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 97.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 183 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 97.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +11.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 84.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -12.4) |
| [[SHP-77 (line)]] | alt | 74.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +11.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 103 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 103 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +11.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 105 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -9.2) |
| [[A-427 (line)]] | wt | 69.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -8.9) |
| [[AN3 CA (line)]] | alt | 62.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.35× (z +8.8) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 125 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -11.3) |
| [[Hs 766T (line)]] | wt | 103 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.421× (z -8.5) |
| [[HS-578T (line)]] | alt | 109 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -14.5) |
| [[hTERT-HPNE (line)]] | wt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -10.2) |
| [[J82 (line)]] | alt | 134 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -13.6) |
| [[LoVo (line)]] | wt | 106 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 118 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +8.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 75.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 151 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -11.1) |
| [[NCI-H661 (line)]] | alt | 120 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -9.9) |
| [[RKO (line)]] | wt | 103 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -11.2) |
| [[SNU-1 (line)]] | wt | 71.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -12.0) |
| [[SW48 (line)]] | wt | 83.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.55× (z +9.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 77.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 80.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 121 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 114 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3204), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RARS2]] | +0.73 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[UBOX5]] | +0.63 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[C1orf52]] | +0.62 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[YIPF5]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SRP54]] | +0.61 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[GDAP2]] | +0.61 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[ING4]] | +0.61 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[PMS2P4-1]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[ATP6V1E1]] | +0.60 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[TMCO1]] | +0.60 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[KDELR1]] | +0.60 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[COPA]] | +0.60 | +0.67 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRC2A]] | -0.58 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[SRSF2]] | -0.54 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[BAHCC1]] | -0.54 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[ADGRA3]] | -0.53 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[CENPB]] | -0.52 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[CDC42EP1]] | -0.51 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[SAYSD1]] | -0.51 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[TBL1XR1]] | -0.51 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[TIGD2]] | -0.51 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[COA7]] | -0.51 | -0.54 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.0, -17.2); signed map (-46.2, 5.7). **Vector** length 78.6, 27.3% of its response variance represented; |z| ≥ 3 in 689 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +1.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.8 | -1.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.1 | +0.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -2.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | -2.4 | +3.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | +0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | actin related protein 2/3 complex subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:110,434,823-110,450,422 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p21-Arc, ARC21 |
| Gene groups (HGNC) | Actin related protein 2/3 complex subunits |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 19 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; EPHB-mediated forward signaling; FCGR3A-mediated phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [O15145](https://www.uniprot.org/uniprotkb/O15145) (Actin-related protein 2/3 complex subunit 3):

> Component of the Arp2/3 complex, a multiprotein complex that mediates actin polymerization upon stimulation by nucleation-promoting factor (NPF). The Arp2/3 complex mediates the formation of branched actin networks in the cytoplasm, providing the force for cell motility. In addition to its role in the cytoplasmic cytoskeleton, the Arp2/3 complex also promotes actin polymerization in the nucleus, thereby regulating gene transcription and repair of damaged DNA. The Arp2/3 complex promotes …

**Summary**, from NCBI Gene [10094](https://www.ncbi.nlm.nih.gov/gene/10094):

> This gene encodes one of seven subunits of the human Arp2/3 protein complex. The Arp2/3 protein complex has been conserved through evolution and is implicated in the control of actin polymerization in cells. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Dec 2013]

**Accessions** — [HGNC:706](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:706) · Entrez [10094](https://www.ncbi.nlm.nih.gov/gene/10094) · UniProt [O15145](https://www.uniprot.org/uniprotkb/O15145) · Ensembl [ENSG00000111229](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111229)

## Data

Gene col 3204: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3204); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3204, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3204]; `tensor/DDL_lfc|DDL_z.npy` [3204]; `embed/gene_vectors.npy` [3204]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3204 or target_col == 3204). Every well: [[ARPC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARPC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
