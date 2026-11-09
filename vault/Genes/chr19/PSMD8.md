---
symbol: "PSMD8"
type: "gene"
col: 1798
ensembl_id: "ENSG00000099341"
name: "proteasome 26S subunit, non-ATPase 8"
location: "19q13.2"
module: 72
arm: "+"
pooled_cpm: 59.26
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# PSMD8

*proteasome 26S subunit, non-ATPase 8* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.59× (z +12.4, q 2e-32, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.486×; ⚠ cell-cycle shift, would explain all of this change); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (SW 1088 0.0620×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMC4]] (+0.65, fdr 1e-05), [[BAG3]] (+0.64, fdr 1e-05), [[ACO2]] (+0.64, fdr 7e-06); moves opposite to [[LUC7L3]] (-0.55, fdr 1e-05), [[UGCG]] (-0.55, fdr 4e-05), [[PRPF4B]] (-0.54, fdr 3e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1798.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.59×** | +12.4 | 2e-32 | 48/48 (HT-29, NCI-H1573, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.46×** | +11.7 | 4e-29 | 46/48 (PANC-1, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.42×** | +11.5 | 2e-28 | 48/48 (HT-29, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +10.9 | 1e-25 | 46/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.33×** | +10.4 | 3e-23 | 47/48 (HT-29, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.16×** | +9.6 | 7e-20 | 40/41 (PANC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +7.0 | 2e-10 | 43/48 (HT-29, C32, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.64×** | +5.9 | 2e-07 | 35/45 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.53×** | +5.5 | 2e-06 | 36/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.51×** | +5.4 | 4e-06 | 32/48 (BT-474, NCI-H460, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +5.0 | 3e-05 | 37/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.46×** | +4.9 | 5e-05 | 36/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.98×** | +4.6 | 2e-04 | 31/45 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.6 | 2e-04 | 37/47 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.45×** | +4.6 | 2e-04 | 31/49 (HEC-1-A, A-427, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.60×** | +4.2 | 0.001 | 36/48 (LOX-IMVI, PANC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.001 | 24/48 (A-172, HOP62, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.75×** | +3.8 | 0.005 | 37/48 (HT-29, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.61×** | +3.2 | 0.029 | 24/48 (PANC-1, SHP-77, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Mifepristone (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.044 | 25/47 (LS 180, KATO III, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.044 | 24/48 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1798.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.486×; ⚠ cell-cycle shift, would explain all of this change); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (SW 1088 0.0620×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.821× | -3.7 | 0.15 | 26/48 (NCI-H2347, NCI-H1792, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.746× | -3.4 | 0.21 | 21/49 (NCI-H23, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.776× | -3.2 | 0.26 | 25/47 (C32, AsPC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.787× | -3.1 | 0.26 | 20/48 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.846× | -3.0 | 0.27 | 16/48 (SNU-423, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1798. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 85.0 | 8 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.79× (z +10.4) | — |
| [[NCI-H460 (line)]] | wt | 32.0 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 74.1 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.83× (z +13.1) | — |
| [[COLO 205 (line)]] | alt | 36.0 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.06× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 48.0 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.29× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 42.3 | 4 (2 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 3.61× (z +9.2) | — |
| [[A549 (line)]] | wt | 94.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 71.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.12× (z +10.7) | — |
| [[LoVo (line)]] | wt | 41.3 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.68× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 59.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 31.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.35× (z +11.0) | — |
| [[A-427 (line)]] | wt | 76.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 55.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 44.6 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.17× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 75.7 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.21× (z +10.6) | — |
| [[KATO III (line)]] | alt | 66.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.88× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 62.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.2) | — |
| [[SW480 (line)]] | alt | 57.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 77.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.1) | — |
| [[A498 (line)]] | wt | 76.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[BT-474 (line)]] | alt | 47.5 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.38× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | — |
| [[C-33 A (line)]] | alt | 44.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[H4 (line)]] | wt | 111 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.18× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 40.8 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.92× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 55.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H2347 (line)]] | alt | 59.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +9.9) | — |
| [[RKO (line)]] | wt | 76.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +8.8) | — |
| [[SW 1088 (line)]] | alt | 53.2 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0620× (z -9.0) |
| [[AN3 CA (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1798), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMC4]] | +0.65 | +0.67 / +0.57 | both halves | 1e-05 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[BAG3]] | +0.64 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[ACO2]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[EIF3I]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 | STRING 454 |
| [[SERPINH1]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[MRPL18]] | +0.61 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[PRR13]] | +0.61 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[FAM219A]] | +0.58 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[PITRM1]] | +0.57 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[PSMB5]] | +0.57 | +0.59 / +0.48 | both halves | 2e-05 | same gene group; pathway: ABC transporter disorders; STRING 991 |
| [[ALKBH6]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[KCTD5]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LUC7L3]] | -0.55 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[UGCG]] | -0.55 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[PRPF4B]] | -0.54 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[EBLN2]] | -0.52 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[HMGN3]] | -0.50 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[MAZ]] | -0.50 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[ASB13]] | -0.49 | -0.41 / -0.51 | both halves | 4e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[CELF1]] | -0.49 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[RNF145]] | -0.49 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[EHMT2]] | -0.48 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[HNRNPD]] | -0.48 | -0.40 / -0.47 | both halves | 5e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 430 |
| [[PUM2]] | -0.48 | -0.41 / -0.53 | both halves | 4e-05 | pathway: Neddylation |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PSMD8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.4, -9.6); signed map (-24.4, -26.6). **Vector** length 80.8, 23.5% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.4 | +10.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.5 | +11.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.3 | +12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +10.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.1 | +4.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.1 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +7.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.4 | +0.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.0 | +1.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -0.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit, non-ATPase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,374,563-38,383,850 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S14, Nin1p, p31, HIP6, HYPF, Rpn12 |
| Gene groups (HGNC) | Proteasome |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 169 pathways, smallest: Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC); Cross-presentation of soluble exogenous antigens (endosomes) |
| Matched by | ensembl_id |

**Function**, from UniProt [P48556](https://www.uniprot.org/uniprotkb/P48556) (26S proteasome non-ATPase regulatory subunit 8):

> Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair.

**Summary**, from NCBI Gene [5714](https://www.ncbi.nlm.nih.gov/gene/5714):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9566](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9566) · Entrez [5714](https://www.ncbi.nlm.nih.gov/gene/5714) · UniProt [P48556](https://www.uniprot.org/uniprotkb/P48556) · Ensembl [ENSG00000099341](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099341)

## Data

Gene col 1798: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1798); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1798, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1798]; `tensor/DDL_lfc|DDL_z.npy` [1798]; `embed/gene_vectors.npy` [1798]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1798 or target_col == 1798). Every well: [[PSMD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
