---
symbol: "MIR2052HG"
type: "gene"
col: 14868
ensembl_id: "ENSG00000254349"
name: "MIR2052 host gene"
location: "8q21.11-q21.13"
module: 27
arm: "+"
pooled_cpm: 11.86
n_lines_expressing: 23
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 18
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 21
direction_downstream: 17
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# MIR2052HG

*MIR2052 host gene* — 8q21.11-q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.24× (z +12.0, q 2e-30, up in 9 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.571× (z -5.9, q 2e-06, down in 15 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01905]] (+0.72, fdr 7e-06), [[SLCO6A1]] (+0.69, fdr 7e-06), [[GABRG2]] (+0.68, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[NELL2]] → it (grade B ⚠); 17 go from it, the strongest it → [[GRIK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14868.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.24×** | +12.0 | 2e-30 | 9/18 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.13×** | +12.0 | 2e-30 | 2/11 (LOX-IMVI, C32) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +9.1 | 1e-17 | 1/9 (LOX-IMVI) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +8.3 | 1e-14 | 4/11 (C32, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +7.3 | 4e-11 | 3/17 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +6.9 | 5e-10 | 5/16 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.79×** | +5.8 | 4e-07 | 9/17 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +5.7 | 1e-06 | 9/20 (LOX-IMVI, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +5.4 | 3e-06 | 3/17 (SK-MEL-2, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.002 | 5/19 (A-172, BT-474, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +4.0 | 0.003 | 3/19 (SW48, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.46×** | +4.0 | 0.003 | 5/19 (LOX-IMVI, A-427, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.013 | 7/18 (SW480, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.015 | 5/20 (SW480, LOX-IMVI, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.015 | 2/21 (hTERT-HPNE, A-172) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.028 | 4/19 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.042 | 1/18 (SW480) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.065 | 6/20 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14868.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.571×** | -5.9 | 2e-06 | 15/18 (SW480, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.685×** | -4.0 | 0.016 | 11/19 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.687×** | -3.9 | 0.016 | 13/20 (SW480, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.710×** | -3.6 | 0.045 | 11/19 (SHP-77, NCI-H1573, …) | top dose only |  |
| [[Auranofin (drug)]] 0.5 µM |  | **0.726×** | -3.4 | 0.085 | 5/18 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.729×** | -3.3 | 0.085 | 13/18 (SHP-77, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.736×** | -3.2 | 0.091 | 12/20 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.736×** | -3.2 | 0.091 | 9/18 (SW480, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.811× | -3.1 | 0.11 | 3/19 (HEC-1-A, SW480, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 5 µM |  | 0.735× | -3.1 | 0.11 | 1/18 (hTERT-HPNE) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14868. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 70.9 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.288× (z -10.7) |
| [[SW480 (line)]] | alt | 30.5 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.193× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 43.8 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -13.2) |
| [[SHP-77 (line)]] | alt | 193 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -9.4) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A-427 (line)]] | wt | 14.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0957× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 37.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0396× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -12.0) |
| [[C32 (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0513× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 9.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.33× (z +11.5) | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 9.97 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0792× (z -8.7) |
| [[A-172 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14868), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01905]] | +0.72 | +0.63 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[SLCO6A1]] | +0.69 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[GABRG2]] | +0.68 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[MGAT4C]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[ARHGAP25]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[STPG2]] | +0.64 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[LINC00491]] | +0.64 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[KCNMB2-AS1]] | +0.63 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[LINC00648]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[AGBL4]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[POU6F2]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[LINC01456]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 3, C 18. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NELL2]] | B | NELL2 activity raises MIR2052HG's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 2.39× lower at baseline in the lines without NELL2 | 0.056 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises MIR2052HG's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers MIR2052HG's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[PI15]] | C | PI15 activity raises MIR2052HG's level | lines that do not express PI15 (36) vs lines expressing it (14) | 5.80× lower at baseline in the lines without PI15 | 6e-04 | ⚠ within organs, on part of the lines; also absent: LINC02566, ENSG00000275016, ASCL1; co-absent with the target |
| [[BRINP3]] | C | BRINP3 activity raises MIR2052HG's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 3.61× lower at baseline in the lines without BRINP3 | 0.004 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent; co-absent with the target |
| [[FUT9]] | C | FUT9 activity raises MIR2052HG's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 4.13× lower at baseline in the lines without FUT9 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[FAR2P1]] | C | FAR2P1 activity raises MIR2052HG's level | lines that do not express FAR2P1 (29) vs lines expressing it (21) | 2.59× lower at baseline in the lines without FAR2P1 | 0.017 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity raises MIR2052HG's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 3.16× lower at baseline in the lines without CSMD3 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[ERBB4]] | C | ERBB4 activity raises MIR2052HG's level | lines that do not express ERBB4 (33) vs lines expressing it (17) | 3.24× lower at baseline in the lines without ERBB4 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, NETO1, CDH10; co-absent with the target |
| [[MIR4500HG]] | C | MIR4500HG activity raises MIR2052HG's level | lines that do not express MIR4500HG (29) vs lines expressing it (21) | 2.88× lower at baseline in the lines without MIR4500HG | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000272046, BMP5, SNCA; co-absent with the target |
| [[LINC02050]] | C | LINC02050 activity raises MIR2052HG's level | lines that do not express LINC02050 (37) vs lines expressing it (13) | 3.55× lower at baseline in the lines without LINC02050 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000286329, ENSG00000242828, PASD1; co-absent with the target |
| [[RIMS2]] | C | RIMS2 activity raises MIR2052HG's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 3.10× lower at baseline in the lines without RIMS2 | 0.023 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 7, C 10. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIK2]] | B | MIR2052HG activity raises GRIK2's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 2.67× lower at baseline in the lines without MIR2052HG | 0.009 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent |
| [[ELAPOR2]] | B | MIR2052HG activity raises ELAPOR2's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 3.02× lower at baseline in the lines without MIR2052HG | 0.048 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent |
| [[BCL11A]] | B | MIR2052HG activity raises BCL11A's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 2.14× lower at baseline in the lines without MIR2052HG | 0.062 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent |
| [[KIF6]] | B | MIR2052HG activity raises KIF6's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 1.54× lower at baseline in the lines without MIR2052HG | 0.068 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent |
| [[KCNMB2-AS1]] | B | MIR2052HG activity raises KCNMB2-AS1's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 2.04× lower at baseline in the lines without MIR2052HG | 0.072 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent |
| [[NELL2]] | B | MIR2052HG activity raises NELL2's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 2.35× lower at baseline in the lines without MIR2052HG | 0.081 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent |
| [[DACH1]] | B | MIR2052HG activity raises DACH1's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 1.70× lower at baseline in the lines without MIR2052HG | 0.097 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent |
| [[RIMS2]] | C | MIR2052HG activity raises RIMS2's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 3.95× lower at baseline in the lines without MIR2052HG | 0.002 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent; co-absent with the target |
| [[ERBB4]] | C | MIR2052HG activity raises ERBB4's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 3.88× lower at baseline in the lines without MIR2052HG | 0.018 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent; co-absent with the target |
| [[MGAT4C]] | C | MIR2052HG activity raises MGAT4C's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 3.30× lower at baseline in the lines without MIR2052HG | 0.027 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent; co-absent with the target |
| [[CSMD3]] | C | MIR2052HG activity raises CSMD3's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 2.44× lower at baseline in the lines without MIR2052HG | 0.039 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent; co-absent with the target |
| [[PI15]] | C | MIR2052HG activity raises PI15's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 2.41× lower at baseline in the lines without MIR2052HG | 0.060 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.493). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.3, 40.2); signed map (48.5, 34.8). **Vector** length 59.8, 17.8% of its response variance represented; |z| ≥ 3 in 490 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +12.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +1.4 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.0 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -5.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -1.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -1.6 | -3.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -1.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | MIR2052 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q21.11-q21.13 — chr8:74,599,775-74,823,313 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51555](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51555) · Entrez [441355](https://www.ncbi.nlm.nih.gov/gene/441355) · Ensembl [ENSG00000254349](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254349)

## Data

Gene col 14868: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14868); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14868, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14868]; `tensor/DDL_lfc|DDL_z.npy` [14868]; `embed/gene_vectors.npy` [14868]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14868 or target_col == 14868). Every well: [[MIR2052HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR2052HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
