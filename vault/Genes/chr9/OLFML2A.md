---
symbol: "OLFML2A"
type: "gene"
col: 11699
ensembl_id: "ENSG00000185585"
name: "olfactomedin like 2A"
location: "9q33.3"
module: 66
arm: "+"
pooled_cpm: 10.52
n_lines_expressing: 30
n_dd_up: 48
n_dd_down: 15
n_dd_up_clean: 42
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 10
direction_downstream: 8
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# OLFML2A

*olfactomedin like 2A* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 48 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.03× (z +16.8, q 0e+00, up in 11 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.51× (z +14.1, q 8e-43, up in 25 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.504× (z -7.4, q 6e-11, down in 20 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MXRA8]] (+0.70, fdr 1e-05), [[COL3A1]] (+0.65, fdr 1e-05), [[EFEMP1]] (+0.62, fdr 1e-05); moves opposite to [[TTC4]] (-0.52, fdr 2e-05), [[DCLRE1C]] (-0.51, fdr 3e-05), [[ADRM1]] (-0.49, fdr 9e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[COL3A1]] → it (grade B ⚠); 8 go from it, the strongest it → [[CCDC3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 48 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11699.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.03×** | +16.8 | 0e+00 | 11/11 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.33×** | +15.9 | 0e+00 | 16/20 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.51×** | +14.1 | 8e-43 | 25/28 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +13.7 | 1e-40 | 15/25 (A549, A-172, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.42×** | +12.3 | 7e-33 | 10/12 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.21×** | +8.6 | 1e-15 | 18/28 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.84×** | +7.8 | 5e-13 | 13/27 (NCI-H460, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +7.0 | 2e-10 | 14/28 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +6.9 | 2e-10 | 13/27 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.84×** | +6.3 | 1e-08 | 11/26 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.79×** | +6.2 | 3e-08 | 12/28 (NCI-H460, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +5.9 | 1e-07 | 11/28 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.59×** | +5.7 | 5e-07 | 11/28 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.74×** | +5.7 | 6e-07 | 14/26 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.54×** | +5.5 | 2e-06 | 10/27 (NCI-H460, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.45×** | +5.5 | 2e-06 | 8/28 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.62×** | +5.2 | 7e-06 | 12/27 (PANC-1, J82, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.38×** | +4.9 | 4e-05 | 12/28 (NCI-H460, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11699.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.504×** | -7.4 | 6e-11 | 20/24 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.555×** | -6.0 | 5e-07 | 14/26 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.602×** | -5.5 | 6e-06 | 16/27 (Panc 03.27, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.593×** | -5.5 | 7e-06 | 15/27 (SW 900, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.617×** | -5.3 | 2e-05 | 12/27 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.617×** | -5.2 | 2e-05 | 15/26 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.642×** | -4.8 | 1e-04 | 13/27 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.654×** | -4.6 | 3e-04 | 9/27 (NCI-H460, CHP-212, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.752×** | -4.4 | 7e-04 | 12/25 (RPMI-7951, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mebendazole (drug)]] 5 µM |  | **0.712×** | -3.5 | 0.022 | 3/27 (MIA PaCa-2, NCI-H23, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.725×** | -3.5 | 0.024 | 11/25 (HS-578T, NCI-H460, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.736×** | -3.3 | 0.038 | 8/28 (NCI-H2030, NCI-H23, …) | rises with dose | position effect removed |
| [[Retinoic acid (drug)]] 5 µM |  | **0.806×** | -3.3 | 0.038 | 11/28 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **0.738×** | -3.3 | 0.038 | 6/27 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.587×** | -3.0 | 0.092 | 4/25 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11699. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 102 | 1 | 4 | [[Trametinib (drug)]] 0.05 µM 3.80× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -11.8) |
| [[PANC-1 (line)]] | alt | 15.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.05× (z +10.9) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.227× (z -10.1) |
| [[SNU-423 (line)]] | alt | 38.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 5.76 | 0 | 2 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0789× (z -8.9) |
| [[SW480 (line)]] | alt | 3.89 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 5.17× (z +10.4) | [[Harringtonine (drug)]] 0.5 µM 0.121× (z -9.6) |
| [[A-172 (line)]] | wt | 8.62 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.81× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 7.73 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.15× (z +8.5) | — |
| [[J82 (line)]] | alt | 5.11 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.85× (z +8.8) | — |
| [[LoVo (line)]] | wt | 6.26 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0391× (z -14.7) |
| [[NCI-H2030 (line)]] | alt | 3.38 | 0 | 1 | — | [[5-Azacytidine (drug)]] 5 µM 0.0763× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 42.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -12.6) |
| [[A-427 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.887 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.63 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.925 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.981 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.15 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11699), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXRA8]] | +0.70 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[COL3A1]] | +0.65 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[EFEMP1]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[CLSTN1]] | +0.60 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[NID2]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[FKBP7]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[GXYLT2]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[MYL9]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[COL5A2]] | +0.59 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[POSTN]] | +0.58 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[NPTXR]] | +0.56 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[MMP2]] | +0.56 | +0.46 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC4]] | -0.52 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[DCLRE1C]] | -0.51 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[ADRM1]] | -0.49 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[PRKAG1]] | -0.48 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[CCDC137]] | -0.48 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[ZNG1F]] | -0.48 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[TATDN1]] | -0.47 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[ZNF778]] | -0.46 | -0.44 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL3A1]] | B | COL3A1 activity raises OLFML2A's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 2.69× lower at baseline in the lines without COL3A1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677 |
| [[COL5A2]] | B | COL5A2 activity raises OLFML2A's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 2.60× lower at baseline in the lines without COL5A2 | 0.041 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2 |
| [[EML1]] | B | EML1 activity raises OLFML2A's level | lines that do not express EML1 (13) vs lines expressing it (37) | 2.70× lower at baseline in the lines without EML1 | 0.049 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FGF2, PYGO1 |
| [[NID2]] | B | NID2 activity raises OLFML2A's level | lines that do not express NID2 (32) vs lines expressing it (18) | 2.42× lower at baseline in the lines without NID2 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1 |
| [[BCAM]] | B | BCAM activity raises OLFML2A's level | lines that do not express BCAM (8) vs lines expressing it (42) | 2.31× lower at baseline in the lines without BCAM | 0.058 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[SMIM10]] | B | SMIM10 activity raises OLFML2A's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 2.25× lower at baseline in the lines without SMIM10 | 0.087 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[ATP6V0E2]] | B | ATP6V0E2 activity raises OLFML2A's level | lines that do not express ATP6V0E2 (5) vs lines expressing it (45) | 2.40× lower at baseline in the lines without ATP6V0E2 | 0.091 | ⚠ within organs, on part of the lines; also absent: CDON, ODAD4 |
| [[FBLN1]] | B | FBLN1 activity raises OLFML2A's level | lines that do not express FBLN1 (20) vs lines expressing it (30) | 2.23× lower at baseline in the lines without FBLN1 | 0.092 | ⚠ within organs, on part of the lines; also absent: GJA1, PCSK1N, MLLT11 |
| [[HTRA1]] | B | HTRA1 activity raises OLFML2A's level | lines that do not express HTRA1 (19) vs lines expressing it (31) | 1.85× lower at baseline in the lines without HTRA1 | 0.098 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1 |
| [[EFEMP1]] | C | EFEMP1 activity raises OLFML2A's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 2.11× lower at baseline in the lines without EFEMP1 | 0.082 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC3]] | B | OLFML2A activity raises CCDC3's level | lines that do not express OLFML2A (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without OLFML2A | 0.003 | ⚠ within organs, on part of the lines; also absent: GBX1, FMNL1-DT, SCN5A |
| [[DOC2A]] | B | OLFML2A activity raises DOC2A's level | lines that do not express OLFML2A (20) vs lines expressing it (30) | 1.70× lower at baseline in the lines without OLFML2A | 0.041 | ⚠ within organs, on part of the lines; also absent: GBX1, FMNL1-DT, SCN5A |
| [[LINC00173]] | B | OLFML2A activity raises LINC00173's level | lines that do not express OLFML2A (20) vs lines expressing it (30) | 1.96× lower at baseline in the lines without OLFML2A | 0.043 | ⚠ within organs, on part of the lines; also absent: GBX1, FMNL1-DT, SCN5A |
| [[EML1]] | B | OLFML2A activity raises EML1's level | lines that do not express OLFML2A (20) vs lines expressing it (30) | 2.54× lower at baseline in the lines without OLFML2A | 0.048 | ⚠ within organs, on part of the lines; also absent: GBX1, FMNL1-DT, SCN5A |
| [[MYLK]] | B | OLFML2A activity raises MYLK's level | lines that do not express OLFML2A (20) vs lines expressing it (30) | 2.81× lower at baseline in the lines without OLFML2A | 0.058 | ⚠ within organs, on part of the lines; also absent: GBX1, FMNL1-DT, SCN5A |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM | B | OLFML2A activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 0.5 µM (protects the cells) | lines that do not express OLFML2A (20) vs lines expressing it (28) | the lines without OLFML2A: 0.86× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: GBX1, FMNL1-DT, SCN5A |
| [[CTSZ]] | B | OLFML2A activity raises CTSZ's level | lines that do not express OLFML2A (20) vs lines expressing it (30) | 1.37× lower at baseline in the lines without OLFML2A | 0.082 | ⚠ within organs, on part of the lines; also absent: GBX1, FMNL1-DT, SCN5A |
| [[EFEMP1]] | C | OLFML2A activity raises EFEMP1's level | lines that do not express OLFML2A (20) vs lines expressing it (30) | 2.90× lower at baseline in the lines without OLFML2A | 0.022 | ⚠ within organs, on part of the lines; also absent: GBX1, FMNL1-DT, SCN5A; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (56.9, 22.7); signed map (43.8, 22.3). **Vector** length 67.6, 15.5% of its response variance represented; |z| ≥ 3 in 757 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Fibronectin matrix formation* (reactome, mean cos +0.51 to 6); *Collagen chain trimerization* (reactome, mean cos +0.51 to 7); *Collagen degradation* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +15.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +16.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +12.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +8.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +7.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.5 | +6.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.4 | +6.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +4.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -7.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.3 | -6.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -4.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | olfactomedin like 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:124,777,133-124,814,885 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00237 |
| Gene groups (HGNC) | Olfactomedin domain containing |
| Matched by | ensembl_id |

UniProt [Q68BL7](https://www.uniprot.org/uniprotkb/Q68BL7) carries no function annotation.

**Summary**, from NCBI Gene [169611](https://www.ncbi.nlm.nih.gov/gene/169611):

> Predicted to enable extracellular matrix binding activity and identical protein binding activity. Predicted to be involved in signal transduction. Predicted to act upstream of or within extracellular matrix organization. Predicted to be located in extracellular matrix. Predicted to be active in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27270](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27270) · Entrez [169611](https://www.ncbi.nlm.nih.gov/gene/169611) · UniProt [Q68BL7](https://www.uniprot.org/uniprotkb/Q68BL7) · Ensembl [ENSG00000185585](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185585)

## Data

Gene col 11699: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11699); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11699, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11699]; `tensor/DDL_lfc|DDL_z.npy` [11699]; `embed/gene_vectors.npy` [11699]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11699 or target_col == 11699). Every well: [[OLFML2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OLFML2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
