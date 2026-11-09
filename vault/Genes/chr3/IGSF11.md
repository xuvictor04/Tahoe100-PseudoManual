---
symbol: "IGSF11"
type: "gene"
col: 6937
ensembl_id: "ENSG00000144847"
name: "immunoglobulin superfamily member 11"
location: "3q13.32"
module: 26
arm: "+"
pooled_cpm: 7.89
n_lines_expressing: 40
n_dd_up: 45
n_dd_down: 1
n_dd_up_clean: 38
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 12
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# IGSF11

*immunoglobulin superfamily member 11* — 3q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 12.7× (z +39.3, q 0e+00, up in 28 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.706× (z -3.8, q 0.076, down in 12 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 0.0565×, NCI-H2030 0.135×; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0682×); [[Harringtonine (drug)]] 0.5 µM in 1 line (A549 0.153×; ⚠ cell-cycle shift, explains ~0% of this change); [[Estrone sulfate (potassium) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0750×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (NCI-H460 0.182×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CASS4]] (+0.73, fdr 1e-05), [[H2AZ1-DT]] (+0.71, fdr 2e-05), [[SNX31]] (+0.70, fdr 7e-06); moves opposite to [[HERC2P2]] (-0.59, fdr 1e-04), [[ZHX3]] (-0.58, fdr 2e-04), [[HERC2P9]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC00278]] → it (grade B ⚠); 12 go from it, the strongest it → [[CPEB2-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6937.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **12.7×** | +39.3 | 0e+00 | 28/29 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **6.26×** | +28.4 | 0e+00 | 27/30 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **10.2×** | +24.4 | 0e+00 | 25/28 (HS-578T, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **6.93×** | +20.4 | 0e+00 | 23/27 (HS-578T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.60×** | +14.0 | 2e-42 | 21/33 (LoVo, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.29×** | +13.0 | 9e-37 | 21/28 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.91×** | +11.7 | 2e-29 | 21/35 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.11×** | +11.6 | 5e-29 | 23/35 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **2.00×** | +10.7 | 6e-25 | 22/35 (CFPAC-1, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **6.17×** | +10.4 | 1e-23 | 26/32 (A498, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.36×** | +9.4 | 4e-19 | 19/34 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +8.5 | 9e-16 | 2/8 (HS-578T, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.09×** | +8.1 | 3e-14 | 20/33 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +6.8 | 6e-10 | 16/35 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +6.4 | 7e-09 | 13/36 (HEC-1-A, HS-578T, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.77×** | +6.2 | 2e-08 | 15/34 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6937.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 0.0565×, NCI-H2030 0.135×; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0682×); [[Harringtonine (drug)]] 0.5 µM in 1 line (A549 0.153×; ⚠ cell-cycle shift, explains ~0% of this change); [[Estrone sulfate (potassium) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0750×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (NCI-H460 0.182×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.706×** | -3.8 | 0.076 | 12/34 (A549, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6937. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 13.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +14.4) | — |
| [[HEC-1-A (line)]] | alt | 7.34 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +14.5) | — |
| [[HS-578T (line)]] | alt | 9.58 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.1× (z +17.7) | — |
| [[PANC-1 (line)]] | alt | 2.56 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.9× (z +13.8) | — |
| [[A498 (line)]] | wt | 12.0 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.15× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.0565× (z -15.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 21.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.67× (z +12.6) | — |
| [[HOP62 (line)]] | alt | 2.12 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.8× (z +14.0) | — |
| [[NCI-H460 (line)]] | wt | 6.24 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +11.3) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.182× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 7.66 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.23× (z +10.8) | [[Ixazomib citrate (drug)]] 0.5 µM 0.0682× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 6.23 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +10.2) | — |
| [[J82 (line)]] | alt | 2.70 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.8× (z +11.5) | — |
| [[LoVo (line)]] | wt | 5.43 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.7× (z +17.1) | — |
| [[NCI-H1573 (line)]] | alt | 10.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.22× (z +13.0) | — |
| [[A-172 (line)]] | wt | 4.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.3× (z +14.5) | — |
| [[A549 (line)]] | wt | 117 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.153× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 3.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 6.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.2× (z +12.5) | — |
| [[HepG2_C3A (line)]] | wt | 2.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 58.5× (z +12.8) | — |
| [[Hs 766T (line)]] | wt | 4.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 2.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 3.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.5× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 2.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.0× (z +10.7) | — |
| [[SHP-77 (line)]] | alt | 8.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.81× (z +11.5) | — |
| [[SK-MEL-2 (line)]] | alt | 7.27 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 12.4× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 2.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.5× (z +11.3) | — |
| [[A-427 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.82 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6937), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASS4]] | +0.73 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[H2AZ1-DT]] | +0.71 | +0.74 / +0.48 | both halves | 2e-05 |  |
| [[SNX31]] | +0.70 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[N4BP2L1]] | +0.69 | +0.72 / +0.43 | both halves | 3e-05 |  |
| [[C2CD6]] | +0.69 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[LINC02763]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.68 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[NEB]] | +0.67 | +0.70 / +0.46 | both halves | 2e-05 |  |
| [[LINC01208]] | +0.67 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[ADCY10]] | +0.67 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[UPP2]] | +0.66 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[KLRD1]] | +0.66 | +0.63 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2P2]] | -0.59 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[ZHX3]] | -0.58 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[HERC2P9]] | -0.57 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[NAA40]] | -0.57 | -0.48 / -0.21 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00278]] | B | LINC00278 activity raises IGSF11's level | lines that do not express LINC00278 (32) vs lines expressing it (18) | 1.90× lower at baseline in the lines without LINC00278 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZFY, PRKY, RPS4Y1 |
| [[ITIH2]] | B | ITIH2 activity raises IGSF11's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 2.13× lower at baseline in the lines without ITIH2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH |
| [[IRF4]] | B | IRF4 activity raises IGSF11's level | lines that do not express IRF4 (34) vs lines expressing it (16) | 1.99× lower at baseline in the lines without IRF4 | 0.039 | ⚠ within organs, on part of the lines; also absent: CHL1, CPS1, UPK1B |
| [[TOP2A]] | B | TOP2A activity lowers IGSF11's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IGFBP1]] | B | IGFBP1 activity raises IGSF11's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 1.76× lower at baseline in the lines without IGFBP1 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2 |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CPEB2-DT]] | B | IGSF11 activity raises CPEB2-DT's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.70× lower at baseline in the lines without IGSF11 | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[DNAH10]] | B | IGSF11 activity raises DNAH10's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.55× lower at baseline in the lines without IGSF11 | 0.029 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[TPTE2]] | B | IGSF11 activity raises TPTE2's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.64× lower at baseline in the lines without IGSF11 | 0.044 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[USP38-DT]] | B | IGSF11 activity raises USP38-DT's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.63× lower at baseline in the lines without IGSF11 | 0.045 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[CFAP53]] | B | IGSF11 activity raises CFAP53's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.43× lower at baseline in the lines without IGSF11 | 0.047 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[TBCE-1]] | B | IGSF11 activity raises TBCE-1's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without IGSF11 | 0.059 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[CCDC30]] | B | IGSF11 activity raises CCDC30's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.68× lower at baseline in the lines without IGSF11 | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[COLQ]] | B | IGSF11 activity raises COLQ's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.69× lower at baseline in the lines without IGSF11 | 0.077 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[CMYA5]] | B | IGSF11 activity raises CMYA5's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.80× lower at baseline in the lines without IGSF11 | 0.077 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[SNX31]] | B | IGSF11 activity raises SNX31's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.77× lower at baseline in the lines without IGSF11 | 0.077 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[DENND6A-AS1]] | B | IGSF11 activity raises DENND6A-AS1's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.18× lower at baseline in the lines without IGSF11 | 0.090 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[LINC02398]] | C | IGSF11 activity raises LINC02398's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 2.32× lower at baseline in the lines without IGSF11 | 0.055 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.679). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (12.0, 17.8); signed map (24.3, 0.1). **Vector** length 66.0, 11.7% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +39.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +28.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +20.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +8.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +24.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +11.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +14.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +6.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +5.4 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | +6.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.3 | +9.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.4 | -0.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | immunoglobulin superfamily member 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.32 — chr3:118,900,557-119,146,068 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BT-IgSF, MGC35227, Igsf13, VSIG3, CT119 |
| Gene groups (HGNC) | V-set domain containing; I-set domain containing; IgCAM CXADR-related subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5DX21](https://www.uniprot.org/uniprotkb/Q5DX21) (Immunoglobulin superfamily member 11):

> Functions as a cell adhesion molecule through homophilic interaction. Stimulates cell growth.

**Summary**, from NCBI Gene [152404](https://www.ncbi.nlm.nih.gov/gene/152404):

> IGSF11 is an immunoglobulin (Ig) superfamily member that is preferentially expressed in brain and testis. It shares significant homology with coxsackievirus and adenovirus receptor (CXADR; MIM 602621) and endothelial cell-selective adhesion molecule (ESAM).[supplied by OMIM, Apr 2005]

**Accessions** — [HGNC:16669](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16669) · Entrez [152404](https://www.ncbi.nlm.nih.gov/gene/152404) · UniProt [Q5DX21](https://www.uniprot.org/uniprotkb/Q5DX21) · Ensembl [ENSG00000144847](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144847)

## Data

Gene col 6937: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6937); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6937, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6937]; `tensor/DDL_lfc|DDL_z.npy` [6937]; `embed/gene_vectors.npy` [6937]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6937 or target_col == 6937). Every well: [[IGSF11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGSF11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
