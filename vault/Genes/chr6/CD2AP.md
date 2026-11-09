---
symbol: "CD2AP"
type: "gene"
col: 12526
ensembl_id: "ENSG00000198087"
name: "CD2 associated protein"
location: "6p12.3"
module: 44
arm: "+"
pooled_cpm: 323.64
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 22
direction_downstream: 0
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# CD2AP

*CD2 associated protein* — 6p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.22× (z +6.6, q 2e-08, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.622× (z -16.0, q 0e+00, down in 45 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 14 lines (MIA PaCa-2 0.342×, SNU-423 0.414×, NCI-H23 0.448×, A-427 0.480×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (A549 0.426×, HEC-1-A 0.516×, HT-29 0.422×, CFPAC-1 0.438×, …; ⚠ cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.288×, LoVo 0.348×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Volasertib (drug)]] 5 µM in 1 line (SW 1271 0.0547×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTNND1]] (+0.60, fdr 1e-05), [[MVP-DT]] (+0.59, fdr 1e-05), [[LIMA1]] (+0.59, fdr 3e-05); moves opposite to [[ZNF275]] (-0.56, fdr 3e-05), [[GPR89A]] (-0.52, fdr 3e-04), [[DPY19L3]] (-0.51, fdr 6e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[ADGRF1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12526.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +6.6 | 2e-08 | 25/48 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.26×** | +6.0 | 4e-07 | 31/49 (LoVo, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.17× | +5.1 | 5e-05 | 22/48 (PANC-1, A549, …) | top dose only | composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +5.0 | 7e-05 | 18/47 (HOP62, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.9 | 1e-04 | 16/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.32×** | +4.8 | 1e-04 | 24/49 (PANC-1, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.10× | +4.5 | 5e-04 | 10/48 (LoVo, A-172, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.14× | +4.3 | 0.001 | 6/48 (hTERT-HPNE, LS 180, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.002 | 24/48 (HOP62, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.13× | +4.1 | 0.003 | 16/49 (HOP62, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.17× | +4.0 | 0.003 | 19/48 (PANC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.12× | +3.8 | 0.008 | 14/50 (HOP62, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.07× | +3.4 | 0.031 | 13/48 (PANC-1, A549, …) | top dose only | composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | 1.09× | +3.3 | 0.038 | 7/48 (HOP62, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 1.20× | +3.1 | 0.062 | 14/48 (SW48, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Hexylresorcinol (drug)]] 0.5 µM |  | 1.12× | +3.0 | 0.085 | 4/49 (A498, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12526.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 14 lines (MIA PaCa-2 0.342×, SNU-423 0.414×, NCI-H23 0.448×, A-427 0.480×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (A549 0.426×, HEC-1-A 0.516×, HT-29 0.422×, CFPAC-1 0.438×, …; ⚠ cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.288×, LoVo 0.348×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Volasertib (drug)]] 5 µM in 1 line (SW 1271 0.0547×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.622×** | -16.0 | 0e+00 | 45/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.641×** | -14.4 | 1e-44 | 44/47 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.655×** | -14.3 | 5e-44 | 40/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.663×** | -13.9 | 1e-41 | 39/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.790×** | -11.3 | 2e-27 | 29/49 (A549, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.733×** | -10.5 | 9e-24 | 32/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.839× | -5.9 | 2e-07 | 20/48 (NCI-H2347, KATO III, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.866× | -4.6 | 3e-04 | 19/48 (COLO 205, LoVo, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.909× | -4.6 | 3e-04 | 2/48 (H4, SW 1088) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.898× | -3.7 | 0.014 | 9/49 (SW1417, RKO, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.864× | -3.5 | 0.022 | 17/48 (KATO III, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.904× | -3.4 | 0.031 | 14/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.909× | -3.2 | 0.053 | 10/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.909× | -3.2 | 0.053 | 9/48 (CFPAC-1, COLO 205, …) | two highest doses |  |
| [[Infigratinib (drug)]] 5 µM |  | 0.838× | -3.1 | 0.067 | 14/48 (Hs 766T, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.940× | -3.0 | 0.094 | 5/48 (HEC-1-A, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12526. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 418 | 4 (3 ⚠) | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.68× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 932 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -16.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.488× (z -10.1) |
| [[COLO 205 (line)]] | alt | 395 | 0 | 9 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -16.1) ⚠ cell-cycle shift, explains ~55% of this change |
| [[HOP62 (line)]] | alt | 246 | 5 (1 ⚠) | 3 (2 ⚠) | [[Trametinib (drug)]] 5 µM 1.87× (z +11.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 1.78× (z +10.1) | [[Auranofin (drug)]] 5 µM 0.495× (z -12.7) |
| [[KATO III (line)]] | alt | 717 | 0 | 8 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -15.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A549 (line)]] | wt | 220 | 4 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +28.5) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.51× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -21.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[AsPC-1 (line)]] | alt | 490 | 1 (1 ⚠) | 6 (5 ⚠) | [[Trametinib (drug)]] 5 µM 1.65× (z +8.6) ⚠ cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 0.5 µM 0.376× (z -16.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.537× (z -10.2) |
| [[HT-29 (line)]] | alt | 712 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -19.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.450× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 782 | 0 | 7 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.452× (z -13.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.559× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 462 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -20.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.571× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 762 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -13.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.548× (z -8.9) |
| [[PANC-1 (line)]] | alt | 243 | 5 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +31.9) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.21× (z +16.0) | [[Auranofin (drug)]] 5 µM 0.623× (z -12.4) |
| [[SNU-423 (line)]] | alt | 388 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.414× (z -14.3) |
| [[SW1417 (line)]] | alt | 417 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.446× (z -15.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 227 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.470× (z -18.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.648× (z -10.7) |
| [[A498 (line)]] | wt | 140 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +26.4) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[NCI-H460 (line)]] | wt | 136 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.78× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.66× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 220 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +10.5) | [[Auranofin (drug)]] 5 µM 0.567× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 330 | 1 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 1.62× (z +8.7) ⚠ cell-cycle shift, explains ~8% of this change | [[Panobinostat (drug)]] 0.5 µM 0.538× (z -11.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LS 180 (line)]] | wt | 419 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.502× (z -12.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 247 | 1 (1 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 1.69× (z +9.4) ⚠ cell-cycle shift, explains ~8% of this change | [[Auranofin (drug)]] 5 µM 0.342× (z -19.9) |
| [[NCI-H23 (line)]] | alt | 347 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.448× (z -14.1) |
| [[SW48 (line)]] | wt | 314 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 3.98× (z +9.0) | — |
| [[A-427 (line)]] | wt | 221 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.417× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.480× (z -14.1) |
| [[HCT15 (line)]] | alt | 398 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.507× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 165 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.97× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.79× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 204 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -14.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H2030 (line)]] | alt | 247 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.591× (z -10.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.619× (z -9.5) |
| [[SW 1271 (line)]] | alt | 217 | 0 | 2 | — | [[Volasertib (drug)]] 5 µM 0.0547× (z -9.8) |
| [[C32 (line)]] | wt | 144 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.537× (z -9.0) |
| [[H4 (line)]] | wt | 254 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.535× (z -8.7) |
| [[HS-578T (line)]] | alt | 212 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -10.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[J82 (line)]] | alt | 215 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.56× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 250 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.375× (z -14.4) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 203 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.532× (z -10.5) |
| [[A-172 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 274 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 282 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 218 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 269 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 182 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 157 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 309 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 273 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 202 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 205 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12526), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTNND1]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 | pathway: Cell-Cell communication |
| [[MVP-DT]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[LIMA1]] | +0.59 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[ELF3-AS1]] | +0.59 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[PTBP3]] | +0.55 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[ALCAM]] | +0.55 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[CXADR]] | +0.55 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[RPS6KA6]] | +0.54 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[ATP8B1]] | +0.54 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[HHLA2]] | +0.53 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[PICALM]] | +0.53 | +0.43 / +0.60 | both halves | 3e-05 | STRING 865 |
| [[CGN]] | +0.53 | +0.46 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF275]] | -0.56 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[GPR89A]] | -0.52 | -0.28 / -0.62 | both halves | 3e-04 |  |
| [[DPY19L3]] | -0.51 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[TRAPPC12]] | -0.51 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[EIF1AD]] | -0.51 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[INTS15]] | -0.51 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[L3MBTL2]] | -0.50 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[GNAS-AS1]] | -0.50 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[SLC30A6]] | -0.50 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[ZKSCAN2-DT]] | -0.50 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[SSH1]] | -0.49 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[PRKAG1]] | -0.49 | -0.45 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 22, C 0. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRF1]] | B | ADGRF1 activity raises CD2AP's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 1.99× lower at baseline in the lines without ADGRF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[PDZK1IP1]] | B | PDZK1IP1 activity raises CD2AP's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 1.88× lower at baseline in the lines without PDZK1IP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[ALOX5]] | B | ALOX5 activity raises CD2AP's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 1.62× lower at baseline in the lines without ALOX5 | 0.002 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[ITGB6]] | B | ITGB6 activity raises CD2AP's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 1.80× lower at baseline in the lines without ITGB6 | 0.005 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[ST14]] | B | ST14 activity raises CD2AP's level | lines that do not express ST14 (32) vs lines expressing it (18) | 1.97× lower at baseline in the lines without ST14 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[PDZK1IP1]] | B | PDZK1IP1 activity strengthens CD2AP's drug response | lines that do not express PDZK1IP1 (32) vs lines expressing it (17) | the lines without PDZK1IP1 respond 0.71× as strongly (z diff +1.45); strongest at Belinostat 5 µM: 0.82x vs 0.60x (z diff +4.1) | 0.006 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8; target measured in part of the lines; artifact flags |
| [[ADGRF1]] | B | ADGRF1 activity strengthens CD2AP's drug response | lines that do not express ADGRF1 (35) vs lines expressing it (14) | the lines without ADGRF1 respond 0.67× as strongly (z diff +1.73); strongest at Belinostat 5 µM: 0.81x vs 0.56x (z diff +4.9) | 0.014 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; target measured in part of the lines; artifact flags |
| [[RASSF6]] | B | RASSF6 activity strengthens CD2AP's drug response | lines that do not express RASSF6 (28) vs lines expressing it (21) | the lines without RASSF6 respond 0.69× as strongly (z diff +1.55); strongest at Belinostat 5 µM: 0.83x vs 0.63x (z diff +3.9) | 0.020 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6; target measured in part of the lines; artifact flags |
| [[ALOX5]] | B | ALOX5 activity strengthens CD2AP's drug response | lines that do not express ALOX5 (28) vs lines expressing it (21) | the lines without ALOX5 respond 0.79× as strongly (z diff +1.01); strongest at Belinostat 5 µM: 0.80x vs 0.65x (z diff +2.7) | 0.036 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6; target measured in part of the lines; artifact flags |
| [[ITGB6]] | B | ITGB6 activity strengthens CD2AP's drug response | lines that do not express ITGB6 (32) vs lines expressing it (17) | the lines without ITGB6 respond 0.71× as strongly (z diff +1.39); strongest at Topotecan (hydrochloride) 0.5 µM: 0.88x vs 0.70x (z diff +3.6) | 0.039 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4; target measured in part of the lines; artifact flags |
| [[CGN]] | B | CGN activity raises CD2AP's level | lines that do not express CGN (21) vs lines expressing it (29) | 1.66× lower at baseline in the lines without CGN | 0.047 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[RASSF6]] | B | RASSF6 activity raises CD2AP's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 1.57× lower at baseline in the lines without RASSF6 | 0.047 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.402). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.4, 8.9); signed map (49.0, 7.1). **Vector** length 126, 40.2% of its response variance represented; |z| ≥ 3 in 1,296 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +8.4 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.9 | -0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | +6.2 | +5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.7 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.5 | +5.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.4 | +4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.3 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.3 | -16.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.3 | -14.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~1% of this change | -4.3 | -4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -4.0 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -3.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.9 | -2.1 |
|  | [[Infigratinib (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | CD2 associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.3 — chr6:47,477,789-47,627,263 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CMS |
| Gene groups (HGNC) | SH3 domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 2 pathways, smallest: Nephrin family interactions; Cell-Cell communication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5K6](https://www.uniprot.org/uniprotkb/Q9Y5K6) (CD2-associated protein):

> Seems to act as an adapter protein between membrane proteins and the actin cytoskeleton. In collaboration with CBLC, modulates the rate of RET turnover and may act as regulatory checkpoint that limits the potency of GDNF on neuronal survival. Controls CBLC function, converting it from an inhibitor to a promoter of RET degradation (By similarity). May play a role in receptor clustering and cytoskeletal polarity in the junction between T-cell and antigen-presenting cell (By similarity). May …

**Summary**, from NCBI Gene [23607](https://www.ncbi.nlm.nih.gov/gene/23607):

> This gene encodes a scaffolding molecule that regulates the actin cytoskeleton. The protein directly interacts with filamentous actin and a variety of cell membrane proteins through multiple actin binding sites, SH3 domains, and a proline-rich region containing binding sites for SH3 domains. The cytoplasmic protein localizes to membrane ruffles, lipid rafts, and the leading edges of cells. It is implicated in dynamic actin remodeling and membrane trafficking that occurs during receptor …

**Accessions** — [HGNC:14258](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14258) · Entrez [23607](https://www.ncbi.nlm.nih.gov/gene/23607) · UniProt [Q9Y5K6](https://www.uniprot.org/uniprotkb/Q9Y5K6) · Ensembl [ENSG00000198087](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198087)

## Data

Gene col 12526: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12526); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12526, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12526]; `tensor/DDL_lfc|DDL_z.npy` [12526]; `embed/gene_vectors.npy` [12526]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12526 or target_col == 12526). Every well: [[CD2AP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CD2AP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
