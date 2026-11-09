---
symbol: "SAMD14"
type: "gene"
col: 9413
ensembl_id: "ENSG00000167100"
name: "sterile alpha motif domain containing 14"
location: "17q21.33"
module: 53
arm: "+"
pooled_cpm: 2.57
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# SAMD14

*sterile alpha motif domain containing 14* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.84× (z +17.8, q 0e+00, up in 20 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.499× (z -6.5, q 3e-08, down in 18 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPT1C]] (+0.70, fdr 1e-05), [[COL23A1]] (+0.68, fdr 7e-06), [[ASGR1]] (+0.67, fdr 7e-06); moves opposite to [[VPS50]] (-0.52, fdr 6e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SSC5D]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9413.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.84×** | +17.8 | 0e+00 | 20/26 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.44×** | +11.6 | 2e-28 | 29/33 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.39×** | +11.5 | 2e-28 | 30/40 (BT-474, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.00×** | +8.8 | 3e-16 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +8.6 | 1e-15 | 1/12 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.40×** | +8.2 | 2e-14 | 25/42 (A-427, A498, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +5.5 | 3e-06 | 11/28 (PANC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +5.3 | 7e-06 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +4.8 | 1e-04 | 7/23 (A498, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.57×** | +4.2 | 0.001 | 12/41 (A-427, CFPAC-1, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.56×** | +4.2 | 0.002 | 10/38 (HOP62, BT-474, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.55×** | +4.1 | 0.002 | 10/42 (SNU-1, A-427, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.51×** | +3.9 | 0.005 | 7/40 (A-427, NCI-H460, …) | all doses, flat |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.98×** | +3.3 | 0.034 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +3.2 | 0.051 | 1/13 (HT-29) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Acetohexamide (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.073 | 2/30 (hTERT-HPNE, HOP62) | inconsistent across doses | position effect removed |
| [[Trimetrexate (drug)]] 0.05 µM |  | **1.38×** | +3.0 | 0.094 | 2/33 (SW480, RPMI-7951) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9413.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.499×** | -6.5 | 3e-08 | 18/36 (NCI-H1573, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.609×** | -4.7 | 8e-04 | 15/34 (BT-474, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.635×** | -4.3 | 0.003 | 12/40 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.668×** | -3.8 | 0.020 | 7/36 (NCI-H1792, RKO, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.778×** | -3.4 | 0.082 | 11/39 (LOX-IMVI, C32, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.703×** | -3.3 | 0.082 | 9/43 (C-33 A, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | 0.705× | -3.1 | 0.14 | 9/44 (NCI-H1573, SW48, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.725× | -3.0 | 0.17 | 9/31 (BT-474, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9413. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 17.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0731× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 7.26 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0969× (z -8.9) ⚠ cell-cycle shift, explains ~53% of this change |
| [[BT-474 (line)]] | alt | 4.70 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0799× (z -9.2) |
| [[HOP62 (line)]] | alt | 8.21 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0880× (z -11.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 3.55 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0398× (z -10.0) ⚠ cell-cycle shift, explains ~87% of this change |
| [[A-427 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.874 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.760 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.738 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.741 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.836 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.990 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.816 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.844 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.760 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9413), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPT1C]] | +0.70 | +0.55 / +0.78 | both halves | 1e-05 |  |
| [[COL23A1]] | +0.68 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[ASGR1]] | +0.67 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.67 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[CELF5]] | +0.66 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[SNAI1]] | +0.65 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[NPAS1]] | +0.64 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[SMIM41]] | +0.63 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[ELAVL3]] | +0.63 | +0.47 / +0.72 | both halves | 2e-05 |  |
| [[PDE2A]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[A3GALT2]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[TTLL13]] | +0.62 | +0.50 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS50]] | -0.52 | -0.39 / -0.62 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSC5D]] | B | SSC5D activity raises SAMD14's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.65× lower at baseline in the lines without SSC5D | 0.046 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[TNFSF9]] | B | TNFSF9 activity lowers SAMD14's level | lines that do not express TNFSF9 (6) vs lines expressing it (44) | 2.26× higher at baseline in the lines without TNFSF9 | 0.060 | ⚠ within organs, on part of the lines; also absent: SNAI1; its own permutation p |
| [[TSHZ3]] | B | TSHZ3 activity raises SAMD14's level | lines that do not express TSHZ3 (25) vs lines expressing it (25) | 1.90× lower at baseline in the lines without TSHZ3 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B |
| [[AQP3]] | B | AQP3 activity lowers SAMD14's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 1.52× higher at baseline in the lines without AQP3 | 0.085 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.649). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.0, -17.1); signed map (16.8, 17.2). **Vector** length 62.1, 10.1% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +11.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +11.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +17.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +4.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +2.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -6.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -2.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | sterile alpha motif domain containing 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:50,110,040-50,130,160 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36890 |
| Gene groups (HGNC) | Sterile alpha motif domain containing |
| Matched by | ensembl_id |

UniProt [Q8IZD0](https://www.uniprot.org/uniprotkb/Q8IZD0) carries no function annotation.

**Summary**, from NCBI Gene [201191](https://www.ncbi.nlm.nih.gov/gene/201191):

> Predicted to enable actin filament binding activity. Predicted to be involved in actin filament organization; calcium-mediated signaling; and neuron projection development. Predicted to be active in several cellular components, including actin cytoskeleton; dendrite; and postsynaptic density. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27312](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27312) · Entrez [201191](https://www.ncbi.nlm.nih.gov/gene/201191) · UniProt [Q8IZD0](https://www.uniprot.org/uniprotkb/Q8IZD0) · Ensembl [ENSG00000167100](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167100)

## Data

Gene col 9413: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9413); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9413, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9413]; `tensor/DDL_lfc|DDL_z.npy` [9413]; `embed/gene_vectors.npy` [9413]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9413 or target_col == 9413). Every well: [[SAMD14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAMD14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
