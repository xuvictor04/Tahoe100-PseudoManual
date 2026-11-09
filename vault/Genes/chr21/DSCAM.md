---
symbol: "DSCAM"
type: "gene"
col: 10135
ensembl_id: "ENSG00000171587"
name: "DS cell adhesion molecule"
location: "21q22.2"
module: 13
arm: "+"
pooled_cpm: 11.93
n_lines_expressing: 13
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 18
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# DSCAM

*DS cell adhesion molecule* — 21q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.78× (z +17.7, q 0e+00, up in 4 of 8 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LOX-IMVI 0.151×, NCI-H1573 0.164×); [[Panobinostat (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0683×); [[Panobinostat (drug)]] 5 µM in 1 line (LOX-IMVI 0.0734×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NLRP3]] (+0.67, fdr 7e-06), [[MARCHF4]] (+0.64, fdr 7e-06), [[ADAMTS18]] (+0.62, fdr 3e-05); moves opposite to [[DHRS3]] (-0.45, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 18 go from it, the strongest it → [[DIRC3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10135.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.78×** | +17.7 | 0e+00 | 4/8 (HOP62, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.19×** | +11.1 | 6e-26 | 1/5 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.40×** | +10.0 | 5e-21 | 6/10 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.35×** | +9.7 | 4e-20 | 2/8 (HOP62, NCI-H23) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.87×** | +8.5 | 3e-15 | 2/6 (HOP62, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **2.04×** | +8.1 | 4e-14 | 8/10 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.79×** | +7.6 | 2e-12 | 1/4 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.60×** | +7.0 | 2e-10 | 2/9 (BT-474, HOP62) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +6.1 | 5e-08 | 0/8 | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.04×** | +5.7 | 6e-07 | 5/10 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +5.3 | 7e-06 | 4/9 (SNU-423, NCI-H1573, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.74×** | +4.5 | 4e-04 | 4/9 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[vincristine (drug)]] 0.5 µM |  | **2.16×** | +4.4 | 5e-04 | 6/8 (NCI-H1573, BT-474, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +4.1 | 0.002 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.64×** | +3.8 | 0.006 | 3/9 (BT-474, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.84×** | +3.5 | 0.015 | 2/7 (HOP62, NCI-H23) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +3.4 | 0.019 | 2/9 (NCI-H23, SNU-423) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 5 µM |  | **2.24×** | +3.4 | 0.021 | 5/7 (NCI-H1573, BT-474, …) | two highest doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10135.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LOX-IMVI 0.151×, NCI-H1573 0.164×); [[Panobinostat (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0683×); [[Panobinostat (drug)]] 5 µM in 1 line (LOX-IMVI 0.0734×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.887× | -3.2 | 0.44 | 2/11 (HOP62, NCI-H23) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.661× | -3.0 | 0.44 | 5/10 (NCI-H1573, AN3 CA, …) | inconsistent across doses |  |
| [[Minodronic acid (drug)]] 0.05 µM |  | 0.668× | -3.0 | 0.44 | 0/10 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10135. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 378 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0683× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 32.1 | 4 (2 ⚠) | 1 | [[Vinblastine (sulfate) (drug)]] 5 µM 6.85× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 3.60 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 32.9× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 5.91 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 12.4× (z +9.2) | — |
| [[A-172 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.40 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10135), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NLRP3]] | +0.67 | +0.63 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[MARCHF4]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS18]] | +0.62 | +0.46 / +0.64 | both halves | 3e-05 | **novel candidate** |
| [[LNCOG]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[NTM]] | +0.59 | +0.41 / +0.67 | both halves | 4e-05 | same gene group |
| [[VEPH1]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[NTNG1]] | +0.58 | +0.48 / +0.56 | both halves | 2e-05 | STRING 469 |
| [[RDUR]] | +0.58 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[ADTRP]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[SAMD3]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ROBO4]] | +0.57 | +0.45 / +0.64 | both halves | 3e-05 | same gene group |
| [[FGF5]] | +0.56 | +0.47 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHRS3]] | -0.45 | -0.34 / -0.42 | both halves | 1e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DSCAM's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NOL4]] | C | NOL4 activity raises DSCAM's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 1.99× lower at baseline in the lines without NOL4 | 0.050 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent; co-absent with the target |
| [[PSG5]] | C | PSG5 activity raises DSCAM's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 2.40× lower at baseline in the lines without PSG5 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |
| [[AJAP1]] | C | AJAP1 activity raises DSCAM's level | lines that do not express AJAP1 (40) vs lines expressing it (10) | 3.09× lower at baseline in the lines without AJAP1 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000230972, LINC01425; co-absent with the target |
| [[NETO1]] | C | NETO1 activity raises DSCAM's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 3.05× lower at baseline in the lines without NETO1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 7, C 11. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIRC3-AS1]] | B | DSCAM activity raises DIRC3-AS1's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 2.79× lower at baseline in the lines without DSCAM | 0.007 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent |
| [[CACNA1A]] | B | DSCAM activity raises CACNA1A's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 3.33× lower at baseline in the lines without DSCAM | 0.011 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent |
| [[FAM167A]] | B | DSCAM activity raises FAM167A's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 2.48× lower at baseline in the lines without DSCAM | 0.051 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent |
| [[KBTBD8]] | B | DSCAM activity raises KBTBD8's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 1.51× lower at baseline in the lines without DSCAM | 0.064 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent |
| [[BMAL2-AS1]] | B | DSCAM activity raises BMAL2-AS1's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 1.12× lower at baseline in the lines without DSCAM | 0.076 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent |
| [[RETREG1-AS1]] | B | DSCAM activity raises RETREG1-AS1's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 1.14× lower at baseline in the lines without DSCAM | 0.089 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent |
| [[CACNA1A]] | B | DSCAM activity weakens CACNA1A's drug response | lines that do not express DSCAM (24) vs lines expressing it (11) | the lines without DSCAM respond 10.06× as strongly (z diff -2.64); strongest at Panobinostat 5 µM: 1.73x vs 0.61x (z diff -4.8) | 0.096 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[NOL4]] | C | DSCAM activity raises NOL4's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 2.95× lower at baseline in the lines without DSCAM | 0.020 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent; co-absent with the target |
| [[PHACTR1]] | C | DSCAM activity raises PHACTR1's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 2.59× lower at baseline in the lines without DSCAM | 0.021 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent; co-absent with the target |
| [[SHANK1]] | C | DSCAM activity raises SHANK1's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 2.36× lower at baseline in the lines without DSCAM | 0.025 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent; co-absent with the target |
| [[NLRP3]] | C | DSCAM activity raises NLRP3's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 3.05× lower at baseline in the lines without DSCAM | 0.033 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent; co-absent with the target |
| [[SAMD3]] | C | DSCAM activity raises SAMD3's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 3.30× lower at baseline in the lines without DSCAM | 0.033 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.326). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.6, 12.2); signed map (17.4, 46.2). **Vector** length 35.8, 11.4% of its response variance represented; |z| ≥ 3 in 292 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +17.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +8.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.6 | +4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.4 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -0.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.9 | -2.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | DS cell adhesion molecule |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.2 — chr21:40,010,999-40,847,158 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CHD2-42, CHD2-52 |
| Gene groups (HGNC) | Fibronectin type III domain containing; V-set domain containing; I-set domain containing; Ig-like cell adhesion molecule family; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: DSCAM interactions; Netrin-1 signaling; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [O60469](https://www.uniprot.org/uniprotkb/O60469) (Cell adhesion molecule DSCAM):

> Cell adhesion molecule that plays a role in neuronal self-avoidance. Promotes repulsion between specific neuronal processes of either the same cell or the same subtype of cells. Mediates within retinal amacrine and ganglion cell subtypes both isoneuronal self-avoidance for creating an orderly dendritic arborization and heteroneuronal self-avoidance to maintain the mosaic spacing between amacrine and ganglion cell bodies. Receptor for netrin required for axon guidance independently of and in …

**Summary**, from NCBI Gene [1826](https://www.ncbi.nlm.nih.gov/gene/1826):

> This gene is a member of the immunoglobulin superfamily of cell adhesion molecules (Ig-CAMs), and is involved in human central and peripheral nervous system development. This gene is a candidate for Down syndrome and congenital heart disease (DSCHD). A gene encoding a similar Ig-CAM protein is located on chromosome 11. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:3039](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3039) · Entrez [1826](https://www.ncbi.nlm.nih.gov/gene/1826) · UniProt [O60469](https://www.uniprot.org/uniprotkb/O60469) · Ensembl [ENSG00000171587](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171587)

## Data

Gene col 10135: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10135); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10135, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10135]; `tensor/DDL_lfc|DDL_z.npy` [10135]; `embed/gene_vectors.npy` [10135]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10135 or target_col == 10135). Every well: [[DSCAM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DSCAM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
