---
symbol: "NPEPPS"
type: "gene"
col: 6498
ensembl_id: "ENSG00000141279"
name: "aminopeptidase puromycin sensitive"
location: "17q21.32"
module: 169
arm: "+"
pooled_cpm: 301.37
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 19
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# NPEPPS

*aminopeptidase puromycin sensitive* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.69× (z +10.3, q 3e-22, up in 41 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.57× (z +8.9, q 2e-16, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.558× (z -16.2, q 0e+00, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIAS1]] (+0.72, fdr 7e-06), [[STK38]] (+0.72, fdr 1e-05), [[AMBRA1]] (+0.64, fdr 7e-06); moves opposite to [[DCTD]] (-0.68, fdr 3e-05), [[ZNF121]] (-0.64, fdr 9e-06), [[THOC6]] (-0.62, fdr 2e-05).
> It is in [[Module 169]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[WFDC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6498.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +10.3 | 3e-22 | 41/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +8.9 | 2e-16 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.98×** | +7.0 | 4e-10 | 39/48 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +6.5 | 1e-08 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +6.2 | 6e-08 | 38/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.33×** | +5.4 | 7e-06 | 39/49 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +5.1 | 3e-05 | 27/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +5.0 | 3e-05 | 25/48 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +5.0 | 4e-05 | 29/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.6 | 3e-04 | 30/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.26×** | +4.4 | 5e-04 | 34/48 (PANC-1, MIA PaCa-2, …) | rises with dose | plate-row cell shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.009 | 21/47 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.20× | +3.6 | 0.014 | 21/50 (A-427, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.6 | 0.014 | 23/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Fumaric acid (drug)]] 5 µM |  | 1.19× | +3.2 | 0.044 | 17/49 (CFPAC-1, HepG2/C3A, …) | top dose only | plate-row cell shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.067 | 16/49 (LoVo, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6498.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.558×** | -16.2 | 0e+00 | 35/48 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.462×** | -15.2 | 0e+00 | 46/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.465×** | -15.1 | 0e+00 | 47/48 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.598×** | -14.3 | 4e-44 | 38/49 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.556×** | -11.6 | 8e-29 | 44/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.564×** | -10.8 | 2e-25 | 36/44 (CFPAC-1, Panc 03.27, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.578×** | -10.8 | 4e-25 | 42/49 (CFPAC-1, Panc 03.27, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.557×** | -10.6 | 1e-24 | 35/45 (CFPAC-1, NCI-H2347, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.570×** | -10.6 | 1e-24 | 45/47 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.609×** | -9.8 | 1e-20 | 40/48 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.673×** | -7.8 | 4e-13 | 40/48 (Panc 03.27, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.715×** | -6.6 | 3e-09 | 39/48 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.731×** | -6.1 | 4e-08 | 37/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.738×** | -5.7 | 4e-07 | 33/48 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -4.9 | 4e-05 | 21/48 (NCI-H2347, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **0.791×** | -4.6 | 2e-04 | 28/48 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.855× | -4.3 | 5e-04 | 23/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.694×** | -3.7 | 0.005 | 29/49 (CFPAC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.832×** | -3.6 | 0.009 | 22/48 (CFPAC-1, SW 900, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.887× | -3.3 | 0.021 | 14/48 (CFPAC-1, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6498. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 819 | 0 | 19 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -29.5) |
| [[NCI-H2347 (line)]] | alt | 801 | 0 | 15 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.252× (z -19.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.383× (z -19.4) |
| [[Panc 03.27 (line)]] | alt | 693 | 0 | 15 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -24.7) |
| [[NCI-H1792 (line)]] | alt | 350 | 2 (1 ⚠) | 10 (7 ⚠) | [[Digitoxin (drug)]] 5 µM 2.47× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -26.2) |
| [[SW480 (line)]] | alt | 251 | 6 (1 ⚠) | 6 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 2.22× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -14.7) |
| [[Hs 766T (line)]] | wt | 328 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -18.8) |
| [[NCI-H460 (line)]] | wt | 267 | 6 (3 ⚠) | 4 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 3.37× (z +16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +13.9) | [[Panobinostat (drug)]] 0.5 µM 0.426× (z -11.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.633× (z -8.7) |
| [[PANC-1 (line)]] | alt | 166 | 10 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +17.7) | — |
| [[SW1417 (line)]] | alt | 361 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.328× (z -17.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -15.2) |
| [[COLO 205 (line)]] | alt | 395 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -30.9) |
| [[HCT15 (line)]] | alt | 402 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -19.3) |
| [[KATO III (line)]] | alt | 360 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -18.9) |
| [[LoVo (line)]] | wt | 224 | 3 (2 ⚠) | 6 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.18× (z +12.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -23.6) |
| [[AsPC-1 (line)]] | alt | 316 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -19.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.388× (z -17.4) |
| [[HEC-1-A (line)]] | alt | 352 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -15.8) |
| [[J82 (line)]] | alt | 269 | 2 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 157 | 1 (1 ⚠) | 7 (5 ⚠) | [[Lonafarnib (drug)]] 5 µM 3.95× (z +9.4) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -15.8) |
| [[SK-MEL-2 (line)]] | alt | 252 | 1 | 7 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 3.17× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.433× (z -11.8) |
| [[SNU-423 (line)]] | alt | 381 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -16.0) |
| [[SW 900 (line)]] | alt | 343 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -13.9) |
| [[HOP62 (line)]] | alt | 311 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.324× (z -12.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.484× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 208 | 5 (2 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.41× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.394× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 339 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -14.8) |
| [[HT-29 (line)]] | alt | 257 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -15.7) |
| [[LS 180 (line)]] | wt | 211 | 1 (1 ⚠) | 4 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 1.98× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -15.2) |
| [[A549 (line)]] | wt | 284 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.322× (z -15.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -14.9) |
| [[BT-474 (line)]] | alt | 173 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.432× (z -11.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -10.4) |
| [[HS-578T (line)]] | alt | 261 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 258 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -14.1) |
| [[A-172 (line)]] | wt | 219 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -11.4) |
| [[C-33 A (line)]] | alt | 171 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.56× (z +10.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +9.1) | — |
| [[C32 (line)]] | wt | 262 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -14.0) |
| [[CHP-212 (line)]] | wt | 520 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HepG2_C3A (line)]] | wt | 236 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -11.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LOX-IMVI (line)]] | wt | 171 | 1 | 2 | [[TAK-901 (drug)]] 0.05 µM 2.04× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 206 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -10.4) |
| [[A-427 (line)]] | wt | 213 | 1 (1 ⚠) | 1 (1 ⚠) | [[Trametinib (drug)]] 5 µM 1.96× (z +10.0) ⚠ cell-cycle shift, explains ~37% of this change | [[Dinaciclib (drug)]] 5 µM 0.546× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[RKO (line)]] | wt | 202 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.16× (z +9.2) ⚠ toxic | — |
| [[A498 (line)]] | wt | 247 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.450× (z -9.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-1 (line)]] | wt | 172 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -9.4) |
| [[AN3 CA (line)]] | alt | 203 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 194 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 566 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 303 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 290 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6498), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIAS1]] | +0.72 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[STK38]] | +0.72 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[AMBRA1]] | +0.64 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[RELCH]] | +0.64 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[SEC24B]] | +0.62 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[DCAF5]] | +0.60 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[TBC1D12]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[CRYZL1]] | +0.60 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[RAB6A]] | +0.60 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[GTF2IP4]] | +0.59 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[PLEKHH3]] | +0.59 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[RNF149]] | +0.59 | +0.69 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTD]] | -0.68 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[ZNF121]] | -0.64 | -0.65 / -0.57 | both halves | 9e-06 |  |
| [[THOC6]] | -0.62 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[MYSM1]] | -0.60 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[SPRY2]] | -0.60 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[CYP27B1]] | -0.60 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[SERPINB8]] | -0.59 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[CCND1]] | -0.59 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[REXO1]] | -0.58 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[MCL1]] | -0.57 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[ERCC1]] | -0.57 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[AGO2]] | -0.57 | -0.57 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WFDC2]] | B | WFDC2 activity raises NPEPPS's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 1.71× lower at baseline in the lines without WFDC2 | 0.002 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[WFDC2]] | B | WFDC2 activity strengthens NPEPPS's drug response | lines that do not express WFDC2 (38) vs lines expressing it (11) | the lines without WFDC2 respond 0.75× as strongly (z diff +1.75); strongest at Homoharringtonine 5 µM: 0.65x vs 0.39x (z diff +4.0) | 0.045 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; target measured in part of the lines; artifact flags |
| [[CCL28]] | B | CCL28 activity raises NPEPPS's level | lines that do not express CCL28 (24) vs lines expressing it (26) | 1.33× lower at baseline in the lines without CCL28 | 0.067 | ⚠ within organs, on part of the lines; also absent: SHROOM4, LINC02432, CD74 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.9, -33.1); signed map (-29.4, 10.3). **Vector** length 120, 50.0% of its response variance represented; |z| ≥ 3 in 1,640 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +7.5 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.9 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +6.8 | +2.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +6.7 | +3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +6.4 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +6.1 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.8 | -9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -16.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -7.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.6 | -2.4 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -3.0 | -0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.8 | -4.6 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -2.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | aminopeptidase puromycin sensitive |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:47,522,942-47,624,665 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PSA, MP100 |
| Gene groups (HGNC) | Aminopeptidases; M1 metallopeptidases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P55786](https://www.uniprot.org/uniprotkb/P55786) (Puromycin-sensitive aminopeptidase):

> Aminopeptidase with broad substrate specificity for several peptides. Involved in proteolytic events essential for cell growth and viability. May act as regulator of neuropeptide activity. Plays a role in the antigen-processing pathway for MHC class I molecules. Involved in the N-terminal trimming of cytotoxic T-cell epitope precursors. Digests the poly-Q peptides found in many cellular proteins. Digests tau from normal brain more efficiently than tau from Alzheimer disease brain.

**Summary**, from NCBI Gene [9520](https://www.ncbi.nlm.nih.gov/gene/9520):

> This gene encodes the puromycin-sensitive aminopeptidase, a zinc metallopeptidase which hydrolyzes amino acids from the N-terminus of its substrate. The protein has been localized to both the cytoplasm and to cellular membranes. This enzyme degrades enkaphalins in the brain, and studies in mouse suggest that it is involved in proteolytic events regulating the cell cycle. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7900](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7900) · Entrez [9520](https://www.ncbi.nlm.nih.gov/gene/9520) · UniProt [P55786](https://www.uniprot.org/uniprotkb/P55786) · Ensembl [ENSG00000141279](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141279)

## Data

Gene col 6498: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6498); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6498, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6498]; `tensor/DDL_lfc|DDL_z.npy` [6498]; `embed/gene_vectors.npy` [6498]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6498 or target_col == 6498). Every well: [[NPEPPS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPEPPS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
