---
symbol: "UBR4"
type: "gene"
col: 4813
ensembl_id: "ENSG00000127481"
name: "ubiquitin protein ligase E3 component n-recognin 4"
location: "1p36.13"
module: 198
arm: "+"
pooled_cpm: 276.68
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 6
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/198"]
generated_by: "tahoemap"
---

# UBR4

*ubiquitin protein ligase E3 component n-recognin 4* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.02× (z +12.6, q 2e-33, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.639× (z -7.7, q 6e-12, down in 43 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 0.825× (z -3.5, q 0.060, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HepG2/C3A 0.469×, HEC-1-A 0.537×, SW 900 0.517×, NCI-H2347 0.577×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.297×, SW 900 0.481×, Panc 03.27 0.507×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.388×, A-172 0.540×, hTERT-HPNE 0.459×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DYNC1H1]] (+0.59, fdr 1e-05), [[CEP170B]] (+0.59, fdr 1e-05), [[ABCB8]] (+0.57, fdr 2e-05); moves opposite to [[RCHY1]] (-0.57, fdr 1e-05), [[ILF3-DT]] (-0.56, fdr 5e-05), [[SLC25A12]] (-0.54, fdr 2e-05).
> It is in [[Module 198]], a single-armed module (Antigen processing: Ubiquitination & Proteasome degradation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4813.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.02×** | +12.6 | 2e-33 | 48/48 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +11.3 | 6e-27 | 36/48 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.82×** | +10.7 | 3e-24 | 46/48 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.74×** | +9.3 | 2e-18 | 45/48 (COLO 205, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.68×** | +9.2 | 4e-18 | 46/48 (COLO 205, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +8.2 | 2e-14 | 47/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +7.9 | 2e-13 | 41/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +7.4 | 7e-12 | 44/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +6.3 | 2e-08 | 43/48 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +6.2 | 3e-08 | 35/48 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +5.8 | 4e-07 | 33/48 (COLO 205, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +4.9 | 5e-05 | 33/48 (C32, BT-474, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.30×** | +4.6 | 2e-04 | 33/48 (COLO 205, SW480, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +3.9 | 0.005 | 23/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.005 | 39/49 (J82, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.006 | 27/48 (HEC-1-A, HCT15, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4813.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HepG2/C3A 0.469×, HEC-1-A 0.537×, SW 900 0.517×, NCI-H2347 0.577×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.297×, SW 900 0.481×, Panc 03.27 0.507×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.388×, A-172 0.540×, hTERT-HPNE 0.459×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.639×** | -7.7 | 6e-12 | 43/47 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.726×** | -5.7 | 3e-06 | 34/49 (HepG2/C3A, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.725×** | -5.5 | 6e-06 | 27/44 (C-33 A, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.755×** | -4.7 | 4e-04 | 28/45 (hTERT-HPNE, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.825×** | -3.5 | 0.060 | 26/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.831×** | -3.3 | 0.082 | 21/48 (A-427, PANC-1, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.889× | -3.0 | 0.21 | 0/48 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4813. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 242 | 12 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +17.0) | — |
| [[SW480 (line)]] | alt | 240 | 10 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +14.4) | — |
| [[BT-474 (line)]] | alt | 200 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +13.9) | — |
| [[COLO 205 (line)]] | alt | 210 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +15.6) | — |
| [[PANC-1 (line)]] | alt | 305 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +18.8) | — |
| [[HepG2_C3A (line)]] | wt | 549 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.469× (z -10.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 283 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +13.5) | — |
| [[SNU-1 (line)]] | wt | 221 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +13.7) | — |
| [[HEC-1-A (line)]] | alt | 279 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.06× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.537× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 323 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +12.0) | — |
| [[C32 (line)]] | wt | 184 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.29× (z +10.6) | — |
| [[H4 (line)]] | wt | 326 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.70× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.425× (z -9.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 363 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 282 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +12.2) | — |
| [[LoVo (line)]] | wt | 265 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.497× (z -9.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 179 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.7) | — |
| [[NCI-H1573 (line)]] | alt | 259 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +13.7) | — |
| [[NCI-H23 (line)]] | alt | 381 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +12.6) | — |
| [[NCI-H2347 (line)]] | alt | 221 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +20.1) | [[Dinaciclib (drug)]] 0.5 µM 0.577× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 242 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +10.4) | — |
| [[A-172 (line)]] | wt | 220 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +10.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.540× (z -9.4) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 230 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +19.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 414 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.20× (z +9.9) | — |
| [[RKO (line)]] | wt | 372 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +16.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.388× (z -11.0) ⚠ toxic |
| [[SW 900 (line)]] | alt | 307 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.481× (z -9.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 300 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.05× (z +10.1) | — |
| [[A498 (line)]] | wt | 284 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +13.0) | — |
| [[A549 (line)]] | wt | 266 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +15.4) | — |
| [[AsPC-1 (line)]] | alt | 287 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 296 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +10.7) | — |
| [[hTERT-HPNE (line)]] | wt | 359 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.400× (z -10.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 315 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +12.5) | — |
| [[Panc 03.27 (line)]] | alt | 177 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.507× (z -9.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 310 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.96× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 409 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 269 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +13.2) | — |
| [[SHP-77 (line)]] | alt | 236 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.04× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 191 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 275 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 167 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 331 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 211 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 272 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 287 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 324 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 268 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4813), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNC1H1]] | +0.59 | +0.50 / +0.66 | both halves | 1e-05 | STRING 648 |
| [[CEP170B]] | +0.59 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[ABCB8]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[ACADVL]] | +0.56 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[CLTC]] | +0.54 | +0.46 / +0.59 | both halves | 3e-05 | STRING 632 |
| [[SMG1]] | +0.53 | +0.45 / +0.56 | both halves | 3e-05 | same gene group |
| [[TINF2]] | +0.53 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[PSMD8]] | +0.52 | +0.58 / +0.47 | both halves | 2e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[RNF123]] | +0.52 | +0.46 / +0.49 | both halves | 2e-05 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[HUWE1]] | +0.52 | +0.44 / +0.61 | both halves | 3e-05 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 881 |
| [[HSPA8]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions |
| [[POLR2J3]] | +0.51 | +0.47 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCHY1]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[ILF3-DT]] | -0.56 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[SLC25A12]] | -0.54 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[SPATA5L1]] | -0.54 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[RPRD2]] | -0.52 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[GUSBP2-1]] | -0.52 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[POMZP3]] | -0.52 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[EID2B]] | -0.52 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[EBLN2]] | -0.51 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[ZNF573]] | -0.51 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[FAM120C]] | -0.50 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[ZNF428]] | -0.50 | -0.48 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 198]] — Antigen processing: Ubiquitination & Proteasome degradation; 16 genes; every member is in the + arm (projection on the module's main direction -0.550). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.2, -5.4); signed map (-9.6, 31.7). **Vector** length 103, 38.1% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.3 | +9.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.6 | +9.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.6 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +4.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.6 | +6.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +1.5 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +2.0 | +2.3 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -10.9 | -0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -9.2 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.2 | -7.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.8 | -0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.4 | -1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin protein ligase E3 component n-recognin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:19,074,510-19,210,266 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1307, KIAA0462, RBAF600, p600; previously ZUBR1 |
| Gene groups (HGNC) | Ubiquitin protein ligase E3 component n-recognins; Armadillo like helical domain containing; UBR4 complex; Degenerate RING E3 ubiquitin ligases |
| Reactome | 9 pathways, smallest: Dengue virus activates/modulates innate and adaptive immune responses; Dengue Virus-Host Interactions; Antigen processing: Ubiquitination & Proteasome degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T4S7](https://www.uniprot.org/uniprotkb/Q5T4S7) (E3 ubiquitin-protein ligase UBR4):

> E3 ubiquitin-protein ligase involved in different protein quality control pathways in the cytoplasm. Component of the N-end rule pathway: ubiquitinates proteins bearing specific N-terminal residues that are destabilizing according to the N-end rule, leading to their degradation. Recognizes both type-1 and type-2 N-degrons, containing positively charged amino acids (Arg, Lys and His) and bulky and hydrophobic amino acids, respectively. Does not ubiquitinate proteins that are acetylated at the …

**Summary**, from NCBI Gene [23352](https://www.ncbi.nlm.nih.gov/gene/23352):

> The protein encoded by this gene is an E3 ubiquitin-protein ligase that interacts with the retinoblastoma-associated protein in the nucleus and with calcium-bound calmodulin in the cytoplasm. The encoded protein appears to be a cytoskeletal component in the cytoplasm and part of the chromatin scaffold in the nucleus. In addition, this protein is a target of the human papillomavirus type 16 E7 oncoprotein. [provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:30313](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30313) · Entrez [23352](https://www.ncbi.nlm.nih.gov/gene/23352) · UniProt [Q5T4S7](https://www.uniprot.org/uniprotkb/Q5T4S7) · Ensembl [ENSG00000127481](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127481)

## Data

Gene col 4813: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4813); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4813, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4813]; `tensor/DDL_lfc|DDL_z.npy` [4813]; `embed/gene_vectors.npy` [4813]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4813 or target_col == 4813). Every well: [[UBR4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBR4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
