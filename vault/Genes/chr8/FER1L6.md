---
symbol: "FER1L6"
type: "gene"
col: 13225
ensembl_id: "ENSG00000214814"
name: "fer-1 like family member 6"
location: "8q24.13"
module: 75
arm: "+"
pooled_cpm: 3.93
n_lines_expressing: 43
n_dd_up: 46
n_dd_down: 0
n_dd_up_clean: 35
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 17
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# FER1L6

*fer-1 like family member 6* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 46 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 16.5× (z +36.4, q 0e+00, up in 23 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 2 lines (KATO III 0.0481×, SNU-1 0.229×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.0654×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.0772×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (SNU-1 0.102×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01033]] (+0.83, fdr 7e-06), [[SYT16]] (+0.78, fdr 7e-06), [[LINC00616]] (+0.78, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 17 go from it, the strongest it → [[CUBN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 46 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13225.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **16.5×** | +36.4 | 0e+00 | 23/24 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **6.34×** | +23.9 | 0e+00 | 25/28 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **10.9×** | +21.9 | 0e+00 | 28/31 (HT-29, A498, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **8.97×** | +19.3 | 0e+00 | 10/17 (HS-578T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **3.66×** | +16.8 | 0e+00 | 16/37 (A498, HS-578T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **6.34×** | +16.3 | 0e+00 | 22/28 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.59×** | +12.3 | 7e-33 | 28/37 (KATO III, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.94×** | +12.1 | 9e-32 | 2/4 (LoVo, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.51×** | +11.5 | 8e-29 | 4/11 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.48×** | +11.4 | 2e-28 | 13/25 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.30×** | +10.1 | 3e-22 | 3/5 (HS-578T, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.58×** | +8.7 | 2e-16 | 17/34 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.37×** | +7.9 | 1e-13 | 19/30 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.11×** | +6.8 | 4e-10 | 16/38 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +5.8 | 2e-07 | 5/37 (A498, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +4.9 | 3e-05 | 11/33 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **2.72×** | +4.8 | 5e-05 | 9/30 (C32, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +4.4 | 3e-04 | 8/33 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13225.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 2 lines (KATO III 0.0481×, SNU-1 0.229×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.0654×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.0772×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (SNU-1 0.102×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.691× | -3.4 | 0.36 | 3/37 (HOP62, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13225. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 146 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0654× (z -16.2) |
| [[NCI-H460 (line)]] | wt | 1.12 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.8× (z +11.5) | — |
| [[A-172 (line)]] | wt | 1.10 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.1× (z +9.9) | — |
| [[C32 (line)]] | wt | 3.02 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.3× (z +11.7) | — |
| [[HS-578T (line)]] | alt | 3.75 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.7× (z +11.3) | — |
| [[A498 (line)]] | wt | 1.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 42.1× (z +12.8) | — |
| [[CFPAC-1 (line)]] | alt | 2.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 1.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.2× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 1.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.4× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 3.34 | 1 | 0 | [[Auranofin (drug)]] 5 µM 69.2× (z +10.4) | — |
| [[KATO III (line)]] | alt | 5.42 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0481× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 2.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.83× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 1.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.1× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 8.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.82× (z +10.4) | — |
| [[A-427 (line)]] | wt | 0.645 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.983 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.971 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.942 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.777 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.852 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13225), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01033]] | +0.83 | +0.71 / +0.80 | both halves | 7e-06 |  |
| [[SYT16]] | +0.78 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[LINC00616]] | +0.78 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[LINC00393]] | +0.76 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.75 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[PKD1L1]] | +0.75 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[LINC02955]] | +0.74 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[LINC01933]] | +0.74 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[IL12RB2]] | +0.74 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[MYO16]] | +0.74 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[PEBP4]] | +0.74 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[DNAH10]] | +0.74 | +0.68 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FER1L6's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 8.7% of all compounds | 0.015 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[LINC00457]] | B | LINC00457 activity raises FER1L6's level | lines that do not express LINC00457 (29) vs lines expressing it (21) | 1.30× lower at baseline in the lines without LINC00457 | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC01440, LINC01456, NTS; maybe low, not absent |
| [[LINC00958]] | B | LINC00958 activity raises FER1L6's level | lines that do not express LINC00958 (39) vs lines expressing it (11) | 1.22× lower at baseline in the lines without LINC00958 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SSX1, LINC01320, LINC00879 |
| [[LINC01917]] | B | LINC01917 activity raises FER1L6's level | lines that do not express LINC01917 (19) vs lines expressing it (31) | 1.65× lower at baseline in the lines without LINC01917 | 0.079 | ⚠ within organs, on part of the lines; also absent: LINC00504, RMEL3, TEK; maybe low, not absent |
| [[KCNIP4]] | B | KCNIP4 activity raises FER1L6's level | lines that do not express KCNIP4 (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without KCNIP4 | 0.096 | ⚠ within organs, on part of the lines; also absent: MLLT3, TEX9, MAMDC2-AS1; maybe low, not absent |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CUBN]] | B | FER1L6 activity lowers CUBN's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 3.02× higher at baseline in the lines without FER1L6 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[LINC02694]] | B | FER1L6 activity raises LINC02694's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without FER1L6 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[MMADHC-DT]] | B | FER1L6 activity raises MMADHC-DT's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 2.03× lower at baseline in the lines without FER1L6 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[SSUH2]] | B | FER1L6 activity raises SSUH2's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 2.14× lower at baseline in the lines without FER1L6 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[B3GALT1-AS1]] | B | FER1L6 activity raises B3GALT1-AS1's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 1.98× lower at baseline in the lines without FER1L6 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[NKAIN1]] | B | FER1L6 activity lowers NKAIN1's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 1.43× higher at baseline in the lines without FER1L6 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[MEIOC]] | B | FER1L6 activity lowers MEIOC's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 1.99× higher at baseline in the lines without FER1L6 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[LINC00393]] | B | FER1L6 activity raises LINC00393's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 1.47× lower at baseline in the lines without FER1L6 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[LINC03036]] | B | FER1L6 activity lowers LINC03036's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 1.36× higher at baseline in the lines without FER1L6 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| cells under [[Irinotecan (drug)]] 0.5 µM | B | FER1L6 activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express FER1L6 (7) vs lines expressing it (41) | the lines without FER1L6: 0.75× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[IGDCC4]] | B | FER1L6 activity lowers IGDCC4's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 2.02× higher at baseline in the lines without FER1L6 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[ARL13B]] | B | FER1L6 activity lowers ARL13B's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 1.64× higher at baseline in the lines without FER1L6 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.820). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.5, 26.1); signed map (23.8, 9.9). **Vector** length 60.7, 10.1% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.2 | +21.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +36.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +23.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +16.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +12.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +1.2 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | +1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.1 | +1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +0.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | fer-1 like family member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:123,851,987-124,120,061 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C8ORFK23 |
| Gene groups (HGNC) | Ferlin family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2WGJ9](https://www.uniprot.org/uniprotkb/Q2WGJ9) (Fer-1-like protein 6):

> Calcium/phospholipid-binding protein which is essential for proper development of skeletal and cardiac muscle.

**Summary**, from NCBI Gene [654463](https://www.ncbi.nlm.nih.gov/gene/654463):

> Predicted to enable calcium-dependent phospholipid binding activity. Predicted to be involved in cardiac muscle tissue development; positive regulation of gene expression; and skeletal muscle tissue development. Predicted to act upstream of or within response to bacterium. Located in plasma membrane; recycling endosome; and trans-Golgi network. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28065](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28065) · Entrez [654463](https://www.ncbi.nlm.nih.gov/gene/654463) · UniProt [Q2WGJ9](https://www.uniprot.org/uniprotkb/Q2WGJ9) · Ensembl [ENSG00000214814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214814)

## Data

Gene col 13225: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13225); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13225, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13225]; `tensor/DDL_lfc|DDL_z.npy` [13225]; `embed/gene_vectors.npy` [13225]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13225 or target_col == 13225). Every well: [[FER1L6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FER1L6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
