---
symbol: "LSM7"
type: "gene"
col: 5053
ensembl_id: "ENSG00000130332"
name: "LSM7 homolog, U6 small nuclear RNA and mRNA degradation associated"
location: "19p13.3"
module: 58
arm: "+"
pooled_cpm: 20.46
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# LSM7

*LSM7 homolog, U6 small nuclear RNA and mRNA degradation associated* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.18× (z +6.8, q 4e-09, up in 40 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Celecoxib (drug)]] 0.5 µM: 2.06× (z +3.9, q 0.008, up in 32 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.286×); [[Docetaxel (drug)]] 0.05 µM in 1 line (SW 900 0.124×; ⚠ transcription drop; cell-cycle shift, explains ~54% of this change); [[Penfluridol (drug)]] 5 µM in 1 line (BT-474 0.127×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPS9]] (+0.64, fdr 7e-06), [[MAP2K7]] (+0.64, fdr 1e-05), [[POLR2J4]] (+0.63, fdr 1e-05); moves opposite to [[YWHAZ]] (-0.73, fdr 7e-06), [[SPTBN1]] (-0.68, fdr 1e-05), [[EIF4G2]] (-0.60, fdr 1e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EPB41L2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5053.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +6.8 | 4e-09 | 40/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +5.7 | 3e-06 | 38/45 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.76×** | +4.9 | 1e-04 | 31/43 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.74×** | +4.6 | 5e-04 | 21/33 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.69×** | +4.6 | 5e-04 | 28/48 (SW480, LOX-IMVI, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.60×** | +4.1 | 0.003 | 28/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **2.06×** | +3.9 | 0.008 | 32/48 (LS 180, A498, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **2.04×** | +3.8 | 0.009 | 31/47 (SW480, A-427, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.95×** | +3.6 | 0.021 | 28/48 (NCI-H460, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.50×** | +3.4 | 0.033 | 27/46 (NCI-H1573, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.47×** | +3.4 | 0.041 | 20/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.85×** | +3.3 | 0.047 | 23/46 (A-427, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.093 | 20/46 (HOP62, PANC-1, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.76×** | +3.0 | 0.093 | 19/44 (SW480, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5053.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.286×); [[Docetaxel (drug)]] 0.05 µM in 1 line (SW 900 0.124×; ⚠ transcription drop; cell-cycle shift, explains ~54% of this change); [[Penfluridol (drug)]] 5 µM in 1 line (BT-474 0.127×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | 0.672× | -3.5 | 0.26 | 25/48 (A498, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.775× | -3.2 | 0.28 | 19/47 (MIA PaCa-2, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.776× | -3.2 | 0.28 | 21/48 (LS 180, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.708× | -3.1 | 0.32 | 20/47 (SW48, SW 1271, …) | rises with dose | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5053. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 18.0 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.127× (z -9.6) |
| [[RKO (line)]] | wt | 28.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -10.5) |
| [[SW 900 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.124× (z -10.5) ⚠ transcription drop; cell-cycle shift, explains ~54% of this change |
| [[A-172 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5053), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS9]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[MAP2K7]] | +0.64 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[POLR2J4]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ANKS3]] | +0.62 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[NSUN4]] | +0.61 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[DNLZ]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[LUC7L]] | +0.60 | +0.48 / +0.48 | both halves | 2e-05 | STRING 565 |
| [[NDUFS7]] | +0.60 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[TRAPPC4]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ZXDC]] | +0.58 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[NDUFAB1]] | +0.58 | +0.48 / +0.60 | both halves | 2e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[MECR]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAZ]] | -0.73 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[SPTBN1]] | -0.68 | -0.56 / -0.72 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.60 | -0.57 / -0.60 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[YWHAE]] | -0.59 | -0.55 / -0.62 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[TLN1]] | -0.57 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[VPS26A]] | -0.56 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ACAA2]] | -0.55 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[MAPRE1]] | -0.55 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[MYOSLID]] | -0.55 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[ACTR3]] | -0.55 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[HMGN1]] | -0.54 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[PDAP1]] | -0.54 | -0.50 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPB41L2]] | B | EPB41L2 activity raises LSM7's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.30× lower at baseline in the lines without EPB41L2 | 0.081 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.432). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.0, -18.5); signed map (-17.9, -0.4). **Vector** length 60.9, 12.7% of its response variance represented; |z| ≥ 3 in 565 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.6 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +6.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +2.7 | +4.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +1.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.6 | +3.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.5 | +0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +1.0 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.5 | +2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.9 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.0 | -1.0 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -1.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | LSM7 homolog, U6 small nuclear RNA and mRNA degradation associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,321,520-2,328,611 (-) |
| Ensembl biotype | protein_coding |
| Also known as | YNL147W |
| Gene groups (HGNC) | LSm proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 6 pathways, smallest: mRNA decay by 5' to 3' exoribonuclease; Deadenylation-dependent mRNA decay; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UK45](https://www.uniprot.org/uniprotkb/Q9UK45) (U6 snRNA-associated Sm-like protein LSm7):

> Plays a role in pre-mRNA splicing as component of the U4/U6-U5 tri-snRNP complex that is involved in spliceosome assembly, and as component of the precatalytic spliceosome (spliceosome B complex). The heptameric LSM2-8 complex binds specifically to the 3'-terminal U-tract of U6 snRNA.

**Summary**, from NCBI Gene [51690](https://www.ncbi.nlm.nih.gov/gene/51690):

> Sm-like proteins were identified in a variety of organisms based on sequence homology with the Sm protein family (see SNRPD2; MIM 601061). Sm-like proteins contain the Sm sequence motif, which consists of 2 regions separated by a linker of variable length that folds as a loop. The Sm-like proteins are thought to form a stable heteromer present in tri-snRNP particles, which are important for pre-mRNA splicing.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:20470](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20470) · Entrez [51690](https://www.ncbi.nlm.nih.gov/gene/51690) · UniProt [Q9UK45](https://www.uniprot.org/uniprotkb/Q9UK45) · Ensembl [ENSG00000130332](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130332)

## Data

Gene col 5053: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5053); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5053, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5053]; `tensor/DDL_lfc|DDL_z.npy` [5053]; `embed/gene_vectors.npy` [5053]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5053 or target_col == 5053). Every well: [[LSM7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSM7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
