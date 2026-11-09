---
symbol: "FDX1"
type: "gene"
col: 6054
ensembl_id: "ENSG00000137714"
name: "ferredoxin 1"
location: "11q22.3"
module: 214
arm: "+"
pooled_cpm: 26.19
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/214"]
generated_by: "tahoemap"
---

# FDX1

*ferredoxin 1* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (17 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.24× (z +13.7, q 5e-40, up in 44 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.90× (z +10.9, q 1e-25, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM: 0.787× (z -3.9, q 0.059, down in 14 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.262×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (H4 0.122×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XPR1]] (+0.62, fdr 1e-05), [[CHPT1]] (+0.61, fdr 8e-06), [[SGPP1]] (+0.59, fdr 1e-05); moves opposite to [[GPATCH2L]] (-0.54, fdr 2e-05), [[TTC36]] (-0.53, fdr 3e-05), [[KIAA0753]] (-0.53, fdr 4e-05).
> It is in [[Module 214]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6054.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +13.7 | 5e-40 | 44/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.92×** | +11.1 | 5e-26 | 38/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.90×** | +10.9 | 1e-25 | 40/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +10.7 | 1e-24 | 42/48 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.84×** | +10.3 | 7e-23 | 41/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.79×** | +9.9 | 4e-21 | 42/47 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +9.2 | 2e-18 | 37/47 (NCI-H460, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.69×** | +8.9 | 5e-17 | 38/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.65×** | +8.2 | 1e-14 | 23/35 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +7.9 | 2e-13 | 34/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +7.7 | 6e-13 | 34/47 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.29×** | +6.2 | 3e-08 | 25/47 (LS 180, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +5.9 | 1e-07 | 27/47 (CFPAC-1, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.41×** | +5.6 | 9e-07 | 23/47 (SW480, A-427, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +5.6 | 1e-06 | 27/47 (RPMI-7951, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +5.1 | 1e-05 | 26/47 (NCI-H2347, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 6e-04 | 20/46 (Panc 03.27, A549, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +3.9 | 0.002 | 10/48 (CFPAC-1, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.14× | +3.1 | 0.039 | 8/48 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.049 | 13/47 (HOP62, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6054.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.262×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (H4 0.122×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.787×** | -3.9 | 0.059 | 14/47 (NCI-H1792, SK-MEL-2, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6054. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 32.5 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.74× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +11.3) | — |
| [[H4 (line)]] | wt | 15.9 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.122× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 23.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.07× (z +10.3) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[PANC-1 (line)]] | alt | 27.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.29× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6054), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPR1]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[CHPT1]] | +0.61 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[SGPP1]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[TMEM131L]] | +0.59 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[AGFG1]] | +0.59 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[SOAT1]] | +0.57 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[MT1A]] | +0.54 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[PPP4R1]] | +0.54 | +0.54 / +0.30 | both halves | 2e-04 |  |
| [[TBC1D2B]] | +0.53 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[PCNX1]] | +0.53 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[SESTD1]] | +0.53 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[PID1]] | +0.53 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH2L]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[TTC36]] | -0.53 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[KIAA0753]] | -0.53 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[ROPN1L]] | -0.53 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[SUPT6H]] | -0.53 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[ZNF543]] | -0.52 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[FANK1]] | -0.52 | -0.38 / -0.59 | both halves | 7e-05 |  |
| [[SP2]] | -0.51 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[ERI2]] | -0.51 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[ZNF546]] | -0.51 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[RECQL5]] | -0.51 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[GTF2F1]] | -0.50 | -0.53 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 214]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.699). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-5.5, -0.6); signed map (-28.3, -17.6). **Vector** length 82.0, 17.8% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +10.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | +3.9 | +4.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +13.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +7.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.0 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +3.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.5 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.4 | +0.1 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.5 | +5.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | +1.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | +2.0 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ferredoxin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:110,429,948-110,464,884 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ADX; previously FDX |
| Gene groups (HGNC) | Ferredoxin family |
| Hallmark sets | COMPLEMENT, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 14 pathways, smallest: Defective CYP11A1 causes AICSR; Electron transport from NADPH to Ferredoxin; Pregnenolone biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P10109](https://www.uniprot.org/uniprotkb/P10109) (Adrenodoxin, mitochondrial):

> Essential for the synthesis of various steroid hormones. Participates in the reduction of mitochondrial cytochrome P450 for steroidogenesis. Transfers electrons from adrenodoxin reductase to CYP11A1, a cytochrome P450 that catalyzes cholesterol side-chain cleavage. Does not form a ternary complex with adrenodoxin reductase and CYP11A1 but shuttles between the two enzymes to transfer electrons (By similarity).

**Summary**, from NCBI Gene [2230](https://www.ncbi.nlm.nih.gov/gene/2230):

> This gene encodes a small iron-sulfur protein that transfers electrons from NADPH through ferredoxin reductase to mitochondrial cytochrome P450, involved in steroid, vitamin D, and bile acid metabolism. Pseudogenes of this functional gene are found on chromosomes 20 and 21. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:3638](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3638) · Entrez [2230](https://www.ncbi.nlm.nih.gov/gene/2230) · UniProt [P10109](https://www.uniprot.org/uniprotkb/P10109) · Ensembl [ENSG00000137714](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137714)

## Data

Gene col 6054: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6054); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6054, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6054]; `tensor/DDL_lfc|DDL_z.npy` [6054]; `embed/gene_vectors.npy` [6054]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6054 or target_col == 6054). Every well: [[FDX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FDX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
