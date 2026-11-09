---
symbol: "TMC3-AS1"
type: "gene"
col: 15188
ensembl_id: "ENSG00000259343"
name: "TMC3 antisense RNA 1"
location: "15q25.1"
module: 49
arm: "+"
pooled_cpm: 4.66
n_lines_expressing: 46
n_dd_up: 24
n_dd_down: 12
n_dd_up_clean: 20
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# TMC3-AS1

*TMC3 antisense RNA 1* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.75× (z +13.4, q 4e-38, up in 38 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.389× (z -8.2, q 2e-13, down in 20 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.415× (z -7.6, q 5e-12, down in 23 of 40 measured lines).
> Its strongest partners by |cos| (77 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO16]] (+0.58, fdr 2e-05), [[GOLGA4]] (+0.58, fdr 2e-05), [[KCNK15-AS1]] (+0.58, fdr 4e-05); moves opposite to [[MAP2K4]] (-0.47, fdr 8e-05), [[SNTB2]] (-0.45, fdr 2e-04), [[TOR1A]] (-0.44, fdr 2e-04).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CAPN14]] → it (grade B ⚠); 3 go from it, the strongest it → [[LINC01117]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15188.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.75×** | +13.4 | 4e-38 | 38/43 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.99×** | +13.3 | 6e-38 | 36/42 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.48×** | +10.7 | 1e-24 | 34/41 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.15×** | +9.5 | 4e-19 | 2/5 (J82, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.15×** | +9.3 | 1e-18 | 20/34 (LoVo, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.85×** | +9.0 | 2e-17 | 30/41 (SW1417, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.75×** | +8.7 | 3e-16 | 30/39 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.66×** | +8.4 | 3e-15 | 31/42 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.61×** | +8.2 | 1e-14 | 27/40 (NCI-H1573, J82, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **2.16×** | +6.6 | 2e-09 | 20/40 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +5.5 | 2e-06 | 2/10 (HEC-1-A, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.32×** | +5.4 | 3e-06 | 15/38 (HOP62, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +5.3 | 5e-06 | 8/17 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +4.8 | 6e-05 | 15/40 (HT-29, H4, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **1.67×** | +4.2 | 0.001 | 14/43 (NCI-H2030, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.63×** | +4.0 | 0.002 | 8/32 (SW480, HOP62, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.39×** | +3.9 | 0.003 | 11/42 (SW480, NCI-H1573, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.011 | 10/32 (A549, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15188.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.389×** | -8.2 | 2e-13 | 20/27 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.396×** | -8.0 | 3e-13 | 29/43 (NCI-H1573, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.415×** | -7.6 | 5e-12 | 23/40 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.472×** | -6.5 | 1e-08 | 19/41 (HCT15, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.557×** | -5.1 | 4e-05 | 19/38 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.541×** | -5.0 | 5e-05 | 16/37 (A498, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.611×** | -4.3 | 0.002 | 19/40 (SW48, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.605×** | -4.2 | 0.002 | 18/38 (A498, LS 180, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.659×** | -3.6 | 0.018 | 8/38 (PANC-1, SNU-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.468×** | -3.4 | 0.034 | 12/36 (A498, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.681×** | -3.3 | 0.042 | 7/42 (SNU-423, NCI-H2030, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.696×** | -3.2 | 0.075 | 4/43 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 0.512× | -3.0 | 0.10 | 7/23 (SW48, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.513× | -3.0 | 0.10 | 11/29 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15188. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 22.8 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0953× (z -19.7) |
| [[HOP62 (line)]] | alt | 3.89 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 6.17× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.0744× (z -9.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 3.08 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0449× (z -12.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 3.48 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0296× (z -11.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 5.41 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0848× (z -9.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 8.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.87× (z +12.8) | — |
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0648× (z -11.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 1.74 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0502× (z -10.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW48 (line)]] | wt | 12.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0763× (z -8.9) |
| [[A-172 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.726 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15188), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 19 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO16]] | +0.58 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[GOLGA4]] | +0.58 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[KCNK15-AS1]] | +0.58 | +0.42 / +0.69 | both halves | 4e-05 | same gene group |
| [[CCDC110]] | +0.54 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[ZNF815P]] | +0.54 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[LINC00408]] | +0.52 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[SEC11C]] | +0.51 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[SAR1B]] | +0.51 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[KSR2]] | +0.49 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[SEC63]] | +0.48 | +0.12 / +0.52 | ⚠ one half (not replicated) | 0.002 |  |
| [[TTC3]] | +0.47 | +0.14 / +0.57 | ⚠ one half (not replicated) | 0.002 |  |
| [[CREB3L2]] | +0.46 | +0.26 / +0.47 | both halves | 4e-04 |  |
| [[KLHL32]] | +0.46 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[LINC01117]] | +0.46 | +0.51 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP2K4]] | -0.47 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[SNTB2]] | -0.45 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[TOR1A]] | -0.44 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[E2F3]] | -0.44 | -0.23 / -0.50 | both halves | 5e-04 |  |
| [[MRPS15]] | -0.44 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[LARS2]] | -0.43 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[PITPNC1]] | -0.43 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[CSRNP2]] | -0.43 | +0.06 / -0.48 | ⚠ not reproduced | 1.00 |  |
| [[UROD]] | -0.43 | -0.16 / -0.41 | ⚠ not reproduced | 0.001 |  |
| [[CDIPT]] | -0.41 | -0.27 / -0.32 | both halves | 3e-04 |  |
| [[LYPLA2]] | -0.41 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[POC1B]] | -0.41 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[GSTCD]] | -0.41 | -0.26 / -0.22 | both halves | 6e-04 |  |
| [[PSEN1]] | -0.40 | -0.28 / -0.53 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAPN14]] | B | CAPN14 activity raises TMC3-AS1's level | lines that do not express CAPN14 (16) vs lines expressing it (34) | 1.43× lower at baseline in the lines without CAPN14 | 0.012 | ⚠ within organs, on part of the lines; also absent: CFAP46, EBF2, GAS7; maybe low, not absent |
| [[KLRG1]] | B | KLRG1 activity raises TMC3-AS1's level | lines that do not express KLRG1 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without KLRG1 | 0.085 | ⚠ within organs, on part of the lines; also absent: DUXAP10, CD226, DUXAP8; maybe low, not absent |
| [[HBG2]] | B | HBG2 activity raises TMC3-AS1's level | lines that do not express HBG2 (17) vs lines expressing it (33) | 1.76× lower at baseline in the lines without HBG2 | 0.097 | ⚠ within organs, on part of the lines; also absent: OR51B5, MKRN3, ENSG00000234147; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01117]] | C | TMC3-AS1 activity raises LINC01117's level | lines that do not express TMC3-AS1 (4) vs lines expressing it (46) | 3.26× lower at baseline in the lines without TMC3-AS1 | 0.015 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000243944, PAQR8, LINC01277; maybe low, not absent |
| [[CCDC7]] | C | TMC3-AS1 activity raises CCDC7's level | lines that do not express TMC3-AS1 (4) vs lines expressing it (46) | 1.75× lower at baseline in the lines without TMC3-AS1 | 0.059 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000243944, PAQR8, LINC01277; maybe low, not absent |
| [[ZNF652]] | C | TMC3-AS1 activity raises ZNF652's level | lines that do not express TMC3-AS1 (4) vs lines expressing it (46) | 1.62× lower at baseline in the lines without TMC3-AS1 | 0.070 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000243944, PAQR8, LINC01277; maybe low, not absent |

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.447). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.7, 34.0); signed map (24.4, 17.4). **Vector** length 67.0, 11.3% of its response variance represented; |z| ≥ 3 in 1,153 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +13.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +8.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +2.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.3 | +0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -0.7 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -1.3 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | TMC3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q25.1 — chr15:81,324,338-81,518,200 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51424](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51424) · Entrez [101929655](https://www.ncbi.nlm.nih.gov/gene/101929655) · Ensembl [ENSG00000259343](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259343)

## Data

Gene col 15188: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15188); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15188, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15188]; `tensor/DDL_lfc|DDL_z.npy` [15188]; `embed/gene_vectors.npy` [15188]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15188 or target_col == 15188). Every well: [[TMC3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMC3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
