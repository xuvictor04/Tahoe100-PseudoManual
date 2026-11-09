---
symbol: "SYT4"
type: "gene"
col: 5386
ensembl_id: "ENSG00000132872"
name: "synaptotagmin 4"
location: "18q12.3"
module: 9
arm: "+"
pooled_cpm: 5.23
n_lines_expressing: 6
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 33
direction_downstream: 56
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SYT4

*synaptotagmin 4* — 18q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.78× (z +7.2, q 4e-10, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.93× (z +4.3, q 0.002, up in 1 of 2 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.0707×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.151×); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.112×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SHP-77 0.154×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIT2]] (+0.99, fdr 7e-06), [[ASCL1]] (+0.97, fdr 7e-06), [[SRRM4]] (+0.97, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 33 arrows point to it, the strongest [[CALCA]] → it (grade C ⚠); 56 go from it, the strongest it → [[RALYL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5386.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.78×** | +7.2 | 4e-10 | 1/2 (CHP-212) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.39×** | +6.5 | 2e-08 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.23×** | +4.7 | 4e-04 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +4.3 | 0.002 | 1/2 (CHP-212) | top dose only | cell-cycle shift (explains ~23% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.92×** | +4.2 | 0.003 | 1/2 (SHP-77) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.87×** | +4.1 | 0.004 | 0/2 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.58×** | +4.0 | 0.004 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.32×** | +3.9 | 0.008 | 0/2 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **3.00×** | +3.6 | 0.020 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.23×** | +3.5 | 0.028 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +3.5 | 0.028 | 2/2 (CHP-212, SHP-77) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.78×** | +3.4 | 0.037 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5386.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.0707×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.151×); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.112×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SHP-77 0.154×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.508× | -3.1 | 0.56 | 1/2 (SHP-77) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.517× | -3.0 | 0.56 | 1/2 (SHP-77) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.49 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5386. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 261 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0707× (z -18.9) |
| [[A-172 (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.742 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.671 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.560 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.567 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.737 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.763 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.488 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.809 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.517 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.599 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.617 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.759 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.661 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.768 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.822 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.547 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5386), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIT2]] | +0.99 | +0.99 / +0.94 | both halves | 7e-06 | STRING 661 |
| [[ASCL1]] | +0.97 | +0.98 / +0.93 | both halves | 7e-06 | **novel candidate** |
| [[SRRM4]] | +0.97 | +0.92 / +0.91 | both halves | 7e-06 | STRING 443 |
| [[LRFN2]] | +0.94 | +0.96 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[LINC02197]] | +0.88 | +0.85 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[KCNB2]] | +0.86 | +0.84 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[GRIK1]] | +0.86 | +0.89 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[RUNX1T1]] | +0.84 | +0.80 / +0.86 | both halves | 7e-06 | STRING 412 |
| [[CGA]] | +0.81 | +0.80 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[CALCA]] | +0.81 | +0.90 / +0.47 | both halves | 2e-05 | **novel candidate** |
| [[PCSK1]] | +0.80 | +0.81 / +0.62 | both halves | 7e-06 |  |
| [[SNTG1]] | +0.78 | +0.78 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 0, C 33. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALCA]] | C | CALCA activity raises SYT4's level | lines that do not express CALCA (45) vs lines expressing it (5) | 7.22× lower at baseline in the lines without CALCA | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises SYT4's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 5.19× lower at baseline in the lines without RIT2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises SYT4's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 4.60× lower at baseline in the lines without ASCL1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[SSX1]] | C | SSX1 activity raises SYT4's level | lines that do not express SSX1 (43) vs lines expressing it (7) | 3.55× lower at baseline in the lines without SSX1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00879, LINC02099, RNF17; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises SYT4's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 4.16× lower at baseline in the lines without KCNB2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[CARD18]] | C | CARD18 activity raises SYT4's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 4.41× lower at baseline in the lines without CARD18 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10; co-absent with the target |
| [[H19]] | C | H19 activity raises SYT4's level | lines that do not express H19 (38) vs lines expressing it (12) | 2.11× lower at baseline in the lines without H19 | 0.012 | ⚠ within organs, on part of the lines; also absent: CALCA, SYT4, CGA; co-absent with the target |
| [[CGA]] | C | CGA activity raises SYT4's level | lines that do not express CGA (44) vs lines expressing it (6) | 5.10× lower at baseline in the lines without CGA | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2; co-absent with the target |
| [[LINC01456]] | C | LINC01456 activity raises SYT4's level | lines that do not express LINC01456 (42) vs lines expressing it (8) | 3.29× lower at baseline in the lines without LINC01456 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, S100A8; co-absent with the target |
| [[AK4P3]] | C | AK4P3 activity raises SYT4's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.65× lower at baseline in the lines without AK4P3 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |
| [[HGF]] | C | HGF activity raises SYT4's level | lines that do not express HGF (38) vs lines expressing it (12) | 3.11× lower at baseline in the lines without HGF | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises SYT4's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 3.07× lower at baseline in the lines without SRRM4 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*56 arrows, 56 of them with an alert ⚠; grade A 0, B 13, C 43. Shown: the 12 strongest; 44 more arrows (44 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RALYL]] | B | SYT4 activity raises RALYL's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 7.31× lower at baseline in the lines without SYT4 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[NELL1]] | B | SYT4 activity raises NELL1's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 3.82× lower at baseline in the lines without SYT4 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[MYT1L]] | B | SYT4 activity raises MYT1L's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 3.57× lower at baseline in the lines without SYT4 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[VENTXP1]] | B | SYT4 activity raises VENTXP1's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 3.32× lower at baseline in the lines without SYT4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[KCNMB2]] | B | SYT4 activity raises KCNMB2's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 5.11× lower at baseline in the lines without SYT4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[LINC02306]] | B | SYT4 activity raises LINC02306's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 4.03× lower at baseline in the lines without SYT4 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[UNC80]] | B | SYT4 activity raises UNC80's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 2.89× lower at baseline in the lines without SYT4 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[CHRM5]] | B | SYT4 activity raises CHRM5's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 2.44× lower at baseline in the lines without SYT4 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[GLRA3]] | B | SYT4 activity raises GLRA3's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 2.40× lower at baseline in the lines without SYT4 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[MAN1C1]] | B | SYT4 activity raises MAN1C1's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 2.94× lower at baseline in the lines without SYT4 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[MTMR7]] | B | SYT4 activity raises MTMR7's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 3.91× lower at baseline in the lines without SYT4 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[MAPK10]] | B | SYT4 activity raises MAPK10's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 4.44× lower at baseline in the lines without SYT4 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.8, 37.0); signed map (44.8, 34.2). **Vector** length 21.3, 18.0% of its response variance represented; |z| ≥ 3 in 60 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.57 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.7 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.8 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.7 | +1.1 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.6 | -1.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.6 | +0.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.6 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.6 | -2.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | synaptotagmin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.3 — chr18:43,267,892-43,277,535 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1342, HsT1192 |
| Gene groups (HGNC) | Synaptotagmins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2B2](https://www.uniprot.org/uniprotkb/Q9H2B2) (Synaptotagmin-4):

> Synaptotagmin family member which does not bind Ca(2+) (By similarity). Involved in neuronal dense core vesicles (DCVs) mobility through its interaction with KIF1A. Upon increased neuronal activity, phosphorylation by MAPK8/JNK1 destabilizes the interaction with KIF1A and captures DCVs to synapses (By similarity). Plays a role in dendrite formation by melanocytes.

**Summary**, from NCBI Gene [6860](https://www.ncbi.nlm.nih.gov/gene/6860):

> Predicted to enable several functions, including calcium ion sensor activity; calcium-dependent phospholipid binding activity; and protein dimerization activity. Involved in negative regulation of catecholamine secretion and positive regulation of dendrite extension. Predicted to be located in neuron projection terminus and secretory vesicle. Predicted to be active in several cellular components, including axon; exocytic vesicle; and synapse. Biomarker of type 2 diabetes mellitus. [provided by …

**Accessions** — [HGNC:11512](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11512) · Entrez [6860](https://www.ncbi.nlm.nih.gov/gene/6860) · UniProt [Q9H2B2](https://www.uniprot.org/uniprotkb/Q9H2B2) · Ensembl [ENSG00000132872](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132872)

## Data

Gene col 5386: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5386); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5386, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5386]; `tensor/DDL_lfc|DDL_z.npy` [5386]; `embed/gene_vectors.npy` [5386]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5386 or target_col == 5386). Every well: [[SYT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
