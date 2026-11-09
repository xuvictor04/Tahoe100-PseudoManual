---
symbol: "SLC16A4-AS1"
type: "gene"
col: 15783
ensembl_id: "ENSG00000273373"
name: ""
location: ""
module: 15
arm: "+"
pooled_cpm: 2.59
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# SLC16A4-AS1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.17× (z +9.3, q 5e-18, up in 21 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.616× (z -4.1, q 0.021, down in 9 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMTOR5-AS1]] (+0.85, fdr 7e-06), [[SNHG10]] (+0.65, fdr 1e-05), [[LINC00115]] (+0.61, fdr 1e-05); moves opposite to [[H3-3B]] (-0.59, fdr 2e-05), [[SNAPIN]] (-0.55, fdr 5e-05), [[ALAS1]] (-0.55, fdr 2e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HOXB6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15783.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +9.3 | 5e-18 | 21/32 (PANC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.72×** | +8.5 | 5e-15 | 24/40 (SK-MEL-2, NCI-H23, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.69×** | +8.4 | 6e-15 | 27/45 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.67×** | +8.3 | 1e-14 | 20/25 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +7.8 | 6e-13 | 1/2 (J82) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +7.0 | 2e-10 | 1/3 (PANC-1) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.23×** | +6.8 | 6e-10 | 20/42 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +6.6 | 4e-09 | 12/21 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.18×** | +6.4 | 1e-08 | 21/38 (PANC-1, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.09×** | +6.3 | 2e-08 | 19/37 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.61×** | +5.7 | 6e-07 | 15/26 (A-172, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.87×** | +5.3 | 5e-06 | 14/37 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +4.2 | 0.001 | 5/12 (MIA PaCa-2, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.64×** | +4.2 | 0.001 | 10/46 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.62×** | +4.1 | 0.002 | 5/24 (LoVo, HEC-1-A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.006 | 10/33 (HCT15, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +3.7 | 0.006 | 8/43 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.57×** | +3.6 | 0.009 | 5/42 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.042 | 4/44 (SNU-423, RPMI-7951, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM |  | **1.28×** | +2.9 | 0.081 | 5/45 (Hs 766T, J82, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15783.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.616×** | -4.1 | 0.021 | 9/44 (SW48, SK-MEL-2, …) | inconsistent across doses |  |
| [[Drospirenone (drug)]] 0.05 µM |  | **0.652×** | -3.6 | 0.075 | 9/43 (C-33 A, RPMI-7951, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 0.681× | -3.3 | 0.20 | 4/43 (hTERT-HPNE, A498, …) | top dose only | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | 0.679× | -3.1 | 0.31 | 7/42 (HepG2/C3A, PANC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15783. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.766 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.844 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.822 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.807 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.881 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15783), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMTOR5-AS1]] | +0.85 | +0.79 / +0.84 | both halves | 7e-06 |  |
| [[SNHG10]] | +0.65 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[LINC00115]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[RBBP4]] | +0.60 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[DIDO1]] | +0.59 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[HSPE1-MOB4]] | +0.59 | +0.39 / +0.68 | both halves | 5e-05 |  |
| [[DYNLT2]] | +0.59 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[ANKRD10]] | +0.59 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[ZNF718]] | +0.58 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[GARS1-DT]] | +0.57 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[GOT1-DT]] | +0.57 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[MED28]] | +0.56 | +0.48 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H3-3B]] | -0.59 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[SNAPIN]] | -0.55 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[ALAS1]] | -0.55 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[STK17A]] | -0.55 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[BCL10]] | -0.54 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[CEP290]] | -0.54 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ZNF699]] | -0.54 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[GALE]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ZNF414]] | -0.53 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[POLD4]] | -0.52 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[ZNF674]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[KYAT3]] | -0.52 | -0.37 / -0.47 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXB6]] | B | HOXB6 activity lowers SLC16A4-AS1's level | lines that do not express HOXB6 (11) vs lines expressing it (39) | 1.39× higher at baseline in the lines without HOXB6 | 0.078 | ⚠ within organs, on part of the lines; co-absent genes; also absent: HOXB3, HOXB8 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.530). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-5.2, 23.2); signed map (32.3, -17.7). **Vector** length 47.5, 5.67% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.8 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +7.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +3.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -4.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.2 | -2.7 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -2.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -3.1 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.0 | -2.2 |

## What is on record

> [!warning] No registry record
> SLC16A4-AS1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 15783: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15783); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15783, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15783]; `tensor/DDL_lfc|DDL_z.npy` [15783]; `embed/gene_vectors.npy` [15783]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15783 or target_col == 15783). Every well: [[SLC16A4-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC16A4-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
