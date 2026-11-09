---
symbol: "CCDC30"
type: "gene"
col: 11811
ensembl_id: "ENSG00000186409"
name: "coiled-coil domain containing 30"
location: "1p34.2"
module: 26
arm: "+"
pooled_cpm: 11.08
n_lines_expressing: 48
n_dd_up: 30
n_dd_down: 9
n_dd_up_clean: 23
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# CCDC30

*coiled-coil domain containing 30* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.70× (z +19.7, q 0e+00, up in 41 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.489× (z -6.5, q 6e-08, down in 32 of 45 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.620× (z -4.3, q 0.002, down in 23 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD7-DT]] (+0.85, fdr 7e-06), [[CASS4]] (+0.83, fdr 7e-06), [[MGAM]] (+0.83, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[FSIP2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11811.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.70×** | +19.7 | 0e+00 | 41/42 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.77×** | +11.5 | 4e-28 | 40/43 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.05×** | +9.1 | 2e-17 | 36/46 (PANC-1, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.81×** | +8.9 | 6e-17 | 38/44 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.40×** | +7.9 | 4e-13 | 30/44 (LoVo, SW48, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.78×** | +7.3 | 2e-11 | 34/46 (J82, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **2.14×** | +6.8 | 7e-10 | 32/46 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +5.4 | 4e-06 | 19/44 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.79×** | +5.2 | 1e-05 | 25/44 (LoVo, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +5.2 | 1e-05 | 25/45 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.74×** | +4.8 | 9e-05 | 26/43 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +4.5 | 3e-04 | 20/42 (LoVo, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.41×** | +4.0 | 0.002 | 17/46 (LoVo, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.0 | 0.002 | 17/37 (MIA PaCa-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.40×** | +3.9 | 0.003 | 16/46 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Afatinib (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.005 | 14/45 (LoVo, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.21×** | +3.7 | 0.006 | 12/44 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11811.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.489×** | -6.5 | 6e-08 | 32/45 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.538×** | -5.6 | 7e-06 | 27/43 (NCI-H1573, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.565×** | -5.1 | 5e-05 | 25/44 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.591×** | -4.7 | 3e-04 | 26/44 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.620×** | -4.3 | 0.002 | 23/45 (Panc 03.27, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.621×** | -4.1 | 0.003 | 21/39 (A-172, J82, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.762×** | -3.5 | 0.041 | 17/45 (CFPAC-1, CHP-212, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.684×** | -3.4 | 0.042 | 18/45 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.692×** | -3.3 | 0.057 | 17/45 (KATO III, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.715× | -3.0 | 0.14 | 16/45 (AN3 CA, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11811. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 8.87 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +10.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.103× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 18.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 24.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +10.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0985× (z -13.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H23 (line)]] | alt | 26.0 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +9.1) | [[Digitoxin (drug)]] 0.5 µM 0.203× (z -8.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 7.15 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.52× (z +13.6) | — |
| [[C32 (line)]] | wt | 27.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0965× (z -12.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 24.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.224× (z -8.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 9.02 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +10.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.126× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 8.52 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +10.5) | — |
| [[PANC-1 (line)]] | alt | 7.88 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +14.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -9.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[RKO (line)]] | wt | 7.32 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.09× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 3.06 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.14× (z +9.3) | [[Zileuton (drug)]] 0.5 µM 0.0541× (z -8.7) |
| [[A-172 (line)]] | wt | 7.56 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0955× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[BT-474 (line)]] | alt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.98× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 17.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 26.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 8.78 | 0 | 1 | — | [[Orlistat (drug)]] 0.5 µM 0.0690× (z -8.6) |
| [[HOP62 (line)]] | alt | 9.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 6.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.87× (z +11.1) | — |
| [[KATO III (line)]] | alt | 7.07 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0492× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 8.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.63× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 13.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +10.4) | — |
| [[NCI-H1792 (line)]] | alt | 5.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.48× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 6.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 9.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.47× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 19.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.64× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +9.8) | — |
| [[SNU-1 (line)]] | wt | 15.0 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0628× (z -10.5) |
| [[SW48 (line)]] | wt | 7.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +10.1) | — |
| [[A-427 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11811), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD7-DT]] | +0.85 | +0.88 / +0.62 | both halves | 7e-06 |  |
| [[CASS4]] | +0.83 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[MGAM]] | +0.83 | +0.83 / +0.66 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.80 | +0.83 / +0.48 | both halves | 2e-05 |  |
| [[DNAI4]] | +0.80 | +0.82 / +0.55 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.79 | +0.78 / +0.50 | both halves | 1e-05 |  |
| [[OXA1L-DT]] | +0.79 | +0.80 / +0.55 | both halves | 1e-05 |  |
| [[NEK11]] | +0.78 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[PKN2-AS1]] | +0.78 | +0.81 / +0.41 | both halves | 4e-05 |  |
| [[LINC01762]] | +0.78 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[HSD17B3]] | +0.77 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.77 | +0.82 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises CCDC30's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 2.36× lower at baseline in the lines without FSIP2-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CCDC30's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01482]] | B | LINC01482 activity raises CCDC30's level | lines that do not express LINC01482 (5) vs lines expressing it (45) | 2.00× lower at baseline in the lines without LINC01482 | 0.045 | ⚠ within organs, on part of the lines; also absent: MAP7D2, SLC35F4, ENSG00000226965; maybe low, not absent |
| [[LINC02641]] | B | LINC02641 activity raises CCDC30's level | lines that do not express LINC02641 (14) vs lines expressing it (36) | 1.53× lower at baseline in the lines without LINC02641 | 0.060 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent |
| [[IGSF11]] | B | IGSF11 activity raises CCDC30's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.68× lower at baseline in the lines without IGSF11 | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[ZIC1]] | B | ZIC1 activity raises CCDC30's level | lines that do not express ZIC1 (34) vs lines expressing it (16) | 1.36× lower at baseline in the lines without ZIC1 | 0.084 | ⚠ within organs, on part of the lines; also absent: PCDH18, MDGA2, DCN |
| [[ST8SIA5]] | B | ST8SIA5 activity raises CCDC30's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.90× lower at baseline in the lines without ST8SIA5 | 0.094 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[LRRIQ3]] | C | LRRIQ3 activity raises CCDC30's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.90× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; co-absent with the target; its own permutation p |
| [[TNNI3K]] | C | TNNI3K activity raises CCDC30's level | lines that do not express TNNI3K (3) vs lines expressing it (47) | 2.29× lower at baseline in the lines without TNNI3K | 0.092 | ⚠ few lines (3 vs 47); across organs; also absent: CORIN, CLEC2D, CFAP58; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.856). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (10.9, 17.2); signed map (23.4, -1.0). **Vector** length 87.8, 20.0% of its response variance represented; |z| ≥ 3 in 1,123 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +19.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.1 | +7.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +11.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +9.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +4.8 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | +1.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.5 | +0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | +3.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.3 | +5.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | +0.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -2.6 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -1.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 30 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:42,463,221-42,657,190 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20972, PFD6L, LOC728621 |
| Matched by | ensembl_id |

UniProt [Q5VVM6](https://www.uniprot.org/uniprotkb/Q5VVM6) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26103](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26103) · Entrez [728621](https://www.ncbi.nlm.nih.gov/gene/728621) · UniProt [Q5VVM6](https://www.uniprot.org/uniprotkb/Q5VVM6) · Ensembl [ENSG00000186409](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186409)

## Data

Gene col 11811: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11811); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11811, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11811]; `tensor/DDL_lfc|DDL_z.npy` [11811]; `embed/gene_vectors.npy` [11811]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11811 or target_col == 11811). Every well: [[CCDC30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
