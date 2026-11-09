---
symbol: "ZKSCAN3"
type: "gene"
col: 12112
ensembl_id: "ENSG00000189298"
name: "zinc finger with KRAB and SCAN domains 3"
location: "6p22.1"
module: 16
arm: "+"
pooled_cpm: 3.25
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZKSCAN3

*zinc finger with KRAB and SCAN domains 3* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.71× (z +4.7, q 0.002, up in 13 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.300× (z -10.6, q 2e-23, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF772]] (+0.66, fdr 7e-06), [[ZSCAN26]] (+0.63, fdr 1e-05), [[ZNF221]] (+0.62, fdr 1e-05); moves opposite to [[ABHD18]] (-0.57, fdr 3e-05), [[PRDX4]] (-0.54, fdr 9e-05), [[HS2ST1]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ZNF606]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12112.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +4.7 | 0.002 | 13/46 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +4.2 | 0.008 | 0/5 | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.37×** | +3.8 | 0.020 | 5/45 (SW480, LOX-IMVI, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +3.8 | 0.020 | 13/43 (A498, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +3.6 | 0.031 | 10/46 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.040 | 10/45 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.052 | 10/45 (KATO III, J82, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.096 | 6/41 (SW480, SNU-423, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.51× | +3.1 | 0.11 | 4/41 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.45× | +3.1 | 0.11 | 5/41 (SW480, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12112.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.300×** | -10.6 | 2e-23 | 39/46 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.336×** | -9.6 | 3e-19 | 29/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.412×** | -7.8 | 1e-12 | 22/31 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.492×** | -6.2 | 6e-08 | 25/42 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.621×** | -4.2 | 0.003 | 16/46 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.611×** | -4.2 | 0.003 | 13/25 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.724×** | -4.0 | 0.004 | 16/43 (SHP-77, SW 900, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.697× | -3.1 | 0.15 | 8/44 (A498, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12112. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.79 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0203× (z -20.2) |
| [[NCI-H460 (line)]] | wt | 3.45 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0495× (z -12.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0675× (z -10.8) |
| [[HOP62 (line)]] | alt | 4.12 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0874× (z -8.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 3.94 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0367× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 5.25 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0685× (z -9.2) |
| [[A-172 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12112), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF772]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 | same gene group |
| [[ZSCAN26]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 | same gene group |
| [[ZNF221]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 | same gene group |
| [[ZNF613]] | +0.62 | +0.58 / +0.57 | both halves | 1e-05 | same gene group |
| [[ZNF780A]] | +0.61 | +0.64 / +0.61 | both halves | 7e-06 | same gene group |
| [[TTC30A]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ASF1A]] | +0.61 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[ZNF691]] | +0.61 | +0.72 / +0.49 | both halves | 1e-05 | same gene group |
| [[C7orf25]] | +0.61 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[BBS10]] | +0.60 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[FANCF]] | +0.59 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[ZFP41]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD18]] | -0.57 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[PRDX4]] | -0.54 | -0.58 / -0.36 | both halves | 9e-05 |  |
| [[HS2ST1]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[TAF5]] | -0.53 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[CERS5]] | -0.52 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[FBXO34]] | -0.52 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[SLC37A3]] | -0.51 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[DDT]] | -0.51 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[NFATC2IP]] | -0.51 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[RELL1]] | -0.51 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[DTX2P1-UPK3BP1-PMS2P11]] | -0.49 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[TSPO]] | -0.49 | -0.53 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF606]] | B | ZNF606 activity raises ZKSCAN3's level | lines that do not express ZNF606 (13) vs lines expressing it (37) | 1.22× lower at baseline in the lines without ZNF606 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, C19orf18, ZNF569 |
| [[ZNF613]] | B | ZNF613 activity raises ZKSCAN3's level | lines that do not express ZNF613 (7) vs lines expressing it (43) | 1.36× lower at baseline in the lines without ZNF613 | 0.058 | ⚠ within organs, on part of the lines; also absent: ZNF850, ENSG00000283201, ZNF571 |
| [[C3orf18]] | B | C3orf18 activity raises ZKSCAN3's level | lines that do not express C3orf18 (10) vs lines expressing it (40) | 1.26× lower at baseline in the lines without C3orf18 | 0.060 | ⚠ within organs, on part of the lines; also absent: TMCC2, SELENOM; maybe low, not absent |
| [[ZNF607]] | B | ZNF607 activity raises ZKSCAN3's level | lines that do not express ZNF607 (7) vs lines expressing it (43) | 1.36× lower at baseline in the lines without ZNF607 | 0.078 | ⚠ within organs, on part of the lines; also absent: ZNF675, ZNF571, ZFP30 |
| [[HDAC6]] | B | HDAC6 activity lowers ZKSCAN3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF391]] | B | ZNF391 activity raises ZKSCAN3's level | lines that do not express ZNF391 (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without ZNF391 | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC00159, ENSG00000283491, ASIC1; maybe low, not absent |
| [[TRIM68]] | C | TRIM68 activity raises ZKSCAN3's level | lines that do not express TRIM68 (3) vs lines expressing it (47) | 1.63× lower at baseline in the lines without TRIM68 | 0.094 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MNS1, ENSG00000283491, AGK; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.640). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-32.5, 10.7); signed map (1.2, -28.5). **Vector** length 44.8, 5.02% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | -0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +3.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -9.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.8 | -6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.5 | -10.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.5 | -7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -0.9 | -1.6 |
|  | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -1.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -0.9 | -1.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -0.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger with KRAB and SCAN domains 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:28,349,947-28,369,172 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Zfp47, ZF47, ZSCAN35; previously ZNF306, ZNF309 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRR0](https://www.uniprot.org/uniprotkb/Q9BRR0) (Zinc finger protein with KRAB and SCAN domains 3):

> Transcriptional factor that binds to the consensus sequence 5'-[GT][AG][AGT]GGGG-3' and acts as a repressor of autophagy. Specifically represses expression of genes involved in autophagy and lysosome biogenesis/function such as MAP1LC3B, ULK1 or WIPI2. Associates with chromatin at the ITGB4 and VEGF promoters. Also acts as a transcription activator and promotes cancer cell progression and/or migration in various tumors and myelomas.

**Summary**, from NCBI Gene [80317](https://www.ncbi.nlm.nih.gov/gene/80317):

> Enables DNA-binding transcription repressor activity, RNA polymerase II-specific; RNA polymerase II cis-regulatory region sequence-specific DNA binding activity; and chromatin binding activity. Involved in several processes, including lysosome organization; negative regulation of cellular senescence; and regulation of DNA-templated transcription. Located in cytoplasm and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13853](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13853) · Entrez [80317](https://www.ncbi.nlm.nih.gov/gene/80317) · UniProt [Q9BRR0](https://www.uniprot.org/uniprotkb/Q9BRR0) · Ensembl [ENSG00000189298](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189298)

## Data

Gene col 12112: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12112); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12112, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12112]; `tensor/DDL_lfc|DDL_z.npy` [12112]; `embed/gene_vectors.npy` [12112]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12112 or target_col == 12112). Every well: [[ZKSCAN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZKSCAN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
