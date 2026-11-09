---
symbol: "HASPIN"
type: "gene"
col: 10839
ensembl_id: "ENSG00000177602"
name: "histone H3 associated protein kinase"
location: "17p13.2"
module: 22
arm: "+"
pooled_cpm: 3.1
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# HASPIN

*histone H3 associated protein kinase* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +7.3, q 1e-10, up in 16 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[palbociclib (drug)]] 0.5 µM: 0.548× (z -3.8, q 0.094, down in 8 of 45 measured lines) ⚠ cell-cycle shift, explains ~43% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (PANC-1 0.103×); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 1 line (A-172 0.0419×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0818×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUV39H1]] (+0.80, fdr 7e-06), [[TMPO]] (+0.79, fdr 7e-06), [[KIF11]] (+0.78, fdr 7e-06); moves opposite to [[KIZ-AS1]] (-0.65, fdr 7e-06, ⚠ KIZ-AS1 in the vector space only through flagged drug-doses).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10839.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +7.3 | 1e-10 | 16/31 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.18×** | +6.3 | 7e-08 | 3/5 (SW480, NCI-H460, …) | inconsistent across doses | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.04×** | +6.0 | 4e-07 | 21/42 (SW480, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.93×** | +5.7 | 1e-06 | 14/43 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +5.7 | 1e-06 | 12/44 (SW480, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.84×** | +5.3 | 9e-06 | 8/20 (HT-29, LoVo, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.39×** | +4.1 | 0.004 | 11/34 (A549, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.54×** | +3.8 | 0.010 | 5/43 (A549, A-172, …) | top dose only | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.49×** | +3.5 | 0.034 | 9/44 (A498, LoVo, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.48×** | +3.4 | 0.039 | 3/46 (A549, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.30×** | +3.2 | 0.065 | 5/43 (LoVo, PANC-1, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.45×** | +3.1 | 0.086 | 7/35 (NCI-H23, HCT15, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.97×** | +3.1 | 0.086 | 0/8 | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.95×** | +3.1 | 0.089 | 5/39 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10839.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (PANC-1 0.103×); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 1 line (A-172 0.0419×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0818×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.548×** | -3.8 | 0.094 | 8/45 (C32, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.760× | -3.4 | 0.18 | 10/41 (SK-MEL-2, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 0.686× | -3.3 | 0.18 | 14/36 (LoVo, LS 180, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.704× | -3.1 | 0.30 | 9/45 (BT-474, SNU-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10839. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.60 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0419× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 3.71 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0818× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 2.88 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.103× (z -10.1) |
| [[A-427 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.516 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.842 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.812 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.988 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10839), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUV39H1]] | +0.80 | +0.79 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[TMPO]] | +0.79 | +0.77 / +0.79 | both halves | 7e-06 |  |
| [[KIF11]] | +0.78 | +0.78 / +0.79 | both halves | 7e-06 | STRING 521 |
| [[ERCC6L]] | +0.78 | +0.75 / +0.79 | both halves | 7e-06 | STRING 441 |
| [[ZNF724]] | +0.77 | +0.69 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[ZWINT]] | +0.77 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[CENPH]] | +0.77 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[ESCO2]] | +0.76 | +0.74 / +0.75 | both halves | 7e-06 | STRING 632 |
| [[FOXM1]] | +0.76 | +0.71 / +0.80 | both halves | 7e-06 | STRING 421 |
| [[PLK4]] | +0.76 | +0.68 / +0.80 | both halves | 7e-06 | STRING 439 |
| [[E2F8]] | +0.75 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[NCAPG]] | +0.75 | +0.76 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIZ-AS1]] ⚠ | -0.65 | -0.60 / -0.59 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises HASPIN's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.07× lower at baseline in the lines without CDC25A | 0.037 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises HASPIN's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.84× lower at baseline in the lines without TCF19 | 0.053 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises HASPIN's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.10× lower at baseline in the lines without AURKB | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[SPDL1]] | C | SPDL1 activity raises HASPIN's level | lines that do not express SPDL1 (3) vs lines expressing it (47) | 2.03× lower at baseline in the lines without SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |
| [[MCM10]] | C | MCM10 activity raises HASPIN's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without MCM10 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.676). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.1, -47.0); signed map (-44.6, -46.2). **Vector** length 64.5, 10.6% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.56 to 60); *DREAM G2/M down* (control, mean cos +0.58 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.53 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | +2.9 | +5.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.9 | +5.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.8 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +7.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.0 | +3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +2.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +1.3 | +2.2 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +1.3 | +2.4 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -3.0 | -3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -2.3 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | -2.0 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.7 | -2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | -1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -0.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | histone H3 associated protein kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:3,723,903-3,726,699 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GSG2 |
| Gene groups (HGNC) | Histone H3 associated protein kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TF76](https://www.uniprot.org/uniprotkb/Q8TF76) (Serine/threonine-protein kinase haspin):

> Serine/threonine-protein kinase that phosphorylates histone H3 at 'Thr-3' (H3T3ph) during mitosis. May act through H3T3ph to both position and modulate activation of AURKB and other components of the chromosomal passenger complex (CPC) at centromeres to ensure proper chromatid cohesion, metaphase alignment and normal progression through the cell cycle.

**Summary**, from NCBI Gene [83903](https://www.ncbi.nlm.nih.gov/gene/83903):

> Enables ATP binding activity and histone H3T3 kinase activity. Involved in several processes, including mitotic sister chromatid cohesion; mitotic spindle assembly checkpoint signaling; and protein localization to chromosome, centromeric region. Located in centrosome; nucleoplasm; and spindle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19682](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19682) · Entrez [83903](https://www.ncbi.nlm.nih.gov/gene/83903) · UniProt [Q8TF76](https://www.uniprot.org/uniprotkb/Q8TF76) · Ensembl [ENSG00000177602](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177602)

## Data

Gene col 10839: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10839); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10839, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10839]; `tensor/DDL_lfc|DDL_z.npy` [10839]; `embed/gene_vectors.npy` [10839]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10839 or target_col == 10839). Every well: [[HASPIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HASPIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
