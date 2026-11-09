---
symbol: "ASB4"
type: "gene"
col: 95
ensembl_id: "ENSG00000005981"
name: "ankyrin repeat and SOCS box containing 4"
location: "7q21.3"
module: 27
arm: "+"
pooled_cpm: 4.5
n_lines_expressing: 19
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 12
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# ASB4

*ankyrin repeat and SOCS box containing 4* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.13× (z +12.3, q 6e-32, up in 9 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.580× (z -4.2, q 0.019, down in 5 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 3 lines (SW480 0.0859×, LS 180 0.0489×, A-427 0.182×); [[Panobinostat (drug)]] 0.5 µM in 3 lines (LS 180 0.0623×, SW480 0.173×, A-427 0.177×); [[Belinostat (drug)]] 5 µM in 3 lines (SW480 0.157×, LS 180 0.0753×, A-427 0.186×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDK4-AS1]] (+0.67, fdr 7e-06, ⚠ same locus), [[CHDH]] (+0.64, fdr 1e-05), [[LGR5]] (+0.64, fdr 1e-05), [[ST18]] (+0.64, fdr 3e-05); moves opposite to [[PLD3]] (-0.52, fdr 9e-05), [[TNNT1]] (-0.48, fdr 8e-04, ⚠ not reproduced), [[GNAI2]] (-0.47, fdr 3e-04), [[VRK3]] (-0.47, fdr 2e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 12 go from it, the strongest it → [[PDK4-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 95.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.13×** | +12.3 | 6e-32 | 9/16 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.02×** | +11.8 | 7e-30 | 1/2 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.08×** | +10.7 | 2e-24 | 4/6 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.72×** | +9.3 | 3e-18 | 3/4 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.63×** | +5.3 | 2e-05 | 6/17 (COLO 205, LoVo, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +4.5 | 6e-04 | 3/17 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.5 | 6e-04 | 3/17 (SW480, A549, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +4.1 | 0.003 | 7/15 (SW 900, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.70×** | +4.0 | 0.004 | 0/10 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.45×** | +3.6 | 0.020 | 1/5 (SHP-77) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.4 | 0.037 | 0/10 | top dose only | cell-cycle shift (explains ~1% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 1.75× | +3.0 | 0.12 | 1/5 (A-427) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 95.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 3 lines (SW480 0.0859×, LS 180 0.0489×, A-427 0.182×); [[Panobinostat (drug)]] 0.5 µM in 3 lines (LS 180 0.0623×, SW480 0.173×, A-427 0.177×); [[Belinostat (drug)]] 5 µM in 3 lines (SW480 0.157×, LS 180 0.0753×, A-427 0.186×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.580×** | -4.2 | 0.019 | 5/17 (SHP-77, NCI-H1792, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.639× | -3.4 | 0.16 | 10/16 (LS 180, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.651× | -3.3 | 0.16 | 2/17 (NCI-H1792, A-427) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | 0.652× | -3.3 | 0.16 | 8/17 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.751× | -3.1 | 0.17 | 3/17 (PANC-1, LS 180, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.668× | -3.1 | 0.17 | 0/17 | inconsistent across doses | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.669× | -3.1 | 0.17 | 4/17 (LS 180, COLO 205, …) | two highest doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.672× | -3.0 | 0.17 | 4/17 (LS 180, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 95. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 55.2 | 0 | 13 (4 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0243× (z -16.2) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0489× (z -13.9) |
| [[SW480 (line)]] | alt | 23.6 | 1 (1 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.83× (z +10.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.0859× (z -16.3) |
| [[A-427 (line)]] | wt | 23.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -9.6) |
| [[SHP-77 (line)]] | alt | 7.79 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0854× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 4.25 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.125× (z -9.3) ⚠ cell-cycle shift, explains ~19% of this change |
| [[A-172 (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.697 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.675 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.614 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.864 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.698 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.563 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.601 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.803 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.742 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.916 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.584 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.947 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.501 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 95), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDK4-AS1]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 | ⚠ same locus (5.0 kb, same strand: neighbours can correlate without regulation) |
| [[CHDH]] | +0.64 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[LGR5]] | +0.64 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[ST18]] | +0.64 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[LINC02058]] | +0.62 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[SMOC2]] | +0.61 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[MYB]] | +0.61 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[LINC01091]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[CLRN3]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[TFF3]] | +0.59 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[HCN1]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[MBNL3]] | +0.57 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[FOXP4-AS1]] | +0.57 | +0.48 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLD3]] | -0.52 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[TNNT1]] | -0.48 | -0.41 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[GNAI2]] | -0.47 | -0.38 / -0.26 | both halves | 3e-04 |  |
| [[VRK3]] | -0.47 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[DLGAP4]] | -0.46 | -0.42 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ASB4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[COLGALT2]] | B | COLGALT2 activity raises ASB4's level | lines that do not express COLGALT2 (23) vs lines expressing it (27) | 1.72× lower at baseline in the lines without COLGALT2 | 0.097 | ⚠ within organs, on part of the lines; also absent: PRRX1, SYT11, GNAT3 |
| [[SMOC2]] | C | SMOC2 activity raises ASB4's level | lines that do not express SMOC2 (33) vs lines expressing it (17) | 2.38× lower at baseline in the lines without SMOC2 | 0.028 | ⚠ within organs, on part of the lines; also absent: LINC01456, TFF3, MIR3667HG; maybe low, not absent; co-absent with the target |
| [[ST18]] | C | ST18 activity raises ASB4's level | lines that do not express ST18 (39) vs lines expressing it (11) | 4.13× lower at baseline in the lines without ST18 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent; co-absent with the target |
| [[LINC02058]] | C | LINC02058 activity raises ASB4's level | lines that do not express LINC02058 (34) vs lines expressing it (16) | 2.75× lower at baseline in the lines without LINC02058 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC02253, ENSG00000260573, ST18; maybe low, not absent; co-absent with the target |
| [[LGR5]] | C | LGR5 activity raises ASB4's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 3.20× lower at baseline in the lines without LGR5 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573; co-absent with the target |
| [[TFF3]] | C | TFF3 activity raises ASB4's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 2.33× lower at baseline in the lines without TFF3 | 0.062 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[AXIN2]] | C | AXIN2 activity raises ASB4's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 2.82× lower at baseline in the lines without AXIN2 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964; co-absent with the target |
| [[PDE3B]] | C | PDE3B activity raises ASB4's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 2.05× lower at baseline in the lines without PDE3B | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4; co-absent with the target |
| [[NKD1]] | C | NKD1 activity raises ASB4's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 2.78× lower at baseline in the lines without NKD1 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDK4-AS1]] | B | ASB4 activity raises PDK4-AS1's level | lines that do not express ASB4 (31) vs lines expressing it (19) | 2.47× lower at baseline in the lines without ASB4 | 0.001 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D |
| [[PDE4D]] | B | ASB4 activity raises PDE4D's level | lines that do not express ASB4 (31) vs lines expressing it (19) | 2.74× lower at baseline in the lines without ASB4 | 0.018 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D |
| [[NDUFA4L2]] | B | ASB4 activity raises NDUFA4L2's level | lines that do not express ASB4 (31) vs lines expressing it (19) | 2.44× lower at baseline in the lines without ASB4 | 0.052 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D |
| [[LRP5]] | B | ASB4 activity raises LRP5's level | lines that do not express ASB4 (31) vs lines expressing it (19) | 2.27× lower at baseline in the lines without ASB4 | 0.067 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D |
| [[MYB]] | B | ASB4 activity raises MYB's level | lines that do not express ASB4 (31) vs lines expressing it (19) | 2.18× lower at baseline in the lines without ASB4 | 0.069 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D |
| [[EPM2A]] | B | ASB4 activity raises EPM2A's level | lines that do not express ASB4 (31) vs lines expressing it (19) | 1.49× lower at baseline in the lines without ASB4 | 0.072 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D |
| [[LRP5]] | B | ASB4 activity strengthens LRP5's drug response | lines that do not express ASB4 (26) vs lines expressing it (17) | the lines without ASB4 respond 0.67× as strongly (z diff +2.04); strongest at Belinostat 5 µM: 0.43x vs 0.24x (z diff +2.7) | 0.085 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D; target measured in part of the lines; artifact flags |
| [[CCDC162P]] | B | ASB4 activity raises CCDC162P's level | lines that do not express ASB4 (31) vs lines expressing it (19) | 1.97× lower at baseline in the lines without ASB4 | 0.098 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D |
| [[PDE3B]] | C | ASB4 activity raises PDE3B's level | lines that do not express ASB4 (31) vs lines expressing it (19) | 3.08× lower at baseline in the lines without ASB4 | 0.010 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D; co-absent with the target |
| [[GLDN]] | C | ASB4 activity raises GLDN's level | lines that do not express ASB4 (31) vs lines expressing it (19) | 2.50× lower at baseline in the lines without ASB4 | 0.043 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D; co-absent with the target |
| [[MIR4713HG]] | C | ASB4 activity raises MIR4713HG's level | lines that do not express ASB4 (31) vs lines expressing it (19) | 3.94× lower at baseline in the lines without ASB4 | 0.044 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D; co-absent with the target |
| [[PROX1-AS1]] | C | ASB4 activity raises PROX1-AS1's level | lines that do not express ASB4 (31) vs lines expressing it (19) | 2.27× lower at baseline in the lines without ASB4 | 0.070 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.635). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.7, 45.6); signed map (62.5, 13.9). **Vector** length 42.0, 9.30% of its response variance represented; |z| ≥ 3 in 495 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +12.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +9.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.6 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +1.9 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -4.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.4 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and SOCS box containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3 — chr7:95,478,444-95,540,233 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ASB-4 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y574](https://www.uniprot.org/uniprotkb/Q9Y574) (Ankyrin repeat and SOCS box protein 4):

> Probable substrate-recognition component of a SCF-like ECS (Elongin-Cullin-SOCS-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Promotes differentiation and maturation of the vascular lineage by an oxygen-dependent mechanism (By similarity). Also acts as a negative regulator of GPS1, a component of the COP9 signalosome (CSN) multiprotein complex, thereby inhibiting the serine phosphorylation of IRS1 …

**Summary**, from NCBI Gene [51666](https://www.ncbi.nlm.nih.gov/gene/51666):

> The protein encoded by this gene is a member of the ankyrin repeat and SOCS box-containing (ASB) family of proteins. They contain ankyrin repeat sequence and SOCS box domain. The SOCS box serves to couple suppressor of cytokine signalling (SOCS) proteins and their binding partners with the elongin B and C complex, possibly targeting them for degradation. Multiple alternatively spliced transcript variants have been described for this gene but some of the full length sequences are not known. …

**Accessions** — [HGNC:16009](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16009) · Entrez [51666](https://www.ncbi.nlm.nih.gov/gene/51666) · UniProt [Q9Y574](https://www.uniprot.org/uniprotkb/Q9Y574) · Ensembl [ENSG00000005981](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005981)

## Data

Gene col 95: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 95); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 95, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 95]; `tensor/DDL_lfc|DDL_z.npy` [95]; `embed/gene_vectors.npy` [95]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 95 or target_col == 95). Every well: [[ASB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
