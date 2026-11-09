---
symbol: "ANKDD1A"
type: "gene"
col: 9368
ensembl_id: "ENSG00000166839"
name: "ankyrin repeat and death domain containing 1A"
location: "15q22.31"
module: 161
arm: "+"
pooled_cpm: 10.35
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# ANKDD1A

*ankyrin repeat and death domain containing 1A* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.95× (z +18.6, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.432× (z -7.6, q 2e-11, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CADM4]] (+0.63, fdr 3e-05), [[SEMA3F]] (+0.62, fdr 4e-05), [[CELF5]] (+0.57, fdr 5e-05); moves opposite to [[GANC]] (-0.53, fdr 5e-04), [[ASH2L]] (-0.50, fdr 1e-04), [[ANGEL2]] (-0.50, fdr 2e-04).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NRARP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9368.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.95×** | +18.6 | 0e+00 | 42/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +15.0 | 0e+00 | 39/47 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.23×** | +13.5 | 3e-39 | 33/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.95×** | +11.5 | 1e-28 | 33/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.88×** | +10.8 | 2e-25 | 28/45 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +10.7 | 1e-24 | 21/44 (A498, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +10.0 | 2e-21 | 23/45 (C32, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +8.3 | 1e-14 | 25/47 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.83×** | +5.4 | 4e-06 | 13/46 (RPMI-7951, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.030 | 5/47 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9368.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.432×** | -7.6 | 2e-11 | 27/46 (A549, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.666×** | -7.0 | 6e-10 | 19/46 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.669×** | -6.7 | 5e-09 | 18/46 (LoVo, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.796×** | -5.6 | 3e-06 | 21/44 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.586×** | -4.8 | 2e-04 | 13/42 (C-33 A, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.761×** | -4.7 | 2e-04 | 11/46 (CHP-212, HEC-1-A, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.834× | -4.5 | 6e-04 | 12/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.780×** | -4.3 | 0.001 | 11/47 (SW 1088, SW 900, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.784×** | -4.2 | 0.002 | 15/45 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.789×** | -4.1 | 0.002 | 12/46 (SW 1271, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.800×** | -3.7 | 0.010 | 15/39 (NCI-H1792, RPMI-7951, …) | top dose only |  |
| [[Lopinavir (drug)]] 0.5 µM |  | **0.812×** | -3.5 | 0.019 | 5/47 (NCI-H661, LoVo, …) | inconsistent across doses |  |
| [[Piroxicam (drug)]] 0.5 µM |  | **0.821×** | -3.4 | 0.034 | 6/47 (SW1417, NCI-H661, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.823×** | -3.2 | 0.049 | 12/46 (HEC-1-A, KATO III, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.880× | -3.1 | 0.062 | 11/47 (SW480, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9368. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 7.54 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.01× (z +19.0) | — |
| [[NCI-H1792 (line)]] | alt | 18.6 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.151× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -8.5) |
| [[PANC-1 (line)]] | alt | 18.5 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -12.9) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 47.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +13.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.164× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 11.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +11.6) | — |
| [[A-172 (line)]] | wt | 17.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 15.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.7× (z +18.7) | — |
| [[LoVo (line)]] | wt | 8.67 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +9.2) | [[Harringtonine (drug)]] 5 µM 0.218× (z -8.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[MIA PaCa-2 (line)]] | alt | 17.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -14.0) |
| [[HCT15 (line)]] | alt | 10.1 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0792× (z -8.9) |
| [[Hs 766T (line)]] | wt | 7.43 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -9.2) |
| [[HS-578T (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 11.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.46× (z +9.2) | — |
| [[KATO III (line)]] | alt | 5.57 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.69× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 4.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 2.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.96× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 5.39 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 0.05 µM 0.0722× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 9.88 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 7.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +11.0) | — |
| [[RKO (line)]] | wt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 8.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 5.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.20× (z +11.2) | — |
| [[A-427 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9368), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 7 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CADM4]] | +0.63 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[SEMA3F]] | +0.62 | +0.40 / +0.59 | both halves | 4e-05 |  |
| [[CELF5]] | +0.57 | +0.39 / +0.69 | both halves | 5e-05 |  |
| [[ASMTL]] | +0.57 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[ATP1A3]] | +0.56 | +0.24 / +0.61 | both halves | 4e-04 |  |
| [[ITGA7]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[GDF11]] | +0.55 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[LMTK3]] | +0.55 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[CCDC88B]] | +0.55 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[SYP]] | +0.55 | +0.24 / +0.60 | both halves | 4e-04 |  |
| [[SHF]] | +0.54 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[FCHO1]] | +0.54 | +0.26 / +0.62 | both halves | 4e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GANC]] | -0.53 | -0.23 / -0.53 | both halves | 5e-04 |  |
| [[ASH2L]] | -0.50 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[ANGEL2]] | -0.50 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[PARG]] | -0.49 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[PSME3IP1]] | -0.49 | -0.18 / -0.51 | ⚠ one half (not replicated) | 0.001 |  |
| [[RNF170]] | -0.48 | -0.21 / -0.35 | both halves | 7e-04 |  |
| [[PPP1R8]] | -0.47 | -0.25 / -0.35 | both halves | 4e-04 |  |
| [[KLHL42]] | -0.47 | -0.29 / -0.33 | both halves | 2e-04 |  |
| [[DECR1]] | -0.47 | -0.20 / -0.41 | both halves | 7e-04 |  |
| [[SETD7]] | -0.47 | -0.43 / -0.22 | both halves | 6e-04 |  |
| [[TXNDC15]] | -0.47 | -0.30 / -0.33 | both halves | 2e-04 |  |
| [[C5orf15]] | -0.47 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[DDX59]] | -0.47 | -0.23 / -0.45 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRARP]] | B | NRARP activity lowers ANKDD1A's level | lines that do not express NRARP (14) vs lines expressing it (36) | 1.54× higher at baseline in the lines without NRARP | 0.051 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A |
| [[BCAM]] | B | BCAM activity raises ANKDD1A's level | lines that do not express BCAM (8) vs lines expressing it (42) | 1.49× lower at baseline in the lines without BCAM | 0.063 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[NRARP]] | B | NRARP activity weakens ANKDD1A's drug response | lines that do not express NRARP (14) vs lines expressing it (33) | the lines without NRARP respond 1.18× as strongly (z diff -0.43); strongest at Homoharringtonine 5 µM: 5.17x vs 1.10x (z diff -8.3) | 0.075 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A; target measured in part of the lines; both ways; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ANKDD1A's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers ANKDD1A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.663). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (2.0, 32.2); signed map (-22.3, 29.1). **Vector** length 75.9, 13.0% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +15.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +10.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | +13.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +10.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +1.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.2 | +2.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.2 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and death domain containing 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:64,911,902-64,958,691 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25870 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q495B1](https://www.uniprot.org/uniprotkb/Q495B1) carries no function annotation.

**Summary**, from NCBI Gene [348094](https://www.ncbi.nlm.nih.gov/gene/348094):

> Predicted to be involved in signal transduction. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28002](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28002) · Entrez [348094](https://www.ncbi.nlm.nih.gov/gene/348094) · UniProt [Q495B1](https://www.uniprot.org/uniprotkb/Q495B1) · Ensembl [ENSG00000166839](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166839)

## Data

Gene col 9368: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9368); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9368, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9368]; `tensor/DDL_lfc|DDL_z.npy` [9368]; `embed/gene_vectors.npy` [9368]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9368 or target_col == 9368). Every well: [[ANKDD1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKDD1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
