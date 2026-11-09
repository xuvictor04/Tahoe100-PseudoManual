---
symbol: "MYH9"
type: "gene"
col: 1933
ensembl_id: "ENSG00000100345"
name: "myosin heavy chain 9"
location: "22q12.3"
module: 111
arm: "+"
pooled_cpm: 589.05
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# MYH9

*myosin heavy chain 9* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.37× (z +13.2, q 3e-37, up in 45 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Peretinoin (drug)]] 0.05 µM: 1.37× (z +4.4, q 0.001, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.633× (z -9.9, q 2e-20, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR1]] (+0.75, fdr 7e-06), [[CSRP1]] (+0.70, fdr 7e-06), [[ACTR3]] (+0.69, fdr 7e-06); moves opposite to [[TMEM101]] (-0.64, fdr 3e-05), [[COA6]] (-0.63, fdr 1e-05), [[MRPL32]] (-0.62, fdr 3e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TPM1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1933.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +13.2 | 3e-37 | 45/48 (SNU-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +12.4 | 1e-32 | 40/43 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +10.8 | 4e-25 | 43/44 (SNU-423, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.37×** | +4.4 | 0.001 | 39/47 (NCI-H23, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.005 | 23/47 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.29×** | +3.9 | 0.008 | 33/47 (C32, NCI-H1573, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.013 | 24/48 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 1.18× | +3.6 | 0.024 | 23/47 (A498, A549, …) | top dose only | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +3.5 | 0.029 | 20/48 (C32, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.23× | +3.0 | 0.14 | 25/47 (NCI-H1792, A498, …) | all doses, flat | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1933.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -9.9 | 2e-20 | 36/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.591×** | -8.1 | 2e-13 | 43/47 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.580×** | -8.1 | 2e-13 | 36/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Anethole trithione (drug)]] 5 µM |  | **0.723×** | -7.0 | 3e-10 | 46/47 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **0.759×** | -6.0 | 3e-07 | 38/47 (A549, PANC-1, …) | rises with dose | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.706×** | -5.2 | 2e-05 | 46/48 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.745×** | -4.4 | 1e-03 | 43/48 (Panc 03.27, NCI-H2030, …) | inconsistent across doses |  |
| [[Clonidine (hydrochloride) (drug)]] 5 µM |  | 0.837× | -3.9 | 0.008 | 19/47 (MIA PaCa-2, RKO, …) | top dose only | position effect removed |
| [[Terfenadine (drug)]] 5 µM |  | 0.841× | -3.7 | 0.011 | 21/47 (NCI-H661, RPMI-7951, …) | rises with dose | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | 0.844× | -3.7 | 0.014 | 20/47 (H4, NCI-H460, …) | top dose only | position effect removed |
| [[Temsirolimus (drug)]] 5 µM |  | 0.864× | -3.2 | 0.078 | 15/48 (SW1417, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.812×** | -3.1 | 0.098 | 24/46 (SK-MEL-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.821× | -3.0 | 0.10 | 26/46 (NCI-H661, CHP-212, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.815× | -3.0 | 0.10 | 24/47 (SW480, PANC-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1933. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 512 | 7 (7 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +16.2) ⚠ cell-cycle shift, explains ~79% of this change | [[Amsacrine (drug)]] 5 µM 0.571× (z -9.3) |
| [[A498 (line)]] | wt | 929 | 7 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +18.2) ⚠ cell-cycle shift, explains ~79% of this change | — |
| [[C32 (line)]] | wt | 340 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.63× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 417 | 6 (6 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +17.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -9.4) |
| [[HOP62 (line)]] | alt | 754 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +9.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -13.9) |
| [[PANC-1 (line)]] | alt | 658 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +12.9) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.326× (z -13.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -13.0) |
| [[AN3 CA (line)]] | alt | 203 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +12.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 736 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.0) ⚠ cell-cycle shift, explains ~79% of this change | — |
| [[LOX-IMVI (line)]] | wt | 546 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -12.0) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.441× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 820 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +10.6) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.490× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 777 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +10.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -14.8) |
| [[SW480 (line)]] | alt | 558 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +9.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -17.8) |
| [[H4 (line)]] | wt | 474 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.4) ⚠ cell-cycle shift, explains ~79% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.324× (z -11.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -9.6) |
| [[Hs 766T (line)]] | wt | 750 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +10.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -9.4) |
| [[HS-578T (line)]] | alt | 1,201 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +13.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 852 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +10.1) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 563 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +11.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -10.0) |
| [[LoVo (line)]] | wt | 445 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +10.0) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.426× (z -9.9) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 381 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 474 | 3 (3 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.76× (z +12.4) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[NCI-H2030 (line)]] | alt | 378 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +13.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 466 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +13.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 344 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.06× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 542 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -11.3) |
| [[SNU-1 (line)]] | wt | 155 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.26× (z +19.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 1,502 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +15.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 519 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.8) ⚠ cell-cycle shift, explains ~79% of this change | — |
| [[A-427 (line)]] | wt | 176 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +16.3) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 464 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 788 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -14.6) |
| [[HEC-1-A (line)]] | alt | 982 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -17.0) |
| [[NCI-H23 (line)]] | alt | 391 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +11.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 242 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +12.1) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 636 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +8.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -12.9) |
| [[SW1417 (line)]] | alt | 336 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.53× (z +10.0) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 481 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -15.0) |
| [[HT-29 (line)]] | alt | 452 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -13.0) |
| [[hTERT-HPNE (line)]] | wt | 1,216 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.360× (z -9.0) ⚠ toxic |
| [[LS 180 (line)]] | wt | 504 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 329 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -11.0) |
| [[SW 1088 (line)]] | alt | 1,231 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -9.3) |
| [[SW48 (line)]] | wt | 403 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +9.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 533 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 569 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 125 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 593 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 451 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 467 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 337 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 462 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1933), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR1]] | +0.75 | +0.72 / +0.77 | both halves | 7e-06 | same gene group; STRING 770 |
| [[CSRP1]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[ACTR3]] | +0.69 | +0.59 / +0.69 | both halves | 7e-06 | pathway: EPH-Ephrin signaling; STRING 812 |
| [[CORO1C]] | +0.69 | +0.56 / +0.72 | both halves | 1e-05 | STRING 404 |
| [[FLNA]] | +0.68 | +0.67 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 861 |
| [[TPM4]] | +0.68 | +0.59 / +0.64 | both halves | 7e-06 | pathway: Signaling by ALK fusions and activated point mutants; STRING 882 |
| [[SPTBN1]] | +0.68 | +0.55 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 671 |
| [[YWHAZ]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 | pathway: RHO GTPase Effectors; STRING 415 |
| [[DBN1]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 | STRING 405 |
| [[MYLK]] | +0.64 | +0.48 / +0.60 | both halves | 2e-05 | pathway: HALLMARK_MYOGENESIS; STRING 770 |
| [[MSN]] | +0.62 | +0.51 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_APICAL_JUNCTION; STRING 941 |
| [[HUWE1]] | +0.62 | +0.53 / +0.65 | both halves | 1e-05 | same gene group; STRING 481 |

## Genes that move opposite

*41 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM101]] | -0.64 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[COA6]] | -0.63 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[MRPL32]] | -0.62 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[RANGRF]] | -0.61 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[MRPS36]] ⚠ | -0.61 | -0.57 / -0.59 | both halves | 9e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[C1orf122]] | -0.59 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[TMEM258]] | -0.57 | -0.45 / -0.61 | both halves | 3e-05 | same gene group |
| [[SNHG9]] | -0.56 | -0.43 / -0.59 | both halves | 4e-05 |  |
| [[YBEY]] | -0.56 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[WDR83OS]] ⚠ | -0.56 | -0.44 / -0.60 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NCBP2AS2]] | -0.56 | -0.37 / -0.62 | both halves | 7e-05 |  |
| [[CLPP]] | -0.56 | -0.29 / -0.61 | both halves | 2e-04 |  |
| [[SMIM27]] | -0.55 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[DNLZ]] | -0.55 | -0.38 / -0.56 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPM1]] | C | TPM1 activity raises MYH9's level | lines that do not express TPM1 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without TPM1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, SSUH2, XIRP2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.802). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.2, 25.4); signed map (-7.9, 35.0). **Vector** length 159, 55.4% of its response variance represented; |z| ≥ 3 in 1,170 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cell-Cell communication* (reactome, mean cos +0.51 to 13); *Platelet activation, signaling and aggregation* (reactome, mean cos +0.56 to 11); *Cell-extracellular matrix interactions* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +10.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.7 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +13.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +3.0 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +4.1 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.5 | +2.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +3.3 | +2.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -12.9 | -8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.3 | -9.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -8.2 | -8.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.7 | -1.8 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -5.2 | -5.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.8 | -6.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | -4.3 | -3.7 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | -3.9 | -3.0 |
|  | [[Adagrasib (drug)]] 5 µM |  | -3.8 | -1.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | myosin heavy chain 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:36,281,280-36,388,010 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NMMHCA, NMHC-II-A, MHA, FTNS, EPSTS; previously DFNA17 |
| Gene groups (HGNC) | Myosin heavy chains, class II; MicroRNA protein coding host genes |
| Hallmark sets | HEDGEHOG_SIGNALING, MYOGENESIS, APICAL_JUNCTION, HYPOXIA, MITOTIC_SPINDLE |
| Reactome | 38 pathways, smallest: CD163 mediating an anti-inflammatory response; RHO GTPases Activate ROCKs; RHO GTPases activate CIT |
| Matched by | ensembl_id |

**Function**, from UniProt [P35579](https://www.uniprot.org/uniprotkb/P35579) (Myosin-9):

> Cellular myosin that appears to play a role in cytokinesis, cell shape, and specialized functions such as secretion and capping. Required for cortical actin clearance prior to oocyte exocytosis (By similarity). Plays a role in regulated exocytosis, probably by providing the contractile force that drives compression and integration of the secretory granule membrane with the cell membrane post-fusion (By similarity). Promotes cell motility in conjunction with S100A4. During cell spreading, plays …

**Summary**, from NCBI Gene [4627](https://www.ncbi.nlm.nih.gov/gene/4627):

> This gene encodes a conventional non-muscle myosin; this protein should not be confused with the unconventional myosin-9a or 9b (MYO9A or MYO9B). The encoded protein is a myosin IIA heavy chain that contains an IQ domain and a myosin head-like domain which is involved in several important functions, including cytokinesis, cell motility and maintenance of cell shape. Defects in this gene have been associated with non-syndromic sensorineural deafness autosomal dominant type 17, Epstein syndrome, …

**Accessions** — [HGNC:7579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7579) · Entrez [4627](https://www.ncbi.nlm.nih.gov/gene/4627) · UniProt [P35579](https://www.uniprot.org/uniprotkb/P35579) · Ensembl [ENSG00000100345](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100345)

## Data

Gene col 1933: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1933); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1933, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1933]; `tensor/DDL_lfc|DDL_z.npy` [1933]; `embed/gene_vectors.npy` [1933]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1933 or target_col == 1933). Every well: [[MYH9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYH9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
