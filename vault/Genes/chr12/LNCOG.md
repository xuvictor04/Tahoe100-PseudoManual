---
symbol: "LNCOG"
type: "gene"
col: 15025
ensembl_id: "ENSG00000257219"
name: "lncRNA osteogenesis associated"
location: "12q21.2"
module: 116
arm: "+"
pooled_cpm: 2.48
n_lines_expressing: 20
n_dd_up: 31
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 14
direction_downstream: 27
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# LNCOG

*lncRNA osteogenesis associated* — 12q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 9.30× (z +14.5, q 3e-45, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 3.01× (z +10.5, q 1e-23, up in 15 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.540× (z -4.1, q 0.023, down in 7 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RDUR]] (+0.65, fdr 7e-06), [[ADTRP]] (+0.65, fdr 7e-06), [[RGS4]] (+0.63, fdr 7e-06).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[ESM1]] → it (grade C ⚠); 27 go from it, the strongest it → [[ARHGAP31]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15025.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.30×** | +14.5 | 3e-45 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **3.01×** | +10.5 | 1e-23 | 15/16 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.40×** | +10.0 | 2e-21 | 2/8 (NCI-H2347, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.63×** | +9.6 | 1e-19 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +9.2 | 3e-18 | 7/13 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.85×** | +7.1 | 1e-10 | 11/15 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.56×** | +6.4 | 2e-08 | 6/16 (SK-MEL-2, Hs 766T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **2.29×** | +5.4 | 5e-06 | 0/6 | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +5.3 | 7e-06 | 0/9 | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.18×** | +5.3 | 8e-06 | 7/16 (J82, A-172, …) | all doses, stronger at high dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.95×** | +5.2 | 9e-06 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.2 | 1e-05 | 3/17 (hTERT-HPNE, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.11×** | +5.0 | 2e-05 | 7/17 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.02×** | +4.7 | 8e-05 | 0/11 | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.96×** | +4.6 | 2e-04 | 4/16 (A-172, Hs 766T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.78×** | +3.9 | 0.004 | 6/15 (hTERT-HPNE, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.79×** | +3.8 | 0.005 | 4/15 (SNU-423, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.005 | 8/16 (SNU-423, SK-MEL-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.69×** | +3.6 | 0.010 | 2/15 (SNU-423, C32) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.69×** | +3.5 | 0.010 | 1/8 (SNU-423) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.70×** | +3.3 | 0.022 | 0/9 | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.67×** | +3.2 | 0.033 | 1/7 (hTERT-HPNE) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +3.2 | 0.033 | 6/17 (Hs 766T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.043 | 2/13 (Hs 766T, A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **1.85×** | +3.0 | 0.058 | 1/10 (SNU-423) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15025.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.540×** | -4.1 | 0.023 | 7/17 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.538×** | -3.9 | 0.024 | 7/17 (RKO, C32, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.579×** | -3.8 | 0.033 | 6/17 (LOX-IMVI, RKO, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.712× | -3.3 | 0.13 | 6/17 (NCI-H460, hTERT-HPNE, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.626× | -3.2 | 0.14 | 8/15 (RKO, J82, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.631× | -3.2 | 0.14 | 8/17 (RKO, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15025. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 49.6 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0722× (z -12.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Cobimetinib (drug)]] 0.5 µM 0.0879× (z -11.8) |
| [[Hs 766T (line)]] | wt | 8.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 21.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -9.0) |
| [[A-172 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.300 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.319 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.249 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.249 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.347 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.290 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.222 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.977 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.661 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.830 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.280 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.233 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15025), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RDUR]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 | same gene group |
| [[ADTRP]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[RGS4]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[ROBO4]] | +0.62 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[LAMA1]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[ELK3]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[TMEM156]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[SMURF2]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[DSCAM]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[DLC1]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[VEPH1]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[LINC02454]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 0, C 14. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESM1]] | C | ESM1 activity raises LNCOG's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 3.50× lower at baseline in the lines without ESM1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865; co-absent with the target |
| [[LINC01812]] | C | LINC01812 activity raises LNCOG's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 2.71× lower at baseline in the lines without LINC01812 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622; co-absent with the target |
| [[ROBO4]] | C | ROBO4 activity raises LNCOG's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.78× lower at baseline in the lines without ROBO4 | 0.004 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1; co-absent with the target |
| [[RGS4]] | C | RGS4 activity raises LNCOG's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 2.66× lower at baseline in the lines without RGS4 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486; co-absent with the target |
| [[ADTRP]] | C | ADTRP activity raises LNCOG's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 2.40× lower at baseline in the lines without ADTRP | 0.021 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2; co-absent with the target |
| [[PDCD1LG2]] | C | PDCD1LG2 activity raises LNCOG's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 2.34× lower at baseline in the lines without PDCD1LG2 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L; co-absent with the target |
| [[CCDC190]] | C | CCDC190 activity raises LNCOG's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 2.63× lower at baseline in the lines without CCDC190 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337; co-absent with the target |
| [[MIR100HG]] | C | MIR100HG activity raises LNCOG's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 2.19× lower at baseline in the lines without MIR100HG | 0.035 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2; co-absent with the target |
| [[SFTA1P]] | C | SFTA1P activity raises LNCOG's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 1.85× lower at baseline in the lines without SFTA1P | 0.043 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1; co-absent with the target |
| [[IL13RA2]] | C | IL13RA2 activity raises LNCOG's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 2.42× lower at baseline in the lines without IL13RA2 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3; co-absent with the target |
| [[RDUR]] | C | RDUR activity raises LNCOG's level | lines that do not express RDUR (28) vs lines expressing it (22) | 2.45× lower at baseline in the lines without RDUR | 0.065 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC; co-absent with the target |
| [[RPSAP52]] | C | RPSAP52 activity raises LNCOG's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 2.08× lower at baseline in the lines without RPSAP52 | 0.075 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 12, C 15. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP31]] | B | LNCOG activity raises ARHGAP31's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 3.60× lower at baseline in the lines without LNCOG | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1 |
| [[CD274]] | B | LNCOG activity raises CD274's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 2.07× lower at baseline in the lines without LNCOG | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1 |
| [[RGMB]] | B | LNCOG activity raises RGMB's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 2.04× lower at baseline in the lines without LNCOG | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1 |
| [[PALM2AKAP2]] | B | LNCOG activity raises PALM2AKAP2's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 3.23× lower at baseline in the lines without LNCOG | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1 |
| [[LINC02454]] | B | LNCOG activity raises LINC02454's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 2.27× lower at baseline in the lines without LNCOG | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1 |
| [[IPPK]] | B | LNCOG activity raises IPPK's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 1.35× lower at baseline in the lines without LNCOG | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1 |
| [[DLC1]] | B | LNCOG activity raises DLC1's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 2.43× lower at baseline in the lines without LNCOG | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1 |
| [[AMOTL1]] | B | LNCOG activity raises AMOTL1's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 3.69× lower at baseline in the lines without LNCOG | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1 |
| [[IQCJ-SCHIP1]] | B | LNCOG activity raises IQCJ-SCHIP1's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 2.69× lower at baseline in the lines without LNCOG | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1 |
| [[KBTBD8]] | B | LNCOG activity raises KBTBD8's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 1.77× lower at baseline in the lines without LNCOG | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1 |
| [[PDE4DIPP2]] | B | LNCOG activity raises PDE4DIPP2's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 2.72× lower at baseline in the lines without LNCOG | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1 |
| [[CFAP58]] | B | LNCOG activity strengthens CFAP58's drug response | lines that do not express LNCOG (25) vs lines expressing it (14) | the lines without LNCOG respond 0.71× as strongly (z diff +0.38); strongest at Doxorubicin (hydrochloride) 5 µM: 1.27x vs 4.31x (z diff +3.5) | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1; target measured in part of the lines; the reference differs; artifact flags |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.716). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.2, 11.5); signed map (15.4, 45.4). **Vector** length 46.2, 12.4% of its response variance represented; |z| ≥ 3 in 453 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +14.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +6.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.6 | +3.8 |
| fall | [[Trametinib (drug)]] 5 µM |  | -1.7 | -4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.2 | -0.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | lncRNA osteogenesis associated |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q21.2 — chr12:76,259,836-76,305,969 (+) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-54A9.1, lncRNA-OG; previously LINC02407 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53336](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53336) · Entrez [105369848](https://www.ncbi.nlm.nih.gov/gene/105369848) · Ensembl [ENSG00000257219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257219)

## Data

Gene col 15025: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15025); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15025, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15025]; `tensor/DDL_lfc|DDL_z.npy` [15025]; `embed/gene_vectors.npy` [15025]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15025 or target_col == 15025). Every well: [[LNCOG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LNCOG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
