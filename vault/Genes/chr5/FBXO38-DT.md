---
symbol: "FBXO38-DT"
type: "gene"
col: 14487
ensembl_id: "ENSG00000247199"
name: "FBXO38 divergent transcript"
location: "5q32"
module: 10
arm: "+"
pooled_cpm: 13.73
n_lines_expressing: 46
n_dd_up: 22
n_dd_down: 5
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 8
direction_downstream: 11
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# FBXO38-DT

*FBXO38 divergent transcript* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.19× (z +16.4, q 0e+00, up in 35 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.608× (z -5.0, q 4e-04, down in 23 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 5 lines (SW480 0.0768×, LOX-IMVI 0.0980×, SK-MEL-2 0.0993×, RPMI-7951 0.0737×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (LOX-IMVI 0.169×, SW480 0.216×; ⚠ cell-cycle shift, explains ~28% of this change); [[Digitoxin (drug)]] 0.5 µM in 2 lines (LOX-IMVI 0.178×, SW480 0.263×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0803×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.236×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEB]] (+0.79, fdr 7e-06), [[PCNX4-DT]] (+0.79, fdr 7e-06), [[TMEM202-AS1]] (+0.78, fdr 7e-06); moves opposite to [[L2HGDH]] (-0.65, fdr 6e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LINC01905]] → it (grade B ⚠); 11 go from it, the strongest it → [[FSIP2-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14487.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.19×** | +16.4 | 0e+00 | 35/40 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.84×** | +14.8 | 0e+00 | 32/38 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.21×** | +11.7 | 3e-29 | 32/42 (NCI-H460, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +10.2 | 2e-22 | 18/29 (PANC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.99×** | +9.7 | 2e-20 | 31/43 (PANC-1, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +8.6 | 1e-15 | 27/39 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +7.3 | 2e-11 | 6/15 (PANC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +7.3 | 2e-11 | 9/20 (HOP62, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.00×** | +6.9 | 3e-10 | 22/38 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.60×** | +6.6 | 2e-09 | 21/44 (A-172, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +6.2 | 3e-08 | 23/38 (NCI-H460, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.70×** | +5.3 | 5e-06 | 23/43 (KATO III, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.64×** | +5.0 | 3e-05 | 14/41 (KATO III, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +4.6 | 2e-04 | 12/42 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.002 | 11/42 (A-172, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.007 | 11/42 (LoVo, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.014 | 11/42 (A-172, A498, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.041 | 8/43 (C32, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14487.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 5 lines (SW480 0.0768×, LOX-IMVI 0.0980×, SK-MEL-2 0.0993×, RPMI-7951 0.0737×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (LOX-IMVI 0.169×, SW480 0.216×; ⚠ cell-cycle shift, explains ~28% of this change); [[Digitoxin (drug)]] 0.5 µM in 2 lines (LOX-IMVI 0.178×, SW480 0.263×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0803×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.236×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.608×** | -5.0 | 4e-04 | 23/42 (LOX-IMVI, SW480, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.646×** | -4.4 | 0.004 | 21/43 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.692×** | -3.7 | 0.042 | 15/40 (SW480, LOX-IMVI, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.711×** | -3.4 | 0.090 | 15/43 (SW480, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.717×** | -3.3 | 0.098 | 18/42 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.727× | -3.2 | 0.13 | 11/42 (H4, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14487. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.6 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0768× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.263× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 85.2 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0980× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.178× (z -10.8) |
| [[LoVo (line)]] | wt | 75.9 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +16.0) | [[Panobinostat (drug)]] 5 µM 0.238× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 10.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +15.0) | — |
| [[NCI-H1573 (line)]] | alt | 24.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.204× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[Hs 766T (line)]] | wt | 17.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.0836× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HS-578T (line)]] | alt | 5.69 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.29× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 3.70 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +9.9) | — |
| [[RKO (line)]] | wt | 7.73 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.31× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 15.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0737× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Hydroxyurea (drug)]] 0.05 µM 0.0803× (z -9.8) |
| [[C-33 A (line)]] | alt | 6.91 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +12.1) | — |
| [[HCT15 (line)]] | alt | 4.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 6.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 5.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 8.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +15.0) | — |
| [[NCI-H23 (line)]] | alt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +16.6) | — |
| [[SHP-77 (line)]] | alt | 44.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -10.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0993× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14487), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEB]] | +0.79 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[PCNX4-DT]] | +0.79 | +0.79 / +0.58 | both halves | 7e-06 | same gene group |
| [[TMEM202-AS1]] | +0.78 | +0.79 / +0.60 | both halves | 7e-06 |  |
| [[TMEM232]] | +0.78 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[UNC79]] | +0.75 | +0.77 / +0.53 | both halves | 1e-05 |  |
| [[PDCL3P4]] | +0.74 | +0.78 / +0.53 | both halves | 1e-05 |  |
| [[LINC00240]] | +0.74 | +0.76 / +0.53 | both halves | 1e-05 |  |
| [[NPAS3]] | +0.74 | +0.78 / +0.46 | both halves | 2e-05 |  |
| [[PKN2-AS1]] | +0.74 | +0.75 / +0.47 | both halves | 2e-05 |  |
| [[DRAIC]] | +0.74 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[MAP3K7CL]] | +0.74 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[DNAH12]] | +0.73 | +0.73 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L2HGDH]] | -0.65 | -0.54 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01905]] | B | LINC01905 activity raises FBXO38-DT's level | lines that do not express LINC01905 (35) vs lines expressing it (15) | 2.06× lower at baseline in the lines without LINC01905 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000267327, ENSG00000267284, SLC25A24P1 |
| [[TOP2A]] | B | TOP2A activity lowers FBXO38-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NPAS3]] | B | NPAS3 activity raises FBXO38-DT's level | lines that do not express NPAS3 (16) vs lines expressing it (34) | 2.07× lower at baseline in the lines without NPAS3 | 0.029 | ⚠ within organs, on part of the lines; also absent: SLC2A14, MARK1, CAMK4; maybe low, not absent |
| [[LY96]] | B | LY96 activity raises FBXO38-DT's level | lines that do not express LY96 (18) vs lines expressing it (32) | 1.77× lower at baseline in the lines without LY96 | 0.032 | ⚠ within organs, on part of the lines; also absent: SOX5, ENSG00000287100, ENSG00000287622; maybe low, not absent |
| [[LINC02405]] | B | LINC02405 activity raises FBXO38-DT's level | lines that do not express LINC02405 (27) vs lines expressing it (23) | 1.88× lower at baseline in the lines without LINC02405 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000286016, ENSG00000278266, LINC02360 |
| [[KCNMB2-AS1]] | B | KCNMB2-AS1 activity raises FBXO38-DT's level | lines that do not express KCNMB2-AS1 (14) vs lines expressing it (36) | 2.01× lower at baseline in the lines without KCNMB2-AS1 | 0.063 | ⚠ within organs, on part of the lines; also absent: FIRRE, STXBP6, LINC01980; maybe low, not absent |
| [[LINC00491]] | B | LINC00491 activity raises FBXO38-DT's level | lines that do not express LINC00491 (33) vs lines expressing it (17) | 1.80× lower at baseline in the lines without LINC00491 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APCDD1L, LINC01905, ADGRG7 |
| [[MAP2K1]] | B | MAP2K1 activity lowers FBXO38-DT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSIP2-AS1]] | C | FBXO38-DT activity raises FSIP2-AS1's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 3.28× lower at baseline in the lines without FBXO38-DT | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent; its own permutation p |
| [[DLG2]] | C | FBXO38-DT activity raises DLG2's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 2.50× lower at baseline in the lines without FBXO38-DT | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent; its own permutation p |
| [[UBA6-DT]] | C | FBXO38-DT activity raises UBA6-DT's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 2.03× lower at baseline in the lines without FBXO38-DT | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent; its own permutation p |
| [[FAM227B]] | C | FBXO38-DT activity raises FAM227B's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 1.97× lower at baseline in the lines without FBXO38-DT | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent; its own permutation p |
| [[H2AZ1-DT]] | C | FBXO38-DT activity raises H2AZ1-DT's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 1.34× lower at baseline in the lines without FBXO38-DT | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent; its own permutation p |
| [[PCNX4-DT]] | C | FBXO38-DT activity raises PCNX4-DT's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 1.42× lower at baseline in the lines without FBXO38-DT | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent |
| [[SEPTIN7-DT]] | C | FBXO38-DT activity raises SEPTIN7-DT's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 1.62× lower at baseline in the lines without FBXO38-DT | 0.075 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent |
| [[CCDC134]] | C | FBXO38-DT activity raises CCDC134's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 1.46× lower at baseline in the lines without FBXO38-DT | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent |
| [[ALOX12-AS1]] | C | FBXO38-DT activity raises ALOX12-AS1's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 2.66× lower at baseline in the lines without FBXO38-DT | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent; its own permutation p |
| [[MAD2L1-DT]] | C | FBXO38-DT activity raises MAD2L1-DT's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without FBXO38-DT | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent; its own permutation p |
| [[RGS5]] | C | FBXO38-DT activity raises RGS5's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without FBXO38-DT | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.792). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (8.8, 15.9); signed map (28.4, -9.9). **Vector** length 87.5, 18.0% of its response variance represented; |z| ≥ 3 in 1,027 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.2 | +16.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.9 | +14.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.3 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.6 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.1 | +9.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +2.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.8 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +3.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | +0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -4.6 | -1.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | +1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.4 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -0.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -3.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | FBXO38 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q32 — chr5:148,088,125-148,383,907 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55589](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55589) · Entrez [102546294](https://www.ncbi.nlm.nih.gov/gene/102546294) · Ensembl [ENSG00000247199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247199)

## Data

Gene col 14487: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14487); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14487, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14487]; `tensor/DDL_lfc|DDL_z.npy` [14487]; `embed/gene_vectors.npy` [14487]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14487 or target_col == 14487). Every well: [[FBXO38-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO38-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
