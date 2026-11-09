---
symbol: "STARD8"
type: "gene"
col: 5020
ensembl_id: "ENSG00000130052"
name: "StAR related lipid transfer domain containing 8"
location: "Xq13.1"
module: 22
arm: "+"
pooled_cpm: 5.77
n_lines_expressing: 41
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# STARD8

*StAR related lipid transfer domain containing 8* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.03× (z +12.7, q 2e-34, up in 22 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Betamethasone dipropionate (drug)]] 5 µM: 0.609× (z -6.1, q 7e-07, down in 13 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HJURP]] (+0.64, fdr 7e-06), [[FAM72B]] (+0.63, fdr 7e-06), [[FAM110A]] (+0.62, fdr 8e-06); moves opposite to [[COPS8]] (-0.50, fdr 4e-05), [[JAK1]] (-0.47, fdr 3e-05), [[DCN]] (-0.46, fdr 4e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MDGA1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MDGA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5020.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.03×** | +12.7 | 2e-34 | 22/31 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +8.3 | 2e-14 | 18/35 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +7.1 | 3e-10 | 18/37 (HEC-1-A, HepG2/C3A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.55×** | +5.5 | 5e-06 | 14/34 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +5.5 | 5e-06 | 11/34 (LoVo, HT-29, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +5.1 | 4e-05 | 9/35 (NCI-H2347, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.4 | 9e-04 | 8/37 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +4.3 | 0.001 | 7/35 (RPMI-7951, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +4.2 | 0.002 | 10/31 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +4.0 | 0.004 | 7/37 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.020 | 8/36 (HepG2/C3A, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.034 | 4/33 (H4, HEC-1-A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.30×** | +3.3 | 0.036 | 2/37 (MIA PaCa-2, NCI-H23) | all doses, flat |  |
| [[EX229 (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.036 | 2/36 (AN3 CA, SNU-423) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5020.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.609×** | -6.1 | 7e-07 | 13/34 (HOP62, HS-578T, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.747×** | -5.3 | 3e-05 | 19/38 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.453×** | -5.3 | 3e-05 | 15/35 (HS-578T, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.709×** | -4.4 | 0.002 | 11/35 (HOP62, SW 900, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.753×** | -3.6 | 0.032 | 10/34 (AN3 CA, HOP62, …) | inconsistent across doses |  |
| [[Econazole (drug)]] 5 µM |  | 0.789× | -3.0 | 0.22 | 9/37 (NCI-H2347, HepG2/C3A, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.791× | -3.0 | 0.22 | 14/35 (H4, A-427, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5020. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 16.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 5.38 | 0 | 2 (1 ⚠) | — | [[Saquinavir (drug)]] 0.5 µM 0.0705× (z -9.6) |
| [[SNU-423 (line)]] | alt | 20.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0937× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 3.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.59× (z +11.9) | — |
| [[RPMI-7951 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.267× (z -8.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.945 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.631 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.729 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5020), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HJURP]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[FAM72B]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[FAM110A]] | +0.62 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[FAM72D]] | +0.57 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[FAM72A]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[CENPA]] | +0.55 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[SGO2]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[KIF14]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ESPL1]] | +0.55 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[UBE2C]] | +0.54 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[PAK6]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 | pathway: CDC42 GTPase cycle |
| [[SCG5]] | +0.54 | +0.51 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS8]] | -0.50 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[JAK1]] | -0.47 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[DCN]] | -0.46 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[VPS50]] | -0.45 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[NTPCR]] | -0.44 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[CCND3]] | -0.44 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[UBE2E1]] | -0.43 | -0.37 / -0.45 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MDGA1]] | B | MDGA1 activity raises STARD8's level | lines that do not express MDGA1 (13) vs lines expressing it (37) | 2.28× lower at baseline in the lines without MDGA1 | 0.045 | ⚠ within organs, on part of the lines; also absent: TCF7L1, ZNF470, FBXL2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MDGA1]] | B | STARD8 activity raises MDGA1's level | lines that do not express STARD8 (9) vs lines expressing it (41) | 2.69× lower at baseline in the lines without STARD8 | 0.085 | ⚠ within organs, on part of the lines; also absent: ADGRG2, TMEM132B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.507). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.4, -59.5); signed map (-53.3, -42.2). **Vector** length 64.0, 11.7% of its response variance represented; |z| ≥ 3 in 849 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +12.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +5.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.5 | +2.8 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.2 | +0.9 |
|  | [[Ferulic acid (drug)]] 0.5 µM |  | +1.0 | +1.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.0 | +1.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -5.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.5 | -3.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.4 | -6.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.2 | -5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.0 | -4.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | StAR related lipid transfer domain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:68,647,666-68,725,842 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0189, ARHGAP38 |
| Gene groups (HGNC) | Rho GTPase activating proteins; StAR related lipid transfer domain containing |
| Reactome | 6 pathways, smallest: RHOB GTPase cycle; RHOA GTPase cycle; CDC42 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92502](https://www.uniprot.org/uniprotkb/Q92502) (StAR-related lipid transfer protein 8):

> Accelerates GTPase activity of RHOA and CDC42, but not RAC1. Stimulates the hydrolysis of phosphatidylinositol 4,5-bisphosphate by PLCD1.

**Summary**, from NCBI Gene [9754](https://www.ncbi.nlm.nih.gov/gene/9754):

> This gene encodes a member of a subfamily of Rho GTPase activating proteins that contain a steroidogenic acute regulatory protein related lipid transfer domain. The encoded protein localizes to focal adhesions and may be involved in regulating cell morphology. This protein may also function as a tumor suppressor. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:19161](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19161) · Entrez [9754](https://www.ncbi.nlm.nih.gov/gene/9754) · UniProt [Q92502](https://www.uniprot.org/uniprotkb/Q92502) · Ensembl [ENSG00000130052](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130052)

## Data

Gene col 5020: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5020); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5020, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5020]; `tensor/DDL_lfc|DDL_z.npy` [5020]; `embed/gene_vectors.npy` [5020]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5020 or target_col == 5020). Every well: [[STARD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STARD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
