---
symbol: "MUC2"
type: "gene"
col: 12676
ensembl_id: "ENSG00000198788"
name: "mucin 2, oligomeric mucus/gel-forming"
location: "11p15.5"
module: 73
arm: "+"
pooled_cpm: 4.3
n_lines_expressing: 8
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 49
direction_downstream: 53
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# MUC2

*mucin 2, oligomeric mucus/gel-forming* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 9.07× (z +8.6, q 4e-15, up in 2 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.77× (z +5.9, q 5e-07, up in 0 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.00636×; ⚠ cell-cycle shift, explains ~32% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (LoVo 0.0342×); [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.0643×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEACAM6]] (+0.80, fdr 7e-06), [[CAPN8]] (+0.80, fdr 7e-06), [[MUC5AC]] (+0.79, fdr 7e-06, ⚠ same locus), [[CEACAM5]] (+0.77, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 49 arrows point to it, the strongest [[IL33]] → it (grade C ⚠); 53 go from it, the strongest it → [[AQP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12676.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.07×** | +8.6 | 4e-15 | 2/3 (LS 180, HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.67×** | +7.8 | 1e-12 | 3/4 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.64×** | +6.0 | 4e-07 | 3/3 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.77×** | +5.9 | 5e-07 | 0/5 | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.59×** | +5.2 | 2e-05 | 0/5 | top dose only | cell-cycle shift (explains ~9% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.82×** | +4.6 | 4e-04 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +4.5 | 6e-04 | 0/5 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.94×** | +4.2 | 0.002 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.47×** | +3.7 | 0.014 | 0/5 | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.27×** | +3.2 | 0.091 | 1/4 (Hs 766T) | top dose only | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12676.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.00636×; ⚠ cell-cycle shift, explains ~32% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (LoVo 0.0342×); [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.0643×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | 0.419× | -3.5 | 0.29 | 0/6 | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12676. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 71.1 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0342× (z -12.0) |
| [[LS 180 (line)]] | wt | 55.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.00636× (z -14.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0643× (z -11.5) |
| [[A-172 (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.251 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.235 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.758 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.656 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.234 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.944 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.398 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.256 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.274 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.324 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.625 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.355 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.216 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.360 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.152 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.183 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.264 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.188 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.266 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.242 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.371 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.314 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12676), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEACAM6]] | +0.80 | +0.77 / +0.72 | both halves | 7e-06 | STRING 453 |
| [[CAPN8]] | +0.80 | +0.81 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[MUC5AC]] | +0.79 | +0.74 / +0.77 | both halves | 7e-06 | same gene group; pathway: C-type lectin receptors (CLRs); STRING 909; ⚠ same locus (47.4 kb, same strand: neighbours can correlate without regulation) |
| [[CEACAM5]] | +0.77 | +0.75 / +0.66 | both halves | 7e-06 | STRING 611 |
| [[CTSE]] | +0.74 | +0.72 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[REG4]] | +0.72 | +0.69 / +0.74 | both halves | 7e-06 | STRING 608 |
| [[FAM3D]] | +0.69 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[KLK10]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[EPHA1]] | +0.65 | +0.62 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[LAD1]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[TFF2]] | +0.64 | +0.57 / +0.64 | both halves | 1e-05 | STRING 646 |
| [[COL17A1]] | +0.64 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[TPTEP1-1]] | +0.63 | +0.64 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 0, C 49. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL33]] | C | IL33 activity raises MUC2's level | lines that do not express IL33 (35) vs lines expressing it (15) | 2.51× lower at baseline in the lines without IL33 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01133, MUC2, LINC01411; co-absent with the target |
| [[REG4]] | C | REG4 activity raises MUC2's level | lines that do not express REG4 (43) vs lines expressing it (7) | 5.79× lower at baseline in the lines without REG4 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[LINC01440]] | C | LINC01440 activity raises MUC2's level | lines that do not express LINC01440 (40) vs lines expressing it (10) | 3.26× lower at baseline in the lines without LINC01440 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000277757, ENSG00000230975, SYT4; maybe low, not absent; co-absent with the target |
| [[CFTR]] | C | CFTR activity raises MUC2's level | lines that do not express CFTR (39) vs lines expressing it (11) | 3.04× lower at baseline in the lines without CFTR | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent; co-absent with the target |
| [[LINC02582]] | C | LINC02582 activity raises MUC2's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 3.27× lower at baseline in the lines without LINC02582 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |
| [[CTSE]] | C | CTSE activity raises MUC2's level | lines that do not express CTSE (42) vs lines expressing it (8) | 4.02× lower at baseline in the lines without CTSE | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, REG4, CFTR; co-absent with the target |
| [[TPTEP1-1]] | C | TPTEP1-1 activity raises MUC2's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 2.85× lower at baseline in the lines without TPTEP1-1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises MUC2's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 3.47× lower at baseline in the lines without CEACAM5 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[CEACAM6]] | C | CEACAM6 activity raises MUC2's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 3.21× lower at baseline in the lines without CEACAM6 | 0.012 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; co-absent with the target |
| [[FAM3D]] | C | FAM3D activity raises MUC2's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 5.61× lower at baseline in the lines without FAM3D | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent; co-absent with the target |
| [[MMP28]] | C | MMP28 activity raises MUC2's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.59× lower at baseline in the lines without MMP28 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises MUC2's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 4.56× lower at baseline in the lines without NPSR1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |

### Downstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 9, C 44. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AQP3]] | B | MUC2 activity raises AQP3's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 4.36× lower at baseline in the lines without MUC2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4 |
| [[PITPNM3]] | B | MUC2 activity raises PITPNM3's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 2.44× lower at baseline in the lines without MUC2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4 |
| [[B4GALNT3]] | B | MUC2 activity raises B4GALNT3's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 3.22× lower at baseline in the lines without MUC2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4 |
| [[ALS2CL]] | B | MUC2 activity raises ALS2CL's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 3.48× lower at baseline in the lines without MUC2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4 |
| [[PITPNM3]] | B | MUC2 activity strengthens PITPNM3's drug response | lines that do not express MUC2 (36) vs lines expressing it (6) | the lines without MUC2 respond 0.47× as strongly (z diff +2.18); strongest at Panobinostat 0.5 µM: 0.59x vs 0.22x (z diff +5.0) | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; target measured in part of the lines; artifact flags |
| [[ABHD11]] | B | MUC2 activity raises ABHD11's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 2.72× lower at baseline in the lines without MUC2 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4 |
| [[SEPTIN9-DT]] | B | MUC2 activity raises SEPTIN9-DT's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 2.15× lower at baseline in the lines without MUC2 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4 |
| [[ADAP1]] | B | MUC2 activity raises ADAP1's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 2.54× lower at baseline in the lines without MUC2 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4 |
| [[HTR1D]] | B | MUC2 activity raises HTR1D's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 2.04× lower at baseline in the lines without MUC2 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4 |
| [[FXYD3]] | C | MUC2 activity raises FXYD3's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 7.96× lower at baseline in the lines without MUC2 | 8e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; co-absent with the target |
| [[CFTR]] | C | MUC2 activity raises CFTR's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 4.80× lower at baseline in the lines without MUC2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; co-absent with the target |
| [[HEPH]] | C | MUC2 activity raises HEPH's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 5.26× lower at baseline in the lines without MUC2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.734). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.9, 50.9); signed map (67.0, 9.6). **Vector** length 23.5, 9.81% of its response variance represented; |z| ≥ 3 in 130 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.2 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.7 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +1.9 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +0.5 | +0.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.5 | +1.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.6 | -0.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.5 | -3.0 |
|  | [[EX229 (drug)]] 5 µM |  | -0.5 | -0.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -0.5 | -0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -0.5 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | mucin 2, oligomeric mucus/gel-forming |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:1,074,875-1,110,511 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MLP, MUC-2 |
| Gene groups (HGNC) | Mucins |
| Reactome | 12 pathways, smallest: Defective GALNT12 causes CRCS1; Defective GALNT3 causes HFTC; Defective C1GALT1C1 causes TNPS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02817](https://www.uniprot.org/uniprotkb/Q02817) (Mucin-2):

> Coats the epithelia of the intestines and other mucus membrane-containing organs to provide a protective, lubricating barrier against particles and infectious agents at mucosal surfaces. Major constituent of the colon mucus, which is mainly formed by large polymeric networks of MUC2 secreted by goblet cells that cover the exposed surfaces of intestine. MUC2 networks form hydrogels that guard the underlying epithelium from pathogens and other hazardous matter entering from the outside world, …

**Summary**, from NCBI Gene [4583](https://www.ncbi.nlm.nih.gov/gene/4583):

> This gene encodes a member of the mucin protein family. Mucins are high molecular weight glycoproteins produced by many epithelial tissues. The protein encoded by this gene is secreted and forms an insoluble mucous barrier that protects the gut lumen. The protein polymerizes into a gel of which 80% is composed of oligosaccharide side chains by weight. The protein features a central domain containing tandem repeats rich in threonine and proline that varies between 50 and 115 copies in different …

**Accessions** — [HGNC:7512](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7512) · Entrez [4583](https://www.ncbi.nlm.nih.gov/gene/4583) · UniProt [Q02817](https://www.uniprot.org/uniprotkb/Q02817) · Ensembl [ENSG00000198788](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198788)

## Data

Gene col 12676: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12676); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12676, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12676]; `tensor/DDL_lfc|DDL_z.npy` [12676]; `embed/gene_vectors.npy` [12676]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12676 or target_col == 12676). Every well: [[MUC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MUC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
