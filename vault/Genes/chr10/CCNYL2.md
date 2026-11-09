---
symbol: "CCNYL2"
type: "gene"
col: 11310
ensembl_id: "ENSG00000182632"
name: "cyclin Y like 2 (pseudogene)"
location: "10q11.21"
module: 108
arm: "+"
pooled_cpm: 5.2
n_lines_expressing: 21
n_dd_up: 34
n_dd_down: 8
n_dd_up_clean: 23
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 13
direction_downstream: 20
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# CCNYL2

*cyclin Y like 2 (pseudogene)* — 10q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.67× (z +18.7, q 0e+00, up in 0 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.49× (z +7.1, q 1e-10, up in 1 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.556× (z -7.4, q 8e-11, down in 12 of 17 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNYL2-1]] (+0.83, fdr 7e-06, ⚠ same locus), [[ZNF677]] (+0.65, fdr 1e-05), [[ZSCAN23]] (+0.63, fdr 4e-05), [[KCTD16]] (+0.60, fdr 3e-05); moves opposite to [[CHN2]] (-0.47, fdr 1e-04), [[FAAH2]] (-0.43, fdr 1e-04), [[GNG11]] (-0.41, fdr 3e-04).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[CATSPERB]] → it (grade B ⚠); 20 go from it, the strongest it → [[DYNC2H1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11310.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.67×** | +18.7 | 0e+00 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.37×** | +9.8 | 4e-20 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.93×** | +8.3 | 2e-14 | 1/12 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.96×** | +7.2 | 1e-10 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.1 | 1e-10 | 1/13 (SNU-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.14×** | +6.9 | 7e-10 | 1/10 (LOX-IMVI) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.70×** | +6.7 | 1e-09 | 0/11 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.61×** | +6.0 | 1e-07 | 1/12 (CHP-212) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.51×** | +5.2 | 1e-05 | 5/15 (SHP-77, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +4.7 | 1e-04 | 8/16 (SK-MEL-2, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +4.5 | 3e-04 | 0/16 | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.64×** | +4.5 | 4e-04 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +4.3 | 7e-04 | 2/13 (CHP-212, SNU-1) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.40×** | +4.2 | 9e-04 | 1/16 (A-427) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.27×** | +4.2 | 1e-03 | 2/17 (A498, SNU-423) | rises with dose | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.59×** | +4.2 | 0.001 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.002 | 2/16 (A-172, J82) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.007 | 2/16 (A-172, SHP-77) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.040 | 0/16 | inconsistent across doses |  |
| [[Elagolix sodium (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.040 | 0/16 | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.046 | 0/15 | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.051 | 8/17 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11310.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.556×** | -7.4 | 8e-11 | 12/17 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.657×** | -5.3 | 3e-05 | 11/16 (PANC-1, H4, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.720×** | -4.1 | 0.007 | 10/17 (PANC-1, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.742×** | -3.8 | 0.024 | 5/17 (A-427, J82, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.748×** | -3.7 | 0.029 | 3/17 (SNU-423, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Palmatine (chloride) (drug)]] 5 µM |  | **0.830×** | -3.3 | 0.083 | 1/16 (SHP-77) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.749×** | -3.3 | 0.083 | 0/17 | inconsistent across doses |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.834× | -3.2 | 0.085 | 3/16 (SK-MEL-2, SHP-77, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.775×** | -3.2 | 0.085 | 8/17 (PANC-1, SNU-423, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11310. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.330× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 40.2 | 0 | 4 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0546× (z -18.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 78.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 25.3 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 9.58 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 29.9 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0396× (z -15.9) |
| [[SNU-423 (line)]] | alt | 7.05 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -11.1) |
| [[A-427 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.396 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.967 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.472 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.683 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.458 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.395 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11310), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNYL2-1]] | +0.83 | +0.81 / +0.78 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF677]] | +0.65 | +0.66 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[ZSCAN23]] | +0.63 | +0.62 / +0.42 | both halves | 4e-05 | **novel candidate** |
| [[KCTD16]] | +0.60 | +0.55 / +0.45 | both halves | 3e-05 | **novel candidate** |
| [[SYT9]] | +0.58 | +0.61 / +0.40 | both halves | 4e-05 |  |
| [[ZNF208]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[ZNF439]] | +0.56 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[COX7B2]] | +0.56 | +0.51 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[SLIT3]] | +0.54 | +0.59 / +0.36 | both halves | 1e-04 |  |
| [[KC6]] | +0.54 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[FAM106A]] | +0.53 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[ZNF354C]] | +0.52 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[APBB1IP]] | +0.51 | +0.43 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHN2]] | -0.47 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[FAAH2]] | -0.43 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[GNG11]] | -0.41 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[SPATA6L]] | -0.40 | -0.26 / -0.36 | both halves | 4e-04 |  |
| [[RPH3AL]] | -0.39 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[OVOL2]] | -0.39 | -0.32 / -0.25 | both halves | 4e-04 |  |
| [[MGC32805]] | -0.39 | -0.31 / -0.28 | both halves | 3e-04 |  |
| [[BCL2L15]] | -0.38 | -0.26 / -0.26 | both halves | 4e-04 |  |
| [[CATSPERB]] | -0.38 | -0.32 / -0.36 | both halves | 1e-04 |  |
| [[LINC01814]] | -0.37 | -0.40 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 1, C 12. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CATSPERB]] | B | CATSPERB activity lowers CCNYL2's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 3.21× higher at baseline in the lines without CATSPERB | 0.097 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[COL11A1]] | C | COL11A1 activity raises CCNYL2's level | lines that do not express COL11A1 (39) vs lines expressing it (11) | 4.52× lower at baseline in the lines without COL11A1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ZNF677, THY1, LINC02566; co-absent with the target |
| [[DENND2A]] | C | DENND2A activity raises CCNYL2's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 3.63× lower at baseline in the lines without DENND2A | 0.011 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent; co-absent with the target |
| [[ZNF677]] | C | ZNF677 activity raises CCNYL2's level | lines that do not express ZNF677 (39) vs lines expressing it (11) | 4.36× lower at baseline in the lines without ZNF677 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL11A1, COL3A1, GCG; co-absent with the target |
| [[KIAA0408]] | C | KIAA0408 activity raises CCNYL2's level | lines that do not express KIAA0408 (22) vs lines expressing it (28) | 3.17× lower at baseline in the lines without KIAA0408 | 0.024 | ⚠ within organs, on part of the lines; also absent: SOGA3, ENSG00000255330, RFTN1; co-absent with the target |
| [[COX7B2]] | C | COX7B2 activity raises CCNYL2's level | lines that do not express COX7B2 (42) vs lines expressing it (8) | 2.71× lower at baseline in the lines without COX7B2 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000285751, GCG, LINC01205; co-absent with the target |
| [[SLC8A1]] | C | SLC8A1 activity raises CCNYL2's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 3.30× lower at baseline in the lines without SLC8A1 | 0.038 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3; co-absent with the target |
| [[CARD18]] | C | CARD18 activity raises CCNYL2's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 1.47× lower at baseline in the lines without CARD18 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10; co-absent with the target |
| [[SOGA3]] | C | SOGA3 activity raises CCNYL2's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 2.99× lower at baseline in the lines without SOGA3 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1; co-absent with the target |
| [[ADAMTS2]] | C | ADAMTS2 activity raises CCNYL2's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 3.01× lower at baseline in the lines without ADAMTS2 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1; co-absent with the target |
| [[LINC01615]] | C | LINC01615 activity raises CCNYL2's level | lines that do not express LINC01615 (36) vs lines expressing it (14) | 2.81× lower at baseline in the lines without LINC01615 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC; co-absent with the target |
| [[ZSCAN23]] | C | ZSCAN23 activity raises CCNYL2's level | lines that do not express ZSCAN23 (23) vs lines expressing it (27) | 2.02× lower at baseline in the lines without ZSCAN23 | 0.090 | ⚠ within organs, on part of the lines; also absent: TRHDE, SUSD5, EDIL3; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 3, C 17. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNC2H1]] | B | CCNYL2, [[CCNYL2-1]] activity raises DYNC2H1's level | lines that do not express CCNYL2, CCNYL2-1 (29) vs lines expressing them (21) | 2.55× lower at baseline in the lines without CCNYL2, CCNYL2-1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent genes |
| [[EVC]] | B | CCNYL2 activity raises EVC's level | lines that do not express CCNYL2 (29) vs lines expressing it (21) | 3.81× lower at baseline in the lines without CCNYL2 | 0.032 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1 |
| [[C19orf33]] | B | CCNYL2 activity lowers C19orf33's level | lines that do not express CCNYL2 (29) vs lines expressing it (21) | 2.87× higher at baseline in the lines without CCNYL2 | 0.082 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1 |
| [[BVES-AS1]] | C | CCNYL2, [[CCNYL2-1]] activity raises BVES-AS1's level | lines that do not express CCNYL2, CCNYL2-1 (29) vs lines expressing them (21) | 1.86× lower at baseline in the lines without CCNYL2, CCNYL2-1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target; co-absent genes |
| [[KC6]] | C | CCNYL2 activity raises KC6's level | lines that do not express CCNYL2 (29) vs lines expressing it (21) | 4.83× lower at baseline in the lines without CCNYL2 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target |
| [[PRR16]] | C | CCNYL2 activity raises PRR16's level | lines that do not express CCNYL2 (29) vs lines expressing it (21) | 8.31× lower at baseline in the lines without CCNYL2 | 0.015 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target |
| [[KCTD16]] | C | CCNYL2, [[CCNYL2-1]] activity raises KCTD16's level | lines that do not express CCNYL2, CCNYL2-1 (29) vs lines expressing them (21) | 4.27× lower at baseline in the lines without CCNYL2, CCNYL2-1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target; co-absent genes |
| [[GLIS1]] | C | CCNYL2 activity raises GLIS1's level | lines that do not express CCNYL2 (29) vs lines expressing it (21) | 3.68× lower at baseline in the lines without CCNYL2 | 0.019 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target |
| [[ZNF677]] | C | CCNYL2, [[CCNYL2-1]] activity raises ZNF677's level | lines that do not express CCNYL2, CCNYL2-1 (29) vs lines expressing them (21) | 3.08× lower at baseline in the lines without CCNYL2, CCNYL2-1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target; co-absent genes |
| [[CARD18]] | C | CCNYL2, [[CCNYL2-1]] activity raises CARD18's level | lines that do not express CCNYL2, CCNYL2-1 (29) vs lines expressing them (21) | 1.88× lower at baseline in the lines without CCNYL2, CCNYL2-1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target; co-absent genes |
| [[COL11A1]] | C | CCNYL2 activity raises COL11A1's level | lines that do not express CCNYL2 (29) vs lines expressing it (21) | 3.64× lower at baseline in the lines without CCNYL2 | 0.036 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target |
| [[LINC02377]] | C | CCNYL2 activity raises LINC02377's level | lines that do not express CCNYL2 (29) vs lines expressing it (21) | 3.62× lower at baseline in the lines without CCNYL2 | 0.041 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (50.4, 23.7); signed map (31.3, 45.9). **Vector** length 40.9, 9.53% of its response variance represented; |z| ≥ 3 in 431 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +18.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +8.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.7 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.9 | +0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.8 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.7 | -0.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | -1.4 | -3.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.3 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -2.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.8 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | -5.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.8 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.8 | -0.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.6 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | cyclin Y like 2 (pseudogene) |
| Locus type | pseudogene |
| Location | 10q11.21 — chr10:42,409,727-42,454,385 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | bA178A10.2, CCNYL2P; previously C10orf21 |
| Gene groups (HGNC) | Cyclins |
| Matched by | ensembl_id |

UniProt [Q5T2Q4](https://www.uniprot.org/uniprotkb/Q5T2Q4) carries no function annotation.

**Summary**, from NCBI Gene [414194](https://www.ncbi.nlm.nih.gov/gene/414194):

> Predicted to enable cyclin-dependent protein serine/threonine kinase activator activity. Predicted to be involved in regulation of canonical Wnt signaling pathway. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23495](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23495) · Entrez [414194](https://www.ncbi.nlm.nih.gov/gene/414194) · UniProt [Q5T2Q4](https://www.uniprot.org/uniprotkb/Q5T2Q4) · Ensembl [ENSG00000182632](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182632)

## Data

Gene col 11310: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11310); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11310, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11310]; `tensor/DDL_lfc|DDL_z.npy` [11310]; `embed/gene_vectors.npy` [11310]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11310 or target_col == 11310). Every well: [[CCNYL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNYL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
