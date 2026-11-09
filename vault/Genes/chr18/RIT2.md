---
symbol: "RIT2"
type: "gene"
col: 7601
ensembl_id: "ENSG00000152214"
name: "Ras like without CAAX 2"
location: "18q12.3"
module: 9
arm: "+"
pooled_cpm: 8.86
n_lines_expressing: 6
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 28
direction_downstream: 64
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# RIT2

*Ras like without CAAX 2* — 18q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.87× (z +8.7, q 2e-15, up in 0 of 1 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 10 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.0274×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.105×); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.0467×; ⚠ cell-cycle shift, explains ~50% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (SHP-77 0.0996×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYT4]] (+0.99, fdr 7e-06), [[ASCL1]] (+0.98, fdr 7e-06), [[SRRM4]] (+0.97, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[CALCA]] → it (grade C ⚠); 64 go from it, the strongest it → [[MYT1L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7601.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.87×** | +8.7 | 2e-15 | 0/1 | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.21×** | +6.8 | 3e-09 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.86×** | +5.9 | 7e-07 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.41×** | +4.7 | 3e-04 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +4.7 | 3e-04 | 0/1 | top dose only | cell-cycle shift (explains ~15% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.99×** | +4.0 | 0.006 | 0/1 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +3.4 | 0.052 | 0/2 | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.052 | 0/1 | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.052 | 0/3 | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.97×** | +3.3 | 0.052 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.19×** | +3.3 | 0.057 | 0/1 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7601.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 10 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.0274×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.105×); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.0467×; ⚠ cell-cycle shift, explains ~50% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (SHP-77 0.0996×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.536× | -3.6 | 0.10 | 1/2 (SHP-77) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.543× | -3.6 | 0.10 | 1/3 (SHP-77) | two highest doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.529× | -3.4 | 0.11 | 0/3 | inconsistent across doses | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.558× | -3.3 | 0.14 | 2/2 (SHP-77, H4) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.577× | -3.1 | 0.22 | 1/3 (SHP-77) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.572× | -3.0 | 0.24 | 1/3 (AN3 CA) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7601. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 433 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0274× (z -28.0) |
| [[A-172 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.921 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.977 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.965 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.930 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.19 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7601), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYT4]] | +0.99 | +0.99 / +0.94 | both halves | 7e-06 | STRING 661 |
| [[ASCL1]] | +0.98 | +0.98 / +0.98 | both halves | 7e-06 | pathway: Signaling by NTRK1 (TRKA) |
| [[SRRM4]] | +0.97 | +0.91 / +0.96 | both halves | 7e-06 | **novel candidate** |
| [[LRFN2]] | +0.95 | +0.96 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[GRIK1]] | +0.89 | +0.90 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[KCNB2]] | +0.87 | +0.84 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[LINC02197]] | +0.86 | +0.83 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[CALCA]] | +0.84 | +0.91 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[CGA]] | +0.83 | +0.80 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[PCSK1]] | +0.82 | +0.82 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[SNTG1]] | +0.80 | +0.78 / +0.82 | both halves | 7e-06 |  |
| [[RUNX1T1]] | +0.80 | +0.78 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 0, C 28. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALCA]] | C | CALCA activity raises RIT2's level | lines that do not express CALCA (45) vs lines expressing it (5) | 7.67× lower at baseline in the lines without CALCA | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises RIT2's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 5.79× lower at baseline in the lines without SYT4 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises RIT2's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 4.68× lower at baseline in the lines without KCNB2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[SSX1]] | C | SSX1 activity raises RIT2's level | lines that do not express SSX1 (43) vs lines expressing it (7) | 3.78× lower at baseline in the lines without SSX1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00879, LINC02099, RNF17; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises RIT2's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 3.36× lower at baseline in the lines without ASCL1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[H19]] | C | H19 activity raises RIT2's level | lines that do not express H19 (38) vs lines expressing it (12) | 2.24× lower at baseline in the lines without H19 | 0.015 | ⚠ within organs, on part of the lines; also absent: CALCA, SYT4, CGA; co-absent with the target |
| [[CGA]] | C | CGA activity raises RIT2's level | lines that do not express CGA (44) vs lines expressing it (6) | 5.43× lower at baseline in the lines without CGA | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2; co-absent with the target |
| [[LINC01456]] | C | LINC01456 activity raises RIT2's level | lines that do not express LINC01456 (42) vs lines expressing it (8) | 3.53× lower at baseline in the lines without LINC01456 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, S100A8; co-absent with the target |
| [[NAA11]] | C | NAA11 activity raises RIT2's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 2.58× lower at baseline in the lines without NAA11 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[HGF]] | C | HGF activity raises RIT2's level | lines that do not express HGF (38) vs lines expressing it (12) | 2.57× lower at baseline in the lines without HGF | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises RIT2's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 3.41× lower at baseline in the lines without SRRM4 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[AK4P3]] | C | AK4P3 activity raises RIT2's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.18× lower at baseline in the lines without AK4P3 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |

### Downstream of this gene

*64 arrows, 64 of them with an alert ⚠; grade A 0, B 14, C 50. Shown: the 12 strongest; 52 more arrows (52 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYT1L]] | B | RIT2 activity raises MYT1L's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.57× lower at baseline in the lines without RIT2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[NELL1]] | B | RIT2 activity raises NELL1's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.83× lower at baseline in the lines without RIT2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[LINC02466]] | B | RIT2 activity raises LINC02466's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 2.34× lower at baseline in the lines without RIT2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[LINC02306]] | B | RIT2 activity raises LINC02306's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 4.02× lower at baseline in the lines without RIT2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[RALYL]] | B | RIT2 activity raises RALYL's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.37× lower at baseline in the lines without RIT2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[VENTXP1]] | B | RIT2 activity raises VENTXP1's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.38× lower at baseline in the lines without RIT2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[UNC80]] | B | RIT2 activity raises UNC80's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 2.58× lower at baseline in the lines without RIT2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[DGKB]] | B | RIT2 activity raises DGKB's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.43× lower at baseline in the lines without RIT2 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[MTMR7]] | B | RIT2 activity raises MTMR7's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 4.14× lower at baseline in the lines without RIT2 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[CHRM5]] | B | RIT2 activity raises CHRM5's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 2.38× lower at baseline in the lines without RIT2 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[KCNMB2]] | B | RIT2 activity raises KCNMB2's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 4.92× lower at baseline in the lines without RIT2 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[GLRA3]] | B | RIT2 activity raises GLRA3's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 2.43× lower at baseline in the lines without RIT2 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.665). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.7, 37.1); signed map (44.8, 34.2). **Vector** length 29.2, 26.2% of its response variance represented; |z| ≥ 3 in 90 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.56 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.2 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +3.4 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -3.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -3.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -1.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | Ras like without CAAX 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.3 — chr18:42,743,227-43,115,691 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RIBA; previously RIN |
| Gene groups (HGNC) | RAS type GTPase family |
| Reactome | 5 pathways, smallest: Signalling to p38 via RIT and RIN; Signalling to ERKs; Signaling by NTRK1 (TRKA) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99578](https://www.uniprot.org/uniprotkb/Q99578) (GTP-binding protein Rit2):

> Binds and exchanges GTP and GDP. Binds and modulates the activation of POU4F1 as gene expression regulator.

**Summary**, from NCBI Gene [6014](https://www.ncbi.nlm.nih.gov/gene/6014):

> RIN belongs to the RAS (HRAS; MIM 190020) superfamily of small GTPases (Shao et al., 1999 [PubMed 10545207]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:10017](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10017) · Entrez [6014](https://www.ncbi.nlm.nih.gov/gene/6014) · UniProt [Q99578](https://www.uniprot.org/uniprotkb/Q99578) · Ensembl [ENSG00000152214](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152214)

## Data

Gene col 7601: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7601); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7601, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7601]; `tensor/DDL_lfc|DDL_z.npy` [7601]; `embed/gene_vectors.npy` [7601]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7601 or target_col == 7601). Every well: [[RIT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
