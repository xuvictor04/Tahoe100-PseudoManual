---
symbol: "NUDT21"
type: "gene"
col: 9404
ensembl_id: "ENSG00000167005"
name: "nudix hydrolase 21"
location: "16q13"
module: 57
arm: "+"
pooled_cpm: 79.81
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# NUDT21

*nudix hydrolase 21* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.21× (z +14.4, q 4e-44, up in 42 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.08× (z +7.5, q 5e-12, up in 45 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 8 lines (NCI-H460 3.55×, A-427 3.43×, SHP-77 3.36×, MIA PaCa-2 3.99×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (MIA PaCa-2 4.29×, SW480 2.49×, LOX-IMVI 4.05×, HT-29 3.23×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 4.03×, A-172 3.10×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SK-MEL-2 2.55×).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.667× (z -11.2, q 1e-26, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPA1]] (+0.82, fdr 7e-06), [[SKP2]] (+0.77, fdr 7e-06), [[COPS7B]] (+0.73, fdr 7e-06); moves opposite to [[LETM2]] (-0.68, fdr 1e-05), [[BOLA1]] (-0.68, fdr 1e-05), [[ZNF341-AS1]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ARL14]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 17 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9404.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 8 lines (NCI-H460 3.55×, A-427 3.43×, SHP-77 3.36×, MIA PaCa-2 3.99×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (MIA PaCa-2 4.29×, SW480 2.49×, LOX-IMVI 4.05×, HT-29 3.23×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 4.03×, A-172 3.10×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SK-MEL-2 2.55×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.21×** | +14.4 | 4e-44 | 42/45 (NCI-H460, A-427, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.25×** | +13.9 | 3e-41 | 43/49 (MIA PaCa-2, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.07×** | +12.8 | 2e-35 | 40/44 (MIA PaCa-2, SW480, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.59×** | +8.2 | 3e-14 | 38/47 (LoVo, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.50×** | +8.0 | 2e-13 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +7.5 | 5e-12 | 45/49 (KATO III, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.44×** | +7.1 | 1e-10 | 34/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.34×** | +5.7 | 6e-07 | 27/48 (HT-29, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +5.4 | 5e-06 | 23/38 (NCI-H1573, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +5.2 | 1e-05 | 33/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.26×** | +4.6 | 2e-04 | 26/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.26×** | +4.5 | 3e-04 | 26/48 (NCI-H1792, NCI-H460, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.24×** | +4.2 | 0.001 | 20/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.23×** | +4.0 | 0.003 | 19/48 (NCI-H1792, RKO, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.22×** | +3.8 | 0.005 | 21/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9404.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.667×** | -11.2 | 1e-26 | 41/48 (AsPC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.716×** | -9.3 | 6e-18 | 34/49 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.676×** | -6.9 | 9e-10 | 36/48 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.819×** | -3.9 | 0.013 | 22/48 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.872× | -3.8 | 0.016 | 16/48 (SW480, KATO III, …) | rises with dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.823×** | -3.4 | 0.056 | 18/49 (NCI-H1573, CFPAC-1, …) | top dose only | plate-row cell shift |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.844× | -3.3 | 0.057 | 14/48 (RKO, hTERT-HPNE, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.844× | -3.3 | 0.057 | 14/48 (CFPAC-1, LS 180, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.845× | -3.3 | 0.057 | 21/48 (SW480, HOP62, …) | rises with dose |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | 0.851× | -3.2 | 0.087 | 10/49 (NCI-H1573, NCI-H2122, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9404. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 57.9 | 5 (5 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.60× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.582× (z -9.5) |
| [[SW480 (line)]] | alt | 112 | 5 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.49× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -12.7) |
| [[HOP62 (line)]] | alt | 90.8 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 71.5 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.55× (z +15.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -11.4) |
| [[A-172 (line)]] | wt | 85.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HT-29 (line)]] | alt | 70.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LoVo (line)]] | wt | 54.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.38× (z +11.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 67.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 95.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 47.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 4.69× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -12.0) |
| [[A-427 (line)]] | wt | 76.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.43× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -11.7) |
| [[A549 (line)]] | wt | 70.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.66× (z +11.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 61.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -16.4) |
| [[C-33 A (line)]] | alt | 98.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[Hs 766T (line)]] | wt | 66.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 67.2 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.56× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[RKO (line)]] | wt | 87.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.82× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 130 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.468× (z -8.6) |
| [[COLO 205 (line)]] | alt | 49.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HCT15 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HEC-1-A (line)]] | alt | 95.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.11× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[J82 (line)]] | alt | 106 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -15.6) |
| [[KATO III (line)]] | alt | 86.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LS 180 (line)]] | wt | 60.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2030 (line)]] | alt | 143 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 88.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 60.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -12.2) |
| [[SHP-77 (line)]] | alt | 96.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.36× (z +13.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 63.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.55× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 55.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW48 (line)]] | wt | 67.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[AN3 CA (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 139 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 66.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 81.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 88.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 87.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9404), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPA1]] | +0.82 | +0.83 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[SKP2]] | +0.77 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[COPS7B]] | +0.73 | +0.76 / +0.79 | both halves | 7e-06 |  |
| [[SDHAP4]] | +0.71 | +0.81 / +0.59 | both halves | 7e-06 |  |
| [[TM9SF2]] | +0.69 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[SHQ1]] | +0.69 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[ANAPC5]] | +0.68 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[ELP1]] | +0.68 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[SUMO1]] | +0.67 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[UBAC1]] | +0.67 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[SNX1]] | +0.67 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[HDAC1]] | +0.66 | +0.63 / +0.51 | both halves | 1e-05 | STRING 473 |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LETM2]] | -0.68 | -0.69 / -0.57 | both halves | 1e-05 |  |
| [[BOLA1]] | -0.68 | -0.68 / -0.56 | both halves | 1e-05 |  |
| [[ZNF341-AS1]] | -0.67 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[RNF103-CHMP3]] | -0.67 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[C14orf119]] | -0.67 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[PBDC1]] | -0.66 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[SPHK1]] | -0.65 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[OFD1]] | -0.65 | -0.67 / -0.59 | both halves | 7e-06 |  |
| [[EIF4EBP3]] | -0.65 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[LINC02307]] | -0.65 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[TRIM47]] | -0.64 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[LRIF1]] | -0.63 | -0.57 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARL14]] | B | ARL14 activity lowers NUDT21's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 1.27× higher at baseline in the lines without ARL14 | 0.011 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |
| [[BMP2]] | B | BMP2 activity lowers NUDT21's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 1.14× higher at baseline in the lines without BMP2 | 0.062 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.807). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-7.6, -13.4); signed map (-37.9, -13.3). **Vector** length 116, 35.7% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +5.3 | +4.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +4.9 | +4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +4.5 | +4.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +0.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.7 | +0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.9 | -11.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -10.1 | -6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.7 | -3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.9 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | nudix hydrolase 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:56,429,133-56,452,199 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CFIM25; previously CPSF5 |
| Gene groups (HGNC) | Nudix hydrolase family; Cleavage factor Im complex subunits |
| Hallmark sets | DNA_REPAIR, E2F_TARGETS |
| Reactome | 10 pathways, smallest: Processing of Intronless Pre-mRNAs; Processing of Capped Intronless Pre-mRNA; RNA Polymerase II Transcription Termination |
| Matched by | ensembl_id |

**Function**, from UniProt [O43809](https://www.uniprot.org/uniprotkb/O43809) (Cleavage and polyadenylation specificity factor subunit 5):

> Component of the cleavage factor Im (CFIm) complex that functions as an activator of the pre-mRNA 3'-end cleavage and polyadenylation processing required for the maturation of pre-mRNA into functional mRNAs. CFIm contributes to the recruitment of multiprotein complexes on specific sequences on the pre-mRNA 3'-end, so called cleavage and polyadenylation signals (pA signals). Most pre-mRNAs contain multiple pA signals, resulting in alternative cleavage and polyadenylation (APA) producing mRNAs …

**Summary**, from NCBI Gene [11051](https://www.ncbi.nlm.nih.gov/gene/11051):

> The protein encoded by this gene is one subunit of a cleavage factor required for 3' RNA cleavage and polyadenylation processing. The interaction of the protein with the RNA is one of the earliest steps in the assembly of the 3' end processing complex and facilitates the recruitment of other processing factors. This gene encodes the 25kD subunit of the protein complex, which is composed of four polypeptides. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13870](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13870) · Entrez [11051](https://www.ncbi.nlm.nih.gov/gene/11051) · UniProt [O43809](https://www.uniprot.org/uniprotkb/O43809) · Ensembl [ENSG00000167005](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167005)

## Data

Gene col 9404: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9404); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9404, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9404]; `tensor/DDL_lfc|DDL_z.npy` [9404]; `embed/gene_vectors.npy` [9404]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9404 or target_col == 9404). Every well: [[NUDT21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
