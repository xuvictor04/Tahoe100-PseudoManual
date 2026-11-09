---
symbol: "RBM12B"
type: "gene"
col: 11459
ensembl_id: "ENSG00000183808"
name: "RNA binding motif protein 12B"
location: "8q22.1"
module: 7
arm: "+"
pooled_cpm: 47.64
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# RBM12B

*RNA binding motif protein 12B* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.41× (z +5.4, q 4e-05, up in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (NCI-H1573 2.31×).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.573× (z -8.7, q 1e-15, down in 36 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Budesonide (drug)]] 0.05 µM: 0.804× (z -3.4, q 0.030, down in 19 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBLL1]] (+0.64, fdr 1e-05), [[ATPSCKMT]] (+0.62, fdr 1e-05), [[FBXO30]] (+0.61, fdr 1e-05); moves opposite to [[NKTR]] (-0.62, fdr 1e-05), [[LLGL2]] (-0.59, fdr 6e-05), [[DNAJC1]] (-0.56, fdr 5e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11459.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (NCI-H1573 2.31×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +5.4 | 4e-05 | 32/48 (C32, LS 180, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.21×** | +4.2 | 0.007 | 24/48 (HS-578T, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.6 | 0.051 | 17/48 (A498, SW 900, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.23× | +3.3 | 0.13 | 14/48 (LoVo, HT-29, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.15× | +3.1 | 0.26 | 7/48 (NCI-H460, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11459.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.573×** | -8.7 | 1e-15 | 36/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.602×** | -7.7 | 6e-12 | 38/47 (NCI-H23, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.651×** | -6.7 | 4e-09 | 32/48 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.894× | -5.8 | 1e-06 | 6/48 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.727×** | -5.0 | 7e-05 | 27/48 (HEC-1-A, SW1417, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **0.758×** | -4.3 | 0.001 | 26/48 (NCI-H23, C32, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.764×** | -4.2 | 0.002 | 25/48 (SW1417, HEC-1-A, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.611×** | -4.0 | 0.004 | 19/37 (SNU-423, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.778×** | -3.8 | 0.010 | 22/42 (A-172, NCI-H1573, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.783×** | -3.5 | 0.022 | 22/45 (HCT15, HOP62, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | 0.852× | -3.5 | 0.022 | 21/47 (HEC-1-A, A-427, …) | top dose only | composition shift |
| [[Budesonide (drug)]] 0.05 µM |  | **0.804×** | -3.4 | 0.030 | 19/48 (SNU-423, HOP62, …) | inconsistent across doses | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.743×** | -3.3 | 0.039 | 17/48 (C-33 A, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.813×** | -3.2 | 0.051 | 22/48 (HEC-1-A, SW1417, …) | rises with dose | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.679×** | -3.2 | 0.057 | 16/42 (COLO 205, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.755×** | -3.1 | 0.060 | 20/48 (COLO 205, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11459. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 68.1 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.31× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.133× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[NCI-H23 (line)]] | alt | 65.5 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.235× (z -14.7) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 67.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[PANC-1 (line)]] | alt | 51.5 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.310× (z -12.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 42.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0858× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[HEC-1-A (line)]] | alt | 73.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -10.6) ⚠ cell-cycle shift, explains ~85% of this change |
| [[SK-MEL-2 (line)]] | alt | 66.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[SW480 (line)]] | alt | 54.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.324× (z -13.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 45.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -8.8) ⚠ cell-cycle shift, explains ~85% of this change |
| [[C-33 A (line)]] | alt | 62.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[C32 (line)]] | wt | 44.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[HCT15 (line)]] | alt | 53.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0840× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[HepG2_C3A (line)]] | wt | 35.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.199× (z -9.3) ⚠ toxic |
| [[HOP62 (line)]] | alt | 55.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.359× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[SNU-1 (line)]] | wt | 49.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.249× (z -8.8) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 44.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0297× (z -14.2) ⚠ toxic |
| [[A498 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 67.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11459), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBLL1]] | +0.64 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ATPSCKMT]] | +0.62 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[FBXO30]] | +0.61 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[GTF3C4]] | +0.59 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[CHTF8]] | +0.59 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[ZNF808]] | +0.59 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[AP5M1]] | +0.59 | +0.53 / +0.36 | both halves | 1e-04 |  |
| [[C17orf80]] | +0.59 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[ZNF189]] | +0.58 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[SMG8]] | +0.58 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[PSMD7]] | +0.58 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[ZNF91]] | +0.57 | +0.48 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKTR]] | -0.62 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[LLGL2]] | -0.59 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[DNAJC1]] | -0.56 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[SIRT2]] | -0.55 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ARL3]] | -0.54 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[TTC3]] | -0.53 | -0.57 / -0.28 | both halves | 3e-04 |  |
| [[ESYT2]] | -0.53 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[FOXO6]] | -0.52 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[PPP1R2]] | -0.52 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[USP2]] | -0.52 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[NOS1AP]] | -0.51 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[PDXDC2P-NPIPB14P]] | -0.51 | -0.55 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.585). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-17.3, 11.0); signed map (3.5, -33.3). **Vector** length 93.1, 21.3% of its response variance represented; |z| ≥ 3 in 831 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.3 | +5.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +5.0 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +2.3 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -5.0 | -5.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.4 | -7.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -4.4 | -3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -3.8 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | -3.3 | -4.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.2 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.1 | -3.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 12B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:93,728,155-93,741,017 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

UniProt [Q8IXT5](https://www.uniprot.org/uniprotkb/Q8IXT5) carries no function annotation.

**Summary**, from NCBI Gene [389677](https://www.ncbi.nlm.nih.gov/gene/389677):

> Enables RNA binding activity. Predicted to be involved in regulation of RNA splicing. Predicted to be part of ribonucleoprotein complex. Predicted to be active in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:32310](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32310) · Entrez [389677](https://www.ncbi.nlm.nih.gov/gene/389677) · UniProt [Q8IXT5](https://www.uniprot.org/uniprotkb/Q8IXT5) · Ensembl [ENSG00000183808](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183808)

## Data

Gene col 11459: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11459); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11459, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11459]; `tensor/DDL_lfc|DDL_z.npy` [11459]; `embed/gene_vectors.npy` [11459]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11459 or target_col == 11459). Every well: [[RBM12B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM12B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
