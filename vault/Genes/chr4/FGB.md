---
symbol: "FGB"
type: "gene"
col: 10132
ensembl_id: "ENSG00000171564"
name: "fibrinogen beta chain"
location: "4q31.3"
module: 155
arm: "+"
pooled_cpm: 22.69
n_lines_expressing: 8
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 38
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# FGB

*fibrinogen beta chain* — 4q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.27× (z +12.6, q 7e-34, up in 3 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.99× (z +6.2, q 1e-07, up in 3 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (BT-474 0.0115×, CFPAC-1 0.0216×, NCI-H2030 0.133×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.0143×, BT-474 0.0169×); [[Tofacitinib (drug)]] 5 µM in 2 lines (CFPAC-1 0.0843×, BT-474 0.0607×); [[Tofacitinib (citrate) (drug)]] 0.5 µM in 1 line (BT-474 0.00942×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGG]] (+0.91, fdr 7e-06, ⚠ same locus), [[SERPINB3]] (+0.86, fdr 7e-06), [[SERPINB4]] (+0.84, fdr 7e-06), [[S100A9]] (+0.79, fdr 7e-06); moves opposite to [[PGR]] (-0.50, fdr 2e-05).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MAP2K2]] → it (grade B ⚠); 38 go from it, the strongest it → [[ODF3B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10132.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.27×** | +12.6 | 7e-34 | 3/5 (NCI-H2030, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.13×** | +10.0 | 4e-21 | 2/4 (HepG2/C3A, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +6.2 | 1e-07 | 3/6 (HepG2/C3A, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.52×** | +5.4 | 7e-06 | 2/4 (NCI-H2030, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.73×** | +3.5 | 0.060 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.60×** | +3.4 | 0.065 | 5/6 (HepG2/C3A, CFPAC-1, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.73×** | +3.4 | 0.065 | 5/6 (HepG2/C3A, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.3 | 0.067 | 2/6 (HepG2/C3A, NCI-H2030) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.68×** | +3.3 | 0.067 | 5/6 (CFPAC-1, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.64×** | +3.2 | 0.069 | 2/5 (NCI-H2030, HepG2/C3A) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10132.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (BT-474 0.0115×, CFPAC-1 0.0216×, NCI-H2030 0.133×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.0143×, BT-474 0.0169×); [[Tofacitinib (drug)]] 5 µM in 2 lines (CFPAC-1 0.0843×, BT-474 0.0607×); [[Tofacitinib (citrate) (drug)]] 0.5 µM in 1 line (BT-474 0.00942×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.574× | -3.6 | 0.17 | 6/6 (CFPAC-1, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.586× | -3.4 | 0.17 | 2/6 (BT-474, A549) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.579× | -3.3 | 0.18 | 0/6 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10132. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 79.1 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0115× (z -14.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.00942× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 67.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0216× (z -14.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0143× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 59.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 595 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -14.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.39 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10132), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGG]] | +0.91 | +0.88 / +0.92 | both halves | 7e-06 | same gene group; pathway: Aggregated β-amyloid interacts with fibrinogen; STRING 999; ⚠ same locus (31.3 kb: neighbours can correlate without regulation) |
| [[SERPINB3]] | +0.86 | +0.79 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[SERPINB4]] | +0.84 | +0.78 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[S100A9]] | +0.79 | +0.74 / +0.76 | both halves | 7e-06 | pathway: Antigen processing-Cross presentation; STRING 571 |
| [[S100A8]] | +0.75 | +0.69 / +0.73 | both halves | 7e-06 | pathway: Antigen processing-Cross presentation; STRING 577 |
| [[GSDMC]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[FGA]] | +0.70 | +0.64 / +0.79 | both halves | 7e-06 | same gene group; pathway: Aggregated β-amyloid interacts with fibrinogen; STRING 999; ⚠ same locus (10.3 kb: neighbours can correlate without regulation) |
| [[FLRT3]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[SLPI]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[LINC01440]] | +0.66 | +0.69 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[SERPINA1]] | +0.66 | +0.57 / +0.64 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation; STRING 810 |
| [[SERPINA3]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 590 |
| [[PDZK1IP1]] | +0.62 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[CDH3]] | +0.62 | +0.55 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGR]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K2]] | B | MAP2K2 activity lowers FGB's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[FGA]] | C | FGA activity raises FGB's level | lines that do not express FGA (43) vs lines expressing it (7) | 10.62× lower at baseline in the lines without FGA | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[FGG]] | C | FGG activity raises FGB's level | lines that do not express FGG (42) vs lines expressing it (8) | 10.94× lower at baseline in the lines without FGG | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[GPR141]] | C | GPR141 activity raises FGB's level | lines that do not express GPR141 (39) vs lines expressing it (11) | 3.88× lower at baseline in the lines without GPR141 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, S100A8, LINC00879; co-absent with the target |
| [[HLA-DRB1]] | C | HLA-DRB1 activity raises FGB's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 2.31× lower at baseline in the lines without HLA-DRB1 | 0.042 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP; co-absent with the target |
| [[P2RY2]] | C | P2RY2 activity raises FGB's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.42× lower at baseline in the lines without P2RY2 | 0.050 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223; co-absent with the target |
| [[SLPI]] | C | SLPI activity raises FGB's level | lines that do not express SLPI (25) vs lines expressing it (25) | 1.79× lower at baseline in the lines without SLPI | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2; co-absent with the target |

### Downstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 10, C 28. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ODF3B]] | B | FGB activity raises ODF3B's level | lines that do not express FGB (42) vs lines expressing it (8) | 2.76× lower at baseline in the lines without FGB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2 |
| [[FBXO39]] | B | FGB activity raises FBXO39's level | lines that do not express FGB (42) vs lines expressing it (8) | 2.53× lower at baseline in the lines without FGB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2 |
| [[SAA2]] | B | FGB activity raises SAA2's level | lines that do not express FGB (42) vs lines expressing it (8) | 3.11× lower at baseline in the lines without FGB | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2 |
| [[PROM2]] | B | FGB activity raises PROM2's level | lines that do not express FGB (42) vs lines expressing it (8) | 2.23× lower at baseline in the lines without FGB | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2 |
| [[STS]] | B | FGB activity raises STS's level | lines that do not express FGB (42) vs lines expressing it (8) | 2.48× lower at baseline in the lines without FGB | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2 |
| [[STAT3]] | B | FGB activity raises STAT3's level | lines that do not express FGB (42) vs lines expressing it (8) | 1.43× lower at baseline in the lines without FGB | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2 |
| [[OPN3]] | B | FGB activity raises OPN3's level | lines that do not express FGB (42) vs lines expressing it (8) | 2.45× lower at baseline in the lines without FGB | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2 |
| [[RGS6]] | B | FGB activity raises RGS6's level | lines that do not express FGB (42) vs lines expressing it (8) | 3.45× lower at baseline in the lines without FGB | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2 |
| [[RBPMS]] | B | FGB activity raises RBPMS's level | lines that do not express FGB (42) vs lines expressing it (8) | 2.82× lower at baseline in the lines without FGB | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2 |
| [[LGALS9]] | B | FGB activity raises LGALS9's level | lines that do not express FGB (42) vs lines expressing it (8) | 1.84× lower at baseline in the lines without FGB | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2 |
| [[FGA]] | C | FGB activity raises FGA's level | lines that do not express FGB (42) vs lines expressing it (8) | 7.06× lower at baseline in the lines without FGB | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2; co-absent with the target |
| [[HLA-DRB1]] | C | FGB activity raises HLA-DRB1's level | lines that do not express FGB (42) vs lines expressing it (8) | 3.32× lower at baseline in the lines without FGB | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2; co-absent with the target |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.864). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.5, 48.5); signed map (54.7, 23.5). **Vector** length 48.0, 22.8% of its response variance represented; |z| ≥ 3 in 308 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antimicrobial peptides* (reactome, mean cos +0.66 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.4 | +3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +3.4 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.5 | -1.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.4 | +0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.1 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | fibrinogen beta chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.3 — chr4:154,563,011-154,572,807 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Receptor ligands; Fibrinogen C domain containing; Fibrinogen chains; Coagulation factors |
| Reactome | 44 pathways, smallest: Aggregated β-amyloid interacts with fibrinogen; Fibrin formation; Defects of Coagulation cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [P02675](https://www.uniprot.org/uniprotkb/P02675) (Fibrinogen beta chain):

> Cleaved by the protease thrombin to yield monomers which, together with fibrinogen alpha (FGA) and fibrinogen gamma (FGG), polymerize to form an insoluble fibrin matrix. Fibrin has a major function in hemostasis as one of the primary components of blood clots. In addition, functions during the early stages of wound repair to stabilize the lesion and guide cell migration during re-epithelialization. Was originally thought to be essential for platelet aggregation, based on in vitro studies using …

**Summary**, from NCBI Gene [2244](https://www.ncbi.nlm.nih.gov/gene/2244):

> The protein encoded by this gene is the beta component of fibrinogen, a blood-borne glycoprotein comprised of three pairs of nonidentical polypeptide chains. Following vascular injury, fibrinogen is cleaved by thrombin to form fibrin which is the most abundant component of blood clots. In addition, various cleavage products of fibrinogen and fibrin regulate cell adhesion and spreading, display vasoconstrictor and chemotactic activities, and are mitogens for several cell types. Fibrinogen serves …

**Accessions** — [HGNC:3662](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3662) · Entrez [2244](https://www.ncbi.nlm.nih.gov/gene/2244) · UniProt [P02675](https://www.uniprot.org/uniprotkb/P02675) · Ensembl [ENSG00000171564](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171564)

## Data

Gene col 10132: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10132); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10132, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10132]; `tensor/DDL_lfc|DDL_z.npy` [10132]; `embed/gene_vectors.npy` [10132]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10132 or target_col == 10132). Every well: [[FGB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
