---
symbol: "GPRC5B"
type: "gene"
col: 9432
ensembl_id: "ENSG00000167191"
name: "G protein-coupled receptor class C group 5 member B"
location: "16p12.3"
module: 147
arm: "+"
pooled_cpm: 13.63
n_lines_expressing: 23
n_dd_up: 28
n_dd_down: 5
n_dd_up_clean: 23
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# GPRC5B

*G protein-coupled receptor class C group 5 member B* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.81× (z +8.6, q 3e-15, up in 6 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.717× (z -4.8, q 1e-03, down in 17 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GBP2]] (+0.64, fdr 7e-06), [[CGNL1]] (+0.61, fdr 1e-05), [[CYRIA]] (+0.59, fdr 2e-05); moves opposite to [[TOP1]] (-0.61, fdr 1e-05), [[HMGA2]] (-0.60, fdr 8e-06), [[CLMP]] (-0.57, fdr 1e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[APOL3]] → it (grade B ⚠); 7 go from it, the strongest it → [[APOL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9432.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +8.6 | 3e-15 | 6/21 (A-172, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.31×** | +8.6 | 3e-15 | 9/20 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.28×** | +8.5 | 5e-15 | 11/20 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.58×** | +6.7 | 4e-09 | 9/21 (C32, Hs 766T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.91×** | +6.6 | 4e-09 | 7/20 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.75×** | +5.7 | 1e-06 | 8/20 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +5.6 | 2e-06 | 2/11 (J82, HS-578T) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **1.58×** | +4.8 | 1e-04 | 9/21 (NCI-H1792, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.60×** | +4.7 | 1e-04 | 12/20 (A549, A-172, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.47×** | +4.3 | 8e-04 | 9/21 (A549, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.18×** | +4.2 | 0.002 | 2/21 (A-172, CFPAC-1) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +3.9 | 0.004 | 5/18 (J82, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.004 | 8/20 (A549, A-172, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.004 | 8/21 (CFPAC-1, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +3.8 | 0.005 | 5/21 (CFPAC-1, C32, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.31×** | +3.8 | 0.005 | 13/21 (C32, Hs 766T, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +3.7 | 0.007 | 4/17 (Panc 03.27, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9432.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -4.8 | 1e-03 | 17/19 (Hs 766T, A498, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | **0.766×** | -3.8 | 0.039 | 9/20 (CHP-212, Hs 766T, …) | top dose only | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.696×** | -3.7 | 0.045 | 6/20 (Hs 766T, NCI-H1792, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.711×** | -3.5 | 0.077 | 5/20 (Hs 766T, NCI-H1573, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -3.3 | 0.097 | 10/20 (C32, A498, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.732× | -3.2 | 0.15 | 9/20 (Hs 766T, NCI-H1792, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9432. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 201 | 0 | 21 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -20.9) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -16.5) |
| [[A498 (line)]] | wt | 92.1 | 2 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.8) ⚠ cell-cycle shift, explains ~11% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -14.8) |
| [[SK-MEL-2 (line)]] | alt | 31.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -11.8) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -10.0) |
| [[C32 (line)]] | wt | 17.8 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0410× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 23.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 24.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -11.1) ⚠ cell-cycle shift, explains ~11% of this change |
| [[A-172 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.871 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.966 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.95 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9432), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBP2]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[CGNL1]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CYRIA]] | +0.59 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[LRIG3]] | +0.57 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[RRAD]] | +0.56 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[CDK18]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[PIM1]] | +0.53 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[PTGIS]] | +0.52 | +0.38 / +0.56 | both halves | 7e-05 |  |
| [[PIK3C2B]] | +0.52 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[SWAP70]] | +0.52 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[KIF13A]] | +0.52 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[BMF]] | +0.52 | +0.52 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOP1]] | -0.61 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[HMGA2]] | -0.60 | -0.57 / -0.58 | both halves | 8e-06 |  |
| [[CLMP]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[MOSMO]] | -0.57 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[HMGA2-AS1]] | -0.55 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[SIPA1L1]] | -0.54 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[SPRY4-AS1]] | -0.54 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[MAP4K4]] | -0.51 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[LINC00941]] | -0.51 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[ERRFI1]] | -0.51 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[MCL1]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ERRFI1-DT]] | -0.50 | -0.43 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOL3]] | B | APOL3 activity raises GPRC5B's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 2.42× lower at baseline in the lines without APOL3 | 0.086 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[MAP2K1]] | B | MAP2K1 activity lowers GPRC5B's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[CGNL1]] | C | CGNL1 activity raises GPRC5B's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 2.64× lower at baseline in the lines without CGNL1 | 0.017 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7; co-absent with the target |
| [[TNFAIP6]] | C | TNFAIP6 activity raises GPRC5B's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 3.36× lower at baseline in the lines without TNFAIP6 | 0.069 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF; co-absent with the target |
| [[TNFRSF9]] | C | TNFRSF9 activity raises GPRC5B's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 2.78× lower at baseline in the lines without TNFRSF9 | 0.088 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOL3]] | B | GPRC5B activity raises APOL3's level | lines that do not express GPRC5B (27) vs lines expressing it (23) | 2.46× lower at baseline in the lines without GPRC5B | 0.040 | ⚠ within organs, on part of the lines; also absent: PALMD, FYB1, AK5 |
| [[ERRFI1]] | B | GPRC5B activity weakens ERRFI1's drug response | lines that do not express GPRC5B (25) vs lines expressing it (21) | the lines without GPRC5B respond 1.43× as strongly (z diff -1.13); strongest at Dinaciclib 5 µM: 0.44x vs 0.68x (z diff -3.7) | 0.046 | ⚠ within organs, on part of the lines; also absent: PALMD, FYB1, AK5; target measured in part of the lines; both ways; artifact flags |
| [[SPRY4-AS1]] | B | GPRC5B activity lowers SPRY4-AS1's level | lines that do not express GPRC5B (27) vs lines expressing it (23) | 1.88× higher at baseline in the lines without GPRC5B | 0.060 | ⚠ within organs, on part of the lines; also absent: PALMD, FYB1, AK5 |
| [[EPB41]] | B | GPRC5B activity raises EPB41's level | lines that do not express GPRC5B (27) vs lines expressing it (23) | 1.10× lower at baseline in the lines without GPRC5B | 0.064 | ⚠ within organs, on part of the lines; also absent: PALMD, FYB1, AK5 |
| [[PTPRG]] | B | GPRC5B activity lowers PTPRG's level | lines that do not express GPRC5B (27) vs lines expressing it (23) | 1.24× higher at baseline in the lines without GPRC5B | 0.094 | ⚠ within organs, on part of the lines; also absent: PALMD, FYB1, AK5 |
| [[CGNL1]] | C | GPRC5B activity raises CGNL1's level | lines that do not express GPRC5B (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without GPRC5B | 0.017 | ⚠ within organs, on part of the lines; also absent: PALMD, FYB1, AK5; co-absent with the target |
| [[P2RX7]] | C | GPRC5B activity raises P2RX7's level | lines that do not express GPRC5B (27) vs lines expressing it (23) | 2.24× lower at baseline in the lines without GPRC5B | 0.091 | ⚠ within organs, on part of the lines; also absent: PALMD, FYB1, AK5; co-absent with the target |

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction -0.586). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.2, 1.0); signed map (45.9, 10.4). **Vector** length 59.5, 15.5% of its response variance represented; |z| ≥ 3 in 548 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +2.8 | +6.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Trametinib (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | +4.8 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.7 | -3.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor class C group 5 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:19,856,691-19,886,167 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAIG-2 |
| Gene groups (HGNC) | G protein-coupled receptors, Class C orphans |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZH0](https://www.uniprot.org/uniprotkb/Q9NZH0) (G protein-coupled receptor family C group 5 member B):

> G protein-coupled receptor involved in the regulation of cell volume.

**Summary**, from NCBI Gene [51704](https://www.ncbi.nlm.nih.gov/gene/51704):

> This gene encodes a member of the type 3 G protein-coupled receptor family. Members of this superfamily are characterized by a signature 7-transmembrane domain motif. The encoded protein may modulate insulin secretion and increased protein expression is associated with type 2 diabetes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2015]

**Accessions** — [HGNC:13308](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13308) · Entrez [51704](https://www.ncbi.nlm.nih.gov/gene/51704) · UniProt [Q9NZH0](https://www.uniprot.org/uniprotkb/Q9NZH0) · Ensembl [ENSG00000167191](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167191)

## Data

Gene col 9432: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9432); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9432, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9432]; `tensor/DDL_lfc|DDL_z.npy` [9432]; `embed/gene_vectors.npy` [9432]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9432 or target_col == 9432). Every well: [[GPRC5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPRC5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
