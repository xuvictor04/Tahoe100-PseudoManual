---
symbol: "ODAD4"
type: "gene"
col: 12921
ensembl_id: "ENSG00000204815"
name: "outer dynein arm docking complex subunit 4"
location: "17q21.2"
module: 17
arm: "+"
pooled_cpm: 5.01
n_lines_expressing: 46
n_dd_up: 16
n_dd_down: 14
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ODAD4

*outer dynein arm docking complex subunit 4* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.39× (z +14.7, q 0e+00, up in 6 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.74× (z +7.0, q 6e-10, up in 23 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.349× (z -13.2, q 9e-37, down in 33 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPHP1]] (+0.63, fdr 7e-06), [[ANKRD24]] (+0.57, fdr 3e-05), [[BBOF1]] (+0.53, fdr 3e-05); moves opposite to [[DUSP22]] (-0.46, fdr 7e-05), [[TBC1D1]] (-0.45, fdr 1e-04), [[SGMS1]] (-0.44, fdr 2e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[DPY19L2P2-1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[OSCP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12921.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.39×** | +14.7 | 0e+00 | 6/8 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +7.1 | 3e-10 | 10/24 (NCI-H2030, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.74×** | +7.0 | 6e-10 | 23/43 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +6.3 | 6e-08 | 19/40 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +5.2 | 1e-05 | 2/10 (NCI-H2030, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +5.2 | 1e-05 | 17/42 (HT-29, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +5.1 | 3e-05 | 9/38 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.50×** | +5.1 | 3e-05 | 9/39 (SW480, C-33 A, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.5 | 5e-04 | 10/36 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.005 | 8/42 (A-172, NCI-H23, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +3.7 | 0.011 | 7/43 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.015 | 3/27 (C32, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.024 | 9/41 (hTERT-HPNE, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.028 | 6/40 (A-172, NCI-H1573, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.2 | 0.050 | 5/43 (A498, HS-578T, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.075 | 5/31 (NCI-H460, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12921.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.349×** | -13.2 | 9e-37 | 33/43 (H4, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.482×** | -9.1 | 2e-17 | 24/33 (HS-578T, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.499×** | -8.7 | 6e-16 | 23/40 (CHP-212, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.513×** | -8.4 | 9e-15 | 22/40 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.594×** | -6.5 | 9e-09 | 19/43 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.676×** | -4.9 | 1e-04 | 14/39 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.759×** | -4.9 | 1e-04 | 16/43 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.691×** | -4.6 | 3e-04 | 11/35 (HT-29, PANC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.712×** | -4.2 | 0.001 | 14/39 (H4, HEC-1-A, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.712×** | -4.2 | 0.001 | 15/40 (HT-29, A-172, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.720×** | -4.1 | 0.002 | 13/41 (SNU-423, NCI-H23, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.750×** | -3.6 | 0.016 | 13/42 (NCI-H460, SNU-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.754×** | -3.4 | 0.031 | 11/39 (A498, NCI-H23, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.774×** | -3.2 | 0.057 | 11/44 (C-33 A, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12921. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 12.7 | 0 | 6 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0409× (z -11.7) |
| [[C32 (line)]] | wt | 9.47 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0877× (z -9.8) ⚠ transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0959× (z -9.4) |
| [[HS-578T (line)]] | alt | 12.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0325× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.169× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 6.15 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 7.92× (z +8.7) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.112× (z -9.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 4.42 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.113× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 14.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0916× (z -12.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.23 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0587× (z -12.6) |
| [[HOP62 (line)]] | alt | 7.19 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 4.61 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0784× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.167× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~10% of this change |
| [[RPMI-7951 (line)]] | alt | 9.31 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0713× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.750 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12921), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHP1]] | +0.63 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[ANKRD24]] | +0.57 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[BBOF1]] | +0.53 | +0.60 / +0.45 | both halves | 3e-05 | STRING 408 |
| [[ODR4]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[LINC00888-1]] | +0.52 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[GNG7]] | +0.52 | +0.63 / +0.37 | both halves | 8e-05 |  |
| [[ZNF404]] | +0.52 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[CWC25]] | +0.51 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[CCDC180]] | +0.51 | +0.56 / +0.37 | both halves | 8e-05 |  |
| [[BRSK1]] | +0.50 | +0.41 / +0.33 | both halves | 1e-04 |  |
| [[POTEF]] | +0.49 | +0.44 / +0.27 | both halves | 3e-04 |  |
| [[FAM161B]] | +0.48 | +0.45 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP22]] | -0.46 | -0.51 / -0.37 | both halves | 7e-05 |  |
| [[TBC1D1]] | -0.45 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[SGMS1]] | -0.44 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[DOCK9]] | -0.43 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[RFLNB]] | -0.43 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[CMTM4]] | -0.42 | -0.52 / -0.29 | both halves | 3e-04 |  |
| [[FAM135A]] | -0.42 | -0.44 / -0.26 | both halves | 4e-04 |  |
| [[MAN2A1]] | -0.42 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[RAN]] | -0.42 | -0.23 / -0.45 | both halves | 5e-04 |  |
| [[JADE3]] | -0.41 | -0.29 / -0.40 | both halves | 3e-04 |  |
| [[TBC1D4]] | -0.41 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[TXN]] | -0.40 | -0.44 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPY19L2P2-1]] | B | DPY19L2P2-1 activity raises ODAD4's level | lines that do not express DPY19L2P2-1 (17) vs lines expressing it (33) | 1.91× lower at baseline in the lines without DPY19L2P2-1 | 0.032 | ⚠ within organs, on part of the lines; also absent: RNF182, ENSG00000234405, FGF2 |
| [[BRSK1]] | B | BRSK1 activity raises ODAD4's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 2.34× lower at baseline in the lines without BRSK1 | 0.063 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[KDM2B-DT]] | C | KDM2B-DT activity raises ODAD4's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 2.30× lower at baseline in the lines without KDM2B-DT | 0.023 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent; co-absent with the target |
| [[CLIP3]] | C | CLIP3 activity raises ODAD4's level | lines that do not express CLIP3 (4) vs lines expressing it (46) | 1.60× lower at baseline in the lines without CLIP3 | 0.077 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RAPGEF4, MEGF11, TMEM170B; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSCP1]] | C | ODAD4 activity raises OSCP1's level | lines that do not express ODAD4 (4) vs lines expressing it (46) | 1.90× lower at baseline in the lines without ODAD4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: GGT7, NAT14, SOGA1; its own permutation p |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.320). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-34.5, 27.7); signed map (-6.9, -2.1). **Vector** length 54.2, 7.68% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +5.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | -0.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +0.8 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +0.9 | +1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +3.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -8.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.1 | -8.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.0 | -0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -13.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -4.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.1 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | outer dynein arm docking complex subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:41,930,617-41,966,503 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434H0115; previously TTC25 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Outer dynein arm docking complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NG3](https://www.uniprot.org/uniprotkb/Q96NG3) (Outer dynein arm-docking complex subunit 4):

> Component of the outer dynein arm-docking complex (ODA-DC) that mediates outer dynein arms (ODA) binding onto the doublet microtubule. Plays an essential role for the assembly of ODA-DC and for the docking of ODA in ciliary axoneme.

**Summary**, from NCBI Gene [83538](https://www.ncbi.nlm.nih.gov/gene/83538):

> This gene encodes a tetratricopeptide repeat domain-containing protein that localizes to ciliary axonmenes and plays a role in the docking of the outer dynein arm to cilia. Mutations in this gene cause severely reduced ciliary motility and the disorder CILD35 (ciliary dyskinesia,primary, 35). Primary ciliary dyskinesia is often associated with recurrent respiratory infections, immotile spermatozoa, and situs inversus; an inversion in left-right body symmetry. Alternative splicing results in …

**Accessions** — [HGNC:25280](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25280) · Entrez [83538](https://www.ncbi.nlm.nih.gov/gene/83538) · UniProt [Q96NG3](https://www.uniprot.org/uniprotkb/Q96NG3) · Ensembl [ENSG00000204815](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204815)

## Data

Gene col 12921: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12921); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12921, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12921]; `tensor/DDL_lfc|DDL_z.npy` [12921]; `embed/gene_vectors.npy` [12921]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12921 or target_col == 12921). Every well: [[ODAD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ODAD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
