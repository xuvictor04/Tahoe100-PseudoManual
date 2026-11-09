---
symbol: "AIFM1"
type: "gene"
col: 8009
ensembl_id: "ENSG00000156709"
name: "apoptosis inducing factor mitochondria associated 1"
location: "Xq26.1"
module: 25
arm: "+"
pooled_cpm: 26.78
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# AIFM1

*apoptosis inducing factor mitochondria associated 1* — Xq26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.21× (z +18.7, q 0e+00, up in 42 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.50× (z +6.5, q 6e-09, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[GSK1059615 (drug)]] 5 µM: 0.596× (z -4.3, q 0.009, down in 21 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.115×; ⚠ cell-cycle shift, explains ~51% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLD]] (+0.69, fdr 1e-05), [[PROSER1]] (+0.66, fdr 7e-06), [[HNRNPR]] (+0.66, fdr 2e-05); moves opposite to [[RABGEF1]] (-0.67, fdr 7e-06), [[PHKG1]] (-0.65, fdr 1e-05), [[TPT1-AS1]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[S100A13]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8009.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.21×** | +18.7 | 0e+00 | 42/43 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.18×** | +17.8 | 0e+00 | 31/34 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.40×** | +13.0 | 4e-36 | 38/41 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.86×** | +9.9 | 6e-21 | 37/48 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.83×** | +9.7 | 5e-20 | 38/48 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.78×** | +8.9 | 6e-17 | 35/45 (NCI-H23, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.68×** | +8.3 | 1e-14 | 35/47 (HOP62, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.54×** | +6.6 | 3e-09 | 30/48 (SW480, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +6.5 | 6e-09 | 27/48 (A-427, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +6.3 | 2e-08 | 24/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.32×** | +6.2 | 3e-08 | 24/48 (KATO III, H4, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.40×** | +5.4 | 3e-06 | 22/46 (Hs 766T, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.36×** | +4.9 | 5e-05 | 25/48 (SNU-423, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.34×** | +4.7 | 1e-04 | 22/48 (LS 180, SW480, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **1.34×** | +4.7 | 1e-04 | 24/44 (HOP62, SW480, …) | all doses, flat | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.001 | 18/47 (SNU-423, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.008 | 12/47 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.008 | 17/47 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.48×** | +3.3 | 0.027 | 9/46 (NCI-H460, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.035 | 12/44 (NCI-H460, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.064 | 8/44 (NCI-H460, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Menadione (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.076 | 11/46 (HepG2/C3A, RKO, …) | top dose only |  |
| [[AZD-7648 (drug)]] 5 µM |  | **1.41×** | +2.9 | 0.078 | 4/45 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +2.8 | 0.086 | 5/48 (PANC-1, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8009.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.115×; ⚠ cell-cycle shift, explains ~51% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **0.596×** | -4.3 | 0.009 | 21/47 (A-427, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.782×** | -3.7 | 0.058 | 14/48 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Gallic acid (drug)]] 5 µM |  | 0.869× | -3.2 | 0.29 | 7/48 (J82, AN3 CA, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8009. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 28.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 29.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.45× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A549 (line)]] | wt | 21.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.43× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[J82 (line)]] | alt | 30.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 34.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.77× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 20.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.49× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H2030 (line)]] | alt | 30.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[PANC-1 (line)]] | alt | 42.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 24.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.55× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SW480 (line)]] | alt | 46.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[Hs 766T (line)]] | wt | 31.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H23 (line)]] | alt | 43.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H460 (line)]] | wt | 38.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.97× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 38.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A498 (line)]] | wt | 46.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[AN3 CA (line)]] | alt | 59.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.115× (z -10.9) ⚠ cell-cycle shift, explains ~51% of this change |
| [[H4 (line)]] | wt | 14.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +8.6) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[HepG2_C3A (line)]] | wt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.98× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 30.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[LOX-IMVI (line)]] | wt | 20.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-172 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8009), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLD]] | +0.69 | +0.55 / +0.72 | both halves | 1e-05 | same gene group; pathway: HALLMARK_ADIPOGENESIS; STRING 591 |
| [[PROSER1]] | +0.66 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[HNRNPR]] | +0.66 | +0.46 / +0.69 | both halves | 2e-05 |  |
| [[ATP5F1A]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 605 |
| [[IPO8]] | +0.65 | +0.43 / +0.71 | both halves | 4e-05 |  |
| [[GOT2]] | +0.65 | +0.57 / +0.69 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[SSX2IP]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[CAPRIN1]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[OCRL]] | +0.63 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[ICMT]] | +0.63 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[PRPS1]] | +0.63 | +0.47 / +0.69 | both halves | 2e-05 | STRING 698 |
| [[RUVBL1]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGEF1]] | -0.67 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[PHKG1]] | -0.65 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[TPT1-AS1]] | -0.63 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[GTF2B]] | -0.61 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[TPT1]] | -0.59 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[RSRP1]] | -0.59 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[ELL]] | -0.59 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[EIF1]] | -0.58 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[ZFAS1]] | -0.58 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[FAM53C]] | -0.58 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[PCF11-AS1]] | -0.58 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[RPS27]] | -0.57 | -0.52 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A13]] | C | S100A13 activity lowers AIFM1's level | lines that do not express S100A13 (4) vs lines expressing it (46) | 2.23× higher at baseline in the lines without S100A13 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CASP4, SP100, KIFC3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.640). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-25.7, -35.0); signed map (-17.3, -44.6). **Vector** length 72.7, 14.3% of its response variance represented; |z| ≥ 3 in 894 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +5.3 | +18.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +4.9 | +17.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +3.3 | +13.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | +3.2 | +8.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.2 | +6.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +1.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +0.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | -2.0 | +3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -0.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.7 | -1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | apoptosis inducing factor mitochondria associated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.1 — chrX:130,124,666-130,165,879 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AIF, CMTX4, DFNX5; previously PDCD8, NAMSD, AUNX1 |
| Gene groups (HGNC) | Flavoproteins; AIF family |
| Hallmark sets | ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Matched by | ensembl_id |

**Function**, from UniProt [O95831](https://www.uniprot.org/uniprotkb/O95831) (Apoptosis-inducing factor 1, mitochondrial):

> Functions both as NADH oxidoreductase and as regulator of apoptosis. In response to apoptotic stimuli, it is released from the mitochondrion intermembrane space into the cytosol and to the nucleus, where it functions as a pro-apoptotic factor in a caspase-independent pathway. Release into the cytoplasm is mediated upon binding to poly-ADP-ribose chains (By similarity). The soluble form (AIFsol) found in the nucleus induces 'parthanatos' i.e. caspase-independent fragmentation of chromosomal DNA. …

**Summary**, from NCBI Gene [9131](https://www.ncbi.nlm.nih.gov/gene/9131):

> This gene encodes a flavoprotein essential for nuclear disassembly in apoptotic cells, and it is found in the mitochondrial intermembrane space in healthy cells. Induction of apoptosis results in the translocation of this protein to the nucleus where it affects chromosome condensation and fragmentation. In addition, this gene product induces mitochondria to release the apoptogenic proteins cytochrome c and caspase-9. Mutations in this gene cause combined oxidative phosphorylation deficiency 6 …

**Accessions** — [HGNC:8768](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8768) · Entrez [9131](https://www.ncbi.nlm.nih.gov/gene/9131) · UniProt [O95831](https://www.uniprot.org/uniprotkb/O95831) · Ensembl [ENSG00000156709](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156709)

## Data

Gene col 8009: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8009); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8009, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8009]; `tensor/DDL_lfc|DDL_z.npy` [8009]; `embed/gene_vectors.npy` [8009]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8009 or target_col == 8009). Every well: [[AIFM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AIFM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
