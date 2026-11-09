---
symbol: "FIBP"
type: "gene"
col: 10264
ensembl_id: "ENSG00000172500"
name: "FGF1 intracellular binding protein"
location: "11q13.1"
module: 206
arm: "+"
pooled_cpm: 11.17
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 5
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/206"]
generated_by: "tahoemap"
---

# FIBP

*FGF1 intracellular binding protein* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.11× (z +10.0, q 7e-21, up in 29 of 33 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.574× (z -4.9, q 5e-04, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNAPIN]] (+0.68, fdr 7e-06), [[MIF4GD]] (+0.63, fdr 7e-06), [[ZNF184]] (+0.63, fdr 4e-05); moves opposite to [[ZNF460-AS1]] (-0.59, fdr 6e-05), [[POU6F1]] (-0.57, fdr 1e-04), [[BCL2L2-PABPN1]] (-0.54, fdr 1e-04).
> It is in [[Module 206]], a single-armed module (Constitutive Signaling by Aberrant PI3K in Cancer).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PHLDB1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 9 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10264.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **3.11×** | +10.0 | 7e-21 | 29/33 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.80×** | +8.7 | 8e-16 | 21/22 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.23×** | +5.9 | 8e-07 | 21/30 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.93×** | +5.8 | 1e-06 | 31/41 (SW480, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +3.8 | 0.016 | 20/46 (NCI-H1573, HOP62, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.47×** | +3.4 | 0.067 | 14/47 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.46× | +3.2 | 0.11 | 17/46 (NCI-H1573, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.45× | +3.2 | 0.11 | 15/40 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 1.43× | +3.1 | 0.12 | 14/47 (COLO 205, RKO, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10264.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.574×** | -4.9 | 5e-04 | 25/46 (RPMI-7951, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.621×** | -4.2 | 0.006 | 23/47 (BT-474, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.647×** | -3.9 | 0.020 | 22/46 (J82, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.663×** | -3.7 | 0.035 | 20/46 (SW 900, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.673×** | -3.5 | 0.047 | 20/46 (HOP62, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10264. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 4.60 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0587× (z -8.9) |
| [[SW48 (line)]] | wt | 13.8 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0696× (z -9.7) |
| [[A-172 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10264), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 6 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAPIN]] | +0.68 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[MIF4GD]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[ZNF184]] | +0.63 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[ELOF1]] | +0.61 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[PRR7]] | +0.60 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[GALE]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ALAS1]] | +0.58 | +0.65 / +0.26 | both halves | 3e-04 |  |
| [[TIMM17B]] ⚠ | +0.57 | +0.53 / +0.58 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NDUFAF3]] | +0.57 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[EMC9]] | +0.56 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[SFR1]] | +0.55 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[SLC35A4]] | +0.55 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[MIDEAS]] | +0.54 | +0.44 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF460-AS1]] | -0.59 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[POU6F1]] | -0.57 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[BCL2L2-PABPN1]] | -0.54 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[SAP30L-AS1]] | -0.54 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[SLC25A53]] | -0.54 | -0.51 / -0.23 | both halves | 5e-04 |  |
| [[CAB39L]] | -0.54 | -0.49 / -0.26 | both halves | 4e-04 |  |
| [[SEC24B-AS1]] | -0.54 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[C8orf44-SGK3]] | -0.53 | -0.26 / -0.54 | both halves | 4e-04 |  |
| [[MKRN5P]] | -0.53 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[GPALPP1]] | -0.52 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[ADAT3]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[SNHG22]] | -0.52 | -0.36 / -0.43 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PHLDB1]] | C | PHLDB1 activity raises FIBP's level | lines that do not express PHLDB1 (4) vs lines expressing it (46) | 1.10× lower at baseline in the lines without PHLDB1 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NUAK1, MYBL1, C12orf75; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 206]] — Constitutive Signaling by Aberrant PI3K in Cancer; 15 genes; every member is in the + arm (projection on the module's main direction 0.554). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-50.0, -11.3); signed map (-20.5, -5.0). **Vector** length 54.8, 9.99% of its response variance represented; |z| ≥ 3 in 571 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.3 | +3.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.2 | +3.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | -0.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | -0.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +2.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.1 | +2.7 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | +1.0 | +0.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +3.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.3 | -4.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.4 | -0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | +0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.6 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.1 | -0.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | FGF1 intracellular binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,883,740-65,888,531 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FGFIBP |
| Matched by | ensembl_id |

**Function**, from UniProt [O43427](https://www.uniprot.org/uniprotkb/O43427) (Acidic fibroblast growth factor intracellular-binding protein):

> May be involved in mitogenic function of FGF1. May mediate with IER2 FGF-signaling in the establishment of laterality in the embryo (By similarity).

**Summary**, from NCBI Gene [9158](https://www.ncbi.nlm.nih.gov/gene/9158):

> Acidic fibroblast growth factor is mitogenic for a variety of different cell types and acts by stimulating mitogenesis or inducing morphological changes and differentiation. The FIBP protein is an intracellular protein that binds selectively to acidic fibroblast growth factor (aFGF). It is postulated that FIBP may be involved in the mitogenic action of aFGF. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3705](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3705) · Entrez [9158](https://www.ncbi.nlm.nih.gov/gene/9158) · UniProt [O43427](https://www.uniprot.org/uniprotkb/O43427) · Ensembl [ENSG00000172500](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172500)

## Data

Gene col 10264: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10264); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10264, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10264]; `tensor/DDL_lfc|DDL_z.npy` [10264]; `embed/gene_vectors.npy` [10264]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10264 or target_col == 10264). Every well: [[FIBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FIBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
