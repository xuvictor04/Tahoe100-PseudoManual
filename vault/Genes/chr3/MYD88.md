---
symbol: "MYD88"
type: "gene"
col: 10318
ensembl_id: "ENSG00000172936"
name: "MYD88 innate immune signal transduction adaptor"
location: "3p22.2"
module: 32
arm: "+"
pooled_cpm: 9.04
n_lines_expressing: 45
n_dd_up: 4
n_dd_down: 26
n_dd_up_clean: 4
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 33
direction_downstream: 19
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# MYD88

*MYD88 innate immune signal transduction adaptor* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.74× (z +4.6, q 0.002, up in 23 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.236× (z -12.1, q 7e-31, down in 38 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DTX3L]] (+0.75, fdr 7e-06), [[DDX60L]] (+0.73, fdr 1e-05), [[IFIT5]] (+0.72, fdr 7e-06); moves opposite to [[TOMM20]] (-0.59, fdr 3e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 33 arrows point to it, the strongest [[SAMD9L]] → it (grade B ⚠); 19 go from it, the strongest it → [[NLRC5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10318.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.74×** | +4.6 | 0.002 | 23/42 (NCI-H2347, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.74×** | +4.5 | 0.002 | 19/40 (A549, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.046 | 14/43 (AsPC-1, HEC-1-A, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +3.6 | 0.046 | 16/41 (NCI-H2347, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.46× | +3.2 | 0.15 | 11/40 (PANC-1, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10318.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.236×** | -12.1 | 7e-31 | 38/42 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.250×** | -11.6 | 1e-28 | 36/42 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.376×** | -11.6 | 1e-28 | 31/38 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.287×** | -10.4 | 2e-23 | 39/42 (RKO, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.439×** | -6.6 | 4e-09 | 26/41 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.514×** | -5.6 | 3e-06 | 28/42 (Hs 766T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.517×** | -5.5 | 3e-06 | 24/42 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.629×** | -5.5 | 3e-06 | 27/40 (HepG2/C3A, RPMI-7951, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.566×** | -4.7 | 1e-04 | 23/42 (NCI-H1792, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.568×** | -4.7 | 1e-04 | 24/41 (RPMI-7951, A498, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.569×** | -4.7 | 1e-04 | 23/39 (SNU-423, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.697×** | -4.2 | 0.001 | 24/41 (A549, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.606×** | -4.2 | 0.001 | 23/38 (SK-MEL-2, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.612×** | -4.1 | 0.002 | 17/41 (SNU-423, A549, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.607×** | -3.9 | 0.003 | 20/40 (A549, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.415×** | -3.8 | 0.004 | 17/41 (COLO 205, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10318. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.06 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0640× (z -22.6) |
| [[LoVo (line)]] | wt | 20.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -14.3) |
| [[NCI-H1573 (line)]] | alt | 9.71 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0608× (z -11.7) |
| [[A549 (line)]] | wt | 15.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0699× (z -16.2) |
| [[AsPC-1 (line)]] | alt | 26.7 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0825× (z -13.5) |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.0825× (z -12.1) |
| [[NCI-H1792 (line)]] | alt | 17.6 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.0778× (z -12.9) |
| [[RKO (line)]] | wt | 11.4 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0240× (z -14.2) |
| [[KATO III (line)]] | alt | 17.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -10.4) |
| [[SW480 (line)]] | alt | 8.40 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.126× (z -13.5) |
| [[BT-474 (line)]] | alt | 4.48 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0752× (z -10.2) |
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0568× (z -10.9) |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.153× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 5.06 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0506× (z -9.7) |
| [[PANC-1 (line)]] | alt | 4.80 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -14.2) |
| [[RPMI-7951 (line)]] | alt | 12.9 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0719× (z -10.1) |
| [[Hs 766T (line)]] | wt | 9.71 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 17.2 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.156× (z -8.5) |
| [[SNU-423 (line)]] | alt | 9.05 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0520× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW1417 (line)]] | alt | 20.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -8.5) |
| [[A-172 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10318), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTX3L]] | +0.75 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[DDX60L]] | +0.73 | +0.57 / +0.75 | both halves | 1e-05 |  |
| [[IFIT5]] | +0.72 | +0.59 / +0.73 | both halves | 7e-06 | STRING 400 |
| [[OAS2]] | +0.71 | +0.65 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 466 |
| [[TRIM21]] | +0.70 | +0.57 / +0.69 | both halves | 8e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 621 |
| [[PARP14]] | +0.70 | +0.56 / +0.71 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[SLC15A3]] | +0.70 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[TAP2]] | +0.69 | +0.55 / +0.69 | both halves | 1e-05 | pathway: Antigen processing-Cross presentation |
| [[IFI35]] | +0.69 | +0.59 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[SAMD9L]] | +0.69 | +0.62 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[ADAR]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[PARP9]] | +0.69 | +0.56 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOMM20]] | -0.59 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 31, C 2. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD9L]] | B | SAMD9L activity raises MYD88's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.78× lower at baseline in the lines without SAMD9L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[ETV7]] | B | ETV7 activity raises MYD88's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 2.73× lower at baseline in the lines without ETV7 | 0.002 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[RSAD2]] | B | RSAD2 activity raises MYD88's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.04× lower at baseline in the lines without RSAD2 | 0.004 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[IFI44]] | B | IFI44 activity raises MYD88's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 1.84× lower at baseline in the lines without IFI44 | 0.004 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[EPSTI1]] | B | EPSTI1 activity raises MYD88's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 1.95× lower at baseline in the lines without EPSTI1 | 0.007 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[OAS2]] | B | OAS2 activity raises MYD88's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 1.54× lower at baseline in the lines without OAS2 | 0.008 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[MX1]] | B | MX1 activity raises MYD88's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.73× lower at baseline in the lines without MX1 | 0.008 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[OAS1]] | B | OAS1 activity raises MYD88's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.81× lower at baseline in the lines without OAS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[OAS3]] | B | OAS3 activity raises MYD88's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 2.44× lower at baseline in the lines without OAS3 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[TRIM22]] | B | TRIM22 activity raises MYD88's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.83× lower at baseline in the lines without TRIM22 | 0.010 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[RASGRP3]] | B | RASGRP3 activity raises MYD88's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 1.66× lower at baseline in the lines without RASGRP3 | 0.010 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[NRIR]] | B | NRIR activity raises MYD88's level | lines that do not express NRIR (14) vs lines expressing it (36) | 1.39× lower at baseline in the lines without NRIR | 0.018 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 18, C 1. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NLRC5]] | B | MYD88 activity raises NLRC5's level | lines that do not express MYD88 (5) vs lines expressing it (45) | 3.09× lower at baseline in the lines without MYD88 | 0.022 | ⚠ within organs, on part of the lines; also absent: PRRG1, KIFC3, HMGA1P4 |
| [[TRANK1]] | B | MYD88 activity raises TRANK1's level | lines that do not express MYD88 (5) vs lines expressing it (45) | 3.39× lower at baseline in the lines without MYD88 | 0.024 | ⚠ within organs, on part of the lines; also absent: PRRG1, KIFC3, HMGA1P4 |
| [[OAS1]] | B | MYD88 activity raises OAS1's level | lines that do not express MYD88 (5) vs lines expressing it (45) | 4.00× lower at baseline in the lines without MYD88 | 0.030 | ⚠ within organs, on part of the lines; also absent: PRRG1, KIFC3, HMGA1P4 |
| [[DDX60]] | B | MYD88 activity raises DDX60's level | lines that do not express MYD88 (5) vs lines expressing it (45) | 2.19× lower at baseline in the lines without MYD88 | 0.032 | ⚠ within organs, on part of the lines; also absent: PRRG1, KIFC3, HMGA1P4 |
| [[PML]] | B | MYD88 activity raises PML's level | lines that do not express MYD88 (5) vs lines expressing it (45) | 1.68× lower at baseline in the lines without MYD88 | 0.045 | ⚠ within organs, on part of the lines; also absent: PRRG1, KIFC3, HMGA1P4 |
| [[PSMB8]] | B | MYD88 activity raises PSMB8's level | lines that do not express MYD88 (5) vs lines expressing it (45) | 2.25× lower at baseline in the lines without MYD88 | 0.045 | ⚠ within organs, on part of the lines; also absent: PRRG1, KIFC3, HMGA1P4 |
| [[SAMD9]] | B | MYD88 activity raises SAMD9's level | lines that do not express MYD88 (5) vs lines expressing it (45) | 2.74× lower at baseline in the lines without MYD88 | 0.060 | ⚠ within organs, on part of the lines; also absent: PRRG1, KIFC3, HMGA1P4 |
| [[SAMD9L]] | B | MYD88 activity raises SAMD9L's level | lines that do not express MYD88 (5) vs lines expressing it (45) | 2.98× lower at baseline in the lines without MYD88 | 0.067 | ⚠ within organs, on part of the lines; also absent: PRRG1, KIFC3, HMGA1P4 |
| [[PARP14]] | B | MYD88 activity raises PARP14's level | lines that do not express MYD88 (5) vs lines expressing it (45) | 2.42× lower at baseline in the lines without MYD88 | 0.070 | ⚠ within organs, on part of the lines; also absent: PRRG1, KIFC3, HMGA1P4 |
| [[TMEM140]] | B | MYD88 activity raises TMEM140's level | lines that do not express MYD88 (5) vs lines expressing it (45) | 2.42× lower at baseline in the lines without MYD88 | 0.077 | ⚠ within organs, on part of the lines; also absent: PRRG1, KIFC3, HMGA1P4 |
| [[XAF1]] | B | MYD88 activity raises XAF1's level | lines that do not express MYD88 (5) vs lines expressing it (45) | 3.35× lower at baseline in the lines without MYD88 | 0.087 | ⚠ within organs, on part of the lines; also absent: PRRG1, KIFC3, HMGA1P4 |
| [[RSAD2]] | B | MYD88 activity raises RSAD2's level | lines that do not express MYD88 (5) vs lines expressing it (45) | 2.83× lower at baseline in the lines without MYD88 | 0.087 | ⚠ within organs, on part of the lines; also absent: PRRG1, KIFC3, HMGA1P4 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.703). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.1, 54.7); signed map (63.6, 33.0). **Vector** length 92.8, 22.4% of its response variance represented; |z| ≥ 3 in 969 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.57 to 56); *interferon* (control, mean cos +0.60 to 23); *Interferon Signaling* (reactome, mean cos +0.58 to 45).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +6.2 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.8 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +3.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.6 | +3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.4 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.6 | +1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.4 | +1.5 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -4.6 | -5.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.4 | -4.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.9 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.4 | -3.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | MYD88 innate immune signal transduction adaptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:38,138,552-38,143,024 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | TIR domain containing; My-T-BRC complex |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, PI3K_AKT_MTOR_SIGNALING, INTERFERON_GAMMA_RESPONSE |
| Reactome | 39 pathways, smallest: DEx/H-box helicases activate type I IFN and inflammatory cytokines production; TRAF6 mediated IRF7 activation in TLR7/8 or 9 signaling; p75NTR recruits signalling complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99836](https://www.uniprot.org/uniprotkb/Q99836) (Myeloid differentiation primary response protein MyD88):

> Adapter protein involved in the Toll-like receptor and IL-1 receptor signaling pathway in the innate immune response. Acts via IRAK1, IRAK2, IRF7 and TRAF6, leading to NF-kappa-B activation, cytokine secretion and the inflammatory response. Increases IL-8 transcription. Involved in IL-18-mediated signaling pathway. Activates IRF1 resulting in its rapid migration into the nucleus to mediate an efficient induction of IFN-beta, NOS2/INOS, and IL12A genes. Upon TLR8 activation by GU-rich …

**Summary**, from NCBI Gene [4615](https://www.ncbi.nlm.nih.gov/gene/4615):

> This gene encodes a cytosolic adapter protein that plays a central role in the innate and adaptive immune response. This protein functions as an essential signal transducer in the interleukin-1 and Toll-like receptor signaling pathways. These pathways regulate that activation of numerous proinflammatory genes. The encoded protein consists of an N-terminal death domain and a C-terminal Toll-interleukin1 receptor domain. Patients with defects in this gene have an increased susceptibility to …

**Accessions** — [HGNC:7562](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7562) · Entrez [4615](https://www.ncbi.nlm.nih.gov/gene/4615) · UniProt [Q99836](https://www.uniprot.org/uniprotkb/Q99836) · Ensembl [ENSG00000172936](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172936)

## Data

Gene col 10318: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10318); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10318, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10318]; `tensor/DDL_lfc|DDL_z.npy` [10318]; `embed/gene_vectors.npy` [10318]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10318 or target_col == 10318). Every well: [[MYD88 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYD88.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
