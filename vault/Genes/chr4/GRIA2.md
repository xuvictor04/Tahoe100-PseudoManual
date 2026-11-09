---
symbol: "GRIA2"
type: "gene"
col: 4168
ensembl_id: "ENSG00000120251"
name: "glutamate ionotropic receptor AMPA type subunit 2"
location: "4q32.1"
module: 9
arm: "+"
pooled_cpm: 2.06
n_lines_expressing: 17
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 26
direction_downstream: 7
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# GRIA2

*glutamate ionotropic receptor AMPA type subunit 2* — 4q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.49× (z +16.2, q 0e+00, up in 1 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0955×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.152×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRRM4]] (+0.77, fdr 7e-06), [[LRFN2]] (+0.76, fdr 7e-06), [[KCNH7]] (+0.75, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[SRRM4]] → it (grade C ⚠); 7 go from it, the strongest it → [[CDH18]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4168.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.49×** | +16.2 | 0e+00 | 1/5 (HOP62) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.72×** | +10.1 | 2e-21 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.38×** | +10.0 | 5e-21 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.88×** | +8.4 | 4e-15 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.01×** | +6.6 | 4e-09 | 2/6 (HOP62, CFPAC-1) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.92×** | +6.2 | 6e-08 | 7/11 (A-427, NCI-H23, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.20×** | +5.6 | 2e-06 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.28×** | +5.5 | 2e-06 | 2/9 (SW 900, A-427) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.20×** | +5.3 | 7e-06 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.12×** | +5.0 | 3e-05 | 3/8 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.00×** | +4.7 | 2e-04 | 6/11 (A-427, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.63×** | +4.6 | 2e-04 | 1/11 (SHP-77) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.92×** | +4.4 | 5e-04 | 0/3 | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.85×** | +4.1 | 0.001 | 5/10 (A-427, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.37×** | +4.1 | 0.001 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.82×** | +3.9 | 0.004 | 3/5 (SHP-77, SK-MEL-2, …) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.005 | 1/5 (SHP-77) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +3.5 | 0.014 | 0/4 | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +3.3 | 0.023 | 2/4 (A-427, SHP-77) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.97×** | +3.3 | 0.026 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4168.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0955×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.152×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | 0.600× | -3.5 | 0.30 | 1/10 (C-33 A) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4168. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 4.65 | 4 | 0 | [[Belinostat (drug)]] 5 µM 26.2× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 26.9 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0955× (z -12.0) |
| [[A-172 (line)]] | wt | 0.451 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.307 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.310 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.978 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.646 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.444 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.355 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.625 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.371 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.458 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.337 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.652 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.329 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.532 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.931 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.604 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.675 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.798 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.421 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.341 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4168), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRRM4]] | +0.77 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[LRFN2]] | +0.76 | +0.61 / +0.74 | both halves | 7e-06 | pathway: Neuronal System; STRING 411 |
| [[KCNH7]] | +0.75 | +0.57 / +0.79 | both halves | 1e-05 | pathway: Neuronal System |
| [[KHDRBS2]] | +0.75 | +0.61 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[NELL1]] | +0.75 | +0.64 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[SYT4]] | +0.75 | +0.57 / +0.77 | both halves | 9e-06 | STRING 614 |
| [[RIT2]] | +0.73 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[LINC02197]] | +0.73 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[ASCL1]] | +0.72 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[CDH10]] | +0.72 | +0.61 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CDH12]] | +0.71 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[NCAM2]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 0, C 26. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRRM4]] | C | SRRM4 activity raises GRIA2's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 4.02× lower at baseline in the lines without SRRM4 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises GRIA2's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 4.36× lower at baseline in the lines without ASCL1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[CCDC144NL-AS1]] | C | CCDC144NL-AS1 activity raises GRIA2's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 2.28× lower at baseline in the lines without CCDC144NL-AS1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[LINC02506]] | C | LINC02506 activity raises GRIA2's level | lines that do not express LINC02506 (40) vs lines expressing it (10) | 3.39× lower at baseline in the lines without LINC02506 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC01610, ENSG00000241168; co-absent with the target |
| [[AK4P3]] | C | AK4P3 activity raises GRIA2's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.76× lower at baseline in the lines without AK4P3 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises GRIA2's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 3.02× lower at baseline in the lines without KCNH7 | 0.027 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises GRIA2's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 2.72× lower at baseline in the lines without GABRG2 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[FUT9]] | C | FUT9 activity raises GRIA2's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 2.89× lower at baseline in the lines without FUT9 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[NLGN4X]] | C | NLGN4X activity raises GRIA2's level | lines that do not express NLGN4X (37) vs lines expressing it (13) | 2.80× lower at baseline in the lines without NLGN4X | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[LINC01446]] | C | LINC01446 activity raises GRIA2's level | lines that do not express LINC01446 (34) vs lines expressing it (16) | 2.43× lower at baseline in the lines without LINC01446 | 0.050 | ⚠ within organs, on part of the lines; also absent: GABRG2, BAGE2, ENSG00000253363; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises GRIA2's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 3.25× lower at baseline in the lines without KCNH5 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises GRIA2's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.12× lower at baseline in the lines without RUNX1T1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDH18]] | C | GRIA2 activity raises CDH18's level | lines that do not express GRIA2 (33) vs lines expressing it (17) | 3.62× lower at baseline in the lines without GRIA2 | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000286099, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[EPHA7]] | C | GRIA2 activity raises EPHA7's level | lines that do not express GRIA2 (33) vs lines expressing it (17) | 3.26× lower at baseline in the lines without GRIA2 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000286099, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[FGF14]] | C | GRIA2 activity raises FGF14's level | lines that do not express GRIA2 (33) vs lines expressing it (17) | 4.34× lower at baseline in the lines without GRIA2 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000286099, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[ADGRL3]] | C | GRIA2 activity raises ADGRL3's level | lines that do not express GRIA2 (33) vs lines expressing it (17) | 3.24× lower at baseline in the lines without GRIA2 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000286099, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[AK4P3]] | C | GRIA2 activity raises AK4P3's level | lines that do not express GRIA2 (33) vs lines expressing it (17) | 3.22× lower at baseline in the lines without GRIA2 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000286099, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[NPFFR2]] | C | GRIA2 activity raises NPFFR2's level | lines that do not express GRIA2 (33) vs lines expressing it (17) | 2.71× lower at baseline in the lines without GRIA2 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000286099, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[SNTG1]] | C | GRIA2 activity raises SNTG1's level | lines that do not express GRIA2 (33) vs lines expressing it (17) | 2.41× lower at baseline in the lines without GRIA2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000286099, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.770). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.8, 36.1); signed map (43.7, 35.0). **Vector** length 23.9, 6.04% of its response variance represented; |z| ≥ 3 in 241 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +16.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | -0.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +1.9 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -3.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -0.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.8 | -1.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -1.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | glutamate ionotropic receptor AMPA type subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.1 — chr4:157,204,182-157,387,146 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GluA2, GLURB, GluR-K2, GluR-B, GluR-2; previously GLUR2 |
| Gene groups (HGNC) | Glutamate ionotropic receptor AMPA type subunits |
| Reactome | 13 pathways, smallest: Activation of AMPA receptors; MECP2 regulates neuronal receptors and channels; Trafficking of GluR2-containing AMPA receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P42262](https://www.uniprot.org/uniprotkb/P42262) (Glutamate receptor 2):

> Ionotropic glutamate receptor that functions as a ligand-gated cation channel, gated by L-glutamate and glutamatergic agonists such as alpha-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid (AMPA), quisqualic acid, and kainic acid. L-glutamate acts as an excitatory neurotransmitter at many synapses in the central nervous system and plays an important role in fast excitatory synaptic transmission. Binding of the excitatory neurotransmitter L-glutamate induces a conformation change, leading to …

**Summary**, from NCBI Gene [2891](https://www.ncbi.nlm.nih.gov/gene/2891):

> Glutamate receptors are the predominant excitatory neurotransmitter receptors in the mammalian brain and are activated in a variety of normal neurophysiologic processes. This gene product belongs to a family of glutamate receptors that are sensitive to alpha-amino-3-hydroxy-5-methyl-4-isoxazole propionate (AMPA), and function as ligand-activated cation channels. These channels are assembled from 4 related subunits, GRIA1-4. The subunit encoded by this gene (GRIA2) is subject to RNA editing …

**Accessions** — [HGNC:4572](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4572) · Entrez [2891](https://www.ncbi.nlm.nih.gov/gene/2891) · UniProt [P42262](https://www.uniprot.org/uniprotkb/P42262) · Ensembl [ENSG00000120251](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120251)

## Data

Gene col 4168: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4168); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4168, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4168]; `tensor/DDL_lfc|DDL_z.npy` [4168]; `embed/gene_vectors.npy` [4168]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4168 or target_col == 4168). Every well: [[GRIA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRIA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
