---
symbol: "SLC23A3"
type: "gene"
col: 13144
ensembl_id: "ENSG00000213901"
name: "solute carrier family 23 member 3"
location: "2q35"
module: 38
arm: "+"
pooled_cpm: 4.73
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# SLC23A3

*solute carrier family 23 member 3* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.64× (z +12.5, q 3e-33, up in 38 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.459× (z -7.1, q 8e-10, down in 30 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.603× (z -4.6, q 8e-04, down in 17 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[QRICH2]] (+0.73, fdr 7e-06), [[LINC02936]] (+0.72, fdr 7e-06), [[SLC22A20P]] (+0.71, fdr 7e-06); moves opposite to [[TRAPPC11]] (-0.63, fdr 9e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13144.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +12.5 | 3e-33 | 38/39 (C32, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +5.5 | 1e-05 | 4/7 (NCI-H2347, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.81×** | +5.4 | 1e-05 | 20/44 (LoVo, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +4.7 | 4e-04 | 3/13 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.60×** | +4.3 | 0.002 | 12/47 (C32, AsPC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.2 | 0.002 | 14/47 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.0 | 0.005 | 14/36 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.012 | 9/45 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.041 | 7/45 (SW48, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.061 | 10/41 (CFPAC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.40× | +3.1 | 0.11 | 6/40 (NCI-H460, NCI-H2030, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13144.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.459×** | -7.1 | 8e-10 | 30/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.597×** | -4.7 | 8e-04 | 19/45 (HCT15, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.603×** | -4.6 | 8e-04 | 17/45 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.637×** | -4.1 | 0.006 | 13/46 (NCI-H1573, BT-474, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.632×** | -4.0 | 0.008 | 19/44 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.650×** | -3.9 | 0.009 | 17/37 (HCT15, HepG2/C3A, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.667×** | -3.5 | 0.038 | 8/45 (LS 180, NCI-H1573, …) | top dose only | plate-row cell shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.692×** | -3.3 | 0.060 | 12/45 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.684×** | -3.3 | 0.064 | 8/45 (A549, C32, …) | top dose only | plate-row cell shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.777×** | -3.2 | 0.071 | 15/45 (LoVo, HT-29, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.706×** | -3.2 | 0.081 | 17/46 (NCI-H1792, LoVo, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.524× | -3.1 | 0.10 | 13/42 (BT-474, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | 0.530× | -3.0 | 0.11 | 6/41 (SW480, A549, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13144. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 7.80 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0486× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~93% of this change |
| [[PANC-1 (line)]] | alt | 4.46 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0969× (z -10.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 2.45 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.5 µM 0.0744× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 3.72 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0498× (z -8.7) ⚠ cell-cycle shift, explains ~46% of this change |
| [[C32 (line)]] | wt | 7.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.22× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 5.04 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 7.61 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0757× (z -8.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HEC-1-A (line)]] | alt | 8.64 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -9.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 3.37 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0806× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 4.64 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.69× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 2.36 | 0 | 1 (1 ⚠) | — | [[Rimonabant (Hydrochloride) (drug)]] 0.05 µM 0.0612× (z -9.0) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 5.75 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0720× (z -8.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SW480 (line)]] | alt | 5.24 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.173× (z -9.0) |
| [[A-172 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13144), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QRICH2]] | +0.73 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.72 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[SLC22A20P]] | +0.71 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[LINC01588]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.71 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[SMBD1P]] | +0.69 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[AVIL]] | +0.69 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[TMEM236]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[CLDN15]] | +0.69 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[ANKDD1B]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[CCDC62]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[MUC20-OT1]] | +0.67 | +0.59 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC11]] | -0.63 | -0.57 / -0.63 | both halves | 9e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC23A3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.5, -16.2); signed map (12.5, 9.6). **Vector** length 72.5, 11.7% of its response variance represented; |z| ≥ 3 in 1,135 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.2 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +12.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +4.3 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +1.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -3.0 | -4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -0.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -0.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.9 | -1.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.8 | -3.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 23 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,161,465-219,170,095 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SVCT3, FLJ31168, Yspl1 |
| Gene groups (HGNC) | Solute carrier family 23 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PIS1](https://www.uniprot.org/uniprotkb/Q6PIS1) (Solute carrier family 23 member 3):

> Acts as a sodium-dependent hypoxanthine transporter. May show xanthine-hypoxanthine exchange activity.

**Summary**, from NCBI Gene [151295](https://www.ncbi.nlm.nih.gov/gene/151295):

> Predicted to enable transmembrane transporter activity. Involved in hypoxanthine transport. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20601](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20601) · Entrez [151295](https://www.ncbi.nlm.nih.gov/gene/151295) · UniProt [Q6PIS1](https://www.uniprot.org/uniprotkb/Q6PIS1) · Ensembl [ENSG00000213901](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213901)

## Data

Gene col 13144: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13144); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13144, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13144]; `tensor/DDL_lfc|DDL_z.npy` [13144]; `embed/gene_vectors.npy` [13144]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13144 or target_col == 13144). Every well: [[SLC23A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC23A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
