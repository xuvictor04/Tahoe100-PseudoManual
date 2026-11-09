---
symbol: "FAM124A"
type: "gene"
col: 7440
ensembl_id: "ENSG00000150510"
name: "family with sequence similarity 124 member A"
location: "13q14.3"
module: 82
arm: "+"
pooled_cpm: 3.2
n_lines_expressing: 36
n_dd_up: 13
n_dd_down: 13
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 15
direction_downstream: 21
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# FAM124A

*family with sequence similarity 124 member A* — 13q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.26× (z +12.7, q 3e-34, up in 25 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.335× (z -12.1, q 9e-31, down in 26 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP6]] (+0.64, fdr 7e-06), [[WSCD1]] (+0.64, fdr 8e-06), [[GPRIN1]] (+0.63, fdr 7e-06); moves opposite to [[TBCK]] (-0.57, fdr 2e-05), [[MBD5]] (-0.53, fdr 4e-05), [[USP49]] (-0.51, fdr 2e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[COL4A3]] → it (grade B ⚠); 21 go from it, the strongest it → [[CYS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7440.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.26×** | +12.7 | 3e-34 | 25/30 (SW480, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.44×** | +9.8 | 3e-20 | 20/27 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.22×** | +8.8 | 2e-16 | 14/31 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.81×** | +6.5 | 9e-09 | 14/31 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.70×** | +5.9 | 5e-07 | 10/31 (C32, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +5.8 | 5e-07 | 11/31 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.60×** | +5.2 | 2e-05 | 9/31 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.43×** | +3.9 | 0.006 | 5/24 (J82, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.006 | 3/32 (NCI-H460, LoVo, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.61×** | +3.7 | 0.011 | 1/10 (A-172) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.39×** | +3.4 | 0.037 | 1/27 (A-427) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +3.4 | 0.037 | 5/26 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.33×** | +3.1 | 0.080 | 4/29 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7440.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.335×** | -12.1 | 9e-31 | 26/32 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.452×** | -8.8 | 5e-16 | 19/29 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.514×** | -7.4 | 4e-11 | 16/23 (NCI-H460, J82, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.489×** | -6.6 | 5e-09 | 16/28 (HS-578T, SW 900, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.554×** | -6.5 | 7e-09 | 16/30 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.572×** | -6.2 | 6e-08 | 16/30 (NCI-H1573, A-172, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -5.0 | 4e-05 | 12/27 (LoVo, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.637×** | -5.0 | 4e-05 | 13/21 (A549, A-172, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.601×** | -4.7 | 1e-04 | 13/18 (A-427, HS-578T, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Erythromycin (drug)]] 0.5 µM |  | **0.736×** | -3.4 | 0.038 | 2/30 (A549, SW480) | inconsistent across doses | position effect removed |
| [[Erlotinib (drug)]] 0.5 µM |  | **0.745×** | -3.3 | 0.057 | 3/32 (SW 1271, C32, …) | inconsistent across doses |  |
| [[Darolutamide (drug)]] 0.5 µM |  | **0.750×** | -3.2 | 0.069 | 4/29 (HCT15, HS-578T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.758×** | -3.1 | 0.093 | 6/32 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7440. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.26 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.120× (z -10.9) |
| [[A549 (line)]] | wt | 6.49 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -10.0) |
| [[HS-578T (line)]] | alt | 12.1 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0320× (z -12.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.203× (z -9.4) |
| [[A-427 (line)]] | wt | 9.81 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.270× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 4.91 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0992× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[A-172 (line)]] | wt | 6.52 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.105× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 7.92 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.131× (z -8.6) |
| [[SW 900 (line)]] | alt | 6.56 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0291× (z -11.0) |
| [[SW480 (line)]] | alt | 1.39 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.80× (z +9.4) | — |
| [[A498 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.888 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.734 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.628 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.330 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.318 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.411 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7440), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP6]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[WSCD1]] | +0.64 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[GPRIN1]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[RASSF2]] | +0.62 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[GALNT12]] | +0.62 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[COL4A4]] | +0.61 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[RIMS3]] | +0.61 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[LMX1B]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ANKRD6]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[RADIL]] | +0.60 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[CDYL2]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[DNMT3B]] | +0.58 | +0.46 / +0.64 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCK]] | -0.57 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[MBD5]] | -0.53 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[USP49]] | -0.51 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[GALK2]] | -0.48 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[CDK19]] | -0.48 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[DYNC2I1]] | -0.48 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[SLC39A1]] | -0.47 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[STAG2]] | -0.47 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[ZNF608]] | -0.47 | -0.37 / -0.40 | both halves | 9e-05 |  |
| [[MPV17]] | -0.46 | -0.36 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 5, C 10. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL4A3]] | B | COL4A3 activity raises FAM124A's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 2.11× lower at baseline in the lines without COL4A3 | 0.027 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4 |
| [[CYS1]] | B | CYS1 activity raises FAM124A's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 1.43× lower at baseline in the lines without CYS1 | 0.030 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4 |
| [[RNF182]] | B | RNF182 activity raises FAM124A's level | lines that do not express RNF182 (22) vs lines expressing it (28) | 1.65× lower at baseline in the lines without RNF182 | 0.060 | ⚠ within organs, on part of the lines; also absent: PTX3, FZD8, ENSG00000230615 |
| [[GBX1]] | B | GBX1 activity raises FAM124A's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 1.60× lower at baseline in the lines without GBX1 | 0.066 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[LRRN2]] | B | LRRN2 activity raises FAM124A's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 1.67× lower at baseline in the lines without LRRN2 | 0.088 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL |
| [[STOX2]] | C | STOX2 activity raises FAM124A's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 1.88× lower at baseline in the lines without STOX2 | 0.002 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27; co-absent with the target |
| [[TUB]] | C | TUB activity raises FAM124A's level | lines that do not express TUB (18) vs lines expressing it (32) | 2.21× lower at baseline in the lines without TUB | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC22A17, CPEB1, ZFP82; co-absent with the target |
| [[VASH1]] | C | VASH1 activity raises FAM124A's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 2.56× lower at baseline in the lines without VASH1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B; co-absent with the target |
| [[RADIL]] | C | RADIL activity raises FAM124A's level | lines that do not express RADIL (21) vs lines expressing it (29) | 2.21× lower at baseline in the lines without RADIL | 0.010 | ⚠ within organs, on part of the lines; also absent: ZYG11A, OLFM1, JAKMIP1; maybe low, not absent; co-absent with the target |
| [[RAB6B]] | C | RAB6B activity raises FAM124A's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 2.83× lower at baseline in the lines without RAB6B | 0.017 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS; co-absent with the target |
| [[TTC7B]] | C | TTC7B activity raises FAM124A's level | lines that do not express TTC7B (9) vs lines expressing it (41) | 2.83× lower at baseline in the lines without TTC7B | 0.037 | ⚠ within organs, on part of the lines; also absent: SYNGR1, HDGFL3, HLTF; co-absent with the target |
| [[FHOD3]] | C | FHOD3 activity raises FAM124A's level | lines that do not express FHOD3 (14) vs lines expressing it (36) | 2.37× lower at baseline in the lines without FHOD3 | 0.037 | ⚠ within organs, on part of the lines; also absent: GJC1, ENSG00000267405, MAMLD1; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 9, C 12. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYS1]] | B | FAM124A activity raises CYS1's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 1.69× lower at baseline in the lines without FAM124A | 0.029 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1 |
| [[KIF26A]] | B | FAM124A activity raises KIF26A's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 2.17× lower at baseline in the lines without FAM124A | 0.038 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1 |
| [[LPAR3]] | B | FAM124A activity raises LPAR3's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 1.95× lower at baseline in the lines without FAM124A | 0.040 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1 |
| [[GALNT16]] | B | FAM124A activity raises GALNT16's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 1.80× lower at baseline in the lines without FAM124A | 0.068 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1 |
| [[ULK2]] | B | FAM124A activity raises ULK2's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 3.24× lower at baseline in the lines without FAM124A | 0.068 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1 |
| [[COL4A3]] | B | FAM124A activity raises COL4A3's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 2.90× lower at baseline in the lines without FAM124A | 0.079 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1 |
| [[MAP3K15]] | B | FAM124A activity raises MAP3K15's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 2.33× lower at baseline in the lines without FAM124A | 0.084 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1 |
| [[MBD5]] | B | FAM124A activity raises MBD5's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 1.31× lower at baseline in the lines without FAM124A | 0.089 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1 |
| [[WASF3]] | B | FAM124A activity raises WASF3's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 3.17× lower at baseline in the lines without FAM124A | 0.099 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1 |
| [[STOX2]] | C | FAM124A activity raises STOX2's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 4.91× lower at baseline in the lines without FAM124A | 3e-04 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1; co-absent with the target |
| [[TTC7B]] | C | FAM124A activity raises TTC7B's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 4.72× lower at baseline in the lines without FAM124A | 0.002 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1; co-absent with the target |
| [[RAB6B]] | C | FAM124A activity raises RAB6B's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 3.95× lower at baseline in the lines without FAM124A | 0.004 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.709). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.0, 40.4); signed map (26.1, 29.6). **Vector** length 49.5, 8.28% of its response variance represented; |z| ≥ 3 in 755 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +12.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.4 | +2.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.4 | +8.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.1 | -0.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.1 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.2 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -12.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.4 | -6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.3 | -8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.1 | +0.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.0 | -0.4 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 124 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.3 — chr13:51,222,334-51,284,239 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30707 |
| Matched by | ensembl_id |

UniProt [Q86V42](https://www.uniprot.org/uniprotkb/Q86V42) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26413](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26413) · Entrez [220108](https://www.ncbi.nlm.nih.gov/gene/220108) · UniProt [Q86V42](https://www.uniprot.org/uniprotkb/Q86V42) · Ensembl [ENSG00000150510](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150510)

## Data

Gene col 7440: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7440); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7440, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7440]; `tensor/DDL_lfc|DDL_z.npy` [7440]; `embed/gene_vectors.npy` [7440]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7440 or target_col == 7440). Every well: [[FAM124A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM124A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
