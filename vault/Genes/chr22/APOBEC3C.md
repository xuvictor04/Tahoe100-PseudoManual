---
symbol: "APOBEC3C"
type: "gene"
col: 14407
ensembl_id: "ENSG00000244509"
name: "apolipoprotein B mRNA editing enzyme catalytic subunit 3C"
location: "22q13.1"
module: 62
arm: "+"
pooled_cpm: 15.87
n_lines_expressing: 45
n_dd_up: 8
n_dd_down: 30
n_dd_up_clean: 3
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# APOBEC3C

*apolipoprotein B mRNA editing enzyme catalytic subunit 3C* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.72× (z +12.2, q 1e-31, up in 30 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.61× (z +8.3, q 2e-14, up in 29 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.428× (z -14.7, q 0e+00, down in 36 of 42 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRM2B]] (+0.67, fdr 5e-05), [[EI24]] (+0.63, fdr 1e-05), [[ACTA2]] (+0.63, fdr 1e-04); moves opposite to [[EIF5B]] (-0.52, fdr 2e-05), [[ZDHHC18]] (-0.45, fdr 2e-04), [[PILRB]] (-0.45, fdr 5e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ACTA2]] → it (grade B ⚠); 3 go from it, the strongest it → [[AMZ2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14407.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.72×** | +12.2 | 1e-31 | 30/34 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +11.2 | 2e-26 | 20/25 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +8.3 | 2e-14 | 29/43 (A498, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +6.7 | 3e-09 | 17/29 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.39×** | +4.1 | 0.005 | 13/43 (A-172, A549, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.37×** | +3.9 | 0.010 | 17/42 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.066 | 14/42 (A549, RKO, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +3.2 | 0.085 | 12/39 (CFPAC-1, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14407.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.428×** | -14.7 | 0e+00 | 36/42 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.358×** | -12.5 | 1e-33 | 29/41 (Hs 766T, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.490×** | -8.7 | 6e-16 | 35/43 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.526×** | -7.9 | 6e-13 | 31/43 (COLO 205, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.540×** | -7.5 | 6e-12 | 27/43 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.559×** | -7.1 | 1e-10 | 29/41 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.546×** | -7.0 | 3e-10 | 28/42 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.555×** | -6.9 | 3e-10 | 29/42 (Panc 03.27, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.595×** | -6.3 | 1e-08 | 25/42 (PANC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.613×** | -6.0 | 1e-07 | 24/40 (HCT15, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.620×** | -5.8 | 3e-07 | 28/41 (LS 180, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.637×** | -5.5 | 2e-06 | 25/43 (A-172, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.645×** | -5.3 | 4e-06 | 26/42 (SW480, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.654×** | -5.2 | 9e-06 | 22/43 (HCT15, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.655×** | -5.2 | 9e-06 | 24/41 (SNU-423, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.680×** | -4.7 | 9e-05 | 24/43 (SW 1088, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14407. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 22.3 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.92× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -12.5) |
| [[SW480 (line)]] | alt | 25.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.72× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -14.1) |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0340× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 9.14 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -9.5) |
| [[PANC-1 (line)]] | alt | 8.78 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -10.7) |
| [[HOP62 (line)]] | alt | 15.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0730× (z -20.2) |
| [[Hs 766T (line)]] | wt | 47.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -13.6) |
| [[J82 (line)]] | alt | 12.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.64× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -9.1) |
| [[LS 180 (line)]] | wt | 23.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 23.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.68× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.128× (z -10.9) |
| [[SW1417 (line)]] | alt | 22.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -11.0) |
| [[A-172 (line)]] | wt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.274× (z -8.7) |
| [[A498 (line)]] | wt | 24.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +8.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 19.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -9.9) |
| [[H4 (line)]] | wt | 32.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -12.8) |
| [[HS-578T (line)]] | alt | 28.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -9.5) |
| [[LoVo (line)]] | wt | 11.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.218× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 14.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.88× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -8.9) |
| [[RKO (line)]] | wt | 18.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 5.88× (z +9.0) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[RPMI-7951 (line)]] | alt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -9.6) |
| [[SHP-77 (line)]] | alt | 7.06 | 0 | 1 | — | [[Megestrol (drug)]] 0.5 µM 0.0759× (z -9.9) |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -10.4) |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -9.1) |
| [[A-427 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14407), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRM2B]] | +0.67 | +0.40 / +0.74 | both halves | 5e-05 |  |
| [[EI24]] | +0.63 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[ACTA2]] | +0.63 | +0.35 / +0.71 | both halves | 1e-04 |  |
| [[ZMAT3]] | +0.60 | +0.32 / +0.65 | both halves | 2e-04 |  |
| [[ITM2B]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PINCR]] | +0.59 | +0.38 / +0.62 | both halves | 6e-05 |  |
| [[DSC3]] | +0.59 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[FAS]] | +0.59 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[PHLDA3]] | +0.58 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[GRIN2C]] | +0.58 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[FDXR]] | +0.58 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[PURPL]] | +0.58 | +0.33 / +0.62 | both halves | 1e-04 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF5B]] | -0.52 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[ZDHHC18]] | -0.45 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[PILRB]] | -0.45 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[SPIRE1]] | -0.44 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[MPP3]] | -0.44 | -0.28 / -0.38 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACTA2]] | B | ACTA2 activity raises APOBEC3C's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 2.48× lower at baseline in the lines without ACTA2 | 0.034 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[DSC3]] | B | DSC3 activity raises APOBEC3C's level | lines that do not express DSC3 (31) vs lines expressing it (19) | 1.56× lower at baseline in the lines without DSC3 | 0.054 | ⚠ within organs, on part of the lines; also absent: TFF2, VGLL3, MUC16 |
| [[ANK1]] | B | ANK1 activity raises APOBEC3C's level | lines that do not express ANK1 (22) vs lines expressing it (28) | 1.91× lower at baseline in the lines without ANK1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LHX1, GPR173; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AMZ2]] | B | APOBEC3C activity raises AMZ2's level | lines that do not express APOBEC3C (5) vs lines expressing it (45) | 1.64× lower at baseline in the lines without APOBEC3C | 0.047 | ⚠ within organs, on part of the lines; also absent: MIR181A2HG, CRTAP |
| [[RBBP9]] | B | APOBEC3C activity raises RBBP9's level | lines that do not express APOBEC3C (5) vs lines expressing it (45) | 1.42× lower at baseline in the lines without APOBEC3C | 0.056 | ⚠ within organs, on part of the lines; also absent: MIR181A2HG, CRTAP |
| [[CCNG1]] | B | APOBEC3C activity raises CCNG1's level | lines that do not express APOBEC3C (5) vs lines expressing it (45) | 1.67× lower at baseline in the lines without APOBEC3C | 0.097 | ⚠ within organs, on part of the lines; also absent: MIR181A2HG, CRTAP |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.652). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.7, 34.9); signed map (42.8, -25.3). **Vector** length 100, 24.3% of its response variance represented; |z| ≥ 3 in 1,136 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.50 to 6); *apoptosis* (hallmark, mean cos +0.50 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +11.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.8 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +12.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +5.6 | +0.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +1.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.0 | -0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | -0.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.4 | -14.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -12.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.8 | -7.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.6 | -5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -4.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -4.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | apolipoprotein B mRNA editing enzyme catalytic subunit 3C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:39,014,257-39,020,352 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APOBEC1L, PBI, bK150C2.3, ARDC2, ARDC4, ARP5 |
| Gene groups (HGNC) | Apolipoprotein B mRNA editing enzyme catalytic subunits |
| Reactome | 4 pathways, smallest: Formation of the Editosome; mRNA Editing: C to U Conversion; mRNA Editing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRW3](https://www.uniprot.org/uniprotkb/Q9NRW3) (DNA dC->dU-editing enzyme APOBEC-3C):

> DNA deaminase (cytidine deaminase) which acts as an inhibitor of retrovirus replication and retrotransposon mobility via deaminase-dependent and -independent mechanisms. After the penetration of retroviral nucleocapsids into target cells of infection and the initiation of reverse transcription, it can induce the conversion of cytosine to uracil in the minus-sense single-strand viral DNA, leading to G-to-A hypermutations in the subsequent plus-strand viral DNA. The resultant detrimental levels …

**Summary**, from NCBI Gene [27350](https://www.ncbi.nlm.nih.gov/gene/27350):

> This gene is a member of the cytidine deaminase gene family. It is one of seven related genes or pseudogenes found in a cluster thought to result from gene duplication, on chromosome 22. Members of the cluster encode proteins that are structurally and functionally related to the C to U RNA-editing cytidine deaminase APOBEC1. It is thought that the proteins may be RNA editing enzymes and have roles in growth or cell cycle control. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17353](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17353) · Entrez [27350](https://www.ncbi.nlm.nih.gov/gene/27350) · UniProt [Q9NRW3](https://www.uniprot.org/uniprotkb/Q9NRW3) · Ensembl [ENSG00000244509](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244509)

## Data

Gene col 14407: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14407); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14407, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14407]; `tensor/DDL_lfc|DDL_z.npy` [14407]; `embed/gene_vectors.npy` [14407]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14407 or target_col == 14407). Every well: [[APOBEC3C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APOBEC3C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
