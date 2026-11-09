---
symbol: "KBTBD11-OT1-1"
type: "gene"
col: 16016
ensembl_id: "ENSG00000283239"
name: ""
location: ""
module: 47
arm: "+"
pooled_cpm: 2.65
n_lines_expressing: 48
n_dd_up: 18
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# KBTBD11-OT1-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.31× (z +8.2, q 1e-13, up in 20 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.319× (z -11.3, q 1e-26, down in 30 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM41]] (+0.67, fdr 1e-05), [[GGT1]] (+0.64, fdr 7e-06), [[FAM131A]] (+0.64, fdr 3e-05); moves opposite to [[GTF2I]] (-0.55, fdr 4e-05), [[CASD1]] (-0.54, fdr 3e-05), [[TMEM123]] (-0.52, fdr 2e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC01234]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16016.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.31×** | +8.2 | 1e-13 | 20/38 (A-172, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +8.1 | 1e-13 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.98×** | +6.7 | 5e-09 | 21/44 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +5.6 | 3e-06 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.67×** | +5.0 | 6e-05 | 13/40 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.9 | 8e-05 | 11/33 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +4.8 | 1e-04 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +4.5 | 6e-04 | 10/34 (NCI-H460, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.4 | 8e-04 | 4/14 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +4.3 | 0.001 | 12/40 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +4.1 | 0.002 | 7/43 (LS 180, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +4.1 | 0.002 | 13/37 (LS 180, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **2.09×** | +3.8 | 0.007 | 1/25 (A498) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.012 | 9/39 (A-172, HOP62, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.040 | 4/34 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16016.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.319×** | -11.3 | 1e-26 | 30/44 (A549, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.428×** | -8.4 | 2e-14 | 24/40 (Hs 766T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.435×** | -8.2 | 4e-14 | 16/25 (BT-474, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.531×** | -6.3 | 6e-08 | 22/40 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.573×** | -5.5 | 4e-06 | 15/37 (RPMI-7951, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.641×** | -4.2 | 0.002 | 11/25 (LoVo, A549, …) | top dose only |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | **0.670×** | -3.8 | 0.011 | 8/35 (KATO III, RPMI-7951, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.534×** | -3.2 | 0.086 | 7/36 (J82, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.719× | -3.0 | 0.16 | 6/41 (NCI-H23, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16016. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 4.12 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0187× (z -13.0) |
| [[BT-474 (line)]] | alt | 8.01 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0719× (z -9.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 3.62 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0248× (z -11.1) |
| [[HS-578T (line)]] | alt | 7.50 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.115× (z -8.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 2.79 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0600× (z -9.5) |
| [[SW480 (line)]] | alt | 1.70 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0657× (z -9.2) |
| [[A-172 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.853 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.969 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.903 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.985 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.941 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16016), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM41]] | +0.67 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[GGT1]] | +0.64 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[FAM131A]] | +0.64 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[PDE2A]] | +0.64 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[CPT1C]] | +0.64 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[MYO15A]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[ST6GALNAC6-1]] | +0.63 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[MSANTD1]] | +0.62 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[SYCE1L]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[FPGS]] | +0.62 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[TINCR]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[FERMT3]] | +0.61 | +0.50 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2I]] | -0.55 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[CASD1]] | -0.54 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[TMEM123]] | -0.52 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[TMPO]] | -0.52 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[MBNL1]] | -0.51 | -0.42 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01234]] | B | LINC01234 activity raises KBTBD11-OT1-1's level | lines that do not express LINC01234 (12) vs lines expressing it (38) | 1.36× lower at baseline in the lines without LINC01234 | 0.083 | ⚠ within organs, on part of the lines; also absent: NXPH4, COP1-DT, LINC00276; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.2, -19.3); signed map (13.3, 15.1). **Vector** length 52.0, 6.62% of its response variance represented; |z| ≥ 3 in 1,077 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.7 | +8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +4.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.1 | +1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +8.1 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.4 | +1.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | -11.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -8.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.8 | -6.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.6 | -8.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.8 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.3 | -2.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -1.1 |

## What is on record

> [!warning] No registry record
> KBTBD11-OT1-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16016: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16016); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16016, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16016]; `tensor/DDL_lfc|DDL_z.npy` [16016]; `embed/gene_vectors.npy` [16016]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16016 or target_col == 16016). Every well: [[KBTBD11-OT1-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KBTBD11-OT1-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
