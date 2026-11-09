---
symbol: "CTSO"
type: "gene"
col: 14970
ensembl_id: "ENSG00000256043"
name: "cathepsin O"
location: "4q32.1"
module: 70
arm: "+"
pooled_cpm: 6.46
n_lines_expressing: 42
n_dd_up: 14
n_dd_down: 22
n_dd_up_clean: 11
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 11
direction_downstream: 15
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# CTSO

*cathepsin O* — 4q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.00× (z +6.5, q 5e-08, up in 12 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 0.5 µM: 1.74× (z +5.2, q 4e-05, up in 20 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.206× (z -14.8, q 0e+00, down in 37 of 39 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERAP1]] (+0.74, fdr 1e-05), [[ANXA2R-AS1]] (+0.69, fdr 6e-05), [[TAPBP]] (+0.66, fdr 1e-05); moves opposite to [[ZFYVE28]] (-0.68, fdr 2e-05), [[PPP2R2C]] (-0.59, fdr 3e-05), [[ANKRD27]] (-0.57, fdr 2e-04).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[GBP4]] → it (grade B ⚠); 15 go from it, the strongest it → [[TAPBP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14970.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +6.5 | 5e-08 | 12/22 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +6.4 | 5e-08 | 10/14 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.74×** | +5.2 | 4e-05 | 20/37 (LoVo, HOP62, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.74×** | +5.0 | 1e-04 | 16/33 (LoVo, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.54×** | +4.9 | 1e-04 | 16/38 (LoVo, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.44×** | +4.7 | 2e-04 | 12/39 (CFPAC-1, NCI-H460, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.50×** | +4.6 | 3e-04 | 18/38 (LoVo, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.63×** | +4.4 | 8e-04 | 17/37 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.57×** | +4.2 | 0.002 | 11/40 (CFPAC-1, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.60×** | +4.2 | 0.002 | 12/37 (CFPAC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.37×** | +4.1 | 0.002 | 14/39 (LoVo, Panc 03.27, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.045 | 5/40 (LoVo, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.62×** | +3.2 | 0.052 | 5/36 (HEC-1-A, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.34×** | +3.1 | 0.083 | 10/40 (LoVo, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14970.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.206×** | -14.8 | 0e+00 | 37/39 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.248×** | -13.1 | 2e-36 | 37/39 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.260×** | -12.6 | 2e-34 | 38/40 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.453×** | -10.5 | 1e-23 | 23/31 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.350×** | -9.8 | 9e-21 | 31/39 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.396×** | -8.7 | 4e-16 | 29/37 (BT-474, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.398×** | -8.6 | 5e-16 | 34/40 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.405×** | -8.5 | 2e-15 | 28/31 (SNU-423, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.430×** | -7.5 | 5e-12 | 25/36 (RPMI-7951, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.677×** | -5.2 | 1e-05 | 19/38 (A-172, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.575×** | -5.0 | 3e-05 | 17/36 (NCI-H1573, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~23% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.602×** | -4.8 | 9e-05 | 16/39 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.622×** | -4.5 | 4e-04 | 17/33 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.411×** | -4.4 | 5e-04 | 17/35 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.647×** | -4.1 | 0.002 | 14/35 (HT-29, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.678×** | -3.7 | 0.008 | 11/38 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14970. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 6.54 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0567× (z -20.1) |
| [[HT-29 (line)]] | alt | 4.93 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0401× (z -11.2) |
| [[LoVo (line)]] | wt | 7.22 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0904× (z -11.7) |
| [[A-172 (line)]] | wt | 22.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -10.0) |
| [[A498 (line)]] | wt | 23.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 9.71 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0805× (z -11.0) |
| [[PANC-1 (line)]] | alt | 4.75 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -12.1) |
| [[BT-474 (line)]] | alt | 6.13 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0586× (z -9.5) |
| [[C32 (line)]] | wt | 10.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.103× (z -9.9) |
| [[H4 (line)]] | wt | 7.56 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0645× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 9.65 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -9.3) |
| [[HS-578T (line)]] | alt | 6.12 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0773× (z -8.6) |
| [[J82 (line)]] | alt | 4.57 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.106× (z -8.5) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 12.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.224× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 4.00 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0559× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 7.98 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -9.8) |
| [[SNU-423 (line)]] | alt | 5.99 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0620× (z -10.1) |
| [[SW 900 (line)]] | alt | 7.41 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0734× (z -9.9) |
| [[A-427 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.896 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.598 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.995 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.620 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14970), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERAP1]] | +0.74 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[ANXA2R-AS1]] | +0.69 | +0.55 / +0.38 | both halves | 6e-05 |  |
| [[TAPBP]] | +0.66 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[IDO1]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[C5orf15]] | +0.63 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[CFH]] | +0.63 | +0.55 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_COAGULATION |
| [[GBP1]] | +0.63 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[SCAMP1-AS1]] | +0.63 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[PDIA3P1]] | +0.62 | +0.57 / +0.31 | both halves | 2e-04 |  |
| [[TLR3]] | +0.62 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[DECR1]] | +0.62 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[CASD1]] | +0.61 | +0.45 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE28]] | -0.68 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[PPP2R2C]] | -0.59 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[ANKRD27]] | -0.57 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[CARMIL2]] | -0.56 | -0.46 / -0.26 | both halves | 4e-04 |  |
| [[EIF4EBP1]] | -0.56 | -0.37 / -0.29 | both halves | 2e-04 |  |
| [[HK1]] | -0.56 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[LRRFIP1]] | -0.55 | -0.45 / -0.27 | both halves | 3e-04 |  |
| [[PBX4]] | -0.55 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[SPTLC2]] | -0.55 | -0.35 / -0.30 | both halves | 2e-04 |  |
| [[ERGIC1]] | -0.55 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[MAPT]] | -0.54 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[FLNB]] | -0.54 | -0.41 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP4]] | B | GBP4 activity raises CTSO's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.04× lower at baseline in the lines without GBP4 | 0.023 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers CTSO's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds |
| [[CFH]] | B | CFH activity raises CTSO's level | lines that do not express CFH (28) vs lines expressing it (22) | 1.93× lower at baseline in the lines without CFH | 0.032 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |
| [[LINC02605]] | B | LINC02605 activity raises CTSO's level | lines that do not express LINC02605 (15) vs lines expressing it (35) | 1.80× lower at baseline in the lines without LINC02605 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000285744, FAR2, ENSG00000285517 |
| [[IFIT2]] | B | IFIT2 activity raises CTSO's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 2.52× lower at baseline in the lines without IFIT2 | 0.064 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[CTSS]] | B | CTSS activity raises CTSO's level | lines that do not express CTSS (15) vs lines expressing it (35) | 1.85× lower at baseline in the lines without CTSS | 0.080 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity lowers CTSO's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets |
| [[ERAP2]] | B | ERAP2 activity raises CTSO's level | lines that do not express ERAP2 (7) vs lines expressing it (43) | 2.15× lower at baseline in the lines without ERAP2 | 0.093 | ⚠ within organs, on part of the lines; also absent: COL13A1, SMOX, TRIM38; maybe low, not absent |
| [[FYB1]] | B | FYB1 activity raises CTSO's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 1.62× lower at baseline in the lines without FYB1 | 0.094 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |
| [[TLR3]] | B | TLR3 activity raises CTSO's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 1.80× lower at baseline in the lines without TLR3 | 0.098 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[RBM43]] | C | RBM43 activity raises CTSO's level | lines that do not express RBM43 (4) vs lines expressing it (46) | 2.83× lower at baseline in the lines without RBM43 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALPK1, RNASEL, TFAP2A |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TAPBP]] | B | CTSO activity raises TAPBP's level | lines that do not express CTSO (8) vs lines expressing it (42) | 1.56× lower at baseline in the lines without CTSO | 0.008 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |
| [[HFE]] | B | CTSO activity raises HFE's level | lines that do not express CTSO (8) vs lines expressing it (42) | 1.32× lower at baseline in the lines without CTSO | 0.009 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |
| [[ARSD]] | B | CTSO activity raises ARSD's level | lines that do not express CTSO (8) vs lines expressing it (42) | 1.61× lower at baseline in the lines without CTSO | 0.032 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |
| [[TAPBPL]] | B | CTSO activity raises TAPBPL's level | lines that do not express CTSO (8) vs lines expressing it (42) | 1.49× lower at baseline in the lines without CTSO | 0.035 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |
| [[CARMIL2]] | B | CTSO activity lowers CARMIL2's level | lines that do not express CTSO (8) vs lines expressing it (42) | 1.81× higher at baseline in the lines without CTSO | 0.043 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |
| [[BCLAF1]] | B | CTSO activity strengthens BCLAF1's drug response | lines that do not express CTSO (8) vs lines expressing it (41) | the lines without CTSO respond 0.95× as strongly (z diff +0.51); strongest at Panobinostat 0.5 µM: 0.73x vs 0.53x (z diff +4.1) | 0.045 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT; target measured in part of the lines; both ways; artifact flags |
| [[MDK]] | B | CTSO activity lowers MDK's level | lines that do not express CTSO (8) vs lines expressing it (42) | 2.22× higher at baseline in the lines without CTSO | 0.056 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |
| [[EIF1B-AS1]] | B | CTSO activity strengthens EIF1B-AS1's drug response | lines that do not express CTSO (8) vs lines expressing it (38) | the lines without CTSO respond 0.53× as strongly (z diff +1.85); strongest at Digitoxin 5 µM: 0.74x vs 0.33x (z diff +3.9) | 0.060 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT; target measured in part of the lines; artifact flags |
| [[PATL2]] | B | CTSO activity raises PATL2's level | lines that do not express CTSO (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without CTSO | 0.072 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |
| [[EIF1B-AS1]] | B | CTSO activity raises EIF1B-AS1's level | lines that do not express CTSO (8) vs lines expressing it (42) | 2.02× lower at baseline in the lines without CTSO | 0.088 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |
| [[RIPK2-DT]] | B | CTSO activity raises RIPK2-DT's level | lines that do not express CTSO (8) vs lines expressing it (42) | 1.66× lower at baseline in the lines without CTSO | 0.088 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |
| [[AGA]] | B | CTSO activity raises AGA's level | lines that do not express CTSO (8) vs lines expressing it (42) | 1.60× lower at baseline in the lines without CTSO | 0.089 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.628). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.5, 3.8); signed map (25.4, -20.3). **Vector** length 75.0, 15.6% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antigen Presentation: Folding, assembly and peptide loading of class I MHC* (reactome, mean cos +0.51 to 9); *CASP4 inflammasome assembly* (reactome, mean cos +0.56 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.0 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | +2.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +4.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.6 | +4.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.0 | -8.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.8 | -13.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.0 | -8.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.6 | -9.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -8.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | cathepsin O |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.1 — chr4:155,921,580-155,953,912 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CTSO1 |
| Gene groups (HGNC) | Cathepsins; Cysteine endopeptidases |
| Hallmark sets | COAGULATION, COMPLEMENT |
| Reactome | 5 pathways, smallest: Processing of antigen in germinal center B cells; MHC class II antigen presentation; Affinity selection of immunoglobulins |
| Matched by | ensembl_id |

**Function**, from UniProt [P43234](https://www.uniprot.org/uniprotkb/P43234) (Cathepsin O):

> Proteolytic enzyme possibly involved in normal cellular protein degradation and turnover.

**Summary**, from NCBI Gene [1519](https://www.ncbi.nlm.nih.gov/gene/1519):

> The protein encoded by the gene is a cysteine proteinase and a member of the papain superfamily. This proteolytic enzyme is involved in cellular protein degradation and turnover. The recombinant form of this enzyme was shown to degrade synthetic peptides typically used as substrates for cysteine proteinases and its proteolytic activity was abolished by an inhibitor of cyteine proteinase. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2542](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2542) · Entrez [1519](https://www.ncbi.nlm.nih.gov/gene/1519) · UniProt [P43234](https://www.uniprot.org/uniprotkb/P43234) · Ensembl [ENSG00000256043](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000256043)

## Data

Gene col 14970: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14970); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14970, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14970]; `tensor/DDL_lfc|DDL_z.npy` [14970]; `embed/gene_vectors.npy` [14970]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14970 or target_col == 14970). Every well: [[CTSO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTSO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
