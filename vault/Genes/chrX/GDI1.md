---
symbol: "GDI1"
type: "gene"
col: 12798
ensembl_id: "ENSG00000203879"
name: "GDP dissociation inhibitor 1"
location: "Xq28"
module: 2
arm: "+"
pooled_cpm: 67.85
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# GDI1

*GDP dissociation inhibitor 1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.81× (z +16.4, q 0e+00, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.45× (z +5.8, q 5e-07, up in 38 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.351×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FCHSD1]] (+0.70, fdr 7e-06), [[PLXNA3]] (+0.69, fdr 7e-06, ⚠ same locus), [[PPP1R12C]] (+0.69, fdr 7e-06), [[DLGAP4]] (+0.66, fdr 7e-06); moves opposite to [[SMAD1]] (-0.54, fdr 1e-04), [[SH2D4A]] (-0.53, fdr 8e-05), [[OSGEPL1]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12798.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.81×** | +16.4 | 0e+00 | 47/49 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +12.5 | 1e-33 | 40/43 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +7.8 | 1e-12 | 36/45 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +6.7 | 3e-09 | 40/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.49×** | +6.3 | 3e-08 | 32/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.45×** | +5.9 | 4e-07 | 33/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +5.8 | 5e-07 | 38/48 (A-427, LoVo, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.4 | 7e-04 | 27/47 (KATO III, C32, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.9 | 0.007 | 29/45 (RKO, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.29×** | +3.8 | 0.009 | 25/47 (LOX-IMVI, H4, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +3.6 | 0.014 | 26/48 (MIA PaCa-2, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.25×** | +3.5 | 0.024 | 23/48 (SW480, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.25×** | +3.5 | 0.024 | 20/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.027 | 25/48 (HT-29, SW48, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.22×** | +3.1 | 0.066 | 21/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.51×** | +3.1 | 0.073 | 12/48 (COLO 205, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12798.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.351×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.786× | -3.7 | 0.13 | 27/48 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.793× | -3.4 | 0.17 | 21/48 (HS-578T, NCI-H460, …) | inconsistent across doses |  |
| [[Adenosine (drug)]] 0.5 µM |  | 0.809× | -3.3 | 0.22 | 16/48 (SHP-77, LoVo, …) | inconsistent across doses | position effect removed |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.813× | -3.1 | 0.29 | 8/48 (LS 180, NCI-H2030, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12798. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 105 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +15.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 74.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.82× (z +9.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 107 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +17.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 141 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 64.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +10.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 54.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.38× (z +11.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 86.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 66.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +10.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 43.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +9.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 62.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.46× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 91.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +12.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 62.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +12.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 81.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 69.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.351× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 69.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +8.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 76.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 67.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 39.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +12.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 56.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +12.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 95.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +11.1) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 48.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 52.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +11.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 77.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +12.6) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 78.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 68.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 37.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +9.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 77.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 74.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 67.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 66.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12798), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHSD1]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[PLXNA3]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 | ⚠ same locus (14.8 kb, same strand: neighbours can correlate without regulation) |
| [[PPP1R12C]] | +0.69 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[DLGAP4]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[TMEM259]] | +0.65 | +0.57 / +0.61 | both halves | 8e-06 |  |
| [[GALNS]] | +0.65 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[LTBP4]] | +0.62 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[PLPPR2]] | +0.62 | +0.66 / +0.43 | both halves | 4e-05 |  |
| [[PLCB3]] | +0.62 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[F11R]] | +0.61 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[MFSD12]] | +0.61 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[GDPD5]] | +0.61 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[TCIRG1]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMAD1]] | -0.54 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[SH2D4A]] | -0.53 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[OSGEPL1]] | -0.52 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[TMA16]] | -0.52 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[QTRT2]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[SINHCAF]] | -0.50 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[PUM2]] | -0.50 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[DIS3L]] | -0.50 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[NUP35]] | -0.50 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[DUT]] | -0.50 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[FAM216A]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ZZZ3]] | -0.50 | -0.37 / -0.47 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.688). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (13.0, -2.9); signed map (-20.4, 24.8). **Vector** length 92.8, 26.9% of its response variance represented; |z| ≥ 3 in 656 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.9 | +2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.7 | +6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.1 | +3.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.9 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.3 | +2.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.0 | +3.1 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.9 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.3 | +0.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.8 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.6 | -1.5 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.2 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | GDP dissociation inhibitor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,436,913-154,443,467 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RABGDIA, XAP-4, OPHN2, FLJ41411; previously MRX48, MRX41, GDIL |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [P31150](https://www.uniprot.org/uniprotkb/P31150) (Rab GDP dissociation inhibitor alpha):

> Regulates the GDP/GTP exchange reaction of most Rab proteins by inhibiting the dissociation of GDP from them, and the subsequent binding of GTP to them. Promotes the dissociation of GDP-bound Rab proteins from the membrane and inhibits their activation. Promotes the dissociation of RAB1A, RAB3A, RAB5A and RAB10 from membranes.

**Summary**, from NCBI Gene [2664](https://www.ncbi.nlm.nih.gov/gene/2664):

> GDP dissociation inhibitors are proteins that regulate the GDP-GTP exchange reaction of members of the rab family, small GTP-binding proteins of the ras superfamily, that are involved in vesicular trafficking of molecules between cellular organelles. GDIs slow the rate of dissociation of GDP from rab proteins and release GDP from membrane-bound rabs. GDI1 is expressed primarily in neural and sensory tissues. Mutations in GDI1 have been linked to X-linked nonspecific cognitive disability. …

**Accessions** — [HGNC:4226](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4226) · Entrez [2664](https://www.ncbi.nlm.nih.gov/gene/2664) · UniProt [P31150](https://www.uniprot.org/uniprotkb/P31150) · Ensembl [ENSG00000203879](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203879)

## Data

Gene col 12798: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12798); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12798, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12798]; `tensor/DDL_lfc|DDL_z.npy` [12798]; `embed/gene_vectors.npy` [12798]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12798 or target_col == 12798). Every well: [[GDI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GDI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
