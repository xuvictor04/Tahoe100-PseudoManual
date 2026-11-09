---
symbol: "SLC46A3"
type: "gene"
col: 6311
ensembl_id: "ENSG00000139508"
name: "solute carrier family 46 member 3"
location: "13q12.3"
module: 81
arm: "+"
pooled_cpm: 4.33
n_lines_expressing: 39
n_dd_up: 11
n_dd_down: 18
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# SLC46A3

*solute carrier family 46 member 3* — 13q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.33× (z +8.0, q 7e-13, up in 0 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.76× (z +5.5, q 6e-06, up in 12 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.308× (z -11.5, q 8e-28, down in 26 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH2D2A]] (+0.66, fdr 7e-06), [[ABTB3]] (+0.60, fdr 1e-05), [[NT5E]] (+0.60, fdr 8e-06); moves opposite to [[STAT5B]] (-0.51, fdr 4e-05), [[FSTL3]] (-0.47, fdr 4e-05), [[NFYB]] (-0.46, fdr 1e-04).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SPOCK1]] → it (grade B ⚠); 7 go from it, the strongest it → [[POMP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6311.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +8.0 | 7e-13 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +5.7 | 3e-06 | 2/9 (HOP62, A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.76×** | +5.5 | 6e-06 | 12/36 (A-172, A498, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +5.3 | 1e-05 | 11/34 (HT-29, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +4.7 | 2e-04 | 15/36 (A498, HT-29, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +4.2 | 0.003 | 7/29 (A-172, LS 180, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.57×** | +3.5 | 0.034 | 4/17 (LS 180, SW 900, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.050 | 6/35 (hTERT-HPNE, COLO 205, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.085 | 1/36 (J82) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | **1.39×** | +3.1 | 0.093 | 2/20 (A-172, SK-MEL-2) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.093 | 1/36 (LoVo) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 1.36× | +3.1 | 0.11 | 6/36 (A-427, A498, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6311.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.308×** | -11.5 | 8e-28 | 26/36 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.439×** | -11.3 | 4e-27 | 24/29 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.434×** | -8.1 | 7e-14 | 22/27 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.455×** | -7.7 | 2e-12 | 20/34 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.476×** | -7.2 | 5e-11 | 15/25 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.508×** | -6.6 | 4e-09 | 20/35 (HT-29, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.564×** | -5.6 | 2e-06 | 19/36 (NCI-H460, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.586×** | -5.0 | 4e-05 | 16/31 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | **0.759×** | -3.8 | 0.011 | 13/36 (LoVo, NCI-H23, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.693×** | -3.4 | 0.033 | 11/33 (HCT15, SW 1271, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.511×** | -3.4 | 0.033 | 9/25 (NCI-H1573, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.522×** | -3.3 | 0.045 | 7/31 (COLO 205, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.789×** | -3.2 | 0.055 | 13/36 (HT-29, RKO, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.727×** | -3.1 | 0.081 | 6/36 (AsPC-1, HT-29, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | **0.799×** | -3.0 | 0.088 | 5/35 (NCI-H1792, J82, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.714×** | -3.0 | 0.088 | 7/34 (KATO III, A-427, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.678×** | -3.0 | 0.097 | 4/35 (NCI-H23, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6311. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 16.0 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0797× (z -11.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.152× (z -9.1) |
| [[A-172 (line)]] | wt | 24.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -12.6) |
| [[HT-29 (line)]] | alt | 7.56 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 7.49 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0388× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 6.06 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0690× (z -8.7) |
| [[PANC-1 (line)]] | alt | 4.54 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0374× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.147× (z -12.4) |
| [[A549 (line)]] | wt | 4.51 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0794× (z -11.7) |
| [[HOP62 (line)]] | alt | 4.21 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0777× (z -9.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -10.0) |
| [[LoVo (line)]] | wt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -14.6) |
| [[SNU-423 (line)]] | alt | 5.53 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -8.8) |
| [[A-427 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.852 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.870 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.428 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.623 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6311), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH2D2A]] | +0.66 | +0.58 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[ABTB3]] | +0.60 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[NT5E]] | +0.60 | +0.57 / +0.58 | both halves | 8e-06 |  |
| [[AMOTL1]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[NLRP3]] | +0.59 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[STC1]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ITGA2]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[SERPIND1]] | +0.56 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[PKIA]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[MYO10]] | +0.55 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[CREG2]] | +0.55 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[MMP1]] | +0.54 | +0.52 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAT5B]] | -0.51 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[FSTL3]] | -0.47 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[NFYB]] | -0.46 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[PCID2]] | -0.46 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[ALG12]] | -0.46 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[TIMM44]] | -0.45 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[TRPM7]] | -0.45 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[H2AZ1-DT]] | -0.45 | -0.40 / -0.26 | both halves | 3e-04 |  |
| [[ROS1]] | -0.44 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[CYB561]] | -0.44 | -0.42 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPOCK1]] | B | SPOCK1 activity raises SLC46A3's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 1.64× lower at baseline in the lines without SPOCK1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[MARCHF3]] | B | MARCHF3 activity raises SLC46A3's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 2.43× lower at baseline in the lines without MARCHF3 | 0.061 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[KIF21B]] | B | KIF21B activity lowers SLC46A3's level | lines that do not express KIF21B (11) vs lines expressing it (39) | 1.29× higher at baseline in the lines without KIF21B | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NLRP3]] | B | NLRP3 activity raises SLC46A3's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 1.63× lower at baseline in the lines without NLRP3 | 0.095 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POMP]] | B | SLC46A3 activity raises POMP's level | lines that do not express SLC46A3 (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without SLC46A3 | 0.035 | ⚠ within organs, on part of the lines; also absent: PLCE1, CLCF1 |
| [[PPFIBP1]] | B | SLC46A3 activity raises PPFIBP1's level | lines that do not express SLC46A3 (11) vs lines expressing it (39) | 1.57× lower at baseline in the lines without SLC46A3 | 0.049 | ⚠ within organs, on part of the lines; also absent: PLCE1, CLCF1 |
| [[LINC02454]] | B | SLC46A3 activity raises LINC02454's level | lines that do not express SLC46A3 (11) vs lines expressing it (39) | 1.66× lower at baseline in the lines without SLC46A3 | 0.072 | ⚠ within organs, on part of the lines; also absent: PLCE1, CLCF1 |
| [[TMEM158]] | B | SLC46A3 activity raises TMEM158's level | lines that do not express SLC46A3 (11) vs lines expressing it (39) | 3.27× lower at baseline in the lines without SLC46A3 | 0.086 | ⚠ within organs, on part of the lines; also absent: PLCE1, CLCF1 |
| cells under [[Cabozantinib (S-malate) (drug)]] 5 µM | B | SLC46A3 activity lowers the cells' numbers under Cabozantinib (S-malate) 5 µM (makes them more sensitive) | lines that do not express SLC46A3 (11) vs lines expressing it (37) | the lines without SLC46A3: 1.19× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: PLCE1, CLCF1 |
| [[MARCHF3]] | B | SLC46A3 activity raises MARCHF3's level | lines that do not express SLC46A3 (11) vs lines expressing it (39) | 1.85× lower at baseline in the lines without SLC46A3 | 0.093 | ⚠ within organs, on part of the lines; also absent: PLCE1, CLCF1 |
| [[STX1A]] | B | SLC46A3 activity raises STX1A's level | lines that do not express SLC46A3 (11) vs lines expressing it (39) | 1.80× lower at baseline in the lines without SLC46A3 | 0.099 | ⚠ within organs, on part of the lines; also absent: PLCE1, CLCF1 |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.620). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.0, 5.0); signed map (3.5, 49.4). **Vector** length 60.3, 10.7% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.5 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | +2.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | +0.9 | -1.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +0.9 | +2.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +0.8 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -11.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.2 | +0.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 46 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.3 — chr13:28,700,064-28,718,970 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686A1775, FLJ42613 |
| Gene groups (HGNC) | Solute carrier family 46 |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z3Q1](https://www.uniprot.org/uniprotkb/Q7Z3Q1) (Lysosomal proton-coupled steroid conjugate and bile acid symporter SLC46A3):

> Lysosomal proton-coupled steroid conjugate and bile acid transporter. Preferentially recognizes lipophilic steroid conjugates or bile acis as endogenous substrates and seems to mediate escape from lysosomes to the cytoplasm. Modulates hepatic cytosolic copper homeostasis, maybe acting as a lysosomal copper transporter and sequestering copper ions in the lysosome (By similarity). Transports catabolites of non-cleavable antibody-drug conjugates from the lysosome to the cytoplasm. Delivers …

**Summary**, from NCBI Gene [283537](https://www.ncbi.nlm.nih.gov/gene/283537):

> The protein encoded by this gene is a member of a transmembrane protein family that transports small molecules across membranes. The encoded protein has been found in lysosomal membranes, where it can transport catabolites from the lysosomes to the cytoplasm. This protein has been shown to be an effective transporter of the cytotoxic drug maytansine, which is used in antibody-based targeting of cancer cells. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:27501](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27501) · Entrez [283537](https://www.ncbi.nlm.nih.gov/gene/283537) · UniProt [Q7Z3Q1](https://www.uniprot.org/uniprotkb/Q7Z3Q1) · Ensembl [ENSG00000139508](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139508)

## Data

Gene col 6311: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6311); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6311, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6311]; `tensor/DDL_lfc|DDL_z.npy` [6311]; `embed/gene_vectors.npy` [6311]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6311 or target_col == 6311). Every well: [[SLC46A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC46A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
