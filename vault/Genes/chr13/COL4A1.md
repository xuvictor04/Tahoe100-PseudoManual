---
symbol: "COL4A1"
type: "gene"
col: 11916
ensembl_id: "ENSG00000187498"
name: "collagen type IV alpha 1 chain"
location: "13q34"
module: 66
arm: "+"
pooled_cpm: 61.48
n_lines_expressing: 21
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 23
direction_downstream: 16
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# COL4A1

*collagen type IV alpha 1 chain* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.71× (z +21.8, q 0e+00, up in 14 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.46× (z +8.9, q 7e-17, up in 8 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[5-Azacytidine (drug)]] 5 µM: 0.701× (z -5.9, q 2e-06, down in 15 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL4A2]] (+0.86, fdr 7e-06, ⚠ same locus), [[PXDN]] (+0.71, fdr 7e-06), [[ANTXR1]] (+0.67, fdr 7e-06), [[COL3A1]] (+0.66, fdr 7e-06); moves opposite to [[SMIM26]] (-0.46, fdr 6e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[SIRT7]] (-0.45, fdr 4e-04), [[ARL8A]] (-0.45, fdr 2e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[ARHGDIB]] → it (grade B ⚠); 16 go from it, the strongest it → [[PRSS23]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11916.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.71×** | +21.8 | 0e+00 | 14/18 (HOP62, A549, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.91×** | +16.4 | 0e+00 | 12/16 (HOP62, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +16.2 | 0e+00 | 13/16 (HOP62, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +8.9 | 7e-17 | 8/19 (NCI-H460, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +8.6 | 8e-16 | 6/19 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +6.6 | 4e-09 | 6/20 (HS-578T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.47×** | +6.4 | 2e-08 | 6/18 (HOP62, Panc 03.27, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.26×** | +5.4 | 5e-06 | 8/19 (Panc 03.27, CFPAC-1, …) | top dose only | composition shift |
| [[Arbutin (drug)]] 0.05 µM |  | **1.41×** | +5.3 | 9e-06 | 14/19 (SNU-423, RPMI-7951, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +4.9 | 6e-05 | 3/19 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.29×** | +4.3 | 0.001 | 9/19 (Panc 03.27, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.0 | 0.003 | 6/16 (HS-578T, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Dorzolamide (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.025 | 0/19 | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.029 | 9/19 (HS-578T, SNU-423, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.22×** | +3.3 | 0.033 | 10/19 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.41×** | +3.0 | 0.099 | 0/18 | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11916.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **0.701×** | -5.9 | 2e-06 | 15/19 (RPMI-7951, hTERT-HPNE, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.729×** | -5.2 | 5e-05 | 10/19 (H4, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.809×** | -4.9 | 2e-04 | 1/19 (C32) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.756×** | -4.6 | 5e-04 | 9/19 (hTERT-HPNE, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.756×** | -4.4 | 0.001 | 0/19 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.799×** | -3.7 | 0.020 | 14/19 (RPMI-7951, SNU-423, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.857× | -3.6 | 0.024 | 9/19 (CFPAC-1, RPMI-7951, …) | top dose only |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.791×** | -3.6 | 0.024 | 1/19 (SW 1088) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.812×** | -3.4 | 0.038 | 12/19 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.691×** | -3.2 | 0.080 | 12/18 (RPMI-7951, SW 1088, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.831× | -3.1 | 0.10 | 1/19 (CFPAC-1) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | 0.831× | -3.1 | 0.10 | 12/19 (hTERT-HPNE, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | 0.703× | -3.0 | 0.10 | 11/19 (A498, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11916. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 342 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +11.1) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.312× (z -10.2) |
| [[A549 (line)]] | wt | 52.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 169 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.99× (z +12.0) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.327× (z -9.8) |
| [[A-427 (line)]] | wt | 27.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 302 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -16.6) ⚠ cell-cycle shift, explains ~68% of this change |
| [[CHP-212 (line)]] | wt | 217 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.177× (z -9.6) |
| [[H4 (line)]] | wt | 121 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0325× (z -21.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 441 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 77.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +18.6) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[A-172 (line)]] | wt | 202 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.328× (z -10.1) |
| [[A498 (line)]] | wt | 302 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +9.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 85.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +18.0) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[J82 (line)]] | alt | 121 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.342× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 21.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +10.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 7.73 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.85 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.18 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.88 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.62 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.16 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.52 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.37 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.55 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.01 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.59 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.83 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.93 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.48 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11916), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL4A2]] | +0.86 | +0.75 / +0.91 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 999; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[PXDN]] | +0.71 | +0.60 / +0.76 | both halves | 7e-06 | pathway: Assembly of collagen fibrils and other multimeric structures; STRING 545 |
| [[ANTXR1]] | +0.67 | +0.58 / +0.64 | both halves | 7e-06 | pathway: Bacterial Infection Pathways |
| [[COL3A1]] | +0.66 | +0.69 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 856 |
| [[FN1]] | +0.62 | +0.60 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 849 |
| [[ITGA4]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 | pathway: Extracellular matrix organization; STRING 750 |
| [[COL1A2]] | +0.61 | +0.68 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 757 |
| [[VCAN]] | +0.60 | +0.61 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 448 |
| [[PDGFRB]] | +0.60 | +0.52 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 480 |
| [[TGFBI]] | +0.60 | +0.49 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 691 |
| [[DKK3]] | +0.60 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[MMP2]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 821 |
| [[NID1]] | +0.57 | +0.43 / +0.61 | both halves | 3e-05 | pathway: Degradation of the extracellular matrix; STRING 855 |

## Genes that move opposite

*4 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | -0.46 | -0.45 / -0.39 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SIRT7]] | -0.45 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[ARL8A]] | -0.45 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[NOL7]] ⚠ | -0.45 | -0.29 / -0.42 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 1, C 22. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGDIB]] | B | ARHGDIB activity raises COL4A1's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.97× lower at baseline in the lines without ARHGDIB | 0.042 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[COL4A2]] | C | COL4A2 activity raises COL4A1's level | lines that do not express COL4A2 (25) vs lines expressing it (25) | 11.77× lower at baseline in the lines without COL4A2 | 3e-04 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, ROR1-AS1; co-absent with the target |
| [[NID2]] | C | NID2 activity raises COL4A1's level | lines that do not express NID2 (32) vs lines expressing it (18) | 9.25× lower at baseline in the lines without NID2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises COL4A1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 11.08× lower at baseline in the lines without PDGFRB | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[COL7A1]] | C | COL7A1 activity raises COL4A1's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 7.42× lower at baseline in the lines without COL7A1 | 0.008 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent; co-absent with the target |
| [[MYLK]] | C | MYLK activity raises COL4A1's level | lines that do not express MYLK (20) vs lines expressing it (30) | 7.13× lower at baseline in the lines without MYLK | 0.011 | ⚠ within organs, on part of the lines; also absent: ADAMTS2, COL4A1, CPEB1; co-absent with the target |
| [[ADAMTS12]] | C | ADAMTS12 activity raises COL4A1's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 8.04× lower at baseline in the lines without ADAMTS12 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |
| [[SPARC]] | C | SPARC activity raises COL4A1's level | lines that do not express SPARC (34) vs lines expressing it (16) | 7.75× lower at baseline in the lines without SPARC | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[DKK3]] | C | DKK3 activity raises COL4A1's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 7.75× lower at baseline in the lines without DKK3 | 0.026 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; co-absent with the target |
| [[ITGA4]] | C | ITGA4 activity raises COL4A1's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 6.76× lower at baseline in the lines without ITGA4 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[VCAN]] | C | VCAN activity raises COL4A1's level | lines that do not express VCAN (28) vs lines expressing it (22) | 5.82× lower at baseline in the lines without VCAN | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01695, ITGA4, LOX; co-absent with the target |
| [[CARMN]] | C | CARMN activity raises COL4A1's level | lines that do not express CARMN (40) vs lines expressing it (10) | 8.87× lower at baseline in the lines without CARMN | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 1, C 15. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS23]] | B | COL4A1 activity raises PRSS23's level | lines that do not express COL4A1 (29) vs lines expressing it (21) | 2.43× lower at baseline in the lines without COL4A1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL4A2, NID2, ABI3BP |
| [[COL4A2]] | C | COL4A1 activity raises COL4A2's level | lines that do not express COL4A1 (29) vs lines expressing it (21) | 15.73× lower at baseline in the lines without COL4A1 | 1e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL4A2, NID2, ABI3BP; co-absent with the target |
| [[NID2]] | C | COL4A1 activity raises NID2's level | lines that do not express COL4A1 (29) vs lines expressing it (21) | 3.60× lower at baseline in the lines without COL4A1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL4A2, NID2, ABI3BP; co-absent with the target |
| [[THBS2]] | C | COL4A1 activity raises THBS2's level | lines that do not express COL4A1 (29) vs lines expressing it (21) | 4.11× lower at baseline in the lines without COL4A1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL4A2, NID2, ABI3BP; co-absent with the target |
| [[MYLK]] | C | COL4A1 activity raises MYLK's level | lines that do not express COL4A1 (29) vs lines expressing it (21) | 6.07× lower at baseline in the lines without COL4A1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL4A2, NID2, ABI3BP; co-absent with the target |
| [[COL5A1]] | C | COL4A1 activity raises COL5A1's level | lines that do not express COL4A1 (29) vs lines expressing it (21) | 9.07× lower at baseline in the lines without COL4A1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL4A2, NID2, ABI3BP; co-absent with the target |
| [[PDGFRB]] | C | COL4A1 activity raises PDGFRB's level | lines that do not express COL4A1 (29) vs lines expressing it (21) | 5.52× lower at baseline in the lines without COL4A1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL4A2, NID2, ABI3BP; co-absent with the target |
| [[ADAMTS12]] | C | COL4A1 activity raises ADAMTS12's level | lines that do not express COL4A1 (29) vs lines expressing it (21) | 4.94× lower at baseline in the lines without COL4A1 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL4A2, NID2, ABI3BP; co-absent with the target |
| [[FRMD4A]] | C | COL4A1 activity raises FRMD4A's level | lines that do not express COL4A1 (29) vs lines expressing it (21) | 4.07× lower at baseline in the lines without COL4A1 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL4A2, NID2, ABI3BP; co-absent with the target |
| [[IGFBP7]] | C | COL4A1 activity raises IGFBP7's level | lines that do not express COL4A1 (29) vs lines expressing it (21) | 5.80× lower at baseline in the lines without COL4A1 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL4A2, NID2, ABI3BP; co-absent with the target |
| [[FBN2]] | C | COL4A1 activity raises FBN2's level | lines that do not express COL4A1 (29) vs lines expressing it (21) | 3.24× lower at baseline in the lines without COL4A1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL4A2, NID2, ABI3BP; co-absent with the target |
| [[FSTL1]] | C | COL4A1 activity raises FSTL1's level | lines that do not express COL4A1 (29) vs lines expressing it (21) | 5.52× lower at baseline in the lines without COL4A1 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL4A2, NID2, ABI3BP; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (55.1, 22.4); signed map (24.9, 41.9). **Vector** length 70.1, 22.0% of its response variance represented; |z| ≥ 3 in 547 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Syndecan interactions* (reactome, mean cos +0.56 to 5); *Developmental Lineage of Pancreatic Ductal Cells* (reactome, mean cos +0.56 to 4); *Developmental Lineage of Pancreatic Endocrine Mid Progenitor Cells* (reactome, mean cos +0.56 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +21.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +16.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +16.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.5 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -5.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -3.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | collagen type IV alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:110,148,963-110,307,202 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Network forming collagens |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION, ADIPOGENESIS |
| Reactome | 27 pathways, smallest: Anchoring fibril formation; Scavenging by Class A Receptors; Crosslinking of collagen fibrils |
| Matched by | ensembl_id |

**Function**, from UniProt [P02462](https://www.uniprot.org/uniprotkb/P02462) (Collagen alpha-1(IV) chain):

> Type IV collagen is the major structural component of glomerular basement membranes (GBM), forming a 'chicken-wire' meshwork together with laminins, proteoglycans and entactin/nidogen.; Arresten, comprising the C-terminal NC1 domain, inhibits angiogenesis and tumor formation. The C-terminal half is found to possess the anti-angiogenic activity. Specifically inhibits endothelial cell proliferation, migration and tube formation.

**Summary**, from NCBI Gene [1282](https://www.ncbi.nlm.nih.gov/gene/1282):

> This gene encodes a type IV collagen alpha protein. Type IV collagen proteins are integral components of basement membranes. This gene shares a bidirectional promoter with a paralogous gene on the opposite strand. The protein consists of an amino-terminal 7S domain, a triple-helix forming collagenous domain, and a carboxy-terminal non-collagenous domain. It functions as part of a heterotrimer and interacts with other extracellular matrix components such as perlecans, proteoglycans, and …

**Accessions** — [HGNC:2202](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2202) · Entrez [1282](https://www.ncbi.nlm.nih.gov/gene/1282) · UniProt [P02462](https://www.uniprot.org/uniprotkb/P02462) · Ensembl [ENSG00000187498](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187498)

## Data

Gene col 11916: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11916); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11916, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11916]; `tensor/DDL_lfc|DDL_z.npy` [11916]; `embed/gene_vectors.npy` [11916]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11916 or target_col == 11916). Every well: [[COL4A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL4A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
