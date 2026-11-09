---
symbol: "COP1"
type: "gene"
col: 6698
ensembl_id: "ENSG00000143207"
name: "COP1 E3 ubiquitin ligase"
location: "1q25.1-q25.2"
module: 36
arm: "+"
pooled_cpm: 284.65
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 17
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# COP1

*COP1 E3 ubiquitin ligase* — 1q25.1-q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.85× (z +6.6, q 3e-08, up in 34 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Ixazomib citrate (drug)]] 5 µM in 5 lines (NCI-H460 1.72×, COLO 205 1.98×, HT-29 1.83×, H4 2.10×, …; ⚠ cell-cycle shift, explains ~21% of this change); [[TAK-901 (drug)]] 5 µM in 4 lines (C32 6.27×, SW480 3.59×, COLO 205 4.29×, LS 180 3.57×); [[PH-797804 (drug)]] 5 µM in 2 lines (C32 7.41×, SW48 4.87×); [[TAK-901 (drug)]] 0.05 µM in 2 lines (LOX-IMVI 2.14×, SW48 2.66×).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.377× (z -21.7, q 0e+00, down in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.517× (z -14.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXW11]] (+0.71, fdr 7e-06), [[CDC123]] (+0.66, fdr 1e-05), [[RAP1GDS1]] (+0.64, fdr 1e-05); moves opposite to [[NFKB2]] (-0.62, fdr 1e-05), [[NR1D1]] (-0.60, fdr 1e-05), [[UAP1L1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6698.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Ixazomib citrate (drug)]] 5 µM in 5 lines (NCI-H460 1.72×, COLO 205 1.98×, HT-29 1.83×, H4 2.10×, …; ⚠ cell-cycle shift, explains ~21% of this change); [[TAK-901 (drug)]] 5 µM in 4 lines (C32 6.27×, SW480 3.59×, COLO 205 4.29×, LS 180 3.57×); [[PH-797804 (drug)]] 5 µM in 2 lines (C32 7.41×, SW48 4.87×); [[TAK-901 (drug)]] 0.05 µM in 2 lines (LOX-IMVI 2.14×, SW48 2.66×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.85×** | +6.6 | 3e-08 | 34/49 (C32, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.73×** | +5.8 | 2e-06 | 39/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.37×** | +5.4 | 1e-05 | 36/48 (HT-29, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.20×** | +4.0 | 0.008 | 24/48 (NCI-H460, COLO 205, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.048 | 14/47 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.17× | +3.4 | 0.074 | 21/47 (NCI-H460, A549, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.35× | +3.2 | 0.11 | 26/49 (RKO, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.11× | +3.1 | 0.13 | 4/48 (SK-MEL-2, NCI-H2030, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | 1.34× | +3.1 | 0.13 | 21/45 (PANC-1, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6698.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.377×** | -21.7 | 0e+00 | 48/49 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.387×** | -20.3 | 0e+00 | 44/44 (SK-MEL-2, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.572×** | -17.3 | 0e+00 | 43/48 (HOP62, J82, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.517×** | -14.7 | 0e+00 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.564×** | -12.2 | 2e-32 | 46/48 (J82, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.548×** | -12.2 | 2e-32 | 38/45 (SW 900, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.575×** | -11.8 | 2e-30 | 46/47 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.588×** | -11.8 | 2e-30 | 46/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.588×** | -11.8 | 2e-30 | 40/48 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **0.663×** | -9.1 | 4e-18 | 46/48 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.670×** | -8.9 | 3e-17 | 44/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.679×** | -8.6 | 4e-16 | 37/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.815×** | -6.3 | 1e-08 | 26/49 (A549, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.785×** | -5.4 | 3e-06 | 31/48 (SK-MEL-2, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.856× | -4.8 | 7e-05 | 20/48 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.815×** | -4.6 | 2e-04 | 26/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.783×** | -3.9 | 0.003 | 32/47 (HS-578T, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.836× | -3.6 | 0.008 | 22/47 (NCI-H460, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.862× | -3.3 | 0.026 | 11/48 (NCI-H1792, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.822×** | -3.1 | 0.047 | 21/48 (Hs 766T, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.906× | -3.1 | 0.052 | 7/48 (NCI-H23, RKO, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.872× | -2.9 | 0.083 | 12/49 (HOP62, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6698. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 235 | 0 | 13 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.368× (z -15.7) |
| [[HOP62 (line)]] | alt | 258 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -24.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.474× (z -11.4) |
| [[HT-29 (line)]] | alt | 277 | 2 (1 ⚠) | 9 (7 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.93× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.413× (z -12.8) |
| [[LoVo (line)]] | wt | 316 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.426× (z -14.3) |
| [[Panc 03.27 (line)]] | alt | 278 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -14.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.440× (z -13.3) |
| [[SW480 (line)]] | alt | 256 | 1 | 10 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 3.59× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.397× (z -16.1) |
| [[A549 (line)]] | wt | 266 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -22.1) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.446× (z -13.5) |
| [[J82 (line)]] | alt | 277 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -23.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.503× (z -9.8) |
| [[LS 180 (line)]] | wt | 328 | 1 | 9 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 3.57× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.413× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 484 | 2 (2 ⚠) | 7 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 1.79× (z +9.7) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -24.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.492× (z -12.2) |
| [[C32 (line)]] | wt | 232 | 3 | 5 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 7.41× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.352× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.501× (z -9.6) |
| [[HS-578T (line)]] | alt | 226 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -21.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -17.4) |
| [[NCI-H1573 (line)]] | alt | 311 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -18.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.383× (z -15.8) |
| [[NCI-H2347 (line)]] | alt | 271 | 0 | 8 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.395× (z -13.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.449× (z -11.8) |
| [[A-427 (line)]] | wt | 586 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -25.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.468× (z -11.8) |
| [[A498 (line)]] | wt | 289 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.431× (z -13.3) |
| [[LOX-IMVI (line)]] | wt | 332 | 1 | 6 (5 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.14× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -22.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.426× (z -13.6) |
| [[SW 900 (line)]] | alt | 414 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.506× (z -9.8) |
| [[SW1417 (line)]] | alt | 234 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.472× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.476× (z -11.7) |
| [[SW48 (line)]] | wt | 285 | 2 | 5 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.66× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -12.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.458× (z -9.0) |
| [[A-172 (line)]] | wt | 302 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.428× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 328 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -17.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.415× (z -13.4) |
| [[H4 (line)]] | wt | 279 | 1 (1 ⚠) | 5 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.10× (z +8.7) ⚠ cell-cycle shift, explains ~21% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.449× (z -9.3) |
| [[Hs 766T (line)]] | wt | 287 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.357× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.445× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 251 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.426× (z -11.0) |
| [[PANC-1 (line)]] | alt | 253 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.569× (z -9.9) |
| [[RKO (line)]] | wt | 367 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -23.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.367× (z -14.8) |
| [[BT-474 (line)]] | alt | 225 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -11.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.456× (z -9.8) |
| [[COLO 205 (line)]] | alt | 301 | 2 (1 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.29× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.525× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 229 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.544× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 303 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.276× (z -18.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.571× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 234 | 1 (1 ⚠) | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.73× (z +8.6) ⚠ cell-cycle shift, explains ~21% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -18.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 196 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.383× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.504× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 221 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.377× (z -14.5) ⚠ toxic |
| [[HCT15 (line)]] | alt | 274 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -12.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 208 | 1 | 3 (2 ⚠) | [[Ponatinib (drug)]] 5 µM 2.04× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.418× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 172 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.298× (z -16.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.505× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 220 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -17.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 262 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -15.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 224 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -13.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 263 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -28.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.508× (z -10.2) |
| [[AN3 CA (line)]] | alt | 240 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -9.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SNU-1 (line)]] | wt | 279 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -20.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 297 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -10.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 243 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -26.0) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 304 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 174 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6698), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW11]] | +0.71 | +0.75 / +0.65 | both halves | 7e-06 | same gene group; pathway: Cell Cycle Checkpoints |
| [[CDC123]] | +0.66 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[RAP1GDS1]] | +0.64 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[FBXW7]] | +0.64 | +0.64 / +0.65 | both halves | 7e-06 | same gene group; pathway: Neddylation |
| [[VTI1A]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[GNAQ]] | +0.63 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[EVI5]] | +0.63 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[TRAPPC10]] | +0.62 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[CCNY]] | +0.62 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[IPO11]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[BIRC6]] | +0.59 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[PPHLN1]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKB2]] | -0.62 | -0.68 / -0.57 | both halves | 1e-05 |  |
| [[NR1D1]] | -0.60 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[UAP1L1]] | -0.59 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[BHLHE41]] | -0.59 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[RELA]] | -0.57 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[LIPT1]] | -0.56 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[ZSCAN9]] | -0.56 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[CLK4]] | -0.55 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[COMMD3]] | -0.55 | -0.62 / -0.54 | both halves | 1e-05 | pathway: Neddylation; STRING 510 |
| [[HUS1]] | -0.55 | -0.59 / -0.47 | both halves | 2e-05 | pathway: Cell Cycle Checkpoints |
| [[SEPSECS]] | -0.54 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[CCDC159]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers COP1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-14.4, -13.0); signed map (-17.1, -49.2). **Vector** length 111, 43.8% of its response variance represented; |z| ≥ 3 in 1,289 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | +7.2 | +5.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +7.0 | +2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.9 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +6.6 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +6.1 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.0 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | -1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +2.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -8.5 | -17.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.9 | -11.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -7.7 | -12.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.7 | -8.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.7 | -4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.6 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | COP1 E3 ubiquitin ligase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.1-q25.2 — chr1:175,944,831-176,207,286 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10416, RNF200, FAP78, CFAP78; previously RFWD2 |
| Gene groups (HGNC) | Ring finger proteins; WD repeat domain containing; Cilia and flagella associated; Small nucleolar RNA protein coding host genes; RING finger E3 ubiquitin protein ligases |
| Reactome | 8 pathways, smallest: Autodegradation of the E3 ubiquitin ligase COP1; Stabilization of p53; p53-Dependent G1 DNA Damage Response |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHY2](https://www.uniprot.org/uniprotkb/Q8NHY2) (E3 ubiquitin-protein ligase COP1):

> E3 ubiquitin-protein ligase that mediates ubiquitination and subsequent proteasomal degradation of target proteins. E3 ubiquitin ligases accept ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfers the ubiquitin to targeted substrates. Involved in JUN ubiquitination and degradation. Directly involved in p53 (TP53) ubiquitination and degradation, thereby abolishing p53-dependent transcription and apoptosis. Ubiquitinates p53 independently of …

**Summary**, from NCBI Gene [64326](https://www.ncbi.nlm.nih.gov/gene/64326):

> Enables ubiquitin protein ligase activity. Involved in several processes, including negative regulation of fatty acid biosynthetic process; positive regulation of proteasomal ubiquitin-dependent protein catabolic process; and response to ionizing radiation. Part of Cul4A-RING E3 ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17440](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17440) · Entrez [64326](https://www.ncbi.nlm.nih.gov/gene/64326) · UniProt [Q8NHY2](https://www.uniprot.org/uniprotkb/Q8NHY2) · Ensembl [ENSG00000143207](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143207)

## Data

Gene col 6698: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6698); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6698, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6698]; `tensor/DDL_lfc|DDL_z.npy` [6698]; `embed/gene_vectors.npy` [6698]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6698 or target_col == 6698). Every well: [[COP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
