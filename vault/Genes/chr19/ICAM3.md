---
symbol: "ICAM3"
type: "gene"
col: 1159
ensembl_id: "ENSG00000076662"
name: "intercellular adhesion molecule 3"
location: "19p13.2"
module: 40
arm: "+"
pooled_cpm: 3.87
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# ICAM3

*intercellular adhesion molecule 3* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.73× (z +10.1, q 4e-21, up in 29 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.682× (z -3.9, q 0.059, down in 16 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (HOP62 0.0816×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cytarabine (drug)]] 5 µM in 1 line (NCI-H2347 0.0694×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (H4 0.0338×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (H4 0.0391×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXL15]] (+0.65, fdr 1e-05), [[ELP5]] (+0.64, fdr 1e-05), [[NABP2]] (+0.64, fdr 2e-05); moves opposite to [[DST]] (-0.55, fdr 3e-05), [[MRPL42]] (-0.54, fdr 9e-05), [[EWSR1]] (-0.53, fdr 1e-04).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1159.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.73×** | +10.1 | 4e-21 | 29/34 (SW480, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.22×** | +7.3 | 6e-11 | 0/7 | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.32×** | +6.0 | 5e-07 | 9/15 (A498, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **2.29×** | +5.9 | 6e-07 | 7/18 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.93×** | +4.1 | 0.004 | 11/31 (SW480, Panc 03.27, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.85×** | +3.8 | 0.011 | 12/29 (SW480, BT-474, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.39×** | +3.3 | 0.078 | 13/33 (J82, A-172, …) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.65× | +3.1 | 0.11 | 4/21 (NCI-H23, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | 1.61× | +3.1 | 0.11 | 1/9 (Hs 766T) | all doses, stronger at high dose | composition shift |
| [[Bendamustine (drug)]] 5 µM |  | 1.64× | +3.1 | 0.11 | 5/30 (HS-578T, Hs 766T, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.83× | +3.1 | 0.11 | 3/16 (SW1417, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1159.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (HOP62 0.0816×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cytarabine (drug)]] 5 µM in 1 line (NCI-H2347 0.0694×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (H4 0.0338×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (H4 0.0391×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.682×** | -3.9 | 0.059 | 16/43 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.629× | -3.3 | 0.25 | 7/38 (HOP62, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.644× | -3.2 | 0.25 | 15/32 (A498, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.613× | -3.1 | 0.25 | 11/45 (NCI-H23, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[RMC-6236 (drug)]] 5 µM |  | 0.447× | -3.0 | 0.25 | 5/41 (SK-MEL-2, SW 900, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1159. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 7.28 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0338× (z -8.9) |
| [[HOP62 (line)]] | alt | 4.99 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0816× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 3.85 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0694× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.749 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1159), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXL15]] | +0.65 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[ELP5]] | +0.64 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[NABP2]] | +0.64 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[BTRC]] | +0.61 | +0.48 / +0.55 | both halves | 2e-05 | pathway: C-type lectin receptors (CLRs) |
| [[CDK7]] | +0.60 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[DIS3]] | +0.59 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[CDK2AP2]] | +0.59 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[NUDT22]] | +0.58 | +0.31 / +0.67 | both halves | 2e-04 |  |
| [[PMS2P4-1]] | +0.58 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[SRP54]] | +0.58 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[TAF5]] | +0.58 | +0.34 / +0.66 | both halves | 1e-04 |  |
| [[CRLS1]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DST]] | -0.55 | -0.46 / -0.60 | both halves | 3e-05 | pathway: Extracellular matrix organization |
| [[MRPL42]] | -0.54 | -0.37 / -0.60 | both halves | 9e-05 |  |
| [[EWSR1]] | -0.53 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[ENAH]] | -0.53 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[MGST1]] | -0.53 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ZNF300]] | -0.52 | -0.34 / -0.61 | both halves | 1e-04 |  |
| [[ARPP19]] | -0.52 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[TARDBP]] | -0.51 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[PTPN11]] | -0.51 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[SMARCC2]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[CBX6]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ICAM3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FSCN1]] | C | FSCN1 activity raises ICAM3's level | lines that do not express FSCN1 (4) vs lines expressing it (46) | 1.84× lower at baseline in the lines without FSCN1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, ELK3, WWTR1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-3.2, -54.9); signed map (-44.9, 16.4). **Vector** length 59.4, 10.6% of its response variance represented; |z| ≥ 3 in 755 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +2.9 | +3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +1.7 | +3.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +1.6 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | +0.8 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +2.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +0.8 | +1.5 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +0.8 | +0.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | intercellular adhesion molecule 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,333,776-10,339,661 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDW50, ICAM-R, CD50 |
| Gene groups (HGNC) | CD molecules; Immunoglobulin like domain containing; Ig-like cell adhesion molecule family |
| Reactome | 7 pathways, smallest: CD209 (DC-SIGN) signaling; Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Integrin cell surface interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P32942](https://www.uniprot.org/uniprotkb/P32942) (Intercellular adhesion molecule 3):

> Cell adhesion molecule that functions as a receptor ligand of the signaling receptor ITGAL:ITGB2/LFA-1 (lymphocyte-function associated (LFA) molecule 1) ensuring apoptotic neutrophil phagocytosis by macrophages. Is also a ligand for integrin ITGAD/ITGB2. Ligand of CD209 on dendritic cells (DC) through an integrin-independent mechanism that requires Ca(2+) and that forms a first contact between DC and resting T cell, facilitating the downstream DC-T cell clustering process and DC-induced …

**Summary**, from NCBI Gene [3385](https://www.ncbi.nlm.nih.gov/gene/3385):

> The protein encoded by this gene is a member of the intercellular adhesion molecule (ICAM) family. All ICAM proteins are type I transmembrane glycoproteins, contain 2-9 immunoglobulin-like C2-type domains, and bind to the leukocyte adhesion LFA-1 protein. This protein is constitutively and abundantly expressed by all leucocytes and may be the most important ligand for LFA-1 in the initiation of the immune response. It functions not only as an adhesion molecule, but also as a potent signalling …

**Accessions** — [HGNC:5346](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5346) · Entrez [3385](https://www.ncbi.nlm.nih.gov/gene/3385) · UniProt [P32942](https://www.uniprot.org/uniprotkb/P32942) · Ensembl [ENSG00000076662](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076662)

## Data

Gene col 1159: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1159); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1159, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1159]; `tensor/DDL_lfc|DDL_z.npy` [1159]; `embed/gene_vectors.npy` [1159]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1159 or target_col == 1159). Every well: [[ICAM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ICAM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
