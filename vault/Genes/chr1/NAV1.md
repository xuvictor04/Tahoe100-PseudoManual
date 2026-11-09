---
symbol: "NAV1"
type: "gene"
col: 5555
ensembl_id: "ENSG00000134369"
name: "neuron navigator 1"
location: "1q32.1"
module: 13
arm: "+"
pooled_cpm: 238.3
n_lines_expressing: 28
n_dd_up: 2
n_dd_down: 37
n_dd_up_clean: 1
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 62
direction_downstream: 46
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# NAV1

*neuron navigator 1* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.25× (z +3.9, q 0.058, up in 8 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.26×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 3.09×); [[Mebendazole (drug)]] 5 µM in 1 line (MIA PaCa-2 2.86×).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.421× (z -21.9, q 0e+00, down in 25 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APCDD1L]] (+0.78, fdr 7e-06), [[COL5A1]] (+0.73, fdr 7e-06), [[LOXL2]] (+0.71, fdr 7e-06); moves opposite to [[MIR3936HG]] (-0.55, fdr 1e-05), [[DLEU1]] (-0.51, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 62 arrows point to it, the strongest [[THBS2]] → it (grade B ⚠); 46 go from it, the strongest it → [[IPO9-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5555.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.26×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 3.09×); [[Mebendazole (drug)]] 5 µM in 1 line (MIA PaCa-2 2.86×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.058 | 8/25 (NCI-H2347, A549, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.23×** | +3.6 | 0.079 | 19/25 (C32, J82, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.22× | +3.4 | 0.11 | 17/25 (SW480, RPMI-7951, …) | rises with dose | low cells (technical?) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.20× | +3.3 | 0.11 | 8/26 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.20× | +3.3 | 0.11 | 5/27 (SW1417, A498, …) | two highest doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.18 | 10/27 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.20 | 9/26 (NCI-H1792, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5555.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.421×** | -21.9 | 0e+00 | 25/26 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.347×** | -18.2 | 0e+00 | 25/26 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.398×** | -16.5 | 0e+00 | 26/26 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.466×** | -13.6 | 3e-40 | 26/26 (HOP62, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.472×** | -13.4 | 4e-39 | 22/26 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.495×** | -12.6 | 2e-34 | 20/26 (SHP-77, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.498×** | -12.5 | 9e-34 | 25/26 (HOP62, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.553×** | -10.6 | 2e-24 | 26/26 (HOP62, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.546×** | -10.2 | 2e-22 | 23/26 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.345×** | -10.0 | 1e-21 | 24/27 (HOP62, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.595×** | -9.3 | 8e-19 | 20/26 (SHP-77, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.593×** | -9.0 | 1e-17 | 24/25 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.618×** | -8.6 | 4e-16 | 18/26 (SHP-77, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.616×** | -8.3 | 4e-15 | 22/26 (HOP62, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.617×** | -8.0 | 5e-14 | 21/23 (HOP62, A-172, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.443×** | -7.6 | 1e-12 | 20/26 (LOX-IMVI, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.727×** | -5.7 | 3e-07 | 18/26 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.729×** | -5.6 | 4e-07 | 18/26 (SHP-77, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.801×** | -5.6 | 5e-07 | 18/26 (C32, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.738×** | -5.4 | 1e-06 | 22/26 (A-172, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.718×** | -5.4 | 1e-06 | 14/26 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.754×** | -5.0 | 9e-06 | 18/26 (LOX-IMVI, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5555. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 1,008 | 0 | 30 (15 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0795× (z -33.9) |
| [[LOX-IMVI (line)]] | wt | 675 | 0 | 28 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0721× (z -33.4) |
| [[J82 (line)]] | alt | 388 | 0 | 24 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -24.5) |
| [[H4 (line)]] | wt | 529 | 0 | 23 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0502× (z -35.8) |
| [[hTERT-HPNE (line)]] | wt | 1,211 | 0 | 23 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0590× (z -29.7) |
| [[A-172 (line)]] | wt | 1,629 | 0 | 21 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0952× (z -34.5) |
| [[HS-578T (line)]] | alt | 650 | 0 | 20 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -24.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.149× (z -21.9) |
| [[C32 (line)]] | wt | 662 | 1 | 17 (10 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.38× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -34.4) |
| [[SHP-77 (line)]] | alt | 299 | 0 | 16 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -22.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.330× (z -16.4) |
| [[RPMI-7951 (line)]] | alt | 693 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -30.8) |
| [[SW480 (line)]] | alt | 105 | 1 | 13 (6 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 1.84× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.177× (z -25.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.328× (z -23.5) |
| [[NCI-H1792 (line)]] | alt | 311 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -25.1) |
| [[SNU-423 (line)]] | alt | 514 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -22.0) |
| [[MIA PaCa-2 (line)]] | alt | 130 | 3 | 6 (4 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.26× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -23.4) |
| [[PANC-1 (line)]] | alt | 126 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -23.3) |
| [[SW 900 (line)]] | alt | 238 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -23.2) |
| [[A498 (line)]] | wt | 198 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -15.5) |
| [[COLO 205 (line)]] | alt | 159 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -18.1) |
| [[SK-MEL-2 (line)]] | alt | 247 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -30.1) |
| [[SW 1088 (line)]] | alt | 548 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -14.7) |
| [[CFPAC-1 (line)]] | alt | 138 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.444× (z -11.1) |
| [[A549 (line)]] | wt | 67.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 88.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -10.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.393× (z -8.6) |
| [[SW1417 (line)]] | alt | 60.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -16.6) |
| [[AN3 CA (line)]] | alt | 185 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.290× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[SW 1271 (line)]] | alt | 66.6 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0804× (z -8.5) ⚠ toxic; unreliable plate only |
| [[A-427 (line)]] | wt | 54.4 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 30.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 29.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 32.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 50.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 42.3 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 54.7 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 21.2 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 22.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 24.1 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 21.3 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 58.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 43.8 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 26.7 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 42.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.7 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 42.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.3 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 58.1 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 37.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 26.0 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 36.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5555), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APCDD1L]] | +0.78 | +0.74 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[COL5A1]] | +0.73 | +0.74 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[LOXL2]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[DENND2A]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[LINC01615]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[CSPG4]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[INSYN2B]] | +0.68 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[TSHZ3]] | +0.67 | +0.66 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS14]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[ITGA11]] | +0.66 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[KCNK3]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[ADAM12]] | +0.66 | +0.62 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR3936HG]] | -0.55 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[DLEU1]] | -0.51 | -0.54 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*62 arrows, 62 of them with an alert ⚠; grade A 0, B 10, C 52. Shown: the 12 strongest; 50 more arrows (50 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THBS2]] | B | THBS2 activity raises NAV1's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 3.55× lower at baseline in the lines without THBS2 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4 |
| [[GPR173]] | B | GPR173 activity raises NAV1's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 3.25× lower at baseline in the lines without GPR173 | 0.046 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2 |
| [[MTSS1]] | B | MTSS1 activity raises NAV1's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 1.93× lower at baseline in the lines without MTSS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[ZNF439]] | B | ZNF439 activity raises NAV1's level | lines that do not express ZNF439 (21) vs lines expressing it (29) | 2.68× lower at baseline in the lines without ZNF439 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000267383, PPP2R2B, CSF1R |
| [[PRRX1]] | B | PRRX1 activity raises NAV1's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 3.03× lower at baseline in the lines without PRRX1 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN |
| [[PATJ]] | B | PATJ activity lowers NAV1's level | lines that do not express PATJ (9) vs lines expressing it (41) | 4.83× higher at baseline in the lines without PATJ | 0.076 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent |
| [[NOXA1]] | B | NOXA1 activity lowers NAV1's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 7.50× higher at baseline in the lines without NOXA1 | 0.079 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[LINC02985]] | B | LINC02985 activity raises NAV1's level | lines that do not express LINC02985 (15) vs lines expressing it (35) | 2.50× lower at baseline in the lines without LINC02985 | 0.081 | ⚠ within organs, on part of the lines; also absent: GXYLT2 |
| [[DENND2A]] | B | DENND2A activity raises NAV1's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 3.39× lower at baseline in the lines without DENND2A | 0.085 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[CA12]] | B | CA12 activity raises NAV1's level | lines that do not express CA12 (29) vs lines expressing it (21) | 2.70× lower at baseline in the lines without CA12 | 0.087 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1 |
| [[ITGA11]] | C | ITGA11 activity raises NAV1's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 5.88× lower at baseline in the lines without ITGA11 | 0.002 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[TMEM200A]] | C | TMEM200A activity raises NAV1's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 3.42× lower at baseline in the lines without TMEM200A | 0.004 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615; co-absent with the target |

### Downstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 10, C 36. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IPO9-AS1]] | B | NAV1 activity raises IPO9-AS1's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 1.78× lower at baseline in the lines without NAV1 | 0.003 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent |
| [[ADAM19]] | B | NAV1 activity raises ADAM19's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 3.26× lower at baseline in the lines without NAV1 | 0.012 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent |
| [[NRSN2]] | B | NAV1 activity raises NRSN2's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 2.03× lower at baseline in the lines without NAV1 | 0.019 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent |
| [[FAM167A]] | B | NAV1 activity raises FAM167A's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 2.15× lower at baseline in the lines without NAV1 | 0.036 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent |
| [[ZNF439]] | B | NAV1 activity raises ZNF439's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 2.57× lower at baseline in the lines without NAV1 | 0.044 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent |
| [[SH2B3]] | B | NAV1 activity raises SH2B3's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 2.44× lower at baseline in the lines without NAV1 | 0.062 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent |
| [[LHFPL2]] | B | NAV1 activity raises LHFPL2's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 1.87× lower at baseline in the lines without NAV1 | 0.069 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent |
| [[MYO10]] | B | NAV1 activity raises MYO10's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 1.99× lower at baseline in the lines without NAV1 | 0.091 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent |
| [[RHBDF2]] | B | NAV1 activity strengthens RHBDF2's drug response | lines that do not express NAV1 (20) vs lines expressing it (23) | the lines without NAV1 respond 0.52× as strongly (z diff +3.23); strongest at Idarubicin (hydrochloride) 5 µM: 0.72x vs 0.39x (z diff +5.1) | 0.095 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ZCCHC24]] | B | NAV1 activity raises ZCCHC24's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 1.97× lower at baseline in the lines without NAV1 | 0.095 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent |
| [[MANCR]] | C | NAV1 activity raises MANCR's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 3.10× lower at baseline in the lines without NAV1 | 0.007 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent; co-absent with the target |
| [[INSYN2B]] | C | NAV1 activity raises INSYN2B's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 4.04× lower at baseline in the lines without NAV1 | 0.008 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.830). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.5, 17.4); signed map (24.8, 47.2). **Vector** length 124, 46.3% of its response variance represented; |z| ≥ 3 in 1,233 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *epithelial mesenchymal transition* (hallmark, mean cos +0.50 to 29); *Extracellular matrix organization* (reactome, mean cos +0.52 to 22); *Collagen formation* (reactome, mean cos +0.53 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.0 | -6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | +4.4 | -7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | +3.9 | -6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +3.4 | -8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | -21.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | -5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Thymol (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[Flutamide (drug)]] 5 µM |  | +1.7 | +2.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.4 | -5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -10.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.9 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -0.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.8 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | neuron navigator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:201,539,127-201,826,969 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12560, FLJ14203, KIAA1151, MGC14961, POMFIL3, steerin-1, DKFZp781D0314 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEY1](https://www.uniprot.org/uniprotkb/Q8NEY1) (Neuron navigator 1):

> May be involved in neuronal migration.

**Summary**, from NCBI Gene [89796](https://www.ncbi.nlm.nih.gov/gene/89796):

> This gene belongs to the neuron navigator family and is expressed predominantly in the nervous system. The encoded protein contains coiled-coil domains and a conserved AAA domain characteristic for ATPases associated with a variety of cellular activities. This gene is similar to unc-53, a Caenorhabditis elegans gene involved in axon guidance. The exact function of this gene is not known, but it is thought to play a role in in neuronal development and regeneration. Alternative splicing results …

**Accessions** — [HGNC:15989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15989) · Entrez [89796](https://www.ncbi.nlm.nih.gov/gene/89796) · UniProt [Q8NEY1](https://www.uniprot.org/uniprotkb/Q8NEY1) · Ensembl [ENSG00000134369](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134369)

## Data

Gene col 5555: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5555); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5555, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5555]; `tensor/DDL_lfc|DDL_z.npy` [5555]; `embed/gene_vectors.npy` [5555]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5555 or target_col == 5555). Every well: [[NAV1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAV1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
