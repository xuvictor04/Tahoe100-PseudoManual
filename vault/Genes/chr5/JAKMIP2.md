---
symbol: "JAKMIP2"
type: "gene"
col: 10675
ensembl_id: "ENSG00000176049"
name: "janus kinase and microtubule interacting protein 2"
location: "5q32"
module: 108
arm: "+"
pooled_cpm: 7.34
n_lines_expressing: 21
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 22
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 11
direction_downstream: 16
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# JAKMIP2

*janus kinase and microtubule interacting protein 2* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.31× (z +19.5, q 0e+00, up in 18 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.647× (z -4.1, q 0.024, down in 10 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A-172 0.143×, SHP-77 0.262×, LOX-IMVI 0.215×, H4 0.265×); [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-172 0.246×, H4 0.208×, A498 0.213×, SHP-77 0.427×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (H4 0.102×, LOX-IMVI 0.137×, A-172 0.306×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH12]] (+0.64, fdr 1e-05), [[KCNH7]] (+0.63, fdr 1e-05), [[GRIA2]] (+0.62, fdr 1e-05); moves opposite to [[GNG12-AS1]] (-0.49, fdr 5e-05).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[LINC01518]] → it (grade C ⚠); 16 go from it, the strongest it → [[GSTA4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10675.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.31×** | +19.5 | 0e+00 | 18/19 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.96×** | +12.5 | 3e-33 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.75×** | +12.5 | 3e-33 | 3/12 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.82×** | +9.8 | 2e-20 | 17/19 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.96×** | +9.5 | 3e-19 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.69×** | +9.3 | 1e-18 | 16/18 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.65×** | +9.2 | 3e-18 | 16/18 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.41×** | +8.3 | 7e-15 | 17/17 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.21×** | +7.5 | 4e-12 | 17/18 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +6.7 | 1e-09 | 1/15 (NCI-H460) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +5.4 | 4e-06 | 10/19 (A-172, H4, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.84×** | +5.1 | 1e-05 | 14/18 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.54×** | +4.8 | 7e-05 | 9/18 (SW480, HT-29, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.69×** | +4.8 | 8e-05 | 11/17 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.56×** | +4.2 | 9e-04 | 3/17 (H4, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +4.1 | 0.001 | 4/17 (HT-29, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.003 | 0/17 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.016 | 10/17 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10675.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A-172 0.143×, SHP-77 0.262×, LOX-IMVI 0.215×, H4 0.265×); [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-172 0.246×, H4 0.208×, A498 0.213×, SHP-77 0.427×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (H4 0.102×, LOX-IMVI 0.137×, A-172 0.306×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.647×** | -4.1 | 0.024 | 10/17 (H4, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.755×** | -3.7 | 0.057 | 9/19 (SHP-77, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10675. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 87.6 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -20.9) |
| [[LOX-IMVI (line)]] | wt | 25.3 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 2.04 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 23.0× (z +14.3) | — |
| [[A498 (line)]] | wt | 8.94 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 9.99× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -9.3) |
| [[H4 (line)]] | wt | 27.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -10.2) |
| [[SHP-77 (line)]] | alt | 91.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -13.3) |
| [[CHP-212 (line)]] | wt | 28.9 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0491× (z -9.2) |
| [[HT-29 (line)]] | alt | 4.44 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 21.8× (z +11.7) | — |
| [[NCI-H1573 (line)]] | alt | 2.12 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.3× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 4.69 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.62× (z +8.6) | — |
| [[SW480 (line)]] | alt | 7.03 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.21× (z +11.0) | — |
| [[A-427 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.42 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10675), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH12]] | +0.64 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[KCNH7]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[GRIA2]] | +0.62 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[SOGA3]] | +0.62 | +0.29 / +0.68 | both halves | 3e-04 |  |
| [[TMEM108]] | +0.62 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[ATRNL1]] | +0.59 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[LINC01446]] | +0.57 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[MAGEA3-DT]] | +0.57 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[GABRA3]] | +0.57 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[ASXL3]] | +0.56 | +0.20 / +0.65 | ⚠ one half (not replicated) | 7e-04 |  |
| [[VAV3]] | +0.55 | +0.38 / +0.51 | both halves | 7e-05 |  |
| [[CCDC110]] | +0.55 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[KC6]] | +0.55 | +0.43 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNG12-AS1]] | -0.49 | -0.40 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01518]] | C | LINC01518 activity raises JAKMIP2's level | lines that do not express LINC01518 (36) vs lines expressing it (14) | 2.98× lower at baseline in the lines without LINC01518 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000285822, CCDC144NL-AS1, PHF2P2; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises JAKMIP2's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 3.74× lower at baseline in the lines without RUNX1T1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[LRRTM4]] | C | LRRTM4 activity raises JAKMIP2's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 2.44× lower at baseline in the lines without LRRTM4 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973; co-absent with the target |
| [[NLGN4X]] | C | NLGN4X activity raises JAKMIP2's level | lines that do not express NLGN4X (37) vs lines expressing it (13) | 3.21× lower at baseline in the lines without NLGN4X | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[LINC02506]] | C | LINC02506 activity raises JAKMIP2's level | lines that do not express LINC02506 (40) vs lines expressing it (10) | 2.33× lower at baseline in the lines without LINC02506 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC01610, ENSG00000241168; co-absent with the target |
| [[FAM106A]] | C | FAM106A activity raises JAKMIP2's level | lines that do not express FAM106A (30) vs lines expressing it (20) | 2.47× lower at baseline in the lines without FAM106A | 0.061 | ⚠ within organs, on part of the lines; also absent: CCDC144BP, SULF1, POSTN; co-absent with the target |
| [[LINC02899]] | C | LINC02899 activity raises JAKMIP2's level | lines that do not express LINC02899 (40) vs lines expressing it (10) | 2.06× lower at baseline in the lines without LINC02899 | 0.066 | ⚠ within organs, on part of the lines; also absent: LINC02999, MUC6, SIM1; co-absent with the target |
| [[LINC01885]] | C | LINC01885 activity raises JAKMIP2's level | lines that do not express LINC01885 (34) vs lines expressing it (16) | 2.49× lower at baseline in the lines without LINC01885 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287598, ZNF208, LINC00383; co-absent with the target |
| [[PTPRN]] | C | PTPRN activity raises JAKMIP2's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 3.94× lower at baseline in the lines without PTPRN | 0.086 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1; co-absent with the target |
| [[CCDC144NL-AS1]] | C | CCDC144NL-AS1 activity raises JAKMIP2's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 2.78× lower at baseline in the lines without CCDC144NL-AS1 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[CDH10]] | C | CDH10 activity raises JAKMIP2's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 2.81× lower at baseline in the lines without CDH10 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 2, C 14. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GSTA4]] | B | JAKMIP2 activity raises GSTA4's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 1.69× lower at baseline in the lines without JAKMIP2 | 0.046 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent |
| [[ELAPOR2]] | B | JAKMIP2 activity raises ELAPOR2's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 2.37× lower at baseline in the lines without JAKMIP2 | 0.064 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent |
| [[GABRG2]] | C | JAKMIP2 activity raises GABRG2's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 2.87× lower at baseline in the lines without JAKMIP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[CDH10]] | C | JAKMIP2 activity raises CDH10's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 4.21× lower at baseline in the lines without JAKMIP2 | 0.026 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[NLGN4X]] | C | JAKMIP2 activity raises NLGN4X's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 3.06× lower at baseline in the lines without JAKMIP2 | 0.029 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[MAGEA3-DT]] | C | JAKMIP2 activity raises MAGEA3-DT's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 3.54× lower at baseline in the lines without JAKMIP2 | 0.046 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[GABRA3]] | C | JAKMIP2 activity raises GABRA3's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 3.12× lower at baseline in the lines without JAKMIP2 | 0.048 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[LRRTM4]] | C | JAKMIP2 activity raises LRRTM4's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 2.45× lower at baseline in the lines without JAKMIP2 | 0.051 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[ASXL3]] | C | JAKMIP2 activity raises ASXL3's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 2.18× lower at baseline in the lines without JAKMIP2 | 0.056 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[CCDC144NL-AS1]] | C | JAKMIP2 activity raises CCDC144NL-AS1's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 2.65× lower at baseline in the lines without JAKMIP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[NELL2]] | C | JAKMIP2 activity raises NELL2's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 2.25× lower at baseline in the lines without JAKMIP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[SLC6A15]] | C | JAKMIP2 activity raises SLC6A15's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 3.62× lower at baseline in the lines without JAKMIP2 | 0.070 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.615). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.0, 34.4); signed map (34.8, 32.9). **Vector** length 51.0, 12.7% of its response variance represented; |z| ≥ 3 in 527 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +19.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +9.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | -0.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +5.1 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -2.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -2.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | janus kinase and microtubule interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:147,585,438-147,782,775 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JAMIP2, KIAA0555 |
| Matched by | ensembl_id |

UniProt [Q96AA8](https://www.uniprot.org/uniprotkb/Q96AA8) carries no function annotation.

**Summary**, from NCBI Gene [9832](https://www.ncbi.nlm.nih.gov/gene/9832):

> The protein encoded by this gene is reported to be a component of the Golgi matrix. It may act as a golgin protein by negatively regulating transit of secretory cargo and by acting as a structural scaffold of the Golgi. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:29067](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29067) · Entrez [9832](https://www.ncbi.nlm.nih.gov/gene/9832) · UniProt [Q96AA8](https://www.uniprot.org/uniprotkb/Q96AA8) · Ensembl [ENSG00000176049](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176049)

## Data

Gene col 10675: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10675); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10675, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10675]; `tensor/DDL_lfc|DDL_z.npy` [10675]; `embed/gene_vectors.npy` [10675]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10675 or target_col == 10675). Every well: [[JAKMIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JAKMIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
