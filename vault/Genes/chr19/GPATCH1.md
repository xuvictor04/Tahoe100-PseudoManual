---
symbol: "GPATCH1"
type: "gene"
col: 1158
ensembl_id: "ENSG00000076650"
name: "G-patch domain containing 1"
location: "19q13.11"
module: 12
arm: "+"
pooled_cpm: 26.49
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# GPATCH1

*G-patch domain containing 1* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.66× (z +17.6, q 0e+00, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.548× (z -14.7, q 0e+00, down in 30 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.713× (z -8.2, q 4e-14, down in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (KATO III 0.0501×, A498 0.270×, A549 0.252×, HepG2/C3A 0.0939×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 0.144×, A498 0.214×, HOP62 0.316×, NCI-H1792 0.276×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (J82 0.176×, HEC-1-A 0.285×, A498 0.380×; ⚠ toxic; transcription drop); [[Menadione (drug)]] 0.05 µM in 1 line (BT-474 0.137×); [[XRK3F2 (drug)]] 0.5 µM in 1 line (Hs 766T 0.110×); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.492×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC4A1AP]] (+0.68, fdr 7e-06), [[KBTBD4]] (+0.65, fdr 7e-06), [[NKAP]] (+0.63, fdr 7e-06); moves opposite to [[MAT2A]] (-0.63, fdr 7e-06), [[VMA21]] (-0.60, fdr 1e-05), [[EMB]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EMB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1158.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +17.6 | 0e+00 | 35/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +13.9 | 2e-41 | 35/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +9.4 | 8e-19 | 35/48 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +8.9 | 1e-16 | 29/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +8.8 | 2e-16 | 26/48 (PANC-1, HOP62, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +7.6 | 2e-12 | 22/48 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +7.6 | 2e-12 | 24/47 (PANC-1, KATO III, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +7.6 | 3e-12 | 24/48 (A-427, LoVo, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +7.3 | 3e-11 | 21/46 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.33×** | +7.1 | 8e-11 | 25/48 (BT-474, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.20×** | +6.4 | 6e-09 | 18/47 (PANC-1, SW1417, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.28×** | +5.8 | 4e-07 | 19/48 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.55×** | +5.6 | 1e-06 | 19/48 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.24×** | +5.3 | 4e-06 | 18/47 (LoVo, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.5 | 3e-04 | 11/47 (BT-474, CFPAC-1, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.41×** | +4.4 | 4e-04 | 9/45 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.38×** | +4.2 | 1e-03 | 11/45 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trimetrexate (drug)]] 5 µM |  | 1.11× | +3.6 | 0.010 | 6/48 (SW480, A498, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.13× | +3.1 | 0.057 | 10/48 (HS-578T, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1158.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (KATO III 0.0501×, A498 0.270×, A549 0.252×, HepG2/C3A 0.0939×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 0.144×, A498 0.214×, HOP62 0.316×, NCI-H1792 0.276×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (J82 0.176×, HEC-1-A 0.285×, A498 0.380×; ⚠ toxic; transcription drop); [[Menadione (drug)]] 0.05 µM in 1 line (BT-474 0.137×); [[XRK3F2 (drug)]] 0.5 µM in 1 line (Hs 766T 0.110×); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.492×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.548×** | -14.7 | 0e+00 | 30/42 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.654×** | -10.0 | 6e-21 | 22/34 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.713×** | -8.2 | 4e-14 | 27/47 (SW480, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.740×** | -6.8 | 2e-09 | 21/36 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.788×** | -5.8 | 9e-07 | 21/48 (MIA PaCa-2, HS-578T, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.785×** | -5.7 | 1e-06 | 24/46 (NCI-H1792, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.796×** | -5.6 | 2e-06 | 19/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.862× | -5.1 | 3e-05 | 17/48 (A498, C32, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.733×** | -3.9 | 0.005 | 14/30 (A-172, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.845× | -3.9 | 0.005 | 17/43 (HT-29, A-172, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.851× | -3.9 | 0.005 | 14/46 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.863× | -3.6 | 0.017 | 11/47 (SW1417, NCI-H460, …) | two highest doses |  |
| [[Auranofin (drug)]] 0.5 µM |  | 0.878× | -3.2 | 0.071 | 4/48 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.878× | -3.0 | 0.10 | 7/47 (H4, MIA PaCa-2, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1158. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 39.0 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.504× (z -9.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 25.0 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.144× (z -18.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 34.6 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.492× (z -8.6) |
| [[A498 (line)]] | wt | 45.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -17.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 49.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -13.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 42.8 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -10.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 27.5 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.135× (z -10.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 34.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 22.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +11.5) | [[Docetaxel (drug)]] 0.05 µM 0.242× (z -11.3) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.105× (z -9.2) ⚠ toxic |
| [[A-427 (line)]] | wt | 18.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -9.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.118× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 20.5 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.137× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -12.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0939× (z -12.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -10.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 20.2 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.110× (z -9.8) |
| [[HS-578T (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -9.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -13.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 31.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0501× (z -26.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 17.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 37.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 22.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.4) | — |
| [[NCI-H460 (line)]] | wt | 15.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1158), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC4A1AP]] | +0.68 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[KBTBD4]] | +0.65 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[NKAP]] | +0.63 | +0.66 / +0.61 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 517 |
| [[AKAP9]] | +0.62 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[ASB8]] | +0.62 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.62 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[LRSAM1]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[CEP350]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[PHC3]] | +0.61 | +0.68 / +0.46 | both halves | 2e-05 |  |
| [[HMGXB4]] | +0.61 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[TTF1]] | +0.60 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[TOGARAM1]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAT2A]] | -0.63 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[VMA21]] | -0.60 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[EMB]] | -0.58 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[DHX15]] | -0.57 | -0.63 / -0.57 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[MARCKSL1]] | -0.53 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[HNRNPA3]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[GNB1]] | -0.52 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[ACTB]] | -0.52 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[ARHGAP4]] | -0.52 | -0.53 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EMB]] | B | EMB activity lowers GPATCH1's level | lines that do not express EMB (21) vs lines expressing it (29) | 1.29× higher at baseline in the lines without EMB | 0.071 | ⚠ within organs, on part of the lines; also absent: CACNA2D1, SUSD5, PKIA |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.571). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-45.9, -3.4); signed map (-7.3, -5.2). **Vector** length 88.8, 17.9% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.6 | +9.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +8.8 |
|  | [[NG25 (drug)]] 5 µM |  | +3.3 | +4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +17.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +13.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +1.8 | +2.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.2 | -6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.9 | -14.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.8 | -5.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.0 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | G-patch domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:33,080,899-33,130,542 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ECGP, FLJ10206, FLJ38686; previously GPATC1 |
| Gene groups (HGNC) | G-patch domain containing; Spliceosomal Bact complex; Spliceosomal C complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

UniProt [Q9BRR8](https://www.uniprot.org/uniprotkb/Q9BRR8) carries no function annotation.

**Summary**, from NCBI Gene [55094](https://www.ncbi.nlm.nih.gov/gene/55094):

> Predicted to enable RNA binding activity. Predicted to be involved in mRNA splicing, via spliceosome. Part of catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24658](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24658) · Entrez [55094](https://www.ncbi.nlm.nih.gov/gene/55094) · UniProt [Q9BRR8](https://www.uniprot.org/uniprotkb/Q9BRR8) · Ensembl [ENSG00000076650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076650)

## Data

Gene col 1158: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1158); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1158, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1158]; `tensor/DDL_lfc|DDL_z.npy` [1158]; `embed/gene_vectors.npy` [1158]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1158 or target_col == 1158). Every well: [[GPATCH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPATCH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
