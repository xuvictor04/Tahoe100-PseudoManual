---
symbol: "HOMER3"
type: "gene"
col: 575
ensembl_id: "ENSG00000051128"
name: "homer scaffold protein 3"
location: "19p13.11"
module: 29
arm: "-"
pooled_cpm: 7.21
n_lines_expressing: 47
n_dd_up: 18
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 11
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# HOMER3

*homer scaffold protein 3* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.65× (z +10.6, q 1e-23, up in 24 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.82× (z +4.6, q 4e-04, up in 15 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.443× (z -8.9, q 2e-16, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DEF8]] (+0.64, fdr 7e-06), [[RIPOR1]] (+0.63, fdr 7e-06), [[ZDHHC1]] (+0.61, fdr 2e-05); moves opposite to [[ATP5F1B]] (-0.60, fdr 3e-05), [[IFNGR1]] (-0.56, fdr 1e-05), [[PRDX3]] (-0.55, fdr 1e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SPHK1]] → it (grade B ⚠); 11 go from it, the strongest it → [[BEND7]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 575.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.65×** | +10.6 | 1e-23 | 24/29 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +8.6 | 3e-15 | 12/14 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.77×** | +6.2 | 1e-07 | 21/34 (NCI-H2347, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +5.4 | 8e-06 | 11/19 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.61×** | +5.2 | 3e-05 | 17/39 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.57×** | +4.7 | 2e-04 | 18/42 (A-172, RKO, …) | rises with dose | composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.82×** | +4.6 | 4e-04 | 15/39 (HS-578T, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +4.3 | 0.001 | 12/42 (SW1417, A498, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.006 | 12/41 (Panc 03.27, SW480, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.31×** | +3.9 | 0.006 | 18/40 (A-172, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **1.65×** | +3.8 | 0.007 | 12/41 (Hs 766T, KATO III, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.41×** | +3.7 | 0.010 | 12/43 (SW 900, LS 180, …) | two highest doses | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.35×** | +3.3 | 0.048 | 5/43 (SNU-423, LoVo, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.048 | 9/42 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.53×** | +3.2 | 0.048 | 7/41 (LS 180, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.50×** | +3.1 | 0.071 | 4/41 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 5 µM |  | **1.71×** | +3.1 | 0.074 | 5/32 (RKO, HEC-1-A, …) | two highest doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.082 | 9/43 (LS 180, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 575.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.443×** | -8.9 | 2e-16 | 31/43 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.503×** | -7.6 | 1e-11 | 31/43 (RKO, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.556×** | -6.5 | 2e-08 | 24/43 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.585×** | -5.9 | 5e-07 | 24/43 (hTERT-HPNE, RKO, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.686×** | -4.2 | 0.004 | 9/45 (MIA PaCa-2, SW480, …) | all doses, flat | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.693×** | -3.8 | 0.013 | 12/42 (C32, SW48, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.535×** | -3.6 | 0.026 | 11/37 (Hs 766T, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.538×** | -3.6 | 0.026 | 12/43 (RKO, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 575. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.0 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +8.7) ⚠ cell-cycle shift, explains ~77% of this change | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 13.6 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -10.2) |
| [[RKO (line)]] | wt | 16.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 575), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DEF8]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[RIPOR1]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ZDHHC1]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[LCAT]] | +0.61 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[SLC31A2]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[HACD1]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ZNF641]] | +0.61 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[FBXL6]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[CDK3]] | +0.59 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[ARVCF]] | +0.59 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[SLC66A1]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[WASHC1]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5F1B]] | -0.60 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[IFNGR1]] | -0.56 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[PRDX3]] | -0.55 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[TMED4]] | -0.53 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[TUFM]] | -0.53 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[LDHB]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[MLEC]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[PDIA3]] | -0.52 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[PARP1]] | -0.52 | -0.36 / -0.58 | both halves | 9e-05 |  |
| [[UQCRC1]] ⚠ | -0.51 | -0.44 / -0.43 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PDIA6]] | -0.50 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[ADD3]] | -0.50 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[GLG1]] | -0.50 | -0.50 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPHK1]] | B | SPHK1 activity raises HOMER3's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 1.66× lower at baseline in the lines without SPHK1 | 0.024 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |
| [[HDAC6]] | B | HDAC6 activity raises HOMER3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BEND7]] | C | HOMER3 activity raises BEND7's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 5.68× lower at baseline in the lines without HOMER3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent; its own permutation p |
| [[IFNGR1]] | C | HOMER3 activity lowers IFNGR1's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 3.00× higher at baseline in the lines without HOMER3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent; its own permutation p |
| [[SLC12A4]] | C | HOMER3 activity raises SLC12A4's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 2.75× lower at baseline in the lines without HOMER3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent; its own permutation p |
| [[PCCA-DT]] | C | HOMER3 activity lowers PCCA-DT's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 2.65× higher at baseline in the lines without HOMER3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent; its own permutation p |
| [[LCAT]] | C | HOMER3 activity raises LCAT's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 1.80× lower at baseline in the lines without HOMER3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent; its own permutation p |
| [[PLEKHM2]] | C | HOMER3 activity raises PLEKHM2's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 1.55× lower at baseline in the lines without HOMER3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent; its own permutation p |
| [[TNFRSF12A]] | C | HOMER3 activity raises TNFRSF12A's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 2.07× lower at baseline in the lines without HOMER3 | 0.064 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent |
| [[LDHB]] | C | HOMER3 activity raises LDHB's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 2.49× lower at baseline in the lines without HOMER3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent; its own permutation p |
| [[SMIM29]] | C | HOMER3 activity raises SMIM29's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without HOMER3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent; its own permutation p |
| [[TJAP1]] | C | HOMER3 activity raises TJAP1's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 1.35× lower at baseline in the lines without HOMER3 | 0.091 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent |
| [[CCDC102A]] | C | HOMER3 activity raises CCDC102A's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 2.30× lower at baseline in the lines without HOMER3 | 0.098 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.464). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (24.3, -7.9); signed map (4.1, -10.3). **Vector** length 61.1, 10.6% of its response variance represented; |z| ≥ 3 in 639 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +5.9 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.5 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +3.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.4 | +3.7 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.1 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | homer scaffold protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,929,201-18,941,261 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HOMER-3 |
| Gene groups (HGNC) | Homer scaffold proteins |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NSC5](https://www.uniprot.org/uniprotkb/Q9NSC5) (Homer protein homolog 3):

> Postsynaptic density scaffolding protein. Binds and cross-links cytoplasmic regions of GRM1, GRM5, ITPR1, DNM3, RYR1, RYR2, SHANK1 and SHANK3. By physically linking GRM1 and GRM5 with ER-associated ITPR1 receptors, it aids the coupling of surface receptors to intracellular calcium release. Isoforms can be differently regulated and may play an important role in maintaining the plasticity at glutamatergic synapses. Negatively regulates T cell activation by inhibiting the calcineurin-NFAT pathway. …

**Summary**, from NCBI Gene [9454](https://www.ncbi.nlm.nih.gov/gene/9454):

> This gene encodes a member of the HOMER family of postsynaptic density scaffolding proteins that share a similar domain structure consisting of an N-terminal Enabled/vasodilator-stimulated phosphoprotein homology 1 domain which mediates protein-protein interactions, and a carboxy-terminal coiled-coil domain and two leucine zipper motifs that are involved in self-oligomerization. The encoded protein binds numerous other proteins including group I metabotropic glutamate receptors, inositol …

**Accessions** — [HGNC:17514](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17514) · Entrez [9454](https://www.ncbi.nlm.nih.gov/gene/9454) · UniProt [Q9NSC5](https://www.uniprot.org/uniprotkb/Q9NSC5) · Ensembl [ENSG00000051128](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000051128)

## Data

Gene col 575: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 575); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 575, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 575]; `tensor/DDL_lfc|DDL_z.npy` [575]; `embed/gene_vectors.npy` [575]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 575 or target_col == 575). Every well: [[HOMER3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOMER3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
