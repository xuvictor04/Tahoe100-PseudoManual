---
symbol: "MGAT2"
type: "gene"
col: 9625
ensembl_id: "ENSG00000168282"
name: "alpha-1,6-mannosyl-glycoprotein 2-beta-N-acetylglucosaminyltransferase"
location: "14q21.3"
module: 7
arm: "+"
pooled_cpm: 7.66
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# MGAT2

*alpha-1,6-mannosyl-glycoprotein 2-beta-N-acetylglucosaminyltransferase* — 14q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +8.7, q 1e-15, up in 34 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.519× (z -7.1, q 9e-10, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM15B]] (+0.66, fdr 7e-06), [[RRAGA]] (+0.64, fdr 1e-05), [[GTF2E1]] (+0.63, fdr 7e-06); moves opposite to [[LRRC75A]] (-0.57, fdr 2e-05), [[SNHG25]] (-0.54, fdr 8e-05), [[SGK3]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9625.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +8.7 | 1e-15 | 34/43 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.62×** | +5.2 | 6e-05 | 19/47 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.61×** | +5.1 | 6e-05 | 20/47 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.8 | 3e-04 | 17/48 (RKO, NCI-H2030, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.50×** | +4.4 | 0.001 | 18/47 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.4 | 0.001 | 9/48 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.007 | 15/42 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.43×** | +3.8 | 0.010 | 18/38 (SW1417, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.37×** | +3.4 | 0.040 | 6/48 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.040 | 7/46 (Panc 03.27, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.38×** | +3.3 | 0.042 | 11/46 (PANC-1, SW1417, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.051 | 9/41 (A-427, SNU-423, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.53×** | +3.2 | 0.051 | 8/43 (LoVo, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.34×** | +3.2 | 0.061 | 5/48 (LS 180, HOP62, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.079 | 11/45 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.32×** | +3.0 | 0.091 | 4/48 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.32×** | +3.0 | 0.091 | 6/46 (A-172, CFPAC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.091 | 12/46 (NCI-H460, NCI-H2030, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9625.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.519×** | -7.1 | 9e-10 | 27/46 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.547×** | -6.5 | 2e-08 | 27/44 (RPMI-7951, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.571×** | -6.0 | 3e-07 | 26/47 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.595×** | -5.4 | 1e-05 | 25/43 (HS-578T, A498, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.619×** | -5.2 | 3e-05 | 22/46 (LoVo, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.684×** | -4.1 | 0.004 | 16/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.702×** | -3.6 | 0.025 | 10/43 (J82, PANC-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.815× | -3.1 | 0.12 | 9/48 (PANC-1, HS-578T, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.750× | -3.1 | 0.12 | 18/48 (NCI-H460, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9625. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 8.10 | 0 | 2 | — | [[Pimozide (drug)]] 0.05 µM 0.0950× (z -8.9) |
| [[HOP62 (line)]] | alt | 8.12 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0447× (z -13.8) ⚠ toxic |
| [[LoVo (line)]] | wt | 9.25 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.187× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 3.58 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0622× (z -9.2) |
| [[PANC-1 (line)]] | alt | 8.68 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[SW1417 (line)]] | alt | 7.03 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0769× (z -10.4) |
| [[A-172 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9625), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM15B]] | +0.66 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[RRAGA]] | +0.64 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[GTF2E1]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[C6orf47]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[MOCS3]] | +0.61 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[CENPBD1P]] | +0.60 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[TMEM115]] | +0.59 | +0.60 / +0.59 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[RNF26]] | +0.59 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[HPS6]] | +0.58 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[CSTF2T]] | +0.58 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[RAB8A]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[C6orf120]] | +0.58 | +0.68 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC75A]] | -0.57 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[SNHG25]] | -0.54 | -0.68 / -0.37 | both halves | 8e-05 |  |
| [[SGK3]] | -0.53 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[RPL37A]] ⚠ | -0.52 | -0.61 / -0.37 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ECI1]] | -0.52 | -0.27 / -0.57 | both halves | 3e-04 |  |
| [[TOMM20]] | -0.52 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[RPS24]] | -0.52 | -0.63 / -0.43 | both halves | 3e-05 | pathway: SARS-CoV-2 Infection |
| [[RPS21]] | -0.51 | -0.70 / -0.38 | both halves | 6e-05 | pathway: SARS-CoV-2 Infection |
| [[RPL36A]] | -0.51 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[RPL38]] | -0.51 | -0.59 / -0.39 | both halves | 6e-05 |  |
| [[PNISR]] | -0.51 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[RPS6]] ⚠ | -0.51 | -0.55 / -0.41 | both halves | 4e-05 | pathway: SARS-CoV-2 Infection; ⚠ in the vector space only through flagged drug-doses |
| [[STAG3L4-1]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[ZBTB47-AS1]] | -0.51 | -0.46 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises MGAT2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.596). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-47.5, 1.3); signed map (-2.3, -28.3). **Vector** length 72.4, 12.4% of its response variance represented; |z| ≥ 3 in 897 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +1.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | +3.7 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +2.9 | +3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +2.7 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +4.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.3 | +3.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +1.8 | +3.0 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +1.7 | +2.3 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.1 | -4.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.1 | -6.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | alpha-1,6-mannosyl-glycoprotein 2-beta-N-acetylglucosaminyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.3 — chr14:49,620,799-49,623,481 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GNT-II |
| Gene groups (HGNC) | Mannosyl-glycoprotein N-acetylglucosaminyltransferases |
| Reactome | 13 pathways, smallest: Reactions specific to the complex N-glycan synthesis pathway; Diseases associated with N-glycosylation of proteins; N-glycan antennae elongation in the medial/trans-Golgi |
| Matched by | ensembl_id |

**Function**, from UniProt [Q10469](https://www.uniprot.org/uniprotkb/Q10469) (Alpha-1,6-mannosyl-glycoprotein 2-beta-N-acetylglucosaminyltransferase):

> Plays an essential role in protein N-glycosylation. Catalyzes the transfer of N-acetylglucosamine (GlcNAc) onto the free terminal mannose moiety in the core structure of the nascent N-linked glycan chain, giving rise to the second branch in complex glycans.

**Summary**, from NCBI Gene [4247](https://www.ncbi.nlm.nih.gov/gene/4247):

> The product of this gene is a Golgi enzyme catalyzing an essential step in the conversion of oligomannose to complex N-glycans. The enzyme has the typical glycosyltransferase domains: a short N-terminal cytoplasmic domain, a hydrophobic non-cleavable signal-anchor domain, and a C-terminal catalytic domain. Mutations in this gene may lead to carbohydrate-deficient glycoprotein syndrome, type II. The coding region of this gene is intronless. Transcript variants with a spliced 5' UTR may exist, …

**Accessions** — [HGNC:7045](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7045) · Entrez [4247](https://www.ncbi.nlm.nih.gov/gene/4247) · UniProt [Q10469](https://www.uniprot.org/uniprotkb/Q10469) · Ensembl [ENSG00000168282](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168282)

## Data

Gene col 9625: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9625); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9625, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9625]; `tensor/DDL_lfc|DDL_z.npy` [9625]; `embed/gene_vectors.npy` [9625]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9625 or target_col == 9625). Every well: [[MGAT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MGAT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
