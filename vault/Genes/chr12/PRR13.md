---
symbol: "PRR13"
type: "gene"
col: 12970
ensembl_id: "ENSG00000205352"
name: "proline rich 13"
location: "12q13.13"
module: 72
arm: "+"
pooled_cpm: 49.05
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# PRR13

*proline rich 13* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.30× (z +13.3, q 9e-38, up in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +8.7, q 9e-16, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.450× (z -4.3, q 0.009, down in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2347 0.378×, Panc 03.27 0.349×, KATO III 0.468×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.176×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD8]] (+0.61, fdr 8e-06), [[EMC4]] (+0.56, fdr 1e-05), [[PSMB4]] (+0.54, fdr 2e-05); moves opposite to [[TERT]] (-0.52, fdr 4e-05), [[TARBP1]] (-0.48, fdr 4e-05), [[ASB13]] (-0.47, fdr 3e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12970.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.30×** | +13.3 | 9e-38 | 43/44 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.88×** | +11.4 | 2e-27 | 34/37 (A549, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +8.7 | 9e-16 | 41/47 (KATO III, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +6.7 | 4e-09 | 33/40 (NCI-H2030, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.69×** | +5.9 | 5e-07 | 38/48 (A-427, HOP62, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.62×** | +5.4 | 6e-06 | 31/46 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +5.3 | 1e-05 | 34/48 (A-427, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +4.9 | 6e-05 | 35/47 (A-427, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.51×** | +4.6 | 3e-04 | 28/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.4 | 5e-04 | 32/48 (KATO III, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.2 | 0.001 | 28/47 (LOX-IMVI, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +4.1 | 0.002 | 27/48 (A-427, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +3.4 | 0.034 | 22/48 (NCI-H2030, PANC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.3 | 0.034 | 23/46 (A-427, J82, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.35×** | +3.3 | 0.034 | 22/48 (LOX-IMVI, SW480, …) | rises with dose | position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.080 | 18/47 (A498, SNU-423, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12970.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2347 0.378×, Panc 03.27 0.349×, KATO III 0.468×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.176×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.450×** | -4.3 | 0.009 | 28/47 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.778×** | -4.0 | 0.022 | 21/47 (NCI-H2347, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.749× | -3.2 | 0.18 | 23/47 (LoVo, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.754× | -3.2 | 0.18 | 19/48 (Panc 03.27, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.820× | -3.1 | 0.18 | 21/48 (A-427, NCI-H2347, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.757× | -3.1 | 0.18 | 20/48 (C-33 A, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.919× | -3.0 | 0.19 | 5/48 (CFPAC-1, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12970. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 101 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 36.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +8.5) | — |
| [[A498 (line)]] | wt | 94.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +11.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 63.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.77× (z +11.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 70.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.01× (z +10.7) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 38.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +10.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 32.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.80× (z +9.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 45.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 68.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +12.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 49.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.54× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 34.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +12.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 97.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 23.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 92.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.96× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 19.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +8.7) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 32.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.38× (z +9.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 40.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 69.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 46.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 55.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -11.3) |
| [[RKO (line)]] | wt | 27.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.176× (z -9.2) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 55.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 42.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.45× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 49.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +11.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12970), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD8]] | +0.61 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[EMC4]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PSMB4]] | +0.54 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[CHMP5]] | +0.54 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[ATP6V1E1]] | +0.53 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[TOX4]] | +0.53 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[UBE2H]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[VIPAS39]] | +0.52 | +0.51 / +0.38 | both halves | 7e-05 |  |
| [[ATP6V1G1]] | +0.51 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[EXOC7]] | +0.51 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[MRPL18]] | +0.50 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[TINF2]] | +0.50 | +0.46 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERT]] | -0.52 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[TARBP1]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ASB13]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ADRA1B]] | -0.46 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[DPY19L2P1]] | -0.44 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[KIF18B]] | -0.44 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[UBA2]] | -0.44 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[DHRS4L2]] | -0.44 | -0.26 / -0.45 | both halves | 4e-04 |  |
| [[DDX11-AS1]] | -0.44 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[TRIM28]] | -0.43 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[SAPCD1]] | -0.43 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[HNRNPD]] | -0.43 | -0.39 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | PRR13's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | PRR13's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.60 | 0.472 over the table, 0.064 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.499). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.9, -47.3); signed map (-23.9, -25.6). **Vector** length 73.6, 19.2% of its response variance represented; |z| ≥ 3 in 727 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.8 | +5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.4 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.3 | +4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +3.2 | +3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +5.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +0.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.4 | -4.0 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -2.7 | -1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.6 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.6 | +3.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.4 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | -0.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.0 | -0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | proline rich 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,441,678-53,446,645 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23818, DKFZP564J157 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZ81](https://www.uniprot.org/uniprotkb/Q9NZ81) (Proline-rich protein 13):

> Negatively regulates TSP1 expression at the level of transcription. This down-regulation was shown to reduce taxane-induced apoptosis.

**Summary**, from NCBI Gene [54458](https://www.ncbi.nlm.nih.gov/gene/54458):

> Predicted to be involved in DNA-templated transcription. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24528](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24528) · Entrez [54458](https://www.ncbi.nlm.nih.gov/gene/54458) · UniProt [Q9NZ81](https://www.uniprot.org/uniprotkb/Q9NZ81) · Ensembl [ENSG00000205352](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205352)

## Data

Gene col 12970: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12970); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12970, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12970]; `tensor/DDL_lfc|DDL_z.npy` [12970]; `embed/gene_vectors.npy` [12970]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12970 or target_col == 12970). Every well: [[PRR13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRR13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
