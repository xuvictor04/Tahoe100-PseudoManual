---
symbol: "SRRM4"
type: "gene"
col: 6345
ensembl_id: "ENSG00000139767"
name: "serine/arginine repetitive matrix 4"
location: "12q24.23"
module: 9
arm: "+"
pooled_cpm: 2.46
n_lines_expressing: 9
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 24
direction_downstream: 59
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SRRM4

*serine/arginine repetitive matrix 4* — 12q24.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.06× (z +10.9, q 9e-25, up in 0 of 1 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.185×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIT2]] (+0.97, fdr 7e-06), [[SYT4]] (+0.97, fdr 7e-06), [[LRFN2]] (+0.95, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[CALCA]] → it (grade C ⚠); 59 go from it, the strongest it → [[NRXN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6345.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.06×** | +10.9 | 9e-25 | 0/1 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.41×** | +9.1 | 2e-17 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.08×** | +7.9 | 5e-13 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.21×** | +6.2 | 8e-08 | 0/1 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.27×** | +6.2 | 8e-08 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.75×** | +5.7 | 1e-06 | 0/1 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.47×** | +4.9 | 8e-05 | 0/1 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.84×** | +4.0 | 0.005 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.68×** | +4.0 | 0.005 | 0/1 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.61×** | +3.9 | 0.006 | 0/1 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.86×** | +3.5 | 0.026 | 0/1 | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.85×** | +3.4 | 0.027 | 1/1 (SHP-77) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +3.2 | 0.051 | 0/1 | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.1 | 0.070 | 0/1 | top dose only | cell-cycle shift (explains ~2% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.1 | 0.072 | 0/1 | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.185×; ⚠ toxic; transcription drop).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6345. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -12.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.452 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.406 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.922 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.516 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.594 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.574 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.637 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.486 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.585 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.573 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.460 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.613 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.527 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.641 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.661 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.586 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.996 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.629 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.474 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6345), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIT2]] | +0.97 | +0.91 / +0.96 | both halves | 7e-06 | **novel candidate** |
| [[SYT4]] | +0.97 | +0.92 / +0.91 | both halves | 7e-06 | STRING 443 |
| [[LRFN2]] | +0.95 | +0.91 / +0.92 | both halves | 7e-06 | **novel candidate** |
| [[ASCL1]] | +0.95 | +0.89 / +0.93 | both halves | 7e-06 | **novel candidate** |
| [[LINC02197]] | +0.86 | +0.76 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[GRIK1]] | +0.86 | +0.83 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[KCNB2]] | +0.85 | +0.71 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[CGA]] | +0.85 | +0.88 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CALCA]] | +0.82 | +0.87 / +0.36 | both halves | 1e-04 | **novel candidate** |
| [[RUNX1T1]] | +0.79 | +0.67 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[PCSK1]] | +0.78 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[SNTG1]] | +0.77 | +0.70 / +0.83 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 0, C 24. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALCA]] | C | CALCA activity raises SRRM4's level | lines that do not express CALCA (45) vs lines expressing it (5) | 4.51× lower at baseline in the lines without CALCA | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises SRRM4's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.57× lower at baseline in the lines without RIT2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises SRRM4's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 3.52× lower at baseline in the lines without SYT4 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[SSX1]] | C | SSX1 activity raises SRRM4's level | lines that do not express SSX1 (43) vs lines expressing it (7) | 2.77× lower at baseline in the lines without SSX1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00879, LINC02099, RNF17; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises SRRM4's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 3.02× lower at baseline in the lines without KCNB2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises SRRM4's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 2.40× lower at baseline in the lines without ASCL1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[H19]] | C | H19 activity raises SRRM4's level | lines that do not express H19 (38) vs lines expressing it (12) | 1.88× lower at baseline in the lines without H19 | 0.021 | ⚠ within organs, on part of the lines; also absent: CALCA, SYT4, CGA; co-absent with the target |
| [[MIR3667HG]] | C | MIR3667HG activity raises SRRM4's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 1.89× lower at baseline in the lines without MIR3667HG | 0.025 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[LINC01456]] | C | LINC01456 activity raises SRRM4's level | lines that do not express LINC01456 (42) vs lines expressing it (8) | 2.58× lower at baseline in the lines without LINC01456 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, S100A8; co-absent with the target |
| [[PHYHIPL]] | C | PHYHIPL activity raises SRRM4's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 2.00× lower at baseline in the lines without PHYHIPL | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |
| [[CGA]] | C | CGA activity raises SRRM4's level | lines that do not express CGA (44) vs lines expressing it (6) | 3.51× lower at baseline in the lines without CGA | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2; co-absent with the target |
| [[ZNF208]] | C | ZNF208 activity raises SRRM4's level | lines that do not express ZNF208 (41) vs lines expressing it (9) | 2.19× lower at baseline in the lines without ZNF208 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC01029, ENSG00000287598; co-absent with the target |

### Downstream of this gene

*59 arrows, 59 of them with an alert ⚠; grade A 0, B 11, C 48. Shown: the 12 strongest; 47 more arrows (47 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRXN1]] | B | SRRM4 activity raises NRXN1's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 4.29× lower at baseline in the lines without SRRM4 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[VENTXP1]] | B | SRRM4 activity raises VENTXP1's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 2.79× lower at baseline in the lines without SRRM4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[RALYL]] | B | SRRM4 activity raises RALYL's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 2.40× lower at baseline in the lines without SRRM4 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[SEMA6D]] | B | SRRM4 activity raises SEMA6D's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 2.34× lower at baseline in the lines without SRRM4 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[UNC80]] | B | SRRM4 activity raises UNC80's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 2.28× lower at baseline in the lines without SRRM4 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[CHRM5]] | B | SRRM4 activity raises CHRM5's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 1.94× lower at baseline in the lines without SRRM4 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[MYT1L]] | B | SRRM4 activity raises MYT1L's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 2.37× lower at baseline in the lines without SRRM4 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[XIRP2]] | B | SRRM4 activity raises XIRP2's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 2.51× lower at baseline in the lines without SRRM4 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[LINC02306]] | B | SRRM4 activity raises LINC02306's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 2.57× lower at baseline in the lines without SRRM4 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[GLRA3]] | B | SRRM4 activity raises GLRA3's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 1.95× lower at baseline in the lines without SRRM4 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[MAN1C1]] | B | SRRM4 activity raises MAN1C1's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 2.76× lower at baseline in the lines without SRRM4 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[KCNJ6]] | C | SRRM4 activity raises KCNJ6's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 6.33× lower at baseline in the lines without SRRM4 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.685). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.8, 37.0); signed map (44.7, 34.3). **Vector** length 12.6, 11.4% of its response variance represented; |z| ≥ 3 in 20 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.57 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.6 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.5 | +10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.1 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +4.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.6 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.6 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.6 | +3.2 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.5 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.5 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.5 | -0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.5 | -1.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.4 | -1.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | serine/arginine repetitive matrix 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.23 — chr12:118,981,541-119,163,051 (+) |
| Ensembl biotype | protein_coding |
| Also known as | nSR100; previously KIAA1853 |
| Matched by | ensembl_id |

**Function**, from UniProt [A7MD48](https://www.uniprot.org/uniprotkb/A7MD48) (Serine/arginine repetitive matrix protein 4):

> Splicing factor specifically required for neural cell differentiation. Acts in conjunction with nPTB/PTBP2 by binding directly to its regulated target transcripts and promotes neural-specific exon inclusion in many genes that function in neural cell differentiation. Required to promote the inclusion of neural-specific exon 10 in nPTB/PTBP2, leading to increased expression of neural-specific nPTB/PTBP2. Also promotes the inclusion of exon 16 in DAAM1 in neuron extracts (By similarity). Promotes …

**Summary**, from NCBI Gene [84530](https://www.ncbi.nlm.nih.gov/gene/84530):

> SRRM4 promotes alternative splicing and inclusion of neural-specific exons in target mRNAs (Calarco et al., 2009 [PubMed 19737518]).[supplied by OMIM, Oct 2009]

**Accessions** — [HGNC:29389](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29389) · Entrez [84530](https://www.ncbi.nlm.nih.gov/gene/84530) · UniProt [A7MD48](https://www.uniprot.org/uniprotkb/A7MD48) · Ensembl [ENSG00000139767](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139767)

## Data

Gene col 6345: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6345); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6345, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6345]; `tensor/DDL_lfc|DDL_z.npy` [6345]; `embed/gene_vectors.npy` [6345]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6345 or target_col == 6345). Every well: [[SRRM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRRM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
