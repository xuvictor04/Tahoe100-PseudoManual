---
symbol: "IGFL2-AS1"
type: "gene"
col: 15604
ensembl_id: "ENSG00000268621"
name: "IGFL2 antisense RNA 1"
location: "19q13.32"
module: 8
arm: "+"
pooled_cpm: 30.89
n_lines_expressing: 14
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 52
direction_downstream: 77
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# IGFL2-AS1

*IGFL2 antisense RNA 1* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.64× (z +8.3, q 3e-14, up in 3 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Osimertinib (mesylate) (drug)]] 5 µM: 2.13× (z +5.0, q 9e-05, up in 11 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.541× (z -4.1, q 0.025, down in 11 of 12 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (COLO 205 0.0277×, HT-29 0.0597×, Hs 766T 0.110×, SW1417 0.219×, …; ⚠ cell-cycle shift, explains ~30% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (COLO 205 0.118×, LoVo 0.161×; ⚠ cell-cycle shift, explains ~30% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LoVo 0.163×, SW480 0.161×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW1417 0.178×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01559]] (+0.68, fdr 7e-06), [[CLIC5]] (+0.68, fdr 1e-05), [[BCL2L15]] (+0.67, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 52 arrows point to it, the strongest [[FUT2]] → it (grade B ⚠); 77 go from it, the strongest it → [[ELF3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15604.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.64×** | +8.3 | 3e-14 | 3/9 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.46×** | +8.3 | 3e-14 | 5/12 (A498, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **2.13×** | +5.0 | 9e-05 | 11/12 (LS 180, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.21×** | +4.9 | 1e-04 | 2/10 (A498, A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +4.8 | 2e-04 | 5/12 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.81×** | +4.0 | 0.007 | 8/12 (COLO 205, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.039 | 7/12 (AsPC-1, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.67×** | +3.4 | 0.043 | 5/12 (A498, HT-29, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.67×** | +3.3 | 0.057 | 9/12 (A-172, COLO 205, …) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.2 | 0.069 | 3/12 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.070 | 3/12 (Hs 766T, COLO 205, …) | rises with dose |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.1 | 0.079 | 5/12 (Hs 766T, COLO 205, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.63×** | +3.1 | 0.079 | 4/12 (HEC-1-A, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +3.1 | 0.079 | 4/12 (Hs 766T, COLO 205, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.088 | 7/12 (LS 180, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15604.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (COLO 205 0.0277×, HT-29 0.0597×, Hs 766T 0.110×, SW1417 0.219×, …; ⚠ cell-cycle shift, explains ~30% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (COLO 205 0.118×, LoVo 0.161×; ⚠ cell-cycle shift, explains ~30% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LoVo 0.163×, SW480 0.161×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW1417 0.178×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.541×** | -4.1 | 0.025 | 11/12 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.606× | -3.1 | 0.37 | 0/12 | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.607× | -3.1 | 0.37 | 1/12 (Panc 03.27) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15604. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 42.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -12.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -9.2) |
| [[COLO 205 (line)]] | alt | 485 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0277× (z -25.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW1417 (line)]] | alt | 363 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -13.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.178× (z -10.6) |
| [[SW480 (line)]] | alt | 157 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -11.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -8.9) |
| [[Hs 766T (line)]] | wt | 54.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -16.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HT-29 (line)]] | alt | 74.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0597× (z -16.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0923× (z -12.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.14 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.67 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.49 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.00 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.66 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.56 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.29 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.02 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.44 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.83 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.26 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.73 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15604), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01559]] | +0.68 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[CLIC5]] | +0.68 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[BCL2L15]] | +0.67 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[ABO]] | +0.66 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[MUC13]] | +0.66 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[GCNT3]] | +0.65 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[PRR15]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[POF1B]] | +0.64 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[CYP4F3]] | +0.63 | +0.58 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[PTPN22]] | +0.63 | +0.57 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[LINC02331]] | +0.63 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[ALOX5]] | +0.63 | +0.64 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 3, C 49. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FUT2]] | B | FUT2 activity raises IGFL2-AS1's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 2.47× lower at baseline in the lines without FUT2 | 0.055 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises IGFL2-AS1's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.29× lower at baseline in the lines without SLC44A3-AS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises IGFL2-AS1's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.67× lower at baseline in the lines without ELF3-AS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[LINC01819]] | C | LINC01819 activity raises IGFL2-AS1's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 4.18× lower at baseline in the lines without LINC01819 | 0.001 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent; co-absent with the target |
| [[LINC01559]] | C | LINC01559 activity raises IGFL2-AS1's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 7.49× lower at baseline in the lines without LINC01559 | 0.002 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17; co-absent with the target |
| [[MYO7B]] | C | MYO7B activity raises IGFL2-AS1's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 5.63× lower at baseline in the lines without MYO7B | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises IGFL2-AS1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 4.84× lower at baseline in the lines without TMPRSS2 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[PRR15]] | C | PRR15 activity raises IGFL2-AS1's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 3.80× lower at baseline in the lines without PRR15 | 0.010 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C; co-absent with the target |
| [[NPSR1-AS1]] | C | NPSR1-AS1 activity raises IGFL2-AS1's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 4.61× lower at baseline in the lines without NPSR1-AS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent; co-absent with the target |
| [[CYP4F12]] | C | CYP4F12 activity raises IGFL2-AS1's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 3.89× lower at baseline in the lines without CYP4F12 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13; co-absent with the target |
| [[PRKCH-AS1]] | C | PRKCH-AS1 activity raises IGFL2-AS1's level | lines that do not express PRKCH-AS1 (34) vs lines expressing it (16) | 4.93× lower at baseline in the lines without PRKCH-AS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent; co-absent with the target |
| [[C6orf132]] | C | C6orf132 activity raises IGFL2-AS1's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 3.89× lower at baseline in the lines without C6orf132 | 0.011 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1; co-absent with the target |

### Downstream of this gene

*77 arrows, 77 of them with an alert ⚠; grade A 0, B 16, C 61. Shown: the 12 strongest; 65 more arrows (65 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3-AS1]] | B | IGFL2-AS1 activity raises ELF3-AS1's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 2.97× lower at baseline in the lines without IGFL2-AS1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559 |
| [[LINC02580]] | B | IGFL2-AS1 activity raises LINC02580's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 1.90× lower at baseline in the lines without IGFL2-AS1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559 |
| [[FUT2]] | B | IGFL2-AS1 activity raises FUT2's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 2.12× lower at baseline in the lines without IGFL2-AS1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559 |
| [[MGST2]] | B | IGFL2-AS1 activity raises MGST2's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 2.61× lower at baseline in the lines without IGFL2-AS1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559 |
| [[PLAAT3]] | B | IGFL2-AS1 activity raises PLAAT3's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 2.35× lower at baseline in the lines without IGFL2-AS1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559 |
| [[C4orf19]] | B | IGFL2-AS1 activity raises C4orf19's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 2.46× lower at baseline in the lines without IGFL2-AS1 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559 |
| [[PLA2R1]] | B | IGFL2-AS1 activity raises PLA2R1's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 3.38× lower at baseline in the lines without IGFL2-AS1 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559 |
| [[TRIM2]] | B | IGFL2-AS1 activity raises TRIM2's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 2.73× lower at baseline in the lines without IGFL2-AS1 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559 |
| [[SLC44A3-AS1]] | B | IGFL2-AS1 activity raises SLC44A3-AS1's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 2.37× lower at baseline in the lines without IGFL2-AS1 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559 |
| [[HDHD3]] | B | IGFL2-AS1 activity raises HDHD3's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 1.80× lower at baseline in the lines without IGFL2-AS1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559 |
| [[MUC20]] | B | IGFL2-AS1 activity raises MUC20's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 2.95× lower at baseline in the lines without IGFL2-AS1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559 |
| [[SLC44A3]] | B | IGFL2-AS1 activity raises SLC44A3's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 2.35× lower at baseline in the lines without IGFL2-AS1 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.9, 52.7); signed map (61.3, 4.4). **Vector** length 50.9, 19.2% of its response variance represented; |z| ≥ 3 in 323 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +8.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +2.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.1 | -4.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -2.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.9 | -2.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -3.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | IGFL2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.32 — chr19:46,189,029-46,203,160 (-) |
| Ensembl biotype | lncRNA |
| Also known as | AC006262.5 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52559](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52559) · Entrez [645553](https://www.ncbi.nlm.nih.gov/gene/645553) · Ensembl [ENSG00000268621](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000268621)

## Data

Gene col 15604: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15604); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15604, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15604]; `tensor/DDL_lfc|DDL_z.npy` [15604]; `embed/gene_vectors.npy` [15604]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15604 or target_col == 15604). Every well: [[IGFL2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGFL2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
