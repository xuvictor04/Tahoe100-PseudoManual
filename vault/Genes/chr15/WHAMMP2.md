---
symbol: "WHAMMP2"
type: "gene"
col: 14533
ensembl_id: "ENSG00000248334"
name: "WHAMM pseudogene 2"
location: "15q13.1"
module: 186
arm: "+"
pooled_cpm: 2.86
n_lines_expressing: 40
n_dd_up: 2
n_dd_down: 6
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/186"]
generated_by: "tahoemap"
---

# WHAMMP2

*WHAMM pseudogene 2* — 15q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.44× (z +3.9, q 0.053, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.26× (z +3.6, q 0.076, up in 2 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.347× (z -11.8, q 1e-29, down in 23 of 36 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WHAMMP3]] (+0.85, fdr 7e-06), [[LINC02256]] (+0.60, fdr 3e-05), [[PRKAB2]] (+0.57, fdr 1e-05); moves opposite to [[CLTC]] (-0.52, fdr 2e-05), [[MICAL2]] (-0.50, fdr 9e-05), [[EIF4EBP2]] (-0.50, fdr 1e-04).
> It is in [[Module 186]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 2 go from it, the strongest it → [[WHAMMP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14533.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +3.9 | 0.053 | 0/3 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.076 | 2/35 (A498, SHP-77) | top dose only | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 1.77× | +3.4 | 0.13 | 1/11 (A-172) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 1.51× | +3.3 | 0.13 | 1/8 (A-172) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 0.5 µM |  | 1.32× | +3.1 | 0.22 | 0/25 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14533.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.347×** | -11.8 | 1e-29 | 23/36 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.351×** | -11.7 | 3e-29 | 24/35 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.411×** | -9.9 | 6e-21 | 22/36 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.868× | -5.5 | 5e-06 | 14/37 (hTERT-HPNE, HEC-1-A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.732×** | -4.9 | 1e-04 | 10/36 (NCI-H460, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.671×** | -4.5 | 8e-04 | 12/28 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.718×** | -3.7 | 0.018 | 9/36 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14533. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 4.12 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0338× (z -10.4) |
| [[C-33 A (line)]] | alt | 7.07 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0565× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 3.87 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0908× (z -9.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 4.01 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 4.62 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -10.3) |
| [[SW480 (line)]] | alt | 1.77 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0799× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.770 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.472 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.255 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.577 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.647 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.794 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.539 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14533), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WHAMMP3]] | +0.85 | +0.83 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[LINC02256]] | +0.60 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[PRKAB2]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[C3orf33]] | +0.57 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[HEIH]] | +0.55 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[HOXA9]] | +0.55 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[VPS37D]] | +0.54 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[HOXA5]] | +0.54 | +0.40 / +0.59 | both halves | 4e-05 |  |
| [[C16orf87]] | +0.54 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[HOXA6]] | +0.54 | +0.32 / +0.53 | both halves | 2e-04 |  |
| [[SHOX2]] | +0.54 | +0.46 / +0.32 | both halves | 2e-04 |  |
| [[RNF135]] | +0.53 | +0.39 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLTC]] | -0.52 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[MICAL2]] | -0.50 | -0.37 / -0.47 | both halves | 9e-05 |  |
| [[EIF4EBP2]] | -0.50 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[GATAD2A]] | -0.49 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[CMIP]] | -0.48 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[TRAPPC9]] | -0.48 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[MIR222HG]] | -0.48 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[PCSK2]] | -0.48 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[CORO1C]] | -0.48 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[MPRIP]] | -0.47 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[SCART1]] | -0.47 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[CFAP299]] | -0.46 | -0.46 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises WHAMMP2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[F3]] | B | F3 activity lowers WHAMMP2's level | lines that do not express F3 (24) vs lines expressing it (26) | 1.29× higher at baseline in the lines without F3 | 0.098 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[RBM43]] | C | RBM43 activity lowers WHAMMP2's level | lines that do not express RBM43 (4) vs lines expressing it (46) | 1.74× higher at baseline in the lines without RBM43 | 0.026 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALPK1, RNASEL, TFAP2A |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WHAMMP3]] | B | WHAMMP2 activity raises WHAMMP3's level | lines that do not express WHAMMP2 (10) vs lines expressing it (40) | 2.80× lower at baseline in the lines without WHAMMP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: LIFR, ZNF512B, ENSG00000286964; maybe low, not absent; its own permutation p |
| [[AMACR]] | B | WHAMMP2 activity raises AMACR's level | lines that do not express WHAMMP2 (10) vs lines expressing it (40) | 1.45× lower at baseline in the lines without WHAMMP2 | 0.089 | ⚠ within organs, on part of the lines; also absent: LIFR, ZNF512B, ENSG00000286964; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 186]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.401). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.3, 21.1); signed map (-8.4, -0.9). **Vector** length 37.2, 4.30% of its response variance represented; |z| ≥ 3 in 744 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.7 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.3 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.1 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.0 | -0.3 |
|  | [[Terfenadine (drug)]] 5 µM |  | +0.7 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.7 | +1.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +0.6 | +1.5 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -2.0 | -11.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.9 | -11.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.6 | -9.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.4 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -4.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -0.7 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.7 | -2.1 |
|  | [[vincristine (drug)]] 5 µM |  | -0.7 | +0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | WHAMM pseudogene 2 |
| Locus type | pseudogene |
| Location | 15q13.1 — chr15:28,737,583-28,754,869 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously WHDC1L2, WHAMML2 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:32360](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32360) · Entrez [440253](https://www.ncbi.nlm.nih.gov/gene/440253) · Ensembl [ENSG00000248334](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248334)

## Data

Gene col 14533: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14533); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14533, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14533]; `tensor/DDL_lfc|DDL_z.npy` [14533]; `embed/gene_vectors.npy` [14533]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14533 or target_col == 14533). Every well: [[WHAMMP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WHAMMP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
