---
symbol: "ASGR1"
type: "gene"
col: 6532
ensembl_id: "ENSG00000141505"
name: "asialoglycoprotein receptor 1"
location: "17p13.1"
module: 53
arm: "+"
pooled_cpm: 4.08
n_lines_expressing: 41
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 27
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# ASGR1

*asialoglycoprotein receptor 1* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.55× (z +11.6, q 2e-28, up in 31 of 39 measured lines) ⚠ position not correctable. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.68× (z +10.7, q 2e-24, up in 23 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 0.567× (z -4.2, q 0.013, down in 13 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLG4]] (+0.76, fdr 7e-06, ⚠ same locus), [[MMP25]] (+0.74, fdr 7e-06), [[ORAI2]] (+0.73, fdr 7e-06), [[CPNE9]] (+0.73, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NEK10]] → it (grade B ⚠); 27 go from it, the strongest it → [[CHRNE]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6532.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.55×** | +11.6 | 2e-28 | 31/39 (SW 900, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.68×** | +10.7 | 2e-24 | 23/28 (C32, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.06×** | +10.4 | 5e-23 | 3/6 (HepG2/C3A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **3.02×** | +8.5 | 2e-15 | 20/33 (A-172, SW480, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.16×** | +8.4 | 7e-15 | 18/30 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.89×** | +7.5 | 4e-12 | 2/7 (SW480, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.44×** | +6.9 | 5e-10 | 4/13 (HepG2/C3A, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +3.2 | 0.083 | 2/18 (HepG2/C3A, A-172) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.50× | +3.1 | 0.12 | 3/31 (SW480, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6532.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.567×** | -4.2 | 0.013 | 13/33 (NCI-H23, HEC-1-A, …) | all doses, flat |  |
| [[Tadalafil (drug)]] 5 µM |  | **0.599×** | -3.8 | 0.031 | 10/31 (A549, SNU-1, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.710×** | -3.8 | 0.031 | 10/36 (HOP62, RKO, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.601×** | -3.7 | 0.031 | 10/37 (NCI-H1573, RKO, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **0.720×** | -3.6 | 0.031 | 13/35 (RKO, J82, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.633×** | -3.6 | 0.035 | 9/37 (A-427, RKO, …) | all doses, flat |  |
| [[Pralsetinib (drug)]] 5 µM |  | 0.454× | -3.2 | 0.11 | 7/16 (NCI-H23, HOP62, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6532. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 14.0 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0584× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0741× (z -11.2) |
| [[A-172 (line)]] | wt | 4.97 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.05 µM 0.0881× (z -9.0) |
| [[A-427 (line)]] | wt | 5.87 | 0 | 1 | — | [[5-Azacytidine (drug)]] 5 µM 0.0499× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 8.71 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0870× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 5.04 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0391× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 1.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.2× (z +12.9) | — |
| [[A498 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.908 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.994 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.995 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 73.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.805 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.569 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.996 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.601 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6532), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLG4]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 | ⚠ same locus (7.6 kb, same strand: neighbours can correlate without regulation) |
| [[MMP25]] | +0.74 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[ORAI2]] | +0.73 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.73 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[HPX]] | +0.73 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[SLC9A5]] | +0.71 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[KIF17]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.70 | +0.65 / +0.80 | both halves | 7e-06 |  |
| [[SLC26A4]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[MYO15A]] | +0.70 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[AZU1]] | +0.70 | +0.69 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEK10]] | B | NEK10 activity raises ASGR1's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 2.42× lower at baseline in the lines without NEK10 | 0.054 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[SLC37A2]] | B | SLC37A2 activity raises ASGR1's level | lines that do not express SLC37A2 (11) vs lines expressing it (39) | 1.59× lower at baseline in the lines without SLC37A2 | 0.062 | ⚠ within organs, on part of the lines; also absent: FAM111B; maybe low, not absent |
| [[MYOM1]] | B | MYOM1 activity raises ASGR1's level | lines that do not express MYOM1 (9) vs lines expressing it (41) | 1.65× lower at baseline in the lines without MYOM1 | 0.067 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC01250]] | B | LINC01250 activity raises ASGR1's level | lines that do not express LINC01250 (10) vs lines expressing it (40) | 1.94× lower at baseline in the lines without LINC01250 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 27, C 0. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHRNE]] | B | ASGR1 activity raises CHRNE's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.90× lower at baseline in the lines without ASGR1 | 0.002 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[DLG4]] | B | ASGR1 activity raises DLG4's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 3.23× lower at baseline in the lines without ASGR1 | 0.004 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[MYO15A]] | B | ASGR1 activity raises MYO15A's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.59× lower at baseline in the lines without ASGR1 | 0.004 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[ORAI2]] | B | ASGR1 activity raises ORAI2's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.55× lower at baseline in the lines without ASGR1 | 0.008 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[PILRA]] | B | ASGR1 activity raises PILRA's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.51× lower at baseline in the lines without ASGR1 | 0.011 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[HCN2]] | B | ASGR1 activity raises HCN2's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 2.02× lower at baseline in the lines without ASGR1 | 0.013 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[SPATA32]] | B | ASGR1 activity raises SPATA32's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.50× lower at baseline in the lines without ASGR1 | 0.025 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[LAG3]] | B | ASGR1 activity raises LAG3's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.87× lower at baseline in the lines without ASGR1 | 0.027 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[PTCH2]] | B | ASGR1 activity raises PTCH2's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.45× lower at baseline in the lines without ASGR1 | 0.029 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[WTIP]] | B | ASGR1 activity raises WTIP's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.94× lower at baseline in the lines without ASGR1 | 0.032 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[SCARF2]] | B | ASGR1 activity raises SCARF2's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.48× lower at baseline in the lines without ASGR1 | 0.037 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[MPP4]] | B | ASGR1 activity raises MPP4's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.80× lower at baseline in the lines without ASGR1 | 0.037 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.762). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.1, -15.3); signed map (16.8, 13.5). **Vector** length 65.8, 12.5% of its response variance represented; |z| ≥ 3 in 835 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.4 | +8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +7.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +1.6 |
| fall | [[Radotinib (drug)]] 5 µM |  | -2.9 | -3.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.0 | -2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | asialoglycoprotein receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,173,431-7,179,564 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLEC4H1 |
| Gene groups (HGNC) | C-type lectin domain containing |
| Reactome | 1 pathways, smallest: Asparagine N-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P07306](https://www.uniprot.org/uniprotkb/P07306) (Asialoglycoprotein receptor 1):

> Transmembrane protein predominantly expressed on hepatocytes that plays a key role in endocytosis of plasma glycoproteins that lack terminal sialic acid residues. Specifically recognizes terminal galactose and N-acetylgalactosamine residues, facilitating the clearance of desialylated glycoproteins from circulation. Plays thereby a role in a variety of physiological processes, such as removal of desialylated platelets, elimination of activated lymphocytes and maintenance of serum glycoprotein …

**Summary**, from NCBI Gene [432](https://www.ncbi.nlm.nih.gov/gene/432):

> This gene encodes a subunit of the asialoglycoprotein receptor. This receptor is a transmembrane protein that plays a critical role in serum glycoprotein homeostasis by mediating the endocytosis and lysosomal degradation of glycoproteins with exposed terminal galactose or N-acetylgalactosamine residues. The asialoglycoprotein receptor may facilitate hepatic infection by multiple viruses including hepatitis B, and is also a target for liver-specific drug delivery. The asialoglycoprotein receptor …

**Accessions** — [HGNC:742](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:742) · Entrez [432](https://www.ncbi.nlm.nih.gov/gene/432) · UniProt [P07306](https://www.uniprot.org/uniprotkb/P07306) · Ensembl [ENSG00000141505](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141505)

## Data

Gene col 6532: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6532); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6532, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6532]; `tensor/DDL_lfc|DDL_z.npy` [6532]; `embed/gene_vectors.npy` [6532]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6532 or target_col == 6532). Every well: [[ASGR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASGR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
