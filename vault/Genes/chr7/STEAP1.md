---
symbol: "STEAP1"
type: "gene"
col: 8979
ensembl_id: "ENSG00000164647"
name: "STEAP family member 1"
location: "7q21.13"
module: 1
arm: "+"
pooled_cpm: 6.92
n_lines_expressing: 39
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 7
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# STEAP1

*STEAP family member 1* — 7q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.76× (z +8.8, q 7e-16, up in 18 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 2.97× (z +4.9, q 9e-05, up in 15 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.517× (z -8.1, q 4e-13, down in 26 of 32 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STEAP2]] (+0.57, fdr 1e-05, ⚠ same locus), [[WDR75]] (+0.50, fdr 3e-04), [[MRPL15]] (+0.49, fdr 5e-05), [[ZNF485]] (+0.49, fdr 1e-04); moves opposite to [[MXD4]] (-0.48, fdr 6e-05), [[IFT140]] (-0.45, fdr 1e-04), [[FANK1]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ARHGEF5]], [[ARHGEF34P]] → it (grade B ⚠); 7 go from it, the strongest it → [[YPEL5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8979.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.76×** | +8.8 | 7e-16 | 18/24 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +8.4 | 2e-14 | 11/13 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.18×** | +6.8 | 2e-09 | 24/35 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +5.8 | 9e-07 | 13/24 (SNU-423, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.97×** | +4.9 | 9e-05 | 15/31 (A498, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **2.80×** | +4.7 | 3e-04 | 18/30 (A498, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +4.5 | 5e-04 | 18/36 (KATO III, A498, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.68×** | +4.5 | 5e-04 | 14/26 (SW1417, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.65×** | +4.4 | 6e-04 | 17/30 (A498, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **2.46×** | +4.1 | 0.003 | 14/27 (A498, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **2.23×** | +3.6 | 0.014 | 12/25 (A498, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.021 | 14/34 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **2.13×** | +3.4 | 0.025 | 13/29 (PANC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.53×** | +3.4 | 0.025 | 7/15 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8979.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.517×** | -8.1 | 4e-13 | 26/32 (NCI-H1573, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.507×** | -5.5 | 8e-06 | 20/32 (SW48, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.574×** | -4.8 | 3e-04 | 16/35 (RKO, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.419×** | -3.9 | 0.010 | 16/32 (SW48, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.420×** | -3.9 | 0.010 | 16/31 (NCI-H2030, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.650×** | -3.7 | 0.019 | 16/34 (SW48, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.653×** | -3.7 | 0.019 | 16/34 (SW48, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.668×** | -3.5 | 0.036 | 12/35 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.695× | -3.1 | 0.11 | 14/31 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | 0.700× | -3.1 | 0.12 | 4/36 (SW480, NCI-H2030, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8979. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 34.1 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.121× (z -10.5) |
| [[KATO III (line)]] | alt | 6.30 | 0 | 2 | — | [[Orlistat (drug)]] 0.05 µM 0.0597× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -13.3) |
| [[A498 (line)]] | wt | 6.79 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -12.7) |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 9.85 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -9.3) |
| [[PANC-1 (line)]] | alt | 5.82 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -10.5) |
| [[A-172 (line)]] | wt | 0.896 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.732 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.873 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.666 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8979), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STEAP2]] | +0.57 | +0.57 / +0.54 | both halves | 1e-05 | same gene group; STRING 979; ⚠ same locus (2.8 kb, same strand: neighbours can correlate without regulation) |
| [[WDR75]] | +0.50 | +0.28 / +0.57 | both halves | 3e-04 |  |
| [[MRPL15]] | +0.49 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[ZNF485]] | +0.49 | +0.34 / +0.46 | both halves | 1e-04 |  |
| [[NOC3L]] | +0.48 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[GRPEL2]] | +0.47 | +0.37 / +0.47 | both halves | 9e-05 |  |
| [[SLC38A1]] | +0.47 | +0.56 / +0.32 | both halves | 2e-04 |  |
| [[WDR17]] | +0.47 | +0.34 / +0.45 | both halves | 1e-04 |  |
| [[MKKS]] | +0.47 | +0.27 / +0.54 | both halves | 3e-04 |  |
| [[C5orf63]] | +0.45 | +0.47 / +0.36 | both halves | 1e-04 |  |
| [[LRRC8D]] | +0.45 | +0.36 / +0.37 | both halves | 1e-04 |  |
| [[LYAR]] | +0.44 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[PROSER1]] | +0.44 | +0.36 / +0.37 | both halves | 9e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXD4]] | -0.48 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[IFT140]] | -0.45 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[FANK1]] | -0.45 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[FBXL20]] | -0.43 | -0.25 / -0.49 | both halves | 4e-04 |  |
| [[ZER1]] | -0.42 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[BSDC1]] | -0.42 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[MOB2]] | -0.42 | -0.13 / -0.53 | ⚠ one half (not replicated) | 0.002 |  |
| [[WDTC1]] | -0.42 | -0.20 / -0.53 | both halves | 7e-04 |  |
| [[HAGH]] | -0.42 | -0.29 / -0.38 | both halves | 2e-04 |  |
| [[UBXN6]] | -0.42 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[OTUD5]] | -0.41 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[YPEL5]] | -0.41 | -0.23 / -0.53 | both halves | 5e-04 |  |
| [[ATG14]] | -0.41 | -0.30 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF5]], [[ARHGEF34P]] | B | ARHGEF5, ARHGEF34P activity raises STEAP1's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 2.49× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[IL18R1]] | B | IL18R1 activity raises STEAP1's level | lines that do not express IL18R1 (15) vs lines expressing it (35) | 1.49× lower at baseline in the lines without IL18R1 | 0.028 | ⚠ within organs, on part of the lines; also absent: JCAD |
| [[ACSL5]] | B | ACSL5 activity raises STEAP1's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 2.23× lower at baseline in the lines without ACSL5 | 0.081 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1 |
| [[PSMB5]] | B | PSMB5 activity raises STEAP1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[STEAP2-AS1]] | C | STEAP2-AS1 activity raises STEAP1's level | lines that do not express STEAP2-AS1 (12) vs lines expressing it (38) | 3.42× lower at baseline in the lines without STEAP2-AS1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: STEAP2, STEAP1, FCGRT; maybe low, not absent; co-absent with the target |
| [[STEAP2]] | C | STEAP2 activity raises STEAP1's level | lines that do not express STEAP2 (11) vs lines expressing it (39) | 3.28× lower at baseline in the lines without STEAP2 | 0.002 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP1, FCGRT; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YPEL5]] | B | STEAP1 activity raises YPEL5's level | lines that do not express STEAP1 (11) vs lines expressing it (39) | 1.36× lower at baseline in the lines without STEAP1 | 0.042 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP2 |
| [[ACSL5]] | B | STEAP1 activity raises ACSL5's level | lines that do not express STEAP1 (11) vs lines expressing it (39) | 3.75× lower at baseline in the lines without STEAP1 | 0.060 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP2 |
| [[HAGH]] | B | STEAP1 activity lowers HAGH's level | lines that do not express STEAP1 (11) vs lines expressing it (39) | 1.26× higher at baseline in the lines without STEAP1 | 0.071 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP2 |
| cells under [[palbociclib (drug)]] 5 µM | B | STEAP1 activity raises the cells' numbers under palbociclib 5 µM (protects the cells) | lines that do not express STEAP1 (11) vs lines expressing it (37) | the lines without STEAP1: 0.81× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP2 |
| [[RITA1]] | B | STEAP1 activity lowers RITA1's level | lines that do not express STEAP1 (11) vs lines expressing it (39) | 1.21× higher at baseline in the lines without STEAP1 | 0.078 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP2 |
| [[STEAP2]] | C | STEAP1 activity raises STEAP2's level | lines that do not express STEAP1 (11) vs lines expressing it (39) | 4.69× lower at baseline in the lines without STEAP1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP2; co-absent with the target |
| [[STEAP2-AS1]] | C | STEAP1 activity raises STEAP2-AS1's level | lines that do not express STEAP1 (11) vs lines expressing it (39) | 2.49× lower at baseline in the lines without STEAP1 | 0.015 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP2; co-absent with the target |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.381). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.7, -46.5); signed map (-2.3, -40.0). **Vector** length 53.1, 9.30% of its response variance represented; |z| ≥ 3 in 693 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +8.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +4.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | +4.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -1.5 | -3.7 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.2 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -3.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.0 | -1.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | STEAP family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.13 — chr7:90,154,456-90,164,829 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRSS24; previously STEAP |
| Gene groups (HGNC) | Serine proteases; STEAP family; Flavoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHE8](https://www.uniprot.org/uniprotkb/Q9UHE8) (STEAP1 protein):

> Does not function as a metalloreductase due to the absence of binding sites for the electron-donating substrate NADPH. Promotes Fe(3+) reduction when fused to the NADPH-binding domain of STEAP4.

**Summary**, from NCBI Gene [26872](https://www.ncbi.nlm.nih.gov/gene/26872):

> This gene is predominantly expressed in prostate tissue, and is found to be upregulated in multiple cancer cell lines. The gene product is predicted to be a six-transmembrane protein, and was shown to be a cell surface antigen significantly expressed at cell-cell junctions. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11378](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11378) · Entrez [26872](https://www.ncbi.nlm.nih.gov/gene/26872) · UniProt [Q9UHE8](https://www.uniprot.org/uniprotkb/Q9UHE8) · Ensembl [ENSG00000164647](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164647)

## Data

Gene col 8979: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8979); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8979, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8979]; `tensor/DDL_lfc|DDL_z.npy` [8979]; `embed/gene_vectors.npy` [8979]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8979 or target_col == 8979). Every well: [[STEAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STEAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
