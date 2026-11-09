---
symbol: "IL17RE"
type: "gene"
col: 8758
ensembl_id: "ENSG00000163701"
name: "interleukin 17 receptor E"
location: "3p25.3"
module: 8
arm: "+"
pooled_cpm: 5.29
n_lines_expressing: 40
n_dd_up: 21
n_dd_down: 10
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 21
direction_downstream: 16
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# IL17RE

*interleukin 17 receptor E* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.69× (z +17.5, q 0e+00, up in 13 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.631× (z -5.8, q 4e-06, down in 16 of 32 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.675× (z -4.9, q 2e-04, down in 15 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RORC]] (+0.62, fdr 7e-06), [[LPAR5]] (+0.58, fdr 3e-05), [[PRSS51]] (+0.58, fdr 2e-05); moves opposite to [[ALMS1]] (-0.53, fdr 2e-05), [[MTOR]] (-0.47, fdr 3e-05), [[OSMR]] (-0.45, fdr 5e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[FUT3]] → it (grade B ⚠); 16 go from it, the strongest it → [[SLC44A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8758.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.69×** | +17.5 | 0e+00 | 13/26 (A549, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.61×** | +17.0 | 0e+00 | 12/27 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.59×** | +11.9 | 2e-30 | 9/26 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +9.4 | 1e-18 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +7.2 | 7e-11 | 11/30 (HOP62, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +7.2 | 7e-11 | 2/14 (HCT15, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +7.2 | 7e-11 | 6/20 (LoVo, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +5.5 | 3e-06 | 12/33 (SW1417, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +5.2 | 1e-05 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +4.5 | 3e-04 | 5/33 (COLO 205, BT-474, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.2 | 0.002 | 6/24 (SW48, SNU-1, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.57×** | +4.0 | 0.003 | 3/23 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.005 | 5/33 (HOP62, A-172, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +3.8 | 0.007 | 0/7 | inconsistent across doses | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.061 | 8/30 (SNU-1, Hs 766T, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.061 | 7/32 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.061 | 2/30 (SW480, SHP-77) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.60×** | +3.1 | 0.061 | 0/18 | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.068 | 1/25 (HepG2/C3A) | inconsistent across doses | low cells (technical?) |
| [[Bendamustine (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.083 | 5/27 (HepG2/C3A, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8758.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.631×** | -5.8 | 4e-06 | 16/32 (LS 180, SW48, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.669×** | -5.0 | 1e-04 | 16/34 (LS 180, SW480, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.675×** | -4.9 | 2e-04 | 15/32 (LS 180, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.677×** | -4.7 | 4e-04 | 8/29 (MIA PaCa-2, LS 180, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.754×** | -3.5 | 0.046 | 14/33 (CFPAC-1, BT-474, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.751×** | -3.5 | 0.052 | 11/30 (COLO 205, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.595×** | -3.4 | 0.053 | 12/28 (MIA PaCa-2, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.764×** | -3.4 | 0.053 | 10/32 (SW480, COLO 205, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.768×** | -3.3 | 0.059 | 11/31 (LS 180, SW1417, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.772×** | -3.2 | 0.069 | 9/31 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.786× | -3.0 | 0.13 | 5/34 (CHP-212, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8758. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 12.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0561× (z -11.1) |
| [[LS 180 (line)]] | wt | 21.5 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -11.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.298× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 7.52 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 2.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.97× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 6.08 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0590× (z -10.3) |
| [[LoVo (line)]] | wt | 4.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 2.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 1.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +9.3) | — |
| [[SW48 (line)]] | wt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.850 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.864 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.984 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.850 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8758), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RORC]] | +0.62 | +0.60 / +0.63 | both halves | 7e-06 | STRING 440 |
| [[LPAR5]] | +0.58 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[PRSS51]] | +0.58 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[LASTR]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[UNC5CL]] | +0.57 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[HNF1A-AS1]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[FUT3]] | +0.55 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[PRRG2]] | +0.53 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[FAXDC2]] | +0.52 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[CRACDL]] | +0.52 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[PIGZ]] | +0.52 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[LINC02580]] | +0.52 | +0.56 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALMS1]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[MTOR]] | -0.47 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[OSMR]] | -0.45 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[TRAPPC9]] | -0.45 | -0.39 / -0.41 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 21, C 0. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FUT3]] | B | FUT3 activity raises IL17RE's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 2.68× lower at baseline in the lines without FUT3 | 0.001 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[SCNN1A]] | B | SCNN1A activity raises IL17RE's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 3.19× lower at baseline in the lines without SCNN1A | 0.002 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[RORC]] | B | RORC activity raises IL17RE's level | lines that do not express RORC (30) vs lines expressing it (20) | 2.83× lower at baseline in the lines without RORC | 0.002 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[ESRP1]] | B | ESRP1 activity raises IL17RE's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 3.24× lower at baseline in the lines without ESRP1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[INAVA]] | B | INAVA activity raises IL17RE's level | lines that do not express INAVA (29) vs lines expressing it (21) | 2.64× lower at baseline in the lines without INAVA | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[FAAH2]] | B | FAAH2 activity raises IL17RE's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.82× lower at baseline in the lines without FAAH2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[LINC01814]] | B | LINC01814 activity raises IL17RE's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 2.86× lower at baseline in the lines without LINC01814 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3 |
| [[SNCG]] | B | SNCG activity raises IL17RE's level | lines that do not express SNCG (30) vs lines expressing it (20) | 2.15× lower at baseline in the lines without SNCG | 0.021 | ⚠ within organs, on part of the lines; also absent: CST6, ENSG00000286546, IGFL2-AS1 |
| [[MUC1]] | B | MUC1 activity raises IL17RE's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 2.16× lower at baseline in the lines without MUC1 | 0.025 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |
| [[RNF43]] | B | RNF43 activity raises IL17RE's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 2.19× lower at baseline in the lines without RNF43 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[HNF1B]] | B | HNF1B activity raises IL17RE's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 1.98× lower at baseline in the lines without HNF1B | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[PRR15L]] | B | PRR15L activity raises IL17RE's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 2.96× lower at baseline in the lines without PRR15L | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3]] | B | IL17RE activity raises SLC44A3's level | lines that do not express IL17RE (10) vs lines expressing it (40) | 2.55× lower at baseline in the lines without IL17RE | 0.023 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent |
| [[LINC02580]] | B | IL17RE activity raises LINC02580's level | lines that do not express IL17RE (10) vs lines expressing it (40) | 1.73× lower at baseline in the lines without IL17RE | 0.025 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent |
| [[NDRG2]] | B | IL17RE activity raises NDRG2's level | lines that do not express IL17RE (10) vs lines expressing it (40) | 1.64× lower at baseline in the lines without IL17RE | 0.035 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent |
| [[RAB11FIP4]] | B | IL17RE activity raises RAB11FIP4's level | lines that do not express IL17RE (10) vs lines expressing it (40) | 2.29× lower at baseline in the lines without IL17RE | 0.035 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent |
| [[MROH7]] | B | IL17RE activity raises MROH7's level | lines that do not express IL17RE (10) vs lines expressing it (40) | 2.19× lower at baseline in the lines without IL17RE | 0.044 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent |
| [[FAXDC2]] | B | IL17RE activity raises FAXDC2's level | lines that do not express IL17RE (10) vs lines expressing it (40) | 1.54× lower at baseline in the lines without IL17RE | 0.047 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent |
| [[PRRG2]] | B | IL17RE activity raises PRRG2's level | lines that do not express IL17RE (10) vs lines expressing it (40) | 1.97× lower at baseline in the lines without IL17RE | 0.057 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent |
| [[SEMA4D]] | B | IL17RE activity strengthens SEMA4D's drug response | lines that do not express IL17RE (8) vs lines expressing it (33) | the lines without IL17RE respond 0.50× as strongly (z diff +2.08); strongest at Dinaciclib 5 µM: 1.06x vs 0.43x (z diff +5.7) | 0.068 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[LPAR5]] | B | IL17RE activity raises LPAR5's level | lines that do not express IL17RE (10) vs lines expressing it (40) | 2.11× lower at baseline in the lines without IL17RE | 0.075 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent |
| [[ESRP1]] | B | IL17RE activity raises ESRP1's level | lines that do not express IL17RE (10) vs lines expressing it (40) | 4.60× lower at baseline in the lines without IL17RE | 0.079 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent |
| [[SYTL1]] | B | IL17RE activity raises SYTL1's level | lines that do not express IL17RE (10) vs lines expressing it (40) | 2.13× lower at baseline in the lines without IL17RE | 0.083 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent |
| [[FGD3]] | B | IL17RE activity raises FGD3's level | lines that do not express IL17RE (10) vs lines expressing it (40) | 1.74× lower at baseline in the lines without IL17RE | 0.089 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.494). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.9, 54.7); signed map (60.7, 0.3). **Vector** length 59.6, 10.8% of its response variance represented; |z| ≥ 3 in 758 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +17.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +17.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +9.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.5 | +11.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | +3.1 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -4.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -4.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -3.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 17 receptor E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:9,902,612-9,916,402 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23658 |
| Gene groups (HGNC) | Interleukin receptors |
| Reactome | 3 pathways, smallest: Interleukin-17 signaling; Signaling by Interleukins; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFR9](https://www.uniprot.org/uniprotkb/Q8NFR9) (Interleukin-17 receptor E):

> Specific functional receptor for IL17C. May be signaling through the NF-kappa-B and MAPK pathways. May require TRAF3IP2 /ACT1 for signaling. May be a crucial regulator in innate immunity to bacterial pathogens. Isoform 2 and isoform 4 may be either cytoplasmic inactive or dominant active forms. Isoform 3 and isoform 5 may act as soluble decoy receptors.

**Summary**, from NCBI Gene [132014](https://www.ncbi.nlm.nih.gov/gene/132014):

> This gene encodes a transmembrane protein that functions as the receptor for interleukin-17C. The encoded protein signals to downstream components of the mitogen activated protein kinase (MAPK) pathway. Activity of this protein is important in the immune response to bacterial pathogens. Alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:18439](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18439) · Entrez [132014](https://www.ncbi.nlm.nih.gov/gene/132014) · UniProt [Q8NFR9](https://www.uniprot.org/uniprotkb/Q8NFR9) · Ensembl [ENSG00000163701](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163701)

## Data

Gene col 8758: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8758); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8758, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8758]; `tensor/DDL_lfc|DDL_z.npy` [8758]; `embed/gene_vectors.npy` [8758]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8758 or target_col == 8758). Every well: [[IL17RE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL17RE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
