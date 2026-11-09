---
symbol: "SH3GLB1"
type: "gene"
col: 1776
ensembl_id: "ENSG00000097033"
name: "SH3 domain containing GRB2 like, endophilin B1"
location: "1p22.3"
module: 5
arm: "-"
pooled_cpm: 129.04
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 19
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SH3GLB1

*SH3 domain containing GRB2 like, endophilin B1* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.21× (z +4.5, q 0.003, up in 24 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.18× (z +4.1, q 0.011, up in 19 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 2.28×, PANC-1 1.73×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 1.81×, A-427 2.22×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (PANC-1 1.81×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.390× (z -23.0, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAM1]] (+0.59, fdr 7e-06), [[UBE2J1]] (+0.53, fdr 1e-05), [[TMEM167B]] (+0.53, fdr 2e-05); moves opposite to [[SNRPB]] (-0.56, fdr 3e-05), [[XXYLT1]] (-0.54, fdr 1e-05), [[PRDM15]] (-0.53, fdr 3e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[BEGAIN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1776.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 2.28×, PANC-1 1.73×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 1.81×, A-427 2.22×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (PANC-1 1.81×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.21×** | +4.5 | 0.003 | 24/47 (J82, SW480, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.18× | +4.1 | 0.011 | 19/47 (SW 900, SW480, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.041 | 17/49 (A498, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 1.10× | +3.5 | 0.078 | 3/48 (SW1417, Hs 766T, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.21× | +3.3 | 0.11 | 15/48 (CHP-212, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.12 | 15/48 (SNU-423, Panc 03.27, …) | inconsistent across doses |  |
| [[Pasireotide (acetate) (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.19 | 5/49 (J82, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1776.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.390×** | -23.0 | 0e+00 | 46/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.413×** | -21.6 | 0e+00 | 47/48 (A498, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.597×** | -17.8 | 0e+00 | 43/49 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.494×** | -17.2 | 0e+00 | 44/48 (A498, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.665×** | -9.6 | 1e-19 | 36/47 (A498, A-172, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.698×** | -8.8 | 2e-16 | 34/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.804×** | -7.5 | 6e-12 | 29/48 (HOP62, Hs 766T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.805×** | -7.5 | 6e-12 | 23/48 (NCI-H1792, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -6.4 | 1e-08 | 0/50 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.771×** | -6.3 | 1e-08 | 29/48 (A498, RPMI-7951, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.770×** | -6.1 | 5e-08 | 29/48 (A498, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.780×** | -6.1 | 7e-08 | 34/48 (A498, SW 900, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.785×** | -5.7 | 6e-07 | 31/50 (SW 900, COLO 205, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.805×** | -5.3 | 5e-06 | 25/48 (COLO 205, HT-29, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.665×** | -5.2 | 8e-06 | 26/49 (HOP62, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.833×** | -4.2 | 9e-04 | 18/47 (NCI-H1573, HT-29, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.738×** | -3.9 | 0.003 | 24/49 (A-172, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.758×** | -3.5 | 0.011 | 19/48 (HOP62, A-172, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.870× | -3.4 | 0.019 | 13/48 (SW1417, LoVo, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.844× | -2.9 | 0.080 | 12/48 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1776. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 210 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.298× (z -23.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.336× (z -21.1) |
| [[HOP62 (line)]] | alt | 91.8 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.275× (z -19.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.349× (z -15.8) |
| [[A-172 (line)]] | wt | 122 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.333× (z -17.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.357× (z -16.1) |
| [[COLO 205 (line)]] | alt | 143 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -16.7) |
| [[HS-578T (line)]] | alt | 244 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.245× (z -20.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.399× (z -18.8) |
| [[CFPAC-1 (line)]] | alt | 231 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -20.6) |
| [[NCI-H1792 (line)]] | alt | 180 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -24.3) |
| [[Hs 766T (line)]] | wt | 187 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -19.3) |
| [[hTERT-HPNE (line)]] | wt | 150 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.285× (z -15.1) |
| [[RPMI-7951 (line)]] | alt | 177 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -16.6) |
| [[SNU-423 (line)]] | alt | 174 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -18.0) |
| [[SW 900 (line)]] | alt | 150 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -14.1) |
| [[A549 (line)]] | wt | 111 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.266× (z -18.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -15.8) |
| [[AsPC-1 (line)]] | alt | 180 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -20.2) |
| [[HepG2_C3A (line)]] | wt | 191 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 159 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.319× (z -15.0) |
| [[HT-29 (line)]] | alt | 134 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -14.2) |
| [[J82 (line)]] | alt | 126 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.417× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 122 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.420× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 160 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.353× (z -16.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.358× (z -16.3) |
| [[PANC-1 (line)]] | alt | 146 | 2 (2 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.81× (z +8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.481× (z -11.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.490× (z -10.7) |
| [[SW480 (line)]] | alt | 94.8 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.81× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.407× (z -14.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.428× (z -13.8) |
| [[BT-474 (line)]] | alt | 79.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.348× (z -11.3) |
| [[H4 (line)]] | wt | 96.8 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.275× (z -11.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.314× (z -10.1) |
| [[KATO III (line)]] | alt | 90.0 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 100 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.388× (z -12.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.413× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 115 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 123 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.367× (z -12.4) |
| [[SW1417 (line)]] | alt | 141 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.385× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 108 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -9.9) |
| [[LoVo (line)]] | wt | 104 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.411× (z -11.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.431× (z -10.6) |
| [[LS 180 (line)]] | wt | 101 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.391× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 68.0 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.504× (z -9.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.526× (z -8.8) |
| [[A-427 (line)]] | wt | 75.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.22× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 102 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -9.5) |
| [[HCT15 (line)]] | alt | 112 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -8.5) |
| [[RKO (line)]] | wt | 115 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.475× (z -8.9) |
| [[AN3 CA (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 72.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1776), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAM1]] | +0.59 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[UBE2J1]] | +0.53 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[TMEM167B]] | +0.53 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[OPTN]] | +0.53 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ARFGEF1]] | +0.53 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[ZYG11B]] | +0.53 | +0.63 / +0.38 | both halves | 7e-05 |  |
| [[NRBP1]] | +0.52 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[SECISBP2L]] | +0.51 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[JAK1]] | +0.51 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[EIF2B4]] | +0.51 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[FBXO7]] | +0.51 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[FYTTD1]] | +0.50 | +0.39 / +0.49 | both halves | 6e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPB]] | -0.56 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[XXYLT1]] | -0.54 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[PRDM15]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[MAD1L1]] | -0.53 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[UHRF1]] | -0.50 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ASMTL-AS1]] | -0.49 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[ZFAT]] | -0.48 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[EIPR1]] | -0.47 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[LIMD1]] | -0.47 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[B3GNTL1]] | -0.47 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[WDR4]] | -0.47 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[MBD3]] | -0.47 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BEGAIN]] | B | BEGAIN activity lowers SH3GLB1's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 1.40× higher at baseline in the lines without BEGAIN | 0.012 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises SH3GLB1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.456). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-9.3, -51.7); signed map (-19.6, -3.3). **Vector** length 111, 33.9% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.5 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.6 | +2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.4 | +1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.5 | +0.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.5 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.2 | +0.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.2 | +1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.1 | +3.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.1 | -5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.0 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -7.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.4 | -4.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain containing GRB2 like, endophilin B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:86,704,570-86,748,184 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-61, KIAA0491, Bif-1, PPP1R70 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; N-BAR domain containing; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y371](https://www.uniprot.org/uniprotkb/Q9Y371) (Endophilin-B1):

> May be required for normal outer mitochondrial membrane dynamics. Required for coatomer-mediated retrograde transport in certain cells (By similarity). May recruit other proteins to membranes with high curvature. May promote membrane fusion. Involved in activation of caspase-dependent apoptosis by promoting BAX/BAK1 activation. Isoform 1 acts pro-apoptotic in fibroblasts (By similarity). Involved in caspase-independent apoptosis during nutrition starvation and involved in the regulation of …

**Summary**, from NCBI Gene [51100](https://www.ncbi.nlm.nih.gov/gene/51100):

> This gene encodes a SRC homology 3 domain-containing protein. The encoded protein interacts with the proapoptotic member of the Bcl-2 family, Bcl-2-associated X protein (Bax) and may be involved in regulating apoptotic signaling pathways. This protein may also be involved in maintaining mitochondrial morphology. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:10833](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10833) · Entrez [51100](https://www.ncbi.nlm.nih.gov/gene/51100) · UniProt [Q9Y371](https://www.uniprot.org/uniprotkb/Q9Y371) · Ensembl [ENSG00000097033](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000097033)

## Data

Gene col 1776: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1776); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1776, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1776]; `tensor/DDL_lfc|DDL_z.npy` [1776]; `embed/gene_vectors.npy` [1776]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1776 or target_col == 1776). Every well: [[SH3GLB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3GLB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
