---
symbol: "REC8"
type: "gene"
col: 2044
ensembl_id: "ENSG00000100918"
name: "REC8 meiotic recombination protein"
location: "14q12"
module: 32
arm: "+"
pooled_cpm: 9.45
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 31
n_dd_up_clean: 0
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 45
direction_downstream: 25
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# REC8

*REC8 meiotic recombination protein* — 14q12

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (9 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.414× (z -7.9, q 1e-12, down in 31 of 45 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Tofacitinib (drug)]] 5 µM: 0.540× (z -7.8, q 1e-12, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IRF9]] (+0.78, fdr 7e-06, ⚠ same locus), [[OAS3]] (+0.72, fdr 7e-06), [[PLSCR1]] (+0.70, fdr 7e-06), [[FBXO39]] (+0.70, fdr 1e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 45 arrows point to it, the strongest [[IFI6]] → it (grade B ⚠); 25 go from it, the strongest it → [[IRF9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2044.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.7 | 0.14 | 3/48 (NCI-H23, SW1417, …) | inconsistent across doses |  |
| [[Hydroxyurea (drug)]] 5 µM |  | 1.42× | +3.0 | 0.73 | 7/44 (NCI-H2030, PANC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2044.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.414×** | -7.9 | 1e-12 | 31/45 (A-172, NCI-H2347, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.403×** | -7.8 | 1e-12 | 28/40 (LoVo, RKO, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.540×** | -7.8 | 1e-12 | 32/45 (LoVo, RKO, …) | rises with dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.581×** | -6.9 | 9e-10 | 30/46 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.508×** | -6.0 | 2e-07 | 27/45 (RKO, LoVo, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.516×** | -5.9 | 3e-07 | 30/44 (NCI-H23, RKO, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.518×** | -5.9 | 3e-07 | 26/46 (NCI-H1573, LoVo, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.558×** | -5.2 | 1e-05 | 24/43 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.546×** | -5.2 | 1e-05 | 23/40 (COLO 205, SNU-423, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.559×** | -5.2 | 1e-05 | 27/46 (RKO, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.562×** | -5.2 | 1e-05 | 27/47 (BT-474, RKO, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.668×** | -5.1 | 2e-05 | 26/46 (NCI-H1792, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.698×** | -4.5 | 3e-04 | 24/47 (NCI-H1792, SK-MEL-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.607×** | -4.3 | 7e-04 | 19/36 (C-33 A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.639×** | -4.0 | 0.002 | 19/44 (RKO, BT-474, …) | rises with dose |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.628×** | -3.9 | 0.003 | 18/44 (C32, BT-474, …) | inconsistent across doses | position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.663×** | -3.7 | 0.008 | 23/44 (C-33 A, BT-474, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.765×** | -3.4 | 0.019 | 17/45 (H4, KATO III, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.486×** | -3.4 | 0.019 | 15/46 (LoVo, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.684×** | -3.4 | 0.019 | 15/45 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2044. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 17.1 | 0 | 5 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.210× (z -12.9) |
| [[RKO (line)]] | wt | 11.8 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0890× (z -9.6) ⚠ toxic · without an alert: [[Tofacitinib (drug)]] 5 µM 0.203× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0704× (z -12.9) |
| [[SNU-423 (line)]] | alt | 11.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0766× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.114× (z -9.4) |
| [[A-172 (line)]] | wt | 6.86 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0780× (z -11.9) |
| [[BT-474 (line)]] | alt | 23.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0337× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.252× (z -9.0) |
| [[C-33 A (line)]] | alt | 14.3 | 0 | 2 | — | [[Tofacitinib (drug)]] 0.5 µM 0.111× (z -8.9) |
| [[C32 (line)]] | wt | 7.88 | 0 | 2 | — | [[TAK-901 (drug)]] 0.05 µM 0.0346× (z -11.8) |
| [[SW 900 (line)]] | alt | 8.90 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -12.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.0481× (z -11.8) |
| [[A549 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.129× (z -9.2) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 5.63 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0825× (z -8.8) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 17.1 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 5 µM 0.279× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -8.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H1792 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 5.89 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.100× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.209× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H460 (line)]] | wt | 2.78 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0737× (z -9.8) |
| [[A-427 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2044), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRF9]] | +0.78 | +0.79 / +0.80 | both halves | 7e-06 | ⚠ same locus (3.8 kb, same strand: neighbours can correlate without regulation) |
| [[OAS3]] | +0.72 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[PLSCR1]] | +0.70 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[FBXO39]] | +0.70 | +0.55 / +0.77 | both halves | 1e-05 |  |
| [[MX1]] | +0.69 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[PARP10]] | +0.69 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[OAS2]] | +0.67 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[CMPK2]] | +0.67 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[STAT1]] | +0.67 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[HERC6]] | +0.66 | +0.51 / +0.74 | both halves | 1e-05 |  |
| [[PLEKHA4]] | +0.66 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[PNPT1]] | +0.65 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[USP18]] | +0.65 | +0.53 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 34, C 11. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI6]] | B | IFI6 activity raises REC8's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.43× lower at baseline in the lines without IFI6 | 3e-04 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[SRMS]] | B | SRMS activity raises REC8's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.01× lower at baseline in the lines without SRMS | 1e-03 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[BATF2]] | B | BATF2 activity raises REC8's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without BATF2 | 0.002 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[OAS2]] | B | OAS2 activity raises REC8's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.01× lower at baseline in the lines without OAS2 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[FBXO39]] | B | FBXO39 activity raises REC8's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 1.77× lower at baseline in the lines without FBXO39 | 0.003 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[OAS1]] | B | OAS1 activity raises REC8's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.05× lower at baseline in the lines without OAS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[PARP9]] | B | PARP9 activity raises REC8's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.24× lower at baseline in the lines without PARP9 | 0.008 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[IFI27]] | B | IFI27 activity raises REC8's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 1.71× lower at baseline in the lines without IFI27 | 0.009 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[SLC15A3]] | B | SLC15A3 activity raises REC8's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 1.64× lower at baseline in the lines without SLC15A3 | 0.011 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[MX1]] | B | MX1 activity raises REC8's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.81× lower at baseline in the lines without MX1 | 0.012 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[SAMD9]] | B | SAMD9 activity raises REC8's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 1.73× lower at baseline in the lines without SAMD9 | 0.021 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[RSAD2]] | B | RSAD2 activity raises REC8's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.64× lower at baseline in the lines without RSAD2 | 0.022 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 0, C 25. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRF9]] | C | REC8's natural level strengthens IRF9's drug response | REC8's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.85, reverse +0.73; direction not clear | 8e-06 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HELZ2]] | C | REC8's natural level strengthens HELZ2's drug response | REC8's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.65; direction not clear | 6e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SAMHD1]] | C | REC8's natural level strengthens SAMHD1's drug response | REC8's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.79, reverse +0.47; direction not clear | 9e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ADAR]] | C | REC8's natural level strengthens ADAR's drug response | REC8's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.75; direction not clear | 0.002 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SHISA5]] | C | REC8's natural level strengthens SHISA5's drug response | REC8's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.36; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP12]] | C | REC8's natural level strengthens PARP12's drug response | REC8's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.69; direction not clear | 0.005 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP10]] | C | REC8's natural level strengthens PARP10's drug response | REC8's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.43; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRIM25]] | C | REC8's natural level strengthens TRIM25's drug response | REC8's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.65; direction not clear | 0.008 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[USP18]] | C | REC8's natural level strengthens USP18's drug response | REC8's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.55; direction not clear | 0.009 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TMEM140]] | C | REC8's natural level strengthens TMEM140's drug response | REC8's natural level across 40 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.33; direction not clear | 0.009 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[IFIT1]] | C | REC8's natural level strengthens IFIT1's drug response | REC8's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.26; direction not clear | 0.013 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SP100]] | C | REC8's natural level strengthens SP100's drug response | REC8's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.62; direction not clear | 0.014 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.665). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.1, 55.2); signed map (66.0, 32.7). **Vector** length 84.0, 16.9% of its response variance represented; |z| ≥ 3 in 1,066 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.55 to 56); *interferon gamma response* (hallmark, mean cos +0.56 to 60); *interferon* (control, mean cos +0.61 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.8 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | -1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +1.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.5 | +0.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +2.5 | -2.8 |
|  | [[Cinacalcet (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.7 | +1.9 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.7 | +0.6 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +1.5 | +1.0 |
|  | [[Saquinavir (drug)]] 0.5 µM |  | +1.4 | +0.5 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -4.2 | -7.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.7 | -6.9 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.4 | -4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.4 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | REC8 meiotic recombination protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,171,853-24,180,257 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Rec8p, kleisin-alpha; previously REC8L1 |
| Gene groups (HGNC) | Cohesin complex; Kleisins |
| Reactome | 4 pathways, smallest: Meiotic synapsis; Meiosis; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [O95072](https://www.uniprot.org/uniprotkb/O95072) (Meiotic recombination protein REC8 homolog):

> Required during meiosis for separation of sister chromatids and homologous chromosomes. Proteolytic cleavage of REC8 on chromosome arms by separin during anaphase I allows for homologous chromosome separation in meiosis I and cleavage of REC8 on centromeres during anaphase II allows for sister chromatid separation in meiosis II (By similarity).

**Summary**, from NCBI Gene [9985](https://www.ncbi.nlm.nih.gov/gene/9985):

> This gene encodes a member of the kleisin family of SMC (structural maintenance of chromosome) protein partners. The protein localizes to the axial elements of chromosomes during meiosis in both oocytes and spermatocytes. In the mouse, the homologous protein is a key component of the meiotic cohesion complex, which regulates sister chromatid cohesion and recombination between homologous chromosomes. Multiple alternatively spliced variants, encoding the same protein, have been found for this …

**Accessions** — [HGNC:16879](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16879) · Entrez [9985](https://www.ncbi.nlm.nih.gov/gene/9985) · UniProt [O95072](https://www.uniprot.org/uniprotkb/O95072) · Ensembl [ENSG00000100918](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100918)

## Data

Gene col 2044: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2044); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2044, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2044]; `tensor/DDL_lfc|DDL_z.npy` [2044]; `embed/gene_vectors.npy` [2044]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2044 or target_col == 2044). Every well: [[REC8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/REC8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
