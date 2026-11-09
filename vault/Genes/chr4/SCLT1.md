---
symbol: "SCLT1"
type: "gene"
col: 7523
ensembl_id: "ENSG00000151466"
name: "sodium channel and clathrin linker 1"
location: "4q28.2"
module: 22
arm: "+"
pooled_cpm: 132.67
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# SCLT1

*sodium channel and clathrin linker 1* — 4q28.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.95× (z +17.7, q 0e+00, up in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.43× (z +7.2, q 1e-10, up in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (NCI-H2347 3.05×, NCI-H460 2.82×, Panc 03.27 3.01×, hTERT-HPNE 3.53×, …; ⚠ cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 2.67×; ⚠ cell-cycle shift, explains ~38% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H2347 2.52×; ⚠ cell-cycle shift, explains ~44% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW1417 2.43×).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.410× (z -17.8, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASPM]] (+0.84, fdr 7e-06), [[KIF23]] (+0.83, fdr 7e-06), [[NDC80]] (+0.83, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CRYAB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7523.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (NCI-H2347 3.05×, NCI-H460 2.82×, Panc 03.27 3.01×, hTERT-HPNE 3.53×, …; ⚠ cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 2.67×; ⚠ cell-cycle shift, explains ~38% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H2347 2.52×; ⚠ cell-cycle shift, explains ~44% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW1417 2.43×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.95×** | +17.7 | 0e+00 | 42/48 (NCI-H2347, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.66×** | +9.7 | 9e-20 | 33/48 (NCI-H2347, LoVo, …) | top dose only | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +7.2 | 1e-10 | 33/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.36×** | +6.2 | 1e-07 | 31/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.32×** | +5.6 | 3e-06 | 28/48 (SW1417, HT-29, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.26×** | +4.6 | 4e-04 | 25/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.26×** | +4.5 | 5e-04 | 27/47 (KATO III, HOP62, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 1.17× | +4.2 | 0.002 | 15/48 (NCI-H2030, NCI-H2347, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.23×** | +4.1 | 0.003 | 23/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +3.9 | 0.005 | 20/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.029 | 17/48 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.029 | 18/48 (H4, A498, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.13× | +3.3 | 0.041 | 10/48 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.18× | +3.3 | 0.046 | 13/49 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.049 | 13/48 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.068 | 10/48 (A-427, H4, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.069 | 15/49 (A549, LS 180, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.090 | 13/49 (RPMI-7951, A549, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.12× | +2.9 | 0.093 | 8/48 (MIA PaCa-2, SW 900, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.16× | +2.9 | 0.096 | 16/49 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7523.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.410×** | -17.8 | 0e+00 | 46/48 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.457×** | -15.6 | 0e+00 | 45/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.445×** | -15.3 | 0e+00 | 46/48 (NCI-H1573, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.519×** | -13.1 | 6e-37 | 45/48 (NCI-H1573, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.632×** | -12.0 | 4e-31 | 40/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.618×** | -9.6 | 6e-20 | 44/48 (KATO III, NCI-H1573, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.418×** | -9.1 | 6e-18 | 37/45 (HEC-1-A, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.645×** | -8.8 | 1e-16 | 40/48 (NCI-H1573, H4, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.811×** | -5.6 | 1e-06 | 30/49 (COLO 205, SK-MEL-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.766×** | -5.3 | 6e-06 | 31/49 (HT-29, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.699×** | -5.1 | 2e-05 | 33/49 (HOP62, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.624×** | -4.9 | 4e-05 | 36/48 (LoVo, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **0.780×** | -4.8 | 8e-05 | 28/47 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.798×** | -4.5 | 3e-04 | 28/48 (SW48, J82, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.667×** | -4.2 | 9e-04 | 20/48 (NCI-H1573, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.687×** | -3.9 | 0.003 | 21/48 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.841× | -3.5 | 0.017 | 16/48 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.839× | -3.4 | 0.022 | 15/49 (NCI-H1573, SNU-423, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.735×** | -3.2 | 0.035 | 18/48 (KATO III, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.854× | -3.2 | 0.042 | 19/48 (A549, LOX-IMVI, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.809×** | -3.0 | 0.061 | 10/48 (SHP-77, AsPC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7523. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 194 | 1 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +8.8) ⚠ cell-cycle shift, explains ~39% of this change | [[Auranofin (drug)]] 5 µM 0.280× (z -14.2) |
| [[LoVo (line)]] | wt | 141 | 2 (2 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.9) ⚠ cell-cycle shift, explains ~39% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.308× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 201 | 1 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.8) ⚠ cell-cycle shift, explains ~39% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.139× (z -19.7) |
| [[HEC-1-A (line)]] | alt | 307 | 1 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +8.9) ⚠ cell-cycle shift, explains ~39% of this change | [[Auranofin (drug)]] 5 µM 0.314× (z -16.9) |
| [[A-172 (line)]] | wt | 162 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +8.7) ⚠ cell-cycle shift, explains ~39% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.251× (z -13.5) |
| [[HT-29 (line)]] | alt | 136 | 0 | 5 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.253× (z -14.3) |
| [[KATO III (line)]] | alt | 110 | 0 | 5 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.326× (z -12.9) |
| [[MIA PaCa-2 (line)]] | alt | 146 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +13.8) ⚠ cell-cycle shift, explains ~39% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.292× (z -12.4) |
| [[SW480 (line)]] | alt | 91.7 | 0 | 5 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.333× (z -15.4) |
| [[A549 (line)]] | wt | 130 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.289× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 123 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +19.6) ⚠ cell-cycle shift, explains ~39% of this change | [[Bortezomib (drug)]] 0.05 µM 0.498× (z -8.8) |
| [[PANC-1 (line)]] | alt | 107 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +13.3) ⚠ cell-cycle shift, explains ~39% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.345× (z -14.2) |
| [[SK-MEL-2 (line)]] | alt | 140 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +11.8) ⚠ cell-cycle shift, explains ~39% of this change | [[Auranofin (drug)]] 5 µM 0.374× (z -10.8) |
| [[A498 (line)]] | wt | 167 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.374× (z -9.9) |
| [[C32 (line)]] | wt | 129 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.6) ⚠ cell-cycle shift, explains ~39% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.270× (z -11.2) |
| [[H4 (line)]] | wt | 163 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.320× (z -10.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.256× (z -8.9) |
| [[HCT15 (line)]] | alt | 168 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.238× (z -11.5) |
| [[J82 (line)]] | alt | 122 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.3) ⚠ cell-cycle shift, explains ~39% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.352× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 108 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +15.7) ⚠ cell-cycle shift, explains ~39% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.377× (z -11.2) |
| [[SW1417 (line)]] | alt | 83.4 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.43× (z +10.0) | [[Ixazomib citrate (drug)]] 5 µM 0.454× (z -8.9) |
| [[SW48 (line)]] | wt | 169 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +13.1) ⚠ cell-cycle shift, explains ~39% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.310× (z -9.6) |
| [[A-427 (line)]] | wt | 142 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.473× (z -11.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.405× (z -10.2) |
| [[AN3 CA (line)]] | alt | 196 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.253× (z -9.8) |
| [[COLO 205 (line)]] | alt | 102 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.275× (z -10.9) |
| [[LS 180 (line)]] | wt | 133 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.5) ⚠ cell-cycle shift, explains ~39% of this change | [[Selinexor (drug)]] 5 µM 0.432× (z -10.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[Panc 03.27 (line)]] | alt | 119 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +14.5) ⚠ cell-cycle shift, explains ~39% of this change | [[Auranofin (drug)]] 5 µM 0.365× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 205 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.273× (z -12.9) |
| [[SHP-77 (line)]] | alt | 123 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.312× (z -12.0) |
| [[SNU-423 (line)]] | alt | 96.2 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.365× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 93.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +13.8) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[BT-474 (line)]] | alt | 82.3 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.323× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 107 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +10.9) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[Hs 766T (line)]] | wt | 134 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +13.4) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[HS-578T (line)]] | alt | 97.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.0) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 129 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +13.8) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1792 (line)]] | alt | 118 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.7) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2030 (line)]] | alt | 78.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.328× (z -10.6) |
| [[RKO (line)]] | wt | 169 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.347× (z -9.6) |
| [[SNU-1 (line)]] | wt | 180 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.250× (z -9.0) |
| [[SW 1088 (line)]] | alt | 143 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0630× (z -9.1) |
| [[SW 900 (line)]] | alt | 162 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.377× (z -9.0) |
| [[C-33 A (line)]] | alt | 119 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 185 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 97.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 182 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7523), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASPM]] | +0.84 | +0.83 / +0.84 | both halves | 7e-06 |  |
| [[KIF23]] | +0.83 | +0.75 / +0.84 | both halves | 7e-06 |  |
| [[NDC80]] | +0.83 | +0.75 / +0.85 | both halves | 7e-06 |  |
| [[KIF18A]] | +0.83 | +0.77 / +0.84 | both halves | 7e-06 |  |
| [[MKI67]] | +0.82 | +0.74 / +0.85 | both halves | 7e-06 |  |
| [[KIF4A]] | +0.81 | +0.73 / +0.84 | both halves | 7e-06 |  |
| [[KNL1]] | +0.81 | +0.74 / +0.83 | both halves | 7e-06 |  |
| [[CENPE]] | +0.80 | +0.81 / +0.80 | both halves | 7e-06 |  |
| [[CENPF]] | +0.80 | +0.77 / +0.81 | both halves | 7e-06 | STRING 588 |
| [[SGO1]] | +0.80 | +0.77 / +0.80 | both halves | 7e-06 |  |
| [[BIRC5]] | +0.80 | +0.75 / +0.82 | both halves | 7e-06 |  |
| [[TOP2A]] | +0.80 | +0.73 / +0.83 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRYAB]] | B | CRYAB activity lowers SCLT1's level | lines that do not express CRYAB (32) vs lines expressing it (18) | 1.08× higher at baseline in the lines without CRYAB | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, S100A1, AMBP |
| [[HDAC6]] | B | HDAC6 activity lowers SCLT1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.816). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.4, -55.8); signed map (-49.8, -44.2). **Vector** length 160, 56.6% of its response variance represented; |z| ≥ 3 in 1,310 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.65 to 60); *DREAM G2/M down* (control, mean cos +0.73 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.63 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +11.0 | +17.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +6.7 | +9.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +6.4 | +6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.2 | +3.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | +5.2 | +4.5 |
|  | [[Docetaxel (drug)]] 5 µM |  | +4.2 | +3.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +3.2 | +3.2 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +3.2 | +3.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.2 | +3.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +3.0 | +3.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -13.0 | -17.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -13.0 | -15.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -12.7 | -15.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -11.0 | -12.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -9.3 | -8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -8.6 | -13.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -5.9 | -5.1 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | sodium channel and clathrin linker 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q28.2 — chr4:128,864,921-129,093,600 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hCAP-1A, FLJ30655 |
| Reactome | 4 pathways, smallest: Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NL6](https://www.uniprot.org/uniprotkb/Q96NL6) (Sodium channel and clathrin linker 1):

> Adapter protein that links SCN10A to clathrin. Regulates SCN10A channel activity, possibly by promoting channel internalization (By similarity).

**Summary**, from NCBI Gene [132320](https://www.ncbi.nlm.nih.gov/gene/132320):

> This gene encodes an adaptor protein. Studies of a related gene in rat suggest that the encoded protein functions to link clathrin to the sodium channel protein type 10 subunit alpha protein. The encoded protein has also been identified as a component of distal appendages of centrioles that is necessary for ciliogenesis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:26406](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26406) · Entrez [132320](https://www.ncbi.nlm.nih.gov/gene/132320) · UniProt [Q96NL6](https://www.uniprot.org/uniprotkb/Q96NL6) · Ensembl [ENSG00000151466](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151466)

## Data

Gene col 7523: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7523); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7523, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7523]; `tensor/DDL_lfc|DDL_z.npy` [7523]; `embed/gene_vectors.npy` [7523]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7523 or target_col == 7523). Every well: [[SCLT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCLT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
