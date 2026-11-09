---
symbol: "NDFIP1"
type: "gene"
col: 5221
ensembl_id: "ENSG00000131507"
name: "Nedd4 family interacting protein 1"
location: "5q31.3"
module: 188
arm: "+"
pooled_cpm: 118.42
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/188"]
generated_by: "tahoemap"
---

# NDFIP1

*Nedd4 family interacting protein 1* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.28× (z +7.4, q 7e-11, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.801× (z -6.7, q 2e-08, down in 26 of 49 measured lines) ⚠ cell-cycle shift, explains ~19% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.783× (z -5.2, q 6e-05, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (LOX-IMVI 0.479×, SK-MEL-2 0.578×, LoVo 0.626×, HOP62 0.583×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (RKO 0.399×, LoVo 0.577×, AsPC-1 0.626×, NCI-H2347 0.603×; ⚠ cell-cycle shift, explains ~19% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (AN3 CA 0.305×, NCI-H1573 0.430×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dexmedetomidine (drug)]] 0.05 µM in 1 line (SW 1088 0.0587×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX4]] (+0.69, fdr 7e-06), [[MRS2]] (+0.68, fdr 7e-06), [[MINDY3]] (+0.68, fdr 7e-06); moves opposite to [[RBBP6]] (-0.63, fdr 7e-06), [[SON]] (-0.60, fdr 1e-05), [[ZNF335]] (-0.59, fdr 2e-05).
> It is in [[Module 188]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZDHHC11]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5221.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +7.4 | 7e-11 | 30/48 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +5.8 | 2e-06 | 33/48 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.30×** | +5.4 | 1e-05 | 28/49 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.28×** | +5.2 | 2e-05 | 29/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +5.0 | 7e-05 | 28/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +4.7 | 2e-04 | 22/49 (SW1417, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.24×** | +4.6 | 4e-04 | 26/48 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.8 | 0.009 | 21/48 (SW480, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.012 | 22/49 (NCI-H460, HCT15, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.20×** | +3.7 | 0.013 | 22/47 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.6 | 0.017 | 21/48 (RKO, SW480, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.024 | 20/48 (HEC-1-A, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.17× | +3.3 | 0.037 | 18/48 (HT-29, HepG2/C3A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.0 | 0.098 | 18/48 (HT-29, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5221.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (LOX-IMVI 0.479×, SK-MEL-2 0.578×, LoVo 0.626×, HOP62 0.583×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (RKO 0.399×, LoVo 0.577×, AsPC-1 0.626×, NCI-H2347 0.603×; ⚠ cell-cycle shift, explains ~19% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (AN3 CA 0.305×, NCI-H1573 0.430×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dexmedetomidine (drug)]] 0.05 µM in 1 line (SW 1088 0.0587×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.801×** | -6.7 | 2e-08 | 26/49 (RKO, LoVo, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.783×** | -5.2 | 6e-05 | 27/48 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.849× | -4.9 | 2e-04 | 22/48 (A-172, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.805×** | -4.6 | 6e-04 | 25/48 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.833×** | -3.9 | 0.011 | 17/48 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.860× | -3.1 | 0.19 | 18/48 (J82, HOP62, …) | top dose only | position effect removed |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.862× | -3.0 | 0.19 | 5/48 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5221. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 97.2 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +12.2) | — |
| [[AsPC-1 (line)]] | alt | 201 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -10.1) ⚠ cell-cycle shift, explains ~19% of this change |
| [[LoVo (line)]] | wt | 146 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -10.8) ⚠ cell-cycle shift, explains ~19% of this change |
| [[NCI-H1573 (line)]] | alt | 145 | 1 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.82× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.430× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 87.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.12× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[PANC-1 (line)]] | alt | 80.9 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.16× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +10.1) | — |
| [[RKO (line)]] | wt | 119 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -16.5) ⚠ cell-cycle shift, explains ~19% of this change |
| [[SW480 (line)]] | alt | 100 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 202 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 81.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.168× (z -10.3) ⚠ toxic |
| [[HCT15 (line)]] | alt | 80.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[HOP62 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.583× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 72.0 | 1 | 0 | [[Selinexor (drug)]] 5 µM 1.94× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 78.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 249 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -9.6) ⚠ cell-cycle shift, explains ~19% of this change |
| [[SK-MEL-2 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.578× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 128 | 0 | 1 | — | [[Dexmedetomidine (drug)]] 0.05 µM 0.0587× (z -11.9) |
| [[SW1417 (line)]] | alt | 230 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 83.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 76.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 166 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 74.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 158 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 149 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 84.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 99.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5221), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX4]] | +0.69 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[MRS2]] | +0.68 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.68 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[STX7]] | +0.66 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[GCSH]] | +0.66 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[GNPTAB]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[TMEM185A]] | +0.62 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[ATP5F1C]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[LTA4H]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[MBD2]] | +0.60 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[CDS2]] | +0.60 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[RTCA]] | +0.60 | +0.70 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP6]] | -0.63 | -0.70 / -0.60 | both halves | 7e-06 |  |
| [[SON]] | -0.60 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[ZNF335]] | -0.59 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[PPP1R10]] | -0.58 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[ARMC5]] | -0.57 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[KCNJ14]] | -0.56 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[PPIEL-1]] | -0.55 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[DNAH1]] | -0.55 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[MPDU1]] | -0.55 | -0.68 / -0.46 | both halves | 3e-05 |  |
| [[THUMPD3-AS1]] | -0.53 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[NLGN3]] | -0.53 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[IDI2-AS1]] | -0.53 | -0.55 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZDHHC11]] | C | ZDHHC11 activity lowers NDFIP1's level | lines that do not express ZDHHC11 (4) vs lines expressing it (46) | 1.33× higher at baseline in the lines without ZDHHC11 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[TRIM72]] | C | TRIM72 activity lowers NDFIP1's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.56× higher at baseline in the lines without TRIM72 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 188]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.7, -9.7); signed map (-32.6, -13.5). **Vector** length 110, 29.9% of its response variance represented; |z| ≥ 3 in 836 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.3 | +7.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.5 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.4 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.0 | +2.5 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +3.9 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +1.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.2 | +3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.3 | -5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -3.3 | -6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.5 | -0.9 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -2.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | Nedd4 family interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:142,108,779-142,154,440 (+) |
| Ensembl biotype | protein_coding |
| Also known as | N4WBP5, MGC10924 |
| Gene groups (HGNC) | NDFIP family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BT67](https://www.uniprot.org/uniprotkb/Q9BT67) (NEDD4 family-interacting protein 1):

> Activates HECT domain-containing E3 ubiquitin-protein ligases, including NEDD4 and ITCH, and consequently modulates the stability of their targets. As a result, controls many cellular processes. Prevents chronic T-helper cell-mediated inflammation by activating ITCH and thus controlling JUNB degradation (By similarity). Promotes pancreatic beta cell death through degradation of JUNB and inhibition of the unfolded protein response, leading to reduction of insulin secretion. Restricts the …

**Summary**, from NCBI Gene [80762](https://www.ncbi.nlm.nih.gov/gene/80762):

> The protein encoded by this gene belongs to a small group of evolutionarily conserved proteins with three transmembrane domains. It is a potential target for ubiquitination by the Nedd4 family of proteins. This protein is thought to be part of a family of integral Golgi membrane proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17592](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17592) · Entrez [80762](https://www.ncbi.nlm.nih.gov/gene/80762) · UniProt [Q9BT67](https://www.uniprot.org/uniprotkb/Q9BT67) · Ensembl [ENSG00000131507](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131507)

## Data

Gene col 5221: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5221); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5221, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5221]; `tensor/DDL_lfc|DDL_z.npy` [5221]; `embed/gene_vectors.npy` [5221]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5221 or target_col == 5221). Every well: [[NDFIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDFIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
