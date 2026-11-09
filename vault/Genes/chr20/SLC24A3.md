---
symbol: "SLC24A3"
type: "gene"
col: 11617
ensembl_id: "ENSG00000185052"
name: "solute carrier family 24 member 3"
location: "20p11.23"
module: 27
arm: "+"
pooled_cpm: 10.77
n_lines_expressing: 13
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 14
direction_downstream: 27
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# SLC24A3

*solute carrier family 24 member 3* — 20p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.00× (z +15.3, q 0e+00, up in 1 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 0.123×, NCI-H1573 0.231×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HS-578T 0.169×); [[Docetaxel (drug)]] 0.05 µM in 1 line (COLO 205 0.0426×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00648]] (+0.53, fdr 5e-05), [[SYNDIG1]] (+0.53, fdr 2e-05), [[MIR2052HG]] (+0.52, fdr 4e-05); moves opposite to [[MRPL37]] (-0.38, fdr 2e-04), [[PHKA1]] (-0.35, fdr 2e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 27 go from it, the strongest it → [[NCALD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11617.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.00×** | +15.3 | 0e+00 | 1/11 (LoVo) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.22×** | +14.2 | 3e-43 | 1/7 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.07×** | +10.3 | 1e-22 | 1/4 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.99×** | +9.2 | 7e-18 | 1/5 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +6.8 | 1e-09 | 1/9 (SW 900) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +6.5 | 8e-09 | 2/11 (LoVo, SHP-77) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +5.3 | 1e-05 | 2/9 (COLO 205, SW 900) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.65×** | +5.0 | 5e-05 | 1/11 (LoVo) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +4.0 | 0.004 | 1/10 (LoVo) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.15×** | +3.9 | 0.005 | 0/7 | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.030 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.045 | 0/9 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.067 | 1/11 (NCI-H1573) | rises with dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11617.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 0.123×, NCI-H1573 0.231×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HS-578T 0.169×); [[Docetaxel (drug)]] 0.05 µM in 1 line (COLO 205 0.0426×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.697× | -3.6 | 0.22 | 3/9 (NCI-H1573, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.719× | -3.2 | 0.22 | 3/10 (HS-578T, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.913× | -3.2 | 0.22 | 0/12 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11617. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 169 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -18.0) |
| [[COLO 205 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0426× (z -13.5) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 23.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -9.2) |
| [[A-172 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11617), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00648]] | +0.53 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[SYNDIG1]] | +0.53 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[MIR2052HG]] | +0.52 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[SLCO6A1]] | +0.51 | +0.45 / +0.38 | both halves | 6e-05 |  |
| [[LINC02360]] | +0.51 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[NTF3]] | +0.50 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[LINC01285]] | +0.49 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[GPR141]] | +0.48 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[LINC01905]] | +0.48 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[LINC01605]] | +0.46 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[LINC02405]] | +0.46 | +0.35 / +0.42 | both halves | 1e-04 |  |
| [[SATB1-AS1]] | +0.45 | +0.41 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL37]] | -0.38 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[PHKA1]] | -0.35 | -0.30 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 1, C 13. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC24A3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ADAM28]] | C | ADAM28 activity raises SLC24A3's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 3.21× lower at baseline in the lines without ADAM28 | 0.003 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5; co-absent with the target |
| [[MGC32805]] | C | MGC32805 activity raises SLC24A3's level | lines that do not express MGC32805 (32) vs lines expressing it (18) | 2.09× lower at baseline in the lines without MGC32805 | 0.007 | ⚠ within organs, on part of the lines; also absent: CEACAM5, ST18, PRR15L; maybe low, not absent; co-absent with the target |
| [[LINC01456]] | C | LINC01456 activity raises SLC24A3's level | lines that do not express LINC01456 (42) vs lines expressing it (8) | 4.06× lower at baseline in the lines without LINC01456 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, S100A8; co-absent with the target |
| [[LINC00540]] | C | LINC00540 activity raises SLC24A3's level | lines that do not express LINC00540 (33) vs lines expressing it (17) | 2.83× lower at baseline in the lines without LINC00540 | 0.017 | ⚠ within organs, on part of the lines; also absent: CPLX2, SLC24A3, CHGB; co-absent with the target |
| [[ADGRG7]] | C | ADGRG7 activity raises SLC24A3's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 4.09× lower at baseline in the lines without ADGRG7 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172; co-absent with the target |
| [[LINC02405]] | C | LINC02405 activity raises SLC24A3's level | lines that do not express LINC02405 (27) vs lines expressing it (23) | 2.20× lower at baseline in the lines without LINC02405 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000286016, ENSG00000278266, LINC02360; co-absent with the target |
| [[ADAMTS14]] | C | ADAMTS14 activity raises SLC24A3's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 1.91× lower at baseline in the lines without ADAMTS14 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411; co-absent with the target |
| [[CARMN]] | C | CARMN activity raises SLC24A3's level | lines that do not express CARMN (40) vs lines expressing it (10) | 3.09× lower at baseline in the lines without CARMN | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |
| [[RFX8]] | C | RFX8 activity raises SLC24A3's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.72× lower at baseline in the lines without RFX8 | 0.054 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN; co-absent with the target |
| [[LINC00491]] | C | LINC00491 activity raises SLC24A3's level | lines that do not express LINC00491 (33) vs lines expressing it (17) | 1.56× lower at baseline in the lines without LINC00491 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APCDD1L, LINC01905, ADGRG7; co-absent with the target |
| [[LINC02253]] | C | LINC02253 activity raises SLC24A3's level | lines that do not express LINC02253 (35) vs lines expressing it (15) | 1.68× lower at baseline in the lines without LINC02253 | 0.071 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02058, ENSG00000289349; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 13, C 14. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCALD]] | B | SLC24A3 activity raises NCALD's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 2.62× lower at baseline in the lines without SLC24A3 | 0.007 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |
| [[CNTNAP2]] | B | SLC24A3 activity raises CNTNAP2's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 3.26× lower at baseline in the lines without SLC24A3 | 0.011 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |
| [[LINC00298]] | B | SLC24A3 activity raises LINC00298's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 2.34× lower at baseline in the lines without SLC24A3 | 0.023 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |
| [[NPTX1]] | B | SLC24A3 activity raises NPTX1's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 1.88× lower at baseline in the lines without SLC24A3 | 0.024 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |
| [[SLCO6A1]] | B | SLC24A3 activity raises SLCO6A1's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 1.78× lower at baseline in the lines without SLC24A3 | 0.040 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |
| [[STEAP2-AS1]] | B | SLC24A3 activity raises STEAP2-AS1's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 1.78× lower at baseline in the lines without SLC24A3 | 0.045 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |
| [[LINC01285]] | B | SLC24A3 activity raises LINC01285's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 1.89× lower at baseline in the lines without SLC24A3 | 0.046 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |
| [[CNTNAP2]] | B | SLC24A3 activity weakens CNTNAP2's drug response | lines that do not express SLC24A3 (27) vs lines expressing it (11) | the lines without SLC24A3 respond 2.93× as strongly (z diff -2.73); strongest at Dinaciclib 0.5 µM: 3.33x vs 1.21x (z diff -5.6) | 0.047 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ISM1]] | B | SLC24A3 activity raises ISM1's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 1.59× lower at baseline in the lines without SLC24A3 | 0.049 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |
| [[SLC14A2]] | B | SLC24A3 activity raises SLC14A2's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 1.68× lower at baseline in the lines without SLC24A3 | 0.053 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |
| [[SLC1A2]] | B | SLC24A3 activity raises SLC1A2's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 1.14× lower at baseline in the lines without SLC24A3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |
| [[CLVS1]] | B | SLC24A3 activity raises CLVS1's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 1.69× lower at baseline in the lines without SLC24A3 | 0.072 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.341). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.9, 39.8); signed map (49.7, 34.0). **Vector** length 32.4, 10.0% of its response variance represented; |z| ≥ 3 in 250 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +14.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +15.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.1 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +0.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +3.3 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -0.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 24 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.23 — chr20:19,212,642-19,722,926 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Solute carrier family 24 |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: Sodium/Calcium exchangers; Metal ion SLC transporters; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HC58](https://www.uniprot.org/uniprotkb/Q9HC58) (Sodium/potassium/calcium exchanger 3):

> Calcium, potassium:sodium antiporter that transports 1 Ca(2+) and 1 K(+) in exchange for 4 Na(+).

**Summary**, from NCBI Gene [57419](https://www.ncbi.nlm.nih.gov/gene/57419):

> Plasma membrane sodium/calcium exchangers are an important component of intracellular calcium homeostasis and electrical conduction. Potassium-dependent sodium/calcium exchangers such as SLC24A3 are believed to transport 1 intracellular calcium and 1 potassium ion in exchange for 4 extracellular sodium ions (Kraev et al., 2001 [PubMed 11294880]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:10977](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10977) · Entrez [57419](https://www.ncbi.nlm.nih.gov/gene/57419) · UniProt [Q9HC58](https://www.uniprot.org/uniprotkb/Q9HC58) · Ensembl [ENSG00000185052](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185052)

## Data

Gene col 11617: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11617); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11617, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11617]; `tensor/DDL_lfc|DDL_z.npy` [11617]; `embed/gene_vectors.npy` [11617]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11617 or target_col == 11617). Every well: [[SLC24A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC24A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
