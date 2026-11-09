---
symbol: "ARSL"
type: "gene"
col: 8067
ensembl_id: "ENSG00000157399"
name: "arylsulfatase L"
location: "Xp22.33"
module: 8
arm: "+"
pooled_cpm: 3.61
n_lines_expressing: 24
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 41
direction_downstream: 43
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ARSL

*arylsulfatase L* — Xp22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.30× (z +12.1, q 9e-31, up in 7 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +4.0, q 0.006, up in 1 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.575× (z -4.0, q 0.032, down in 9 of 21 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.0530×, A549 0.246×, CFPAC-1 0.185×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (COLO 205 0.0644×, LoVo 0.0872×, A549 0.215×; ⚠ cell-cycle shift, explains ~5% of this change); [[Belinostat (drug)]] 0.5 µM in 2 lines (HT-29 0.0710×, HEC-1-A 0.165×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.0379×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (COLO 205 0.0628×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNF1A-AS1]] (+0.72, fdr 7e-06), [[SEC16B]] (+0.70, fdr 7e-06), [[RNF183]] (+0.69, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 41 arrows point to it, the strongest [[DCDC2]] → it (grade B ⚠); 43 go from it, the strongest it → [[LINC01504]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8067.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.30×** | +12.1 | 9e-31 | 7/11 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.45×** | +10.4 | 7e-23 | 6/7 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.59×** | +8.5 | 2e-15 | 4/9 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +4.3 | 0.003 | 3/10 (NCI-H2347, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.006 | 1/18 (LS 180) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.007 | 4/21 (A549, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.008 | 5/20 (KATO III, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.67×** | +3.7 | 0.014 | 3/12 (SK-MEL-2, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.62×** | +3.5 | 0.029 | 7/21 (A549, KATO III, …) | rises with dose |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.60×** | +3.4 | 0.042 | 1/16 (HCT15) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.88×** | +3.1 | 0.086 | 2/11 (COLO 205, LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8067.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.0530×, A549 0.246×, CFPAC-1 0.185×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (COLO 205 0.0644×, LoVo 0.0872×, A549 0.215×; ⚠ cell-cycle shift, explains ~5% of this change); [[Belinostat (drug)]] 0.5 µM in 2 lines (HT-29 0.0710×, HEC-1-A 0.165×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.0379×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (COLO 205 0.0628×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.575×** | -4.0 | 0.032 | 9/21 (COLO 205, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8067. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 34.7 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0530× (z -22.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0379× (z -17.8) |
| [[A549 (line)]] | wt | 19.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 10.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.22× (z +9.9) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 0.5 µM 0.165× (z -9.2) |
| [[A498 (line)]] | wt | 7.20 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -8.9) ⚠ cell-cycle shift, explains ~5% of this change |
| [[CFPAC-1 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0921× (z -9.6) |
| [[HT-29 (line)]] | alt | 5.47 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0710× (z -9.5) |
| [[LoVo (line)]] | wt | 7.31 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0872× (z -11.1) ⚠ cell-cycle shift, explains ~5% of this change |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.871 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.275 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.574 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.834 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.646 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.432 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.330 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8067), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNF1A-AS1]] | +0.72 | +0.73 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[SEC16B]] | +0.70 | +0.66 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[RNF183]] | +0.69 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[SMIM2-AS1]] | +0.68 | +0.65 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[ABCC6]] | +0.68 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[FXYD2]] | +0.66 | +0.69 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[BCL2L15]] | +0.66 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[TCN1]] | +0.66 | +0.62 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[PLCH1]] | +0.64 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[FMO5]] | +0.63 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[SLC40A1]] | +0.63 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[EPCAM-DT]] | +0.62 | +0.59 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*41 arrows, 41 of them with an alert ⚠; grade A 0, B 4, C 37. Shown: the 12 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCDC2]] | B | DCDC2 activity raises ARSL's level | lines that do not express DCDC2 (25) vs lines expressing it (25) | 2.13× lower at baseline in the lines without DCDC2 | 0.055 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |
| [[FRMD4B]] | B | FRMD4B activity raises ARSL's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without FRMD4B | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[SLC40A1]] | B | SLC40A1 activity raises ARSL's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 1.59× lower at baseline in the lines without SLC40A1 | 0.068 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[TARID]] | B | TARID activity raises ARSL's level | lines that do not express TARID (29) vs lines expressing it (21) | 1.66× lower at baseline in the lines without TARID | 0.073 | ⚠ within organs, on part of the lines; also absent: STEAP4, ANXA10, HLA-DRB1 |
| [[MMP7]] | C | MMP7 activity raises ARSL's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 3.03× lower at baseline in the lines without MMP7 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP; co-absent with the target |
| [[TRIM31]] | C | TRIM31 activity raises ARSL's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 2.63× lower at baseline in the lines without TRIM31 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1; co-absent with the target |
| [[ITIH2]] | C | ITIH2 activity raises ARSL's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 3.33× lower at baseline in the lines without ITIH2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; co-absent with the target |
| [[SLC44A4]] | C | SLC44A4 activity raises ARSL's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.81× lower at baseline in the lines without SLC44A4 | 0.006 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[APOL1]] | C | APOL1 activity raises ARSL's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.52× lower at baseline in the lines without APOL1 | 0.008 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1; co-absent with the target |
| [[HAVCR1]] | C | HAVCR1 activity raises ARSL's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 3.58× lower at baseline in the lines without HAVCR1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA; co-absent with the target |
| [[SMIM2-AS1]] | C | SMIM2-AS1 activity raises ARSL's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 2.40× lower at baseline in the lines without SMIM2-AS1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent; co-absent with the target |
| [[PDZK1IP1]] | C | PDZK1IP1 activity raises ARSL's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 2.66× lower at baseline in the lines without PDZK1IP1 | 0.011 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8; co-absent with the target |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 15, C 28. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01504]] | B | ARSL activity raises LINC01504's level | lines that do not express ARSL (26) vs lines expressing it (24) | 1.69× lower at baseline in the lines without ARSL | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4 |
| [[ACSM3]] | B | ARSL activity raises ACSM3's level | lines that do not express ARSL (26) vs lines expressing it (24) | 1.46× lower at baseline in the lines without ARSL | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4 |
| [[FMO5]] | B | ARSL activity raises FMO5's level | lines that do not express ARSL (26) vs lines expressing it (24) | 1.81× lower at baseline in the lines without ARSL | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4 |
| [[SPTLC3]] | B | ARSL activity raises SPTLC3's level | lines that do not express ARSL (26) vs lines expressing it (24) | 2.49× lower at baseline in the lines without ARSL | 0.032 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4 |
| [[TMEM51-AS1]] | B | ARSL activity raises TMEM51-AS1's level | lines that do not express ARSL (26) vs lines expressing it (24) | 2.18× lower at baseline in the lines without ARSL | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4 |
| [[SCIN]] | B | ARSL activity raises SCIN's level | lines that do not express ARSL (26) vs lines expressing it (24) | 1.87× lower at baseline in the lines without ARSL | 0.037 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4 |
| [[LINC00298]] | B | ARSL activity raises LINC00298's level | lines that do not express ARSL (26) vs lines expressing it (24) | 1.94× lower at baseline in the lines without ARSL | 0.044 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4 |
| [[RNF43]] | B | ARSL activity strengthens RNF43's drug response | lines that do not express ARSL (11) vs lines expressing it (11) | the lines without ARSL respond 0.57× as strongly (z diff +1.97); strongest at Homoharringtonine 0.5 µM: 0.64x vs 0.31x (z diff +4.2) | 0.049 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4; target measured in part of the lines; artifact flags |
| [[TMC4]] | B | ARSL activity raises TMC4's level | lines that do not express ARSL (26) vs lines expressing it (24) | 2.18× lower at baseline in the lines without ARSL | 0.056 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4 |
| [[ENPP3]] | B | ARSL activity raises ENPP3's level | lines that do not express ARSL (26) vs lines expressing it (24) | 1.52× lower at baseline in the lines without ARSL | 0.058 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4 |
| [[TNFRSF14-AS1]] | B | ARSL activity raises TNFRSF14-AS1's level | lines that do not express ARSL (26) vs lines expressing it (24) | 1.64× lower at baseline in the lines without ARSL | 0.059 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4 |
| [[PLSCR4]] | B | ARSL activity raises PLSCR4's level | lines that do not express ARSL (26) vs lines expressing it (24) | 1.77× lower at baseline in the lines without ARSL | 0.063 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.1, 52.8); signed map (61.0, -0.5). **Vector** length 43.9, 9.80% of its response variance represented; |z| ≥ 3 in 490 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -0.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.3 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | arylsulfatase L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.33 — chrX:2,934,045-2,968,475 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CDPX, CDPX1, ARSE |
| Gene groups (HGNC) | Sulfatases |
| Reactome | 6 pathways, smallest: The activation of arylsulfatases; Glycosphingolipid catabolism; Glycosphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P51690](https://www.uniprot.org/uniprotkb/P51690) (Arylsulfatase L):

> Exhibits arylsulfatase activity towards the artificial substrate 4-methylumbelliferyl sulfate. May be essential for the correct composition of cartilage and bone matrix during development. Has no activity toward steroid sulfates.

**Summary**, from NCBI Gene [415](https://www.ncbi.nlm.nih.gov/gene/415):

> Arylsulfatase E is a member of the sulfatase family. It is glycosylated postranslationally and localized to the golgi apparatus. Sulfatases are essential for the correct composition of bone and cartilage matrix. X-linked chondrodysplasia punctata, a disease characterized by abnormalities in cartilage and bone development, has been linked to mutations in this gene. Alternative splicing results in multiple transcript variants. A pseudogene related to this gene is located on the Y chromosome. …

**Accessions** — [HGNC:719](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:719) · Entrez [415](https://www.ncbi.nlm.nih.gov/gene/415) · UniProt [P51690](https://www.uniprot.org/uniprotkb/P51690) · Ensembl [ENSG00000157399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157399)

## Data

Gene col 8067: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8067); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8067, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8067]; `tensor/DDL_lfc|DDL_z.npy` [8067]; `embed/gene_vectors.npy` [8067]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8067 or target_col == 8067). Every well: [[ARSL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARSL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
