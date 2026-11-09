---
symbol: "ST6GALNAC6"
type: "gene"
col: 8347
ensembl_id: "ENSG00000160408"
name: "ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 6"
location: "9q34.11"
module: 2
arm: "+"
pooled_cpm: 9.33
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ST6GALNAC6

*ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 6* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.44× (z +6.4, q 8e-08, up in 19 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.421× (z -21.5, q 0e+00, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST6GALNAC4]] (+0.76, fdr 7e-06, ⚠ same locus), [[TRABD]] (+0.75, fdr 7e-06), [[ZDHHC8]] (+0.75, fdr 7e-06), [[IMPDH1]] (+0.74, fdr 7e-06); moves opposite to [[ZNF518A]] (-0.71, fdr 7e-06), [[BAZ2B]] (-0.71, fdr 2e-05), [[FAM111A]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8347.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +6.4 | 8e-08 | 19/47 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.88×** | +5.8 | 2e-06 | 7/31 (Panc 03.27, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +5.6 | 3e-06 | 14/40 (A-172, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +5.4 | 9e-06 | 12/47 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.3 | 2e-05 | 4/17 (HS-578T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.21×** | +4.6 | 3e-04 | 7/48 (LoVo, AsPC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +4.5 | 6e-04 | 13/47 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +4.1 | 0.003 | 11/44 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.24×** | +3.8 | 0.011 | 12/32 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.4 | 0.033 | 1/48 (BT-474) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.042 | 2/43 (MIA PaCa-2, KATO III) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.20×** | +3.2 | 0.063 | 7/42 (SNU-1, HOP62, …) | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.089 | 10/44 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8347.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.421×** | -21.5 | 0e+00 | 39/45 (BT-474, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.378×** | -16.4 | 0e+00 | 36/45 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.591×** | -9.2 | 6e-18 | 25/43 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.624×** | -8.3 | 2e-14 | 24/47 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.649×** | -7.6 | 4e-12 | 24/46 (A-172, J82, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.671×** | -7.0 | 3e-10 | 24/46 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.679×** | -6.8 | 1e-09 | 20/46 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.479×** | -6.7 | 1e-09 | 20/47 (MIA PaCa-2, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.691×** | -6.5 | 6e-09 | 22/47 (HT-29, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.779×** | -6.2 | 3e-08 | 19/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.783×** | -6.1 | 7e-08 | 23/43 (RKO, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.734×** | -5.4 | 3e-06 | 17/46 (H4, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.743×** | -5.0 | 2e-05 | 19/43 (BT-474, SW48, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.762×** | -4.8 | 8e-05 | 14/47 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.774×** | -4.5 | 3e-04 | 15/47 (H4, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Hexylresorcinol (drug)]] 0.5 µM |  | **0.792×** | -4.1 | 0.002 | 12/48 (CHP-212, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.658×** | -3.8 | 0.004 | 10/42 (COLO 205, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.820×** | -3.5 | 0.014 | 6/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8347. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 34.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -12.3) |
| [[J82 (line)]] | alt | 15.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -11.0) |
| [[A-172 (line)]] | wt | 19.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -10.8) |
| [[HT-29 (line)]] | alt | 9.03 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 26.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.163× (z -12.9) |
| [[SW480 (line)]] | alt | 6.21 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.172× (z -9.9) |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 5.56 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -10.6) |
| [[PANC-1 (line)]] | alt | 9.10 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -11.2) |
| [[A-427 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8347), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC4]] | +0.76 | +0.72 / +0.64 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; ⚠ same locus (2.5 kb, same strand: neighbours can correlate without regulation) |
| [[TRABD]] | +0.75 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[ZDHHC8]] | +0.75 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[IMPDH1]] | +0.74 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[LPCAT1]] | +0.73 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[ST6GALNAC6-1]] | +0.73 | +0.67 / +0.70 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ANKRD27]] | +0.72 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[INTS11]] | +0.70 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[LIMK1]] | +0.70 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[PACC1]] | +0.68 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[NEIL2]] | +0.68 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[CCNB1IP1]] | +0.68 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[USP35]] | +0.68 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[FPGS]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF518A]] | -0.71 | -0.67 / -0.58 | both halves | 7e-06 |  |
| [[BAZ2B]] | -0.71 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[FAM111A]] | -0.67 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[CASD1]] | -0.65 | -0.52 / -0.44 | both halves | 3e-05 | STRING 423 |
| [[HMGN2]] | -0.64 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[PNRC2]] | -0.64 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[WAC-AS1]] | -0.64 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[TIA1]] | -0.63 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[CGGBP1]] | -0.63 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[UNK]] | -0.63 | -0.64 / -0.36 | both halves | 1e-04 |  |
| [[ANKRD26]] | -0.63 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[CASC9]] | -0.63 | -0.59 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ST6GALNAC6's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BRSK2]] | B | BRSK2 activity raises ST6GALNAC6's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.19× lower at baseline in the lines without BRSK2 | 0.063 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[S100A14]] | B | S100A14 activity lowers ST6GALNAC6's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 1.30× higher at baseline in the lines without S100A14 | 0.072 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.705). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-0.4, 0.5); signed map (-42.6, -6.6). **Vector** length 71.0, 11.2% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.3 | +5.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.2 | +4.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.2 | +6.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +1.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.6 | +4.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -16.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -21.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -9.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.1 | -6.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -4.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.5 | -3.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:127,885,321-127,905,408 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ST6GALNACVI; previously SIAT7F |
| Gene groups (HGNC) | Sialyltransferases |
| Reactome | 11 pathways, smallest: Lewis blood group biosynthesis; Blood group systems biosynthesis; Glycosphingolipid biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969X2](https://www.uniprot.org/uniprotkb/Q969X2) (Alpha-N-acetylgalactosaminide alpha-2,6-sialyltransferase 6):

> Transfers the sialyl group (N-acetyl-alpha-neuraminyl or NeuAc) from CMP-NeuAc onto glycoproteins and glycolipids, forming an alpha-2,6-linkage. Produces branched type disialyl structures by transfer of a sialyl group onto the GalNAc or GlcNAc residue inside backbone core chains having a terminal sialic acid with an alpha-2,3-linkage on Gal. ST6GalNAcVI prefers glycolipids to glycoproteins, predominantly catalyzing the biosynthesis of ganglioside GD1alpha from GM1b. Besides GMb1, MSGG and other …

**Summary**, from NCBI Gene [30815](https://www.ncbi.nlm.nih.gov/gene/30815):

> ST6GALNAC6 belongs to a family of sialyltransferases that modify proteins and ceramides on the cell surface to alter cell-cell or cell-extracellular matrix interactions (Tsuchida et al., 2003 [PubMed 12668675]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:23364](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23364) · Entrez [30815](https://www.ncbi.nlm.nih.gov/gene/30815) · UniProt [Q969X2](https://www.uniprot.org/uniprotkb/Q969X2) · Ensembl [ENSG00000160408](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160408)

## Data

Gene col 8347: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8347); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8347, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8347]; `tensor/DDL_lfc|DDL_z.npy` [8347]; `embed/gene_vectors.npy` [8347]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8347 or target_col == 8347). Every well: [[ST6GALNAC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST6GALNAC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
