---
symbol: "BEX2"
type: "gene"
col: 5424
ensembl_id: "ENSG00000133134"
name: "brain expressed X-linked 2"
location: "Xq22.2"
module: 63
arm: "+"
pooled_cpm: 4.47
n_lines_expressing: 32
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# BEX2

*brain expressed X-linked 2* — Xq22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 2.36× (z +6.7, q 1e-08, up in 18 of 28 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BEX4]] (+0.79, fdr 7e-06), [[UBE2B]] (+0.65, fdr 7e-06), [[NUPR1]] (+0.64, fdr 1e-05); moves opposite to [[PRKDC]] (-0.59, fdr 1e-05), [[XRCC6]] (-0.58, fdr 5e-05), [[EIF2S1]] (-0.57, fdr 2e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PLEKHG1]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5424.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **2.36×** | +6.7 | 1e-08 | 18/28 (J82, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.30×** | +6.5 | 2e-08 | 20/21 (Panc 03.27, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.10×** | +6.4 | 3e-08 | 22/26 (PANC-1, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.21×** | +6.1 | 2e-07 | 18/28 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.90×** | +5.0 | 5e-05 | 12/25 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.45×** | +4.9 | 1e-04 | 15/20 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.08×** | +4.2 | 0.003 | 8/16 (A498, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +3.7 | 0.013 | 12/25 (NCI-H2030, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.86×** | +3.5 | 0.028 | 16/27 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.5 | 0.028 | 8/21 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.56×** | +3.4 | 0.032 | 13/27 (NCI-H23, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +3.3 | 0.045 | 7/15 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.78×** | +3.3 | 0.047 | 14/27 (NCI-H23, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +3.0 | 0.099 | 3/11 (J82, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5424.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.551× | -3.4 | 0.38 | 12/28 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.583× | -3.1 | 0.38 | 5/28 (NCI-H661, J82, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5424. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.53 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.98× (z +9.1) | — |
| [[J82 (line)]] | alt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +8.7) | — |
| [[A-172 (line)]] | wt | 0.715 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.427 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.597 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.547 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.537 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.976 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.480 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.802 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.488 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5424), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BEX4]] | +0.79 | +0.73 / +0.80 | both halves | 7e-06 | same gene group; STRING 551 |
| [[UBE2B]] | +0.65 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[NUPR1]] | +0.64 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ERICH2]] | +0.63 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[LDAF1]] | +0.63 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[GDF15]] | +0.59 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[DDIT3]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[EPB41L4A-AS1]] | +0.59 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[SNHG7]] | +0.58 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[HRK]] | +0.58 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[TCEAL3]] | +0.58 | +0.57 / +0.61 | both halves | 1e-05 | STRING 566 |
| [[CLGN]] | +0.58 | +0.49 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | -0.59 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[XRCC6]] | -0.58 | -0.40 / -0.69 | both halves | 5e-05 |  |
| [[EIF2S1]] | -0.57 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[XRCC5]] | -0.56 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[BANF1]] | -0.56 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[CPSF3]] | -0.55 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[TUBA1B]] | -0.54 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[NUP155]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[EMC1]] | -0.53 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[ATP5F1A]] | -0.52 | -0.43 / -0.51 | both halves | 4e-05 |  |
| [[COPS3]] | -0.52 | -0.26 / -0.64 | both halves | 3e-04 |  |
| [[SMC1A]] | -0.51 | -0.37 / -0.52 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHG1]] | B | PLEKHG1 activity raises BEX2's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 1.55× lower at baseline in the lines without PLEKHG1 | 0.016 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[BEX4]] | C | BEX4 activity raises BEX2's level | lines that do not express BEX4 (22) vs lines expressing it (28) | 2.88× lower at baseline in the lines without BEX4 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, ZNF229, BEX2; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | B | BEX2 activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express BEX2 (18) vs lines expressing it (30) | the lines without BEX2: 0.83× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000232386, BEX4, PAPLN |
| [[EPB41L4A-AS1]] | B | BEX2 activity raises EPB41L4A-AS1's level | lines that do not express BEX2 (18) vs lines expressing it (32) | 1.05× lower at baseline in the lines without BEX2 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000232386, BEX4, PAPLN |
| [[BEX4]] | C | BEX2 activity raises BEX4's level | lines that do not express BEX2 (18) vs lines expressing it (32) | 2.97× lower at baseline in the lines without BEX2 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000232386, BEX4, PAPLN; co-absent with the target |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.477). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.9, 48.9); signed map (-11.1, 22.8). **Vector** length 62.7, 18.0% of its response variance represented; |z| ≥ 3 in 481 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.4 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +5.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +3.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +0.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -3.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | brain expressed X-linked 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.2 — chrX:103,309,346-103,311,007 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DJ79P11.1 |
| Gene groups (HGNC) | Brain expressed X-linked family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXY8](https://www.uniprot.org/uniprotkb/Q9BXY8) (Protein BEX2):

> Regulator of mitochondrial apoptosis and G1 cell cycle in breast cancer. Protects the breast cancer cells against mitochondrial apoptosis and this effect is mediated through the modulation of BCL2 protein family, which involves the positive regulation of anti-apoptotic member BCL2 and the negative regulation of pro-apoptotic members BAD, BAK1 and PUMA. Required for the normal cell cycle progression during G1 in breast cancer cells through the regulation of CCND1 and CDKN1A. Regulates the level …

**Summary**, from NCBI Gene [84707](https://www.ncbi.nlm.nih.gov/gene/84707):

> This gene belongs to the brain expressed X-linked gene family. The encoded protein interacts with the transcription factor LIM domain only 2 in a DNA-binding complex that recognizes the E-box element and promotes transcription. This gene has been found to be a tumor suppressor that is silenced in human glioma. In breast cancer cells, this gene product modulates apoptosis in response to estrogen and tamoxifen, and enhances the anti-proliferative effect of tamoxifen. Multiple transcript variants …

**Accessions** — [HGNC:30933](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30933) · Entrez [84707](https://www.ncbi.nlm.nih.gov/gene/84707) · UniProt [Q9BXY8](https://www.uniprot.org/uniprotkb/Q9BXY8) · Ensembl [ENSG00000133134](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133134)

## Data

Gene col 5424: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5424); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5424, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5424]; `tensor/DDL_lfc|DDL_z.npy` [5424]; `embed/gene_vectors.npy` [5424]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5424 or target_col == 5424). Every well: [[BEX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BEX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
