---
symbol: "ASTE1"
type: "gene"
col: 422
ensembl_id: "ENSG00000034533"
name: "asteroid structure-specific endonuclease 1"
location: "3q22.1"
module: 149
arm: "+"
pooled_cpm: 6.02
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# ASTE1

*asteroid structure-specific endonuclease 1* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.57× (z +6.6, q 2e-08, up in 17 of 32 measured lines) ⚠ toxic. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.32× (z +6.0, q 6e-07, up in 15 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.630× (z -6.9, q 4e-09, down in 20 of 36 measured lines) ⚠ toxic. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H1792 0.0797×; ⚠ toxic); [[Harringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.102×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.161×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC27]] (+0.66, fdr 1e-05), [[THAP6]] (+0.64, fdr 1e-05), [[YJU2B]] (+0.62, fdr 1e-05); moves opposite to [[DIAPH1]] (-0.63, fdr 1e-05), [[GATAD2A]] (-0.58, fdr 1e-05), [[ACTN1]] (-0.57, fdr 1e-05).
> It is in [[Module 149]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF573]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 422.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +6.6 | 2e-08 | 17/32 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +6.0 | 6e-07 | 15/45 (SW1417, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +4.6 | 6e-04 | 5/46 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +4.6 | 6e-04 | 12/39 (NCI-H1573, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.7 | 0.022 | 4/45 (A-427, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.29×** | +3.6 | 0.030 | 3/17 (NCI-H460, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.030 | 10/40 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.042 | 5/45 (LS 180, PANC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.054 | 6/45 (J82, PANC-1, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.054 | 5/44 (SNU-423, SW1417, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.094 | 1/47 (PANC-1) | top dose only |  |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.097 | 6/43 (MIA PaCa-2, SHP-77, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 422.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H1792 0.0797×; ⚠ toxic); [[Harringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.102×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.161×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.630×** | -6.9 | 4e-09 | 20/36 (NCI-H1792, HS-578T, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.795×** | -3.6 | 0.077 | 6/46 (Panc 03.27, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.796×** | -3.5 | 0.077 | 6/47 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.813× | -3.1 | 0.29 | 7/41 (HOP62, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 422. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 5.56 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0703× (z -8.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 5.29 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.102× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 6.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 5.49 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0797× (z -9.4) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 3.92 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[A-172 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 422), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC27]] | +0.66 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[THAP6]] | +0.64 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[YJU2B]] | +0.62 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[TTI2]] | +0.61 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[MORN4]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[OSCP1]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ZNF594-DT]] | +0.60 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[LINC02256]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[MTO1]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[KRT10-AS1]] | +0.59 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[ZNF766]] | +0.58 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[FPGT]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIAPH1]] | -0.63 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.58 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[ACTN1]] | -0.57 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[CORO1C]] | -0.54 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[MPRIP]] | -0.53 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[MACROH2A1]] | -0.50 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[TRAPPC9]] | -0.49 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[MSN]] | -0.49 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[TPM4]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[DBN1]] | -0.49 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[ACTB]] | -0.48 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[HNRNPA2B1]] | -0.48 | -0.43 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF573]] | C | ZNF573 activity raises ASTE1's level | lines that do not express ZNF573 (4) vs lines expressing it (46) | 1.34× lower at baseline in the lines without ZNF573 | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with FBXW7; also absent: ZNF540, ZNF675, ZNF571 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.510). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-24.8, 21.2); signed map (-7.0, -9.5). **Vector** length 50.0, 5.86% of its response variance represented; |z| ≥ 3 in 836 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +6.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.8 | +6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +3.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +3.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.1 | +3.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.0 | +2.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.3 | -6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.9 | -1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.2 | -0.4 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -1.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | asteroid structure-specific endonuclease 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1 — chr3:131,013,875-131,027,649 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HT001 |
| Gene groups (HGNC) | PIN-like domain superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2TB18](https://www.uniprot.org/uniprotkb/Q2TB18) (Single-strand DNA endonuclease ASTE1):

> Structure-specific DNA endonuclease that specifically cleaves single-stranded DNA and 3' overhang DNA. Contributes to the control of DNA double-strand break repair choice by antagonizing BRCA1-dependent homologous recombination (HR) and promoting non-homologous end-joining (NHEJ). Recruited to the single-stranded DNA ends by SHLD2 and cleaves the 3' exposed DNA ends, therefore inhibiting DNA end resection (necessary for HR) and promoting DNA end protection (necessary for NHEJ).

**Summary**, from NCBI Gene [28990](https://www.ncbi.nlm.nih.gov/gene/28990):

> Enables 3' overhang single-stranded DNA endonuclease activity. Involved in double-strand break repair via homologous recombination and double-strand break repair via nonhomologous end joining. Implicated in Lynch syndrome and mismatch repair cancer syndrome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25021](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25021) · Entrez [28990](https://www.ncbi.nlm.nih.gov/gene/28990) · UniProt [Q2TB18](https://www.uniprot.org/uniprotkb/Q2TB18) · Ensembl [ENSG00000034533](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000034533)

## Data

Gene col 422: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 422); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 422, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 422]; `tensor/DDL_lfc|DDL_z.npy` [422]; `embed/gene_vectors.npy` [422]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 422 or target_col == 422). Every well: [[ASTE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASTE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
