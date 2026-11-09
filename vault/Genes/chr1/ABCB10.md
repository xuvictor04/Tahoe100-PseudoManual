---
symbol: "ABCB10"
type: "gene"
col: 5756
ensembl_id: "ENSG00000135776"
name: "ATP binding cassette subfamily B member 10"
location: "1q42.13"
module: 175
arm: "+"
pooled_cpm: 20.84
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# ABCB10

*ATP binding cassette subfamily B member 10* — 1q42.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.58× (z +7.9, q 2e-12, up in 19 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.21× (z +3.5, q 0.054, up in 10 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.397× (z -23.1, q 0e+00, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BIVM]] (+0.70, fdr 7e-06), [[GK5]] (+0.70, fdr 7e-06), [[ALG6]] (+0.69, fdr 7e-06); moves opposite to [[TUT7]] (-0.62, fdr 8e-06), [[ADNP2]] (-0.61, fdr 1e-05), [[IER5]] (-0.60, fdr 1e-05).
> It is in [[Module 175]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TRIB1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5756.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +7.9 | 2e-12 | 19/34 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +7.8 | 2e-12 | 23/42 (NCI-H2030, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.5 | 0.001 | 20/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.29×** | +4.2 | 0.004 | 15/36 (KATO III, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.054 | 10/48 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.14× | +3.3 | 0.088 | 6/48 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.088 | 4/47 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.10 | 4/48 (HOP62, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5756.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.397×** | -23.1 | 0e+00 | 39/47 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.329×** | -19.1 | 0e+00 | 36/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.556×** | -10.5 | 2e-23 | 32/47 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.573×** | -10.0 | 3e-21 | 31/46 (J82, HCT15, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.640×** | -8.0 | 2e-13 | 30/48 (A549, J82, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.655×** | -7.6 | 4e-12 | 32/47 (HEC-1-A, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.664×** | -7.3 | 2e-11 | 29/48 (A549, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.678×** | -6.9 | 3e-10 | 28/48 (NCI-H1573, HOP62, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.699×** | -6.4 | 1e-08 | 26/48 (NCI-H460, A-172, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.517×** | -6.2 | 3e-08 | 26/48 (Panc 03.27, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.787×** | -5.9 | 2e-07 | 25/48 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.724×** | -5.8 | 4e-07 | 25/47 (SNU-1, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.727×** | -5.7 | 5e-07 | 25/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.751×** | -5.1 | 1e-05 | 20/47 (C32, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -4.5 | 3e-04 | 2/48 (SW 900, RPMI-7951) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.795×** | -4.1 | 0.001 | 17/47 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.848× | -4.1 | 0.002 | 21/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.753×** | -3.6 | 0.009 | 14/48 (HEC-1-A, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.815×** | -3.4 | 0.021 | 15/46 (H4, A-172, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5756. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 45.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -25.1) |
| [[A498 (line)]] | wt | 24.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -19.1) |
| [[A549 (line)]] | wt | 29.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -15.1) |
| [[C32 (line)]] | wt | 24.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0985× (z -20.9) |
| [[HEC-1-A (line)]] | alt | 20.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -15.5) |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 37.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -14.8) |
| [[SNU-1 (line)]] | wt | 22.7 | 0 | 4 | — | [[Decitabine (drug)]] 0.05 µM 0.0518× (z -13.9) |
| [[HOP62 (line)]] | alt | 19.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -17.7) |
| [[J82 (line)]] | alt | 20.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -19.5) |
| [[LOX-IMVI (line)]] | wt | 18.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -17.3) |
| [[NCI-H1573 (line)]] | alt | 14.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -12.6) |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 2 | — | [[Resveratrol (drug)]] 0.5 µM 0.0540× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 32.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -15.9) |
| [[NCI-H2030 (line)]] | alt | 23.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 21.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.224× (z -9.7) |
| [[PANC-1 (line)]] | alt | 20.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 20.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -12.1) |
| [[A-427 (line)]] | wt | 26.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 11.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -8.7) |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -8.9) |
| [[H4 (line)]] | wt | 15.7 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0754× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 18.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -13.4) |
| [[SNU-423 (line)]] | alt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -14.2) |
| [[SW1417 (line)]] | alt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.5) |
| [[AN3 CA (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5756), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BIVM]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[GK5]] | +0.70 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[ALG6]] | +0.69 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[WHAMMP1]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[CHPT1]] | +0.67 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[SETD3]] | +0.66 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[SEPHS1]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[RNPEP]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[NAE1]] | +0.65 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[WDR5]] | +0.64 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[RPA1]] | +0.64 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[SRD5A1]] | +0.64 | +0.66 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUT7]] | -0.62 | -0.64 / -0.58 | both halves | 8e-06 |  |
| [[ADNP2]] | -0.61 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[IER5]] | -0.60 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[NFAT5]] | -0.60 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[BMP2]] | -0.60 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[BCL10]] | -0.59 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[HES1]] | -0.58 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[KIAA1217]] | -0.57 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[CSNK1A1]] | -0.57 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[PPP1R10]] | -0.55 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[ZSWIM4]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[DNAH17]] | -0.55 | -0.58 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIB1]] | B | TRIB1 activity lowers ABCB10's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 1.60× higher at baseline in the lines without TRIB1 | 0.068 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[NT5M]] | B | NT5M activity raises ABCB10's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.41× lower at baseline in the lines without NT5M | 0.074 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[ADCY3]] | B | ADCY3 activity raises ABCB10's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.33× lower at baseline in the lines without ADCY3 | 0.083 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[FHL2]] | C | FHL2 activity lowers ABCB10's level | lines that do not express FHL2 (4) vs lines expressing it (46) | 1.68× higher at baseline in the lines without FHL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EPS8, MYO1E, RUNX1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.834). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.3, -14.5); signed map (-38.7, -15.1). **Vector** length 95.6, 21.2% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.1 | +3.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.4 | -19.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -23.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -5.9 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily B member 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.13 — chr1:229,516,582-229,558,707 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EST20237, M-ABC2, MTABC2 |
| Gene groups (HGNC) | ATP binding cassette subfamily B |
| Reactome | 3 pathways, smallest: Mitochondrial ABC transporters; ABC-family protein mediated transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRK6](https://www.uniprot.org/uniprotkb/Q9NRK6) (ATP-binding cassette sub-family B member 10, mitochondrial):

> ATP-dependent transporter located in the mitochondrial inner membrane that catalyzes the export of biliverdin from the mitochondrial matrix, and plays a crucial role in hemoglobin synthesis and antioxidative stress. Participates in the early step of the heme biosynthetic process during insertion of iron into protoporphyrin IX (PPIX). Involved in the stabilization of the iron transporter mitoferrin-1/SLC25A37 (By similarity). In addition may be involved in mitochondrial unfolded protein response …

**Summary**, from NCBI Gene [23456](https://www.ncbi.nlm.nih.gov/gene/23456):

> The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MDR/TAP subfamily. Members of the MDR/TAP subfamily are involved in multidrug resistance. The function of this mitochondrial protein is unknown. …

**Accessions** — [HGNC:41](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41) · Entrez [23456](https://www.ncbi.nlm.nih.gov/gene/23456) · UniProt [Q9NRK6](https://www.uniprot.org/uniprotkb/Q9NRK6) · Ensembl [ENSG00000135776](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135776)

## Data

Gene col 5756: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5756); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5756, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5756]; `tensor/DDL_lfc|DDL_z.npy` [5756]; `embed/gene_vectors.npy` [5756]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5756 or target_col == 5756). Every well: [[ABCB10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCB10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
