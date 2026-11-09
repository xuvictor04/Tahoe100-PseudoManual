---
symbol: "BRK1"
type: "gene"
col: 14908
ensembl_id: "ENSG00000254999"
name: "BRICK1 subunit of SCAR/WAVE actin nucleating complex"
location: "3p25.3"
module: 105
arm: "+"
pooled_cpm: 43.83
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 4
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# BRK1

*BRICK1 subunit of SCAR/WAVE actin nucleating complex* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.37× (z +11.1, q 6e-26, up in 42 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.70× (z +6.8, q 2e-09, up in 41 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (HEC-1-A 2.81×, PANC-1 3.00×, A549 3.44×, HOP62 2.72×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (HOP62 3.49×, SW480 3.22×, PANC-1 2.69×, NCI-H1792 3.12×; ⚠ cell-cycle shift, explains ~65% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 2.94×, A498 3.33×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.534× (z -11.5, q 8e-28, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDK3]] (+0.68, fdr 1e-05), [[HDAC3]] (+0.67, fdr 1e-05), [[FAM210A]] (+0.65, fdr 1e-05); moves opposite to [[GABPB2]] (-0.65, fdr 1e-05), [[FIZ1]] (-0.64, fdr 1e-04), [[NME6]] (-0.62, fdr 1e-04).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14908.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (HEC-1-A 2.81×, PANC-1 3.00×, A549 3.44×, HOP62 2.72×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (HOP62 3.49×, SW480 3.22×, PANC-1 2.69×, NCI-H1792 3.12×; ⚠ cell-cycle shift, explains ~65% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 2.94×, A498 3.33×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.37×** | +11.1 | 6e-26 | 42/47 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.93×** | +8.1 | 1e-13 | 35/40 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +6.8 | 2e-09 | 41/48 (SNU-1, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.57×** | +5.4 | 1e-05 | 37/44 (HOP62, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.50×** | +5.2 | 2e-05 | 32/48 (HOP62, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.44×** | +4.7 | 2e-04 | 34/47 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **1.34×** | +3.7 | 0.015 | 27/46 (KATO III, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.33×** | +3.7 | 0.015 | 27/48 (NCI-H23, COLO 205, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.7 | 0.015 | 26/47 (CFPAC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.47×** | +3.6 | 0.021 | 27/47 (MIA PaCa-2, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.29×** | +3.2 | 0.062 | 22/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14908.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.534×** | -11.5 | 8e-28 | 43/47 (A-427, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.672×** | -5.2 | 6e-05 | 34/47 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.468×** | -5.1 | 6e-05 | 42/48 (RPMI-7951, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.748×** | -3.8 | 0.024 | 30/48 (NCI-H2030, HCT15, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.746× | -3.3 | 0.12 | 21/48 (C32, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.780× | -3.2 | 0.12 | 22/48 (C-33 A, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14908. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 64.1 | 3 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.49× (z +11.7) ⚠ cell-cycle shift, explains ~65% of this change | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -9.1) |
| [[PANC-1 (line)]] | alt | 32.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 63.3 | 2 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +9.1) ⚠ cell-cycle shift, explains ~65% of this change | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -12.2) |
| [[SW480 (line)]] | alt | 37.9 | 2 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +11.6) ⚠ cell-cycle shift, explains ~65% of this change | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -8.9) |
| [[A498 (line)]] | wt | 22.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.33× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[C-33 A (line)]] | alt | 67.6 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0724× (z -19.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.366× (z -11.1) |
| [[LoVo (line)]] | wt | 28.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 51.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -12.6) |
| [[A-427 (line)]] | wt | 38.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -17.9) |
| [[A549 (line)]] | wt | 53.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[AN3 CA (line)]] | alt | 28.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.105× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 31.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -13.5) |
| [[CHP-212 (line)]] | wt | 41.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.133× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 43.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 75.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[Hs 766T (line)]] | wt | 53.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[J82 (line)]] | alt | 59.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 46.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 32.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H460 (line)]] | wt | 32.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[Panc 03.27 (line)]] | alt | 34.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -10.2) |
| [[RKO (line)]] | wt | 53.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 83.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -11.5) |
| [[SNU-1 (line)]] | wt | 40.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -11.9) |
| [[SNU-423 (line)]] | alt | 49.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SW 900 (line)]] | alt | 42.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -8.7) |
| [[A-172 (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14908), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDK3]] | +0.68 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.67 | +0.74 / +0.49 | both halves | 1e-05 |  |
| [[FAM210A]] | +0.65 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[TMED4]] | +0.64 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[ALDOA]] | +0.64 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[PGK1]] | +0.63 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[PLEKHA8]] | +0.63 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[HERC3]] | +0.62 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[AK2]] | +0.62 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[BTAF1]] | +0.61 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[ATRN]] | +0.60 | +0.66 / +0.40 | both halves | 4e-05 |  |
| [[FAM162A]] | +0.60 | +0.72 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABPB2]] | -0.65 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[FIZ1]] | -0.64 | -0.74 / -0.35 | both halves | 1e-04 |  |
| [[NME6]] | -0.62 | -0.68 / -0.36 | both halves | 1e-04 |  |
| [[SRSF8]] | -0.60 | -0.65 / -0.38 | both halves | 7e-05 |  |
| [[CCT6P3]] | -0.59 | -0.63 / -0.36 | both halves | 1e-04 |  |
| [[CCDC102A]] | -0.59 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[PPP3CB-AS1]] | -0.58 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[CCAR1]] | -0.58 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[NAIF1]] | -0.58 | -0.66 / -0.28 | both halves | 3e-04 |  |
| [[YJU2]] | -0.57 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[FNBP4]] | -0.57 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[MEPCE]] | -0.57 | -0.62 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.640). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.5, -17.1); signed map (-39.1, 24.6). **Vector** length 92.7, 25.0% of its response variance represented; |z| ≥ 3 in 726 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.2 | +6.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.1 | +2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +3.6 | +3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +3.4 | +5.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +1.2 |
|  | [[Relugolix (drug)]] 0.5 µM |  | +1.7 | +0.3 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +1.7 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.0 | -11.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.4 | -5.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -3.7 | -0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -5.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.2 | +0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | BRICK1 subunit of SCAR/WAVE actin nucleating complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:10,115,675-10,127,190 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MDS027, HSPC300; previously C3orf10 |
| Gene groups (HGNC) | SCAR/WAVE complex |
| Reactome | 19 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; FCGR3A-mediated phagocytosis; Leishmania phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUW1](https://www.uniprot.org/uniprotkb/Q8WUW1) (Protein BRICK1):

> Involved in regulation of actin and microtubule organization. Part of a WAVE complex that activates the Arp2/3 complex. As component of the WAVE1 complex, required for BDNF-NTRK2 endocytic trafficking and signaling from early endosomes (By similarity).

**Summary**, from NCBI Gene [55845](https://www.ncbi.nlm.nih.gov/gene/55845):

> Enables identical protein binding activity. Contributes to small GTPase binding activity. Involved in Rac protein signal transduction and positive regulation of cellular component organization. Located in extracellular exosome. Part of SCAR complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23057](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23057) · Entrez [55845](https://www.ncbi.nlm.nih.gov/gene/55845) · UniProt [Q8WUW1](https://www.uniprot.org/uniprotkb/Q8WUW1) · Ensembl [ENSG00000254999](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254999)

## Data

Gene col 14908: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14908); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14908, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14908]; `tensor/DDL_lfc|DDL_z.npy` [14908]; `embed/gene_vectors.npy` [14908]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14908 or target_col == 14908). Every well: [[BRK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
