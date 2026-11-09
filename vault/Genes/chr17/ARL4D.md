---
symbol: "ARL4D"
type: "gene"
col: 10664
ensembl_id: "ENSG00000175906"
name: "ARF like GTPase 4D"
location: "17q21.31"
module: 79
arm: "+"
pooled_cpm: 7.25
n_lines_expressing: 45
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# ARL4D

*ARF like GTPase 4D* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.69× (z +15.0, q 0e+00, up in 38 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.688× (z -4.4, q 0.007, down in 12 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (Hs 766T 0.153×, SW1417 0.272×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.127×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.05 µM in 1 line (PANC-1 0.0441×); [[Hesperidin (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0627×); [[Fusidic acid (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0505×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NGFR]] (+0.67, fdr 7e-06), [[RYBP]] (+0.64, fdr 3e-05), [[PPP1R3C]] (+0.62, fdr 1e-05); moves opposite to [[ARIH2]] (-0.57, fdr 1e-05), [[NAF1]] (-0.57, fdr 3e-05), [[TIMM23B-AGAP6]] (-0.57, fdr 3e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GNG2]] → it (grade B ⚠); 4 go from it, the strongest it → [[PRDM10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10664.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.69×** | +15.0 | 0e+00 | 38/42 (A549, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.47×** | +14.7 | 0e+00 | 26/35 (SW1417, HS-578T, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.06×** | +12.9 | 7e-36 | 35/41 (A549, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.11×** | +12.1 | 9e-32 | 36/42 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.83×** | +12.0 | 3e-31 | 36/41 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.46×** | +10.0 | 2e-21 | 21/37 (SW1417, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.79×** | +9.5 | 3e-19 | 25/43 (A-172, HOP62, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.96×** | +7.7 | 9e-13 | 26/39 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.89×** | +7.3 | 1e-11 | 24/41 (A549, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +6.6 | 2e-09 | 20/40 (SW1417, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.73×** | +6.3 | 2e-08 | 24/43 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +6.3 | 2e-08 | 15/35 (SW1417, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.67×** | +5.9 | 2e-07 | 17/41 (A498, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +5.8 | 2e-07 | 9/23 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +4.6 | 1e-04 | 10/37 (A-427, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.48×** | +4.5 | 2e-04 | 15/39 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10664.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (Hs 766T 0.153×, SW1417 0.272×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.127×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.05 µM in 1 line (PANC-1 0.0441×); [[Hesperidin (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0627×); [[Fusidic acid (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0505×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.688×** | -4.4 | 0.007 | 12/41 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Demeclocycline (drug)]] 5 µM |  | **0.805×** | -3.6 | 0.085 | 8/42 (LOX-IMVI, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10664. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 24.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 5.07 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +9.0) ⚠ cell-cycle shift, explains ~51% of this change | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.115× (z -8.7) ⚠ toxic |
| [[A-172 (line)]] | wt | 7.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +9.8) | — |
| [[A498 (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 8.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 6.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 9.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 7.39 | 0 | 1 | — | [[Hesperidin (drug)]] 0.5 µM 0.0627× (z -9.2) |
| [[PANC-1 (line)]] | alt | 1.94 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0441× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 3.66 | 0 | 1 | — | [[Fusidic acid (drug)]] 0.05 µM 0.0505× (z -8.7) |
| [[SW480 (line)]] | alt | 6.96 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -9.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.665 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.840 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10664), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NGFR]] | +0.67 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[RYBP]] | +0.64 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[PPP1R3C]] | +0.62 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[AVPI1]] | +0.61 | +0.39 / +0.62 | both halves | 6e-05 |  |
| [[PELO]] | +0.59 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[CAPN5]] | +0.59 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[ADM]] | +0.58 | +0.31 / +0.62 | both halves | 2e-04 |  |
| [[BIK]] | +0.58 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[MT1F]] | +0.57 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ABCG1]] | +0.57 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[SH3TC1]] | +0.56 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[ID1]] | +0.56 | +0.32 / +0.54 | both halves | 1e-04 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARIH2]] | -0.57 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[NAF1]] | -0.57 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[TIMM23B-AGAP6]] | -0.57 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[NDUFA10]] | -0.55 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[CASTOR3P-1]] | -0.54 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[NUDT3]] | -0.53 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ATR]] | -0.53 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[EIF3F]] | -0.52 | -0.19 / -0.51 | ⚠ one half (not replicated) | 8e-04 |  |
| [[MSANTD2]] | -0.52 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[PSMD6-AS1]] | -0.52 | -0.15 / -0.60 | ⚠ one half (not replicated) | 0.001 |  |
| [[MSL3]] | -0.51 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[KCTD13]] | -0.51 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[PAK2]] | -0.51 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[HCFC1]] | -0.51 | -0.31 / -0.55 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNG2]] | B | GNG2 activity raises ARL4D's level | lines that do not express GNG2 (22) vs lines expressing it (28) | 2.07× lower at baseline in the lines without GNG2 | 0.005 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT |
| [[NEDD9]] | B | NEDD9 activity raises ARL4D's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 2.10× lower at baseline in the lines without NEDD9 | 0.010 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[STK32A]] | B | STK32A activity raises ARL4D's level | lines that do not express STK32A (23) vs lines expressing it (27) | 1.92× lower at baseline in the lines without STK32A | 0.043 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1 |
| [[NGFR]] | B | NGFR activity raises ARL4D's level | lines that do not express NGFR (19) vs lines expressing it (31) | 1.92× lower at baseline in the lines without NGFR | 0.086 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11 |
| [[GGT7]] | C | GGT7 activity raises ARL4D's level | lines that do not express GGT7 (5) vs lines expressing it (45) | 3.50× lower at baseline in the lines without GGT7 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: BBS5, ODAD4, ALK; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRDM10]] | B | ARL4D activity lowers PRDM10's level | lines that do not express ARL4D (5) vs lines expressing it (45) | 1.85× higher at baseline in the lines without ARL4D | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: GGT7, SOGA1, ELOVL5 |
| [[ITFG1]] | B | ARL4D activity lowers ITFG1's level | lines that do not express ARL4D (5) vs lines expressing it (45) | 1.43× higher at baseline in the lines without ARL4D | 0.057 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: GGT7, SOGA1, ELOVL5 |
| [[CTR9]] | B | ARL4D activity raises CTR9's level | lines that do not express ARL4D (5) vs lines expressing it (45) | 1.29× lower at baseline in the lines without ARL4D | 0.092 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: GGT7, SOGA1, ELOVL5 |
| [[GGT7]] | C | ARL4D activity raises GGT7's level | lines that do not express ARL4D (5) vs lines expressing it (45) | 5.81× lower at baseline in the lines without ARL4D | 0.025 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: GGT7, SOGA1, ELOVL5; co-absent with the target |

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.432). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.0, -12.3); signed map (-8.2, 16.4). **Vector** length 75.4, 14.4% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +12.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.8 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +7.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.5 | +4.5 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +3.1 | +6.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.8 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +2.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +0.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.6 | -0.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.5 | +1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.9 | -2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.5 | -0.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Dapagliflozin (drug)]] 0.05 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 4D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:43,398,993-43,401,137 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ARF4L |
| Gene groups (HGNC) | ARF GTPase family |
| Matched by | ensembl_id |

**Function**, from UniProt [P49703](https://www.uniprot.org/uniprotkb/P49703) (ADP-ribosylation factor-like protein 4D):

> Small GTP-binding protein which cycles between an inactive GDP-bound and an active GTP-bound form, and the rate of cycling is regulated by guanine nucleotide exchange factors (GEF) and GTPase-activating proteins (GAP). GTP-binding protein that does not act as an allosteric activator of the cholera toxin catalytic subunit. Recruits CYTH1, CYTH2, CYTH3 and CYTH4 to the plasma membrane in GDP-bound form.

**Summary**, from NCBI Gene [379](https://www.ncbi.nlm.nih.gov/gene/379):

> ADP-ribosylation factor 4D is a member of the ADP-ribosylation factor family of GTP-binding proteins. ARL4D is closely similar to ARL4A and ARL4C and each has a nuclear localization signal and an unusually high guanine nucleotide exchange rate. This protein may play a role in membrane-associated intracellular trafficking. [provided by RefSeq, Jul 2021]

**Accessions** — [HGNC:656](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:656) · Entrez [379](https://www.ncbi.nlm.nih.gov/gene/379) · UniProt [P49703](https://www.uniprot.org/uniprotkb/P49703) · Ensembl [ENSG00000175906](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175906)

## Data

Gene col 10664: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10664); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10664, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10664]; `tensor/DDL_lfc|DDL_z.npy` [10664]; `embed/gene_vectors.npy` [10664]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10664 or target_col == 10664). Every well: [[ARL4D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL4D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
