---
symbol: "UFL1"
type: "gene"
col: 283
ensembl_id: "ENSG00000014123"
name: "UFM1 specific ligase 1"
location: "6q16.1"
module: 41
arm: "+"
pooled_cpm: 83.51
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 31
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# UFL1

*UFM1 specific ligase 1* — 6q16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.23× (z +4.5, q 0.004, up in 22 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 5 lines (NCI-H1573 4.58×, RKO 3.14×, LoVo 2.82×, SW480 1.94×, …; ⚠ cell-cycle shift, explains ~27% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H1573 2.11×, LoVo 2.20×, LOX-IMVI 1.78×; ⚠ cell-cycle shift, explains ~16% of this change); [[Selinexor (drug)]] 5 µM in 1 line (NCI-H2347 1.78×; ⚠ cell-cycle shift, explains ~16% of this change).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (18 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.423× (z -18.8, q 0e+00, down in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.436× (z -18.2, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPIL4]] (+0.81, fdr 7e-06), [[ZRSR2]] (+0.77, fdr 7e-06), [[GOLGA2]] (+0.76, fdr 7e-06); moves opposite to [[PTK2]] (-0.58, fdr 2e-05), [[GATAD2A]] (-0.57, fdr 1e-05), [[EIF5A]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 283.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 5 lines (NCI-H1573 4.58×, RKO 3.14×, LoVo 2.82×, SW480 1.94×, …; ⚠ cell-cycle shift, explains ~27% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H1573 2.11×, LoVo 2.20×, LOX-IMVI 1.78×; ⚠ cell-cycle shift, explains ~16% of this change); [[Selinexor (drug)]] 5 µM in 1 line (NCI-H2347 1.78×; ⚠ cell-cycle shift, explains ~16% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.23×** | +4.5 | 0.004 | 22/48 (NCI-H1573, RKO, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.12× | +3.4 | 0.19 | 20/48 (NCI-H1573, LoVo, …) | two highest doses | composition shift |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.11× | +3.3 | 0.20 | 5/49 (CFPAC-1, KATO III, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.11× | +3.1 | 0.22 | 4/48 (SW480, BT-474, …) | top dose only |  |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.22 | 8/48 (NCI-H1792, SW480, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 22 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 283.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.423×** | -18.8 | 0e+00 | 46/48 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.436×** | -18.2 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.444×** | -17.8 | 0e+00 | 47/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.520×** | -14.3 | 3e-44 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.559×** | -12.7 | 4e-35 | 39/48 (HS-578T, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.352×** | -12.0 | 5e-31 | 46/49 (Hs 766T, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.585×** | -11.7 | 8e-30 | 39/48 (H4, HCT15, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.595×** | -11.4 | 4e-28 | 39/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.377×** | -11.2 | 4e-27 | 45/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.714×** | -10.5 | 8e-24 | 42/48 (SNU-1, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.623×** | -10.0 | 1e-21 | 38/47 (SNU-423, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.640×** | -9.0 | 8e-18 | 30/45 (LS 180, A549, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.669×** | -8.5 | 1e-15 | 30/48 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.734×** | -6.8 | 5e-10 | 36/48 (Hs 766T, NCI-H1792, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.750×** | -6.3 | 1e-08 | 29/48 (NCI-H2030, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.760×** | -6.0 | 6e-08 | 33/48 (HCT15, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.827×** | -5.9 | 1e-07 | 24/48 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.780×** | -5.4 | 2e-06 | 27/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.718×** | -5.3 | 3e-06 | 29/47 (LOX-IMVI, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.825×** | -4.1 | 1e-03 | 24/48 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.737×** | -3.5 | 0.008 | 16/49 (SW 900, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.899× | -3.3 | 0.015 | 8/48 (KATO III, RPMI-7951, …) | top dose only |  |
| [[Acetohexamide (drug)]] 5 µM |  | 0.912× | -2.9 | 0.064 | 4/48 (HS-578T, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 283. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 101 | 0 | 13 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -14.5) |
| [[NCI-H1792 (line)]] | alt | 104 | 0 | 11 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.357× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.366× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 72.0 | 0 | 10 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.346× (z -15.2) |
| [[SNU-423 (line)]] | alt | 116 | 0 | 10 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.264× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.291× (z -16.3) |
| [[PANC-1 (line)]] | alt | 99.3 | 0 | 9 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -17.8) |
| [[SW480 (line)]] | alt | 95.2 | 1 (1 ⚠) | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.94× (z +9.3) ⚠ cell-cycle shift, explains ~27% of this change | [[Digitoxin (drug)]] 5 µM 0.262× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.308× (z -16.3) |
| [[HS-578T (line)]] | alt | 99.1 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.340× (z -13.8) |
| [[A-172 (line)]] | wt | 75.1 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.446× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.469× (z -9.4) |
| [[HOP62 (line)]] | alt | 77.5 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.279× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -15.8) |
| [[Hs 766T (line)]] | wt | 146 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.265× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.129× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 69.9 | 2 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.58× (z +16.8) ⚠ cell-cycle shift, explains ~27% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.339× (z -11.4) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.408× (z -9.8) |
| [[H4 (line)]] | wt | 85.1 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -13.3) |
| [[HCT15 (line)]] | alt | 153 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.292× (z -11.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.389× (z -8.6) |
| [[J82 (line)]] | alt | 73.3 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.311× (z -14.1) |
| [[LS 180 (line)]] | wt | 107 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.248× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -15.8) |
| [[SW 900 (line)]] | alt | 71.0 | 0 | 5 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.150× (z -10.3) |
| [[A549 (line)]] | wt | 62.1 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.303× (z -12.8) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.348× (z -10.9) |
| [[KATO III (line)]] | alt | 162 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.27× (z +8.6) ⚠ cell-cycle shift, explains ~27% of this change | [[Digitoxin (drug)]] 5 µM 0.268× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.383× (z -9.8) |
| [[LoVo (line)]] | wt | 87.8 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.4) ⚠ cell-cycle shift, explains ~16% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.315× (z -11.2) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 55.1 | 1 (1 ⚠) | 3 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.78× (z +9.6) ⚠ cell-cycle shift, explains ~16% of this change | [[Digitoxin (drug)]] 5 µM 0.418× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.484× (z -8.7) |
| [[SW48 (line)]] | wt | 133 | 0 | 4 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -10.4) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.419× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 79.2 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.0) ⚠ cell-cycle shift, explains ~16% of this change | [[PH-797804 (drug)]] 5 µM 0.198× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 61.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.337× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.373× (z -10.5) |
| [[SHP-77 (line)]] | alt | 56.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.309× (z -10.6) |
| [[SNU-1 (line)]] | wt | 89.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0922× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.287× (z -14.7) |
| [[AsPC-1 (line)]] | alt | 48.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.337× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.349× (z -10.5) |
| [[BT-474 (line)]] | alt | 52.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.295× (z -10.4) |
| [[C32 (line)]] | wt | 73.1 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.292× (z -11.9) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.347× (z -9.8) |
| [[COLO 205 (line)]] | alt | 71.6 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.289× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 77.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.373× (z -8.9) |
| [[RKO (line)]] | wt | 96.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.14× (z +12.4) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -10.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.377× (z -9.6) |
| [[A-427 (line)]] | wt | 78.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.470× (z -8.9) |
| [[C-33 A (line)]] | alt | 56.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.271× (z -9.7) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 51.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.416× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 70.5 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.198× (z -10.0) ⚠ toxic |
| [[HT-29 (line)]] | alt | 79.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.334× (z -10.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.428× (z -8.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 58.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[A498 (line)]] | wt | 84.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 97.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 70.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 69.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 283), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIL4]] | +0.81 | +0.82 / +0.68 | both halves | 7e-06 |  |
| [[ZRSR2]] | +0.77 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[GOLGA2]] | +0.76 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[TMF1]] | +0.75 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[TGDS]] | +0.73 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[NKAP]] | +0.72 | +0.79 / +0.66 | both halves | 7e-06 |  |
| [[ERCC5]] | +0.72 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[GOLGA5]] | +0.71 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[GOLGA4]] | +0.69 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[LYSMD3]] | +0.68 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[RINT1]] | +0.68 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[TBC1D23]] | +0.68 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTK2]] | -0.58 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[GATAD2A]] | -0.57 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[EIF5A]] | -0.57 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[GNG12]] | -0.56 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[TCF20]] | -0.56 | -0.65 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.803). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (10.8, -38.4); signed map (-51.2, 15.6). **Vector** length 125, 41.3% of its response variance represented; |z| ≥ 3 in 1,303 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Intra-Golgi and retrograde Golgi-to-ER traffic* (reactome, mean cos +0.52 to 12); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.53 to 8); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +10.3 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +9.5 | +4.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +4.8 | +2.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +2.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.9 | +1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.6 | +1.0 |
|  | [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | +2.3 | +3.1 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | +2.3 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -7.2 | -18.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.8 | -18.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.0 | -14.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.8 | -12.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.8 | -10.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.6 | -11.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -10.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.9 | -4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.7 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | UFM1 specific ligase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.1 — chr6:96,521,595-96,555,276 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NLBP, Maxer, RCAD; previously KIAA0776 |
| Gene groups (HGNC) | Atypical E3 ubiquitin ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [O94874](https://www.uniprot.org/uniprotkb/O94874) (E3 UFM1-protein ligase 1):

> E3 protein ligase that mediates ufmylation, the covalent attachment of the ubiquitin-like modifier UFM1 to lysine residues on target proteins, and which plays a key role in various processes, such as ribosome recycling, response to DNA damage, interferon response or reticulophagy (also called ER-phagy). Catalyzes ufmylation of many protein, such as CD274/PD-L1, CDK5RAP3, CYB5R3, DDRGK1, EIF6, histone H4, MRE11, P4HB, PDCD1/PD-1, TRIP4, RPN1, RPS20/uS10, RPL10/uL16, RPL26/uL24, SYVN1/HRD1 and …

**Summary**, from NCBI Gene [23376](https://www.ncbi.nlm.nih.gov/gene/23376):

> Enables UFM1 ligase activity and protein kinase binding activity. Involved in several processes, including positive regulation of reticulophagy; regulation of intracellular signal transduction; and regulation of protein metabolic process. Acts upstream of or within several processes, including positive regulation of cell population proliferation; regulation of proteasomal ubiquitin-dependent protein catabolic process; and response to endoplasmic reticulum stress. Located in cytoplasm; nucleus; …

**Accessions** — [HGNC:23039](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23039) · Entrez [23376](https://www.ncbi.nlm.nih.gov/gene/23376) · UniProt [O94874](https://www.uniprot.org/uniprotkb/O94874) · Ensembl [ENSG00000014123](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000014123)

## Data

Gene col 283: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 283); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 283, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 283]; `tensor/DDL_lfc|DDL_z.npy` [283]; `embed/gene_vectors.npy` [283]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 283 or target_col == 283). Every well: [[UFL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UFL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
