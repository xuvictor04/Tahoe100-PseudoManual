---
symbol: "CCT6B"
type: "gene"
col: 5277
ensembl_id: "ENSG00000132141"
name: "chaperonin containing TCP1 subunit 6B"
location: "17q12"
module: 35
arm: "+"
pooled_cpm: 6.15
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# CCT6B

*chaperonin containing TCP1 subunit 6B* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.13× (z +24.4, q 0e+00, up in 41 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.517× (z -8.0, q 5e-13, down in 23 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.578× (z -6.7, q 4e-09, down in 26 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (LoVo 0.0724×, SW480 0.130×, RKO 0.118×, HEC-1-A 0.209×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.0572×, BT-474 0.0618×; ⚠ cell-cycle shift, explains ~31% of this change); [[Orlistat (drug)]] 0.05 µM in 1 line (A549 0.0840×); [[Doxycycline (monohydrate) (drug)]] 5 µM in 1 line (SNU-423 0.0955×); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (A-172 0.107×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM15-AS1]] (+0.86, fdr 7e-06), [[CPEB2-DT]] (+0.83, fdr 1e-05), [[UBE2D3-AS1]] (+0.82, fdr 7e-06); moves opposite to [[WRAP73]] (-0.69, fdr 2e-05), [[NAA40]] (-0.68, fdr 3e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5277.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.13×** | +24.4 | 0e+00 | 41/42 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.04×** | +12.2 | 6e-32 | 37/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.03×** | +12.2 | 7e-32 | 29/41 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +10.7 | 1e-24 | 25/39 (HEC-1-A, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.19×** | +9.5 | 2e-19 | 27/42 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +9.0 | 3e-17 | 25/39 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +8.6 | 4e-16 | 12/20 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +4.9 | 6e-05 | 16/45 (HEC-1-A, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +4.6 | 2e-04 | 3/11 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.43×** | +4.3 | 9e-04 | 10/44 (J82, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.002 | 11/47 (PANC-1, BT-474, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.71×** | +3.4 | 0.031 | 3/12 (A498, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.085 | 7/44 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5277.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (LoVo 0.0724×, SW480 0.130×, RKO 0.118×, HEC-1-A 0.209×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.0572×, BT-474 0.0618×; ⚠ cell-cycle shift, explains ~31% of this change); [[Orlistat (drug)]] 0.05 µM in 1 line (A549 0.0840×); [[Doxycycline (monohydrate) (drug)]] 5 µM in 1 line (SNU-423 0.0955×); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (A-172 0.107×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.517×** | -8.0 | 5e-13 | 23/39 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.540×** | -7.5 | 2e-11 | 24/47 (KATO III, J82, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.578×** | -6.7 | 4e-09 | 26/46 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.608×** | -6.1 | 2e-07 | 21/45 (RPMI-7951, BT-474, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.611×** | -6.0 | 2e-07 | 23/46 (A-427, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.538×** | -4.0 | 0.007 | 12/36 (SW480, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.807×** | -3.7 | 0.016 | 11/46 (HS-578T, SW 1271, …) | top dose only |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM |  | 0.768× | -3.0 | 0.19 | 6/43 (LOX-IMVI, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5277. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.20 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +9.7) | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.107× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 8.56 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +13.0) | [[Digitoxin (drug)]] 5 µM 0.209× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[KATO III (line)]] | alt | 12.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -9.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H2030 (line)]] | alt | 14.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 6.17 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +9.2) | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.0955× (z -8.9) |
| [[SW480 (line)]] | alt | 5.50 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +10.9) | [[Digitoxin (drug)]] 5 µM 0.130× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A498 (line)]] | wt | 6.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +9.0) | — |
| [[A549 (line)]] | wt | 7.68 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0840× (z -9.8) |
| [[BT-474 (line)]] | alt | 7.24 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0618× (z -10.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HOP62 (line)]] | alt | 6.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.33× (z +11.8) | — |
| [[LoVo (line)]] | wt | 7.52 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0724× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[LOX-IMVI (line)]] | wt | 3.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.86× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 3.51 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.05 µM 0.0689× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 8.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.23× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 9.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 2.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.97× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 4.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 4.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.13× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 4.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.64× (z +13.6) | — |
| [[RKO (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RPMI-7951 (line)]] | alt | 7.57 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0572× (z -10.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 5.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.19× (z +10.4) | — |
| [[A-427 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5277), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM15-AS1]] | +0.86 | +0.84 / +0.69 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.83 | +0.83 / +0.52 | both halves | 1e-05 |  |
| [[UBE2D3-AS1]] | +0.82 | +0.81 / +0.65 | both halves | 7e-06 |  |
| [[PCBP1-AS1]] | +0.81 | +0.81 / +0.49 | both halves | 1e-05 |  |
| [[TMEM202-AS1]] | +0.80 | +0.80 / +0.55 | both halves | 1e-05 |  |
| [[PBLD]] | +0.80 | +0.77 / +0.48 | both halves | 2e-05 |  |
| [[LINC00880]] | +0.79 | +0.81 / +0.43 | both halves | 3e-05 |  |
| [[MSH4]] | +0.78 | +0.80 / +0.44 | both halves | 3e-05 |  |
| [[ZCWPW1]] | +0.77 | +0.77 / +0.50 | both halves | 1e-05 |  |
| [[LINC02955]] | +0.77 | +0.77 / +0.47 | both halves | 2e-05 |  |
| [[GSK3B-DT]] | +0.77 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[DDX19A-DT]] | +0.77 | +0.74 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRAP73]] | -0.69 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[NAA40]] | -0.68 | -0.55 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCT6B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABCA10]] | B | ABCA10 activity raises CCT6B's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.49× lower at baseline in the lines without ABCA10 | 0.011 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[CDK6-AS1]] | B | CDK6-AS1 activity raises CCT6B's level | lines that do not express CDK6-AS1 (6) vs lines expressing it (44) | 1.31× lower at baseline in the lines without CDK6-AS1 | 0.066 | ⚠ within organs, on part of the lines; also absent: PLS3, CDK6, UACA; maybe low, not absent |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity raises CCT6B's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.50× lower at baseline in the lines without ZNF341-AS1 | 0.099 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.807). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (10.6, 11.4); signed map (22.3, -3.6). **Vector** length 82.7, 15.2% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +24.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +6.0 | +12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +8.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +4.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +1.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.2 | -6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -3.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.8 | -1.5 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.6 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | chaperonin containing TCP1 subunit 6B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:34,927,859-34,981,078 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Cctz2, TSA303 |
| Gene groups (HGNC) | Chaperonin containing TCP1 |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 8 pathways, smallest: Folding of actin by CCT/TriC; Formation of tubulin folding intermediates by CCT/TriC; Prefoldin mediated transfer of substrate  to CCT/TriC |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92526](https://www.uniprot.org/uniprotkb/Q92526) (Probable T-complex protein 1 subunit zeta-2):

> Could function as a component of a tissue-specific chaperonin-containing T-complex (TRiC), a molecular chaperone complex that assists the folding of actin, tubulin and other proteins upon ATP hydrolysis.

**Summary**, from NCBI Gene [10693](https://www.ncbi.nlm.nih.gov/gene/10693):

> This gene encodes a molecular chaperone that is a member of the chaperonin-containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including actin and tubulin. Alternative splicing results in multiple transcript variants. [provided by RefSeq, …

**Accessions** — [HGNC:1621](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1621) · Entrez [10693](https://www.ncbi.nlm.nih.gov/gene/10693) · UniProt [Q92526](https://www.uniprot.org/uniprotkb/Q92526) · Ensembl [ENSG00000132141](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132141)

## Data

Gene col 5277: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5277); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5277, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5277]; `tensor/DDL_lfc|DDL_z.npy` [5277]; `embed/gene_vectors.npy` [5277]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5277 or target_col == 5277). Every well: [[CCT6B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCT6B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
