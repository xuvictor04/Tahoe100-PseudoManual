---
symbol: "KRT14"
type: "gene"
col: 11861
ensembl_id: "ENSG00000186847"
name: "keratin 14"
location: "17q21.2"
module: 31
arm: "+"
pooled_cpm: 6.77
n_lines_expressing: 7
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 15
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# KRT14

*keratin 14* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.60× (z +7.8, q 3e-12, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 3.42× (z +4.9, q 1e-04, up in 4 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KRT16]] (+0.76, fdr 7e-06, ⚠ same locus), [[HHIPL2]] (+0.54, fdr 2e-05), [[MAP1A]] (+0.53, fdr 2e-05), [[KRT6A]] (+0.51, fdr 5e-05); moves opposite to [[GYPC]] (-0.44, fdr 1e-04), [[TMEM87B]] (-0.41, fdr 2e-04), [[SHC3]] (-0.40, fdr 4e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[DSG4]] → it (grade C ⚠); 15 go from it, the strongest it → [[NCF2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11861.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.60×** | +7.8 | 3e-12 | 2/2 (Hs 766T, HS-578T) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.32×** | +7.4 | 4e-11 | 2/2 (Hs 766T, HS-578T) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **7.11×** | +7.3 | 7e-11 | 2/2 (Hs 766T, HS-578T) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.42×** | +4.9 | 1e-04 | 4/5 (Hs 766T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.17×** | +4.4 | 0.001 | 1/2 (Hs 766T) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.84×** | +4.1 | 0.004 | 1/3 (A-172) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **6.12×** | +3.8 | 0.011 | 2/3 (Hs 766T, A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.95×** | +3.8 | 0.011 | 1/5 (SW48) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.52×** | +3.7 | 0.013 | 1/3 (Hs 766T) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.34×** | +3.4 | 0.035 | 4/5 (Hs 766T, HS-578T, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.82×** | +3.4 | 0.035 | 0/5 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +3.2 | 0.075 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +3.1 | 0.094 | 3/5 (Hs 766T, HS-578T, …) | top dose only | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11861. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.323 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.341 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.390 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.761 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.418 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 254 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.729 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.489 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.727 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.460 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11861), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRT16]] | +0.76 | +0.77 / +0.59 | both halves | 7e-06 | same gene group; pathway: Formation of the cornified envelope; STRING 868; ⚠ same locus (22.9 kb, same strand: neighbours can correlate without regulation) |
| [[HHIPL2]] | +0.54 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[MAP1A]] | +0.53 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[KRT6A]] | +0.51 | +0.51 / +0.40 | both halves | 5e-05 | pathway: Formation of the cornified envelope; STRING 732 |
| [[SEMA3B]] | +0.51 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[KRT17]] | +0.49 | +0.40 / +0.41 | both halves | 5e-05 | same gene group; pathway: Formation of the cornified envelope; STRING 814; ⚠ same locus (32.5 kb, same strand: neighbours can correlate without regulation) |
| [[PPP2R2B]] | +0.48 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[GUCY1B1]] | +0.48 | +0.40 / +0.39 | both halves | 5e-05 |  |
| [[MISP]] | +0.47 | +0.45 / +0.35 | both halves | 1e-04 |  |
| [[PIK3AP1]] | +0.46 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[ZNF736P9Y]] | +0.46 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[CLTB]] | +0.45 | +0.44 / +0.28 | both halves | 3e-04 |  |
| [[MMP28]] | +0.44 | +0.51 / +0.36 | both halves | 9e-05 |  |
| [[NCF2]] | +0.44 | +0.59 / +0.32 | both halves | 1e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GYPC]] | -0.44 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[TMEM87B]] | -0.41 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[SHC3]] | -0.40 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[HMGA2]] | -0.39 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[MME]] | -0.38 | -0.32 / -0.29 | both halves | 3e-04 | STRING 466 |
| [[IKBIP]] | -0.38 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[BBIP1]] | -0.38 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[FOXC2]] | -0.37 | -0.30 / -0.31 | both halves | 2e-04 |  |
| [[DPY19L3]] | -0.36 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[ZBTB25]] | -0.36 | -0.39 / -0.25 | both halves | 4e-04 |  |
| [[SLC19A2]] | -0.36 | -0.31 / -0.32 | both halves | 2e-04 |  |
| [[POLR1HASP]] | -0.36 | -0.30 / -0.37 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSG4]] | C | DSG4 activity raises KRT14's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 1.91× lower at baseline in the lines without DSG4 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031; co-absent with the target |
| [[CALB1]] | C | CALB1 activity raises KRT14's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 2.42× lower at baseline in the lines without CALB1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[KRT6A]] | C | KRT6A activity raises KRT14's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 2.71× lower at baseline in the lines without KRT6A | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[SULF1]] | C | SULF1 activity raises KRT14's level | lines that do not express SULF1 (35) vs lines expressing it (15) | 2.01× lower at baseline in the lines without SULF1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00958, LINC01592, TBXT; co-absent with the target |
| [[LINC01133]] | C | LINC01133 activity raises KRT14's level | lines that do not express LINC01133 (34) vs lines expressing it (16) | 2.32× lower at baseline in the lines without LINC01133 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPH, IL33, UGT1A1; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises KRT14's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 2.03× lower at baseline in the lines without C5orf46 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[TIMP3]] | C | TIMP3 activity raises KRT14's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 1.97× lower at baseline in the lines without TIMP3 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 2, C 13. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCF2]] | B | KRT14 activity raises NCF2's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 3.18× lower at baseline in the lines without KRT14 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13 |
| [[WARS1]] | B | KRT14 activity raises WARS1's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 1.94× lower at baseline in the lines without KRT14 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13 |
| [[KRT6A]] | C | KRT14 activity raises KRT6A's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 4.95× lower at baseline in the lines without KRT14 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13; co-absent with the target |
| [[LINC01133]] | C | KRT14 activity raises LINC01133's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 5.36× lower at baseline in the lines without KRT14 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13; co-absent with the target |
| [[KRT16]] | C | KRT14 activity raises KRT16's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 3.71× lower at baseline in the lines without KRT14 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13; co-absent with the target |
| [[SULF1]] | C | KRT14 activity raises SULF1's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 4.71× lower at baseline in the lines without KRT14 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13; co-absent with the target |
| [[CALB1]] | C | KRT14 activity raises CALB1's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 4.92× lower at baseline in the lines without KRT14 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13; co-absent with the target |
| [[MMP28]] | C | KRT14 activity raises MMP28's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 2.53× lower at baseline in the lines without KRT14 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13; co-absent with the target |
| [[ITPK1]] | C | KRT14 activity weakens ITPK1's drug response | lines that do not express KRT14 (41) vs lines expressing it (4) | the lines without KRT14 respond 18.97× as strongly (z diff -2.05); strongest at Panobinostat 5 µM: 1.36x vs 0.47x (z diff -8.7) | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13; target measured in part of the lines; artifact flags |
| [[DSG4]] | C | KRT14 activity raises DSG4's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 2.62× lower at baseline in the lines without KRT14 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13; co-absent with the target |
| [[TDO2]] | C | KRT14 activity raises TDO2's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 2.78× lower at baseline in the lines without KRT14 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13; co-absent with the target |
| [[SERPINB5]] | C | KRT14 activity raises SERPINB5's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 4.86× lower at baseline in the lines without KRT14 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13; co-absent with the target |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.362). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.5, 53.3); signed map (52.9, -14.2). **Vector** length 16.2, 5.39% of its response variance represented; |z| ≥ 3 in 127 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.3 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.2 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.0 | +7.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +0.7 | +4.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +0.7 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.7 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.6 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.6 | +1.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.5 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.5 | +3.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.7 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.5 | +0.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.5 | -2.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.4 | -1.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.3 | -1.8 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.3 | -0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.3 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | keratin 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:41,582,279-41,586,895 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously EBS3, EBS4 |
| Gene groups (HGNC) | Keratins, type I |
| Reactome | 5 pathways, smallest: Type I hemidesmosome assembly; Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [P02533](https://www.uniprot.org/uniprotkb/P02533) (Keratin, type I cytoskeletal 14):

> Structural component of intermediate filaments in basal keratinocytes of stratified epithelia. Forms heteropolymers with type II keratin KRT5, contributing to the keratin intermediate filament network that confers mechanical strength and structural integrity to the basal layer of the epidermis and other stratified epithelial. The nonhelical tail domain is involved in promoting KRT5-KRT14 filaments to self-organize into large bundles and enhances the mechanical properties involved in resilience …

**Summary**, from NCBI Gene [3861](https://www.ncbi.nlm.nih.gov/gene/3861):

> This gene encodes a member of the keratin family, the most diverse group of intermediate filaments. This gene product, a type I keratin, is usually found as a heterotetramer with two keratin 5 molecules, a type II keratin. Together they form the cytoskeleton of epithelial cells. Mutations in the genes for these keratins are associated with epidermolysis bullosa simplex. At least one pseudogene has been identified at 17p12-p11. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6416](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6416) · Entrez [3861](https://www.ncbi.nlm.nih.gov/gene/3861) · UniProt [P02533](https://www.uniprot.org/uniprotkb/P02533) · Ensembl [ENSG00000186847](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186847)

## Data

Gene col 11861: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11861); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11861, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11861]; `tensor/DDL_lfc|DDL_z.npy` [11861]; `embed/gene_vectors.npy` [11861]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11861 or target_col == 11861). Every well: [[KRT14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRT14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
