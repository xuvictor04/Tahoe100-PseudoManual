---
symbol: "SLC51A"
type: "gene"
col: 8823
ensembl_id: "ENSG00000163959"
name: "solute carrier family 51 member A"
location: "3q29"
module: 21
arm: "+"
pooled_cpm: 2.44
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SLC51A

*solute carrier family 51 member A* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.19× (z +12.3, q 3e-32, up in 4 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +7.9, q 5e-13, up in 15 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM: 0.667× (z -4.1, q 0.028, down in 5 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0657×; ⚠ cell-cycle shift, explains ~35% of this change); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0886×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZRANB2-AS1]] (+0.76, fdr 7e-06), [[RN7SL2]] (+0.74, fdr 7e-06), [[SLC13A4]] (+0.72, fdr 1e-05); moves opposite to [[VMA21]] (-0.65, fdr 8e-06), [[ALG10]] (-0.63, fdr 1e-05), [[MTHFD1]] (-0.56, fdr 5e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SPATA21]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8823.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.19×** | +12.3 | 3e-32 | 4/12 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.31×** | +12.2 | 5e-32 | 2/5 (NCI-H2347, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.73×** | +9.9 | 1e-20 | 1/6 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +7.9 | 5e-13 | 15/31 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.84×** | +6.5 | 1e-08 | 3/11 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.81×** | +6.3 | 3e-08 | 13/43 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.69×** | +5.5 | 2e-06 | 18/40 (SW480, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +5.0 | 3e-05 | 11/37 (A-172, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.29×** | +3.8 | 0.008 | 6/34 (C32, NCI-H460, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.008 | 4/35 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.022 | 6/45 (Panc 03.27, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.4 | 0.030 | 6/41 (A-172, COLO 205, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.3 | 0.038 | 3/12 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.041 | 2/28 (LOX-IMVI, Panc 03.27) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.041 | 5/39 (A-172, LoVo, …) | top dose only |  |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.052 | 2/25 (HT-29, HEC-1-A) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8823.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0657×; ⚠ cell-cycle shift, explains ~35% of this change); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0886×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM |  | **0.667×** | -4.1 | 0.028 | 5/38 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -3.4 | 0.23 | 14/47 (HOP62, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8823. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0657× (z -10.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H2347 (line)]] | alt | 2.21 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0886× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8823), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZRANB2-AS1]] | +0.76 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[RN7SL2]] | +0.74 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[SLC13A4]] | +0.72 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[PP2D1]] | +0.70 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[VPS39-DT]] | +0.69 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[GCNT7]] | +0.69 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[RHOQ-AS1]] | +0.69 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[RETREG1-AS1]] | +0.69 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[PKD2L2]] | +0.69 | +0.55 / +0.78 | both halves | 1e-05 |  |
| [[TTC36-AS1]] | +0.68 | +0.48 / +0.76 | both halves | 2e-05 |  |
| [[SLC23A1]] | +0.68 | +0.52 / +0.76 | both halves | 1e-05 |  |
| [[UBOX5-AS1]] | +0.68 | +0.56 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.65 | -0.58 / -0.62 | both halves | 8e-06 |  |
| [[ALG10]] | -0.63 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[MTHFD1]] | -0.56 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[ICMT]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[SIGMAR1]] | -0.55 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[AKAP11]] | -0.55 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[PRKDC]] | -0.54 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[ATIC]] | -0.54 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[MANEA]] | -0.54 | -0.36 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPATA21]] | C | SPATA21's natural level weakens SLC51A's drug response | SPATA21's natural level across 43 lines (lineage-adjusted; a glimpse) | r -0.74, reverse +0.04; direction clear | 0.013 | ⚠ tissue can mimic it; precision caveat |
| [[ABAT]] | C | ABAT's natural level weakens SLC51A's drug response | ABAT's natural level across 41 lines (lineage-adjusted; a glimpse) | r -0.70, reverse +0.18; direction not clear | 0.054 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.8, 29.2); signed map (34.1, 6.7). **Vector** length 30.0, 2.21% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +12.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.5 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +12.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.3 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +5.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | -0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -3.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -1.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 51 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:196,211,487-196,243,178 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OSTalpha, SLC51A1 |
| Gene groups (HGNC) | SLC51 subunits; Solute carrier family 51 |
| Reactome | 4 pathways, smallest: Recycling of bile acids and salts; Bile acid and bile salt metabolism; Metabolism of steroids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UW1](https://www.uniprot.org/uniprotkb/Q86UW1) (Organic solute transporter subunit alpha):

> Essential component of the OST-alpha/OST-beta complex, a heterotetramer that acts as the intestinal basolateral transporter responsible for bile acid export from enterocytes into portal blood. The OST-alpha/OST-beta complex efficiently transports the major species of bile acids (taurocholate). Taurine conjugates are transported more efficiently across the basolateral membrane than glycine-conjugated bile acids (By similarity). In the complex, SLC51A/OST-alpha adopts a G protein-coupled receptor …

**Summary**, from NCBI Gene [200931](https://www.ncbi.nlm.nih.gov/gene/200931):

> Predicted to enable protein heterodimerization activity; protein homodimerization activity; and transmembrane transporter activity. Involved in bile acid secretion. Located in basolateral plasma membrane. Implicated in progressive familial intrahepatic cholestasis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29955](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29955) · Entrez [200931](https://www.ncbi.nlm.nih.gov/gene/200931) · UniProt [Q86UW1](https://www.uniprot.org/uniprotkb/Q86UW1) · Ensembl [ENSG00000163959](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163959)

## Data

Gene col 8823: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8823); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8823, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8823]; `tensor/DDL_lfc|DDL_z.npy` [8823]; `embed/gene_vectors.npy` [8823]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8823 or target_col == 8823). Every well: [[SLC51A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC51A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
