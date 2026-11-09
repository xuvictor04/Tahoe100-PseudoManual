---
symbol: "OR9Q1"
type: "gene"
col: 11824
ensembl_id: "ENSG00000186509"
name: "olfactory receptor family 9 subfamily Q member 1"
location: "11q12.1"
module: 13
arm: "+"
pooled_cpm: 6.18
n_lines_expressing: 24
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 54
direction_downstream: 38
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# OR9Q1

*olfactory receptor family 9 subfamily Q member 1* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.79× (z +13.5, q 6e-39, up in 4 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.489× (z -6.6, q 2e-08, down in 18 of 21 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Betamethasone dipropionate (drug)]] 5 µM: 0.643× (z -3.9, q 0.007, down in 7 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSC-AS1]] (+0.67, fdr 7e-06), [[PTGFR]] (+0.67, fdr 7e-06), [[LINC01411]] (+0.66, fdr 7e-06); moves opposite to [[LRP5]] (-0.51, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 54 arrows point to it, the strongest [[EVC2]] → it (grade B ⚠); 38 go from it, the strongest it → [[LINC01807]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11824.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.79×** | +13.5 | 6e-39 | 4/20 (HCT15, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.12×** | +9.9 | 1e-20 | 14/20 (A549, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +9.5 | 3e-19 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.24×** | +7.5 | 8e-12 | 13/19 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +7.0 | 4e-10 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.69×** | +4.8 | 1e-04 | 3/10 (SNU-423, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +4.2 | 0.002 | 1/19 (A-172) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +3.8 | 0.008 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.008 | 4/20 (A-172, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.49×** | +3.8 | 0.008 | 10/20 (A549, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.008 | 6/20 (HOP62, Hs 766T, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **2.02×** | +3.4 | 0.030 | 6/15 (NCI-H1792, A549, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.049 | 5/18 (NCI-H460, A549, …) | two highest doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.059 | 6/18 (HS-578T, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11824.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.489×** | -6.6 | 2e-08 | 18/21 (NCI-H1792, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.506×** | -6.3 | 7e-08 | 19/21 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.580×** | -5.1 | 8e-05 | 17/21 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.618×** | -4.5 | 0.001 | 11/20 (H4, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.608×** | -4.4 | 0.001 | 15/20 (NCI-H1792, A549, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.641×** | -4.1 | 0.003 | 8/21 (H4, HOP62, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.643×** | -3.9 | 0.007 | 7/18 (NCI-H460, H4, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 5 µM |  | **0.677×** | -3.5 | 0.036 | 7/20 (J82, A549, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.773×** | -3.4 | 0.046 | 10/20 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.702×** | -3.3 | 0.056 | 7/19 (SNU-423, RPMI-7951, …) | inconsistent across doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | **0.703×** | -3.3 | 0.056 | 4/19 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | 0.531× | -3.1 | 0.10 | 10/19 (HOP62, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.56 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11824. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 50.1 | 0 | 13 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0240× (z -18.8) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.1000× (z -16.4) |
| [[NCI-H1792 (line)]] | alt | 37.1 | 0 | 12 (10 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0250× (z -19.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.236× (z -11.5) |
| [[HS-578T (line)]] | alt | 41.7 | 0 | 11 (8 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0209× (z -20.1) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -9.1) |
| [[SNU-423 (line)]] | alt | 29.3 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0237× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -13.6) |
| [[hTERT-HPNE (line)]] | wt | 42.1 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0448× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -9.6) |
| [[H4 (line)]] | wt | 24.0 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -11.0) |
| [[HOP62 (line)]] | alt | 13.4 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0946× (z -11.2) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.212× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 4 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0486× (z -13.1) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -9.2) |
| [[A549 (line)]] | wt | 11.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -11.2) |
| [[J82 (line)]] | alt | 4.15 | 0 | 1 | — | [[Regorafenib (drug)]] 0.05 µM 0.0449× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 4.66 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0568× (z -8.6) ⚠ cell-cycle shift, explains ~77% of this change |
| [[A-172 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.599 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.734 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.962 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.838 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.993 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.853 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.788 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.864 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.844 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.733 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11824), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSC-AS1]] | +0.67 | +0.67 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[PTGFR]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[LINC01411]] | +0.66 | +0.63 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[LINC02109]] | +0.66 | +0.60 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1L-DT]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[APCDD1L]] | +0.66 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[APBB1IP]] | +0.63 | +0.63 / +0.58 | both halves | 8e-06 | **novel candidate** |
| [[LINC01435]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[KC6]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SYNDIG1]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[LINC00536]] | +0.60 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[PAPPA]] | +0.60 | +0.65 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRP5]] | -0.51 | -0.60 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*54 arrows, 54 of them with an alert ⚠; grade A 0, B 1, C 53. Shown: the 12 strongest; 42 more arrows (42 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EVC2]] | B | EVC2 activity strengthens OR9Q1's drug response | lines that do not express EVC2 (11) vs lines expressing it (10) | the lines without EVC2 respond 0.97× as strongly (z diff +0.09); strongest at Panobinostat 0.5 µM: 0.39x vs 0.13x (z diff +5.7) | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; target measured in part of the lines; artifact flags |
| [[APCDD1L]] | C | APCDD1L activity raises OR9Q1's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 5.75× lower at baseline in the lines without APCDD1L | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[HTR1F]] | C | HTR1F activity raises OR9Q1's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 4.15× lower at baseline in the lines without HTR1F | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent; co-absent with the target |
| [[SIRLNT]] | C | SIRLNT activity raises OR9Q1's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 4.12× lower at baseline in the lines without SIRLNT | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1; co-absent with the target |
| [[ABI3BP]] | C | ABI3BP activity raises OR9Q1's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 4.32× lower at baseline in the lines without ABI3BP | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises OR9Q1's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 5.90× lower at baseline in the lines without LINC01411 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[EVC2]] | C | EVC2 activity raises OR9Q1's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 4.61× lower at baseline in the lines without EVC2 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |
| [[ADAM12]] | C | ADAM12 activity raises OR9Q1's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 4.19× lower at baseline in the lines without ADAM12 | 0.003 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |
| [[TNS1]] | C | TNS1 activity raises OR9Q1's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.79× lower at baseline in the lines without TNS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786; co-absent with the target |
| [[CA12]] | C | CA12 activity raises OR9Q1's level | lines that do not express CA12 (29) vs lines expressing it (21) | 2.77× lower at baseline in the lines without CA12 | 0.003 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1; co-absent with the target |
| [[LINC01705]] | C | LINC01705 activity raises OR9Q1's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 3.84× lower at baseline in the lines without LINC01705 | 0.004 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137; co-absent with the target |
| [[STAC]] | C | STAC activity raises OR9Q1's level | lines that do not express STAC (25) vs lines expressing it (25) | 3.32× lower at baseline in the lines without STAC | 0.005 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11; co-absent with the target |

### Downstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 10, C 28. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01807]] | B | OR9Q1 activity raises LINC01807's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 2.31× lower at baseline in the lines without OR9Q1 | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L |
| [[CLDN14]] | B | OR9Q1 activity raises CLDN14's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 2.10× lower at baseline in the lines without OR9Q1 | 0.019 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L |
| [[LRP5]] | B | OR9Q1 activity lowers LRP5's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 2.70× higher at baseline in the lines without OR9Q1 | 0.032 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L |
| [[APH1B]] | B | OR9Q1 activity raises APH1B's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 2.39× lower at baseline in the lines without OR9Q1 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L |
| [[NR2F2-AS1]] | B | OR9Q1 activity raises NR2F2-AS1's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 2.89× lower at baseline in the lines without OR9Q1 | 0.050 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L |
| [[CCN4]] | B | OR9Q1 activity raises CCN4's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 1.87× lower at baseline in the lines without OR9Q1 | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L |
| [[HMGN2P46]] | B | OR9Q1 activity raises HMGN2P46's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 2.92× lower at baseline in the lines without OR9Q1 | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L |
| [[SLC8A1-AS1]] | B | OR9Q1 activity raises SLC8A1-AS1's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 1.54× lower at baseline in the lines without OR9Q1 | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L |
| [[SLC14A2]] | B | OR9Q1 activity raises SLC14A2's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 1.99× lower at baseline in the lines without OR9Q1 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L |
| cells under [[OTS514 (drug)]] 5 µM | B | OR9Q1 activity lowers the cells' numbers under OTS514 5 µM (makes them more sensitive) | lines that do not express OR9Q1 (26) vs lines expressing it (22) | the lines without OR9Q1: 1.17× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L |
| [[ABI3BP]] | C | OR9Q1 activity raises ABI3BP's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 4.54× lower at baseline in the lines without OR9Q1 | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L; co-absent with the target |
| [[CLDN14-AS1]] | C | OR9Q1 activity raises CLDN14-AS1's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 4.12× lower at baseline in the lines without OR9Q1 | 0.023 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.7, 20.0); signed map (29.3, 45.7). **Vector** length 72.1, 22.9% of its response variance represented; |z| ≥ 3 in 602 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +7.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +2.2 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -1.6 | -4.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | olfactory receptor family 9 subfamily Q member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:58,023,881-58,181,616 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Olfactory receptors, family 9 |
| Reactome | 3 pathways, smallest: Expression and translocation of olfactory receptors; Olfactory Signaling Pathway; Sensory Perception |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NGQ5](https://www.uniprot.org/uniprotkb/Q8NGQ5) (Olfactory receptor 9Q1):

> Odorant receptor.

**Summary**, from NCBI Gene [219956](https://www.ncbi.nlm.nih.gov/gene/219956):

> Olfactory receptors interact with odorant molecules in the nose, to initiate a neuronal response that triggers the perception of a smell. The olfactory receptor proteins are members of a large family of G-protein-coupled receptors (GPCR) arising from single coding-exon genes. Olfactory receptors share a 7-transmembrane domain structure with many neurotransmitter and hormone receptors and are responsible for the recognition and G protein-mediated transduction of odorant signals. The olfactory …

**Accessions** — [HGNC:14724](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14724) · Entrez [219956](https://www.ncbi.nlm.nih.gov/gene/219956) · UniProt [Q8NGQ5](https://www.uniprot.org/uniprotkb/Q8NGQ5) · Ensembl [ENSG00000186509](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186509)

## Data

Gene col 11824: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11824); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11824, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11824]; `tensor/DDL_lfc|DDL_z.npy` [11824]; `embed/gene_vectors.npy` [11824]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11824 or target_col == 11824). Every well: [[OR9Q1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OR9Q1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
