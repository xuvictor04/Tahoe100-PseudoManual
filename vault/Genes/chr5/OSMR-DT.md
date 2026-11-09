---
symbol: "OSMR-DT"
type: "gene"
col: 14631
ensembl_id: "ENSG00000249740"
name: "OSMR divergent transcript"
location: "5p13.1"
module: 101
arm: "+"
pooled_cpm: 108.1
n_lines_expressing: 35
n_dd_up: 2
n_dd_down: 50
n_dd_up_clean: 2
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 8
direction_downstream: 4
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# OSMR-DT

*OSMR divergent transcript* — 5p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.46× (z +7.3, q 2e-10, up in 26 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (SW 900 2.72×, HOP62 2.26×, MIA PaCa-2 2.63×, AsPC-1 2.32×, …); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HOP62 2.97×, SW 900 3.50×, HS-578T 3.71×).
> Pooled over the cell lines (median), lowered significantly by 50 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.227× (z -28.5, q 0e+00, down in 32 of 32 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OSMR]] (+0.72, fdr 7e-06, ⚠ same locus), [[LINC00862]] (+0.65, fdr 1e-05), [[LUCAT1]] (+0.63, fdr 9e-06), [[ITGA2-AS1]] (+0.58, fdr 1e-05); moves opposite to [[CCDC6]] (-0.55, fdr 1e-05), [[SORL1]] (-0.52, fdr 5e-05), [[PHKB]] (-0.52, fdr 1e-04).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[C11orf91]] → it (grade B ⚠); 4 go from it, the strongest it → [[RNF217]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14631.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (SW 900 2.72×, HOP62 2.26×, MIA PaCa-2 2.63×, AsPC-1 2.32×, …); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HOP62 2.97×, SW 900 3.50×, HS-578T 3.71×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.3 | 2e-10 | 26/34 (SW 900, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +5.8 | 2e-06 | 21/33 (HOP62, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 50 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14631.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.227×** | -28.5 | 0e+00 | 32/32 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.207×** | -20.6 | 0e+00 | 33/33 (A549, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.275×** | -17.5 | 0e+00 | 33/33 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.359×** | -13.9 | 8e-42 | 31/33 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.367×** | -13.6 | 5e-40 | 29/34 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.371×** | -12.9 | 2e-36 | 31/32 (SNU-423, C32, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.376×** | -12.8 | 2e-35 | 26/29 (LOX-IMVI, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.368×** | -11.4 | 2e-28 | 33/33 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.502×** | -9.3 | 7e-19 | 27/32 (A549, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[NG25 (drug)]] 5 µM |  | **0.302×** | -8.5 | 1e-15 | 30/32 (NCI-H23, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.642×** | -8.5 | 1e-15 | 30/34 (C32, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.572×** | -7.6 | 2e-12 | 25/33 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.574×** | -7.5 | 3e-12 | 25/33 (PANC-1, SW 1271, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.378×** | -6.9 | 2e-10 | 25/33 (C32, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.604×** | -6.8 | 3e-10 | 28/33 (BT-474, HepG2/C3A, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.707×** | -6.6 | 1e-09 | 29/34 (C32, BT-474, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.620×** | -6.5 | 3e-09 | 31/34 (BT-474, C32, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.412×** | -6.3 | 1e-08 | 26/34 (H4, C32, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.614×** | -6.2 | 1e-08 | 26/33 (CFPAC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14631. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 152 | 0 | 19 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0507× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.158× (z -18.2) |
| [[C32 (line)]] | wt | 118 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -26.5) |
| [[LOX-IMVI (line)]] | wt | 119 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -24.1) |
| [[A549 (line)]] | wt | 207 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0468× (z -38.6) |
| [[HOP62 (line)]] | alt | 115 | 2 | 10 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -17.8) |
| [[NCI-H1573 (line)]] | alt | 384 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0446× (z -40.3) |
| [[NCI-H23 (line)]] | alt | 313 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -26.1) |
| [[NCI-H1792 (line)]] | alt | 203 | 0 | 11 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.103× (z -19.8) |
| [[PANC-1 (line)]] | alt | 125 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -21.9) |
| [[CFPAC-1 (line)]] | alt | 145 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -21.4) |
| [[hTERT-HPNE (line)]] | wt | 186 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -16.6) |
| [[NCI-H460 (line)]] | wt | 154 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.260× (z -14.4) |
| [[SNU-423 (line)]] | alt | 104 | 0 | 8 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0694× (z -20.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.165× (z -20.7) |
| [[H4 (line)]] | wt | 165 | 0 | 7 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.128× (z -16.0) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.220× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 105 | 1 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +11.1) | [[Harringtonine (drug)]] 5 µM 0.0835× (z -19.1) |
| [[SW 900 (line)]] | alt | 128 | 2 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -19.4) |
| [[A-427 (line)]] | wt | 65.9 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.164× (z -15.6) |
| [[AsPC-1 (line)]] | alt | 151 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +10.6) | [[Harringtonine (drug)]] 5 µM 0.200× (z -13.7) |
| [[HepG2_C3A (line)]] | wt | 87.8 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -17.0) |
| [[NCI-H2030 (line)]] | alt | 189 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.142× (z -13.0) |
| [[Panc 03.27 (line)]] | alt | 95.8 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -19.8) |
| [[NCI-H2347 (line)]] | alt | 126 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -23.8) |
| [[A-172 (line)]] | wt | 122 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -20.0) |
| [[SW 1271 (line)]] | alt | 295 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.169× (z -9.2) |
| [[A498 (line)]] | wt | 130 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0861× (z -27.3) |
| [[CHP-212 (line)]] | wt | 33.3 | 0 | 3 (1 ⚠) | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0546× (z -10.7) |
| [[Hs 766T (line)]] | wt | 160 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HS-578T (line)]] | alt | 161 | 1 | 2 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -19.7) |
| [[J82 (line)]] | alt | 183 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 84.5 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.137× (z -14.0) |
| [[SW 1088 (line)]] | alt | 132 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0426× (z -11.6) |
| [[AN3 CA (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.21 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.86 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.30 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 26.5 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.68 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.96 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.66 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.55 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 62.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.83 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.53 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14631), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSMR]] | +0.72 | +0.82 / +0.70 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[LINC00862]] | +0.65 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[LUCAT1]] | +0.63 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[ITGA2-AS1]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[SPRED3]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[TEX21P]] | +0.57 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[TMEM165]] | +0.57 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[LINC01829]] | +0.57 | +0.36 / +0.62 | both halves | 9e-05 |  |
| [[TPTEP2-CSNK1E]] | +0.54 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[GPATCH2L]] | +0.53 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[EFCAB13]] | +0.53 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[CCDC168]] | +0.53 | +0.50 / +0.39 | both halves | 6e-05 |  |
| [[C11orf91]] | +0.52 | +0.49 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC6]] | -0.55 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[SORL1]] | -0.52 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[PHKB]] | -0.52 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[EHMT2]] | -0.52 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[NHLRC3]] | -0.51 | -0.50 / -0.40 | both halves | 4e-05 |  |
| [[PIK3C2B]] | -0.50 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[MPP7]] | -0.49 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[MAP2K6]] | -0.49 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[LRP4]] | -0.49 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[STXBP6]] | -0.49 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[TTC5]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[FYCO1]] | -0.48 | -0.32 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C11orf91]] | B | C11orf91 activity raises OSMR-DT's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 3.71× lower at baseline in the lines without C11orf91 | 0.003 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[DUSP5-DT]] | B | DUSP5-DT activity raises OSMR-DT's level | lines that do not express DUSP5-DT (7) vs lines expressing it (43) | 1.19× lower at baseline in the lines without DUSP5-DT | 0.057 | ⚠ within organs, on part of the lines; also absent: PRR5L, MAMLD1; maybe low, not absent |
| [[GABRE]] | B | GABRE activity raises OSMR-DT's level | lines that do not express GABRE (20) vs lines expressing it (30) | 1.53× lower at baseline in the lines without GABRE | 0.061 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |
| [[ADORA1]] | B | ADORA1 activity raises OSMR-DT's level | lines that do not express ADORA1 (7) vs lines expressing it (43) | 2.02× lower at baseline in the lines without ADORA1 | 0.063 | ⚠ within organs, on part of the lines; also absent: DRAM1, HHAT, SUGCT; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers OSMR-DT's level | compounds that target TOP2A: 2 of 5 raise it (Doxorubicin, Idarubicin) | 40% of the class's compounds vs 0.6% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[IL1RAP]] | B | IL1RAP activity raises OSMR-DT's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 3.65× lower at baseline in the lines without IL1RAP | 0.077 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[ITGA2-AS1]] | C | ITGA2-AS1 activity raises OSMR-DT's level | lines that do not express ITGA2-AS1 (4) vs lines expressing it (46) | 2.20× lower at baseline in the lines without ITGA2-AS1 | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYNJ2, ZNF827, NABP1; maybe low, not absent |
| [[OSMR]] | C | OSMR activity raises OSMR-DT's level | lines that do not express OSMR (13) vs lines expressing it (37) | 11.71× lower at baseline in the lines without OSMR | 0.060 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A, APC, SETD1B; also absent: OSMR-DT, LIFR, IL1R1; co-absent with the target; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF217]] | B | OSMR-DT activity raises RNF217's level | lines that do not express OSMR-DT (15) vs lines expressing it (35) | 1.85× lower at baseline in the lines without OSMR-DT | 0.068 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: OSMR, LIFR, IL1R1 |
| [[GABRE]] | B | OSMR-DT activity raises GABRE's level | lines that do not express OSMR-DT (15) vs lines expressing it (35) | 1.53× lower at baseline in the lines without OSMR-DT | 0.070 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: OSMR, LIFR, IL1R1 |
| [[OSMR]] | C | OSMR-DT activity raises OSMR's level | lines that do not express OSMR-DT (15) vs lines expressing it (35) | 11.12× lower at baseline in the lines without OSMR-DT | 5e-05 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: OSMR, LIFR, IL1R1; co-absent with the target |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | OSMR-DT's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | OSMR-DT's natural level across 33 lines (lineage-adjusted; a glimpse) | r -0.71 | 0.507 over the table, 0.088 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.484). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.6, -15.5); signed map (-0.1, 30.9). **Vector** length 124, 42.1% of its response variance represented; |z| ≥ 3 in 1,282 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +7.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +2.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.1 | +0.9 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +1.7 | +2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +1.2 |
| fall | [[NG25 (drug)]] 5 µM |  | -6.2 | -8.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.1 | -6.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.8 | -12.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.8 | -6.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.6 | -8.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.6 | -3.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.4 | -6.6 |

## What is on record

|  |  |
|---|---|
| Name | OSMR divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5p13.1 — chr5:38,682,581-38,845,829 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously OSMR-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50296](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50296) · Entrez [101929768](https://www.ncbi.nlm.nih.gov/gene/101929768) · Ensembl [ENSG00000249740](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249740)

## Data

Gene col 14631: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14631); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14631, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14631]; `tensor/DDL_lfc|DDL_z.npy` [14631]; `embed/gene_vectors.npy` [14631]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14631 or target_col == 14631). Every well: [[OSMR-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSMR-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
