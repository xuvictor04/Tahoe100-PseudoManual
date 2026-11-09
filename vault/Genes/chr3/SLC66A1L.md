---
symbol: "SLC66A1L"
type: "gene"
col: 10539
ensembl_id: "ENSG00000174899"
name: "solute carrier family 66 member 1 like, pseudogene"
location: "3q25.32"
module: 82
arm: "+"
pooled_cpm: 3.65
n_lines_expressing: 25
n_dd_up: 30
n_dd_down: 7
n_dd_up_clean: 20
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# SLC66A1L

*solute carrier family 66 member 1 like, pseudogene* — 3q25.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.08× (z +14.2, q 3e-43, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.15× (z +9.8, q 2e-20, up in 5 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.579× (z -5.0, q 1e-04, down in 17 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FKBP1B]] (+0.58, fdr 2e-05), [[OTX1]] (+0.58, fdr 4e-05), [[ESYT3]] (+0.57, fdr 9e-05); moves opposite to [[RFX3]] (-0.51, fdr 4e-05), [[R3HDM2]] (-0.46, fdr 3e-04), [[ASXL2]] (-0.46, fdr 3e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CARD11]] → it (grade C ⚠); 4 go from it, the strongest it → [[SARDH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10539.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.08×** | +14.2 | 3e-43 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +9.8 | 2e-20 | 5/19 (A549, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.74×** | +9.2 | 8e-18 | 2/11 (SW480, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.04×** | +9.1 | 8e-18 | 16/21 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +7.9 | 2e-13 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.02×** | +6.4 | 2e-08 | 16/20 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.64×** | +6.3 | 2e-08 | 10/21 (A498, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.83×** | +5.5 | 3e-06 | 1/9 (PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.27×** | +5.3 | 6e-06 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +4.8 | 7e-05 | 2/20 (A498, HS-578T) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.7 | 1e-04 | 0/11 | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.6 | 2e-04 | 1/21 (HOP62) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.36×** | +4.1 | 0.002 | 0/6 | rises with dose | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.09×** | +3.5 | 0.019 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.023 | 0/15 | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.68×** | +3.3 | 0.029 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.029 | 4/18 (SK-MEL-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.029 | 1/16 (A549) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.67×** | +3.3 | 0.029 | 0/17 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.43×** | +3.2 | 0.038 | 1/21 (SW480) | all doses, stronger at high dose |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.039 | 2/20 (A498, MIA PaCa-2) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.63×** | +3.2 | 0.039 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.44×** | +3.0 | 0.053 | 1/16 (SW480) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10539.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.579×** | -5.0 | 1e-04 | 17/21 (J82, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.568×** | -5.0 | 1e-04 | 14/20 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.595×** | -4.8 | 3e-04 | 16/21 (NCI-H23, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.646×** | -4.0 | 0.007 | 11/17 (SW480, A498, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.663×** | -3.8 | 0.016 | 12/21 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Malotilate (drug)]] 5 µM |  | **0.687×** | -3.5 | 0.048 | 1/21 (SW 900) | all doses, stronger at high dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.685×** | -3.4 | 0.059 | 2/21 (hTERT-HPNE, RPMI-7951) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.719× | -3.1 | 0.16 | 4/21 (HOP62, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.704× | -3.0 | 0.16 | 0/20 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10539. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 35.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -17.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -13.6) |
| [[J82 (line)]] | alt | 8.53 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0590× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.112× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 18.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -16.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -15.1) |
| [[SW480 (line)]] | alt | 3.69 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0230× (z -17.1) |
| [[CFPAC-1 (line)]] | alt | 9.06 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -13.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 5.51 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.115× (z -8.8) |
| [[HS-578T (line)]] | alt | 4.91 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0742× (z -9.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 5.29 | 0 | 1 | — | [[Darinaparsin (drug)]] 0.05 µM 0.0634× (z -8.8) |
| [[A-172 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.261 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.770 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.360 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.518 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.329 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.324 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.332 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 0.946 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.328 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.344 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10539), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP1B]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[OTX1]] | +0.58 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[ESYT3]] | +0.57 | +0.36 / +0.54 | both halves | 9e-05 |  |
| [[ETNK2]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MAP6]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[HEYL]] | +0.54 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[LHX6]] | +0.54 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[BMP8B]] | +0.53 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[RAB6B]] | +0.52 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[FXYD6]] | +0.51 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[KIF5A]] | +0.51 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[LPAR3]] | +0.51 | +0.32 / +0.62 | both halves | 2e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFX3]] | -0.51 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[R3HDM2]] | -0.46 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[ASXL2]] | -0.46 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[TSC22D1]] | -0.44 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[CUX1]] | -0.44 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[DPY19L1P1]] | -0.44 | -0.32 / -0.37 | both halves | 1e-04 |  |
| [[CLOCK]] | -0.43 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[ARID1B]] | -0.43 | -0.33 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD11]] | C | CARD11 activity raises SLC66A1L's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.30× lower at baseline in the lines without CARD11 | 0.003 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3; co-absent with the target |
| [[MAP6]] | C | MAP6 activity raises SLC66A1L's level | lines that do not express MAP6 (22) vs lines expressing it (28) | 1.52× lower at baseline in the lines without MAP6 | 0.030 | ⚠ within organs, on part of the lines; also absent: PCSK1N, ZFP28, SNAP91; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SARDH]] | B | SLC66A1L activity raises SARDH's level | lines that do not express SLC66A1L (25) vs lines expressing it (25) | 1.53× lower at baseline in the lines without SLC66A1L | 0.074 | ⚠ within organs, on part of the lines; also absent: MIR137HG, ADAMTS12, SLC8A1 |
| [[MAP6]] | C | SLC66A1L activity raises MAP6's level | lines that do not express SLC66A1L (25) vs lines expressing it (25) | 1.86× lower at baseline in the lines without SLC66A1L | 0.015 | ⚠ within organs, on part of the lines; also absent: MIR137HG, ADAMTS12, SLC8A1; co-absent with the target |
| [[CARD11]] | C | SLC66A1L activity raises CARD11's level | lines that do not express SLC66A1L (25) vs lines expressing it (25) | 2.89× lower at baseline in the lines without SLC66A1L | 0.048 | ⚠ within organs, on part of the lines; also absent: MIR137HG, ADAMTS12, SLC8A1; co-absent with the target |
| [[SLIT3]] | C | SLC66A1L activity raises SLIT3's level | lines that do not express SLC66A1L (25) vs lines expressing it (25) | 2.76× lower at baseline in the lines without SLC66A1L | 0.062 | ⚠ within organs, on part of the lines; also absent: MIR137HG, ADAMTS12, SLC8A1; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.555). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.9, 39.8); signed map (-24.8, 33.4). **Vector** length 45.1, 9.48% of its response variance represented; |z| ≥ 3 in 497 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +14.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +3.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.3 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -4.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.1 | -5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -0.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 66 member 1 like, pseudogene |
| Locus type | pseudogene |
| Location | 3q25.32 — chr3:157,569,501-157,578,466 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | ; previously C3orf55, PQLC2L, SLC66A1L |
| Gene groups (HGNC) | Solute carrier family 66; Unitary pseudogenes |
| Matched by | ensembl_id |

UniProt [A1A4F0](https://www.uniprot.org/uniprotkb/A1A4F0) carries no function annotation.

**Summary**, from NCBI Gene [152078](https://www.ncbi.nlm.nih.gov/gene/152078):

> Predicted to enable L-lysine transmembrane transporter activity. Predicted to be involved in L-lysine transmembrane transport and basic amino acid transmembrane transport. Predicted to be located in lytic vacuole membrane. Predicted to be active in lysosomal membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25146](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25146) · Entrez [152078](https://www.ncbi.nlm.nih.gov/gene/152078) · UniProt [A1A4F0](https://www.uniprot.org/uniprotkb/A1A4F0) · Ensembl [ENSG00000174899](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174899)

## Data

Gene col 10539: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10539); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10539, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10539]; `tensor/DDL_lfc|DDL_z.npy` [10539]; `embed/gene_vectors.npy` [10539]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10539 or target_col == 10539). Every well: [[SLC66A1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC66A1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
