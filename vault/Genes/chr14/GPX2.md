---
symbol: "GPX2"
type: "gene"
col: 10688
ensembl_id: "ENSG00000176153"
name: "glutathione peroxidase 2"
location: "14q23.3"
module: 55
arm: "+"
pooled_cpm: 14.71
n_lines_expressing: 14
n_dd_up: 5
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 128
direction_downstream: 141
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# GPX2

*glutathione peroxidase 2* — 14q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.09× (z +11.5, q 5e-28, up in 5 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pimozide (drug)]] 0.05 µM: 1.67× (z +4.2, q 0.003, up in 2 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.485× (z -5.9, q 2e-06, down in 11 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01819]] (+0.86, fdr 7e-06), [[C9orf152]] (+0.85, fdr 7e-06), [[TPRXL]] (+0.81, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 128 arrows point to it, the strongest [[EPS8L1]] → it (grade B ⚠); 141 go from it, the strongest it → [[PLS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10688.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.09×** | +11.5 | 5e-28 | 5/12 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.25×** | +11.4 | 1e-27 | 3/8 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.66×** | +7.4 | 2e-11 | 5/10 (A549, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.84×** | +5.0 | 1e-04 | 6/12 (SW480, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.67×** | +4.2 | 0.003 | 2/12 (SW480, HepG2/C3A) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | 1.50× | +3.2 | 0.13 | 3/12 (NCI-H1573, HepG2/C3A, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.49× | +3.1 | 0.15 | 4/12 (NCI-H1573, A549, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10688.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.485×** | -5.9 | 2e-06 | 11/12 (LS 180, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.489×** | -5.7 | 4e-06 | 10/12 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.516×** | -5.4 | 1e-05 | 11/12 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.617×** | -3.9 | 0.016 | 7/12 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.371×** | -3.7 | 0.022 | 8/12 (HT-29, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.646×** | -3.6 | 0.030 | 6/12 (HT-29, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.657×** | -3.5 | 0.043 | 11/12 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.666×** | -3.2 | 0.082 | 11/12 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.689× | -3.1 | 0.13 | 10/12 (LS 180, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.669× | -3.1 | 0.13 | 4/12 (LoVo, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10688. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 122 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0788× (z -19.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0400× (z -16.6) |
| [[LoVo (line)]] | wt | 49.7 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0225× (z -28.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0333× (z -17.8) |
| [[KATO III (line)]] | alt | 198 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0502× (z -25.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0359× (z -19.9) |
| [[HT-29 (line)]] | alt | 110 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0263× (z -32.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.134× (z -12.6) |
| [[SW480 (line)]] | alt | 19.0 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0608× (z -23.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0283× (z -21.2) |
| [[LS 180 (line)]] | wt | 46.8 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0378× (z -21.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0366× (z -15.6) |
| [[CFPAC-1 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.83 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10688), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01819]] | +0.86 | +0.85 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[C9orf152]] | +0.85 | +0.82 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[TPRXL]] | +0.81 | +0.84 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[LGALS4]] | +0.80 | +0.77 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[NPSR1]] | +0.80 | +0.77 / +0.79 | both halves | 7e-06 |  |
| [[LINC01559]] | +0.80 | +0.87 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[BMP4]] | +0.79 | +0.78 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[ST6GALNAC1]] | +0.79 | +0.77 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[EDAR]] | +0.79 | +0.79 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[HNF4A]] | +0.78 | +0.82 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[MUC5B]] | +0.78 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[LINC02331]] | +0.77 | +0.79 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*128 arrows, 128 of them with an alert ⚠; grade A 0, B 3, C 125. Shown: the 12 strongest; 116 more arrows (116 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | EPS8L1 activity raises GPX2's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.52× lower at baseline in the lines without EPS8L1 | 0.073 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[LDLRAD4]] | B | LDLRAD4 activity raises GPX2's level | lines that do not express LDLRAD4 (23) vs lines expressing it (27) | 1.62× lower at baseline in the lines without LDLRAD4 | 0.093 | ⚠ within organs, on part of the lines; also absent: TTTY14, NLGN4X, ENSG00000260958 |
| [[HDAC6]] | B | HDAC6 activity raises GPX2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOX3]] | C | TOX3 activity raises GPX2's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 5.90× lower at baseline in the lines without TOX3 | 2e-04 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises GPX2's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 9.52× lower at baseline in the lines without GCNT3 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[CEACAM1]] | C | CEACAM1 activity raises GPX2's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 4.37× lower at baseline in the lines without CEACAM1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises GPX2's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 7.72× lower at baseline in the lines without CEACAM5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[ARHGEF38]] | C | ARHGEF38 activity raises GPX2's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 6.61× lower at baseline in the lines without ARHGEF38 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1; co-absent with the target |
| [[TMEM45B]] | C | TMEM45B activity raises GPX2's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 6.00× lower at baseline in the lines without TMEM45B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881; co-absent with the target |
| [[LINC03040]] | C | LINC03040 activity raises GPX2's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 4.89× lower at baseline in the lines without LINC03040 | 0.002 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2; co-absent with the target |
| [[CLRN3]] | C | CLRN3 activity raises GPX2's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 10.61× lower at baseline in the lines without CLRN3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |
| [[FAM3D]] | C | FAM3D activity raises GPX2's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 9.86× lower at baseline in the lines without FAM3D | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*141 arrows, 141 of them with an alert ⚠; grade A 0, B 23, C 118. Shown: the 12 strongest; 129 more arrows (129 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLS1]] | B | GPX2 activity raises PLS1's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 4.21× lower at baseline in the lines without GPX2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31 |
| [[BCAR3-AS1]] | B | GPX2 activity raises BCAR3-AS1's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 2.18× lower at baseline in the lines without GPX2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31 |
| [[TNFRSF21]] | B | GPX2 activity raises TNFRSF21's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 4.42× lower at baseline in the lines without GPX2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31 |
| [[ZNF503-AS1]] | B | GPX2 activity raises ZNF503-AS1's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 3.00× lower at baseline in the lines without GPX2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31 |
| [[SLC12A2]] | B | GPX2 activity raises SLC12A2's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 2.65× lower at baseline in the lines without GPX2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31 |
| [[LINC00511]] | B | GPX2 activity raises LINC00511's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 3.45× lower at baseline in the lines without GPX2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31 |
| [[SEMA4G]] | B | GPX2 activity raises SEMA4G's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 2.48× lower at baseline in the lines without GPX2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31 |
| [[SNTB1]] | B | GPX2 activity raises SNTB1's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 4.19× lower at baseline in the lines without GPX2 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31 |
| [[EPS8L1]] | B | GPX2 activity raises EPS8L1's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 3.15× lower at baseline in the lines without GPX2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31 |
| [[PLS1]] | B | GPX2 activity weakens PLS1's drug response | lines that do not express GPX2 (22) vs lines expressing it (13) | the lines without GPX2 respond 3.03× as strongly (z diff -4.25); strongest at Panobinostat 5 µM: 2.99x vs 1.20x (z diff -7.0) | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31; target measured in part of the lines; the reference differs; artifact flags |
| [[MROH7]] | B | GPX2 activity raises MROH7's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 2.26× lower at baseline in the lines without GPX2 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31 |
| [[FKBP9P1]] | B | GPX2 activity raises FKBP9P1's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 1.55× lower at baseline in the lines without GPX2 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.893). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.4, 49.5); signed map (63.6, 9.1). **Vector** length 68.4, 33.9% of its response variance represented; |z| ≥ 3 in 311 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.1 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -3.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -2.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | glutathione peroxidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.3 — chr14:64,939,152-64,942,746 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GSHPX-GI |
| Gene groups (HGNC) | Selenoproteins; Glutathione peroxidase family |
| Hallmark sets | P53_PATHWAY |
| Reactome | 12 pathways, smallest: Synthesis of 12-eicosatetraenoic acid derivatives; Synthesis of 15-eicosatetraenoic acid derivatives; Synthesis of 5-eicosatetraenoic acids |
| Matched by | ensembl_id |

**Function**, from UniProt [P18283](https://www.uniprot.org/uniprotkb/P18283) (Glutathione peroxidase 2):

> Catalyzes the reduction of hydroperoxides in a glutathione-dependent manner thus regulating cellular redox homeostasis. Can reduce small soluble hydroperoxides such as H2O2, cumene hydroperoxide and tert-butyl hydroperoxide, as well as several fatty acid-derived hydroperoxides. Cannot reduce phosphatidycholine hydroperoxide.

**Summary**, from NCBI Gene [2877](https://www.ncbi.nlm.nih.gov/gene/2877):

> The protein encoded by this gene belongs to the glutathione peroxidase family, members of which catalyze the reduction of organic hydroperoxides and hydrogen peroxide (H2O2) by glutathione, and thereby protect cells against oxidative damage. Several isozymes of this gene family exist in vertebrates, which vary in cellular location and substrate specificity. This isozyme is predominantly expressed in the gastrointestinal tract (also in liver in human), is localized in the cytoplasm, and whose …

**Accessions** — [HGNC:4554](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4554) · Entrez [2877](https://www.ncbi.nlm.nih.gov/gene/2877) · UniProt [P18283](https://www.uniprot.org/uniprotkb/P18283) · Ensembl [ENSG00000176153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176153)

## Data

Gene col 10688: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10688); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10688, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10688]; `tensor/DDL_lfc|DDL_z.npy` [10688]; `embed/gene_vectors.npy` [10688]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10688 or target_col == 10688). Every well: [[GPX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
