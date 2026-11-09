---
symbol: "FKBP5"
type: "gene"
col: 1759
ensembl_id: "ENSG00000096060"
name: "FKBP prolyl isomerase 5"
location: "6p21.31"
module: 98
arm: "+"
pooled_cpm: 31.68
n_lines_expressing: 44
n_dd_up: 64
n_dd_down: 4
n_dd_up_clean: 40
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# FKBP5

*FKBP prolyl isomerase 5* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 64 drug-doses (24 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 13.9× (z +39.7, q 0e+00, up in 39 of 41 measured lines) ⚠ position correction uncertain. The strongest without an alert is [[Budesonide (drug)]] 0.5 µM: 11.8× (z +37.2, q 0e+00, up in 35 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.492× (z -5.6, q 1e-05, down in 23 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[PH-797804 (drug)]] 5 µM in 1 line (RKO 0.0423×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.201×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 900 0.152×); [[TAK-901 (drug)]] 5 µM in 1 line (RKO 0.0982×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAOA]] (+0.73, fdr 7e-06), [[CCND3]] (+0.73, fdr 7e-06), [[TLR2]] (+0.70, fdr 7e-06); moves opposite to [[TCP10L]] (-0.53, fdr 2e-05), [[ADAMTS16]] (-0.50, fdr 3e-05), [[CRLF2]] (-0.49, fdr 2e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 71 in all, 25 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 64 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1759.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM | ⚠ position correction uncertain | **13.9×** | +39.7 | 0e+00 | 39/41 (A498, NCI-H2347, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM | ⚠ position correction uncertain | **13.3×** | +39.1 | 0e+00 | 39/41 (A498, SNU-423, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM | ⚠ position correction uncertain | **12.3×** | +37.8 | 0e+00 | 33/41 (A498, SNU-423, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **11.8×** | +37.2 | 0e+00 | 35/41 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **11.5×** | +36.9 | 0e+00 | 32/41 (A498, SNU-423, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **10.9×** | +36.1 | 0e+00 | 32/42 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **10.5×** | +35.5 | 0e+00 | 33/41 (A498, SNU-423, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **9.99×** | +34.7 | 0e+00 | 33/41 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **9.98×** | +34.7 | 0e+00 | 29/41 (A498, SNU-423, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **9.92×** | +34.6 | 0e+00 | 30/41 (A498, SNU-423, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **9.65×** | +32.9 | 0e+00 | 33/41 (A498, SNU-423, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **10.4×** | +32.6 | 0e+00 | 33/41 (A498, SNU-423, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **4.93×** | +32.1 | 0e+00 | 30/42 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **7.94×** | +31.3 | 0e+00 | 29/41 (A498, NCI-H2347, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **7.77×** | +30.9 | 0e+00 | 30/41 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[Econazole (drug)]] 5 µM |  | **6.40×** | +28.0 | 0e+00 | 29/41 (A498, Hs 766T, …) | top dose only |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **6.28×** | +27.7 | 0e+00 | 35/42 (A498, SNU-423, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **5.02×** | +24.3 | 0e+00 | 30/42 (A498, SNU-423, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1759.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[PH-797804 (drug)]] 5 µM in 1 line (RKO 0.0423×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.201×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 900 0.152×); [[TAK-901 (drug)]] 5 µM in 1 line (RKO 0.0982×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.492×** | -5.6 | 1e-05 | 23/42 (RKO, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.561×** | -4.6 | 0.001 | 21/41 (RKO, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.792×** | -4.5 | 0.002 | 16/42 (HCT15, SNU-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.579×** | -4.3 | 0.002 | 16/39 (RKO, SW480, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.748× | -3.2 | 0.17 | 12/42 (NCI-H23, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.759× | -3.0 | 0.24 | 14/42 (AN3 CA, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.01 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1759. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 45.3 | 30 (7 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 16.7× (z +23.4) ⚠ position correction uncertain · without an alert: [[Phenylephrine (hydrochloride) (drug)]] 5 µM 13.9× (z +21.9) | — |
| [[NCI-H460 (line)]] | wt | 18.6 | 30 (10 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 23.2× (z +20.2) ⚠ position correction uncertain · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 14.2× (z +17.1) | — |
| [[A498 (line)]] | wt | 48.5 | 29 (7 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 28.8× (z +29.0) ⚠ position correction uncertain · without an alert: [[Budesonide (drug)]] 5 µM 22.5× (z +26.9) | — |
| [[NCI-H1573 (line)]] | alt | 13.2 | 29 (6 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 79.3× (z +15.7) ⚠ position correction uncertain · without an alert: [[Citalopram (hydrobromide) (drug)]] 0.05 µM 69.2× (z +15.2) | — |
| [[SNU-423 (line)]] | alt | 40.8 | 29 (9 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 46.1× (z +22.6) ⚠ position correction uncertain · without an alert: [[Budesonide (drug)]] 5 µM 43.6× (z +22.3) | — |
| [[HOP62 (line)]] | alt | 21.2 | 28 (8 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 127× (z +21.2) ⚠ position correction uncertain · without an alert: [[Budesonide (drug)]] 5 µM 96.8× (z +20.1) | — |
| [[SW 900 (line)]] | alt | 37.6 | 26 (6 ⚠) | 1 | [[Clobetasol propionate (drug)]] 0.5 µM 37.3× (z +20.9) ⚠ position correction uncertain · without an alert: [[Budesonide (drug)]] 0.5 µM 36.1× (z +20.7) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.152× (z -11.0) |
| [[Hs 766T (line)]] | wt | 77.8 | 25 (4 ⚠) | 1 (1 ⚠) | [[Budesonide (drug)]] 5 µM 34.0× (z +21.7) | [[Bortezomib (drug)]] 5 µM 0.0567× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 43.4 | 26 (5 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 39.8× (z +21.4) ⚠ position correction uncertain · without an alert: [[Dexamethasone (drug)]] 0.5 µM 33.5× (z +20.4) | — |
| [[Panc 03.27 (line)]] | alt | 37.3 | 26 (6 ⚠) | 0 | [[Triamcinolone (drug)]] 5 µM 10.6× (z +18.5) | — |
| [[PANC-1 (line)]] | alt | 51.1 | 26 (9 ⚠) | 0 | [[Budesonide (drug)]] 0.5 µM 8.54× (z +22.5) | — |
| [[AsPC-1 (line)]] | alt | 38.7 | 25 (5 ⚠) | 0 | [[Triamcinolone (drug)]] 5 µM 13.8× (z +20.5) | — |
| [[A-172 (line)]] | wt | 29.4 | 23 (7 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 22.8× (z +21.2) ⚠ position correction uncertain · without an alert: [[Budesonide (drug)]] 0.5 µM 19.0× (z +19.9) | — |
| [[A549 (line)]] | wt | 22.3 | 23 (4 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 27.5× (z +19.3) ⚠ position correction uncertain · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 20.8× (z +17.7) | — |
| [[CFPAC-1 (line)]] | alt | 22.8 | 23 (6 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 35.9× (z +20.1) ⚠ position correction uncertain · without an alert: [[Budesonide (drug)]] 5 µM 25.6× (z +18.2) | — |
| [[hTERT-HPNE (line)]] | wt | 15.5 | 22 (5 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 49.6× (z +14.3) ⚠ position correction uncertain · without an alert: [[Budesonide (drug)]] 5 µM 39.1× (z +13.4) | — |
| [[J82 (line)]] | alt | 18.3 | 22 (6 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 12.3× (z +15.4) ⚠ position correction uncertain · without an alert: [[Dexamethasone (drug)]] 0.5 µM 10.6× (z +14.4) | — |
| [[SK-MEL-2 (line)]] | alt | 33.5 | 22 (7 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 10.1× (z +13.3) ⚠ position correction uncertain · without an alert: [[Budesonide (drug)]] 0.5 µM 9.84× (z +13.1) | — |
| [[LOX-IMVI (line)]] | wt | 23.7 | 21 (6 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 35.3× (z +20.6) ⚠ position correction uncertain · without an alert: [[Budesonide (drug)]] 0.5 µM 28.1× (z +19.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.7 | 21 (6 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 12.5× (z +15.6) ⚠ position correction uncertain · without an alert: [[Budesonide (drug)]] 0.5 µM 12.4× (z +15.6) | — |
| [[HS-578T (line)]] | alt | 10.1 | 20 (3 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 55.3× (z +15.0) ⚠ position correction uncertain · without an alert: [[Triamcinolone (drug)]] 5 µM 17.0× (z +13.9) | — |
| [[C32 (line)]] | wt | 24.9 | 18 (3 ⚠) | 0 | [[Budesonide (drug)]] 0.5 µM 19.9× (z +15.6) | — |
| [[H4 (line)]] | wt | 14.3 | 18 (3 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 46.6× (z +11.4) ⚠ position correction uncertain · without an alert: [[Triamcinolone (drug)]] 5 µM 17.4× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 58.7 | 18 (7 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 7.72× (z +13.7) ⚠ position correction uncertain · without an alert: [[Budesonide (drug)]] 0.5 µM 7.13× (z +13.1) | — |
| [[SW480 (line)]] | alt | 65.5 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.1) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 3.33× (z +12.5) | — |
| [[LoVo (line)]] | wt | 27.0 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +13.5) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 3.33× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 36.3 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +16.2) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 3.73× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 20.5 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.43× (z +15.1) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 5.26× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 19.8 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.30× (z +9.7) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[RKO (line)]] | wt | 76.4 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | [[PH-797804 (drug)]] 5 µM 0.0423× (z -13.8) |
| [[A-427 (line)]] | wt | 47.4 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.35× (z +9.8) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[LS 180 (line)]] | wt | 16.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +8.9) ⚠ position correction uncertain | — |
| [[AN3 CA (line)]] | alt | 237 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[CHP-212 (line)]] | wt | 27.7 | 1 (1 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 16.0× (z +9.0) ⚠ position correction uncertain | — |
| [[COLO 205 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.49× (z +13.9) ⚠ position correction uncertain | — |
| [[BT-474 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1759), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAOA]] | +0.73 | +0.70 / +0.75 | both halves | 7e-06 | STRING 542 |
| [[CCND3]] | +0.73 | +0.75 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[TLR2]] | +0.70 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[ACSL1]] | +0.67 | +0.70 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[ADGRG2]] | +0.67 | +0.64 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[KLF9]] | +0.66 | +0.72 / +0.60 | both halves | 7e-06 | STRING 642 |
| [[STOM]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[VSTM2L]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[FGD4]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[IRAK3]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 | same gene group |
| [[SLC26A2]] | +0.63 | +0.63 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[MT1M]] | +0.63 | +0.69 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCP10L]] | -0.53 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ADAMTS16]] | -0.50 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[CRLF2]] | -0.49 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[FAM107B]] | -0.48 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[SIRLNT]] | -0.48 | -0.47 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FKBP5's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 10.4% of all compounds | 0.024 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[FAM107B]] | C | FAM107B activity weakens FKBP5's drug response | lines that do not express FAM107B (9) vs lines expressing it (33) | the lines without FAM107B respond 0.82× as strongly (z diff -3.03); strongest at Clobetasol propionate 0.5 µM: 5.50x vs 12x (z diff -3.7) | 0.014 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1; target measured in part of the lines; rests on the correction |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.829). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.4, 15.6); signed map (17.2, 30.8). **Vector** length 128, 42.6% of its response variance represented; |z| ≥ 3 in 2,009 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 0.05 µM | ⚠ position correction uncertain | +9.6 | +39.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM | ⚠ position correction uncertain | +9.2 | +39.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +9.2 | +36.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +8.6 | +32.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +8.5 | +34.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.4 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -4.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.4 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.1 | +12.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -2.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | FKBP prolyl isomerase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:35,573,585-35,728,583 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FKBP51, FKBP54, PPIase, P54, Ptg-10 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; FKBP prolyl isomerase family; MicroRNA protein coding host genes |
| Hallmark sets | ANDROGEN_RESPONSE, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 10 pathways, smallest: MECP2 regulates neuronal receptors and channels; Modulation of host responses by IFN-stimulated genes; HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13451](https://www.uniprot.org/uniprotkb/Q13451) (Peptidyl-prolyl cis-trans isomerase FKBP5):

> Immunophilin protein with PPIase and co-chaperone activities. Component of unligated steroid receptors heterocomplexes through interaction with heat-shock protein 90 (HSP90). Plays a role in the intracellular trafficking of heterooligomeric forms of steroid hormone receptors maintaining the complex into the cytoplasm when unliganded. Acts as a regulator of Akt/AKT1 activity by promoting the interaction between Akt/AKT1 and PHLPP1, thereby enhancing dephosphorylation and subsequent activation of …

**Summary**, from NCBI Gene [2289](https://www.ncbi.nlm.nih.gov/gene/2289):

> The protein encoded by this gene is a member of the immunophilin protein family, which play a role in immunoregulation and basic cellular processes involving protein folding and trafficking. This encoded protein is a cis-trans prolyl isomerase that binds to the immunosuppressants FK506 and rapamycin. It is thought to mediate calcineurin inhibition. It also interacts functionally with mature hetero-oligomeric progesterone receptor complexes along with the 90 kDa heat shock protein and P23 …

**Accessions** — [HGNC:3721](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3721) · Entrez [2289](https://www.ncbi.nlm.nih.gov/gene/2289) · UniProt [Q13451](https://www.uniprot.org/uniprotkb/Q13451) · Ensembl [ENSG00000096060](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000096060)

## Data

Gene col 1759: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1759); `tables/drug_effects.parquet` (77 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1759, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1759]; `tensor/DDL_lfc|DDL_z.npy` [1759]; `embed/gene_vectors.npy` [1759]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1759 or target_col == 1759). Every well: [[FKBP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FKBP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
