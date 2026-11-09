---
symbol: "ATG7"
type: "gene"
col: 12413
ensembl_id: "ENSG00000197548"
name: "autophagy related 7"
location: "3p25.3"
module: 171
arm: "-"
pooled_cpm: 191.09
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# ATG7

*autophagy related 7* — 3p25.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (AsPC-1 2.33×, hTERT-HPNE 2.31×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 1.91×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (AsPC-1 2.13×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (A-427 1.96×).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.550× (z -10.6, q 2e-23, down in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.624× (z -8.2, q 3e-14, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIATNB]] (+0.59, fdr 7e-06), [[FAM120B]] (+0.58, fdr 1e-05), [[NT5E]] (+0.58, fdr 1e-05); moves opposite to [[FBXO7]] (-0.59, fdr 3e-05), [[SGCE]] (-0.57, fdr 1e-05), [[PPP1CB]] (-0.55, fdr 3e-05).
> It sits in the **-** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12413.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (AsPC-1 2.33×, hTERT-HPNE 2.31×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 1.91×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (AsPC-1 2.13×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (A-427 1.96×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.3 | 0.008 | 22/48 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 1.20× | +3.4 | 0.22 | 22/48 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.27 | 21/48 (AsPC-1, BT-474, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.27 | 22/48 (A-172, A498, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.0 | 0.27 | 19/47 (HOP62, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12413.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.550×** | -10.6 | 2e-23 | 43/49 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -9.2 | 9e-18 | 39/44 (NCI-H1573, HCT15, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.607×** | -8.4 | 1e-14 | 36/45 (NCI-H23, A549, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.624×** | -8.2 | 3e-14 | 37/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.742×** | -7.6 | 3e-12 | 38/49 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.675×** | -7.1 | 9e-11 | 38/48 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.724×** | -5.6 | 1e-06 | 33/47 (CHP-212, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.748×** | -5.1 | 3e-05 | 35/47 (LoVo, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.630×** | -4.4 | 8e-04 | 31/47 (C32, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.798×** | -4.0 | 0.004 | 23/48 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.803×** | -4.0 | 0.004 | 25/48 (C32, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.861× | -3.8 | 0.006 | 15/48 (PANC-1, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.862× | -3.8 | 0.006 | 17/48 (A498, SHP-77, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.820×** | -3.6 | 0.013 | 25/48 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.822×** | -3.6 | 0.014 | 25/49 (NCI-H2122, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.823×** | -3.4 | 0.021 | 24/48 (SW1417, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12413. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 359 | 0 | 11 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -20.8) |
| [[NCI-H1573 (line)]] | alt | 292 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 0.297× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 353 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -18.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.321× (z -14.8) |
| [[C32 (line)]] | wt | 190 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.443× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 292 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.331× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 343 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -10.9) |
| [[A-427 (line)]] | wt | 150 | 1 | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 1.96× (z +8.8) | [[Harringtonine (drug)]] 0.5 µM 0.358× (z -13.2) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.396× (z -11.8) |
| [[A549 (line)]] | wt | 322 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -18.7) |
| [[hTERT-HPNE (line)]] | wt | 189 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.31× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.257× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -9.2) |
| [[KATO III (line)]] | alt | 159 | 0 | 5 (5 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.426× (z -12.2) ⚠ transcription drop |
| [[NCI-H2030 (line)]] | alt | 241 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -12.2) |
| [[SW480 (line)]] | alt | 152 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.501× (z -11.9) |
| [[A498 (line)]] | wt | 134 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.422× (z -10.1) |
| [[LS 180 (line)]] | wt | 158 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.415× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.466× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 160 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 146 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.405× (z -10.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 119 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.379× (z -11.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 145 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.210× (z -10.6) ⚠ toxic |
| [[HCT15 (line)]] | alt | 227 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -17.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 125 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.490× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 149 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.498× (z -10.0) |
| [[SW1417 (line)]] | alt | 163 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -16.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.405× (z -9.8) |
| [[J82 (line)]] | alt | 174 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -8.9) |
| [[LoVo (line)]] | wt | 162 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.489× (z -10.2) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 175 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -11.2) |
| [[NCI-H596 (line)]] | alt | 169 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0681× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 149 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.408× (z -9.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 241 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.331× (z -11.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -12.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 225 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -10.6) |
| [[SW 900 (line)]] | alt | 168 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.418× (z -8.9) ⚠ transcription drop |
| [[AN3 CA (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 123 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 91.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 127 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 186 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 181 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 145 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 351 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 146 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12413), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIATNB]] | +0.59 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[FAM120B]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[NT5E]] | +0.58 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[BACH1]] | +0.55 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[KATNIP]] | +0.54 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[SNRPB]] | +0.54 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[BLZF2P]] | +0.54 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[MYL12A]] | +0.54 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[HMGA2]] | +0.53 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[DOCK1]] | +0.53 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ANTXR2]] | +0.53 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[MIR31HG]] | +0.53 | +0.53 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO7]] | -0.59 | -0.60 / -0.43 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[SGCE]] | -0.57 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[PPP1CB]] | -0.55 | -0.50 / -0.46 | both halves | 3e-05 | pathway: Oncogenic MAPK signaling |
| [[TMEM94]] | -0.54 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[TADA1]] | -0.54 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[SLC25A30]] | -0.53 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[BPNT1]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[PRKAB2]] | -0.52 | -0.58 / -0.40 | both halves | 5e-05 | pathway: Autophagy |
| [[CCDC6]] | -0.52 | -0.62 / -0.46 | both halves | 2e-05 |  |
| [[KCTD3]] | -0.51 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[HSF2]] | -0.51 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[RCOR3]] | -0.51 | -0.47 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | ATG7's natural level raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | ATG7's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.70 | 0.268 over the table, 0.011 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Sulfatinib (drug)]] 5 µM | C | ATG7's natural level raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | ATG7's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64 | 0.383 over the table, 0.086 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | ATG7's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | ATG7's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.59 | 0.476 over the table, 0.076 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | ATG7's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | ATG7's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.491 over the table, 0.094 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **-** arm (projection on the module's main direction -0.546). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (18.3, -9.5); signed map (9.8, 42.6). **Vector** length 134, 46.8% of its response variance represented; |z| ≥ 3 in 1,272 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.5 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.8 | +3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.7 | +3.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.4 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +1.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.0 | +2.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.9 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +2.4 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.3 | -9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -7.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -5.6 | -4.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.5 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.4 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.9 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | autophagy related 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:11,272,309-11,557,665 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GSA7, DKFZp434N0735; previously APG7L |
| Gene groups (HGNC) | Ubiquitin like modifier activating enzymes; Autophagy related |
| Reactome | 13 pathways, smallest: Dengue Virus Attachment and Entry; Signaling by BRAF and RAF1 fusions; Oncogenic MAPK signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O95352](https://www.uniprot.org/uniprotkb/O95352) (Ubiquitin-like modifier-activating enzyme ATG7):

> E1-like activating enzyme involved in the 2 ubiquitin-like systems required for cytoplasm to vacuole transport (Cvt) and autophagy. Activates ATG12 for its conjugation with ATG5 as well as the ATG8 family proteins for their conjugation with phosphatidylethanolamine. Both systems are needed for the ATG8 association to Cvt vesicles and autophagosomes membranes. Required for autophagic death induced by caspase-8 inhibition. Facilitates LC3-I lipidation with phosphatidylethanolamine to form LC3-II …

**Summary**, from NCBI Gene [10533](https://www.ncbi.nlm.nih.gov/gene/10533):

> This gene encodes an E1-like activating enzyme that is essential for autophagy and cytoplasmic to vacuole transport. The encoded protein is also thought to modulate p53-dependent cell cycle pathways during prolonged metabolic stress. It has been associated with multiple functions, including axon membrane trafficking, axonal homeostasis, mitophagy, adipose differentiation, and hematopoietic stem cell maintenance. Alternative splicing results in multiple transcript variants. [provided by RefSeq, …

**Accessions** — [HGNC:16935](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16935) · Entrez [10533](https://www.ncbi.nlm.nih.gov/gene/10533) · UniProt [O95352](https://www.uniprot.org/uniprotkb/O95352) · Ensembl [ENSG00000197548](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197548)

## Data

Gene col 12413: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12413); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12413, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12413]; `tensor/DDL_lfc|DDL_z.npy` [12413]; `embed/gene_vectors.npy` [12413]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12413 or target_col == 12413). Every well: [[ATG7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATG7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
