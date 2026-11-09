---
symbol: "SSB"
type: "gene"
col: 6166
ensembl_id: "ENSG00000138385"
name: "small RNA binding exonuclease protection factor La"
location: "2q31.1"
module: 1
arm: "+"
pooled_cpm: 119.9
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SSB

*small RNA binding exonuclease protection factor La* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.06× (z +12.4, q 3e-32, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.77× (z +6.3, q 2e-08, up in 42 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (SW 1271 0.101×; ⚠ transcription drop; cell-cycle shift, explains ~85% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.474×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLTM]] (+0.69, fdr 7e-06), [[U2SURP]] (+0.62, fdr 1e-05), [[ZNHIT6]] (+0.61, fdr 1e-05); moves opposite to [[MXD3]] (-0.54, fdr 2e-04), [[PDCD6]] (-0.54, fdr 6e-05), [[IFI27L1]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6166.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.06×** | +12.4 | 3e-32 | 49/49 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.82×** | +11.4 | 2e-27 | 42/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.15×** | +8.1 | 1e-13 | 40/45 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.03×** | +7.8 | 1e-12 | 42/48 (NCI-H1573, NCI-H1792, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.58×** | +7.2 | 9e-11 | 37/48 (A-172, A549, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.87×** | +6.9 | 6e-10 | 40/47 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.77×** | +6.5 | 5e-09 | 39/48 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.77×** | +6.3 | 2e-08 | 42/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.55×** | +5.0 | 3e-05 | 35/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.0 | 3e-05 | 37/47 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +4.7 | 1e-04 | 38/48 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +4.5 | 4e-04 | 36/48 (BT-474, SW480, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.45×** | +4.3 | 8e-04 | 37/48 (LoVo, NCI-H460, …) | rises with dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.003 | 31/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.004 | 33/48 (NCI-H2347, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.018 | 31/48 (HS-578T, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +3.4 | 0.023 | 32/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.086 | 27/48 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6166.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (SW 1271 0.101×; ⚠ transcription drop; cell-cycle shift, explains ~85% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.474×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.806× | -3.3 | 0.50 | 31/48 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.764× | -3.0 | 0.69 | 27/48 (J82, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6166. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 118 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.42× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.27× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 67.0 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.59× (z +8.7) | — |
| [[A-172 (line)]] | wt | 103 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +15.9) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.70× (z +8.8) | — |
| [[LoVo (line)]] | wt | 68.8 | 6 (6 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.23× (z +10.2) ⚠ toxic; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H460 (line)]] | wt | 123 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.13× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.92× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 74.0 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +11.9) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[HS-578T (line)]] | alt | 88.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 136 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SNU-423 (line)]] | alt | 84.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.23× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[CFPAC-1 (line)]] | alt | 101 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +12.4) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[Hs 766T (line)]] | wt | 77.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.00× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 102 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.61× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 172 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1573 (line)]] | alt | 77.4 | 3 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.52× (z +11.5) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[SW480 (line)]] | alt | 167 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.38× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 152 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.12× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A498 (line)]] | wt | 144 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[C32 (line)]] | wt | 75.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +10.8) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[H4 (line)]] | wt | 80.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[KATO III (line)]] | alt | 108 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LOX-IMVI (line)]] | wt | 122 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 91.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RPMI-7951 (line)]] | alt | 121 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 105 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW 900 (line)]] | alt | 95.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +10.8) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[AsPC-1 (line)]] | alt | 87.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +10.0) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[HCT15 (line)]] | alt | 138 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.91× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.1) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[HepG2_C3A (line)]] | wt | 125 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 77.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[J82 (line)]] | alt | 110 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H23 (line)]] | alt | 237 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.53× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[Panc 03.27 (line)]] | alt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RKO (line)]] | wt | 199 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.33× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW 1271 (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.101× (z -11.1) ⚠ transcription drop; cell-cycle shift, explains ~85% of this change |
| [[AN3 CA (line)]] | alt | 166 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 188 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 153 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 170 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6166), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLTM]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 | same gene group |
| [[U2SURP]] | +0.62 | +0.69 / +0.51 | both halves | 1e-05 | same gene group; STRING 414 |
| [[ZNHIT6]] | +0.61 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[MTIF2]] | +0.61 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[RSL1D1]] | +0.61 | +0.63 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 460 |
| [[ZMYM4]] | +0.58 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[RAD50]] | +0.58 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[ZNF326]] | +0.58 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[RBM28]] | +0.57 | +0.59 / +0.59 | both halves | 7e-06 | same gene group |
| [[EIF3A]] | +0.57 | +0.60 / +0.51 | both halves | 1e-05 | STRING 518 |
| [[NUDT9]] | +0.57 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[FKTN]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXD3]] | -0.54 | -0.31 / -0.58 | both halves | 2e-04 |  |
| [[PDCD6]] | -0.54 | -0.38 / -0.59 | both halves | 6e-05 |  |
| [[IFI27L1]] | -0.53 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[RER1]] | -0.53 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[SLC35E1]] | -0.52 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[SENP5]] | -0.52 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[SEC16A]] | -0.52 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[GMPPB]] | -0.52 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[MAPK7]] | -0.52 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[P3H1]] | -0.52 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[TOP3A]] | -0.51 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[CRELD2]] | -0.51 | -0.21 / -0.59 | both halves | 7e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.485). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-35.4, -26.0); signed map (12.2, -37.2). **Vector** length 77.6, 29.5% of its response variance represented; |z| ≥ 3 in 858 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.9 | +3.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.6 | +3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +3.5 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.4 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +3.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.3 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | -0.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.7 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -0.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.8 | -0.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.6 | +1.4 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -1.6 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | small RNA binding exonuclease protection factor La |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:169,791,933-169,812,064 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SSB/La, LARP3, La, La/SSB |
| Gene groups (HGNC) | La ribonucleoproteins; RNA binding motif containing |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 3 pathways, smallest: RNA Polymerase III Transcription Termination; RNA Polymerase III Abortive And Retractive Initiation; RNA Polymerase III Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [P05455](https://www.uniprot.org/uniprotkb/P05455) (Lupus La protein):

> Binds to the 3' poly(U) terminus of nascent RNA polymerase III transcripts, protecting them from exonuclease digestion and facilitating their folding and maturation. In case of Coxsackievirus B3 infection, binds to the viral internal ribosome entry site (IRES) and stimulates the IRES-mediated translation.

**Summary**, from NCBI Gene [6741](https://www.ncbi.nlm.nih.gov/gene/6741):

> The protein encoded by this gene is involved in diverse aspects of RNA metabolism, including binding and protecting poly(U) termini of nascent RNA polymerase III transcripts from exonuclease digestion, processing 5' and 3' ends of pre-tRNA precursors, acting as an RNA chaperone, and binding viral RNAs associated with hepatitis C virus. Autoantibodies reacting with this protein are found in the sera of patients with Sjogren syndrome and systemic lupus erythematosus. Alternative promoter usage …

**Accessions** — [HGNC:11316](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11316) · Entrez [6741](https://www.ncbi.nlm.nih.gov/gene/6741) · UniProt [P05455](https://www.uniprot.org/uniprotkb/P05455) · Ensembl [ENSG00000138385](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138385)

## Data

Gene col 6166: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6166); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6166, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6166]; `tensor/DDL_lfc|DDL_z.npy` [6166]; `embed/gene_vectors.npy` [6166]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6166 or target_col == 6166). Every well: [[SSB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
