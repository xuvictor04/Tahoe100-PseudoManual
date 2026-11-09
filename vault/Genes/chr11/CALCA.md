---
symbol: "CALCA"
type: "gene"
col: 3153
ensembl_id: "ENSG00000110680"
name: "calcitonin related polypeptide alpha"
location: "11p15.2"
module: 9
arm: "+"
pooled_cpm: 15.57
n_lines_expressing: 5
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 24
direction_downstream: 57
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CALCA

*calcitonin related polypeptide alpha* — 11p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 8.63× (z +10.0, q 1e-20, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 3.77× (z +3.9, q 0.010, up in 0 of 1 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.0945×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SHP-77 0.154×).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CGA]] (+0.88, fdr 7e-06), [[RIT2]] (+0.84, fdr 1e-05), [[ASCL1]] (+0.83, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[RIT2]] → it (grade C ⚠); 57 go from it, the strongest it → [[MYT1L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3153.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **8.63×** | +10.0 | 1e-20 | 1/1 (SHP-77) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.77×** | +7.5 | 2e-11 | 1/1 (SHP-77) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.94×** | +7.1 | 2e-10 | 1/1 (SHP-77) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.00×** | +4.9 | 1e-04 | 0/1 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **3.77×** | +3.9 | 0.010 | 0/1 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.30×** | +3.9 | 0.011 | 0/1 | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **2.29×** | +3.8 | 0.011 | 0/1 | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +3.6 | 0.023 | 0/2 | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3153.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.0945×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SHP-77 0.154×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.431× | -3.6 | 0.17 | 1/2 (SHP-77) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.448× | -3.4 | 0.17 | 1/2 (SHP-77) | inconsistent across doses | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.490× | -3.3 | 0.19 | 0/3 | inconsistent across doses |  |
| [[Decitabine (drug)]] 5 µM |  | 0.505× | -3.0 | 0.33 | 1/1 (SHP-77) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3153. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 805 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0945× (z -20.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -11.4) |
| [[NCI-H2122 (line)]] | alt | 28.3 | 1 (1 ⚠) | 0 | [[Raltitrexed (drug)]] 5 µM 1.58× (z +21.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.901 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H23 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.41 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3153), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGA]] | +0.88 | +0.83 / +0.72 | both halves | 7e-06 | pathway: G alpha (s) signalling events; STRING 477 |
| [[RIT2]] | +0.84 | +0.91 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[ASCL1]] | +0.83 | +0.89 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[GRIK1]] | +0.82 | +0.85 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[SRRM4]] | +0.82 | +0.87 / +0.36 | both halves | 1e-04 | **novel candidate** |
| [[LRFN2]] | +0.81 | +0.89 / +0.43 | both halves | 3e-05 | **novel candidate** |
| [[SYT4]] | +0.81 | +0.90 / +0.47 | both halves | 2e-05 | **novel candidate** |
| [[PCSK1]] | +0.77 | +0.77 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[LINC02197]] | +0.66 | +0.73 / +0.29 | both halves | 2e-04 |  |
| [[SNTG1]] | +0.64 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[NELL1]] | +0.64 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[KCNB2]] | +0.62 | +0.68 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 0, C 24. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIT2]] | C | RIT2 activity raises CALCA's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 7.98× lower at baseline in the lines without RIT2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises CALCA's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 8.04× lower at baseline in the lines without SYT4 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises CALCA's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 6.22× lower at baseline in the lines without KCNB2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises CALCA's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 4.35× lower at baseline in the lines without ASCL1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[H19]] | C | H19 activity raises CALCA's level | lines that do not express H19 (38) vs lines expressing it (12) | 2.76× lower at baseline in the lines without H19 | 0.007 | ⚠ within organs, on part of the lines; also absent: CALCA, SYT4, CGA; co-absent with the target |
| [[CGA]] | C | CGA activity raises CALCA's level | lines that do not express CGA (44) vs lines expressing it (6) | 7.77× lower at baseline in the lines without CGA | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises CALCA's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 4.36× lower at baseline in the lines without SRRM4 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[AK4P3]] | C | AK4P3 activity raises CALCA's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.57× lower at baseline in the lines without AK4P3 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |
| [[GTSF1]] | C | GTSF1 activity raises CALCA's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 3.51× lower at baseline in the lines without GTSF1 | 0.018 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[ST18]] | C | ST18 activity raises CALCA's level | lines that do not express ST18 (39) vs lines expressing it (11) | 3.28× lower at baseline in the lines without ST18 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent; co-absent with the target |
| [[LINC02492]] | C | LINC02492 activity raises CALCA's level | lines that do not express LINC02492 (32) vs lines expressing it (18) | 2.02× lower at baseline in the lines without LINC02492 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000260289, ENSG00000254337, RHOJ; maybe low, not absent; co-absent with the target |
| [[SNTG1]] | C | SNTG1 activity raises CALCA's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 3.16× lower at baseline in the lines without SNTG1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*57 arrows, 57 of them with an alert ⚠; grade A 0, B 20, C 37. Shown: the 12 strongest; 45 more arrows (45 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYT1L]] | B | CALCA activity raises MYT1L's level | lines that do not express CALCA (45) vs lines expressing it (5) | 4.58× lower at baseline in the lines without CALCA | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[NELL1]] | B | CALCA activity raises NELL1's level | lines that do not express CALCA (45) vs lines expressing it (5) | 5.04× lower at baseline in the lines without CALCA | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[LINC02306]] | B | CALCA activity raises LINC02306's level | lines that do not express CALCA (45) vs lines expressing it (5) | 5.33× lower at baseline in the lines without CALCA | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[VENTXP1]] | B | CALCA activity raises VENTXP1's level | lines that do not express CALCA (45) vs lines expressing it (5) | 4.20× lower at baseline in the lines without CALCA | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[RALYL]] | B | CALCA activity raises RALYL's level | lines that do not express CALCA (45) vs lines expressing it (5) | 4.20× lower at baseline in the lines without CALCA | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[KCNMB2]] | B | CALCA activity raises KCNMB2's level | lines that do not express CALCA (45) vs lines expressing it (5) | 7.17× lower at baseline in the lines without CALCA | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[CHRM5]] | B | CALCA activity raises CHRM5's level | lines that do not express CALCA (45) vs lines expressing it (5) | 2.93× lower at baseline in the lines without CALCA | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[UNC80]] | B | CALCA activity raises UNC80's level | lines that do not express CALCA (45) vs lines expressing it (5) | 3.21× lower at baseline in the lines without CALCA | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[GLRA3]] | B | CALCA activity raises GLRA3's level | lines that do not express CALCA (45) vs lines expressing it (5) | 2.91× lower at baseline in the lines without CALCA | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[MTMR7]] | B | CALCA activity raises MTMR7's level | lines that do not express CALCA (45) vs lines expressing it (5) | 4.95× lower at baseline in the lines without CALCA | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[CNBD1]] | B | CALCA activity raises CNBD1's level | lines that do not express CALCA (45) vs lines expressing it (5) | 2.50× lower at baseline in the lines without CALCA | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[PTPRT]] | B | CALCA activity raises PTPRT's level | lines that do not express CALCA (45) vs lines expressing it (5) | 1.85× lower at baseline in the lines without CALCA | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.526). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.8, 37.2); signed map (44.9, 34.5). **Vector** length 8.51, 4.48% of its response variance represented; |z| ≥ 3 in 23 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.8 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.7 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.7 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.7 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.6 | +2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.3 | +0.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.3 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.3 | -0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.3 | +3.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.3 | -3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.2 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.2 | -3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.2 | -0.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.2 | +0.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.2 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.2 | +0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | calcitonin related polypeptide alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.2 — chr11:14,966,622-14,972,354 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGRP, CGRP-alpha; previously CALC1 |
| Gene groups (HGNC) | Neuropeptides |
| Reactome | 7 pathways, smallest: Calcitonin-like ligand receptors; Class B/2 (Secretin family receptors); Amyloid fiber formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P01258](https://www.uniprot.org/uniprotkb/P01258) (Calcitonin):

> [Calcitonin]: Peptide hormone secreted by thyroid parafollicular (C) cells that acts as a high-affinity agonist of the calcitonin receptor/CALCR that primarily couples to Gs/adenylate cyclase signaling, resulting in activation of cAMP-dependent pathways, and can additionally mobilize intracellular calcium and activate ERK signaling. Acutely lowers blood calcium levels predominantly by inhibiting osteoclast-mediated bone resorption. In osteoclasts, receptor activation rapidly induces loss of the …

**Summary**, from NCBI Gene [796](https://www.ncbi.nlm.nih.gov/gene/796):

> This gene encodes the peptide hormones calcitonin, calcitonin gene-related peptide and katacalcin by tissue-specific alternative RNA splicing of the gene transcripts and cleavage of inactive precursor proteins. Calcitonin is involved in calcium regulation and acts to regulate phosphorus metabolism. Calcitonin gene-related peptide functions as a vasodilator and as an antimicrobial peptide while katacalcin is a calcium-lowering peptide. Multiple transcript variants encoding different isoforms …

**Accessions** — [HGNC:1437](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1437) · Entrez [796](https://www.ncbi.nlm.nih.gov/gene/796) · UniProt [P01258](https://www.uniprot.org/uniprotkb/P01258) · Ensembl [ENSG00000110680](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110680)

## Data

Gene col 3153: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3153); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3153, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3153]; `tensor/DDL_lfc|DDL_z.npy` [3153]; `embed/gene_vectors.npy` [3153]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3153 or target_col == 3153). Every well: [[CALCA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CALCA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
