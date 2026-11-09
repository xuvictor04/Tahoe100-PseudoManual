---
symbol: "FA2H"
type: "gene"
col: 2318
ensembl_id: "ENSG00000103089"
name: "fatty acid 2-hydroxylase"
location: "16q23.1"
module: 31
arm: "+"
pooled_cpm: 75.55
n_lines_expressing: 23
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 7
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 79
direction_downstream: 138
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# FA2H

*fatty acid 2-hydroxylase* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.95× (z +11.3, q 1e-26, up in 8 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.670× (z -6.8, q 8e-09, down in 17 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HS3ST1]] (+0.76, fdr 7e-06), [[PRSS3]] (+0.75, fdr 7e-06), [[JUP]] (+0.75, fdr 7e-06); moves opposite to [[ZNF507]] (-0.57, fdr 1e-05), [[ZMYND11]] (-0.53, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 79 arrows point to it, the strongest [[TMCC3]] → it (grade B ⚠); 138 go from it, the strongest it → [[PTK2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2318.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.95×** | +11.3 | 1e-26 | 8/21 (SW1417, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.04×** | +8.5 | 6e-15 | 8/21 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.94×** | +7.9 | 5e-13 | 7/21 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +5.6 | 3e-06 | 9/22 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +5.2 | 2e-05 | 8/21 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +4.5 | 7e-04 | 1/22 (HCT15) | inconsistent across doses | cell-cycle shift (explains ~9% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.98×** | +4.0 | 0.005 | 17/21 (SW480, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.063 | 12/21 (NCI-H460, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.33× | +3.1 | 0.11 | 11/21 (LS 180, SW480, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2318.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.670×** | -6.8 | 8e-09 | 17/21 (NCI-H1573, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.724×** | -5.5 | 1e-05 | 20/21 (COLO 205, NCI-H2347, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.898× | -4.9 | 2e-04 | 1/23 (NCI-H460) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.661×** | -4.7 | 3e-04 | 19/20 (CFPAC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.699×** | -4.3 | 0.002 | 9/21 (NCI-H1792, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.703×** | -4.2 | 0.002 | 17/21 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -4.1 | 0.004 | 17/21 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.722×** | -3.9 | 0.007 | 12/21 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.712×** | -3.7 | 0.011 | 8/21 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.734×** | -3.7 | 0.012 | 10/21 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.736×** | -3.7 | 0.013 | 12/21 (CFPAC-1, LS 180, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.742×** | -3.6 | 0.017 | 13/21 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Larotrectinib (drug)]] 5 µM |  | **0.825×** | -3.3 | 0.049 | 16/21 (SW48, BT-474, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.747×** | -3.2 | 0.051 | 11/21 (NCI-H1573, A549, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.830×** | -3.2 | 0.060 | 5/21 (NCI-H1792, A549, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.591×** | -3.1 | 0.067 | 12/21 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.772×** | -3.1 | 0.067 | 12/21 (LS 180, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2318. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 461 | 0 | 13 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -31.6) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -12.4) |
| [[A549 (line)]] | wt | 464 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -22.8) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -13.4) |
| [[NCI-H1573 (line)]] | alt | 167 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -19.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0841× (z -18.8) |
| [[LoVo (line)]] | wt | 223 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -20.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -14.5) |
| [[LS 180 (line)]] | wt | 184 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.252× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 76.8 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -18.8) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.405× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 58.3 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.267× (z -11.1) |
| [[KATO III (line)]] | alt | 275 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -21.4) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -10.5) |
| [[COLO 205 (line)]] | alt | 184 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0667× (z -20.0) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.209× (z -11.5) |
| [[SW1417 (line)]] | alt | 24.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.16× (z +12.4) | — |
| [[SW480 (line)]] | alt | 33.8 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.49× (z +10.3) | [[Digitoxin (drug)]] 0.5 µM 0.318× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 335 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -19.0) ⚠ cell-cycle shift, explains ~56% of this change |
| [[Panc 03.27 (line)]] | alt | 70.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -16.4) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.452× (z -8.7) |
| [[HCT15 (line)]] | alt | 53.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -13.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 185 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -12.9) ⚠ cell-cycle shift, explains ~56% of this change |
| [[Hs 766T (line)]] | wt | 58.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -10.6) ⚠ cell-cycle shift, explains ~56% of this change |
| [[NCI-H596 (line)]] | alt | 70.4 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.141× (z -12.6) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.54 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.20 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.88 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.81 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.59 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.48 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.19 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.74 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.99 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 17.7 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.48 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.66 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.74 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.71 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.01 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.80 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.93 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 35.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2318), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HS3ST1]] | +0.76 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[PRSS3]] | +0.75 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[JUP]] | +0.75 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.74 | +0.65 / +0.78 | both halves | 7e-06 |  |
| [[CRYBG2]] | +0.74 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[SULT2B1]] | +0.74 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[RDH13]] | +0.71 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[CDH1]] | +0.70 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[BAIAP2L1]] | +0.69 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[LMTK3]] | +0.68 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[TMEM92]] | +0.68 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[AGPAT2]] | +0.68 | +0.61 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF507]] | -0.57 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.53 | -0.50 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*79 arrows, 79 of them with an alert ⚠; grade A 0, B 13, C 66. Shown: the 12 strongest; 67 more arrows (67 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMCC3]] | B | TMCC3 activity raises FA2H's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 3.90× lower at baseline in the lines without TMCC3 | 0.003 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[CDA]] | B | CDA activity raises FA2H's level | lines that do not express CDA (16) vs lines expressing it (34) | 4.01× lower at baseline in the lines without CDA | 0.013 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[CREG2]] | B | CREG2 activity raises FA2H's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 2.37× lower at baseline in the lines without CREG2 | 0.015 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[XYLT1]] | B | XYLT1 activity raises FA2H's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 1.89× lower at baseline in the lines without XYLT1 | 0.033 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805 |
| [[TFF1]] | B | TFF1 activity weakens FA2H's drug response | lines that do not express TFF1 (8) vs lines expressing it (15) | the lines without TFF1 respond 4.22× as strongly (z diff -2.45); strongest at Panobinostat 5 µM: 2.21x vs 0.78x (z diff -7.2) | 0.046 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC; target measured in part of the lines; artifact flags |
| [[NGEF]] | B | NGEF activity raises FA2H's level | lines that do not express NGEF (12) vs lines expressing it (38) | 4.42× lower at baseline in the lines without NGEF | 0.067 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TSPAN15, PDGFB |
| [[SLC44A4]] | B | SLC44A4 activity weakens FA2H's drug response | lines that do not express SLC44A4 (11) vs lines expressing it (12) | the lines without SLC44A4 respond 3.09× as strongly (z diff -1.63); strongest at Tucidinostat 5 µM: 1.62x vs 0.93x (z diff -4.9) | 0.068 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; target measured in part of the lines; both ways; artifact flags |
| [[PPARG]] | B | PPARG activity raises FA2H's level | lines that do not express PPARG (20) vs lines expressing it (30) | 3.21× lower at baseline in the lines without PPARG | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[WNT7B]] | B | WNT7B activity raises FA2H's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 2.59× lower at baseline in the lines without WNT7B | 0.077 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers FA2H's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers FA2H's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GPRC5A]] | B | GPRC5A activity raises FA2H's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 3.43× lower at baseline in the lines without GPRC5A | 0.088 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |

### Downstream of this gene

*138 arrows, 138 of them with an alert ⚠; grade A 0, B 74, C 64. Shown: the 12 strongest; 126 more arrows (126 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTK2B]] | B | FA2H activity raises PTK2B's level | lines that do not express FA2H (27) vs lines expressing it (23) | 3.52× lower at baseline in the lines without FA2H | 5e-04 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[ARHGAP27]] | B | FA2H activity raises ARHGAP27's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.69× lower at baseline in the lines without FA2H | 0.001 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[GPRC5A]] | B | FA2H activity raises GPRC5A's level | lines that do not express FA2H (27) vs lines expressing it (23) | 4.08× lower at baseline in the lines without FA2H | 0.001 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[KIAA1522]] | B | FA2H activity raises KIAA1522's level | lines that do not express FA2H (27) vs lines expressing it (23) | 3.08× lower at baseline in the lines without FA2H | 0.002 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[RASSF7]] | B | FA2H activity raises RASSF7's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.29× lower at baseline in the lines without FA2H | 0.003 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[PROSER2]] | B | FA2H activity raises PROSER2's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.96× lower at baseline in the lines without FA2H | 0.003 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[EPS8L1]] | B | FA2H activity raises EPS8L1's level | lines that do not express FA2H (27) vs lines expressing it (23) | 3.68× lower at baseline in the lines without FA2H | 0.003 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[KPNA7]] | B | FA2H activity raises KPNA7's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.57× lower at baseline in the lines without FA2H | 0.004 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[MCU]] | B | FA2H activity raises MCU's level | lines that do not express FA2H (27) vs lines expressing it (23) | 1.75× lower at baseline in the lines without FA2H | 0.005 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[CDA]] | B | FA2H activity raises CDA's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.80× lower at baseline in the lines without FA2H | 0.005 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[RHPN2]] | B | FA2H activity raises RHPN2's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.77× lower at baseline in the lines without FA2H | 0.007 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[SERPINB1]] | B | FA2H activity raises SERPINB1's level | lines that do not express FA2H (27) vs lines expressing it (23) | 3.93× lower at baseline in the lines without FA2H | 0.007 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.767). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.4, 55.8); signed map (-1.1, 38.3). **Vector** length 110, 43.2% of its response variance represented; |z| ≥ 3 in 745 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +11.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.2 | +7.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +8.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +5.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.6 | +5.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +1.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -3.9 | -6.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -3.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -3.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.6 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | fatty acid 2-hydroxylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:74,712,955-74,774,831 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FAAH, FLJ25287; previously FAXDC1, SPG35 |
| Gene groups (HGNC) | Fatty acid hydroxylase domain containing; Cytochrome b5 domain containing |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L5A8](https://www.uniprot.org/uniprotkb/Q7L5A8) (Fatty acid 2-hydroxylase):

> Catalyzes the hydroxylation of free fatty acids at the C-2 position to produce 2-hydroxy fatty acids, which are building blocks of sphingolipids and glycosphingolipids common in neural tissue and epidermis. FA2H is stereospecific for the production of (R)-2-hydroxy fatty acids. Plays an essential role in the synthesis of galactosphingolipids of the myelin sheath (By similarity). Responsible for the synthesis of sphingolipids and glycosphingolipids involved in the formation of epidermal lamellar …

**Summary**, from NCBI Gene [79152](https://www.ncbi.nlm.nih.gov/gene/79152):

> This gene encodes a protein that catalyzes the synthesis of 2-hydroxysphingolipids, a subset of sphingolipids that contain 2-hydroxy fatty acids. Sphingolipids play roles in many cellular processes and their structural diversity arises from modification of the hydrophobic ceramide moiety, such as by 2-hydroxylation of the N-acyl chain, and the existence of many different head groups. Mutations in this gene have been associated with leukodystrophy dysmyelinating with spastic paraparesis with or …

**Accessions** — [HGNC:21197](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21197) · Entrez [79152](https://www.ncbi.nlm.nih.gov/gene/79152) · UniProt [Q7L5A8](https://www.uniprot.org/uniprotkb/Q7L5A8) · Ensembl [ENSG00000103089](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103089)

## Data

Gene col 2318: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2318); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2318, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2318]; `tensor/DDL_lfc|DDL_z.npy` [2318]; `embed/gene_vectors.npy` [2318]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2318 or target_col == 2318). Every well: [[FA2H — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FA2H.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
