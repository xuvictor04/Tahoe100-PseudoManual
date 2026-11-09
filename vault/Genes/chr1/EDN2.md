---
symbol: "EDN2"
type: "gene"
col: 4791
ensembl_id: "ENSG00000127129"
name: "endothelin 2"
location: "1p34.2"
module: 106
arm: "+"
pooled_cpm: 2.81
n_lines_expressing: 20
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 9
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# EDN2

*endothelin 2* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.31× (z +9.1, q 4e-17, up in 5 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0193×; ⚠ cell-cycle shift, explains ~27% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0291×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (BT-474 0.0378×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLVCR2]] (+0.70, fdr 7e-06), [[PER1]] (+0.60, fdr 1e-05), [[TSC22D3]] (+0.59, fdr 1e-05); moves opposite to [[DCBLD2]] (-0.68, fdr 7e-06), [[NT5E]] (-0.60, fdr 1e-05), [[AADACP1]] (-0.57, fdr 1e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 9 go from it, the strongest it → [[PLEKHA7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4791.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.31×** | +9.1 | 4e-17 | 5/13 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.45×** | +6.3 | 6e-08 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 0.05 µM |  | **3.21×** | +5.2 | 5e-05 | 10/17 (A498, NCI-H2347, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **3.15×** | +5.1 | 5e-05 | 10/17 (A498, CFPAC-1, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **3.14×** | +5.1 | 5e-05 | 9/15 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.92×** | +4.7 | 2e-04 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.04×** | +4.5 | 4e-04 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.89×** | +4.5 | 5e-04 | 10/17 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.58×** | +4.0 | 0.003 | 2/8 (J82, A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.48×** | +4.0 | 0.003 | 4/13 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.85×** | +3.8 | 0.006 | 11/17 (A498, A549, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **2.36×** | +3.8 | 0.007 | 5/15 (A498, NCI-H2347, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +3.7 | 0.008 | 10/17 (A549, H4, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | **2.31×** | +3.7 | 0.009 | 9/17 (A498, H4, …) | all doses, flat | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.11×** | +3.6 | 0.013 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +3.5 | 0.017 | 4/15 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.71×** | +3.3 | 0.026 | 0/16 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **2.07×** | +3.2 | 0.038 | 9/14 (A498, A549, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **2.04×** | +3.1 | 0.048 | 4/13 (A549, A498, …) | inconsistent across doses | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **2.12×** | +3.1 | 0.059 | 6/12 (A498, A549, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4791.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0193×; ⚠ cell-cycle shift, explains ~27% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0291×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (BT-474 0.0378×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.460× | -3.4 | 0.18 | 9/17 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.462× | -3.4 | 0.18 | 12/17 (CFPAC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4791. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 26.5 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0193× (z -13.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0291× (z -12.1) |
| [[A-172 (line)]] | wt | 3.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0378× (z -11.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 0.241 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.599 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.909 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.193 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.575 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.213 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.199 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.443 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.321 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.787 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.198 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.215 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.527 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.289 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.722 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4791), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLVCR2]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[PER1]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[TSC22D3]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[MAOA]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[MUC1]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[KLF9]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[SCNN1A]] | +0.56 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[PPP1CB]] | +0.56 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[MTMR4]] | +0.55 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[STOM]] | +0.54 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[POLR3GL]] | +0.54 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[JPH2]] | +0.54 | +0.50 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCBLD2]] | -0.68 | -0.62 / -0.68 | both halves | 7e-06 |  |
| [[NT5E]] | -0.60 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[AADACP1]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[SLC4A7]] | -0.55 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[ASPH]] | -0.55 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[AADAC]] | -0.54 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[BICD1]] | -0.54 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[MMP1]] | -0.53 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[ITGA2]] | -0.52 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[IQCJ-SCHIP1]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[ADAM19]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[C12orf75-AS1]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises EDN2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.5% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[TRIM29]] | C | TRIM29 activity raises EDN2's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 1.89× lower at baseline in the lines without TRIM29 | 0.029 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2; co-absent with the target |
| [[SGPP2]] | C | SGPP2 activity raises EDN2's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 1.79× lower at baseline in the lines without SGPP2 | 0.046 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4; co-absent with the target |
| [[DPP4]] | C | DPP4 activity raises EDN2's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 1.68× lower at baseline in the lines without DPP4 | 0.056 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10; co-absent with the target |
| [[SAA1]] | C | SAA1 activity raises EDN2's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 1.79× lower at baseline in the lines without SAA1 | 0.061 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11; co-absent with the target |
| [[NHS]] | C | NHS activity raises EDN2's level | lines that do not express NHS (17) vs lines expressing it (33) | 2.07× lower at baseline in the lines without NHS | 0.068 | ⚠ within organs, on part of the lines; also absent: ANKRD29, WNT7B, ABCC3; co-absent with the target |
| [[MUC1]] | C | MUC1 activity raises EDN2's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 1.71× lower at baseline in the lines without MUC1 | 0.072 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223; co-absent with the target |
| [[SCNN1A]] | C | SCNN1A activity raises EDN2's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 1.59× lower at baseline in the lines without SCNN1A | 0.090 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1; co-absent with the target |
| [[SAA2-SAA4]], [[SAA4]] | C | SAA2-SAA4, SAA4 activity raises EDN2's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 2.03× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.095 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent with the target; co-absent genes |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHA7]] | B | EDN2 activity raises PLEKHA7's level | lines that do not express EDN2 (30) vs lines expressing it (20) | 1.99× lower at baseline in the lines without EDN2 | 0.009 | ⚠ within organs, on part of the lines; also absent: WNT7A, FAM83A, CST6 |
| [[TLE1]] | B | EDN2 activity raises TLE1's level | lines that do not express EDN2 (30) vs lines expressing it (20) | 1.37× lower at baseline in the lines without EDN2 | 0.082 | ⚠ within organs, on part of the lines; also absent: WNT7A, FAM83A, CST6 |
| [[MAP3K8]] | B | EDN2 activity raises MAP3K8's level | lines that do not express EDN2 (30) vs lines expressing it (20) | 1.81× lower at baseline in the lines without EDN2 | 0.087 | ⚠ within organs, on part of the lines; also absent: WNT7A, FAM83A, CST6 |
| [[MYO3B]] | B | EDN2 activity raises MYO3B's level | lines that do not express EDN2 (30) vs lines expressing it (20) | 1.30× lower at baseline in the lines without EDN2 | 0.087 | ⚠ within organs, on part of the lines; also absent: WNT7A, FAM83A, CST6 |
| [[DCBLD2]] | B | EDN2 activity raises DCBLD2's level | lines that do not express EDN2 (30) vs lines expressing it (20) | 1.77× lower at baseline in the lines without EDN2 | 0.096 | ⚠ within organs, on part of the lines; also absent: WNT7A, FAM83A, CST6 |
| [[SH3TC1]] | B | EDN2 activity raises SH3TC1's level | lines that do not express EDN2 (30) vs lines expressing it (20) | 1.76× lower at baseline in the lines without EDN2 | 0.098 | ⚠ within organs, on part of the lines; also absent: WNT7A, FAM83A, CST6 |
| [[SCNN1A]] | C | EDN2 activity raises SCNN1A's level | lines that do not express EDN2 (30) vs lines expressing it (20) | 3.40× lower at baseline in the lines without EDN2 | 0.011 | ⚠ within organs, on part of the lines; also absent: WNT7A, FAM83A, CST6; co-absent with the target |
| [[TRIM29]] | C | EDN2 activity raises TRIM29's level | lines that do not express EDN2 (30) vs lines expressing it (20) | 2.81× lower at baseline in the lines without EDN2 | 0.015 | ⚠ within organs, on part of the lines; also absent: WNT7A, FAM83A, CST6; co-absent with the target |
| [[SGPP2]] | C | EDN2 activity raises SGPP2's level | lines that do not express EDN2 (30) vs lines expressing it (20) | 3.38× lower at baseline in the lines without EDN2 | 0.061 | ⚠ within organs, on part of the lines; also absent: WNT7A, FAM83A, CST6; co-absent with the target |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.7, 10.6); signed map (15.2, 28.7). **Vector** length 55.5, 17.0% of its response variance represented; |z| ≥ 3 in 485 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Budesonide (drug)]] 0.05 µM |  | +2.2 | +5.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.1 | +3.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.0 | +4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.0 | +9.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | endothelin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:41,478,775-41,484,683 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ET2 |
| Gene groups (HGNC) | Endothelins |
| Hallmark sets | KRAS_SIGNALING_DN, HYPOXIA |
| Reactome | 6 pathways, smallest: Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P20800](https://www.uniprot.org/uniprotkb/P20800) (Endothelin-2):

> Endothelins are endothelium-derived vasoconstrictor peptides.

**Summary**, from NCBI Gene [1907](https://www.ncbi.nlm.nih.gov/gene/1907):

> This gene encodes a member of the endothelin protein family of secretory vasoconstrictive peptides. The preproprotein is processed to a short mature form which functions as a ligand for the endothelin receptors that initiate intracellular signaling events. This gene product is involved in a wide range of biological processes, such as hypertension and ovulation. Altered expression of this gene is implicated in tumorigenesis. Alternative splicing results in multiple transcript variants. [provided …

**Accessions** — [HGNC:3177](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3177) · Entrez [1907](https://www.ncbi.nlm.nih.gov/gene/1907) · UniProt [P20800](https://www.uniprot.org/uniprotkb/P20800) · Ensembl [ENSG00000127129](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127129)

## Data

Gene col 4791: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4791); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4791, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4791]; `tensor/DDL_lfc|DDL_z.npy` [4791]; `embed/gene_vectors.npy` [4791]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4791 or target_col == 4791). Every well: [[EDN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EDN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
