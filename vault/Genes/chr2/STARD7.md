---
symbol: "STARD7"
type: "gene"
col: 1392
ensembl_id: "ENSG00000084090"
name: "StAR related lipid transfer domain containing 7"
location: "2q11.2"
module: 33
arm: "+"
pooled_cpm: 41.41
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# STARD7

*StAR related lipid transfer domain containing 7* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (13 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.04× (z +13.1, q 2e-36, up in 39 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.132×, C-33 A 0.244×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 0.350×, A549 0.173×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ipatasertib (drug)]] 0.5 µM in 1 line (SNU-1 0.0659×); [[Cysteamine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H661 0.120×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC123]] (+0.71, fdr 7e-06), [[ELAC2]] (+0.68, fdr 9e-06), [[POP1]] (+0.68, fdr 7e-06); moves opposite to [[NFKBIB]] (-0.57, fdr 1e-05), [[OFD1]] (-0.56, fdr 1e-05), [[TNRC6C]] (-0.55, fdr 9e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1392.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.04×** | +13.1 | 2e-36 | 39/48 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.02×** | +12.9 | 7e-36 | 44/48 (AsPC-1, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.86×** | +11.4 | 5e-28 | 41/48 (A498, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.84×** | +11.2 | 8e-27 | 41/48 (NCI-H1792, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.85×** | +10.7 | 1e-24 | 35/48 (NCI-H23, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.78×** | +10.2 | 3e-22 | 38/46 (NCI-H2030, SW1417, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.72×** | +10.0 | 2e-21 | 42/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +8.3 | 5e-15 | 4/48 (NCI-H2030, NCI-H661, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.14×** | +7.3 | 1e-11 | 33/48 (HEC-1-A, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +6.2 | 4e-08 | 25/48 (A549, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.37×** | +5.7 | 5e-07 | 29/48 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +5.5 | 2e-06 | 29/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.34×** | +5.0 | 2e-05 | 29/47 (HEC-1-A, C32, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.31×** | +5.0 | 3e-05 | 26/48 (LoVo, SW1417, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +4.8 | 6e-05 | 26/48 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.002 | 18/48 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.006 | 20/48 (RKO, NCI-H1573, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.012 | 13/48 (LoVo, NCI-H460, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.024 | 13/48 (A-172, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.1 | 0.038 | 10/48 (HepG2/C3A, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1392.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.132×, C-33 A 0.244×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 0.350×, A549 0.173×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ipatasertib (drug)]] 0.5 µM in 1 line (SNU-1 0.0659×); [[Cysteamine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H661 0.120×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.825× | -3.6 | 0.19 | 17/48 (A498, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1392. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 31.7 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.75× (z +10.8) | — |
| [[A498 (line)]] | wt | 56.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.02× (z +9.0) ⚠ cell-cycle shift, explains ~44% of this change | [[Dinaciclib (drug)]] 5 µM 0.350× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 32.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.55× (z +11.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 47.7 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.54× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 83.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.29× (z +11.5) | — |
| [[NCI-H460 (line)]] | wt | 41.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.58× (z +8.7) | — |
| [[A-427 (line)]] | wt | 40.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 29.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.34× (z +9.1) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[C-33 A (line)]] | alt | 64.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 41.6 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0826× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 32.7 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.82× (z +10.2) ⚠ unreliable plate only | — |
| [[NCI-H2030 (line)]] | alt | 53.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.51× (z +9.2) ⚠ toxic; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H661 (line)]] | alt | 64.5 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.05 µM 0.120× (z -9.1) |
| [[PANC-1 (line)]] | alt | 42.7 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.35× (z +10.3) | — |
| [[RKO (line)]] | wt | 53.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 35.5 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0659× (z -12.4) |
| [[AN3 CA (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 63.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1392), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC123]] | +0.71 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[ELAC2]] | +0.68 | +0.76 / +0.57 | both halves | 9e-06 |  |
| [[POP1]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[RITA1]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[CCT3]] | +0.66 | +0.73 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[CHCHD6]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[PHB1]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[NKRF]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[POLR3B]] | +0.64 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[VWA8]] | +0.64 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[NAA25]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKBIB]] | -0.57 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[OFD1]] | -0.56 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.55 | -0.60 / -0.37 | both halves | 9e-05 |  |
| [[LRCH3]] | -0.54 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[ANKRD12]] | -0.54 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[CEP95]] | -0.54 | -0.63 / -0.35 | both halves | 1e-04 |  |
| [[SMIM14]] | -0.54 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[XIAP]] | -0.53 | -0.53 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.654). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.0, -33.7); signed map (-11.5, -50.0). **Vector** length 97.9, 23.6% of its response variance represented; |z| ≥ 3 in 987 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.2 | +13.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.3 | +10.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.8 | +10.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.3 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | +4.6 | +10.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.5 | +5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.6 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.4 | -1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.7 | +0.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.4 | +1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -3.2 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | +1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | -2.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.5 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | StAR related lipid transfer domain containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:96,184,859-96,208,827 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GTT1 |
| Gene groups (HGNC) | StAR related lipid transfer domain containing |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 8 pathways, smallest: Ubiquinol biosynthesis; Metabolism of cofactors; Synthesis of PC |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQZ5](https://www.uniprot.org/uniprotkb/Q9NQZ5) (StAR-related lipid transfer protein 7, mitochondrial):

> Mediates non-vesicular transfer of phosphatidylcholine to mitochondria, thereby maintaining mitochondrial membrane lipid composition, cristae organization, and respiratory function across diverse tissues.; [StAR-related lipid transfer protein 7, mitochondrial]: Transfers phosphatidylcholine (PC) from the endoplasmic reticulum to the mitochondrial outer membrane at ER-mitochondria contact sites, thereby maintaining mitochondrial PC content, respiratory complex stability and mitochondrial cristae …

**Summary**, from NCBI Gene [56910](https://www.ncbi.nlm.nih.gov/gene/56910):

> Enables phosphatidylcholine transfer activity. Involved in intermembrane phospholipid transfer; mitochondrial membrane organization; and regulation of cellular respiration. Located in cytosol; mitochondrial intermembrane space; and mitochondrial outer membrane. Implicated in familial adult myoclonic epilepsy 2. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18063](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18063) · Entrez [56910](https://www.ncbi.nlm.nih.gov/gene/56910) · UniProt [Q9NQZ5](https://www.uniprot.org/uniprotkb/Q9NQZ5) · Ensembl [ENSG00000084090](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084090)

## Data

Gene col 1392: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1392); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1392, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1392]; `tensor/DDL_lfc|DDL_z.npy` [1392]; `embed/gene_vectors.npy` [1392]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1392 or target_col == 1392). Every well: [[STARD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STARD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
