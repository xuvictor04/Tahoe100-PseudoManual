---
symbol: "SYNJ2"
type: "gene"
col: 1216
ensembl_id: "ENSG00000078269"
name: "synaptojanin 2"
location: "6q25.3"
module: 112
arm: "+"
pooled_cpm: 141.49
n_lines_expressing: 46
n_dd_up: 0
n_dd_down: 57
n_dd_up_clean: 0
n_dd_down_clean: 46
in_vector_space: true
direction_upstream: 49
direction_downstream: 28
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# SYNJ2

*synaptojanin 2* — 6q25.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-172 3.47×, SK-MEL-2 3.40×, COLO 205 2.35×, HS-578T 2.13×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 5 lines (A-172 3.58×, COLO 205 3.14×, HS-578T 2.55×, SK-MEL-2 3.33×, …; ⚠ cell-cycle shift, explains ~30% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (HEC-1-A 1.74×); [[TAK-901 (drug)]] 0.05 µM in 1 line (C32 2.51×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H1573 2.89×).
> Pooled over the cell lines (median), lowered significantly by 57 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.598× (z -15.9, q 0e+00, down in 33 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD44]] (+0.70, fdr 7e-06), [[ARL4C]] (+0.69, fdr 7e-06), [[SHB]] (+0.69, fdr 7e-06); moves opposite to [[CHPT1]] (-0.61, fdr 1e-05), [[ADGRG2]] (-0.56, fdr 1e-05), [[CLASP1]] (-0.54, fdr 1e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 49 arrows point to it, the strongest [[COL7A1]] → it (grade B ⚠); 28 go from it, the strongest it → [[ITGA2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1216.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-172 3.47×, SK-MEL-2 3.40×, COLO 205 2.35×, HS-578T 2.13×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 5 lines (A-172 3.58×, COLO 205 3.14×, HS-578T 2.55×, SK-MEL-2 3.33×, …; ⚠ cell-cycle shift, explains ~30% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (HEC-1-A 1.74×); [[TAK-901 (drug)]] 0.05 µM in 1 line (C32 2.51×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H1573 2.89×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.9 | 6e-04 | 20/44 (HEC-1-A, BT-474, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.13× | +3.8 | 0.036 | 11/45 (SNU-423, HS-578T, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.17× | +3.5 | 0.074 | 17/44 (NCI-H1792, J82, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.090 | 14/44 (KATO III, C32, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.090 | 13/44 (SW1417, NCI-H1792, …) | inconsistent across doses |  |
| [[DTP3 (drug)]] 5 µM |  | 1.31× | +3.1 | 0.17 | 7/44 (COLO 205, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.17 | 16/43 (SW48, H4, …) | two highest doses | low cells (technical?) |
| [[Naproxen (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.17 | 2/44 (C-33 A, LOX-IMVI) | two highest doses | position effect removed |
| [[Omeprazole (drug)]] 5 µM |  | 1.14× | +3.0 | 0.17 | 6/44 (HEC-1-A, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 77 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 57 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1216.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.598×** | -15.9 | 0e+00 | 33/45 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.609×** | -10.9 | 4e-25 | 31/44 (SNU-423, HOP62, …) | two highest doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.633×** | -10.0 | 2e-21 | 31/44 (SNU-423, HOP62, …) | two highest doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.627×** | -9.9 | 1e-20 | 28/40 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.652×** | -9.4 | 7e-19 | 28/44 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.663×** | -9.0 | 2e-17 | 30/44 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.656×** | -8.9 | 5e-17 | 26/43 (Hs 766T, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.647×** | -8.8 | 7e-17 | 29/40 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.469×** | -8.7 | 2e-16 | 34/45 (KATO III, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.679×** | -8.5 | 1e-15 | 24/44 (Hs 766T, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.680×** | -8.5 | 1e-15 | 30/44 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.681×** | -8.4 | 2e-15 | 26/44 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.683×** | -8.4 | 3e-15 | 30/45 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.693×** | -8.0 | 4e-14 | 27/44 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.705×** | -7.7 | 6e-13 | 27/44 (SNU-423, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.690×** | -7.5 | 2e-12 | 27/43 (Hs 766T, HS-578T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.710×** | -7.2 | 2e-11 | 28/44 (A-172, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.721×** | -7.2 | 3e-11 | 26/44 (Hs 766T, hTERT-HPNE, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.724×** | -7.1 | 4e-11 | 26/44 (Hs 766T, SNU-423, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.796×** | -7.0 | 5e-11 | 25/44 (Hs 766T, A549, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1216. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 270 | 1 (1 ⚠) | 26 (5 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 1.95× (z +8.5) ⚠ cell-cycle shift, explains ~6% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -16.8) |
| [[hTERT-HPNE (line)]] | wt | 240 | 0 | 23 (2 ⚠) | — | [[Budesonide (drug)]] 5 µM 0.216× (z -14.4) |
| [[SNU-423 (line)]] | alt | 423 | 0 | 23 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -19.4) |
| [[A549 (line)]] | wt | 135 | 0 | 21 (1 ⚠) | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.313× (z -13.1) |
| [[Hs 766T (line)]] | wt | 292 | 0 | 21 (3 ⚠) | — | [[Budesonide (drug)]] 5 µM 0.279× (z -16.5) |
| [[HS-578T (line)]] | alt | 254 | 2 (2 ⚠) | 17 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +12.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -20.3) |
| [[SW 900 (line)]] | alt | 302 | 0 | 15 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -17.1) |
| [[H4 (line)]] | wt | 131 | 1 (1 ⚠) | 13 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.83× (z +9.0) ⚠ cell-cycle shift, explains ~6% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.263× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 287 | 0 | 14 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -18.0) |
| [[PANC-1 (line)]] | alt | 257 | 0 | 13 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -20.6) |
| [[SW480 (line)]] | alt | 190 | 0 | 12 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 81.2 | 1 | 10 | [[Ixazomib citrate (drug)]] 5 µM 2.89× (z +8.8) | [[Budesonide (drug)]] 0.5 µM 0.271× (z -10.8) |
| [[A-172 (line)]] | wt | 135 | 2 (2 ⚠) | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +19.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Trametinib (drug)]] 5 µM 0.294× (z -15.6) |
| [[C32 (line)]] | wt | 184 | 1 | 8 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.51× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.466× (z -11.0) |
| [[SW1417 (line)]] | alt | 171 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -21.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -13.6) |
| [[KATO III (line)]] | alt | 165 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.309× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -11.8) |
| [[LoVo (line)]] | wt | 138 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.456× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 64.5 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +9.2) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.331× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 75.5 | 3 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +14.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.88× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.192× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -9.7) |
| [[COLO 205 (line)]] | alt | 143 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.480× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 128 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.475× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 239 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -17.3) |
| [[HEC-1-A (line)]] | alt | 96.1 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.74× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 229 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.405× (z -8.5) |
| [[HT-29 (line)]] | alt | 136 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -13.8) |
| [[J82 (line)]] | alt | 167 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.619× (z -8.8) |
| [[SW 1271 (line)]] | alt | 188 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0827× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -9.8) |
| [[A-427 (line)]] | wt | 48.0 | 1 (1 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +8.6) ⚠ cell-cycle shift, explains ~9% of this change | — |
| [[A498 (line)]] | wt | 77.5 | 0 | 1 | — | [[Triamcinolone (drug)]] 5 µM 0.571× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 124 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -8.9) |
| [[LS 180 (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.461× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 75.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.288× (z -10.3) |
| [[SW 1088 (line)]] | alt | 274 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -8.5) |
| [[SW48 (line)]] | wt | 118 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 29.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.2 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1216), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD44]] | +0.70 | +0.68 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ARL4C]] | +0.69 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[SHB]] | +0.69 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[WNT7B]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[EHD1]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[ADAM19]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[LIF]] | +0.65 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[LINC00973]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[FZD8]] | +0.64 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[IQCJ-SCHIP1]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[AFF3]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[HBEGF]] | +0.63 | +0.65 / +0.63 | both halves | 7e-06 | pathway: Clathrin-mediated endocytosis |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHPT1]] | -0.61 | -0.56 / -0.61 | both halves | 1e-05 | pathway: Phospholipid metabolism |
| [[ADGRG2]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[CLASP1]] | -0.54 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[COPS8]] | -0.53 | -0.54 / -0.56 | both halves | 1e-05 | pathway: Clathrin-mediated endocytosis |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 47, C 2. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL7A1]] | B | COL7A1 activity raises SYNJ2's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 2.40× lower at baseline in the lines without COL7A1 | 0.001 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[WNT7B]] | B | WNT7B activity raises SYNJ2's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 2.24× lower at baseline in the lines without WNT7B | 0.005 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[ADAM19]] | B | ADAM19 activity raises SYNJ2's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 2.48× lower at baseline in the lines without ADAM19 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[FRMD4A]] | B | FRMD4A activity raises SYNJ2's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.07× lower at baseline in the lines without FRMD4A | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[NLRP1]] | B | NLRP1 activity raises SYNJ2's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 2.10× lower at baseline in the lines without NLRP1 | 0.005 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12 |
| [[COL7A1]] | B | COL7A1 activity strengthens SYNJ2's drug response | lines that do not express COL7A1 (21) vs lines expressing it (24) | the lines without COL7A1 respond 0.46× as strongly (z diff +2.80); strongest at Idarubicin (hydrochloride) 5 µM: 0.80x vs 0.46x (z diff +4.8) | 0.006 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SMAD3]] | B | SMAD3 activity raises SYNJ2's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 3.29× lower at baseline in the lines without SMAD3 | 0.007 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[LINC02813]] | B | LINC02813 activity raises SYNJ2's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 1.73× lower at baseline in the lines without LINC02813 | 0.008 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[PRKCA]] | B | PRKCA activity raises SYNJ2's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 3.11× lower at baseline in the lines without PRKCA | 0.008 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[CD82]] | B | CD82 activity raises SYNJ2's level | lines that do not express CD82 (11) vs lines expressing it (39) | 2.21× lower at baseline in the lines without CD82 | 0.011 | ⚠ within organs, on part of the lines; also absent: ITGA3, GBP3, CXCL3; maybe low, not absent |
| [[GPR39]] | B | GPR39 activity raises SYNJ2's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 2.23× lower at baseline in the lines without GPR39 | 0.016 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[PTHLH]] | B | PTHLH activity raises SYNJ2's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 2.08× lower at baseline in the lines without PTHLH | 0.018 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 0, C 28. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA2]] | C | SYNJ2 activity raises ITGA2's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 6.33× lower at baseline in the lines without SYNJ2 | 0.008 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |
| [[GPR39]] | C | SYNJ2 activity raises GPR39's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 4.61× lower at baseline in the lines without SYNJ2 | 0.008 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |
| [[KLF12]] | C | SYNJ2 activity raises KLF12's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 5.20× lower at baseline in the lines without SYNJ2 | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |
| [[CMKLR2]] | C | SYNJ2 activity lowers CMKLR2's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 2.31× higher at baseline in the lines without SYNJ2 | 0.017 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |
| [[MAST4]] | C | SYNJ2 activity raises MAST4's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 4.97× lower at baseline in the lines without SYNJ2 | 0.018 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |
| [[FRMD5]] | C | SYNJ2 activity raises FRMD5's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 5.53× lower at baseline in the lines without SYNJ2 | 0.025 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |
| [[HRH1]] | C | SYNJ2 activity raises HRH1's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 3.42× lower at baseline in the lines without SYNJ2 | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |
| [[PRDX6]] | C | SYNJ2 activity lowers PRDX6's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 1.45× higher at baseline in the lines without SYNJ2 | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |
| [[ANP32B]] | C | SYNJ2 activity lowers ANP32B's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 1.39× higher at baseline in the lines without SYNJ2 | 0.036 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |
| [[SMAD3]] | C | SYNJ2 activity raises SMAD3's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 2.66× lower at baseline in the lines without SYNJ2 | 0.037 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |
| [[TGFA]] | C | SYNJ2 activity raises TGFA's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 5.36× lower at baseline in the lines without SYNJ2 | 0.047 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |
| [[PRKCA]] | C | SYNJ2 activity raises PRKCA's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 2.38× lower at baseline in the lines without SYNJ2 | 0.050 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.5, 1.0); signed map (3.6, 44.4). **Vector** length 136, 45.1% of its response variance represented; |z| ≥ 3 in 1,876 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *inflammatory response* (hallmark, mean cos +0.53 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +4.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.6 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.1 | +2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | -0.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +3.1 | +3.8 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -7.4 | -7.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -7.3 | -7.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -7.1 | -5.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -6.7 | -6.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -6.6 | -7.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -6.6 | -8.5 |

## What is on record

|  |  |
|---|---|
| Name | synaptojanin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:157,981,863-158,099,176 (+) |
| Ensembl biotype | protein_coding |
| Also known as | INPP5H |
| Gene groups (HGNC) | Phosphoinositide phosphatases |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 7 pathways, smallest: Synthesis of PIPs at the plasma membrane; PI Metabolism; Clathrin-mediated endocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [O15056](https://www.uniprot.org/uniprotkb/O15056) (Polyphosphatidylinositol phosphatase SYNJ2):

> Phosphatase that hydrolyzes phosphate groups from the inositol ring of phosphoinositides and inositol phosphates, in a domain-specific manner. The 5-PPase domain catalyzes removal of the 5-phosphate from substrates such as phosphatidylinositol-4,5-bisphosphate (PtdIns(4,5)P2), phosphatidylinositol-3,4,5-trisphosphate (PtdIns(3,4,5)P3), inositol-1,4,5-trisphosphate (Ins(1,4,5)P3) and inositol-1,3,4,5-tetrakisphosphate (Ins(1,3,4,5)P4). The SAC domain hydrolyzes phosphates at the 3- and …

**Summary**, from NCBI Gene [8871](https://www.ncbi.nlm.nih.gov/gene/8871):

> The gene is a member of the inositol-polyphosphate 5-phosphatase family. The encoded protein interacts with the ras-related C3 botulinum toxin substrate 1, which causes translocation of the encoded protein to the plasma membrane where it inhibits clathrin-mediated endocytosis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:11504](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11504) · Entrez [8871](https://www.ncbi.nlm.nih.gov/gene/8871) · UniProt [O15056](https://www.uniprot.org/uniprotkb/O15056) · Ensembl [ENSG00000078269](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078269)

## Data

Gene col 1216: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1216); `tables/drug_effects.parquet` (86 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1216, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1216]; `tensor/DDL_lfc|DDL_z.npy` [1216]; `embed/gene_vectors.npy` [1216]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1216 or target_col == 1216). Every well: [[SYNJ2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYNJ2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
