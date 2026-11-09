---
symbol: "COMMD4"
type: "gene"
col: 6394
ensembl_id: "ENSG00000140365"
name: "COMM domain containing 4"
location: "15q24.2"
module: 46
arm: "+"
pooled_cpm: 8.56
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# COMMD4

*COMM domain containing 4* — 15q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.52× (z +11.4, q 2e-27, up in 30 of 31 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 9.92×, PANC-1 5.08×, A498 5.45×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 5.46×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.606× (z -5.3, q 5e-05, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.129×; ⚠ cell-cycle shift, would explain all of this change); [[APTO-253 (drug)]] 0.05 µM in 1 line (Hs 766T 0.0590×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DYRK1A]] (+0.61, fdr 9e-05), [[HMGN2P5]] (+0.61, fdr 1e-05), [[RAF1]] (+0.58, fdr 2e-04); moves opposite to [[FLNB]] (-0.47, fdr 3e-04), [[HSP90B1]] (-0.45, fdr 1e-04), [[SNHG29]] (-0.45, fdr 8e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GOLGA2P5-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 8 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6394.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 9.92×, PANC-1 5.08×, A498 5.45×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 5.46×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **4.52×** | +11.4 | 2e-27 | 30/31 (NCI-H460, PANC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.19×** | +8.4 | 1e-14 | 11/12 (PANC-1, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.99×** | +7.7 | 4e-12 | 21/22 (A498, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.97×** | +5.1 | 4e-05 | 23/36 (SW1417, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.76×** | +4.1 | 0.004 | 22/38 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.0 | 0.005 | 19/36 (NCI-H2030, J82, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.35× | +3.2 | 0.11 | 20/44 (BT-474, NCI-H2347, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.33× | +3.1 | 0.16 | 11/48 (NCI-H2030, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6394.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.129×; ⚠ cell-cycle shift, would explain all of this change); [[APTO-253 (drug)]] 0.05 µM in 1 line (Hs 766T 0.0590×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.606×** | -5.3 | 5e-05 | 34/48 (LS 180, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.609× | -3.5 | 0.10 | 18/47 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.633× | -3.5 | 0.10 | 20/46 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6394. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.46× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A498 (line)]] | wt | 13.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[Hs 766T (line)]] | wt | 5.29 | 0 | 1 | — | [[APTO-253 (drug)]] 0.05 µM 0.0590× (z -8.5) |
| [[LS 180 (line)]] | wt | 7.20 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 6.22 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.92× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6394), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYRK1A]] | +0.61 | +0.36 / +0.52 | both halves | 9e-05 |  |
| [[HMGN2P5]] | +0.61 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[RAF1]] | +0.58 | +0.30 / +0.55 | both halves | 2e-04 |  |
| [[BLOC1S1]] | +0.58 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[THSD8]] ⚠ | +0.57 | +0.60 / +0.61 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[PXMP2]] | +0.57 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[TIMM10]] | +0.56 | +0.42 / +0.68 | both halves | 4e-05 |  |
| [[ALDH16A1]] | +0.55 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[C4orf46]] | +0.55 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[CENPS]] | +0.54 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[RPRD1B]] | +0.53 | +0.42 / +0.37 | both halves | 8e-05 |  |
| [[GTF3C6]] | +0.53 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[PKMYT1]] | +0.52 | +0.45 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLNB]] | -0.47 | -0.50 / -0.29 | both halves | 3e-04 |  |
| [[HSP90B1]] | -0.45 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[SNHG29]] | -0.45 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[EIF4E3]] | -0.45 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[SSR3]] | -0.45 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[PDE4DIP]] | -0.44 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[RFESD]] | -0.44 | -0.09 / -0.46 | ⚠ not reproduced | 0.003 |  |
| [[FLNB-AS1]] | -0.44 | -0.48 / -0.25 | both halves | 4e-04 |  |
| [[PABPC1]] | -0.44 | -0.17 / -0.52 | ⚠ one half (not replicated) | 0.001 |  |
| [[P4HB]] | -0.44 | -0.49 / -0.26 | both halves | 4e-04 |  |
| [[EEF2]] | -0.44 | -0.20 / -0.45 | ⚠ not reproduced | 8e-04 |  |
| [[MTFR1]] | -0.44 | -0.34 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GOLGA2P5-1]] | B | GOLGA2P5-1 activity raises COMMD4's level | lines that do not express GOLGA2P5-1 (8) vs lines expressing it (42) | 1.43× lower at baseline in the lines without GOLGA2P5-1 | 0.054 | ⚠ within organs, on part of the lines; also absent: GOLGA2P5, ENSG00000257489, KCNIP3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.490). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-46.8, -37.2); signed map (-36.5, -53.0). **Vector** length 52.0, 9.03% of its response variance represented; |z| ≥ 3 in 594 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.1 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +2.6 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +2.6 | +11.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +2.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.3 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.2 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.5 | -3.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | COMM domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.2 — chr15:75,336,020-75,343,224 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20452 |
| Gene groups (HGNC) | COMM domain containing; CCC complex |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0A8](https://www.uniprot.org/uniprotkb/Q9H0A8) (COMM domain-containing protein 4):

> Scaffold protein in the commander complex that is essential for endosomal recycling of transmembrane cargos; the commander complex is composed of the CCC subcomplex and the retriever subcomplex. May modulate activity of cullin-RING E3 ubiquitin ligase (CRL) complexes. Down-regulates activation of NF-kappa-B.

**Summary**, from NCBI Gene [54939](https://www.ncbi.nlm.nih.gov/gene/54939):

> Predicted to be involved in signal transduction. Located in cytosol. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26027](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26027) · Entrez [54939](https://www.ncbi.nlm.nih.gov/gene/54939) · UniProt [Q9H0A8](https://www.uniprot.org/uniprotkb/Q9H0A8) · Ensembl [ENSG00000140365](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140365)

## Data

Gene col 6394: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6394); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6394, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6394]; `tensor/DDL_lfc|DDL_z.npy` [6394]; `embed/gene_vectors.npy` [6394]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6394 or target_col == 6394). Every well: [[COMMD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COMMD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
