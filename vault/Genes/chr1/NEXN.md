---
symbol: "NEXN"
type: "gene"
col: 8543
ensembl_id: "ENSG00000162614"
name: "nexilin F-actin binding protein"
location: "1p31.1"
module: 68
arm: "+"
pooled_cpm: 14.09
n_lines_expressing: 49
n_dd_up: 31
n_dd_down: 5
n_dd_up_clean: 26
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# NEXN

*nexilin F-actin binding protein* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.59× (z +14.2, q 1e-42, up in 28 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +7.8, q 1e-12, up in 27 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.585× (z -5.9, q 2e-06, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AEBP2]] (+0.67, fdr 4e-05), [[TIAM2]] (+0.65, fdr 1e-05), [[CFAP70]] (+0.61, fdr 2e-04); moves opposite to [[RNF168]] (-0.62, fdr 1e-05), [[HPCAL1]] (-0.60, fdr 1e-04), [[ABTB3]] (-0.60, fdr 1e-04).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[SLFN12]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8543.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.59×** | +14.2 | 1e-42 | 28/34 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.20×** | +12.4 | 9e-33 | 18/20 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.73×** | +10.3 | 1e-22 | 22/28 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +7.8 | 1e-12 | 27/44 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +7.5 | 7e-12 | 29/47 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +7.3 | 2e-11 | 25/43 (A498, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.95×** | +7.1 | 9e-11 | 24/46 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +6.4 | 1e-08 | 23/46 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.3 | 9e-06 | 23/47 (PANC-1, HS-578T, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.0 | 3e-05 | 17/41 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.45×** | +4.9 | 4e-05 | 24/47 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.39×** | +4.3 | 9e-04 | 17/47 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.3 | 9e-04 | 17/42 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.49×** | +4.3 | 9e-04 | 17/46 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.001 | 17/47 (SNU-423, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.003 | 17/46 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.42×** | +3.9 | 0.003 | 13/47 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.007 | 14/46 (HS-578T, A-172, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8543.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.585×** | -5.9 | 2e-06 | 25/47 (A498, NCI-H661, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.661×** | -4.6 | 0.001 | 21/47 (A498, H4, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.694×** | -4.1 | 0.010 | 22/47 (KATO III, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.719×** | -3.7 | 0.036 | 17/45 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.729×** | -3.5 | 0.051 | 19/47 (A498, H4, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.750× | -3.0 | 0.24 | 10/45 (NCI-H1792, A549, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8543. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 68.3 | 4 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -12.6) |
| [[HS-578T (line)]] | alt | 31.0 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 16.4× (z +15.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.98× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 14.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.75× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.50× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 13.5 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 5.20× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 27.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.1× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.27× (z +9.5) | — |
| [[A549 (line)]] | wt | 7.32 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +9.6) | — |
| [[J82 (line)]] | alt | 24.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.84× (z +11.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 8.53 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.120× (z -9.5) |
| [[A-172 (line)]] | wt | 17.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +9.3) | — |
| [[A-427 (line)]] | wt | 3.97 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0567× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 16.5 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.109× (z -12.4) |
| [[HOP62 (line)]] | alt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 8.99 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.18× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0872× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[NCI-H460 (line)]] | wt | 5.07 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.29× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 31.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0567× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 25.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.33× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 20.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.08× (z +9.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8543), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 14 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AEBP2]] | +0.67 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[TIAM2]] | +0.65 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[CFAP70]] | +0.61 | +0.67 / +0.30 | both halves | 2e-04 |  |
| [[NQO1-DT]] | +0.61 | +0.59 / +0.33 | both halves | 1e-04 |  |
| [[RIPK2-DT]] | +0.60 | +0.63 / +0.33 | both halves | 1e-04 |  |
| [[CFLAR]] | +0.60 | +0.54 / +0.38 | both halves | 6e-05 |  |
| [[TTC33]] | +0.60 | +0.57 / +0.32 | both halves | 2e-04 |  |
| [[PPP1R12A-AS2]] | +0.59 | +0.60 / +0.23 | both halves | 5e-04 |  |
| [[SLFN12]] | +0.59 | +0.63 / +0.39 | both halves | 5e-05 |  |
| [[ROS1]] | +0.59 | +0.64 / +0.39 | both halves | 6e-05 |  |
| [[ANKRD18B]] | +0.58 | +0.50 / +0.28 | both halves | 3e-04 |  |
| [[PATL2]] | +0.58 | +0.58 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF168]] | -0.62 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[HPCAL1]] | -0.60 | -0.56 / -0.36 | both halves | 1e-04 |  |
| [[ABTB3]] | -0.60 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[UBA6]] | -0.56 | -0.61 / -0.24 | both halves | 5e-04 |  |
| [[GNA12]] | -0.55 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[CIB1]] | -0.55 | -0.58 / -0.28 | both halves | 3e-04 |  |
| [[DNAAF3]] | -0.54 | -0.27 / -0.38 | both halves | 3e-04 |  |
| [[RIMS3]] | -0.54 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[KCNK3]] | -0.54 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[FHIP1B]] | -0.54 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[SEMA4B]] | -0.53 | -0.57 / -0.32 | both halves | 2e-04 |  |
| [[ETV5]] | -0.53 | -0.51 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLFN12]] | B | SLFN12 activity raises NEXN's level | lines that do not express SLFN12 (22) vs lines expressing it (28) | 2.25× lower at baseline in the lines without SLFN12 | 0.005 | ⚠ within organs, on part of the lines; also absent: LAMA4, CHSY3, NLRP1 |
| [[GPR176]] | B | GPR176 activity raises NEXN's level | lines that do not express GPR176 (18) vs lines expressing it (32) | 2.16× lower at baseline in the lines without GPR176 | 0.010 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, AFAP1L1 |
| [[ROS1]] | B | ROS1 activity raises NEXN's level | lines that do not express ROS1 (30) vs lines expressing it (20) | 1.78× lower at baseline in the lines without ROS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: COL1A1, APCDD1L, GYPC; maybe low, not absent |
| [[SUCLG2-DT]] | B | SUCLG2-DT activity raises NEXN's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 2.25× lower at baseline in the lines without SUCLG2-DT | 0.030 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers NEXN's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises NEXN's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAGI2-AS3]] | B | MAGI2-AS3 activity raises NEXN's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 1.83× lower at baseline in the lines without MAGI2-AS3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC |
| [[TGFB2]] | B | TGFB2 activity raises NEXN's level | lines that do not express TGFB2 (15) vs lines expressing it (35) | 1.83× lower at baseline in the lines without TGFB2 | 0.097 | ⚠ within organs, on part of the lines; also absent: CTSF, EHD3, MAP9 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.582). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (33.9, -10.2); signed map (21.5, 4.3). **Vector** length 94.6, 20.2% of its response variance represented; |z| ≥ 3 in 1,230 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +12.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +7.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.3 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +14.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +5.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.5 | +3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.4 | +4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +1.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.4 | -5.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.8 | -4.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -3.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -2.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.4 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | nexilin F-actin binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:77,888,513-77,943,895 (+) |
| Ensembl biotype | protein_coding |
| Also known as | nexilin, NELIN |
| Gene groups (HGNC) | I-set domain containing |
| Hallmark sets | APICAL_JUNCTION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0ZGT2](https://www.uniprot.org/uniprotkb/Q0ZGT2) (Nexilin):

> Involved in regulating cell migration through association with the actin cytoskeleton. Has an essential role in the maintenance of Z line and sarcomere integrity.

**Summary**, from NCBI Gene [91624](https://www.ncbi.nlm.nih.gov/gene/91624):

> This gene encodes a filamentous actin-binding protein that may function in cell adhesion and migration. Mutations in this gene have been associated with dilated cardiomyopathy, also known as CMD1CC. Alternatively spliced transcript variants have been described.[provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:29557](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29557) · Entrez [91624](https://www.ncbi.nlm.nih.gov/gene/91624) · UniProt [Q0ZGT2](https://www.uniprot.org/uniprotkb/Q0ZGT2) · Ensembl [ENSG00000162614](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162614)

## Data

Gene col 8543: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8543); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8543, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8543]; `tensor/DDL_lfc|DDL_z.npy` [8543]; `embed/gene_vectors.npy` [8543]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8543 or target_col == 8543). Every well: [[NEXN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEXN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
