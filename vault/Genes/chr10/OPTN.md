---
symbol: "OPTN"
type: "gene"
col: 4419
ensembl_id: "ENSG00000123240"
name: "optineurin"
location: "10p13"
module: 59
arm: "+"
pooled_cpm: 194.07
n_lines_expressing: 48
n_dd_up: 14
n_dd_down: 23
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# OPTN

*optineurin* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.32× (z +7.0, q 2e-09, up in 24 of 46 measured lines) ⚠ cell-cycle shift, explains ~18% of this change. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 1.26× (z +5.0, q 1e-04, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.582× (z -10.1, q 2e-21, down in 39 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.685× (z -7.1, q 2e-10, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYLD]] (+0.72, fdr 7e-06), [[SWAP70]] (+0.68, fdr 7e-06), [[KMT2A]] (+0.67, fdr 7e-06); moves opposite to [[MRPS27]] (-0.64, fdr 7e-06), [[HMBS]] (-0.64, fdr 7e-06), [[EIPR1]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GBP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4419.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.32×** | +7.0 | 2e-09 | 24/46 (SW1417, RKO, …) | inconsistent across doses | composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.35×** | +5.8 | 2e-06 | 31/48 (NCI-H596, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.26×** | +5.0 | 1e-04 | 27/46 (A-427, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +4.9 | 1e-04 | 26/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 8e-04 | 26/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +4.4 | 9e-04 | 26/45 (hTERT-HPNE, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.26×** | +4.3 | 0.002 | 22/46 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.20×** | +4.1 | 0.003 | 21/46 (MIA PaCa-2, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.26×** | +4.0 | 0.003 | 26/46 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.22×** | +3.8 | 0.008 | 20/47 (NCI-H2030, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.019 | 28/48 (J82, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.037 | 15/46 (SNU-423, A498, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.040 | 22/46 (MIA PaCa-2, LoVo, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.050 | 21/46 (HOP62, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Resveratrol (drug)]] 5 µM |  | 1.14× | +3.2 | 0.057 | 8/47 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.1 | 0.058 | 12/46 (RPMI-7951, A-427, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | 1.18× | +3.0 | 0.069 | 14/46 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Alpelisib (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.084 | 22/45 (MIA PaCa-2, AsPC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4419.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.582×** | -10.1 | 2e-21 | 39/46 (MIA PaCa-2, NCI-H1792, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.652×** | -7.7 | 5e-12 | 32/45 (KATO III, HT-29, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.680×** | -7.2 | 1e-10 | 29/46 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.685×** | -7.1 | 2e-10 | 35/46 (MIA PaCa-2, HT-29, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.736×** | -5.3 | 1e-05 | 29/46 (HT-29, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.779×** | -4.6 | 3e-04 | 28/46 (HT-29, A549, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.780×** | -4.6 | 3e-04 | 28/46 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.629×** | -4.5 | 4e-04 | 32/43 (HepG2/C3A, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.773×** | -4.5 | 4e-04 | 26/45 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.786×** | -4.5 | 4e-04 | 29/46 (A549, NCI-H1792, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.633×** | -4.5 | 4e-04 | 25/47 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.831×** | -4.5 | 4e-04 | 22/47 (NCI-H1792, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.794×** | -4.3 | 8e-04 | 26/46 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.665×** | -4.0 | 0.003 | 24/46 (MIA PaCa-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.677×** | -3.8 | 0.005 | 23/46 (NCI-H2347, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.826×** | -3.6 | 0.012 | 22/46 (NCI-H460, A549, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.826×** | -3.6 | 0.012 | 21/46 (NCI-H460, BT-474, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.697×** | -3.5 | 0.012 | 23/46 (MIA PaCa-2, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Cilostazol (drug)]] 5 µM |  | **0.828×** | -3.4 | 0.021 | 18/46 (RKO, BT-474, …) | top dose only | position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | 0.840× | -3.2 | 0.030 | 17/46 (A549, NCI-H460, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.784×** | -3.2 | 0.031 | 18/46 (HEC-1-A, LoVo, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.720×** | -3.2 | 0.032 | 23/46 (AsPC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.843× | -3.2 | 0.035 | 20/46 (NCI-H460, A549, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4419. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 509 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -14.2) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.245× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 407 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -14.5) ⚠ cell-cycle shift, explains ~18% of this change |
| [[A549 (line)]] | wt | 294 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.406× (z -12.2) ⚠ unreliable plate only · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.465× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 433 | 0 | 5 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.363× (z -13.2) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 198 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.403× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~44% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.403× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 210 | 0 | 5 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.240× (z -17.6) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.422× (z -10.6) |
| [[J82 (line)]] | alt | 231 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.0) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[NCI-H596 (line)]] | alt | 147 | 2 (1 ⚠) | 1 | [[Fulvestrant (drug)]] 5 µM 2.39× (z +9.2) | [[Atazanavir (sulfate) (drug)]] 5 µM 0.154× (z -19.7) |
| [[Panc 03.27 (line)]] | alt | 265 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.462× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[A-427 (line)]] | wt | 76.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.49× (z +14.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[BT-474 (line)]] | alt | 105 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +11.8) ⚠ cell-cycle shift, explains ~18% of this change | [[Dinaciclib (drug)]] 5 µM 0.354× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 115 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.317× (z -9.1) ⚠ cell-cycle shift, explains ~84% of this change |
| [[Hs 766T (line)]] | wt | 299 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -9.3) ⚠ cell-cycle shift, explains ~70% of this change |
| [[KATO III (line)]] | alt | 107 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.0) ⚠ cell-cycle shift, explains ~18% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.332× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[NCI-H2030 (line)]] | alt | 173 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +11.3) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 125 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +11.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 155 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +12.7) ⚠ cell-cycle shift, explains ~18% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.426× (z -8.7) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 176 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +14.4) ⚠ cell-cycle shift, explains ~18% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.448× (z -10.3) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 408 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.509× (z -8.8) ⚠ cell-cycle shift, explains ~84% of this change |
| [[CHP-212 (line)]] | wt | 161 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.6) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[HEC-1-A (line)]] | alt | 210 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.519× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 283 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.246× (z -9.8) ⚠ toxic |
| [[LoVo (line)]] | wt | 165 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.437× (z -11.0) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 127 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.449× (z -8.6) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 67.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.0) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[SW 1271 (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.337× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.449× (z -9.9) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 295 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 178 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 48.0 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 239 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 231 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 301 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.8 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 478 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 76.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4419), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYLD]] | +0.72 | +0.73 / +0.73 | both halves | 7e-06 | pathway: Death Receptor Signaling; STRING 938 |
| [[SWAP70]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[KMT2A]] | +0.67 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[PIK3IP1]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[RRAGC]] | +0.66 | +0.71 / +0.62 | both halves | 7e-06 | pathway: Autophagy |
| [[NUB1]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[SLC41A2]] | +0.65 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[LACTB]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[HLA-E]] | +0.65 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[SKAP2]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[GABARAP]] ⚠ | +0.62 | +0.60 / +0.61 | both halves | 7e-06 | pathway: Autophagy; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[DAAM1]] | +0.61 | +0.65 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[NEU1]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS27]] | -0.64 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[HMBS]] | -0.64 | -0.64 / -0.60 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM |
| [[EIPR1]] | -0.63 | -0.67 / -0.61 | both halves | 7e-06 |  |
| [[WDR4]] | -0.62 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[TBRG4]] | -0.62 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[SNRPD1]] | -0.61 | -0.68 / -0.57 | both halves | 1e-05 |  |
| [[NOP2]] | -0.61 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[ALG8]] | -0.59 | -0.64 / -0.58 | both halves | 8e-06 |  |
| [[URB1]] | -0.59 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[DHX33]] | -0.58 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[POLR1A]] | -0.58 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[TOMM40]] | -0.57 | -0.63 / -0.49 | both halves | 1e-05 | pathway: Autophagy; STRING 515 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP2]] | B | GBP2 activity raises OPTN's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 1.94× lower at baseline in the lines without GBP2 | 0.039 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers OPTN's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-0.4, -37.9); signed map (-9.7, 13.2). **Vector** length 157, 56.3% of its response variance represented; |z| ≥ 3 in 1,505 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +7.7 | +5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +7.3 | +5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +7.2 | +7.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +6.4 | +4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.4 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +5.8 | +4.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +5.7 | +4.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.4 | -10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -7.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.6 | -4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | -5.2 | -7.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.1 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.5 | -4.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.4 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | optineurin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:13,099,449-13,138,308 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FIP2, HYPL, FIP-2, TFIIIA-INTP, NRP, HIP7; previously GLC1E |
| Gene groups (HGNC) | Zinc fingers C2HC NEMO-type |
| Hallmark sets | BILE_ACID_METABOLISM, HEME_METABOLISM |
| Reactome | 29 pathways, smallest: Regulation of TBK1, IKKε-mediated activation of IRF3, IRF7 upon TLR3 ligation; Regulation of TBK1, IKKε (IKBKE)-mediated activation of IRF3, IRF7; TICAM1-dependent activation of IRF3/IRF7 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CV9](https://www.uniprot.org/uniprotkb/Q96CV9) (Optineurin):

> Plays an important role in the maintenance of the Golgi complex, in membrane trafficking, in exocytosis, through its interaction with myosin VI and Rab8. Links myosin VI to the Golgi complex and plays an important role in Golgi ribbon formation. Plays a role in the activation of innate immune response during viral infection. Mechanistically, recruits TBK1 at the Golgi apparatus, promoting its trans-phosphorylation after RLR or TLR3 stimulation. In turn, activated TBK1 phosphorylates its …

**Summary**, from NCBI Gene [10133](https://www.ncbi.nlm.nih.gov/gene/10133):

> This gene encodes the coiled-coil containing protein optineurin. Optineurin may play a role in normal-tension glaucoma and adult-onset primary open angle glaucoma. Optineurin interacts with adenovirus E3-14.7K protein and may utilize tumor necrosis factor-alpha or Fas-ligand pathways to mediate apoptosis, inflammation or vasoconstriction. Optineurin may also function in cellular morphogenesis and membrane trafficking, vesicle trafficking, and transcription activation through its interactions …

**Accessions** — [HGNC:17142](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17142) · Entrez [10133](https://www.ncbi.nlm.nih.gov/gene/10133) · UniProt [Q96CV9](https://www.uniprot.org/uniprotkb/Q96CV9) · Ensembl [ENSG00000123240](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123240)

## Data

Gene col 4419: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4419); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4419, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4419]; `tensor/DDL_lfc|DDL_z.npy` [4419]; `embed/gene_vectors.npy` [4419]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4419 or target_col == 4419). Every well: [[OPTN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OPTN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
