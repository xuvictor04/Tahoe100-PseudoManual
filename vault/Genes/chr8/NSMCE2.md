---
symbol: "NSMCE2"
type: "gene"
col: 8016
ensembl_id: "ENSG00000156831"
name: "NSE2 SUMO ligase component of SMC5/6 complex"
location: "8q24.13"
module: 185
arm: "+"
pooled_cpm: 250.32
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/185"]
generated_by: "tahoemap"
---

# NSMCE2

*NSE2 SUMO ligase component of SMC5/6 complex* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.62× (z +9.1, q 5e-17, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.559× (z -10.5, q 3e-23, down in 45 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.838× (z -4.7, q 1e-04, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 6 lines (RKO 0.222×, NCI-H2030 0.206×, MIA PaCa-2 0.291×, SW1417 0.284×, …; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 3 lines (HCT15 0.228×, KATO III 0.319×, NCI-H23 0.341×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HT-29 0.303×, LoVo 0.385×, C32 0.315×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.455×); [[PH-797804 (drug)]] 5 µM in 1 line (C32 0.272×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC38A7]] (+0.66, fdr 7e-06), [[VPS13B]] (+0.65, fdr 7e-06), [[ZFYVE26]] (+0.60, fdr 7e-06); moves opposite to [[SLC25A30]] (-0.47, fdr 9e-05), [[DDHD2]] (-0.47, fdr 5e-05), [[GLUD1]] (-0.46, fdr 1e-04).
> It is in [[Module 185]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8016.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +9.1 | 5e-17 | 42/48 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +6.6 | 1e-08 | 26/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +6.0 | 3e-07 | 36/48 (CFPAC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +6.0 | 3e-07 | 40/48 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +4.8 | 2e-04 | 25/48 (Hs 766T, SW1417, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.50×** | +4.0 | 0.006 | 37/50 (NCI-H1573, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.7 | 0.018 | 26/48 (PANC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.022 | 20/49 (NCI-H1573, RPMI-7951, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.022 | 26/48 (PANC-1, LoVo, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +3.5 | 0.028 | 10/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.20×** | +3.5 | 0.028 | 22/48 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.028 | 24/47 (AsPC-1, RKO, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.028 | 25/49 (NCI-H460, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.3 | 0.034 | 20/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.20× | +3.3 | 0.042 | 21/48 (RKO, NCI-H23, …) | top dose only |  |
| [[AZD-8055 (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.069 | 24/49 (NCI-H1573, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.072 | 10/48 (AsPC-1, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8016.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 6 lines (RKO 0.222×, NCI-H2030 0.206×, MIA PaCa-2 0.291×, SW1417 0.284×, …; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 3 lines (HCT15 0.228×, KATO III 0.319×, NCI-H23 0.341×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HT-29 0.303×, LoVo 0.385×, C32 0.315×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.455×); [[PH-797804 (drug)]] 5 µM in 1 line (C32 0.272×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.559×** | -10.5 | 3e-23 | 45/47 (RKO, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.565×** | -10.0 | 7e-21 | 40/45 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.625×** | -8.5 | 3e-15 | 38/44 (HCT15, KATO III, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.570×** | -8.5 | 3e-15 | 41/49 (NCI-H23, HT-29, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.660×** | -7.5 | 6e-12 | 40/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.715×** | -6.3 | 2e-08 | 33/48 (LS 180, SW480, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.548×** | -5.9 | 2e-07 | 29/38 (A-172, C32, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **0.730×** | -5.9 | 2e-07 | 39/48 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -4.7 | 1e-04 | 21/48 (LoVo, RKO, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.815×** | -3.9 | 0.006 | 27/49 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.815×** | -3.7 | 0.010 | 29/48 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.876× | -3.5 | 0.020 | 12/49 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8016. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 338 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -15.1) |
| [[Hs 766T (line)]] | wt | 333 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +16.8) | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -14.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 293 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -17.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 224 | 2 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.72× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.385× (z -14.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 237 | 0 | 6 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.493× (z -11.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 788 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.303× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 260 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +23.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.465× (z -11.4) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 163 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +27.4) | [[Dinaciclib (drug)]] 0.05 µM 0.487× (z -10.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 217 | 1 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.79× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.440× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 180 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -11.4) ⚠ cell-cycle shift, explains ~68% of this change |
| [[HS-578T (line)]] | alt | 297 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.459× (z -10.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 294 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.349× (z -14.4) ⚠ toxic |
| [[LS 180 (line)]] | wt | 193 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.351× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SHP-77 (line)]] | alt | 284 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.387× (z -12.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 189 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -12.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 180 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.291× (z -16.1) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 223 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -20.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 410 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.93× (z +8.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.222× (z -19.8) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 240 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -12.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 319 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 225 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 333 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.427× (z -9.6) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 168 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -9.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 171 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.5) | — |
| [[J82 (line)]] | alt | 300 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +14.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.398× (z -11.6) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 223 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.372× (z -11.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 286 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.284× (z -15.9) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 269 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -10.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 202 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +17.4) | — |
| [[CFPAC-1 (line)]] | alt | 169 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.393× (z -11.2) ⚠ toxic |
| [[HCT15 (line)]] | alt | 251 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -17.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 193 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.262× (z -10.0) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 310 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.206× (z -19.4) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 214 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 229 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 205 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +15.6) | — |
| [[SNU-1 (line)]] | wt | 181 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.330× (z -10.7) ⚠ toxic |
| [[A-427 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 199 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 189 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 163 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 208 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8016), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC38A7]] | +0.66 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[VPS13B]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ZFYVE26]] | +0.60 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[IFT43]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[KATNIP]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[CEP162]] | +0.56 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[SCAPER]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[SUMF1]] | +0.55 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[DNAJC8]] | +0.55 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[COMMD10]] | +0.55 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[XRCC4]] | +0.54 | +0.46 / +0.61 | both halves | 2e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[SFSWAP]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A30]] | -0.47 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[DDHD2]] | -0.47 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[GLUD1]] | -0.46 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[POGLUT2]] | -0.45 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[CLDND1]] | -0.44 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ZNF589]] | -0.44 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[TSPAN12]] | -0.44 | -0.21 / -0.43 | both halves | 7e-04 |  |
| [[FZD3]] | -0.44 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[CHST7]] | -0.43 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[SRP54-AS1]] | -0.43 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[ZNF710-AS1]] | -0.43 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[DGKA]] | -0.43 | -0.35 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 185]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-26.7, 29.4); signed map (-6.2, -20.4). **Vector** length 121, 46.2% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.3 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +6.3 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +3.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +4.3 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +4.8 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +1.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -12.6 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -10.7 | -3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.2 | -10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.3 | -8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.2 | -10.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.4 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.9 | -2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.4 | -1.4 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | NSE2 SUMO ligase component of SMC5/6 complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:125,091,679-125,367,120 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32440, MMS21, NSE2, ZMIZ7; previously C8orf36 |
| Gene groups (HGNC) | Zinc fingers MIZ-type; SMC5/6 complex |
| Reactome | 3 pathways, smallest: SUMOylation of DNA damage response and repair proteins; SUMO E3 ligases SUMOylate target proteins; SUMOylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MF7](https://www.uniprot.org/uniprotkb/Q96MF7) (E3 SUMO-protein ligase NSE2):

> E3 SUMO-protein ligase component of the SMC5-SMC6 complex, a complex involved in DNA double-strand break repair by homologous recombination. Is not be required for the stability of the complex. The complex may promote sister chromatid homologous recombination by recruiting the SMC1-SMC3 cohesin complex to double-strand breaks. The complex is required for telomere maintenance via recombination in ALT (alternative lengthening of telomeres) cell lines and mediates sumoylation of shelterin complex …

**Summary**, from NCBI Gene [286053](https://www.ncbi.nlm.nih.gov/gene/286053):

> This gene encodes a member of a family of E3 small ubiquitin-related modifier (SUMO) ligases that mediates the attachment of a SUMO protein to proteins involved in nuclear transport, transcription, chromosome segregation and DNA repair. The encoded protein is part of the structural maintenance of chromosomes (SMC) 5/6 complex which plays a key role genome maintenance, facilitating chromosome segregation and suppressing mitotic recombination. A knockout of the orthologous mouse gene is lethal …

**Accessions** — [HGNC:26513](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26513) · Entrez [286053](https://www.ncbi.nlm.nih.gov/gene/286053) · UniProt [Q96MF7](https://www.uniprot.org/uniprotkb/Q96MF7) · Ensembl [ENSG00000156831](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156831)

## Data

Gene col 8016: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8016); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8016, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8016]; `tensor/DDL_lfc|DDL_z.npy` [8016]; `embed/gene_vectors.npy` [8016]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8016 or target_col == 8016). Every well: [[NSMCE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSMCE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
