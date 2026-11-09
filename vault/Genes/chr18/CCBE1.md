---
symbol: "CCBE1"
type: "gene"
col: 11388
ensembl_id: "ENSG00000183287"
name: "collagen and calcium binding EGF domains 1"
location: "18q21.32"
module: 104
arm: "+"
pooled_cpm: 39.65
n_lines_expressing: 22
n_dd_up: 50
n_dd_down: 2
n_dd_up_clean: 38
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 13
direction_downstream: 26
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# CCBE1

*collagen and calcium binding EGF domains 1* — 18q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 50 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.54× (z +23.0, q 0e+00, up in 8 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 0.736× (z -5.4, q 4e-05, down in 16 of 20 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H1792 0.345×, J82 0.404×, A498 0.442×); [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-423 0.175×, NCI-H1792 0.272×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 2 lines (J82 0.269×, A498 0.323×; ⚠ cell-cycle shift, explains ~25% of this change); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM in 2 lines (A-172 0.218×, A498 0.357×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (J82 0.311×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PID1]] (+0.64, fdr 1e-05), [[DAW1]] (+0.62, fdr 7e-06), [[PTX3]] (+0.58, fdr 1e-05); moves opposite to [[ANXA10]] (-0.56, fdr 4e-05), [[MRPS6]] (-0.48, fdr 3e-05), [[MANCR]] (-0.47, fdr 7e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[EVA1A-AS]] → it (grade B ⚠); 26 go from it, the strongest it → [[LPAR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 50 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11388.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +23.0 | 0e+00 | 8/20 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.64×** | +16.9 | 0e+00 | 4/19 (Panc 03.27, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +16.1 | 0e+00 | 13/20 (SNU-423, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +12.7 | 1e-34 | 8/19 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +12.4 | 2e-33 | 10/20 (RPMI-7951, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +11.0 | 4e-26 | 5/18 (CFPAC-1, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +10.8 | 4e-25 | 3/16 (A-172, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +10.3 | 6e-23 | 1/19 (Hs 766T) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +10.0 | 1e-21 | 10/20 (RPMI-7951, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +8.9 | 3e-17 | 9/19 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.48×** | +8.3 | 7e-15 | 13/20 (SNU-423, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +7.5 | 4e-12 | 13/20 (RPMI-7951, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +7.3 | 1e-11 | 4/19 (RPMI-7951, Hs 766T, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.52×** | +7.0 | 8e-11 | 12/19 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.9 | 2e-10 | 6/20 (hTERT-HPNE, Hs 766T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +6.8 | 5e-10 | 5/20 (HOP62, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +6.1 | 3e-08 | 11/19 (SNU-423, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +5.9 | 1e-07 | 11/20 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +5.9 | 1e-07 | 12/20 (SNU-423, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11388.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H1792 0.345×, J82 0.404×, A498 0.442×); [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-423 0.175×, NCI-H1792 0.272×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 2 lines (J82 0.269×, A498 0.323×; ⚠ cell-cycle shift, explains ~25% of this change); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM in 2 lines (A-172 0.218×, A498 0.357×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (J82 0.311×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.736×** | -5.4 | 4e-05 | 16/20 (A-172, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.760×** | -4.8 | 4e-04 | 10/20 (NCI-H2030, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.871× | -3.4 | 0.10 | 6/20 (NCI-H23, A549, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.876× | -3.3 | 0.10 | 11/20 (J82, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Rifaximin (drug)]] 0.05 µM |  | 0.817× | -3.3 | 0.10 | 2/19 (SNU-423, NCI-H23) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 0.831× | -3.3 | 0.10 | 3/19 (SW 1088, Panc 03.27, …) | inconsistent across doses |  |
| [[Pimozide (drug)]] 0.05 µM |  | 0.840× | -3.1 | 0.15 | 1/18 (NCI-H2347) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11388. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 397 | 0 | 8 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.191× (z -19.5) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -13.8) |
| [[SNU-423 (line)]] | alt | 260 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -13.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 95.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 174 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.0) | — |
| [[A-172 (line)]] | wt | 32.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +8.7) | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.218× (z -9.2) |
| [[Hs 766T (line)]] | wt | 36.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +12.5) | — |
| [[NCI-H1792 (line)]] | alt | 84.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 69.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.619× (z -9.4) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.159× (z -8.6) |
| [[A-427 (line)]] | wt | 2.63 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.92 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.76 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.01 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.13 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.83 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 107 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.99 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.65 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.48 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.46 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.52 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.17 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11388), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PID1]] | +0.64 | +0.64 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[DAW1]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[PTX3]] | +0.58 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[PHLDB2]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[IL1R1]] | +0.54 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[SLC39A14]] | +0.53 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[ROS1]] | +0.52 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[TGFB2]] | +0.52 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[GPR176]] | +0.52 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[VGLL3]] | +0.51 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[SRGN]] | +0.51 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[HIPK2]] | +0.51 | +0.49 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANXA10]] | -0.56 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[MRPS6]] | -0.48 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[MANCR]] | -0.47 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[LINC02813]] | -0.47 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[SLC5A3]] | -0.44 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[GDNF]] | -0.43 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[EVA1A-AS]] | -0.43 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[PTHLH]] | -0.42 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[LINC01705]] | -0.42 | -0.47 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 4, C 9. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EVA1A-AS]] | B | EVA1A-AS activity raises CCBE1's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 1.78× lower at baseline in the lines without EVA1A-AS | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[MT1E]] | B | MT1E activity raises CCBE1's level | lines that do not express MT1E (22) vs lines expressing it (28) | 1.86× lower at baseline in the lines without MT1E | 0.036 | ⚠ within organs, on part of the lines; also absent: MT1M, ENSG00000291105, ACSL5 |
| [[LPAR1]] | B | LPAR1 activity raises CCBE1's level | lines that do not express LPAR1 (15) vs lines expressing it (35) | 4.12× lower at baseline in the lines without LPAR1 | 0.073 | ⚠ within organs, on part of the lines; also absent: SVEP1, PAPSS2, TOX2 |
| [[GCNT1]] | B | GCNT1 activity raises CCBE1's level | lines that do not express GCNT1 (5) vs lines expressing it (45) | 3.55× lower at baseline in the lines without GCNT1 | 0.073 | ⚠ within organs, on part of the lines; also absent: ANKH, MLLT3, TLE4; maybe low, not absent |
| [[TLR2]] | C | TLR2 activity raises CCBE1's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 4.10× lower at baseline in the lines without TLR2 | 0.015 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA; co-absent with the target |
| [[GPR176]] | C | GPR176 activity raises CCBE1's level | lines that do not express GPR176 (18) vs lines expressing it (32) | 5.64× lower at baseline in the lines without GPR176 | 0.034 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, AFAP1L1; co-absent with the target |
| [[FOXC2]] | C | FOXC2 activity raises CCBE1's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 4.06× lower at baseline in the lines without FOXC2 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT; co-absent with the target |
| [[NNMT]] | C | NNMT activity raises CCBE1's level | lines that do not express NNMT (24) vs lines expressing it (26) | 5.01× lower at baseline in the lines without NNMT | 0.043 | ⚠ within organs, on part of the lines; also absent: KC6, DPYSL3, ENSG00000230615; co-absent with the target |
| [[LINC01705]] | C | LINC01705 activity raises CCBE1's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 3.54× lower at baseline in the lines without LINC01705 | 0.049 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137; co-absent with the target |
| [[EFEMP1]] | C | EFEMP1 activity raises CCBE1's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 5.25× lower at baseline in the lines without EFEMP1 | 0.058 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA; co-absent with the target |
| [[ROS1]] | C | ROS1 activity raises CCBE1's level | lines that do not express ROS1 (30) vs lines expressing it (20) | 4.57× lower at baseline in the lines without ROS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: COL1A1, APCDD1L, GYPC; maybe low, not absent; co-absent with the target |
| [[PTHLH]] | C | PTHLH activity raises CCBE1's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 4.19× lower at baseline in the lines without PTHLH | 0.068 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 17, C 9. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LPAR1]] | B | CCBE1 activity raises LPAR1's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 5.37× lower at baseline in the lines without CCBE1 | 0.002 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[PALM2AKAP2]] | B | CCBE1 activity raises PALM2AKAP2's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 4.01× lower at baseline in the lines without CCBE1 | 0.004 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[PGM5P2]] | B | CCBE1 activity raises PGM5P2's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 1.90× lower at baseline in the lines without CCBE1 | 0.011 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[ETS1]] | B | CCBE1 activity raises ETS1's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 3.51× lower at baseline in the lines without CCBE1 | 0.016 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[CACNA1C]] | B | CCBE1 activity weakens CACNA1C's drug response | lines that do not express CCBE1 (22) vs lines expressing it (14) | the lines without CCBE1 respond 2.08× as strongly (z diff -2.00); strongest at Dinaciclib 0.5 µM: 1.58x vs 0.57x (z diff -5.0) | 0.036 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1; target measured in part of the lines; artifact flags |
| [[RUNX2]] | B | CCBE1 activity raises RUNX2's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 2.16× lower at baseline in the lines without CCBE1 | 0.042 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[B4GALT1]] | B | CCBE1 activity raises B4GALT1's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 1.77× lower at baseline in the lines without CCBE1 | 0.047 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[HEG1]] | B | CCBE1 activity raises HEG1's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 2.69× lower at baseline in the lines without CCBE1 | 0.052 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[LAMB1]] | B | CCBE1 activity raises LAMB1's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 2.39× lower at baseline in the lines without CCBE1 | 0.056 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[TGFB2]] | B | CCBE1 activity raises TGFB2's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 3.62× lower at baseline in the lines without CCBE1 | 0.063 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[ARID5B]] | B | CCBE1 activity raises ARID5B's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 1.53× lower at baseline in the lines without CCBE1 | 0.067 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[GCNT1]] | B | CCBE1 activity raises GCNT1's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 1.24× lower at baseline in the lines without CCBE1 | 0.068 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.602). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.9, 17.2); signed map (19.1, 34.7). **Vector** length 76.9, 22.9% of its response variance represented; |z| ≥ 3 in 740 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +12.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +8.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.8 | +5.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.5 | +5.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.5 | +2.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~12% of this change | -2.5 | +1.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.4 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -0.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -2.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Vilanterol (drug)]] 5 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | collagen and calcium binding EGF domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.32 — chr18:59,430,939-59,697,662 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30681, KIAA1983 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UXH8](https://www.uniprot.org/uniprotkb/Q6UXH8) (Collagen and calcium-binding EGF domain-containing protein 1):

> Required for lymphangioblast budding and angiogenic sprouting from venous endothelium during embryogenesis.

**Summary**, from NCBI Gene [147372](https://www.ncbi.nlm.nih.gov/gene/147372):

> This gene is thought to function in extracellular matrix remodeling and migration. It is predominantly expressed in the ovary, but down regulated in ovarian cancer cell lines and primary carcinomas, suggesting its role as a tumour suppressor. Mutations in this gene have been associated with Hennekam lymphangiectasia-lymphedema syndrome, a generalized lymphatic dysplasia in humans. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:29426](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29426) · Entrez [147372](https://www.ncbi.nlm.nih.gov/gene/147372) · UniProt [Q6UXH8](https://www.uniprot.org/uniprotkb/Q6UXH8) · Ensembl [ENSG00000183287](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183287)

## Data

Gene col 11388: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11388); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11388, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11388]; `tensor/DDL_lfc|DDL_z.npy` [11388]; `embed/gene_vectors.npy` [11388]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11388 or target_col == 11388). Every well: [[CCBE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCBE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
