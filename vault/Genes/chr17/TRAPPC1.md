---
symbol: "TRAPPC1"
type: "gene"
col: 9898
ensembl_id: "ENSG00000170043"
name: "trafficking protein particle complex subunit 1"
location: "17p13.1"
module: 3
arm: "+"
pooled_cpm: 17.81
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# TRAPPC1

*trafficking protein particle complex subunit 1* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.14× (z +7.9, q 1e-12, up in 37 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 5.63×, A549 6.59×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 4.80×, A-427 6.14×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.294× (z -13.6, q 3e-39, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP1S1]] (+0.76, fdr 7e-06), [[GNB2]] (+0.73, fdr 7e-06), [[RRAS]] (+0.71, fdr 7e-06); moves opposite to [[GABPB2]] (-0.69, fdr 8e-05), [[KCNMB3]] (-0.66, fdr 7e-05), [[NEPRO-AS1]] (-0.65, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CPEB1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LAMTOR2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9898.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 5.63×, A549 6.59×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 4.80×, A-427 6.14×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.14×** | +7.9 | 1e-12 | 37/40 (PANC-1, A-427, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.82×** | +7.8 | 2e-12 | 23/29 (SW480, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.85×** | +4.2 | 0.005 | 22/34 (Panc 03.27, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.64×** | +3.9 | 0.016 | 29/48 (SW480, LS 180, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.6 | 0.036 | 21/41 (HT-29, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.58×** | +3.6 | 0.036 | 22/44 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | 1.33× | +3.2 | 0.13 | 17/48 (C32, NCI-H1792, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 1.48× | +3.1 | 0.15 | 16/48 (SW480, SNU-1, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.32× | +3.0 | 0.16 | 18/48 (Hs 766T, LOX-IMVI, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9898.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.294×** | -13.6 | 3e-39 | 46/47 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.363×** | -8.0 | 5e-13 | 40/46 (SW 900, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.458×** | -5.9 | 7e-07 | 34/47 (HS-578T, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.584×** | -4.0 | 0.009 | 29/48 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.376×** | -3.8 | 0.016 | 25/45 (H4, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.622×** | -3.7 | 0.017 | 25/48 (SW 900, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.646×** | -3.4 | 0.047 | 26/47 (AN3 CA, J82, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.663×** | -3.2 | 0.087 | 23/48 (BT-474, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.444×** | -3.2 | 0.095 | 18/37 (SW480, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9898. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 27.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -13.7) |
| [[HS-578T (line)]] | alt | 24.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.9) |
| [[A-172 (line)]] | wt | 32.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -19.2) |
| [[A498 (line)]] | wt | 33.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.2) |
| [[C32 (line)]] | wt | 16.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 14.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 12.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -12.9) |
| [[SW 900 (line)]] | alt | 30.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0866× (z -14.3) |
| [[A549 (line)]] | wt | 23.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.59× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[CFPAC-1 (line)]] | alt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.1) |
| [[H4 (line)]] | wt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 18.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -10.7) |
| [[HOP62 (line)]] | alt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -12.2) |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -12.2) |
| [[J82 (line)]] | alt | 23.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -13.5) |
| [[KATO III (line)]] | alt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 7.83 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0948× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H2030 (line)]] | alt | 34.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -16.1) |
| [[NCI-H23 (line)]] | alt | 27.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -9.0) |
| [[PANC-1 (line)]] | alt | 17.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RKO (line)]] | wt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -13.9) |
| [[RPMI-7951 (line)]] | alt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -9.2) |
| [[SW480 (line)]] | alt | 18.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.63× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[AN3 CA (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9898), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP1S1]] | +0.76 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[GNB2]] | +0.73 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[RRAS]] | +0.71 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.69 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[YIF1B]] | +0.69 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[RTL8C]] | +0.69 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[TUSC2]] | +0.68 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[IGSF8]] | +0.67 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[AP2S1]] | +0.67 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[VKORC1]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[NOMO1]] | +0.66 | +0.69 / +0.33 | both halves | 1e-04 |  |
| [[ZDHHC12]] | +0.66 | +0.58 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABPB2]] | -0.69 | -0.70 / -0.37 | both halves | 8e-05 |  |
| [[KCNMB3]] | -0.66 | -0.72 / -0.38 | both halves | 7e-05 |  |
| [[NEPRO-AS1]] | -0.65 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[ZXDA]] | -0.64 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[FKRP]] | -0.62 | -0.59 / -0.36 | both halves | 9e-05 |  |
| [[ZCWPW1]] | -0.62 | -0.66 / -0.20 | ⚠ one half (not replicated) | 7e-04 |  |
| [[ST7L]] | -0.61 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[TIA1]] | -0.61 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[HNRNPU]] | -0.60 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[FBXO4]] | -0.60 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[GALNT7-DT]] | -0.59 | -0.58 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[ANKRD18A]] | -0.59 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[LEKR1]] | -0.59 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[IQCH-AS1]] | -0.59 | -0.61 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CPEB1]] | B | CPEB1 activity raises TRAPPC1's level | lines that do not express CPEB1 (24) vs lines expressing it (26) | 1.47× lower at baseline in the lines without CPEB1 | 0.032 | ⚠ within organs, on part of the lines; also absent: GLIS1, COLEC12, TUB |
| [[PSMB5]] | B | PSMB5 activity raises TRAPPC1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMTOR2]] | C | TRAPPC1's natural level strengthens LAMTOR2's drug response | TRAPPC1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.23; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (2.6, -14.2); signed map (-36.0, 13.6). **Vector** length 71.6, 18.3% of its response variance represented; |z| ≥ 3 in 674 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.8 | +3.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +3.3 | +3.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.0 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.1 | +2.9 |
|  | [[vincristine (drug)]] 0.05 µM |  | +1.1 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.7 | -13.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -8.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.0 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -0.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.6 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | trafficking protein particle complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,930,345-7,932,123 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MUM2, BET5 |
| Gene groups (HGNC) | Trafficking protein particle complex subunits |
| Reactome | 10 pathways, smallest: COPII-mediated vesicle transport; RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5R8](https://www.uniprot.org/uniprotkb/Q9Y5R8) (Trafficking protein particle complex subunit 1):

> May play a role in vesicular transport from endoplasmic reticulum to Golgi.

**Summary**, from NCBI Gene [58485](https://www.ncbi.nlm.nih.gov/gene/58485):

> This gene product plays a role in vesicular transport of proteins to the Golgi apparatus from the endoplasmic reticulum. The encoded protein is a component of the multisubunit transport protein particle (TRAPP) complex. Alternative splicing results in multiple transcript variants.[provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:19894](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19894) · Entrez [58485](https://www.ncbi.nlm.nih.gov/gene/58485) · UniProt [Q9Y5R8](https://www.uniprot.org/uniprotkb/Q9Y5R8) · Ensembl [ENSG00000170043](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170043)

## Data

Gene col 9898: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9898); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9898, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9898]; `tensor/DDL_lfc|DDL_z.npy` [9898]; `embed/gene_vectors.npy` [9898]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9898 or target_col == 9898). Every well: [[TRAPPC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAPPC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
