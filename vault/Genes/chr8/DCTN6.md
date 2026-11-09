---
symbol: "DCTN6"
type: "gene"
col: 2480
ensembl_id: "ENSG00000104671"
name: "dynactin subunit 6"
location: "8p12"
module: 12
arm: "+"
pooled_cpm: 18.29
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# DCTN6

*dynactin subunit 6* — 8p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.98× (z +8.6, q 3e-15, up in 30 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.52× (z +5.3, q 2e-05, up in 29 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.547× (z -7.7, q 1e-11, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMADHC]] (+0.76, fdr 7e-06), [[CCDC43]] (+0.68, fdr 7e-06), [[OCIAD1]] (+0.68, fdr 7e-06); moves opposite to [[COLGALT1]] (-0.68, fdr 7e-06), [[SETD3]] (-0.65, fdr 9e-06), [[MLEC]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2480.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +8.6 | 3e-15 | 30/40 (RPMI-7951, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +6.0 | 7e-07 | 19/31 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.56×** | +5.4 | 1e-05 | 27/47 (NCI-H460, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +5.3 | 2e-05 | 29/46 (A-427, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +4.7 | 3e-04 | 25/47 (AsPC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +4.7 | 3e-04 | 24/48 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +4.2 | 0.002 | 21/47 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +4.0 | 0.005 | 19/48 (KATO III, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.36×** | +3.9 | 0.006 | 22/47 (NCI-H1792, RKO, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.31×** | +3.4 | 0.039 | 16/46 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~78% of this change | **1.28×** | +3.1 | 0.094 | 19/45 (AsPC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.27× | +3.0 | 0.12 | 10/48 (SNU-1, AsPC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2480.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.547×** | -7.7 | 1e-11 | 40/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.598×** | -6.5 | 2e-08 | 38/47 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.699×** | -6.4 | 2e-08 | 29/47 (AsPC-1, SW48, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.625×** | -6.0 | 4e-07 | 30/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -4.2 | 0.004 | 20/46 (HS-578T, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.739×** | -3.8 | 0.012 | 17/48 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.598×** | -3.3 | 0.080 | 13/48 (A498, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -3.3 | 0.080 | 6/48 (NCI-H23, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2480. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 17.4 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.254× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 22.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -10.2) |
| [[H4 (line)]] | wt | 20.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 22.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -8.6) |
| [[LoVo (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -11.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 22.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -8.9) |
| [[SW480 (line)]] | alt | 21.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -11.0) |
| [[A-172 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2480), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMADHC]] | +0.76 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[CCDC43]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[OCIAD1]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[PDRG1]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[WASHC1]] | +0.67 | +0.76 / +0.49 | both halves | 1e-05 |  |
| [[SEC62]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[NMT1]] | +0.66 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[COIL]] | +0.66 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[CWC22]] | +0.66 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[SNRNP27]] | +0.65 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[CCDC174]] | +0.65 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[NFU1]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COLGALT1]] | -0.68 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[SETD3]] | -0.65 | -0.57 / -0.66 | both halves | 9e-06 |  |
| [[MLEC]] | -0.63 | -0.57 / -0.57 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[RBBP7]] | -0.62 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[CDK2]] | -0.62 | -0.68 / -0.45 | both halves | 3e-05 |  |
| [[ADAM15]] | -0.62 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[NAGA]] | -0.61 | -0.57 / -0.49 | both halves | 2e-05 |  |
| [[SLC25A39]] | -0.61 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[IMPA2]] | -0.60 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[AKT1]] | -0.60 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[WRNIP1]] | -0.60 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[NTAQ1]] | -0.58 | -0.49 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises DCTN6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DNAJC18]] | C | DNAJC18 activity lowers DCTN6's level | lines that do not express DNAJC18 (4) vs lines expressing it (46) | 1.71× higher at baseline in the lines without DNAJC18 | 0.034 | ⚠ few lines (4 vs 46); across organs; also absent: TBKBP1, TTC23L, TMEFF1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.711). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-34.0, 3.7); signed map (-0.3, -17.3). **Vector** length 56.0, 9.56% of its response variance represented; |z| ≥ 3 in 641 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.0 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +5.0 | +3.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +4.1 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +3.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.2 | -6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.2 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -0.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.8 | -6.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.5 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.9 | -2.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | +1.1 |
|  | [[Tirabrutinib (drug)]] 0.05 µM |  | -0.8 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | dynactin subunit 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p12 — chr8:30,156,319-30,183,639 (+) |
| Ensembl biotype | protein_coding |
| Also known as | WS-3, p27 |
| Gene groups (HGNC) | Dynactin subunits |
| Reactome | 17 pathways, smallest: COPI-independent Golgi-to-ER retrograde traffic; HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; Processing of antigen in germinal center B cells |
| Matched by | ensembl_id |

**Function**, from UniProt [O00399](https://www.uniprot.org/uniprotkb/O00399) (Dynactin subunit 6):

> Part of the dynactin complex that activates the molecular motor dynein for ultra-processive transport along microtubules.

**Summary**, from NCBI Gene [10671](https://www.ncbi.nlm.nih.gov/gene/10671):

> The protein encoded by this gene contains an RGD (Arg-Gly-Asp) motif in the N-terminal region, which confers adhesive properties to macromolecular proteins like fibronectin. It shares a high degree of sequence similarity with the mouse homolog, which has been suggested to play a role in mitochondrial biogenesis. The exact biological function of this gene is not known. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16964](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16964) · Entrez [10671](https://www.ncbi.nlm.nih.gov/gene/10671) · UniProt [O00399](https://www.uniprot.org/uniprotkb/O00399) · Ensembl [ENSG00000104671](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104671)

## Data

Gene col 2480: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2480); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2480, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2480]; `tensor/DDL_lfc|DDL_z.npy` [2480]; `embed/gene_vectors.npy` [2480]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2480 or target_col == 2480). Every well: [[DCTN6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCTN6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
