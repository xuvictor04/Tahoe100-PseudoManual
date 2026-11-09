---
symbol: "GOLGA2"
type: "gene"
col: 9418
ensembl_id: "ENSG00000167110"
name: "golgin A2"
location: "9q34.11"
module: 41
arm: "+"
pooled_cpm: 162.26
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 29
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# GOLGA2

*golgin A2* — 9q34.11

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (SK-MEL-2 2.70×, NCI-H1573 2.11×, LOX-IMVI 1.72×, HepG2/C3A 2.02×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 2.81×, NCI-H1573 2.16×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 2.87×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (17 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.603× (z -8.6, q 4e-15, down in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.729× (z -7.6, q 8e-12, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMF1]] (+0.83, fdr 7e-06), [[ACBD3]] (+0.79, fdr 7e-06), [[OSBP]] (+0.78, fdr 7e-06); moves opposite to [[VMA21]] (-0.67, fdr 7e-06), [[THAP12]] (-0.63, fdr 7e-06), [[PRRC2B]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9418.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (SK-MEL-2 2.70×, NCI-H1573 2.11×, LOX-IMVI 1.72×, HepG2/C3A 2.02×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 2.81×, NCI-H1573 2.16×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 2.87×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM |  | 1.23× | +3.7 | 0.12 | 28/49 (A-427, NCI-H23, …) | all doses, flat |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.67 | 6/49 (CFPAC-1, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 18 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9418.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.603×** | -8.6 | 4e-15 | 38/48 (H4, A498, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.717×** | -7.8 | 2e-12 | 32/49 (A-172, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.729×** | -7.6 | 8e-12 | 41/48 (A-172, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.658×** | -6.8 | 1e-09 | 33/45 (H4, NCI-H1792, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.756×** | -6.6 | 5e-09 | 41/48 (A498, A-172, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.506×** | -6.3 | 3e-08 | 33/48 (Panc 03.27, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.702×** | -6.3 | 3e-08 | 34/48 (NCI-H2347, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.510×** | -6.2 | 3e-08 | 40/49 (A-427, SW1417, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.704×** | -6.2 | 4e-08 | 32/48 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.715×** | -5.9 | 2e-07 | 35/48 (A498, A-172, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.714×** | -5.7 | 6e-07 | 35/50 (HS-578T, hTERT-HPNE, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.715×** | -5.7 | 6e-07 | 31/47 (HOP62, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.736×** | -5.4 | 3e-06 | 29/49 (COLO 205, H4, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.743×** | -5.3 | 6e-06 | 26/48 (A498, A-172, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.747×** | -5.2 | 9e-06 | 32/48 (A498, HOP62, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.749×** | -5.1 | 1e-05 | 30/48 (A-172, H4, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.801×** | -5.1 | 1e-05 | 28/48 (SNU-423, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.758×** | -4.9 | 3e-05 | 29/48 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.775×** | -4.3 | 4e-04 | 29/48 (LoVo, COLO 205, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.777×** | -4.2 | 6e-04 | 30/47 (Panc 03.27, SW48, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.791×** | -4.0 | 0.002 | 27/48 (SW 900, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.807×** | -3.8 | 0.003 | 29/49 (A498, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adenine (drug)]] 5 µM |  | 0.874× | -3.2 | 0.026 | 13/48 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.839× | -3.1 | 0.036 | 20/48 (LS 180, RKO, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.843× | -3.0 | 0.044 | 20/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9418. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 245 | 0 | 11 (10 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -14.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.380× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 222 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.400× (z -10.0) |
| [[A-172 (line)]] | wt | 365 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -18.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.559× (z -13.2) |
| [[HS-578T (line)]] | alt | 219 | 0 | 8 (6 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.552× (z -11.8) |
| [[A498 (line)]] | wt | 303 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -16.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.595× (z -11.3) |
| [[HOP62 (line)]] | alt | 180 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.459× (z -10.7) ⚠ cell-cycle shift, explains ~70% of this change |
| [[NCI-H2347 (line)]] | alt | 181 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.463× (z -10.4) |
| [[SW 900 (line)]] | alt | 150 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.361× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 134 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -9.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[CFPAC-1 (line)]] | alt | 113 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.438× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.451× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 128 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.439× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[Panc 03.27 (line)]] | alt | 156 | 0 | 3 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.130× (z -14.2) |
| [[A-427 (line)]] | wt | 69.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.81× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 291 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.345× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 153 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.366× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H460 (line)]] | wt | 122 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -10.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.407× (z -10.1) |
| [[COLO 205 (line)]] | alt | 262 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[HepG2_C3A (line)]] | wt | 99.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 263 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.460× (z -8.9) ⚠ cell-cycle shift, explains ~70% of this change |
| [[LOX-IMVI (line)]] | wt | 109 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 166 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[NCI-H23 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[RPMI-7951 (line)]] | alt | 173 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.442× (z -8.9) ⚠ cell-cycle shift, explains ~70% of this change |
| [[SK-MEL-2 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 198 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[SNU-423 (line)]] | alt | 153 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.526× (z -10.1) |
| [[A549 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 109 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 156 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 155 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 148 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 223 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 285 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9418), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMF1]] | +0.83 | +0.80 / +0.85 | both halves | 7e-06 | same gene group |
| [[ACBD3]] | +0.79 | +0.77 / +0.79 | both halves | 7e-06 | STRING 434 |
| [[OSBP]] | +0.78 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[SRP54]] | +0.76 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[UFL1]] | +0.76 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[FAM114A1]] | +0.76 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[SPTY2D1]] | +0.75 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[TULP3]] | +0.74 | +0.69 / +0.79 | both halves | 7e-06 |  |
| [[POFUT2]] | +0.74 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[TBC1D23]] | +0.74 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.74 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[COPE]] | +0.73 | +0.71 / +0.66 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 418 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.67 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[THAP12]] | -0.63 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[PRRC2B]] | -0.61 | -0.59 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GOLGA2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RCN3]] | B | RCN3 activity lowers GOLGA2's level | lines that do not express RCN3 (11) vs lines expressing it (39) | 1.53× higher at baseline in the lines without RCN3 | 0.050 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.877). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.0, -37.3); signed map (-51.0, 15.0). **Vector** length 148, 55.4% of its response variance represented; |z| ≥ 3 in 1,208 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Intra-Golgi and retrograde Golgi-to-ER traffic* (reactome, mean cos +0.63 to 12); *Intra-Golgi traffic* (reactome, mean cos +0.55 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.2 | -0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +4.3 | -5.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +4.0 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +0.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +3.5 | -5.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.8 | +2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.8 | +2.6 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +2.7 | +2.4 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -6.2 | -4.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.1 | -6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.8 | -6.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.7 | -4.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.4 | -6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.4 | -7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -6.6 |

## What is on record

|  |  |
|---|---|
| Name | golgin A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,255,829-128,276,026 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GM130, golgin-95 |
| Gene groups (HGNC) | Golgins |
| Reactome | 16 pathways, smallest: Golgi Cisternae Pericentriolar Stack Reorganization; Deregulated CDK5 triggers multiple neurodegenerative pathways in Alzheimer's disease models; Neurodegenerative Diseases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08379](https://www.uniprot.org/uniprotkb/Q08379) (Golgin subfamily A member 2):

> Peripheral membrane component of the cis-Golgi stack that acts as a membrane skeleton that maintains the structure of the Golgi apparatus, and as a vesicle thether that facilitates vesicle fusion to the Golgi membrane (Probable). Required for normal protein transport from the endoplasmic reticulum to the Golgi apparatus and the cell membrane (By similarity). Together with p115/USO1 and STX5, involved in vesicle tethering and fusion at the cis-Golgi membrane to maintain the stacked and …

**Summary**, from NCBI Gene [2801](https://www.ncbi.nlm.nih.gov/gene/2801):

> The Golgi apparatus, which participates in glycosylation and transport of proteins and lipids in the secretory pathway, consists of a series of stacked cisternae (flattened membrane sacs). Interactions between the Golgi and microtubules are thought to be important for the reorganization of the Golgi after it fragments during mitosis. This gene encodes one of the golgins, a family of proteins localized to the Golgi. This encoded protein has been postulated to play roles in the stacking of Golgi …

**Accessions** — [HGNC:4425](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4425) · Entrez [2801](https://www.ncbi.nlm.nih.gov/gene/2801) · UniProt [Q08379](https://www.uniprot.org/uniprotkb/Q08379) · Ensembl [ENSG00000167110](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167110)

## Data

Gene col 9418: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9418); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9418, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9418]; `tensor/DDL_lfc|DDL_z.npy` [9418]; `embed/gene_vectors.npy` [9418]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9418 or target_col == 9418). Every well: [[GOLGA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLGA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
