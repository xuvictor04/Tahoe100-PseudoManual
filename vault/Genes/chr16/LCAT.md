---
symbol: "LCAT"
type: "gene"
col: 13103
ensembl_id: "ENSG00000213398"
name: "lecithin-cholesterol acyltransferase"
location: "16q22.1"
module: 29
arm: "-"
pooled_cpm: 2.23
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# LCAT

*lecithin-cholesterol acyltransferase* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.92× (z +11.7, q 5e-29, up in 26 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.372× (z -4.0, q 0.036, down in 9 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC12A4]] (+0.83, fdr 7e-06, ⚠ read-through risk), [[WNK4]] (+0.66, fdr 7e-06), [[LIME1]] (+0.65, fdr 7e-06), [[PAQR6]] (+0.62, fdr 7e-06); moves opposite to [[CUL2]] (-0.61, fdr 1e-05), [[PEBP1]] (-0.60, fdr 4e-05), [[PRDX3]] (-0.58, fdr 1e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HOMER3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13103.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.92×** | +11.7 | 5e-29 | 26/31 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.47×** | +9.3 | 6e-18 | 2/2 (A498, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.11×** | +8.8 | 3e-16 | 23/28 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.54×** | +6.7 | 4e-09 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +5.4 | 9e-06 | 2/11 (PANC-1, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.01×** | +5.2 | 2e-05 | 17/39 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **2.27×** | +4.5 | 5e-04 | 4/22 (LoVo, A-172, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +4.1 | 0.003 | 4/12 (HEC-1-A, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.61×** | +3.6 | 0.017 | 7/27 (SW480, AsPC-1, …) | top dose only | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.6 | 0.020 | 5/23 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.64×** | +3.5 | 0.020 | 4/17 (NCI-H460, A-172, …) | all doses, flat |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.57×** | +3.5 | 0.024 | 4/21 (NCI-H460, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.031 | 9/44 (HCT15, A-427, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.032 | 9/44 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +3.2 | 0.047 | 8/37 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[vincristine (drug)]] 5 µM |  | **2.20×** | +3.2 | 0.047 | 0/12 | two highest doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.51×** | +3.2 | 0.047 | 2/41 (SW480, SNU-423) | inconsistent across doses | position effect removed |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.48×** | +3.0 | 0.069 | 4/26 (HepG2/C3A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +3.0 | 0.077 | 6/42 (SNU-1, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[DTP3 (drug)]] 5 µM |  | **2.07×** | +2.9 | 0.078 | 1/17 (NCI-H23) | top dose only | noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.69×** | +2.9 | 0.089 | 3/27 (J82, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13103.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.372×** | -4.0 | 0.036 | 9/33 (HEC-1-A, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | 0.726× | -3.5 | 0.13 | 14/43 (SW480, hTERT-HPNE, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~17% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13103. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.924 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.600 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.985 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.950 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.893 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13103), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC12A4]] | +0.83 | +0.76 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_XENOBIOTIC_METABOLISM; STRING 628; ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of SLC12A4 on the same strand (can correlate by spillover, not regulation) |
| [[WNK4]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[LIME1]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[PAQR6]] | +0.62 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[CDK3]] | +0.62 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[ARVCF]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[HOMER3]] | +0.61 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[KMT2B]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[WASHC1]] | +0.60 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[RNF166]] | +0.59 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[CC2D1B]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[PPP1R37]] | +0.58 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[FBXL6]] | +0.58 | +0.62 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CUL2]] | -0.61 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[PEBP1]] | -0.60 | -0.57 / -0.43 | both halves | 4e-05 |  |
| [[PRDX3]] | -0.58 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[LANCL1]] | -0.58 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[SUMO1]] | -0.58 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[KDM1A]] | -0.58 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[PPT1]] | -0.57 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[SKP2]] | -0.57 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[SCARB2]] | -0.56 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[GRB2]] | -0.56 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[MRPL19]] | -0.55 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[MINPP1]] | -0.55 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOMER3]] | C | HOMER3 activity raises LCAT's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 1.80× lower at baseline in the lines without HOMER3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (24.5, -8.6); signed map (2.7, -10.2). **Vector** length 53.2, 7.34% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +11.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +6.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.2 | +4.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +2.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.8 | +1.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -1.9 | -3.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.9 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -1.4 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.7 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | lecithin-cholesterol acyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,939,750-67,944,131 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Acyltransferases |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 4 pathways, smallest: HDL remodeling; Plasma lipoprotein remodeling; Plasma lipoprotein assembly, remodeling, and clearance |
| Matched by | ensembl_id |

**Function**, from UniProt [P04180](https://www.uniprot.org/uniprotkb/P04180) (Phosphatidylcholine-sterol acyltransferase):

> Central enzyme in the extracellular metabolism of plasma lipoproteins. Synthesized mainly in the liver and secreted into plasma where it converts cholesterol and phosphatidylcholines (lecithins) to cholesteryl esters and lysophosphatidylcholines on the surface of high and low density lipoproteins (HDLs and LDLs). The cholesterol ester is then transported back to the liver. Has a preference for plasma 16:0-18:2 or 18:O-18:2 phosphatidylcholines. Also produced in the brain by primary astrocytes, …

**Summary**, from NCBI Gene [3931](https://www.ncbi.nlm.nih.gov/gene/3931):

> This gene encodes the extracellular cholesterol esterifying enzyme, lecithin-cholesterol acyltransferase. The esterification of cholesterol is required for cholesterol transport. Mutations in this gene have been found to cause fish-eye disease as well as LCAT deficiency. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6522](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6522) · Entrez [3931](https://www.ncbi.nlm.nih.gov/gene/3931) · UniProt [P04180](https://www.uniprot.org/uniprotkb/P04180) · Ensembl [ENSG00000213398](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213398)

## Data

Gene col 13103: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13103); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13103, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13103]; `tensor/DDL_lfc|DDL_z.npy` [13103]; `embed/gene_vectors.npy` [13103]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13103 or target_col == 13103). Every well: [[LCAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LCAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
