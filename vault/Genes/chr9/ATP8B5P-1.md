---
symbol: "ATP8B5P-1"
type: "gene"
col: 16488
ensembl_id: "ENSG00000290567"
name: ""
location: ""
module: 47
arm: "+"
pooled_cpm: 3.94
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# ATP8B5P-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.46× (z +9.3, q 1e-17, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.494× (z -5.3, q 6e-05, down in 22 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.524× (z -4.9, q 3e-04, down in 22 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02803]] (+0.71, fdr 7e-06), [[LINC02133]] (+0.65, fdr 7e-06), [[WNT2B]] (+0.65, fdr 7e-06); moves opposite to [[TMEM94]] (-0.65, fdr 7e-06), [[RCOR3]] (-0.59, fdr 1e-05), [[CIAO2A]] (-0.56, fdr 3e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16488.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.46×** | +9.3 | 1e-17 | 41/46 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.98×** | +8.1 | 1e-13 | 38/43 (NCI-H23, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +6.7 | 5e-09 | 1/4 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.36×** | +6.4 | 2e-08 | 25/44 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +5.6 | 3e-06 | 1/6 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.98×** | +5.1 | 3e-05 | 23/45 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +4.2 | 0.002 | 6/20 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 1.53× | +3.2 | 0.11 | 11/35 (LS 180, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16488.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.494×** | -5.3 | 6e-05 | 22/34 (A549, BT-474, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.524×** | -4.9 | 3e-04 | 22/45 (BT-474, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.642×** | -4.7 | 4e-04 | 15/41 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.567×** | -4.3 | 0.003 | 18/42 (BT-474, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.341×** | -4.2 | 0.003 | 20/41 (BT-474, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.352×** | -4.1 | 0.004 | 14/32 (BT-474, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.362×** | -4.0 | 0.005 | 14/30 (BT-474, RKO, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.598×** | -3.7 | 0.014 | 17/39 (BT-474, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.619×** | -3.6 | 0.019 | 19/41 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Anethole trithione (drug)]] 5 µM |  | **0.741×** | -3.2 | 0.074 | 9/45 (LoVo, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.644×** | -3.2 | 0.074 | 13/27 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.655×** | -3.1 | 0.099 | 12/44 (C32, A549, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16488. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 22.2 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -9.5) |
| [[A549 (line)]] | wt | 6.15 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0682× (z -8.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 4.41 | 0 | 1 | — | [[Fumaric acid (drug)]] 5 µM 0.0559× (z -8.5) |
| [[KATO III (line)]] | alt | 3.60 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.05 µM 0.0473× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 4.75 | 0 | 1 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 0.5 µM 0.0610× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 5.97 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0725× (z -9.8) |
| [[A-172 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.682 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16488), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02803]] | +0.71 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[LINC02133]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[WNT2B]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[UCKL1-AS1]] | +0.65 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[C3orf62]] | +0.64 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[MSANTD1]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[SPTBN5]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PTCH2]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.62 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[BLZF2P]] | +0.62 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[CHRNA10]] | +0.62 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.62 | +0.64 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM94]] | -0.65 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[RCOR3]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[CIAO2A]] | -0.56 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[MBIP]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ZNF224]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[MINDY1]] | -0.52 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[C20orf96]] | -0.52 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[ATP23]] | -0.50 | -0.25 / -0.37 | both halves | 4e-04 |  |
| [[CNTNAP1]] | -0.50 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[RIDA]] | -0.49 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[PMS2]] | -0.49 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[NKIRAS1]] | -0.49 | -0.27 / -0.36 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ATP8B5P-1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CD226]] | B | CD226 activity raises ATP8B5P-1's level | lines that do not express CD226 (7) vs lines expressing it (43) | 1.55× lower at baseline in the lines without CD226 | 0.079 | ⚠ within organs, on part of the lines; also absent: FRZB, GALNT16, KLRG1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.5, -19.6); signed map (15.6, 14.7). **Vector** length 70.5, 11.9% of its response variance represented; |z| ≥ 3 in 1,101 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +5.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.2 | +9.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.8 | +2.0 |
| fall | [[Radotinib (drug)]] 5 µM |  | -3.5 | -4.7 |
|  | [[NG25 (drug)]] 5 µM |  | -3.4 | -4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | -1.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.2 | -1.5 |
|  | [[Afatinib (drug)]] 5 µM |  | -2.1 | -1.3 |

## What is on record

> [!warning] No registry record
> ATP8B5P-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16488: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16488); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16488, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16488]; `tensor/DDL_lfc|DDL_z.npy` [16488]; `embed/gene_vectors.npy` [16488]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16488 or target_col == 16488). Every well: [[ATP8B5P-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP8B5P-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
