---
symbol: "KLHL32"
type: "gene"
col: 11796
ensembl_id: "ENSG00000186231"
name: "kelch like family member 32"
location: "6q16.1"
module: 99
arm: "+"
pooled_cpm: 5.34
n_lines_expressing: 37
n_dd_up: 32
n_dd_down: 24
n_dd_up_clean: 28
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 6
direction_downstream: 9
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# KLHL32

*kelch like family member 32* — 6q16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.18× (z +22.4, q 0e+00, up in 30 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.357× (z -11.3, q 4e-27, down in 25 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPRE2]] (+0.60, fdr 2e-05), [[CA8]] (+0.59, fdr 1e-05), [[INSIG2]] (+0.57, fdr 1e-04); moves opposite to [[ATR]] (-0.55, fdr 3e-05), [[MFSD14CP-1]] (-0.54, fdr 3e-05), [[EHMT1]] (-0.53, fdr 1e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[FGF9]] → it (grade B ⚠); 9 go from it, the strongest it → [[CNGA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11796.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.18×** | +22.4 | 0e+00 | 30/32 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.28×** | +18.6 | 0e+00 | 19/28 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.59×** | +16.9 | 0e+00 | 28/34 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.26×** | +16.0 | 0e+00 | 28/33 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.39×** | +13.5 | 1e-39 | 26/30 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.12×** | +12.6 | 2e-34 | 27/33 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.05×** | +12.3 | 4e-33 | 26/33 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +7.8 | 6e-13 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.96×** | +7.5 | 5e-12 | 14/32 (C32, NCI-H460, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **3.13×** | +6.6 | 2e-09 | 18/31 (LoVo, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.78×** | +6.4 | 7e-09 | 15/32 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +5.6 | 8e-07 | 8/29 (LoVo, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.60×** | +5.0 | 2e-05 | 7/32 (SW480, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.003 | 9/29 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.012 | 8/32 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.38×** | +3.6 | 0.013 | 3/32 (NCI-H2347, A-427, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11796.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.357×** | -11.3 | 4e-27 | 25/32 (HCT15, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.373×** | -10.9 | 4e-25 | 25/34 (HCT15, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.399×** | -10.1 | 9e-22 | 21/30 (HCT15, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.477×** | -8.2 | 5e-14 | 23/32 (CFPAC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.495×** | -7.7 | 1e-12 | 18/30 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.501×** | -7.6 | 3e-12 | 16/31 (CFPAC-1, LoVo, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.515×** | -7.3 | 2e-11 | 18/24 (SHP-77, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.556×** | -6.5 | 7e-09 | 21/32 (CFPAC-1, HCT15, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.575×** | -5.8 | 3e-07 | 14/31 (SW 900, SNU-423, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.595×** | -5.7 | 7e-07 | 16/32 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.599×** | -5.6 | 9e-07 | 15/32 (NCI-H1573, SW 1271, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.706×** | -5.4 | 3e-06 | 18/32 (AsPC-1, SW 1271, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.601×** | -5.3 | 6e-06 | 19/30 (CFPAC-1, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.631×** | -5.1 | 2e-05 | 13/33 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.636×** | -5.0 | 3e-05 | 16/32 (CFPAC-1, NCI-H23, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.653×** | -4.7 | 1e-04 | 17/28 (NCI-H2030, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.498×** | -4.0 | 0.002 | 9/27 (LoVo, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.721×** | -3.4 | 0.016 | 7/33 (SHP-77, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11796. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 16.1 | 0 | 11 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0942× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 21.3 | 0 | 8 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0681× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Budesonide (drug)]] 5 µM 0.109× (z -10.2) |
| [[SHP-77 (line)]] | alt | 57.6 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -10.3) |
| [[HCT15 (line)]] | alt | 16.1 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0217× (z -14.4) |
| [[NCI-H1573 (line)]] | alt | 7.57 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0973× (z -9.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.113× (z -9.4) |
| [[SW 900 (line)]] | alt | 7.43 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0832× (z -9.3) |
| [[LS 180 (line)]] | wt | 9.97 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 4.29× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.110× (z -9.4) |
| [[A-427 (line)]] | wt | 5.20 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0828× (z -8.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 9.87 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0828× (z -8.5) |
| [[HT-29 (line)]] | alt | 4.07 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0482× (z -8.9) |
| [[LoVo (line)]] | wt | 5.19 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.85× (z +10.8) | — |
| [[NCI-H2347 (line)]] | alt | 4.86 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.03× (z +10.9) | — |
| [[SW1417 (line)]] | alt | 1.88 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 15.3× (z +9.8) | — |
| [[SW480 (line)]] | alt | 6.17 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.58× (z +11.8) | — |
| [[A-172 (line)]] | wt | 0.840 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.966 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11796), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE2]] | +0.60 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[CA8]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.57 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[MPP7]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[GPR160]] | +0.56 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[KSR2]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[PJA2]] | +0.55 | +0.34 / +0.50 | both halves | 1e-04 |  |
| [[DBP]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[PFKFB4]] | +0.54 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[CDON]] | +0.54 | +0.38 / +0.61 | both halves | 6e-05 |  |
| [[VAV1]] | +0.53 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[SUCO]] | +0.53 | +0.40 / +0.50 | both halves | 5e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATR]] | -0.55 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[MFSD14CP-1]] | -0.54 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[EHMT1]] | -0.53 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[NUTM2B-AS1]] | -0.52 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[LARS2]] | -0.50 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[TANGO6]] | -0.50 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[LETM1]] | -0.50 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[NUTM2A-AS1]] | -0.49 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[METTL8]] | -0.49 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[LRRK1]] | -0.49 | -0.27 / -0.61 | both halves | 3e-04 |  |
| [[ENOX2]] | -0.48 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[MTHFD1L]] | -0.48 | -0.53 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGF9]] | B | FGF9 activity raises KLHL32's level | lines that do not express FGF9 (31) vs lines expressing it (19) | 2.06× lower at baseline in the lines without FGF9 | 0.016 | ⚠ within organs, on part of the lines; also absent: VWA2, LINC02253, PRR15L |
| [[MPP7]] | B | MPP7 activity raises KLHL32's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 1.81× lower at baseline in the lines without MPP7 | 0.022 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[NR3C2]] | B | NR3C2 activity raises KLHL32's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.83× lower at baseline in the lines without NR3C2 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers KLHL32's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KSR2]] | B | KSR2 activity raises KLHL32's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 1.90× lower at baseline in the lines without KSR2 | 0.085 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent |
| [[F11-AS1]] | B | F11-AS1 activity raises KLHL32's level | lines that do not express F11-AS1 (34) vs lines expressing it (16) | 1.90× lower at baseline in the lines without F11-AS1 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNGA1]] | B | KLHL32 activity raises CNGA1's level | lines that do not express KLHL32 (13) vs lines expressing it (37) | 1.76× lower at baseline in the lines without KLHL32 | 0.008 | ⚠ within organs, on part of the lines; also absent: ATP8A1, ENSG00000270265, CHN2; maybe low, not absent |
| [[FHIP1A]] | B | KLHL32 activity raises FHIP1A's level | lines that do not express KLHL32 (13) vs lines expressing it (37) | 2.86× lower at baseline in the lines without KLHL32 | 0.013 | ⚠ within organs, on part of the lines; also absent: ATP8A1, ENSG00000270265, CHN2; maybe low, not absent |
| [[FBXO33]] | B | KLHL32 activity raises FBXO33's level | lines that do not express KLHL32 (13) vs lines expressing it (37) | 1.47× lower at baseline in the lines without KLHL32 | 0.036 | ⚠ within organs, on part of the lines; also absent: ATP8A1, ENSG00000270265, CHN2; maybe low, not absent |
| [[ENPP5]] | B | KLHL32 activity raises ENPP5's level | lines that do not express KLHL32 (13) vs lines expressing it (37) | 2.48× lower at baseline in the lines without KLHL32 | 0.041 | ⚠ within organs, on part of the lines; also absent: ATP8A1, ENSG00000270265, CHN2; maybe low, not absent |
| [[SFN]] | B | KLHL32 activity raises SFN's level | lines that do not express KLHL32 (13) vs lines expressing it (37) | 2.25× lower at baseline in the lines without KLHL32 | 0.053 | ⚠ within organs, on part of the lines; also absent: ATP8A1, ENSG00000270265, CHN2; maybe low, not absent |
| [[MPP7]] | B | KLHL32 activity raises MPP7's level | lines that do not express KLHL32 (13) vs lines expressing it (37) | 2.87× lower at baseline in the lines without KLHL32 | 0.064 | ⚠ within organs, on part of the lines; also absent: ATP8A1, ENSG00000270265, CHN2; maybe low, not absent |
| [[SLAIN1]] | B | KLHL32 activity raises SLAIN1's level | lines that do not express KLHL32 (13) vs lines expressing it (37) | 2.03× lower at baseline in the lines without KLHL32 | 0.065 | ⚠ within organs, on part of the lines; also absent: ATP8A1, ENSG00000270265, CHN2; maybe low, not absent |
| [[KSR2]] | B | KLHL32 activity raises KSR2's level | lines that do not express KLHL32 (13) vs lines expressing it (37) | 2.65× lower at baseline in the lines without KLHL32 | 0.079 | ⚠ within organs, on part of the lines; also absent: ATP8A1, ENSG00000270265, CHN2; maybe low, not absent |
| [[BARX2]] | B | KLHL32 activity raises BARX2's level | lines that do not express KLHL32 (13) vs lines expressing it (37) | 1.68× lower at baseline in the lines without KLHL32 | 0.091 | ⚠ within organs, on part of the lines; also absent: ATP8A1, ENSG00000270265, CHN2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.528). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.9, 34.0); signed map (32.6, 29.6). **Vector** length 75.0, 16.1% of its response variance represented; |z| ≥ 3 in 1,027 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +22.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +13.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +18.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.5 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +6.4 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -5.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -11.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -5.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 32 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.1 — chr6:96,924,620-97,140,754 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously BKLHD5, KIAA1900 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Matched by | ensembl_id |

UniProt [Q96NJ5](https://www.uniprot.org/uniprotkb/Q96NJ5) carries no function annotation.

**Summary**, from NCBI Gene [114792](https://www.ncbi.nlm.nih.gov/gene/114792):

> Predicted to enable ubiquitin-like ligase-substrate adaptor activity. Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process. Predicted to be part of Cul3-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21221](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21221) · Entrez [114792](https://www.ncbi.nlm.nih.gov/gene/114792) · UniProt [Q96NJ5](https://www.uniprot.org/uniprotkb/Q96NJ5) · Ensembl [ENSG00000186231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186231)

## Data

Gene col 11796: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11796); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11796, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11796]; `tensor/DDL_lfc|DDL_z.npy` [11796]; `embed/gene_vectors.npy` [11796]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11796 or target_col == 11796). Every well: [[KLHL32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
