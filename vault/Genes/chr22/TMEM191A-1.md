---
symbol: "TMEM191A-1"
type: "gene"
col: 16575
ensembl_id: "ENSG00000291085"
name: ""
location: ""
module: 58
arm: "+"
pooled_cpm: 2.41
n_lines_expressing: 48
n_dd_up: 4
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# TMEM191A-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.45× (z +4.4, q 0.003, up in 1 of 1 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.34× (z +4.4, q 0.003, up in 17 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.422× (z -4.3, q 0.008, down in 15 of 27 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C4orf48]] (+0.75, fdr 9e-06), [[CDKN2D]] (+0.72, fdr 1e-05), [[POLR2J]] (+0.71, fdr 2e-04, ⚠ POLR2J in the vector space only through flagged drug-doses), [[COMMD6]] (+0.70, fdr 4e-05); moves opposite to [[U2AF2]] (-0.71, fdr 1e-04), [[SRSF1]] (-0.70, fdr 4e-05), [[EWSR1]] (-0.69, fdr 1e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[C19orf33]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16575.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.45×** | +4.4 | 0.003 | 1/1 (NCI-H2347) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **2.35×** | +4.4 | 0.003 | 6/14 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.34×** | +4.4 | 0.003 | 17/37 (HT-29, A498, …) | two highest doses | cell-cycle shift (explains ~23% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.05×** | +3.7 | 0.034 | 15/38 (A498, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | 1.91× | +3.3 | 0.11 | 5/13 (NCI-H23, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.93× | +3.2 | 0.11 | 4/15 (SW1417, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16575.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.422×** | -4.3 | 0.008 | 15/27 (NCI-H2030, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.475×** | -3.7 | 0.043 | 18/41 (HS-578T, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.595×** | -3.7 | 0.043 | 19/29 (NCI-H460, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.287× | -3.3 | 0.14 | 14/32 (NCI-H2030, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.532× | -3.2 | 0.16 | 13/38 (J82, KATO III, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.304× | -3.1 | 0.16 | 17/23 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16575. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.45 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0790× (z -10.1) |
| [[A-172 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.648 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.484 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.673 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.788 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.838 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.736 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.710 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.607 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.771 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.970 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.205 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.737 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16575), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 11 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C4orf48]] | +0.75 | +0.57 / +0.74 | both halves | 9e-06 |  |
| [[CDKN2D]] | +0.72 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[POLR2J]] ⚠ | +0.71 | +0.32 / +0.74 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[COMMD6]] | +0.70 | +0.42 / +0.75 | both halves | 4e-05 |  |
| [[MRPL41]] ⚠ | +0.70 | +0.27 / +0.71 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[OCEL1]] | +0.69 | +0.28 / +0.70 | both halves | 3e-04 |  |
| [[ATP5MJ]] | +0.69 | +0.35 / +0.70 | both halves | 1e-04 |  |
| [[SIGIRR]] | +0.69 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[TSTD1]] | +0.69 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[LAMTOR5]] | +0.69 | +0.37 / +0.71 | both halves | 9e-05 |  |
| [[RPL36AL]] ⚠ | +0.68 | +0.40 / +0.76 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MPG]] | +0.67 | +0.30 / +0.68 | both halves | 2e-04 |  |
| [[CARHSP1]] | +0.67 | +0.39 / +0.62 | both halves | 5e-05 |  |
| [[TMEM256]] | +0.66 | +0.39 / +0.59 | both halves | 6e-05 |  |
| [[LIN7B]] | +0.66 | +0.38 / +0.67 | both halves | 7e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[U2AF2]] | -0.71 | -0.33 / -0.67 | both halves | 1e-04 |  |
| [[SRSF1]] | -0.70 | -0.42 / -0.75 | both halves | 4e-05 |  |
| [[EWSR1]] | -0.69 | -0.36 / -0.74 | both halves | 1e-04 |  |
| [[PSME3IP1]] | -0.68 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[PSME3]] | -0.67 | -0.48 / -0.70 | both halves | 2e-05 |  |
| [[VPS52]] | -0.67 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[SSU72]] | -0.66 | -0.38 / -0.67 | both halves | 7e-05 |  |
| [[UBQLN4]] | -0.66 | -0.37 / -0.68 | both halves | 7e-05 |  |
| [[ATP13A1]] | -0.65 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[SETD7]] | -0.64 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[RCN1]] | -0.64 | -0.33 / -0.62 | both halves | 1e-04 |  |
| [[HNRNPL]] | -0.64 | -0.30 / -0.67 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C19orf33]] | B | C19orf33 activity raises TMEM191A-1's level | lines that do not express C19orf33 (19) vs lines expressing it (31) | 1.66× lower at baseline in the lines without C19orf33 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: KRT80, MISP, AREG |
| [[IFI27L2]] | B | IFI27L2 activity lowers TMEM191A-1's level | lines that do not express IFI27L2 (6) vs lines expressing it (44) | 1.54× higher at baseline in the lines without IFI27L2 | 0.049 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-45.0, -17.8); signed map (-28.8, 14.7). **Vector** length 49.8, 9.34% of its response variance represented; |z| ≥ 3 in 548 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | +4.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.6 | +3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.3 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +1.2 | +2.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.1 | +1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +2.4 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.0 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.0 | +2.6 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.0 | +2.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.7 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -2.5 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | -2.3 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.0 | -4.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.4 | -1.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -2.6 |

## What is on record

> [!warning] No registry record
> TMEM191A-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16575: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16575); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16575, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16575]; `tensor/DDL_lfc|DDL_z.npy` [16575]; `embed/gene_vectors.npy` [16575]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16575 or target_col == 16575). Every well: [[TMEM191A-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM191A-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
