---
symbol: "ECE1"
type: "gene"
col: 3892
ensembl_id: "ENSG00000117298"
name: "endothelin converting enzyme 1"
location: "1p36.12"
module: 78
arm: "+"
pooled_cpm: 142.92
n_lines_expressing: 47
n_dd_up: 7
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 8
direction_downstream: 3
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# ECE1

*endothelin converting enzyme 1* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.03× (z +15.5, q 0e+00, up in 36 of 45 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 6 lines (HEC-1-A 3.04×, LoVo 3.16×, SW1417 3.69×, SW480 2.81×, …; ⚠ cell-cycle shift, explains ~27% of this change); [[Panobinostat (drug)]] 0.5 µM in 4 lines (HEC-1-A 2.59×, RKO 3.71×, KATO III 2.85×, SW1417 3.08×; ⚠ cell-cycle shift, explains ~32% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 3.15×, AsPC-1 2.31×; ⚠ cell-cycle shift, explains ~0% of this change); [[Trametinib (drug)]] 0.5 µM in 1 line (HepG2/C3A 1.89×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (HepG2/C3A 2.17×); [[Cobimetinib (drug)]] 5 µM in 1 line (HepG2/C3A 2.17×).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.586× (z -11.7, q 1e-28, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD82]] (+0.70, fdr 7e-06), [[WWTR1]] (+0.63, fdr 7e-06), [[HIVEP3]] (+0.62, fdr 1e-05); moves opposite to [[TYW3]] (-0.56, fdr 3e-05), [[MTRF1]] (-0.56, fdr 3e-05), [[COA6]] (-0.55, fdr 5e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TGM2]] → it (grade B ⚠); 3 go from it, the strongest it → [[RIN2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3892.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 6 lines (HEC-1-A 3.04×, LoVo 3.16×, SW1417 3.69×, SW480 2.81×, …; ⚠ cell-cycle shift, explains ~27% of this change); [[Panobinostat (drug)]] 0.5 µM in 4 lines (HEC-1-A 2.59×, RKO 3.71×, KATO III 2.85×, SW1417 3.08×; ⚠ cell-cycle shift, explains ~32% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 3.15×, AsPC-1 2.31×; ⚠ cell-cycle shift, explains ~0% of this change); [[Trametinib (drug)]] 0.5 µM in 1 line (HepG2/C3A 1.89×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (HepG2/C3A 2.17×); [[Cobimetinib (drug)]] 5 µM in 1 line (HepG2/C3A 2.17×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.03×** | +15.5 | 0e+00 | 36/45 (HEC-1-A, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.78×** | +12.6 | 5e-34 | 33/45 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.67×** | +11.2 | 5e-27 | 34/45 (HEC-1-A, RKO, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.40×** | +7.4 | 2e-11 | 25/46 (A-427, NCI-H23, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +6.5 | 8e-09 | 26/45 (NCI-H23, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.25×** | +4.6 | 3e-04 | 19/41 (A-172, A-427, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **1.24×** | +4.3 | 0.001 | 18/42 (HEC-1-A, C-33 A, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +4.1 | 0.003 | 12/45 (SW480, HEC-1-A, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~70% of this change | 1.16× | +3.2 | 0.084 | 18/44 (NCI-H460, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.15× | +3.0 | 0.14 | 15/45 (LoVo, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3892.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.586×** | -11.7 | 1e-28 | 34/45 (J82, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.759×** | -8.5 | 4e-15 | 27/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.735×** | -6.7 | 3e-09 | 29/45 (HS-578T, MIA PaCa-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.733×** | -6.4 | 2e-08 | 32/45 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.749×** | -6.3 | 3e-08 | 25/45 (HepG2/C3A, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.746×** | -6.2 | 7e-08 | 30/44 (HS-578T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.760×** | -6.0 | 2e-07 | 28/45 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.763×** | -5.9 | 3e-07 | 23/45 (SK-MEL-2, SW 900, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.764×** | -5.9 | 3e-07 | 27/45 (MIA PaCa-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.834× | -5.6 | 1e-06 | 23/46 (HepG2/C3A, SW 900, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.783×** | -5.3 | 5e-06 | 25/45 (HepG2/C3A, HS-578T, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -5.3 | 6e-06 | 4/47 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.854× | -4.9 | 4e-05 | 23/45 (NCI-H2030, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.807×** | -4.7 | 1e-04 | 23/45 (MIA PaCa-2, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.834× | -4.5 | 2e-04 | 21/45 (A498, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.822×** | -4.3 | 6e-04 | 22/45 (MIA PaCa-2, SW 900, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.828×** | -4.1 | 0.001 | 19/45 (NCI-H1792, SW 900, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.819×** | -4.0 | 0.002 | 22/44 (MIA PaCa-2, C-33 A, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.887× | -3.6 | 0.008 | 12/45 (SK-MEL-2, NCI-H1792, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.890× | -3.6 | 0.008 | 15/45 (HS-578T, A498, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.849× | -3.4 | 0.014 | 17/46 (SW 1088, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3892. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 239 | 3 | 6 (4 ⚠) | [[Trametinib (drug)]] 0.5 µM 1.89× (z +8.9) | [[Ixazomib citrate (drug)]] 5 µM 0.360× (z -11.7) |
| [[LoVo (line)]] | wt | 54.6 | 8 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +19.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HS-578T (line)]] | alt | 601 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.334× (z -13.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.439× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 338 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.404× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 98.4 | 3 (3 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.50× (z +11.5) ⚠ cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.389× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 91.3 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.429× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 348 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.364× (z -11.0) |
| [[SK-MEL-2 (line)]] | alt | 77.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.339× (z -9.2) |
| [[A-427 (line)]] | wt | 53.6 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.01× (z +12.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HEC-1-A (line)]] | alt | 89.0 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.04× (z +16.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[RKO (line)]] | wt | 59.9 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.83× (z +12.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[C-33 A (line)]] | alt | 73.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +9.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[Hs 766T (line)]] | wt | 320 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.472× (z -9.2) |
| [[KATO III (line)]] | alt | 97.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.85× (z +12.0) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[PANC-1 (line)]] | alt | 173 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.454× (z -10.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.490× (z -9.4) |
| [[SW1417 (line)]] | alt | 55.2 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.69× (z +13.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW480 (line)]] | alt | 80.2 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +13.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 148 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.522× (z -10.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.453× (z -9.4) |
| [[A498 (line)]] | wt | 187 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.366× (z -10.8) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.422× (z -9.8) |
| [[J82 (line)]] | alt | 182 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.302× (z -14.9) |
| [[NCI-H2347 (line)]] | alt | 162 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.471× (z -13.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H460 (line)]] | wt | 64.0 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 56.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.35× (z +10.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 64.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 119 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 224 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.518× (z -11.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[COLO 205 (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 55.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.28× (z +9.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HT-29 (line)]] | alt | 136 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.417× (z -9.1) |
| [[LS 180 (line)]] | wt | 94.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.21× (z +9.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 356 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.364× (z -10.6) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 112 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.12× (z +9.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW 900 (line)]] | alt | 160 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.286× (z -10.0) ⚠ cell-cycle shift, explains ~24% of this change |
| [[AN3 CA (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 229 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 237 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.9 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.3 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 559 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3892), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD82]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[WWTR1]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[HIVEP3]] | +0.62 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[RIPK4]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[RAC2]] | +0.61 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[ITGA3]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[PODXL]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[TBC1D10A]] | +0.61 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[SFRP1]] | +0.60 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[SMOX]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[ZCCHC24]] | +0.60 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[SH2B3]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYW3]] | -0.56 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[MTRF1]] | -0.56 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[COA6]] | -0.55 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[RRAGB]] | -0.55 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ZNF234]] | -0.54 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[RWDD3]] | -0.54 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[POLR3C]] | -0.53 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ZNF790]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[TMLHE]] | -0.52 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[YARS2]] | -0.52 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[FAIM]] | -0.52 | -0.51 / -0.27 | both halves | 3e-04 |  |
| [[ARMCX5-GPRASP2]] | -0.51 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGM2]] | B | TGM2 activity raises ECE1's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 1.92× lower at baseline in the lines without TGM2 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[HDAC6]] | B | HDAC6 activity lowers ECE1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RAC2]] | B | RAC2 activity raises ECE1's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 1.99× lower at baseline in the lines without RAC2 | 0.048 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[CCDC33]] | B | CCDC33 activity raises ECE1's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 1.58× lower at baseline in the lines without CCDC33 | 0.050 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8 |
| [[SMAD3]] | B | SMAD3 activity raises ECE1's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without SMAD3 | 0.063 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[CD82]] | B | CD82 activity raises ECE1's level | lines that do not express CD82 (11) vs lines expressing it (39) | 2.10× lower at baseline in the lines without CD82 | 0.068 | ⚠ within organs, on part of the lines; also absent: ITGA3, GBP3, CXCL3; maybe low, not absent |
| [[MMP14]] | B | MMP14 activity raises ECE1's level | lines that do not express MMP14 (19) vs lines expressing it (31) | 1.64× lower at baseline in the lines without MMP14 | 0.090 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A |
| [[SLC6A6]] | C | SLC6A6 activity raises ECE1's level | lines that do not express SLC6A6 (4) vs lines expressing it (46) | 1.37× lower at baseline in the lines without SLC6A6 | 0.092 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000288891; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIN2]] | C | ECE1 activity strengthens RIN2's drug response | lines that do not express ECE1 (3) vs lines expressing it (36) | the lines without ECE1 respond 0.62× as strongly (z diff +3.10); strongest at Homoharringtonine 0.5 µM: 0.61x vs 0.28x (z diff +5.2) | 0.027 | ⚠ few lines (3 vs 47); across organs; also absent: KIAA1522, ENSG00000257489, SLC9A3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CARD10]] | C | ECE1 activity raises CARD10's level | lines that do not express ECE1 (3) vs lines expressing it (47) | 3.60× lower at baseline in the lines without ECE1 | 0.041 | ⚠ few lines (3 vs 47); across organs; also absent: KIAA1522, ENSG00000257489, SLC9A3; maybe low, not absent |
| [[HPCAL1]] | C | ECE1 activity raises HPCAL1's level | lines that do not express ECE1 (3) vs lines expressing it (47) | 3.27× lower at baseline in the lines without ECE1 | 0.089 | ⚠ few lines (3 vs 47); across organs; also absent: KIAA1522, ENSG00000257489, SLC9A3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.4, 5.6); signed map (5.0, 49.6). **Vector** length 137, 41.0% of its response variance represented; |z| ≥ 3 in 1,461 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +8.5 | +15.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +8.2 | +12.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +8.1 | +11.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | +5.9 | +6.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.0 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.0 | +2.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -10.3 | -8.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.4 | -6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.2 | -6.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | -6.1 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -11.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | -5.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.2 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | endothelin converting enzyme 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:21,217,247-21,345,572 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ECE |
| Gene groups (HGNC) | M13 metallopeptidases |
| Reactome | 4 pathways, smallest: Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); GPCR ligand binding |
| Matched by | ensembl_id |

**Function**, from UniProt [P42892](https://www.uniprot.org/uniprotkb/P42892) (Endothelin-converting enzyme 1):

> Converts big endothelin-1 to endothelin-1.

**Summary**, from NCBI Gene [1889](https://www.ncbi.nlm.nih.gov/gene/1889):

> The protein encoded by this gene is involved in proteolytic processing of endothelin precursors to biologically active peptides. Mutations in this gene are associated with Hirschsprung disease, cardiac defects and autonomic dysfunction. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene.[provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:3146](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3146) · Entrez [1889](https://www.ncbi.nlm.nih.gov/gene/1889) · UniProt [P42892](https://www.uniprot.org/uniprotkb/P42892) · Ensembl [ENSG00000117298](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117298)

## Data

Gene col 3892: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3892); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3892, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3892]; `tensor/DDL_lfc|DDL_z.npy` [3892]; `embed/gene_vectors.npy` [3892]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3892 or target_col == 3892). Every well: [[ECE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ECE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
