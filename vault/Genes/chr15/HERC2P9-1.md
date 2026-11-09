---
symbol: "HERC2P9-1"
type: "gene"
col: 16573
ensembl_id: "ENSG00000291082"
name: ""
location: ""
module: 36
arm: "+"
pooled_cpm: 2.03
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# HERC2P9-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.66× (z +10.8, q 3e-24, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 2.02× (z +5.8, q 2e-06, up in 14 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.863× (z -4.2, q 0.009, down in 17 of 45 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H460 0.0708×); [[Docetaxel (drug)]] 0.05 µM in 1 line (PANC-1 0.116×; ⚠ transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HERC2]] (+0.78, fdr 7e-06), [[PSMD1]] (+0.71, fdr 7e-06), [[HERC2P9]] (+0.67, fdr 7e-06, ⚠ same locus), [[HERC2P3]] (+0.66, fdr 7e-06); moves opposite to [[KDM5B]] (-0.64, fdr 8e-06), [[HOOK2]] (-0.60, fdr 3e-05), [[KLHL28]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16573.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.66×** | +10.8 | 3e-24 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +6.5 | 2e-08 | 1/2 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.02×** | +5.8 | 2e-06 | 14/34 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.93×** | +5.7 | 2e-06 | 23/45 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.83×** | +5.2 | 2e-05 | 13/40 (COLO 205, PANC-1, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +4.7 | 2e-04 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.68×** | +4.5 | 5e-04 | 12/39 (NCI-H1792, hTERT-HPNE, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +3.9 | 0.008 | 6/43 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.07×** | +3.3 | 0.062 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.42× | +3.0 | 0.14 | 2/43 (SW48, CFPAC-1) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16573.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H460 0.0708×); [[Docetaxel (drug)]] 0.05 µM in 1 line (PANC-1 0.116×; ⚠ transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.863× | -4.2 | 0.009 | 17/45 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.615×** | -4.2 | 0.009 | 13/46 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.670× | -3.3 | 0.15 | 11/39 (J82, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Aprepitant (drug)]] 0.05 µM |  | 0.682× | -3.3 | 0.15 | 9/42 (NCI-H1792, A-427, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.683× | -3.1 | 0.16 | 10/44 (KATO III, RPMI-7951, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | 0.693× | -3.1 | 0.16 | 14/21 (PANC-1, LoVo, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.509× | -3.0 | 0.18 | 7/35 (NCI-H460, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Allopurinol (drug)]] 0.05 µM |  | 0.702× | -3.0 | 0.18 | 6/44 (AsPC-1, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16573. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.84 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0708× (z -10.1) |
| [[PANC-1 (line)]] | alt | 2.81 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.116× (z -8.8) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.874 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.828 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.783 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.937 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16573), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2]] | +0.78 | +0.72 / +0.85 | both halves | 7e-06 |  |
| [[PSMD1]] | +0.71 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[HERC2P9]] | +0.67 | +0.63 / +0.69 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[HERC2P3]] | +0.66 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[CLPB]] | +0.64 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[SPATA5]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[CCT3]] | +0.63 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[EXOC2]] | +0.63 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[CCT5]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[CCT6A]] | +0.62 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[ELAC2]] | +0.61 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[IDE]] | +0.61 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[NIT2]] | +0.61 | +0.63 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM5B]] | -0.64 | -0.57 / -0.65 | both halves | 8e-06 |  |
| [[HOOK2]] | -0.60 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[KLHL28]] | -0.60 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[FAM117A]] | -0.59 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[ATP23]] | -0.59 | -0.30 / -0.62 | both halves | 2e-04 |  |
| [[ZNF821]] | -0.58 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[FOXO3]] | -0.58 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.58 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[GLIS2]] | -0.57 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[HES7]] | -0.57 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[DBP]] | -0.57 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.56 | -0.44 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers HERC2P9-1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PLAG1]] | B | PLAG1 activity lowers HERC2P9-1's level | lines that do not express PLAG1 (9) vs lines expressing it (41) | 1.21× higher at baseline in the lines without PLAG1 | 0.074 | ⚠ within organs, on part of the lines; also absent: FCGRT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.565). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-7.2, -31.7); signed map (-13.3, -46.6). **Vector** length 36.8, 3.41% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +2.8 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.7 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +5.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.6 | +2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.1 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.9 | +1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +0.9 | +2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.7 | +0.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -0.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -1.6 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | +0.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -0.9 | -2.0 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -0.8 | -2.0 |

## What is on record

> [!warning] No registry record
> HERC2P9-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16573: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16573); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16573, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16573]; `tensor/DDL_lfc|DDL_z.npy` [16573]; `embed/gene_vectors.npy` [16573]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16573 or target_col == 16573). Every well: [[HERC2P9-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HERC2P9-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
