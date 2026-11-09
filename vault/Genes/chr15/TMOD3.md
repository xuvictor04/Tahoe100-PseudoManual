---
symbol: "TMOD3"
type: "gene"
col: 6189
ensembl_id: "ENSG00000138594"
name: "tropomodulin 3"
location: "15q21.2"
module: 111
arm: "+"
pooled_cpm: 242.29
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# TMOD3

*tropomodulin 3* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.34× (z +11.6, q 2e-28, up in 33 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 1.19× (z +6.6, q 4e-09, up in 19 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (A549 2.57×, HCT15 2.24×, A-427 2.05×, Panc 03.27 1.65×; ⚠ toxic; transcription drop); [[Vinblastine (sulfate) (drug)]] 5 µM in 4 lines (CFPAC-1 1.62×, NCI-H1573 1.54×, LS 180 1.44×, LoVo 1.31×); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A549 2.05×, SW480 1.67×, Panc 03.27 1.68×; ⚠ toxic; transcription drop); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 3 lines (NCI-H1573 1.73×, LS 180 1.65×, CFPAC-1 1.58×); [[Peretinoin (drug)]] 5 µM in 3 lines (LS 180 1.74×, CFPAC-1 1.64×, NCI-H1573 1.69×).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.561× (z -32.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IQGAP1]] (+0.60, fdr 1e-05), [[RHOA]] (+0.60, fdr 7e-06), [[ARPC5]] (+0.57, fdr 1e-05); moves opposite to [[HMGXB3]] (-0.49, fdr 3e-04), [[PLD6]] (-0.47, fdr 3e-05), [[ASPSCR1]] (-0.47, fdr 5e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC02057]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6189.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (A549 2.57×, HCT15 2.24×, A-427 2.05×, Panc 03.27 1.65×; ⚠ toxic; transcription drop); [[Vinblastine (sulfate) (drug)]] 5 µM in 4 lines (CFPAC-1 1.62×, NCI-H1573 1.54×, LS 180 1.44×, LoVo 1.31×); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A549 2.05×, SW480 1.67×, Panc 03.27 1.68×; ⚠ toxic; transcription drop); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 3 lines (NCI-H1573 1.73×, LS 180 1.65×, CFPAC-1 1.58×); [[Peretinoin (drug)]] 5 µM in 3 lines (LS 180 1.74×, CFPAC-1 1.64×, NCI-H1573 1.69×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +11.6 | 2e-28 | 33/49 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +11.0 | 1e-25 | 29/44 (A549, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.20× | +7.2 | 1e-10 | 22/47 (CFPAC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.19× | +6.6 | 4e-09 | 19/47 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +6.5 | 7e-09 | 16/49 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.16× | +5.9 | 5e-07 | 16/48 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.15× | +5.6 | 1e-06 | 15/47 (LS 180, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +5.2 | 2e-05 | 14/48 (LS 180, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +5.0 | 4e-05 | 16/48 (LS 180, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.13× | +4.8 | 7e-05 | 13/48 (A549, A498, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.13× | +4.8 | 9e-05 | 15/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.11× | +4.0 | 0.003 | 15/47 (NCI-H460, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.11× | +3.9 | 0.004 | 12/47 (A549, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.005 | 18/48 (HEC-1-A, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 1.10× | +3.8 | 0.006 | 7/48 (CFPAC-1, COLO 205, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | 1.10× | +3.6 | 0.011 | 8/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.09× | +3.4 | 0.020 | 16/48 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | 1.15× | +2.9 | 0.087 | 17/48 (NCI-H1573, A549, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6189.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.561×** | -32.7 | 0e+00 | 47/48 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.681×** | -15.4 | 0e+00 | 35/48 (RPMI-7951, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.714×** | -13.5 | 3e-39 | 32/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.716×** | -13.4 | 1e-38 | 35/48 (HOP62, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.759×** | -11.0 | 3e-26 | 32/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.756×** | -10.8 | 4e-25 | 34/47 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.822×** | -7.9 | 3e-13 | 25/48 (HOP62, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -6.7 | 2e-09 | 24/48 (C32, A-172, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.897× | -6.2 | 4e-08 | 15/49 (A549, HT-29, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.864× | -5.8 | 3e-07 | 12/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.899× | -4.3 | 0.001 | 13/48 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.929× | -4.2 | 0.001 | 12/48 (NCI-H2347, HT-29, …) | rises with dose | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **0.829×** | -3.9 | 0.004 | 17/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | 0.839× | -3.7 | 0.009 | 18/48 (SW480, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.913× | -3.7 | 0.009 | 8/48 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | 0.915× | -3.6 | 0.012 | 5/48 (SW48, AsPC-1, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 0.915× | -3.6 | 0.012 | 5/48 (CHP-212, AsPC-1, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.888× | -3.4 | 0.020 | 9/48 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | 0.918× | -3.4 | 0.021 | 4/49 (HEC-1-A, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.923× | -3.2 | 0.035 | 11/49 (HOP62, Panc 03.27, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | 0.863× | -3.1 | 0.053 | 15/49 (HOP62, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | 0.864× | -3.1 | 0.055 | 12/48 (Hs 766T, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.927× | -3.0 | 0.055 | 2/48 (BT-474, H4) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6189. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 377 | 6 (5 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.57× (z +19.6) ⚠ toxic; transcription drop · without an alert: [[Binimetinib (drug)]] 5 µM 1.55× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -22.4) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.592× (z -11.3) |
| [[HOP62 (line)]] | alt | 246 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -29.6) |
| [[CFPAC-1 (line)]] | alt | 308 | 5 (2 ⚠) | 2 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.62× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -23.0) |
| [[Panc 03.27 (line)]] | alt | 372 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.68× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -22.4) |
| [[A-172 (line)]] | wt | 269 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -17.6) |
| [[LS 180 (line)]] | wt | 221 | 5 (2 ⚠) | 1 | [[Peretinoin (drug)]] 5 µM 1.74× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.589× (z -13.7) |
| [[NCI-H1573 (line)]] | alt | 287 | 4 (1 ⚠) | 2 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.54× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -22.3) |
| [[HEC-1-A (line)]] | alt | 271 | 0 | 5 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.575× (z -12.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.606× (z -11.3) |
| [[J82 (line)]] | alt | 302 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.53× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.645× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 277 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -21.2) |
| [[AsPC-1 (line)]] | alt | 287 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -16.9) |
| [[HS-578T (line)]] | alt | 180 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -21.2) |
| [[HT-29 (line)]] | alt | 365 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.628× (z -10.7) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.638× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 340 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.57× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.589× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 197 | 1 (1 ⚠) | 3 | [[Pitavastatin (Calcium) (drug)]] 5 µM 1.61× (z +9.5) ⚠ cell-cycle shift, explains ~4% of this change | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -18.9) |
| [[SW480 (line)]] | alt | 206 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.67× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.632× (z -15.9) |
| [[C32 (line)]] | wt | 204 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -19.9) |
| [[H4 (line)]] | wt | 234 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.15× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -12.5) |
| [[Hs 766T (line)]] | wt | 261 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -21.8) |
| [[hTERT-HPNE (line)]] | wt | 223 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.87× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 163 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.397× (z -14.7) |
| [[RKO (line)]] | wt | 175 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -14.9) |
| [[RPMI-7951 (line)]] | alt | 277 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -34.0) |
| [[SNU-423 (line)]] | alt | 162 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -19.9) |
| [[SW1417 (line)]] | alt | 268 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.609× (z -9.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.640× (z -9.2) |
| [[SW48 (line)]] | wt | 312 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.461× (z -10.3) |
| [[A-427 (line)]] | wt | 114 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.05× (z +10.4) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 198 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -16.5) |
| [[HCT15 (line)]] | alt | 217 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.24× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -11.2) |
| [[KATO III (line)]] | alt | 270 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.62× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -15.1) |
| [[LoVo (line)]] | wt | 276 | 1 (1 ⚠) | 1 | [[Daptomycin (drug)]] 5 µM 1.51× (z +9.3) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.558× (z -18.7) |
| [[PANC-1 (line)]] | alt | 209 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.52× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 194 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.505× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.650× (z -9.2) |
| [[CHP-212 (line)]] | wt | 154 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.330× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 266 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -25.2) |
| [[NCI-H2030 (line)]] | alt | 310 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -18.9) |
| [[NCI-H23 (line)]] | alt | 207 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -13.1) |
| [[SHP-77 (line)]] | alt | 183 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.659× (z -9.9) |
| [[SW 900 (line)]] | alt | 149 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -12.4) |
| [[A498 (line)]] | wt | 203 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 157 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 176 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 212 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 323 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 179 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 209 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6189), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQGAP1]] | +0.60 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[RHOA]] | +0.60 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[ARPC5]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ANXA2]] | +0.56 | +0.50 / +0.63 | both halves | 1e-05 | pathway: Muscle contraction |
| [[AIDA]] | +0.56 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[RAC1]] | +0.54 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ADAM9]] | +0.54 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ADD1]] | +0.54 | +0.55 / +0.56 | both halves | 1e-05 | STRING 955 |
| [[MAP4]] | +0.53 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[CDC42BPB]] | +0.53 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ATL3]] | +0.53 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[ANXA1]] | +0.53 | +0.52 / +0.51 | both halves | 1e-05 | pathway: Muscle contraction |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGXB3]] | -0.49 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[PLD6]] | -0.47 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[ASPSCR1]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[PDP2]] | -0.47 | -0.39 / -0.59 | both halves | 6e-05 |  |
| [[ZNF316]] | -0.47 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[TMEM216]] | -0.47 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[AGER]] | -0.46 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[CHERP]] | -0.45 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[C16orf46]] | -0.45 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[SEMA4C]] | -0.45 | -0.38 / -0.37 | both halves | 9e-05 |  |
| [[ZCCHC3]] | -0.44 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[ZNF557]] | -0.44 | -0.44 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02057]] | B | LINC02057 activity raises TMOD3's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 1.25× lower at baseline in the lines without LINC02057 | 0.018 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[KRT81]] | B | KRT81 activity strengthens TMOD3's drug response | lines that do not express KRT81 (34) vs lines expressing it (15) | the lines without KRT81 respond 0.72× as strongly (z diff +1.56); strongest at Panobinostat 0.5 µM: 0.78x vs 0.66x (z diff +3.2) | 0.058 | ⚠ within organs, on part of the lines; also absent: CARD11, ANXA8, PSG9; target measured in part of the lines; artifact flags |
| [[IGFBP6]] | B | IGFBP6 activity strengthens TMOD3's drug response | lines that do not express IGFBP6 (16) vs lines expressing it (33) | the lines without IGFBP6 respond 0.65× as strongly (z diff +1.75); strongest at Panobinostat 0.5 µM: 0.83x vs 0.70x (z diff +3.1) | 0.083 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, HOXA10, COL6A1; target measured in part of the lines; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises TMOD3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.548). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.4, 10.2); signed map (-10.8, 35.3). **Vector** length 122, 37.1% of its response variance represented; |z| ≥ 3 in 1,386 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *RHO GTPases activate KTN1* (reactome, mean cos +0.52 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.4 | +6.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.4 | +6.6 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +6.3 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +11.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.9 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.2 | +5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.1 | +3.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.4 | +5.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.5 | -32.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.7 | -11.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.7 | -5.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -3.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -2.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | tropomodulin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:51,829,628-51,947,295 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UTMOD |
| Gene groups (HGNC) | Tropomodulins |
| Reactome | 8 pathways, smallest: Striated Muscle Contraction; RHOBTB2 GTPase cycle; RHOBTB GTPase Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYL9](https://www.uniprot.org/uniprotkb/Q9NYL9) (Tropomodulin-3):

> Blocks the elongation and depolymerization of the actin filaments at the pointed end. The Tmod/TM complex contributes to the formation of the short actin protofilament, which in turn defines the geometry of the membrane skeleton (By similarity).

**Summary**, from NCBI Gene [29766](https://www.ncbi.nlm.nih.gov/gene/29766):

> Enables cadherin binding activity involved in cell-cell adhesion. Predicted to be involved in actin filament organization; muscle contraction; and myofibril assembly. Predicted to act upstream of or within actin cytoskeleton organization; erythrocyte development; and positive regulation of mitotic cell cycle phase transition. Located in adherens junction. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11873](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11873) · Entrez [29766](https://www.ncbi.nlm.nih.gov/gene/29766) · UniProt [Q9NYL9](https://www.uniprot.org/uniprotkb/Q9NYL9) · Ensembl [ENSG00000138594](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138594)

## Data

Gene col 6189: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6189); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6189, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6189]; `tensor/DDL_lfc|DDL_z.npy` [6189]; `embed/gene_vectors.npy` [6189]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6189 or target_col == 6189). Every well: [[TMOD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMOD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
