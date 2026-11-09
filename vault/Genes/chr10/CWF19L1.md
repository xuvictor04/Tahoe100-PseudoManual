---
symbol: "CWF19L1"
type: "gene"
col: 1746
ensembl_id: "ENSG00000095485"
name: "CWF19 like cell cycle control factor 1"
location: "10q24.31"
module: 142
arm: "+"
pooled_cpm: 37.65
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 5
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# CWF19L1

*CWF19 like cell cycle control factor 1* — 10q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.97× (z +12.0, q 2e-30, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.690× (z -11.1, q 9e-26, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBOX5]] (+0.75, fdr 7e-06), [[PARL]] (+0.72, fdr 7e-06), [[ZBTB49]] (+0.69, fdr 7e-06); moves opposite to [[ARHGAP26]] (-0.57, fdr 1e-05), [[KLF12]] (-0.57, fdr 1e-05), [[PEAK1]] (-0.55, fdr 1e-05).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1746.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.97×** | +12.0 | 2e-30 | 42/48 (NCI-H460, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.25×** | +8.9 | 1e-16 | 35/48 (PANC-1, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.3 | 4e-08 | 25/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.32×** | +5.6 | 3e-06 | 25/46 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.28×** | +5.0 | 7e-05 | 21/48 (PANC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.18× | +4.9 | 1e-04 | 15/48 (J82, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.7 | 3e-04 | 0/48 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.23×** | +4.4 | 1e-03 | 22/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.16× | +3.1 | 0.14 | 14/48 (NCI-H460, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1746.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.690×** | -11.1 | 9e-26 | 39/48 (A-172, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.733×** | -6.6 | 2e-08 | 27/48 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.799×** | -4.8 | 4e-04 | 22/48 (NCI-H2347, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **0.833×** | -3.9 | 0.016 | 18/48 (PANC-1, H4, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~9% of this change | **0.831×** | -3.8 | 0.019 | 19/47 (A498, A-172, …) | top dose only |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.846× | -3.5 | 0.037 | 7/48 (hTERT-HPNE, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1746. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 36.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 36.8 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.09× (z +10.5) | — |
| [[A-427 (line)]] | wt | 39.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 58.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 40.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.366× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 50.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0671× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.105× (z -11.3) ⚠ toxic |
| [[LoVo (line)]] | wt | 28.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.12× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 38.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 47.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 32.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.222× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 36.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1746), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBOX5]] | +0.75 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[PARL]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[ZBTB49]] | +0.69 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[BRAP]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[ALG5]] | +0.68 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[DRG1]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[SLC30A6]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[GLE1]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[PAAF1]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[DERL2]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[WDR53]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[GTF3C2]] | +0.61 | +0.58 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP26]] | -0.57 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[KLF12]] | -0.57 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[PEAK1]] | -0.55 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[WWC2]] | -0.54 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[AHR]] | -0.53 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[JUN]] | -0.53 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[RFK]] | -0.52 | -0.46 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CWF19L1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[PSMB5]] | B | PSMB5 activity lowers CWF19L1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-28.3, -6.7); signed map (-13.7, -13.7). **Vector** length 95.1, 20.7% of its response variance represented; |z| ≥ 3 in 822 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +12.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +8.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | +4.0 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.5 | +2.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.4 | +4.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.6 | -11.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.4 | -6.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~9% of this change | -4.6 | -3.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.2 | -4.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | CWF19 like cell cycle control factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.31 — chr10:100,232,298-100,267,680 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C19L1, FLJ10998, hDrn1 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q69YN2](https://www.uniprot.org/uniprotkb/Q69YN2) (Pre-mRNA splicing factor CWF19L1):

> Acts as a splicing regulator which modulates global alternative splicing. Regulates expression of immune-related genes through direct regulation of alternative splicing and modulation of upstream transcription factors. Promotes T cell toxicity by enhancing T cell cytokine production.

**Summary**, from NCBI Gene [55280](https://www.ncbi.nlm.nih.gov/gene/55280):

> This gene encodes a member of the CWF19 protein family. Mutations in this gene have been associated with autosomal recessive spinocerebellar ataxia-17 and mild cognitive disability. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:25613](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25613) · Entrez [55280](https://www.ncbi.nlm.nih.gov/gene/55280) · UniProt [Q69YN2](https://www.uniprot.org/uniprotkb/Q69YN2) · Ensembl [ENSG00000095485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095485)

## Data

Gene col 1746: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1746); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1746, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1746]; `tensor/DDL_lfc|DDL_z.npy` [1746]; `embed/gene_vectors.npy` [1746]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1746 or target_col == 1746). Every well: [[CWF19L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CWF19L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
