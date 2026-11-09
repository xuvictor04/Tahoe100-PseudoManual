---
symbol: "LCP1"
type: "gene"
col: 5830
ensembl_id: "ENSG00000136167"
name: "lymphocyte cytosolic protein 1"
location: "13q14.13"
module: 116
arm: "+"
pooled_cpm: 25.11
n_lines_expressing: 17
n_dd_up: 33
n_dd_down: 7
n_dd_up_clean: 24
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 11
direction_downstream: 6
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# LCP1

*lymphocyte cytosolic protein 1* — 13q14.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.63× (z +18.3, q 0e+00, up in 7 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.99× (z +12.1, q 3e-31, up in 10 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 0.05 µM: 0.707× (z -6.0, q 9e-07, down in 9 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB3B]] (+0.63, fdr 1e-05), [[IL31RA]] (+0.63, fdr 1e-05), [[ACTN1]] (+0.59, fdr 1e-05); moves opposite to [[B9D2]] (-0.55, fdr 5e-05), [[CHKB]] (-0.50, fdr 3e-05), [[DYRK1B]] (-0.46, fdr 2e-04).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[LTBP2]] → it (grade B ⚠); 6 go from it, the strongest it → [[CD274]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5830.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.63×** | +18.3 | 0e+00 | 7/10 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.22×** | +14.5 | 1e-45 | 10/13 (Panc 03.27, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.99×** | +12.1 | 3e-31 | 10/15 (Panc 03.27, C32, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.89×** | +11.1 | 2e-26 | 7/15 (Panc 03.27, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +7.4 | 2e-11 | 6/13 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.75×** | +6.7 | 2e-09 | 8/15 (Panc 03.27, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +6.6 | 2e-09 | 7/14 (SW480, Panc 03.27, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +5.9 | 2e-07 | 9/15 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.57×** | +5.6 | 2e-06 | 11/15 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.37×** | +5.5 | 3e-06 | 8/15 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +4.7 | 1e-04 | 9/15 (RPMI-7951, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +4.6 | 2e-04 | 3/15 (NCI-H1573, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.4 | 4e-04 | 4/14 (CFPAC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[EX229 (drug)]] 5 µM |  | **1.89×** | +4.2 | 0.001 | 6/14 (H4, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.88×** | +4.1 | 0.002 | 8/15 (SW480, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.002 | 7/14 (RPMI-7951, SNU-423, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.002 | 3/15 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.83×** | +3.9 | 0.003 | 8/14 (HEC-1-A, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.005 | 7/14 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.009 | 6/14 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.49×** | +3.5 | 0.011 | 6/15 (CFPAC-1, NCI-H1573, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.016 | 9/14 (NCI-H1573, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5830.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | **0.707×** | -6.0 | 9e-07 | 9/15 (RKO, H4, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.619×** | -5.5 | 9e-06 | 8/15 (RKO, C32, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.785×** | -4.2 | 0.006 | 6/15 (SW480, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.745×** | -3.7 | 0.033 | 10/15 (RKO, C32, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.824×** | -3.4 | 0.069 | 5/15 (H4, Panc 03.27, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.772×** | -3.2 | 0.099 | 5/15 (H4, Panc 03.27, …) | top dose only |  |
| [[Larotrectinib (drug)]] 0.5 µM |  | **0.772×** | -3.2 | 0.099 | 7/15 (J82, RPMI-7951, …) | two highest doses | position effect removed |
| [[XRK3F2 (drug)]] 0.05 µM |  | 0.764× | -3.2 | 0.11 | 0/15 | inconsistent across doses |  |
| [[Norepinephrine (hydrochloride) (drug)]] 0.05 µM |  | 0.780× | -3.1 | 0.11 | 3/15 (Panc 03.27, HS-578T, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.840× | -3.1 | 0.11 | 2/15 (SW 1088, SNU-423) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.783× | -3.1 | 0.11 | 4/14 (C32, CFPAC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.785× | -3.0 | 0.12 | 2/15 (H4, SW 1088) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5830. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 109 | 1 | 5 (5 ⚠) | [[Auranofin (drug)]] 5 µM 3.05× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -13.9) ⚠ cell-cycle shift, explains ~19% of this change |
| [[RKO (line)]] | wt | 270 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -21.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.371× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 27.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.78× (z +8.8) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -10.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 15.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +12.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[H4 (line)]] | wt | 46.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0452× (z -21.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 7.60 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +9.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[J82 (line)]] | alt | 292 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 70.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.07× (z +12.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.17 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.95 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.66 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.17 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.47 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.60 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5830), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3B]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[IL31RA]] | +0.63 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[ACTN1]] | +0.59 | +0.52 / +0.55 | both halves | 1e-05 | STRING 403 |
| [[ADTRP]] | +0.59 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[BCAN-AS2]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[CORO1C]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CAPN2]] | +0.55 | +0.56 / +0.49 | both halves | 1e-05 | same gene group |
| [[NF2]] | +0.54 | +0.40 / +0.53 | both halves | 4e-05 |  |
| [[LNCOG]] | +0.54 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[COTL1]] | +0.53 | +0.37 / +0.50 | both halves | 9e-05 | STRING 542 |
| [[DLC1]] | +0.53 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[ZNF697]] | +0.53 | +0.40 / +0.57 | both halves | 5e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B9D2]] | -0.55 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[CHKB]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[DYRK1B]] | -0.46 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[UBN2]] | -0.46 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[GID8]] | -0.46 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[PHPT1]] | -0.45 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[TMEM91]] | -0.45 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[TERF2IP]] | -0.45 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[YY1]] | -0.44 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LTBP2]] | B | LTBP2 activity raises LCP1's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 2.87× lower at baseline in the lines without LTBP2 | 0.037 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[ZFPM2-AS1]] | B | ZFPM2-AS1 activity raises LCP1's level | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (34) | 1.96× lower at baseline in the lines without ZFPM2-AS1 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6 |
| [[MAP2K2]] | B | MAP2K2 activity raises LCP1's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[TM4SF19]] | B | TM4SF19 activity raises LCP1's level | lines that do not express TM4SF19 (20) vs lines expressing it (30) | 2.85× lower at baseline in the lines without TM4SF19 | 0.094 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS9, KYNU, PAK3 |
| [[FRMPD4]] | C | FRMPD4 activity raises LCP1's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 3.14× lower at baseline in the lines without FRMPD4 | 0.010 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3; co-absent with the target |
| [[ADTRP]] | C | ADTRP activity raises LCP1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 2.82× lower at baseline in the lines without ADTRP | 0.037 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2; co-absent with the target |
| [[TMPRSS15]] | C | TMPRSS15 activity raises LCP1's level | lines that do not express TMPRSS15 (41) vs lines expressing it (9) | 2.68× lower at baseline in the lines without TMPRSS15 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, ENSG00000224865, ENSG00000222032; co-absent with the target |
| [[PDCD1LG2]] | C | PDCD1LG2 activity raises LCP1's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 2.61× lower at baseline in the lines without PDCD1LG2 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L; co-absent with the target |
| [[LNCOG]] | C | LNCOG activity raises LCP1's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 3.00× lower at baseline in the lines without LNCOG | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1; co-absent with the target |
| [[LAMA1]] | C | LAMA1 activity raises LCP1's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 2.88× lower at baseline in the lines without LAMA1 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1; co-absent with the target |
| [[MIR4280HG]] | C | MIR4280HG activity raises LCP1's level | lines that do not express MIR4280HG (21) vs lines expressing it (29) | 2.16× lower at baseline in the lines without MIR4280HG | 0.099 | ⚠ within organs, on part of the lines; also absent: EVA1A, MILR1, LNX1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD274]] | B | LCP1 activity raises CD274's level | lines that do not express LCP1 (33) vs lines expressing it (17) | 2.03× lower at baseline in the lines without LCP1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000237268, GRIN2A, ENSG00000234352 |
| [[ZFPM2-AS1]] | B | LCP1 activity raises ZFPM2-AS1's level | lines that do not express LCP1 (33) vs lines expressing it (17) | 2.82× lower at baseline in the lines without LCP1 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000237268, GRIN2A, ENSG00000234352 |
| [[LAMA1]] | C | LCP1 activity raises LAMA1's level | lines that do not express LCP1 (33) vs lines expressing it (17) | 2.49× lower at baseline in the lines without LCP1 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000237268, GRIN2A, ENSG00000234352; co-absent with the target |
| [[FRMPD4]] | C | LCP1 activity raises FRMPD4's level | lines that do not express LCP1 (33) vs lines expressing it (17) | 3.60× lower at baseline in the lines without LCP1 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000237268, GRIN2A, ENSG00000234352; co-absent with the target |
| [[PDCD1LG2]] | C | LCP1 activity raises PDCD1LG2's level | lines that do not express LCP1 (33) vs lines expressing it (17) | 2.88× lower at baseline in the lines without LCP1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000237268, GRIN2A, ENSG00000234352; co-absent with the target |
| [[PDE1C]] | C | LCP1 activity raises PDE1C's level | lines that do not express LCP1 (33) vs lines expressing it (17) | 2.61× lower at baseline in the lines without LCP1 | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000237268, GRIN2A, ENSG00000234352; co-absent with the target |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.615). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.8, 12.2); signed map (14.2, 43.9). **Vector** length 51.5, 15.2% of its response variance represented; |z| ≥ 3 in 446 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +18.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +14.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +6.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +5.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.4 | +3.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.3 | +3.7 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -5.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -1.7 | -2.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.5 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -0.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.3 | -3.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | lymphocyte cytosolic protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.13 — chr13:46,125,920-46,211,871 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PLS2, CP64, L-PLASTIN, LC64P |
| Gene groups (HGNC) | EF-hand domain containing; Plastin family |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 5 pathways, smallest: Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation; Interleukin-12 signaling; Interleukin-12 family signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P13796](https://www.uniprot.org/uniprotkb/P13796) (Plastin-2):

> Actin-binding protein. Plays a role in the activation of T-cells in response to costimulation through TCR/CD3 and CD2 or CD28. Modulates the cell surface expression of IL2RA/CD25 and CD69.

**Summary**, from NCBI Gene [3936](https://www.ncbi.nlm.nih.gov/gene/3936):

> Plastins are a family of actin-binding proteins that are conserved throughout eukaryote evolution and expressed in most tissues of higher eukaryotes. In humans, two ubiquitous plastin isoforms (L and T) have been identified. Plastin 1 (otherwise known as Fimbrin) is a third distinct plastin isoform which is specifically expressed at high levels in the small intestine. The L isoform is expressed only in hemopoietic cell lineages, while the T isoform has been found in all other normal cells of …

**Accessions** — [HGNC:6528](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6528) · Entrez [3936](https://www.ncbi.nlm.nih.gov/gene/3936) · UniProt [P13796](https://www.uniprot.org/uniprotkb/P13796) · Ensembl [ENSG00000136167](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136167)

## Data

Gene col 5830: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5830); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5830, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5830]; `tensor/DDL_lfc|DDL_z.npy` [5830]; `embed/gene_vectors.npy` [5830]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5830 or target_col == 5830). Every well: [[LCP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LCP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
