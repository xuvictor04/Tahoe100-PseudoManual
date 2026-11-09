---
symbol: "RRP9"
type: "gene"
col: 3584
ensembl_id: "ENSG00000114767"
name: "ribosomal RNA processing 9, U3 small nucleolar RNA binding protein"
location: "3p21.2"
module: 1
arm: "+"
pooled_cpm: 7.9
n_lines_expressing: 50
n_dd_up: 44
n_dd_down: 4
n_dd_up_clean: 24
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# RRP9

*ribosomal RNA processing 9, U3 small nucleolar RNA binding protein* — 3p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (20 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.73× (z +20.2, q 0e+00, up in 46 of 47 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 3.13× (z +18.7, q 0e+00, up in 41 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.683× (z -4.3, q 0.006, down in 14 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRMT61A]] (+0.71, fdr 7e-06), [[PWP2]] (+0.69, fdr 7e-06), [[BOP1]] (+0.68, fdr 7e-06); moves opposite to [[GNAS]] (-0.55, fdr 1e-05), [[SRP14]] (-0.53, fdr 4e-05), [[TMEM59]] (-0.51, fdr 5e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 20 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3584.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **5.73×** | +20.2 | 0e+00 | 46/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.13×** | +18.7 | 0e+00 | 41/43 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **4.53×** | +17.5 | 0e+00 | 46/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.46×** | +17.3 | 0e+00 | 36/40 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **4.23×** | +16.7 | 0e+00 | 47/47 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **3.16×** | +12.8 | 2e-35 | 40/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +12.8 | 2e-35 | 35/42 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.99×** | +12.7 | 6e-35 | 42/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **2.39×** | +9.7 | 2e-20 | 7/15 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **2.15×** | +8.8 | 5e-17 | 22/32 (LoVo, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.02×** | +8.1 | 3e-14 | 35/47 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.95×** | +7.7 | 5e-13 | 31/46 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **2.04×** | +7.6 | 1e-12 | 13/19 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.96×** | +7.5 | 3e-12 | 28/36 (NCI-H460, SHP-77, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.88×** | +7.3 | 1e-11 | 28/47 (SW480, AsPC-1, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.41×** | +5.3 | 3e-06 | 19/40 (NCI-H460, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +5.0 | 1e-05 | 21/47 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.20×** | +4.8 | 5e-05 | 17/44 (NCI-H460, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.6 | 9e-05 | 15/48 (HOP62, A-172, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.49×** | +4.4 | 2e-04 | 17/44 (NCI-H1573, NCI-H1792, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.49×** | +4.3 | 4e-04 | 11/40 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **2.01×** | +4.2 | 5e-04 | 15/41 (RKO, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.97×** | +4.1 | 8e-04 | 9/41 (NCI-H460, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.83×** | +3.7 | 0.005 | 8/36 (LoVo, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3584.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.683×** | -4.3 | 0.006 | 14/45 (A-427, A549, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.744×** | -4.2 | 0.006 | 10/47 (SW480, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.719×** | -4.2 | 0.006 | 10/48 (AsPC-1, C-33 A, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.790×** | -3.9 | 0.015 | 15/47 (SW480, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.757× | -3.3 | 0.10 | 12/47 (LoVo, HT-29, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.794× | -3.3 | 0.10 | 10/47 (SW480, A-427, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | 0.768× | -3.2 | 0.11 | 12/48 (LoVo, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.749× | -3.2 | 0.11 | 10/47 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.829× | -3.1 | 0.14 | 11/47 (H4, SK-MEL-2, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.776× | -3.0 | 0.15 | 10/45 (Hs 766T, HS-578T, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.71 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3584. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.8 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.05× (z +13.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.93× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 5.95 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.91× (z +9.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.57× (z +9.0) | — |
| [[J82 (line)]] | alt | 9.81 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +10.0) | — |
| [[KATO III (line)]] | alt | 6.67 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.39× (z +9.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 9.36 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.10× (z +10.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 5.18 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +9.4) | — |
| [[A-172 (line)]] | wt | 4.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +8.7) | — |
| [[A549 (line)]] | wt | 5.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 9.68 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.67× (z +9.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LoVo (line)]] | wt | 7.11 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.97× (z +9.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LS 180 (line)]] | wt | 5.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 9.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +8.7) | — |
| [[A-427 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3584), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT61A]] | +0.71 | +0.78 / +0.63 | both halves | 7e-06 | STRING 657 |
| [[PWP2]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[BOP1]] | +0.68 | +0.62 / +0.70 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 928 |
| [[RRP1]] | +0.68 | +0.62 / +0.63 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 810 |
| [[CLUH]] | +0.67 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[RRS1]] | +0.67 | +0.68 / +0.69 | both halves | 7e-06 | same gene group; STRING 854 |
| [[NOL6]] | +0.66 | +0.70 / +0.61 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[BCS1L]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[HGH1]] | +0.66 | +0.68 / +0.66 | both halves | 7e-06 | STRING 448 |
| [[NOC4L]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 999 |
| [[ZPR1]] | +0.65 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[ALKBH2]] | +0.64 | +0.61 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[SRP14]] | -0.53 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[TMEM59]] | -0.51 | -0.62 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises RRP9's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity raises RRP9's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers RRP9's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.544). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.9, -39.3); signed map (-3.1, -44.9). **Vector** length 66.3, 12.4% of its response variance represented; |z| ≥ 3 in 1,126 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +17.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.3 | +12.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | +3.6 | +8.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +4.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +4.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +5.3 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | -4.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -2.6 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -3.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.1 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal RNA processing 9, U3 small nucleolar RNA binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.2 — chr3:51,933,429-51,941,904 (-) |
| Ensembl biotype | protein_coding |
| Also known as | U3-55K; previously RNU3IP2 |
| Gene groups (HGNC) | WD repeat domain containing; U3 small nucleolar ribonucleoprotein; Ribosome biogenesis factors |
| Hallmark sets | MYC_TARGETS_V2, UNFOLDED_PROTEIN_RESPONSE, MTORC1_SIGNALING, MYC_TARGETS_V1 |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [O43818](https://www.uniprot.org/uniprotkb/O43818) (U3 small nucleolar RNA-interacting protein 2):

> Component of a nucleolar small nuclear ribonucleoprotein particle (snoRNP) thought to participate in the processing and modification of pre-ribosomal RNA (pre-rRNA). Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, …

**Summary**, from NCBI Gene [9136](https://www.ncbi.nlm.nih.gov/gene/9136):

> This gene encodes a member of the WD-repeat protein family. The encoded protein is a component of the nucleolar small nuclear ribonucleoprotein particle (snoRNP) and is essential for 18s rRNA processing during ribosome synthesis. It contains seven WD domains required for nucleolar localization and specific interaction with the U3 small nucleolar RNA (U3 snoRNA). [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:16829](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16829) · Entrez [9136](https://www.ncbi.nlm.nih.gov/gene/9136) · UniProt [O43818](https://www.uniprot.org/uniprotkb/O43818) · Ensembl [ENSG00000114767](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114767)

## Data

Gene col 3584: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3584); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3584, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3584]; `tensor/DDL_lfc|DDL_z.npy` [3584]; `embed/gene_vectors.npy` [3584]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3584 or target_col == 3584). Every well: [[RRP9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRP9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
