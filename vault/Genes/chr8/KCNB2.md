---
symbol: "KCNB2"
type: "gene"
col: 11314
ensembl_id: "ENSG00000182674"
name: "potassium voltage-gated channel subfamily B member 2"
location: "8q21.11"
module: 9
arm: "+"
pooled_cpm: 10.61
n_lines_expressing: 7
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 24
direction_downstream: 54
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# KCNB2

*potassium voltage-gated channel subfamily B member 2* — 8q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.46× (z +20.5, q 0e+00, up in 0 of 2 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.257×; ⚠ cell-cycle shift, explains ~92% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIT2]] (+0.87, fdr 7e-06), [[LRFN2]] (+0.87, fdr 7e-06), [[SYT4]] (+0.86, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 54 go from it, the strongest it → [[NELL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11314.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.46×** | +20.5 | 0e+00 | 0/2 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.47×** | +15.3 | 0e+00 | 2/2 (SW48, SHP-77) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.96×** | +10.0 | 5e-21 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.82×** | +9.3 | 2e-18 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.99×** | +7.3 | 3e-11 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.97×** | +7.0 | 3e-10 | 1/4 (H4) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +5.5 | 4e-06 | 1/3 (H4) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.11×** | +5.4 | 5e-06 | 1/4 (SW48) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +4.8 | 1e-04 | 0/2 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.89×** | +4.6 | 2e-04 | 0/2 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.5 | 4e-04 | 1/5 (SW48) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +4.4 | 6e-04 | 1/2 (SW48) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.71×** | +3.7 | 0.008 | 1/2 (SW48) | inconsistent across doses | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.51× | +3.0 | 0.11 | 0/4 | rises with dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11314.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.257×; ⚠ cell-cycle shift, explains ~92% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.598× | -3.4 | 0.23 | 0/4 | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.627× | -3.3 | 0.23 | 2/3 (SW48, SHP-77) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11314. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 488 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -8.7) ⚠ cell-cycle shift, explains ~92% of this change |
| [[A-172 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.86 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11314), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIT2]] | +0.87 | +0.84 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[LRFN2]] | +0.87 | +0.84 / +0.86 | both halves | 7e-06 | pathway: Neuronal System |
| [[SYT4]] | +0.86 | +0.84 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[SRRM4]] | +0.85 | +0.71 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[ASCL1]] | +0.85 | +0.83 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[RUNX1T1]] | +0.83 | +0.81 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[PCSK1]] | +0.80 | +0.78 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[LINC02197]] | +0.80 | +0.74 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[GRIK1]] | +0.79 | +0.80 / +0.70 | both halves | 7e-06 | pathway: Neuronal System |
| [[SNTG1]] | +0.74 | +0.72 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[RMST]] | +0.74 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[DACH1]] | +0.68 | +0.61 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 1, C 23. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KCNB2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CALCA]] | C | CALCA activity raises KCNB2's level | lines that do not express CALCA (45) vs lines expressing it (5) | 7.40× lower at baseline in the lines without CALCA | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises KCNB2's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 5.85× lower at baseline in the lines without RIT2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises KCNB2's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 4.78× lower at baseline in the lines without SRRM4 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises KCNB2's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 5.30× lower at baseline in the lines without SYT4 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[CARD18]] | C | CARD18 activity raises KCNB2's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 4.35× lower at baseline in the lines without CARD18 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises KCNB2's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 3.04× lower at baseline in the lines without ASCL1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[PGR]] | C | PGR activity raises KCNB2's level | lines that do not express PGR (36) vs lines expressing it (14) | 2.89× lower at baseline in the lines without PGR | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent; co-absent with the target |
| [[ST18]] | C | ST18 activity raises KCNB2's level | lines that do not express ST18 (39) vs lines expressing it (11) | 3.46× lower at baseline in the lines without ST18 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent; co-absent with the target |
| [[CGA]] | C | CGA activity raises KCNB2's level | lines that do not express CGA (44) vs lines expressing it (6) | 5.25× lower at baseline in the lines without CGA | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2; co-absent with the target |
| [[LINC01456]] | C | LINC01456 activity raises KCNB2's level | lines that do not express LINC01456 (42) vs lines expressing it (8) | 3.48× lower at baseline in the lines without LINC01456 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, S100A8; co-absent with the target |
| [[GTSF1]] | C | GTSF1 activity raises KCNB2's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 2.62× lower at baseline in the lines without GTSF1 | 0.034 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |

### Downstream of this gene

*54 arrows, 54 of them with an alert ⚠; grade A 0, B 10, C 44. Shown: the 12 strongest; 42 more arrows (42 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NELL1]] | B | KCNB2 activity raises NELL1's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 3.14× lower at baseline in the lines without KCNB2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent |
| [[LINC02306]] | B | KCNB2 activity raises LINC02306's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 3.28× lower at baseline in the lines without KCNB2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent |
| [[RALYL]] | B | KCNB2 activity raises RALYL's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 2.78× lower at baseline in the lines without KCNB2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent |
| [[MYT1L]] | B | KCNB2 activity raises MYT1L's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 3.00× lower at baseline in the lines without KCNB2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent |
| [[CHRM5]] | B | KCNB2 activity raises CHRM5's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 2.24× lower at baseline in the lines without KCNB2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent |
| [[VENTXP1]] | B | KCNB2 activity raises VENTXP1's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 2.85× lower at baseline in the lines without KCNB2 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent |
| [[KCNMB2]] | B | KCNB2 activity raises KCNMB2's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 3.85× lower at baseline in the lines without KCNB2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent |
| [[UNC80]] | B | KCNB2 activity raises UNC80's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 2.20× lower at baseline in the lines without KCNB2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent |
| [[GLRA3]] | B | KCNB2 activity raises GLRA3's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 2.16× lower at baseline in the lines without KCNB2 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent |
| [[LINC01250]] | B | KCNB2 activity raises LINC01250's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 2.43× lower at baseline in the lines without KCNB2 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent |
| [[GNAT3]] | C | KCNB2 activity raises GNAT3's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 2.61× lower at baseline in the lines without KCNB2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[CALCA]] | C | KCNB2 activity raises CALCA's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 6.22× lower at baseline in the lines without KCNB2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.6, 37.0); signed map (45.1, 34.2). **Vector** length 17.3, 8.80% of its response variance represented; |z| ≥ 3 in 65 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.9 | +15.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +20.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +4.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.7 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.7 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +2.9 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.6 | -2.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.6 | -2.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.5 | -2.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.5 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel subfamily B member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.11 — chr8:72,537,225-72,938,349 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Kv2.2 |
| Gene groups (HGNC) | Potassium voltage-gated channels; BTB domain containing |
| Reactome | 3 pathways, smallest: Voltage gated Potassium channels; Potassium Channels; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92953](https://www.uniprot.org/uniprotkb/Q92953) (Potassium voltage-gated channel subfamily B member 2):

> Voltage-gated potassium channel that mediates transmembrane potassium transport in excitable membranes, primarily in the brain and smooth muscle cells. Channels open or close in response to the voltage difference across the membrane, letting potassium ions pass in accordance with their electrochemical gradient. Homotetrameric channels mediate a delayed-rectifier voltage-dependent outward potassium current that display rapid activation and slow inactivation in response to membrane …

**Summary**, from NCBI Gene [9312](https://www.ncbi.nlm.nih.gov/gene/9312):

> Voltage-gated potassium (Kv) channels represent the most complex class of voltage-gated ion channels from both functional and structural standpoints. Their diverse functions include regulating neurotransmitter release, heart rate, insulin secretion, neuronal excitability, epithelial electrolyte transport, smooth muscle contraction, and cell volume. Four sequence-related potassium channel genes - shaker, shaw, shab, and shal - have been identified in Drosophila, and each has been shown to have …

**Accessions** — [HGNC:6232](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6232) · Entrez [9312](https://www.ncbi.nlm.nih.gov/gene/9312) · UniProt [Q92953](https://www.uniprot.org/uniprotkb/Q92953) · Ensembl [ENSG00000182674](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182674)

## Data

Gene col 11314: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11314); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11314, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11314]; `tensor/DDL_lfc|DDL_z.npy` [11314]; `embed/gene_vectors.npy` [11314]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11314 or target_col == 11314). Every well: [[KCNB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
