---
symbol: "DNAJC27-AS1"
type: "gene"
col: 13382
ensembl_id: "ENSG00000224165"
name: "DNAJC27 antisense RNA 1"
location: "2p23.3"
module: 23
arm: "+"
pooled_cpm: 6.75
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 6
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# DNAJC27-AS1

*DNAJC27 antisense RNA 1* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 19.2× (z +33.7, q 0e+00, up in 27 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.29× (z +19.2, q 0e+00, up in 37 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.582× (z -6.2, q 3e-07, down in 18 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.05 µM: 0.606× (z -5.7, q 3e-06, down in 14 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 5 µM in 1 line (NCI-H1573 0.0576×; ⚠ toxic; cell-cycle shift, explains ~20% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LS 180 0.0658×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.122×; ⚠ cell-cycle shift, explains ~26% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYB5D2]] (+0.82, fdr 7e-06), [[MROH8]] (+0.73, fdr 7e-06), [[UGDH-AS1]] (+0.72, fdr 7e-06).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13382.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **19.2×** | +33.7 | 0e+00 | 27/27 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **18.8×** | +32.2 | 0e+00 | 13/13 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **10.9×** | +25.2 | 0e+00 | 16/17 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.29×** | +19.2 | 0e+00 | 37/39 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +9.4 | 5e-19 | 22/42 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +7.3 | 3e-11 | 17/31 (NCI-H2347, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +4.8 | 1e-04 | 19/45 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.48×** | +4.7 | 2e-04 | 11/47 (NCI-H2030, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.41×** | +4.7 | 2e-04 | 13/46 (A-427, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.5 | 3e-04 | 10/36 (HS-578T, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.46×** | +4.4 | 5e-04 | 11/47 (NCI-H23, SW480, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.46×** | +4.3 | 7e-04 | 14/44 (HEC-1-A, HOP62, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.31×** | +4.2 | 0.001 | 13/47 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.46×** | +4.2 | 0.001 | 9/43 (C-33 A, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.30×** | +4.1 | 0.001 | 9/47 (SW480, NCI-H2030, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.43×** | +4.1 | 0.001 | 9/46 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.35×** | +4.0 | 0.002 | 13/45 (SW480, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.004 | 9/46 (C-33 A, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.013 | 8/40 (HEC-1-A, A-427, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13382.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 5 µM in 1 line (NCI-H1573 0.0576×; ⚠ toxic; cell-cycle shift, explains ~20% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LS 180 0.0658×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.122×; ⚠ cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.582×** | -6.2 | 3e-07 | 18/46 (H4, A-427, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.606×** | -5.7 | 3e-06 | 14/44 (BT-474, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.654×** | -4.7 | 6e-04 | 15/32 (LS 180, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.717×** | -3.8 | 0.019 | 15/45 (A-427, LS 180, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.726×** | -3.7 | 0.028 | 11/45 (NCI-H2030, BT-474, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.557×** | -3.5 | 0.043 | 10/37 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.766× | -3.1 | 0.15 | 16/46 (BT-474, HEC-1-A, …) | two highest doses | composition shift |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.751× | -3.0 | 0.15 | 4/46 (H4, CHP-212, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.831× | -3.0 | 0.15 | 6/47 (SW480, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13382. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.49 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 45.9× (z +21.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.20× (z +11.7) | — |
| [[CFPAC-1 (line)]] | alt | 6.27 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 29.3× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 6.41 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 35.2× (z +14.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 4.45 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 18.8× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 15.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 29.5× (z +16.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 11.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 39.0× (z +11.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 10.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 48.2× (z +14.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 4.13 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 20.5× (z +9.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 7.79 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 18.8× (z +11.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 17.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 7.87× (z +12.5) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.0576× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~20% of this change |
| [[NCI-H2030 (line)]] | alt | 9.70 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.122× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 4.38 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 16.2× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.68× (z +9.1) | — |
| [[SW480 (line)]] | alt | 6.13 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 29.4× (z +16.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.165× (z -8.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 3.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +11.4) | — |
| [[A549 (line)]] | wt | 9.10 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.4× (z +12.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 4.62 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0658× (z -8.9) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 7.15 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.9× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.56× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 6.53 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 39.2× (z +13.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13382), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5D2]] | +0.82 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[MROH8]] | +0.73 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[UGDH-AS1]] | +0.72 | +0.66 / +0.65 | both halves | 7e-06 | same gene group |
| [[EPM2A-DT]] | +0.71 | +0.73 / +0.47 | both halves | 2e-05 |  |
| [[PJVK]] | +0.71 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[COPB2-DT]] | +0.71 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[OXA1L-DT]] | +0.70 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[USP38-DT]] | +0.69 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[TMEM202-AS1]] | +0.68 | +0.72 / +0.50 | both halves | 1e-05 | same gene group |
| [[TBCE-1]] | +0.68 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[MSTO1]] | +0.68 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[SEPTIN7-DT]] | +0.68 | +0.67 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers DNAJC27-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[TOP2A]] | B | TOP2A activity lowers DNAJC27-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.673). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (5.9, 19.3); signed map (30.2, -7.4). **Vector** length 76.3, 13.6% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.6 | +25.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +32.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +33.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +19.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +9.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +4.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.8 | +4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +4.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -6.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +0.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -0.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | DNAJC27 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p23.3 — chr2:24,971,390-25,039,716 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42943](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42943) · Entrez [729723](https://www.ncbi.nlm.nih.gov/gene/729723) · Ensembl [ENSG00000224165](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224165)

## Data

Gene col 13382: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13382); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13382, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13382]; `tensor/DDL_lfc|DDL_z.npy` [13382]; `embed/gene_vectors.npy` [13382]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13382 or target_col == 13382). Every well: [[DNAJC27-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC27-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
