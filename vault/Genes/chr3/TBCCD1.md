---
symbol: "TBCCD1"
type: "gene"
col: 3507
ensembl_id: "ENSG00000113838"
name: "TBCC domain containing 1"
location: "3q27.3"
module: 222
arm: "+"
pooled_cpm: 13.07
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 5
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/222"]
generated_by: "tahoemap"
---

# TBCCD1

*TBCC domain containing 1* — 3q27.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.08× (z +23.8, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.738× (z -4.9, q 4e-04, down in 10 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.810× (z -4.2, q 0.005, down in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 0.106×, SW480 0.276×, HS-578T 0.205×; ⚠ toxic; transcription drop); [[Tofacitinib (drug)]] 0.5 µM in 1 line (HCT15 0.0789×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0877×); [[Acetohexamide (drug)]] 0.5 µM in 1 line (HCT15 0.0897×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRYGS]] (+0.69, fdr 7e-06, ⚠ same locus), [[ARHGAP1]] (+0.60, fdr 4e-05), [[C11orf24]] (+0.52, fdr 2e-04), [[TUT1]] (+0.52, fdr 1e-05); moves opposite to [[GCNT2]] (-0.57, fdr 2e-05), [[QPRT]] (-0.54, fdr 4e-05), [[DENND5B]] (-0.52, fdr 3e-04).
> It is in [[Module 222]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3507.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.08×** | +23.8 | 0e+00 | 43/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.67×** | +22.0 | 0e+00 | 43/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.27×** | +20.0 | 0e+00 | 44/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +18.1 | 0e+00 | 39/47 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +16.5 | 0e+00 | 34/47 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +11.9 | 2e-30 | 33/45 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +11.6 | 2e-29 | 34/46 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +10.6 | 2e-24 | 31/41 (SNU-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +8.1 | 2e-14 | 27/46 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +7.8 | 3e-13 | 31/47 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.59×** | +6.5 | 3e-09 | 16/31 (A498, J82, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +5.6 | 8e-07 | 23/46 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +5.4 | 3e-06 | 17/44 (HepG2/C3A, SW1417, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +4.9 | 4e-05 | 18/47 (LoVo, HT-29, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.8 | 5e-05 | 18/48 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.65×** | +4.4 | 4e-04 | 10/47 (C32, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.8 | 0.004 | 12/48 (SW1417, BT-474, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3507.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 0.106×, SW480 0.276×, HS-578T 0.205×; ⚠ toxic; transcription drop); [[Tofacitinib (drug)]] 0.5 µM in 1 line (HCT15 0.0789×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0877×); [[Acetohexamide (drug)]] 0.5 µM in 1 line (HCT15 0.0897×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.738×** | -4.9 | 4e-04 | 10/22 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.776×** | -4.3 | 0.005 | 17/36 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.810×** | -4.2 | 0.005 | 16/48 (HepG2/C3A, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.741×** | -3.6 | 0.040 | 9/44 (SW480, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.867× | -3.3 | 0.086 | 8/48 (A-427, CHP-212, …) | all doses, flat |  |
| [[Clotrimazole (drug)]] 5 µM |  | 0.871× | -3.3 | 0.086 | 7/48 (SW 1088, CHP-212, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.692×** | -3.3 | 0.091 | 14/44 (SW480, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.951× | -3.2 | 0.11 | 4/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.827× | -3.1 | 0.11 | 14/40 (A-172, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.836× | -3.1 | 0.11 | 6/48 (H4, SW480, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3507. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 21.7 | 8 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.14× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -12.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 10.7 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.23× (z +12.0) | — |
| [[PANC-1 (line)]] | alt | 21.5 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.67× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.106× (z -18.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 10.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +9.0) | — |
| [[KATO III (line)]] | alt | 25.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.42× (z +13.2) | — |
| [[NCI-H460 (line)]] | wt | 8.05 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +10.7) | — |
| [[A-427 (line)]] | wt | 34.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.75× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 12.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 11.1 | 0 | 2 | — | [[Tofacitinib (drug)]] 0.5 µM 0.0789× (z -9.8) |
| [[HS-578T (line)]] | alt | 17.0 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.205× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 16.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +12.4) | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +10.0) | — |
| [[A498 (line)]] | wt | 7.90 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.75× (z +10.7) | — |
| [[C-33 A (line)]] | alt | 16.7 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.144× (z -9.1) |
| [[COLO 205 (line)]] | alt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +10.2) | — |
| [[HOP62 (line)]] | alt | 10.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.01× (z +8.5) | — |
| [[J82 (line)]] | alt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +11.6) | — |
| [[LS 180 (line)]] | wt | 7.80 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +10.8) | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0877× (z -9.6) |
| [[SHP-77 (line)]] | alt | 16.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 19.0 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.120× (z -8.7) |
| [[SNU-423 (line)]] | alt | 7.29 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.45× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +10.4) | — |
| [[A-172 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3507), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYGS]] | +0.69 | +0.68 / +0.74 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ARHGAP1]] | +0.60 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[C11orf24]] | +0.52 | +0.32 / +0.48 | both halves | 2e-04 |  |
| [[TUT1]] | +0.52 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[TRIOBP]] | +0.52 | +0.32 / +0.47 | both halves | 2e-04 |  |
| [[KATNA1]] | +0.52 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[HNRNPLL]] | +0.52 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[CAPRIN2]] | +0.51 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[ITGB5]] | +0.50 | +0.29 / +0.45 | both halves | 2e-04 |  |
| [[LINC00941]] | +0.50 | +0.36 / +0.42 | both halves | 1e-04 |  |
| [[CRLS1]] | +0.49 | +0.34 / +0.38 | both halves | 1e-04 |  |
| [[ZNF333]] | +0.48 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[SLX4]] | +0.47 | +0.30 / +0.53 | both halves | 2e-04 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCNT2]] | -0.57 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[QPRT]] | -0.54 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[DENND5B]] | -0.52 | -0.59 / -0.29 | both halves | 3e-04 |  |
| [[STAU2]] | -0.51 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[HSPB1]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[MID1]] | -0.50 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[FBXO2]] | -0.50 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[PSMA4]] | -0.49 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[CYP4F3]] | -0.49 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[PRKG1]] | -0.49 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[CLN3]] | -0.48 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[GNGT1]] | -0.48 | -0.29 / -0.54 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TBCCD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 222]]; 10 genes; every member is in the + arm (projection on the module's main direction -0.674). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.2, 14.4); signed map (-47.0, 4.9). **Vector** length 62.5, 10.1% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +18.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +11.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +11.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +1.6 | +3.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.3 | +2.1 |
|  | [[Bexarotene (drug)]] 5 µM |  | +1.3 | +2.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.1 | +1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.0 | +2.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.0 | +1.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -3.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.7 | -1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -4.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | TBCC domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.3 — chr3:186,546,067-186,570,543 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10560 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVR7](https://www.uniprot.org/uniprotkb/Q9NVR7) (TBCC domain-containing protein 1):

> Plays a role in the regulation of centrosome and Golgi apparatus positioning, with consequences on cell shape and cell migration.

**Summary**, from NCBI Gene [55171](https://www.ncbi.nlm.nih.gov/gene/55171):

> Involved in several processes, including maintenance of Golgi location; maintenance of centrosome location; and regulation of cell shape. Located in spindle pole centrosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25546](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25546) · Entrez [55171](https://www.ncbi.nlm.nih.gov/gene/55171) · UniProt [Q9NVR7](https://www.uniprot.org/uniprotkb/Q9NVR7) · Ensembl [ENSG00000113838](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113838)

## Data

Gene col 3507: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3507); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3507, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3507]; `tensor/DDL_lfc|DDL_z.npy` [3507]; `embed/gene_vectors.npy` [3507]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3507 or target_col == 3507). Every well: [[TBCCD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBCCD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
