---
symbol: "CX3CL1"
type: "gene"
col: 106
ensembl_id: "ENSG00000006210"
name: "C-X3-C motif chemokine ligand 1"
location: "16q21"
module: 14
arm: "+"
pooled_cpm: 5.58
n_lines_expressing: 22
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 17
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CX3CL1

*C-X3-C motif chemokine ligand 1* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.87× (z +21.9, q 0e+00, up in 17 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 2 lines (PANC-1 0.104×, SW 900 0.0413×; ⚠ cell-cycle shift, explains ~75% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (PANC-1 0.166×); [[Panobinostat (drug)]] 5 µM in 1 line (PANC-1 0.0965×; ⚠ cell-cycle shift, explains ~34% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (PANC-1 0.149×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (PANC-1 0.156×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFAIP2]] (+0.74, fdr 7e-06), [[STAT5A]] (+0.73, fdr 7e-06), [[BCL3]] (+0.72, fdr 7e-06); moves opposite to [[ZCCHC17]] (-0.62, fdr 2e-05), [[ZNF731P]] (-0.57, fdr 2e-05), [[VPS53]] (-0.57, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ADGRG1]] → it (grade B ⚠); 17 go from it, the strongest it → [[RND1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 106.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.87×** | +21.9 | 0e+00 | 17/17 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.53×** | +13.2 | 3e-37 | 18/18 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.29×** | +11.7 | 3e-29 | 12/16 (HEC-1-A, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.30×** | +9.6 | 2e-19 | 2/11 (A498, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.28×** | +9.2 | 6e-18 | 1/7 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.08×** | +9.0 | 2e-17 | 11/16 (BT-474, SW 900, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.11×** | +8.4 | 3e-15 | 16/19 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.55×** | +6.9 | 3e-10 | 1/8 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.33×** | +6.8 | 8e-10 | 13/19 (SW 900, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.02×** | +5.6 | 1e-06 | 10/17 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +5.3 | 6e-06 | 2/12 (SW480, SW 900) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.92×** | +5.2 | 9e-06 | 9/19 (BT-474, SW 900, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +5.0 | 3e-05 | 6/14 (SW 900, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.77×** | +4.6 | 2e-04 | 3/11 (HepG2/C3A, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **2.95×** | +4.3 | 5e-04 | 10/18 (BT-474, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.12×** | +4.3 | 6e-04 | 1/14 (HT-29) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.010 | 6/19 (CHP-212, HepG2/C3A, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.83×** | +3.5 | 0.015 | 2/12 (A498, HS-578T) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Flutamide (drug)]] 0.5 µM |  | **1.54×** | +3.4 | 0.016 | 0/19 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.018 | 2/15 (A498, HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.76×** | +3.2 | 0.028 | 2/14 (HepG2/C3A, CFPAC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Roxadustat (drug)]] 0.05 µM |  | **1.54×** | +3.2 | 0.030 | 2/16 (SW480, CHP-212) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 106.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 2 lines (PANC-1 0.104×, SW 900 0.0413×; ⚠ cell-cycle shift, explains ~75% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (PANC-1 0.166×); [[Panobinostat (drug)]] 5 µM in 1 line (PANC-1 0.0965×; ⚠ cell-cycle shift, explains ~34% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (PANC-1 0.149×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (PANC-1 0.156×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.627× | -3.5 | 0.23 | 1/19 (CHP-212) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.668× | -3.2 | 0.23 | 8/17 (HEC-1-A, HS-578T, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.669× | -3.2 | 0.23 | 5/19 (NCI-H2347, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 106. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 32.3 | 2 | 8 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 12.9× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 1.97 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.7× (z +12.5) | — |
| [[HepG2_C3A (line)]] | wt | 25.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.0× (z +18.1) | — |
| [[SW 900 (line)]] | alt | 9.09 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.30× (z +11.2) | [[Bortezomib (drug)]] 0.05 µM 0.0413× (z -11.4) ⚠ cell-cycle shift, explains ~75% of this change |
| [[BT-474 (line)]] | alt | 97.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.09× (z +8.5) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.133× (z -11.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 10.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.8× (z +18.7) | — |
| [[HT-29 (line)]] | alt | 3.42 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.39× (z +8.8) | [[Panobinostat (drug)]] 0.05 µM 0.0400× (z -9.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SK-MEL-2 (line)]] | alt | 3.76 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 28.7× (z +8.5) | — |
| [[A-172 (line)]] | wt | 0.670 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.304 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.837 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.759 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.722 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.391 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.545 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.633 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.409 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.450 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.567 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 106), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFAIP2]] | +0.74 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[STAT5A]] | +0.73 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[BCL3]] | +0.72 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[NFKBIA]] | +0.70 | +0.62 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[SLC2A6]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[CSF1]] | +0.68 | +0.54 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 605 |
| [[STAP2]] | +0.67 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[ANO9]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[ARHGEF40]] | +0.66 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[TEF]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[SYNPO]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[EBI3]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC17]] | -0.62 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[ZNF731P]] | -0.57 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[VPS53]] | -0.57 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[CTDP1]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[UFD1]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[BCAP31]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRG1]] | B | ADGRG1 activity raises CX3CL1's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 2.53× lower at baseline in the lines without ADGRG1 | 0.021 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[ANO9]] | B | ANO9 activity raises CX3CL1's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 1.97× lower at baseline in the lines without ANO9 | 0.054 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[LGALS3]] | B | LGALS3 activity raises CX3CL1's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 2.42× lower at baseline in the lines without LGALS3 | 0.085 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[MARCKS]] | B | MARCKS activity raises CX3CL1's level | lines that do not express MARCKS (10) vs lines expressing it (40) | 2.44× lower at baseline in the lines without MARCKS | 0.097 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RND1]] | B | CX3CL1 activity raises RND1's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 1.96× lower at baseline in the lines without CX3CL1 | 0.008 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[RASSF5]] | B | CX3CL1 activity raises RASSF5's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 1.86× lower at baseline in the lines without CX3CL1 | 0.009 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[TSPAN15]] | B | CX3CL1 activity raises TSPAN15's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 1.96× lower at baseline in the lines without CX3CL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[ADGRG1]] | B | CX3CL1 activity raises ADGRG1's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 2.88× lower at baseline in the lines without CX3CL1 | 0.020 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[SLC12A7]] | B | CX3CL1 activity raises SLC12A7's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 1.63× lower at baseline in the lines without CX3CL1 | 0.025 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[PIM3]] | B | CX3CL1 activity raises PIM3's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 1.37× lower at baseline in the lines without CX3CL1 | 0.030 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[LITAF]] | B | CX3CL1 activity raises LITAF's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 1.82× lower at baseline in the lines without CX3CL1 | 0.030 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[GABBR1]] | B | CX3CL1 activity strengthens GABBR1's drug response | lines that do not express CX3CL1 (24) vs lines expressing it (17) | the lines without CX3CL1 respond 0.75× as strongly (z diff +0.68); strongest at Homoharringtonine 5 µM: 0.96x vs 1.99x (z diff +6.3) | 0.033 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB; target measured in part of the lines; both ways; artifact flags |
| [[ANO9]] | B | CX3CL1 activity raises ANO9's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 1.61× lower at baseline in the lines without CX3CL1 | 0.041 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[IL23A]] | B | CX3CL1 activity raises IL23A's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 1.42× lower at baseline in the lines without CX3CL1 | 0.045 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[LGALS3]] | B | CX3CL1 activity raises LGALS3's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 2.28× lower at baseline in the lines without CX3CL1 | 0.053 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[FRMD4B]] | B | CX3CL1 activity raises FRMD4B's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 2.03× lower at baseline in the lines without CX3CL1 | 0.055 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.815). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.2, 4.9); signed map (43.9, 7.0). **Vector** length 51.2, 12.7% of its response variance represented; |z| ≥ 3 in 461 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.54 to 43); *NF-kB* (control, mean cos +0.58 to 12); *Interleukin-10 signaling* (reactome, mean cos +0.51 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.0 | +13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +21.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.5 | +11.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +0.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.4 | +2.4 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.1 | -0.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~75% of this change | -2.1 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -2.7 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.2 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -0.0 |
|  | [[EX229 (drug)]] 5 µM |  | -1.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | C-X3-C motif chemokine ligand 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:57,372,477-57,385,044 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NTN, C3Xkine, ABCD-3, CXC3C, CXC3; previously SCYD1 |
| Gene groups (HGNC) | Chemokine ligands |
| Hallmark sets | APICAL_SURFACE, INFLAMMATORY_RESPONSE, APICAL_JUNCTION |
| Reactome | 7 pathways, smallest: Chemokine receptors bind chemokines; Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [P78423](https://www.uniprot.org/uniprotkb/P78423) (Fractalkine):

> Chemokine that acts as a ligand for both CX3CR1 and integrins ITGAV:ITGB3 and ITGA4:ITGB1. The CX3CR1-CX3CL1 signaling exerts distinct functions in different tissue compartments, such as immune response, inflammation, cell adhesion and chemotaxis. Regulates leukocyte adhesion and migration processes at the endothelium. Can activate integrins in both a CX3CR1-dependent and CX3CR1-independent manner. In the presence of CX3CR1, activates integrins by binding to the classical ligand-binding site …

**Summary**, from NCBI Gene [6376](https://www.ncbi.nlm.nih.gov/gene/6376):

> This gene belongs to the CX3C subgroup of chemokines, characterized by the number of amino acids located between the conserved cysteine residues. This is the only member of the CX3C subgroup, which contains three amino acids between cysteine residues, resulting in a Cys-X-X-X-Cys configuration. The encoded protein contains an extended mucin-like stalk with a chemokine domain on top, and exists in both a membrane-anchored form where it acts as a binding molecule, or, in soluble form, as a …

**Accessions** — [HGNC:10647](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10647) · Entrez [6376](https://www.ncbi.nlm.nih.gov/gene/6376) · UniProt [P78423](https://www.uniprot.org/uniprotkb/P78423) · Ensembl [ENSG00000006210](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006210)

## Data

Gene col 106: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 106); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 106, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 106]; `tensor/DDL_lfc|DDL_z.npy` [106]; `embed/gene_vectors.npy` [106]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 106 or target_col == 106). Every well: [[CX3CL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CX3CL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
