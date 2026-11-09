---
symbol: "CLRN3"
type: "gene"
col: 11125
ensembl_id: "ENSG00000180745"
name: "clarin 3"
location: "10q26.2"
module: 55
arm: "+"
pooled_cpm: 3.37
n_lines_expressing: 10
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 79
direction_downstream: 89
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# CLRN3

*clarin 3* — 10q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.81× (z +8.6, q 3e-15, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.66× (z +4.1, q 0.006, up in 5 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.383× (z -5.5, q 2e-05, down in 7 of 8 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Rutin (trihydrate) (drug)]] 0.05 µM: 0.504× (z -3.6, q 0.076, down in 0 of 8 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 0.161×, HT-29 0.136×); [[Auranofin (drug)]] 5 µM in 2 lines (LS 180 0.129×, SW480 0.165×); [[Vinblastine (sulfate) (drug)]] 5 µM in 2 lines (HT-29 0.154×, LS 180 0.302×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C9orf152]] (+0.87, fdr 7e-06), [[GJB1]] (+0.84, fdr 7e-06), [[LINC01819]] (+0.83, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 79 arrows point to it, the strongest [[NCALD]] → it (grade B ⚠); 89 go from it, the strongest it → [[NUDT4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11125.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.81×** | +8.6 | 3e-15 | 1/4 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.19×** | +8.2 | 7e-14 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.24×** | +6.2 | 1e-07 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.66×** | +4.1 | 0.006 | 5/8 (COLO 205, HT-29, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.68×** | +4.0 | 0.007 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.55×** | +3.8 | 0.011 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +3.8 | 0.011 | 1/7 (LS 180) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.88×** | +3.6 | 0.022 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.5 | 0.028 | 0/7 | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +3.4 | 0.032 | 1/7 (SW1417) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.11×** | +3.4 | 0.036 | 1/3 (SW1417) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +3.3 | 0.045 | 0/7 | top dose only | cell-cycle shift (explains ~3% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 2.10× | +3.0 | 0.11 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11125.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 0.161×, HT-29 0.136×); [[Auranofin (drug)]] 5 µM in 2 lines (LS 180 0.129×, SW480 0.165×); [[Vinblastine (sulfate) (drug)]] 5 µM in 2 lines (HT-29 0.154×, LS 180 0.302×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.383×** | -5.5 | 2e-05 | 7/8 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.504×** | -3.6 | 0.076 | 0/8 | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM |  | 0.440× | -3.4 | 0.14 | 0/8 | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.587× | -3.1 | 0.31 | 0/8 | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11125. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.8 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0583× (z -23.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0506× (z -17.1) |
| [[LS 180 (line)]] | wt | 37.0 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0879× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.129× (z -12.1) |
| [[COLO 205 (line)]] | alt | 15.1 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0275× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -9.0) |
| [[HT-29 (line)]] | alt | 7.85 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -12.3) |
| [[KATO III (line)]] | alt | 9.18 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -10.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 3.32 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0243× (z -11.2) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 0.396 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.399 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.840 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.978 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.622 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.427 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.458 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.570 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.544 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.355 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.330 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.313 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.422 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.451 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.475 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.816 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.492 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11125), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C9orf152]] | +0.87 | +0.84 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[GJB1]] | +0.84 | +0.79 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[LINC01819]] | +0.83 | +0.86 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[TMEM139]] | +0.82 | +0.78 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[EDAR]] | +0.82 | +0.82 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[KCNE3]] | +0.82 | +0.77 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[BMP4]] | +0.80 | +0.78 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[LINC02058]] | +0.80 | +0.80 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[IL20RA]] | +0.80 | +0.77 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[VWA2]] | +0.78 | +0.78 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[TFF3]] | +0.78 | +0.81 / +0.66 | both halves | 7e-06 |  |
| [[VSNL1]] | +0.77 | +0.74 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*79 arrows, 79 of them with an alert ⚠; grade A 0, B 1, C 78. Shown: the 12 strongest; 67 more arrows (67 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCALD]] | B | NCALD activity raises CLRN3's level | lines that do not express NCALD (18) vs lines expressing it (32) | 1.86× lower at baseline in the lines without NCALD | 0.061 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[TMPRSS2]] | C | TMPRSS2 activity raises CLRN3's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.34× lower at baseline in the lines without TMPRSS2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[GJB1]] | C | GJB1 activity raises CLRN3's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 3.94× lower at baseline in the lines without GJB1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B; co-absent with the target |
| [[NPSR1-AS1]] | C | NPSR1-AS1 activity raises CLRN3's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 3.31× lower at baseline in the lines without NPSR1-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent; co-absent with the target |
| [[GPX2]] | C | GPX2 activity raises CLRN3's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 3.57× lower at baseline in the lines without GPX2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31; co-absent with the target |
| [[TFF3]] | C | TFF3 activity raises CLRN3's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 3.36× lower at baseline in the lines without TFF3 | 0.003 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[INPP5D]] | C | INPP5D activity raises CLRN3's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 3.23× lower at baseline in the lines without INPP5D | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5; co-absent with the target |
| [[FGD5]] | C | FGD5 activity raises CLRN3's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 2.52× lower at baseline in the lines without FGD5 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5; co-absent with the target |
| [[ARHGEF38]] | C | ARHGEF38 activity raises CLRN3's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 3.58× lower at baseline in the lines without ARHGEF38 | 0.004 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1; co-absent with the target |
| [[LINC01819]] | C | LINC01819 activity raises CLRN3's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 2.48× lower at baseline in the lines without LINC01819 | 0.004 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent; co-absent with the target |
| [[A1CF]] | C | A1CF activity raises CLRN3's level | lines that do not express A1CF (35) vs lines expressing it (15) | 2.96× lower at baseline in the lines without A1CF | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VIL1, NPSR1-AS1, MUC13; co-absent with the target |
| [[UGT1A8]] | C | UGT1A8 activity raises CLRN3's level | lines that do not express UGT1A8 (33) vs lines expressing it (17) | 2.48× lower at baseline in the lines without UGT1A8 | 0.005 | ⚠ within organs, on part of the lines; co-absent genes; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target |

### Downstream of this gene

*89 arrows, 89 of them with an alert ⚠; grade A 0, B 14, C 75. Shown: the 12 strongest; 77 more arrows (77 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUDT4]] | B | CLRN3 activity raises NUDT4's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 2.77× lower at baseline in the lines without CLRN3 | 1e-03 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13 |
| [[RSPH1]] | B | CLRN3 activity raises RSPH1's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 2.97× lower at baseline in the lines without CLRN3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13 |
| [[MROH7]] | B | CLRN3 activity raises MROH7's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 3.24× lower at baseline in the lines without CLRN3 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13 |
| [[PLS1]] | B | CLRN3 activity raises PLS1's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 4.76× lower at baseline in the lines without CLRN3 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13 |
| [[ACOT11]] | B | CLRN3 activity raises ACOT11's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 3.49× lower at baseline in the lines without CLRN3 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13 |
| [[ZNF503-AS1]] | B | CLRN3 activity raises ZNF503-AS1's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 3.57× lower at baseline in the lines without CLRN3 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13 |
| [[ABHD12B]] | B | CLRN3 activity raises ABHD12B's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 2.83× lower at baseline in the lines without CLRN3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13 |
| [[SNTB1]] | B | CLRN3 activity raises SNTB1's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 4.66× lower at baseline in the lines without CLRN3 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13 |
| [[DNAJC15]] | B | CLRN3 activity raises DNAJC15's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 3.40× lower at baseline in the lines without CLRN3 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13 |
| [[PIK3C2B]] | B | CLRN3 activity raises PIK3C2B's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 2.57× lower at baseline in the lines without CLRN3 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13 |
| [[NCALD]] | B | CLRN3 activity raises NCALD's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 3.66× lower at baseline in the lines without CLRN3 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13 |
| [[PLS1]] | B | CLRN3 activity weakens PLS1's drug response | lines that do not express CLRN3 (26) vs lines expressing it (9) | the lines without CLRN3 respond 8.47× as strongly (z diff -5.22); strongest at Panobinostat 5 µM: 2.82x vs 0.92x (z diff -9.0) | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.854). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.7, 46.7); signed map (62.8, 12.6). **Vector** length 53.0, 28.8% of its response variance represented; |z| ≥ 3 in 229 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.1 | +0.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.1 | +0.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -5.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -0.7 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.8 | -2.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.7 | -2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | clarin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.2 — chr10:127,877,841-127,892,941 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC32871, USH3AL1; previously TMEM12 |
| Gene groups (HGNC) | Clarins |
| Matched by | ensembl_id |

UniProt [Q8NCR9](https://www.uniprot.org/uniprotkb/Q8NCR9) carries no function annotation.

**Summary**, from NCBI Gene [119467](https://www.ncbi.nlm.nih.gov/gene/119467):

> Predicted to be involved in sensory perception of sound. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20795](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20795) · Entrez [119467](https://www.ncbi.nlm.nih.gov/gene/119467) · UniProt [Q8NCR9](https://www.uniprot.org/uniprotkb/Q8NCR9) · Ensembl [ENSG00000180745](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180745)

## Data

Gene col 11125: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11125); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11125, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11125]; `tensor/DDL_lfc|DDL_z.npy` [11125]; `embed/gene_vectors.npy` [11125]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11125 or target_col == 11125). Every well: [[CLRN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLRN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
