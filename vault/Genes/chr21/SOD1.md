---
symbol: "SOD1"
type: "gene"
col: 6600
ensembl_id: "ENSG00000142168"
name: "superoxide dismutase 1"
location: "21q22.11"
module: 60
arm: "+"
pooled_cpm: 87.96
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# SOD1

*superoxide dismutase 1* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.67× (z +14.9, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 3.54× (z +11.5, q 2e-28, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.283×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.221×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPB1]] (+0.78, fdr 7e-06), [[PSMB4]] (+0.75, fdr 7e-06), [[UBB]] (+0.74, fdr 7e-06); moves opposite to [[ENTR1]] (-0.56, fdr 3e-05), [[CTU2]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6600.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **4.67×** | +14.9 | 0e+00 | 49/49 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **4.26×** | +13.5 | 6e-39 | 43/43 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.54×** | +11.5 | 2e-28 | 48/48 (CFPAC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.29×** | +11.5 | 2e-28 | 48/48 (LOX-IMVI, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.25×** | +11.4 | 5e-28 | 48/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.07×** | +9.8 | 8e-21 | 45/45 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.46×** | +8.7 | 3e-16 | 48/48 (C32, LOX-IMVI, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +8.2 | 1e-14 | 46/49 (A-172, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.98×** | +5.5 | 2e-06 | 44/45 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.74×** | +5.2 | 1e-05 | 41/47 (C32, NCI-H1573, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.70×** | +5.1 | 1e-05 | 44/48 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.7 | 1e-04 | 37/47 (MIA PaCa-2, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.08×** | +3.7 | 0.009 | 41/47 (HepG2/C3A, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.47×** | +3.6 | 0.014 | 33/50 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.16×** | +3.5 | 0.020 | 37/49 (LOX-IMVI, CFPAC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6600.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.283×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.221×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.785× | -3.1 | 0.84 | 32/48 (SW 900, SW1417, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6600. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 159 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +11.2) | — |
| [[C32 (line)]] | wt | 64.3 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.16× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 7.50× (z +13.5) | — |
| [[HOP62 (line)]] | alt | 78.9 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.95× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 6.25× (z +13.7) | — |
| [[LOX-IMVI (line)]] | wt | 58.2 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.47× (z +13.1) | — |
| [[A-427 (line)]] | wt | 129 | 5 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.59× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -13.1) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 93.1 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.34× (z +12.9) | — |
| [[HEC-1-A (line)]] | alt | 113 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.92× (z +11.3) | — |
| [[HT-29 (line)]] | alt | 67.6 | 6 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 4.29× (z +10.7) | — |
| [[KATO III (line)]] | alt | 91.5 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.76× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 4.26× (z +11.8) | — |
| [[LoVo (line)]] | wt | 85.0 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.91× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.44× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 127 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.10× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 3.96× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 84.7 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.61× (z +9.4) | — |
| [[A498 (line)]] | wt | 163 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.25× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.70× (z +10.0) | — |
| [[H4 (line)]] | wt | 113 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.72× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 82.9 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.44× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 4.65× (z +11.4) | — |
| [[hTERT-HPNE (line)]] | wt | 60.4 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.25× (z +11.4) | — |
| [[NCI-H2347 (line)]] | alt | 99.5 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +10.8) | — |
| [[Panc 03.27 (line)]] | alt | 73.0 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.02× (z +10.8) | — |
| [[SW 900 (line)]] | alt | 69.5 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 4.04× (z +10.4) | — |
| [[SW1417 (line)]] | alt | 82.3 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.22× (z +12.2) | — |
| [[A549 (line)]] | wt | 69.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.37× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +10.1) | — |
| [[J82 (line)]] | alt | 72.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.09× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 60.8 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.6× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 5.53× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 51.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.1× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 75.5 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.99× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.18× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 59.6 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.07× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 82.2 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.04× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 3.57× (z +9.1) | — |
| [[SW480 (line)]] | alt | 99.9 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.45× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 55.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 3.84× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 47.6 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.22× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 70.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 3.59× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 76.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.56× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[AN3 CA (line)]] | alt | 108 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.17× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Harringtonine (drug)]] 5 µM 0.221× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.56× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[Hs 766T (line)]] | wt | 62.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 130 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 99.3 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 3.76× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 65.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.69× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SNU-1 (line)]] | wt | 90.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[C-33 A (line)]] | alt | 86.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H23 (line)]] | alt | 31.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.54× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[RKO (line)]] | wt | 83.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.35× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW48 (line)]] | wt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[BT-474 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 91.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6600), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPB1]] | +0.78 | +0.76 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS; STRING 666 |
| [[PSMB4]] | +0.75 | +0.76 / +0.66 | both halves | 7e-06 | pathway: Cellular response to chemical stress; STRING 726 |
| [[UBB]] | +0.74 | +0.75 / +0.75 | both halves | 7e-06 | pathway: Cellular response to chemical stress |
| [[HSPA1B]] | +0.74 | +0.69 / +0.77 | both halves | 7e-06 | STRING 453 |
| [[HSP90AA2P]] | +0.74 | +0.82 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[MRPL18]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[CACYBP]] | +0.70 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[HSPE1]] | +0.68 | +0.69 / +0.63 | both halves | 7e-06 | STRING 688 |
| [[HSPA1A]] | +0.68 | +0.62 / +0.73 | both halves | 7e-06 | STRING 440 |
| [[HSP90AA1]] | +0.67 | +0.69 / +0.76 | both halves | 7e-06 | STRING 779 |
| [[PSMA1]] | +0.67 | +0.72 / +0.58 | both halves | 8e-06 | pathway: Cellular response to chemical stress; STRING 754 |
| [[HSP90AB3P]] | +0.66 | +0.73 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENTR1]] | -0.56 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[CTU2]] | -0.53 | -0.45 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.816). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-18.2, -10.7); signed map (-25.0, -27.7). **Vector** length 83.6, 34.8% of its response variance represented; |z| ≥ 3 in 840 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *heat shock* (control, mean cos +0.61 to 13); *Attenuation phase* (reactome, mean cos +0.61 to 13); *HSF1-dependent transactivation* (reactome, mean cos +0.61 to 14).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +10.8 | +11.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +10.7 | +11.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.2 | +11.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.3 | +5.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.0 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +8.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | -0.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.9 | -0.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.3 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -3.2 | +14.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -3.1 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.0 | +9.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -0.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.2 | +0.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | +0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | +1.0 |
|  | [[EX229 (drug)]] 0.5 µM |  | -1.9 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | superoxide dismutase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:31,659,666-31,668,931 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IPOA; previously ALS, ALS1 |
| Gene groups (HGNC) | Superoxide dismutases |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, BILE_ACID_METABOLISM, PEROXISOME, PROTEIN_SECRETION, APOPTOSIS, GLYCOLYSIS, ADIPOGENESIS |
| Reactome | 13 pathways, smallest: Detoxification of Reactive Oxygen Species; Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation; Interleukin-12 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P00441](https://www.uniprot.org/uniprotkb/P00441) (Superoxide dismutase):

> Destroys radicals which are normally produced within the cells and which are toxic to biological systems. Catalyzes the oxidation of hydrogen sulfide (H2S) to sulfate, playing an important role in detoxifying H2S and limiting the accumulation of reactive sulfur species (RSS) such as persulfides and polysulfides.

**Summary**, from NCBI Gene [6647](https://www.ncbi.nlm.nih.gov/gene/6647):

> The protein encoded by this gene binds copper and zinc ions and is one of two isozymes responsible for destroying free superoxide radicals in the body. The encoded isozyme is a soluble cytoplasmic protein, acting as a homodimer to convert naturally-occuring but harmful superoxide radicals to molecular oxygen and hydrogen peroxide. The other isozyme is a mitochondrial protein. In addition, this protein contains an antimicrobial peptide that displays antibacterial, antifungal, and anti-MRSA …

**Accessions** — [HGNC:11179](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11179) · Entrez [6647](https://www.ncbi.nlm.nih.gov/gene/6647) · UniProt [P00441](https://www.uniprot.org/uniprotkb/P00441) · Ensembl [ENSG00000142168](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142168)

## Data

Gene col 6600: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6600); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6600, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6600]; `tensor/DDL_lfc|DDL_z.npy` [6600]; `embed/gene_vectors.npy` [6600]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6600 or target_col == 6600). Every well: [[SOD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
