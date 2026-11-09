---
symbol: "RPL39L"
type: "gene"
col: 8810
ensembl_id: "ENSG00000163923"
name: "ribosomal protein L39 like"
location: "3q27.3"
module: 22
arm: "+"
pooled_cpm: 7.51
n_lines_expressing: 34
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# RPL39L

*ribosomal protein L39 like* — 3q27.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.89× (z +7.6, q 2e-11, up in 17 of 22 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.49× (z +6.7, q 2e-09, up in 14 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.709× (z -4.1, q 0.020, down in 12 of 31 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.491× (z -3.8, q 0.023, down in 9 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ESPL1]] (+0.53, fdr 3e-05), [[HYLS1]] (+0.52, fdr 3e-05), [[SGO1]] (+0.51, fdr 3e-05); moves opposite to [[STRAP]] (-0.45, fdr 1e-04), [[VSIG10L]] (-0.43, fdr 1e-04), [[HSF4]] (-0.40, fdr 1e-04).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); 2 go from it, the strongest it → [[CHAMP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8810.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.89×** | +7.6 | 2e-11 | 17/22 (A498, A-427, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.83×** | +7.2 | 1e-10 | 15/21 (HOP62, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.90×** | +6.8 | 2e-09 | 7/11 (A498, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +6.7 | 2e-09 | 14/31 (PANC-1, NCI-H1573, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.84×** | +6.4 | 2e-08 | 17/30 (PANC-1, A-172, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +5.1 | 3e-05 | 14/29 (BT-474, PANC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.59×** | +4.9 | 1e-04 | 8/18 (A-427, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.45×** | +4.5 | 6e-04 | 11/26 (BT-474, PANC-1, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.55×** | +3.7 | 0.012 | 4/26 (HOP62, NCI-H1792, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.35×** | +3.6 | 0.017 | 9/30 (A-172, HS-578T, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.24×** | +3.6 | 0.017 | 10/32 (CFPAC-1, HOP62, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.32×** | +3.3 | 0.040 | 9/30 (HOP62, NCI-H2030, …) | two highest doses |  |
| [[Imiquimod (maleate) (drug)]] 0.05 µM |  | **1.37×** | +3.3 | 0.043 | 6/29 (SNU-423, C32, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.31×** | +3.2 | 0.058 | 9/31 (BT-474, A-172, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.075 | 6/31 (NCI-H23, SW 900, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8810.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.709×** | -4.1 | 0.020 | 12/31 (A-172, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.704×** | -4.0 | 0.020 | 11/29 (A-172, LS 180, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.491×** | -3.8 | 0.023 | 9/27 (LoVo, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.777×** | -3.8 | 0.024 | 13/31 (HEC-1-A, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.741×** | -3.4 | 0.076 | 9/30 (HEC-1-A, BT-474, …) | inconsistent across doses |  |
| [[Pentagastrin (drug)]] 5 µM |  | **0.820×** | -3.3 | 0.076 | 4/32 (SK-MEL-2, HS-578T, …) | top dose only |  |
| [[Allantoin (drug)]] 0.5 µM |  | 0.768× | -3.2 | 0.13 | 6/29 (CFPAC-1, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8810. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 10.6 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | [[Mozavaptan (drug)]] 0.05 µM 0.0780× (z -10.3) |
| [[A498 (line)]] | wt | 17.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H2347 (line)]] | alt | 7.18 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 14.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.710 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.715 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.698 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.655 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.676 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.697 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.844 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.698 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.619 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8810), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESPL1]] | +0.53 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[HYLS1]] | +0.52 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[SGO1]] | +0.51 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[C18orf54]] | +0.50 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[ZNF700]] | +0.49 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[FAM110A]] | +0.49 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[RHNO1]] | +0.49 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ZNF85]] | +0.49 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[NHLRC2]] | +0.49 | +0.53 / +0.39 | both halves | 6e-05 |  |
| [[SKA3]] | +0.47 | +0.54 / +0.39 | both halves | 6e-05 |  |
| [[SS18]] | +0.47 | +0.46 / +0.38 | both halves | 6e-05 |  |
| [[NUP37]] | +0.47 | +0.51 / +0.44 | both halves | 3e-05 | pathway: Influenza Infection |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRAP]] | -0.45 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[VSIG10L]] | -0.43 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[HSF4]] | -0.40 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[PIP5KL1]] | -0.40 | -0.44 / -0.27 | both halves | 3e-04 |  |
| [[VDAC2]] | -0.40 | -0.31 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises RPL39L's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHAMP1]] | B | RPL39L activity lowers CHAMP1's level | lines that do not express RPL39L (16) vs lines expressing it (34) | 1.50× higher at baseline in the lines without RPL39L | 0.026 | ⚠ within organs, on part of the lines; also absent: ANKRD6, RNF150, EVL |
| [[KBTBD2]] | B | RPL39L activity lowers KBTBD2's level | lines that do not express RPL39L (16) vs lines expressing it (34) | 1.07× higher at baseline in the lines without RPL39L | 0.048 | ⚠ within organs, on part of the lines; also absent: ANKRD6, RNF150, EVL |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.438). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.8, -58.0); signed map (-53.0, -45.7). **Vector** length 50.5, 9.62% of its response variance represented; |z| ≥ 3 in 519 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +3.8 | +6.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.1 | +6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.3 | +3.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | +2.0 | +4.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | +2.0 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.2 | +1.4 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.0 | +1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +2.8 |
|  | [[vincristine (drug)]] 0.05 µM |  | +1.0 | +2.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.3 | -4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | -1.9 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | -3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -3.8 |
|  | [[EX229 (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L39 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.3 — chr3:187,120,948-187,180,908 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RPL39L1 |
| Gene groups (HGNC) | L ribosomal proteins |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EH5](https://www.uniprot.org/uniprotkb/Q96EH5) (Ribosomal protein eL39-like 2):

> Male germ cell-specific component of the ribosome, which is required for the formation of sperm and male fertility. Replaces the RPL39 paralog in the ribosome of male germ cells. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. The male germ cell-specific ribosome displays a ribosomal polypeptide exit tunnel of distinct size and charge states compared with the classical ribosome. It is responsible for regulating the biosynthesis and …

**Summary**, from NCBI Gene [116832](https://www.ncbi.nlm.nih.gov/gene/116832):

> This gene encodes a protein sharing high sequence similarity with ribosomal protein L39. Although the name of this gene has been referred to as 'ribosomal protein L39' in the public databases, its official name is 'ribosomal protein L39-like'. It is not currently known whether the encoded protein is a functional ribosomal protein or whether it has evolved a function that is independent of the ribosome. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17094](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17094) · Entrez [116832](https://www.ncbi.nlm.nih.gov/gene/116832) · UniProt [Q96EH5](https://www.uniprot.org/uniprotkb/Q96EH5) · Ensembl [ENSG00000163923](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163923)

## Data

Gene col 8810: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8810); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8810, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8810]; `tensor/DDL_lfc|DDL_z.npy` [8810]; `embed/gene_vectors.npy` [8810]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8810 or target_col == 8810). Every well: [[RPL39L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL39L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
