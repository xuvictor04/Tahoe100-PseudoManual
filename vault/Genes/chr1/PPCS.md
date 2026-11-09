---
symbol: "PPCS"
type: "gene"
col: 4790
ensembl_id: "ENSG00000127125"
name: "phosphopantothenoylcysteine synthetase"
location: "1p34.2"
module: 11
arm: "+"
pooled_cpm: 27.5
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# PPCS

*phosphopantothenoylcysteine synthetase* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.67× (z +5.1, q 9e-05, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.422× (z -8.6, q 4e-15, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1orf131]] (+0.81, fdr 7e-06), [[RPP25L]] (+0.78, fdr 7e-06), [[SNW1]] (+0.76, fdr 7e-06); moves opposite to [[TCF3]] (-0.68, fdr 1e-05), [[TPST2]] (-0.65, fdr 1e-05), [[CPSF6]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MARVELD2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4790.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.67×** | +5.1 | 9e-05 | 34/47 (HOP62, LS 180, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.66×** | +5.1 | 9e-05 | 35/47 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.7 | 6e-04 | 34/46 (RKO, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.5 | 8e-04 | 29/43 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.51×** | +4.0 | 0.006 | 24/46 (LS 180, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +4.0 | 0.006 | 21/35 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.53×** | +4.0 | 0.006 | 30/45 (COLO 205, HS-578T, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.48×** | +3.9 | 0.006 | 23/43 (HEC-1-A, NCI-H2347, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.021 | 24/47 (HS-578T, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.26×** | +3.3 | 0.051 | 25/47 (PANC-1, HEC-1-A, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.35× | +3.0 | 0.13 | 18/46 (A498, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4790.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.422×** | -8.6 | 4e-15 | 41/47 (HT-29, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.432×** | -8.4 | 2e-14 | 43/46 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.545×** | -6.1 | 3e-07 | 34/46 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.561×** | -5.8 | 1e-06 | 38/46 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.497×** | -3.7 | 0.027 | 28/45 (A-427, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.695×** | -3.6 | 0.027 | 23/46 (SW48, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.715×** | -3.3 | 0.063 | 22/46 (SNU-1, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.716×** | -3.3 | 0.063 | 23/46 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4790. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.8 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.212× (z -10.3) |
| [[LoVo (line)]] | wt | 33.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -13.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 39.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.205× (z -10.1) |
| [[PANC-1 (line)]] | alt | 43.6 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.323× (z -8.7) |
| [[BT-474 (line)]] | alt | 22.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.185× (z -9.1) |
| [[HCT15 (line)]] | alt | 35.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.202× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 40.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[RPMI-7951 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -9.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0841× (z -11.7) |
| [[A-172 (line)]] | wt | 6.69 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4790), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf131]] | +0.81 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.78 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[SNW1]] | +0.76 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[NSMCE3]] | +0.76 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[RPP38]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.74 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[TRMT1L]] | +0.73 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[SDSL]] | +0.72 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[FDX2]] | +0.70 | +0.56 / +0.77 | both halves | 1e-05 |  |
| [[BTN2A1]] | +0.70 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[MRPS31]] | +0.70 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[PEX12]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF3]] | -0.68 | -0.73 / -0.52 | both halves | 1e-05 |  |
| [[TPST2]] | -0.65 | -0.76 / -0.49 | both halves | 1e-05 |  |
| [[CPSF6]] | -0.61 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[APMAP]] | -0.61 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[COLGALT1]] | -0.61 | -0.62 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MARVELD2]] | B | MARVELD2 activity raises PPCS's level | lines that do not express MARVELD2 (14) vs lines expressing it (36) | 1.42× lower at baseline in the lines without MARVELD2 | 0.038 | ⚠ within organs, on part of the lines; also absent: CHMP4C, ARHGEF5, LLGL2; maybe low, not absent |
| [[CDKN2B]] | C | CDKN2B activity strengthens PPCS's drug response | recorded loss-of-function mutation of CDKN2B in 11 lines vs 36 not recorded | the CDKN2B-altered lines respond 1.01× as strongly (z diff -0.01); strongest at Homoharringtonine 0.05 µM: 1.47x vs 1.67x (z diff +1.6) | 0.203 over the table, 0.070 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines; target measured in part of the lines; both ways; the reference differs; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.753). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.4, 4.8); signed map (1.9, -18.4). **Vector** length 80.8, 21.7% of its response variance represented; |z| ≥ 3 in 738 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.3 | +5.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +6.0 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.4 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.8 | +2.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | -3.5 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Baicalin (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | phosphopantothenoylcysteine synthetase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:42,456,117-42,473,385 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11838 |
| Gene groups (HGNC) | Ligases |
| Reactome | 4 pathways, smallest: Coenzyme A biosynthesis; Vitamin B5 (pantothenate) metabolism; Metabolism of water-soluble vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAB8](https://www.uniprot.org/uniprotkb/Q9HAB8) (Phosphopantothenate--cysteine ligase):

> Catalyzes the second step in the biosynthesis of coenzyme A from vitamin B5, where cysteine is conjugated to 4'-phosphopantothenate to form 4-phosphopantothenoylcysteine. Has a preference for ATP over CTP as a cosubstrate.

**Summary**, from NCBI Gene [79717](https://www.ncbi.nlm.nih.gov/gene/79717):

> Biosynthesis of coenzyme A (CoA) from pantothenic acid (vitamin B5) is an essential universal pathway in prokaryotes and eukaryotes. PPCS (EC 6.3.2.5), one of the last enzymes in this pathway, converts phosphopantothenate to phosphopantothenoylcysteine (Daugherty et al., 2002 [PubMed 11923312]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:25686](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25686) · Entrez [79717](https://www.ncbi.nlm.nih.gov/gene/79717) · UniProt [Q9HAB8](https://www.uniprot.org/uniprotkb/Q9HAB8) · Ensembl [ENSG00000127125](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127125)

## Data

Gene col 4790: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4790); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4790, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4790]; `tensor/DDL_lfc|DDL_z.npy` [4790]; `embed/gene_vectors.npy` [4790]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4790 or target_col == 4790). Every well: [[PPCS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPCS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
