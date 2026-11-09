---
symbol: "GTSF1"
type: "gene"
col: 9985
ensembl_id: "ENSG00000170627"
name: "gametocyte specific factor 1"
location: "12q13.13"
module: 9
arm: "+"
pooled_cpm: 3.2
n_lines_expressing: 10
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 17
direction_downstream: 28
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# GTSF1

*gametocyte specific factor 1* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.34× (z +10.0, q 7e-21, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +5.2, q 2e-05, up in 0 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (75 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 28 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CGA]] (+0.56, fdr 4e-05), [[FRG1FP]] (+0.55, fdr 3e-05), [[NAA11]] (+0.52, fdr 2e-04); moves opposite to [[CROCC]] (-0.38, fdr 8e-04, ⚠ not reproduced).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[NAA11]] → it (grade C ⚠); 28 go from it, the strongest it → [[FRG1FP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9985.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.34×** | +10.0 | 7e-21 | 2/5 (NCI-H1573, SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.03×** | +9.3 | 4e-18 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.14×** | +6.3 | 5e-08 | 1/4 (SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +5.2 | 2e-05 | 0/5 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.21×** | +4.7 | 3e-04 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.67×** | +4.3 | 0.001 | 1/5 (NCI-H1573) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.34×** | +4.3 | 0.001 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +3.8 | 0.011 | 1/5 (C-33 A) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.23×** | +3.7 | 0.015 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +3.5 | 0.028 | 0/5 | top dose only | cell-cycle shift (explains ~14% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.76×** | +3.4 | 0.039 | 1/6 (SHP-77) | two highest doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.55×** | +3.3 | 0.042 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.3 | 0.046 | 1/5 (SK-MEL-2) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9985.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | 0.573× | -3.1 | 0.51 | 1/5 (SK-MEL-2) | inconsistent across doses | position effect removed |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.603× | -3.0 | 0.51 | 1/5 (NCI-H1573) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9985. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.371 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.336 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.866 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.545 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.401 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.507 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.425 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.392 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.960 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.889 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.486 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.355 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9985), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 27 of them with an alert (⚠; 24 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGA]] | +0.56 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[FRG1FP]] | +0.55 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[NAA11]] | +0.52 | +0.29 / +0.46 | both halves | 2e-04 |  |
| [[LINC02197]] | +0.52 | +0.37 / +0.55 | both halves | 7e-05 |  |
| [[SRRM4]] | +0.52 | +0.30 / +0.51 | both halves | 2e-04 |  |
| [[KCNH7]] | +0.51 | +0.23 / +0.52 | both halves | 5e-04 |  |
| [[KHDRBS2]] | +0.50 | +0.18 / +0.52 | ⚠ one half (not replicated) | 1e-03 |  |
| [[LRFN2]] | +0.49 | +0.28 / +0.52 | both halves | 3e-04 |  |
| [[RUNX1T1]] | +0.48 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[CSRNP3]] | +0.48 | +0.33 / +0.47 | both halves | 1e-04 |  |
| [[RMST]] | +0.47 | +0.38 / +0.56 | both halves | 7e-05 |  |
| [[MAGEA10]] | +0.47 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[GRIA2]] | +0.47 | +0.41 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCC]] | -0.38 | -0.19 / -0.34 | ⚠ not reproduced | 8e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 0, C 17. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAA11]] | C | NAA11 activity raises GTSF1's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 2.85× lower at baseline in the lines without NAA11 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[MAGEA10]] | C | MAGEA10 activity raises GTSF1's level | lines that do not express MAGEA10 (42) vs lines expressing it (8) | 6.11× lower at baseline in the lines without MAGEA10 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, SOX10, LINC01425; co-absent with the target |
| [[CGA]] | C | CGA activity raises GTSF1's level | lines that do not express CGA (44) vs lines expressing it (6) | 4.53× lower at baseline in the lines without CGA | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2; co-absent with the target |
| [[MIR3667HG]] | C | MIR3667HG activity raises GTSF1's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 2.46× lower at baseline in the lines without MIR3667HG | 0.023 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[LINC01446]] | C | LINC01446 activity raises GTSF1's level | lines that do not express LINC01446 (34) vs lines expressing it (16) | 2.45× lower at baseline in the lines without LINC01446 | 0.032 | ⚠ within organs, on part of the lines; also absent: GABRG2, BAGE2, ENSG00000253363; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises GTSF1's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 2.64× lower at baseline in the lines without KCNH7 | 0.033 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[F11-AS1]] | C | F11-AS1 activity raises GTSF1's level | lines that do not express F11-AS1 (34) vs lines expressing it (16) | 1.92× lower at baseline in the lines without F11-AS1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent; co-absent with the target |
| [[MAGEB2]] | C | MAGEB2 activity raises GTSF1's level | lines that do not express MAGEB2 (42) vs lines expressing it (8) | 4.11× lower at baseline in the lines without MAGEB2 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, MAGEA10, TBXT; co-absent with the target |
| [[PEX5L]] | C | PEX5L activity raises GTSF1's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 2.23× lower at baseline in the lines without PEX5L | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent; co-absent with the target |
| [[FAM83F]] | C | FAM83F activity raises GTSF1's level | lines that do not express FAM83F (32) vs lines expressing it (18) | 1.59× lower at baseline in the lines without FAM83F | 0.059 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TRIM15, TMEM45B; co-absent with the target |
| [[LINC02327]] | C | LINC02327 activity raises GTSF1's level | lines that do not express LINC02327 (41) vs lines expressing it (9) | 2.27× lower at baseline in the lines without LINC02327 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000258028, LINC02566, ENSG00000289605; co-absent with the target |
| [[AK4P3]] | C | AK4P3 activity raises GTSF1's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.70× lower at baseline in the lines without AK4P3 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 1, C 27. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRG1FP]] | B | GTSF1 activity raises FRG1FP's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 1.99× lower at baseline in the lines without GTSF1 | 0.076 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566 |
| [[MIR3667HG]] | C | GTSF1 activity raises MIR3667HG's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 7.69× lower at baseline in the lines without GTSF1 | 0.005 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[FAM83F]] | C | GTSF1 activity raises FAM83F's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 1.33× lower at baseline in the lines without GTSF1 | 0.006 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[MAGEA10]] | C | GTSF1 activity raises MAGEA10's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 4.94× lower at baseline in the lines without GTSF1 | 0.006 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[NAA11]] | C | GTSF1 activity raises NAA11's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 3.79× lower at baseline in the lines without GTSF1 | 0.007 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[SLITRK6]] | C | GTSF1 activity raises SLITRK6's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 3.26× lower at baseline in the lines without GTSF1 | 0.009 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[KCNH7]] | C | GTSF1 activity raises KCNH7's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 3.66× lower at baseline in the lines without GTSF1 | 0.015 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[AK4P3]] | C | GTSF1 activity raises AK4P3's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 6.39× lower at baseline in the lines without GTSF1 | 0.015 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[MAGEB2]] | C | GTSF1 activity raises MAGEB2's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 3.22× lower at baseline in the lines without GTSF1 | 0.015 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[CALCA]] | C | GTSF1 activity raises CALCA's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 3.51× lower at baseline in the lines without GTSF1 | 0.018 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[CGA]] | C | GTSF1 activity raises CGA's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 2.84× lower at baseline in the lines without GTSF1 | 0.020 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[PEX5L]] | C | GTSF1 activity raises PEX5L's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 3.25× lower at baseline in the lines without GTSF1 | 0.022 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.471). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.1, 36.6); signed map (44.0, 35.6). **Vector** length 11.4, 3.04% of its response variance represented; |z| ≥ 3 in 61 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.4 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.3 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.0 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | -0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.9 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.6 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.5 | +2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.4 | +0.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.4 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.5 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.4 | -2.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.4 | -2.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.4 | -2.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.4 | -2.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | gametocyte specific factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:54,455,950-54,473,602 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32942, Cue110; previously FAM112B |
| Gene groups (HGNC) | Zinc fingers U11-48K-like CHHC-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WW33](https://www.uniprot.org/uniprotkb/Q8WW33) (Gametocyte-specific factor 1):

> Required for spermatogenesis and is involved in the suppression of retrotransposon transcription in male germ cells.

**Summary**, from NCBI Gene [121355](https://www.ncbi.nlm.nih.gov/gene/121355):

> Enables tRNA binding activity. Predicted to be involved in cell differentiation; regulatory ncRNA-mediated gene silencing; and spermatogenesis. Predicted to be located in cytoplasm. Predicted to be active in piP-body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26565](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26565) · Entrez [121355](https://www.ncbi.nlm.nih.gov/gene/121355) · UniProt [Q8WW33](https://www.uniprot.org/uniprotkb/Q8WW33) · Ensembl [ENSG00000170627](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170627)

## Data

Gene col 9985: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9985); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9985, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9985]; `tensor/DDL_lfc|DDL_z.npy` [9985]; `embed/gene_vectors.npy` [9985]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9985 or target_col == 9985). Every well: [[GTSF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTSF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
