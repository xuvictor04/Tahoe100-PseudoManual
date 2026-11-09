---
symbol: "MAGI2-AS3"
type: "gene"
col: 13961
ensembl_id: "ENSG00000234456"
name: "MAGI2 antisense RNA 3"
location: "7q21.11"
module: 121
arm: "+"
pooled_cpm: 9.21
n_lines_expressing: 20
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 11
direction_downstream: 15
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# MAGI2-AS3

*MAGI2 antisense RNA 3* — 7q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.77× (z +18.6, q 0e+00, up in 12 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.483× (z -9.4, q 3e-18, down in 15 of 16 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAGI2]] (+0.77, fdr 1e-05, ⚠ same locus), [[DPY19L2]] (+0.74, fdr 7e-06), [[CACNA2D1]] (+0.70, fdr 1e-05), [[FLRT2]] (+0.69, fdr 6e-05); moves opposite to [[PCMT1]] (-0.56, fdr 1e-04), [[GTF2E2]] (-0.55, fdr 2e-04), [[TAF5L]] (-0.55, fdr 1e-04).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 15 go from it, the strongest it → [[SSPN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13961.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.77×** | +18.6 | 0e+00 | 12/15 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.51×** | +16.2 | 0e+00 | 11/13 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.24×** | +14.6 | 1e-45 | 8/11 (PANC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.21×** | +10.2 | 2e-22 | 12/16 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +9.4 | 5e-19 | 7/16 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.92×** | +7.8 | 5e-13 | 4/12 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +6.3 | 3e-08 | 11/17 (SK-MEL-2, hTERT-HPNE, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +4.8 | 1e-04 | 12/17 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +4.5 | 5e-04 | 8/16 (SNU-423, PANC-1, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.6 | 0.016 | 6/16 (SNU-423, PANC-1, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.018 | 4/16 (PANC-1, A-172, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +3.5 | 0.018 | 2/16 (HepG2/C3A, HS-578T) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pemigatinib (drug)]] 0.05 µM |  | **1.32×** | +3.4 | 0.033 | 2/16 (HS-578T, HepG2/C3A) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.3 | 0.033 | 3/12 (LOX-IMVI, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.035 | 1/16 (HOP62) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.038 | 6/17 (HepG2/C3A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.046 | 6/16 (SK-MEL-2, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.073 | 0/16 | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.076 | 1/16 (PANC-1) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.26×** | +2.9 | 0.087 | 3/16 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13961.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.483×** | -9.4 | 3e-18 | 15/16 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.497×** | -9.0 | 5e-17 | 16/16 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.509×** | -8.7 | 4e-16 | 15/17 (SNU-423, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.579×** | -7.1 | 2e-10 | 14/17 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.694×** | -4.7 | 3e-04 | 10/16 (SNU-423, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.702×** | -4.2 | 0.002 | 0/17 | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.572×** | -3.8 | 0.013 | 9/16 (SNU-423, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.750×** | -3.7 | 0.014 | 1/18 (NCI-H1792) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13961. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 31.7 | 4 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +14.1) | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -14.7) |
| [[PANC-1 (line)]] | alt | 26.9 | 5 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +16.2) | [[Panobinostat (drug)]] 5 µM 0.293× (z -11.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.294× (z -11.6) |
| [[SNU-423 (line)]] | alt | 51.6 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +28.6) | [[Panobinostat (drug)]] 5 µM 0.0710× (z -23.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.194× (z -14.3) |
| [[HOP62 (line)]] | alt | 17.9 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +13.8) | [[Panobinostat (drug)]] 0.5 µM 0.0815× (z -17.2) |
| [[hTERT-HPNE (line)]] | wt | 30.3 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.25× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.132× (z -11.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.186× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 33.9 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +11.9) | [[Panobinostat (drug)]] 0.5 µM 0.192× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 28.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0896× (z -16.3) |
| [[C32 (line)]] | wt | 72.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -16.6) |
| [[NCI-H1792 (line)]] | alt | 36.7 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0835× (z -19.5) |
| [[A-172 (line)]] | wt | 3.60 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.2× (z +14.6) | — |
| [[HepG2_C3A (line)]] | wt | 38.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +12.8) | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 17.1 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.135× (z -12.6) |
| [[H4 (line)]] | wt | 7.81 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0581× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 14.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +9.2) | — |
| [[A-427 (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.660 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.792 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.715 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.756 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.935 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.696 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.694 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.678 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.623 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.767 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.844 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.977 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.964 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.668 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13961), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGI2]] | +0.77 | +0.85 / +0.52 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[DPY19L2]] | +0.74 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[CACNA2D1]] | +0.70 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[FLRT2]] | +0.69 | +0.75 / +0.38 | both halves | 6e-05 |  |
| [[ANKRD18B]] | +0.68 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[FAP]] | +0.66 | +0.70 / +0.34 | both halves | 1e-04 |  |
| [[ZIC1]] | +0.66 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[ARNT2-DT]] | +0.65 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[SUCLG2-DT]] | +0.64 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[C7orf31]] | +0.64 | +0.54 / +0.39 | both halves | 6e-05 |  |
| [[MIR548XHG]] | +0.63 | +0.64 / +0.35 | both halves | 1e-04 |  |
| [[PLS3-AS1]] | +0.63 | +0.53 / +0.35 | both halves | 1e-04 | same gene group |
| [[LINC00383]] | +0.63 | +0.54 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCMT1]] | -0.56 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[GTF2E2]] | -0.55 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[TAF5L]] | -0.55 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[SPTLC2]] | -0.54 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[RALGPS1]] | -0.54 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[COG5]] | -0.54 | -0.44 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MAGI2-AS3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HOXD3]] | B | HOXD3 activity raises MAGI2-AS3's level | lines that do not express HOXD3 (17) vs lines expressing it (33) | 1.60× lower at baseline in the lines without HOXD3 | 0.088 | ⚠ within organs, on part of the lines; also absent: PPFIA2, SCN8A, FGF14 |
| [[MAGI2]] | C | MAGI2 activity raises MAGI2-AS3's level | lines that do not express MAGI2 (30) vs lines expressing it (20) | 9.02× lower at baseline in the lines without MAGI2 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGI2-AS3, MMP2, PHACTR1; co-absent with the target |
| [[PHACTR1]] | C | PHACTR1 activity raises MAGI2-AS3's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 5.73× lower at baseline in the lines without PHACTR1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L; co-absent with the target |
| [[GYPC]] | C | GYPC activity raises MAGI2-AS3's level | lines that do not express GYPC (35) vs lines expressing it (15) | 4.98× lower at baseline in the lines without GYPC | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4; co-absent with the target |
| [[DPY19L2]] | C | DPY19L2 activity raises MAGI2-AS3's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 4.31× lower at baseline in the lines without DPY19L2 | 0.038 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ; co-absent with the target |
| [[ZNF626]] | C | ZNF626 activity raises MAGI2-AS3's level | lines that do not express ZNF626 (28) vs lines expressing it (22) | 3.18× lower at baseline in the lines without ZNF626 | 0.044 | ⚠ within organs, on part of the lines; also absent: ROS1, GDNF, HTRA3; co-absent with the target |
| [[IRAG2]] | C | IRAG2 activity raises MAGI2-AS3's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 3.07× lower at baseline in the lines without IRAG2 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411; co-absent with the target |
| [[JAM2]] | C | JAM2 activity raises MAGI2-AS3's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 3.65× lower at baseline in the lines without JAM2 | 0.066 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R; co-absent with the target |
| [[ANGPT1]] | C | ANGPT1 activity raises MAGI2-AS3's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 3.10× lower at baseline in the lines without ANGPT1 | 0.077 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5; co-absent with the target |
| [[MSC]] | C | MSC activity raises MAGI2-AS3's level | lines that do not express MSC (34) vs lines expressing it (16) | 4.92× lower at baseline in the lines without MSC | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 3, C 12. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSPN]] | B | MAGI2-AS3 activity raises SSPN's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 2.82× lower at baseline in the lines without MAGI2-AS3 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC |
| [[NEXN]] | B | MAGI2-AS3 activity raises NEXN's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 1.83× lower at baseline in the lines without MAGI2-AS3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC |
| [[DPY19L2P2]] | B | MAGI2-AS3 activity raises DPY19L2P2's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 1.85× lower at baseline in the lines without MAGI2-AS3 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC |
| [[MAGI2]] | C | MAGI2-AS3 activity raises MAGI2's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 12.91× lower at baseline in the lines without MAGI2-AS3 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC; co-absent with the target |
| [[DPY19L2]] | C | MAGI2-AS3 activity raises DPY19L2's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 3.59× lower at baseline in the lines without MAGI2-AS3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC; co-absent with the target |
| [[COL12A1]] | C | MAGI2-AS3 activity raises COL12A1's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 4.95× lower at baseline in the lines without MAGI2-AS3 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC; co-absent with the target |
| [[PHACTR1]] | C | MAGI2-AS3 activity raises PHACTR1's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 3.16× lower at baseline in the lines without MAGI2-AS3 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC; co-absent with the target |
| [[JAM2]] | C | MAGI2-AS3 activity raises JAM2's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 3.97× lower at baseline in the lines without MAGI2-AS3 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC; co-absent with the target |
| [[COL11A1]] | C | MAGI2-AS3 activity raises COL11A1's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 4.03× lower at baseline in the lines without MAGI2-AS3 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC; co-absent with the target |
| [[LINC00383]] | C | MAGI2-AS3 activity raises LINC00383's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 1.64× lower at baseline in the lines without MAGI2-AS3 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC; co-absent with the target |
| [[TWIST1]] | C | MAGI2-AS3 activity raises TWIST1's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 4.98× lower at baseline in the lines without MAGI2-AS3 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC; co-absent with the target |
| [[DNAH11]] | C | MAGI2-AS3 activity raises DNAH11's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 3.46× lower at baseline in the lines without MAGI2-AS3 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.769). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.2, 25.0); signed map (43.8, 25.6). **Vector** length 57.4, 17.4% of its response variance represented; |z| ≥ 3 in 382 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +16.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +14.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +18.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +1.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.8 | -9.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.5 | -9.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.4 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | MAGI2 antisense RNA 3 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q21.11 — chr7:79,452,877-79,471,208 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ENST00000414797 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40862) · Entrez [100505881](https://www.ncbi.nlm.nih.gov/gene/100505881) · Ensembl [ENSG00000234456](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234456)

## Data

Gene col 13961: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13961); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13961, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13961]; `tensor/DDL_lfc|DDL_z.npy` [13961]; `embed/gene_vectors.npy` [13961]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13961 or target_col == 13961). Every well: [[MAGI2-AS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAGI2-AS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
