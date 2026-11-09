---
symbol: "MARCOL"
type: "gene"
col: 14518
ensembl_id: "ENSG00000248109"
name: "MARCO like"
location: "5q32"
module: 19
arm: "+"
pooled_cpm: 7.93
n_lines_expressing: 5
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 33
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# MARCOL

*MARCO like* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.29× (z +8.7, q 1e-15, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.52× (z +6.8, q 1e-09, up in 2 of 3 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (A-172 24.3×).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (LoVo 0.0256×, NCI-H460 0.0483×; ⚠ cell-cycle shift, explains ~41% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (LoVo 0.0374×; ⚠ cell-cycle shift, explains ~33% of this change); [[Belinostat (drug)]] 5 µM in 1 line (LoVo 0.0434×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPINK13]] (+0.93, fdr 7e-06, ⚠ same locus), [[ABCC9]] (+0.65, fdr 1e-05), [[GLP2R]] (+0.61, fdr 1e-05), [[GASK1B]] (+0.59, fdr 1e-05); moves opposite to [[ETV5]] (-0.52, fdr 4e-05), [[CKLF]] (-0.51, fdr 7e-05), [[LTBP3]] (-0.46, fdr 4e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[SCARA5]] → it (grade C ⚠); 33 go from it, the strongest it → [[SLC9A2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14518.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (A-172 24.3×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.29×** | +8.7 | 1e-15 | 1/3 (NCI-H460) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.97×** | +8.1 | 2e-13 | 1/1 (LoVo) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.41×** | +7.2 | 1e-10 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.52×** | +6.8 | 1e-09 | 2/3 (A-172, LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.32×** | +4.4 | 0.001 | 1/3 (A-172) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +3.9 | 0.011 | 1/3 (A-172) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +3.6 | 0.022 | 0/3 | top dose only | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +3.6 | 0.026 | 2/3 (A-172, LoVo) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +3.5 | 0.031 | 1/3 (A-172) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.88×** | +3.2 | 0.084 | 0/3 | rises with dose | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.79× | +3.0 | 0.12 | 0/3 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14518.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (LoVo 0.0256×, NCI-H460 0.0483×; ⚠ cell-cycle shift, explains ~41% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (LoVo 0.0374×; ⚠ cell-cycle shift, explains ~33% of this change); [[Belinostat (drug)]] 5 µM in 1 line (LoVo 0.0434×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.534× | -3.3 | 0.49 | 0/3 | two highest doses | position effect removed |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.534× | -3.1 | 0.59 | 0/3 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14518. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 201 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0256× (z -15.1) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0434× (z -12.9) |
| [[A-172 (line)]] | wt | 6.88 | 1 | 0 | [[Selinexor (drug)]] 5 µM 24.3× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 6.45 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0483× (z -10.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-427 (line)]] | wt | 0.623 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.743 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.737 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.808 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.792 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.962 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.773 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.740 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.778 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.848 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.727 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.766 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.928 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.685 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.759 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.644 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.823 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.773 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.675 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.739 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.920 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.693 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14518), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPINK13]] | +0.93 | +0.95 / +0.92 | both halves | 7e-06 | ⚠ same locus (24.6 kb, same strand: neighbours can correlate without regulation) |
| [[ABCC9]] | +0.65 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[GLP2R]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[GASK1B]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[TLL1]] | +0.58 | +0.62 / +0.38 | both halves | 7e-05 |  |
| [[PSG4]] | +0.56 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[LINC01508]] | +0.56 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[LINC00457]] | +0.56 | +0.68 / +0.38 | both halves | 6e-05 |  |
| [[GASK1B-AS1]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[COL16A1]] | +0.55 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[MYO16-AS1]] | +0.55 | +0.50 / +0.36 | both halves | 1e-04 |  |
| [[SLC6A7]] | +0.55 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[NKAIN2]] | +0.55 | +0.43 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETV5]] | -0.52 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[CKLF]] | -0.51 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[LTBP3]] | -0.46 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[RGS17]] | -0.45 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[EIF4EBP1]] | -0.45 | -0.32 / -0.41 | both halves | 1e-04 |  |
| [[NUP43]] | -0.45 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[TOX2]] | -0.45 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[HPCAL1]] | -0.44 | -0.26 / -0.48 | both halves | 3e-04 |  |
| [[ABLIM3]] | -0.44 | -0.33 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCARA5]] | C | SCARA5 activity raises MARCOL's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 3.88× lower at baseline in the lines without SCARA5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[PRICKLE1]] | C | PRICKLE1 activity raises MARCOL's level | lines that do not express PRICKLE1 (26) vs lines expressing it (24) | 1.45× lower at baseline in the lines without PRICKLE1 | 0.013 | ⚠ within organs, on part of the lines; also absent: COL4A2, NR0B1, THBD; co-absent with the target |
| [[LINC01508]] | C | LINC01508 activity raises MARCOL's level | lines that do not express LINC01508 (42) vs lines expressing it (8) | 2.88× lower at baseline in the lines without LINC01508 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SPINK13, RHEX; co-absent with the target |
| [[NLGN4Y]] | C | NLGN4Y activity raises MARCOL's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 1.42× lower at baseline in the lines without NLGN4Y | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[GSG1L2]] | C | GSG1L2 activity raises MARCOL's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 2.38× lower at baseline in the lines without GSG1L2 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises MARCOL's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 2.05× lower at baseline in the lines without LINC03000 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[TBXT]] | C | TBXT activity raises MARCOL's level | lines that do not express TBXT (47) vs lines expressing it (3) | 3.71× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[P3H2]] | C | P3H2 activity raises MARCOL's level | lines that do not express P3H2 (28) vs lines expressing it (22) | 1.55× lower at baseline in the lines without P3H2 | 0.061 | ⚠ within organs, on part of the lines; also absent: P3H2-AS1, SRGN, SPOCK1; co-absent with the target |
| [[PDE1A]] | C | PDE1A activity raises MARCOL's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 1.53× lower at baseline in the lines without PDE1A | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |
| [[PSG9]] | C | PSG9 activity raises MARCOL's level | lines that do not express PSG9 (45) vs lines expressing it (5) | 2.03× lower at baseline in the lines without PSG9 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, PSG1, NPPB; co-absent with the target; its own permutation p |
| [[ALPK2]] | C | ALPK2 activity raises MARCOL's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 1.22× lower at baseline in the lines without ALPK2 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 5, C 28. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC9A2]] | B | MARCOL, [[SPINK13]] activity raises SLC9A2's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 3.00× lower at baseline in the lines without MARCOL, SPINK13 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent genes |
| [[PTPRB]] | B | MARCOL, [[SPINK13]] activity raises PTPRB's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 3.76× lower at baseline in the lines without MARCOL, SPINK13 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent genes |
| [[KRTAP5-AS1]] | B | MARCOL activity raises KRTAP5-AS1's level | lines that do not express MARCOL (45) vs lines expressing it (5) | 2.73× lower at baseline in the lines without MARCOL | 0.058 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975 |
| [[LINC00534]] | B | MARCOL, [[SPINK13]] activity raises LINC00534's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 2.33× lower at baseline in the lines without MARCOL, SPINK13 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent genes |
| [[SOX6]] | B | MARCOL, [[SPINK13]] activity raises SOX6's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 1.69× lower at baseline in the lines without MARCOL, SPINK13 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent genes |
| [[SCARA5]] | C | MARCOL, [[SPINK13]] activity raises SCARA5's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 4.95× lower at baseline in the lines without MARCOL, SPINK13 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[LINC00457]] | C | MARCOL, [[SPINK13]] activity raises LINC00457's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 2.89× lower at baseline in the lines without MARCOL, SPINK13 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[TBXT]] | C | MARCOL, [[SPINK13]] activity raises TBXT's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 5.87× lower at baseline in the lines without MARCOL, SPINK13 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[PRICKLE1]] | C | MARCOL, [[SPINK13]] activity raises PRICKLE1's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 2.63× lower at baseline in the lines without MARCOL, SPINK13 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[P3H2-AS1]] | C | MARCOL, [[SPINK13]] activity raises P3H2-AS1's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 3.44× lower at baseline in the lines without MARCOL, SPINK13 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[LINC03000]] | C | MARCOL, [[SPINK13]] activity raises LINC03000's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 6.55× lower at baseline in the lines without MARCOL, SPINK13 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[CHL1]] | C | MARCOL, [[SPINK13]] activity raises CHL1's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 4.98× lower at baseline in the lines without MARCOL, SPINK13 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.524). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.2, 26.0); signed map (41.4, 27.2). **Vector** length 18.9, 8.71% of its response variance represented; |z| ≥ 3 in 108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.5 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.4 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.3 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.2 | +6.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.9 | +2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.8 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.8 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.8 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.7 | +0.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -0.6 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.6 | -2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -0.6 | -1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -0.5 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.5 | -1.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.5 | -0.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.4 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | MARCO like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:148,221,650-148,243,580 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [A0A1B0GUY1](https://www.uniprot.org/uniprotkb/A0A1B0GUY1) carries no function annotation.

**Summary**, from NCBI Gene [105378220](https://www.ncbi.nlm.nih.gov/gene/105378220):

> Predicted to be located in endoplasmic reticulum lumen. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:53644](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53644) · Entrez [105378220](https://www.ncbi.nlm.nih.gov/gene/105378220) · UniProt [A0A1B0GUY1](https://www.uniprot.org/uniprotkb/A0A1B0GUY1) · Ensembl [ENSG00000248109](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248109)

## Data

Gene col 14518: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14518); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14518, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14518]; `tensor/DDL_lfc|DDL_z.npy` [14518]; `embed/gene_vectors.npy` [14518]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14518 or target_col == 14518). Every well: [[MARCOL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARCOL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
