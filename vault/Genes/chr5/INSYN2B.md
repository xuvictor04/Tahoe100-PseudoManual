---
symbol: "INSYN2B"
type: "gene"
col: 12919
ensembl_id: "ENSG00000204767"
name: "inhibitory synaptic factor family member 2B"
location: "5q35.1"
module: 13
arm: "+"
pooled_cpm: 9.83
n_lines_expressing: 19
n_dd_up: 8
n_dd_down: 26
n_dd_up_clean: 2
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 58
direction_downstream: 92
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# INSYN2B

*inhibitory synaptic factor family member 2B* — 5q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.19× (z +11.4, q 2e-27, up in 2 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.53× (z +6.2, q 9e-08, up in 4 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.667× (z -5.8, q 4e-06, down in 16 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GDNF]] (+0.75, fdr 7e-06), [[TMEM200A]] (+0.74, fdr 7e-06), [[SAMD3]] (+0.74, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 58 arrows point to it, the strongest [[PRSS23]] → it (grade B ⚠); 92 go from it, the strongest it → [[ITPR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12919.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.19×** | +11.4 | 2e-27 | 2/14 (SW 900, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.77×** | +10.5 | 4e-23 | 0/15 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +6.8 | 2e-09 | 1/14 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +6.2 | 9e-08 | 4/17 (SW 900, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.1 | 0.005 | 2/15 (SW 900, HS-578T) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +3.9 | 0.007 | 0/15 | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +3.9 | 0.007 | 8/16 (SW 900, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.44×** | +3.8 | 0.011 | 9/16 (SW 900, LOX-IMVI, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | 1.52× | +3.1 | 0.14 | 6/15 (SW 900, SNU-423, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, none with an alert; shown: the 15 strongest. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12919.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.667×** | -5.8 | 4e-06 | 16/17 (C32, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.593×** | -5.2 | 7e-05 | 11/17 (J82, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.589×** | -5.0 | 1e-04 | 7/16 (J82, CHP-212, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.634×** | -4.6 | 6e-04 | 10/16 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.653×** | -4.3 | 0.002 | 10/16 (HOP62, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.744×** | -4.2 | 0.002 | 11/17 (NCI-H1792, HOP62, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.456×** | -4.1 | 0.003 | 7/17 (J82, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.688×** | -3.8 | 0.011 | 13/16 (C32, HOP62, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.679×** | -3.8 | 0.011 | 8/16 (J82, SW 900, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.499×** | -3.6 | 0.015 | 8/17 (J82, CHP-212, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.772×** | -3.6 | 0.015 | 4/17 (J82, A549, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.702×** | -3.6 | 0.016 | 13/16 (HOP62, A-172, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.703×** | -3.6 | 0.016 | 6/16 (HOP62, H4, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.706×** | -3.5 | 0.017 | 11/16 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.756×** | -3.5 | 0.017 | 7/17 (A549, J82, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12919. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 25.3 | 0 | 14 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -16.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.117× (z -15.5) |
| [[C32 (line)]] | wt | 34.1 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0303× (z -23.0) |
| [[A-172 (line)]] | wt | 73.2 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -17.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.221× (z -13.5) |
| [[J82 (line)]] | alt | 37.3 | 0 | 8 (2 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0552× (z -14.4) |
| [[H4 (line)]] | wt | 36.2 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0660× (z -10.9) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Dexamethasone (drug)]] 5 µM 0.0740× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 29.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -14.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.153× (z -13.9) |
| [[RPMI-7951 (line)]] | alt | 16.7 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0356× (z -13.6) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.115× (z -12.4) |
| [[SW 900 (line)]] | alt | 13.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0936× (z -16.3) |
| [[CHP-212 (line)]] | wt | 77.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0667× (z -9.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 29.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -9.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.210× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 82.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -15.5) |
| [[SNU-423 (line)]] | alt | 17.5 | 0 | 2 (2 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0485× (z -12.0) ⚠ cell-cycle shift, explains ~17% of this change |
| [[A549 (line)]] | wt | 5.07 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -8.6) |
| [[HS-578T (line)]] | alt | 7.59 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0644× (z -10.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 6.29 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -10.4) |
| [[A-427 (line)]] | wt | 0.580 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.674 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.827 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.883 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.838 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.850 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.775 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.913 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.706 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.706 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.750 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.862 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.801 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.970 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.796 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.915 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.702 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12919), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDNF]] | +0.75 | +0.68 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[TMEM200A]] | +0.74 | +0.69 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[SAMD3]] | +0.74 | +0.64 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[FRMD4A]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[SPOCD1]] | +0.72 | +0.66 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[ITGA11]] | +0.72 | +0.73 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS6]] | +0.71 | +0.65 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[GPR68]] | +0.70 | +0.62 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1L]] | +0.70 | +0.66 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[LINC01411]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[AFF3]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[HS3ST3A1]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*58 arrows, 58 of them with an alert ⚠; grade A 0, B 6, C 52. Shown: the 12 strongest; 46 more arrows (46 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS23]] | B | PRSS23 activity raises INSYN2B's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 2.31× lower at baseline in the lines without PRSS23 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[PATJ]] | B | PATJ activity lowers INSYN2B's level | lines that do not express PATJ (9) vs lines expressing it (41) | 7.50× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[ARL4C]] | B | ARL4C activity raises INSYN2B's level | lines that do not express ARL4C (14) vs lines expressing it (36) | 1.80× lower at baseline in the lines without ARL4C | 0.068 | ⚠ within organs, on part of the lines; also absent: NLRP1, ENSG00000225330, TRPM8 |
| [[NR3C1]] | B | NR3C1 activity lowers INSYN2B's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers INSYN2B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[COL13A1]] | B | COL13A1 activity raises INSYN2B's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 3.23× lower at baseline in the lines without COL13A1 | 0.087 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[FGF5]] | C | FGF5 activity raises INSYN2B's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 7.37× lower at baseline in the lines without FGF5 | 7e-04 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702; co-absent with the target |
| [[TMEM200A]] | C | TMEM200A activity raises INSYN2B's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 5.09× lower at baseline in the lines without TMEM200A | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615; co-absent with the target |
| [[SAMD3]] | C | SAMD3 activity raises INSYN2B's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 4.52× lower at baseline in the lines without SAMD3 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises INSYN2B's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 6.06× lower at baseline in the lines without FRMD4A | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[COL15A1]] | C | COL15A1 activity raises INSYN2B's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 5.82× lower at baseline in the lines without COL15A1 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises INSYN2B's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 5.36× lower at baseline in the lines without COL5A1 | 0.002 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |

### Downstream of this gene

*92 arrows, 92 of them with an alert ⚠; grade A 0, B 18, C 74. Shown: the 12 strongest; 80 more arrows (80 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITPR1]] | B | INSYN2B activity raises ITPR1's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 4.53× lower at baseline in the lines without INSYN2B | 0.005 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[PRSS23]] | B | INSYN2B activity raises PRSS23's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 3.20× lower at baseline in the lines without INSYN2B | 0.009 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[PPFIBP1]] | B | INSYN2B activity raises PPFIBP1's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 1.68× lower at baseline in the lines without INSYN2B | 0.015 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[LINC02454]] | B | INSYN2B activity raises LINC02454's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without INSYN2B | 0.016 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[CD82]] | B | INSYN2B activity raises CD82's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 2.68× lower at baseline in the lines without INSYN2B | 0.016 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[BOC]] | B | INSYN2B activity raises BOC's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 2.38× lower at baseline in the lines without INSYN2B | 0.022 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[ARL4C]] | B | INSYN2B activity raises ARL4C's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 2.15× lower at baseline in the lines without INSYN2B | 0.031 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[EFL1]] | B | INSYN2B activity raises EFL1's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 1.44× lower at baseline in the lines without INSYN2B | 0.035 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[EVC]] | B | INSYN2B activity raises EVC's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 3.54× lower at baseline in the lines without INSYN2B | 0.044 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[PATJ]] | B | INSYN2B activity lowers PATJ's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 3.28× higher at baseline in the lines without INSYN2B | 0.047 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[ENG]] | B | INSYN2B activity raises ENG's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 3.13× lower at baseline in the lines without INSYN2B | 0.047 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[COL13A1]] | B | INSYN2B activity raises COL13A1's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 3.52× lower at baseline in the lines without INSYN2B | 0.052 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.839). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.8, 15.0); signed map (21.0, 47.4). **Vector** length 79.1, 27.5% of its response variance represented; |z| ≥ 3 in 624 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Extracellular matrix organization* (reactome, mean cos +0.51 to 22); *Defective B3GALTL causes PpS* (reactome, mean cos +0.57 to 8); *O-glycosylation of TSR domain-containing proteins* (reactome, mean cos +0.57 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +4.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.5 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +2.2 |
|  | [[Flutamide (drug)]] 5 µM |  | +1.2 | +1.2 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -2.9 | -3.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.6 | -4.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.4 | -3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | inhibitory synaptic factor family member 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.1 — chr5:169,861,303-169,980,495 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C5orf57, FAM196B |
| Matched by | ensembl_id |

UniProt [A6NMK8](https://www.uniprot.org/uniprotkb/A6NMK8) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:37271](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37271) · Entrez [100131897](https://www.ncbi.nlm.nih.gov/gene/100131897) · UniProt [A6NMK8](https://www.uniprot.org/uniprotkb/A6NMK8) · Ensembl [ENSG00000204767](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204767)

## Data

Gene col 12919: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12919); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12919, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12919]; `tensor/DDL_lfc|DDL_z.npy` [12919]; `embed/gene_vectors.npy` [12919]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12919 or target_col == 12919). Every well: [[INSYN2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INSYN2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
