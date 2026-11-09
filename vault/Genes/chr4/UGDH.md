---
symbol: "UGDH"
type: "gene"
col: 3085
ensembl_id: "ENSG00000109814"
name: "UDP-glucose 6-dehydrogenase"
location: "4p14"
module: 38
arm: "+"
pooled_cpm: 116.63
n_lines_expressing: 47
n_dd_up: 11
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# UGDH

*UDP-glucose 6-dehydrogenase* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.10× (z +17.5, q 0e+00, up in 33 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.98× (z +16.1, q 0e+00, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.453× (z -18.7, q 0e+00, down in 35 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGD]] (+0.53, fdr 2e-05), [[USO1]] (+0.52, fdr 2e-05), [[LINC00571]] (+0.50, fdr 6e-05); moves opposite to [[IMMP1L]] (-0.51, fdr 3e-05), [[NR2C1]] (-0.48, fdr 2e-04), [[SCML2]] (-0.45, fdr 2e-04).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FBXW10B]] → it (grade B ⚠); 2 go from it, the strongest it → [[IMMP1L]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3085.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +17.5 | 0e+00 | 33/45 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.98×** | +16.1 | 0e+00 | 41/45 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +15.7 | 0e+00 | 27/38 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +9.0 | 4e-17 | 21/42 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +8.0 | 1e-13 | 26/44 (NCI-H1573, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.91×** | +8.0 | 1e-13 | 33/45 (HS-578T, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.69×** | +6.4 | 1e-08 | 29/42 (HS-578T, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.17× | +5.3 | 7e-06 | 20/45 (hTERT-HPNE, SNU-423, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.23×** | +5.0 | 4e-05 | 23/45 (hTERT-HPNE, NCI-H1792, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.24×** | +4.9 | 5e-05 | 22/45 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +4.8 | 1e-04 | 22/45 (Hs 766T, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.21×** | +4.4 | 5e-04 | 22/44 (SW48, hTERT-HPNE, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +4.1 | 0.002 | 14/45 (SW48, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.002 | 18/45 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.18× | +4.0 | 0.002 | 13/46 (C-33 A, A549, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.008 | 13/45 (HT-29, HepG2/C3A, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.11× | +3.6 | 0.010 | 8/45 (COLO 205, SW1417, …) | rises with dose |  |
| [[Gefitinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.055 | 11/45 (NCI-H1573, RKO, …) | top dose only |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.09× | +3.0 | 0.071 | 7/46 (MIA PaCa-2, AsPC-1, …) | top dose only |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.09× | +3.0 | 0.071 | 5/46 (HS-578T, RPMI-7951, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.13× | +2.9 | 0.072 | 19/44 (SW48, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Cyclosporin A (drug)]] 5 µM |  | 1.13× | +2.9 | 0.072 | 11/45 (BT-474, SW1417, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.14× | +2.8 | 0.096 | 13/44 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 5 µM |  | 1.09× | +2.8 | 0.096 | 7/46 (CFPAC-1, HS-578T, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 1.13× | +2.8 | 0.099 | 6/46 (CFPAC-1, COLO 205, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3085.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.453×** | -18.7 | 0e+00 | 35/45 (HT-29, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.494×** | -16.7 | 0e+00 | 36/45 (HT-29, SW 900, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.533×** | -14.9 | 0e+00 | 37/45 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.708×** | -11.5 | 1e-28 | 34/45 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.642×** | -10.5 | 1e-23 | 32/45 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.548×** | -7.4 | 1e-11 | 30/46 (AsPC-1, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.744×** | -6.7 | 1e-09 | 29/44 (HS-578T, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.771×** | -6.2 | 5e-08 | 27/46 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.775×** | -6.0 | 1e-07 | 23/45 (NCI-H2347, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -5.2 | 1e-05 | 22/45 (SW48, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.804×** | -5.2 | 1e-05 | 23/45 (HS-578T, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.819×** | -4.7 | 1e-04 | 21/45 (HT-29, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.877× | -4.4 | 5e-04 | 15/45 (AsPC-1, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | 0.840× | -4.1 | 0.002 | 20/45 (HT-29, BT-474, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.846× | -3.9 | 0.003 | 17/45 (SW48, A-172, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.842× | -3.9 | 0.003 | 15/44 (SK-MEL-2, RKO, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.895× | -3.7 | 0.006 | 6/45 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.844× | -3.7 | 0.006 | 17/44 (LoVo, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Bentamapimod (drug)]] 0.05 µM |  | 0.851× | -3.6 | 0.008 | 9/44 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3085. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 202 | 7 (5 ⚠) | 7 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.70× (z +11.1) | [[Tucidinostat (drug)]] 5 µM 0.403× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 140 | 10 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 2.25× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.316× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 276 | 1 | 10 (4 ⚠) | [[Auranofin (drug)]] 5 µM 1.92× (z +8.9) | [[Tucidinostat (drug)]] 5 µM 0.416× (z -16.8) |
| [[A498 (line)]] | wt | 265 | 5 (4 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +14.6) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.32× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.441× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 103 | 9 (8 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 8.43× (z +22.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 3.19× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 177 | 2 (1 ⚠) | 7 (5 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 5.63× (z +12.6) | [[Selinexor (drug)]] 5 µM 0.218× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.275× (z -8.9) |
| [[HT-29 (line)]] | alt | 196 | 1 | 7 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.16× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.238× (z -15.9) |
| [[hTERT-HPNE (line)]] | wt | 96.3 | 5 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +20.5) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.26× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.325× (z -10.4) |
| [[SW480 (line)]] | alt | 66.9 | 5 (4 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 3.32× (z +14.8) | [[Panobinostat (drug)]] 0.5 µM 0.453× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 136 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +8.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.419× (z -10.4) |
| [[A549 (line)]] | wt | 114 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.04× (z +16.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 3.17× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 101 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.287× (z -13.0) |
| [[CFPAC-1 (line)]] | alt | 239 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -12.4) |
| [[LoVo (line)]] | wt | 139 | 1 | 3 | [[Auranofin (drug)]] 5 µM 3.64× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 230 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.23× (z +13.1) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 266 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.261× (z -15.2) |
| [[AsPC-1 (line)]] | alt | 142 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.363× (z -11.2) |
| [[C-33 A (line)]] | alt | 44.2 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.86× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 52.5 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.56× (z +13.0) | — |
| [[HepG2_C3A (line)]] | wt | 243 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.359× (z -11.0) |
| [[SNU-423 (line)]] | alt | 76.6 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +18.0) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.52× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.367× (z -9.6) |
| [[BT-474 (line)]] | alt | 124 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 37.2 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.18× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 158 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 54.4 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.94× (z +13.3) | [[Tucidinostat (drug)]] 5 µM 0.519× (z -8.8) |
| [[PANC-1 (line)]] | alt | 71.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.92× (z +13.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 53.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -11.7) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.354× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 60.5 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.02× (z +8.8) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 67.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.420× (z -9.1) |
| [[H4 (line)]] | wt | 101 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.297× (z -10.1) |
| [[HCT15 (line)]] | alt | 195 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -8.8) ⚠ cell-cycle shift, explains ~11% of this change |
| [[Hs 766T (line)]] | wt | 68.3 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.50× (z +8.5) | — |
| [[J82 (line)]] | alt | 37.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +8.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 133 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.422× (z -8.8) |
| [[LS 180 (line)]] | wt | 81.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.23× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 65.9 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.629× (z -11.7) ⚠ position not correctable |
| [[NCI-H23 (line)]] | alt | 45.0 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.659× (z -10.3) ⚠ position not correctable |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.121× (z -10.4) ⚠ cell-cycle shift, explains ~85% of this change |
| [[SNU-1 (line)]] | wt | 49.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 27.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 96.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 86.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3085), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGD]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 | same gene group; pathway: HALLMARK_XENOBIOTIC_METABOLISM; STRING 597 |
| [[USO1]] | +0.52 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[LINC00571]] | +0.50 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[C6orf62]] | +0.49 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[MC1R]] | +0.49 | +0.27 / +0.57 | both halves | 3e-04 |  |
| [[UBE2J1]] | +0.49 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[NECAB2]] | +0.49 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[DESI1]] | +0.48 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[MIR22HG]] | +0.48 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[PXDC1]] | +0.47 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[PTOV1-AS1]] | +0.47 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[SLC7A11]] | +0.47 | +0.42 / +0.49 | both halves | 4e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMMP1L]] | -0.51 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[NR2C1]] | -0.48 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[SCML2]] | -0.45 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[LSM2]] | -0.45 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[GLMN]] | -0.45 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[DENND6A]] | -0.44 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[ABHD6]] | -0.44 | -0.34 / -0.40 | both halves | 1e-04 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[FBXL5]] | -0.43 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[HDHD5]] | -0.43 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[RSAD1]] | -0.43 | -0.21 / -0.51 | both halves | 6e-04 |  |
| [[CENPW]] | -0.43 | -0.32 / -0.34 | both halves | 1e-04 |  |
| [[MRPL39]] | -0.43 | -0.25 / -0.46 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXW10B]] | B | FBXW10B activity raises UGDH's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 1.87× lower at baseline in the lines without FBXW10B | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[NTN4]] | B | NTN4 activity raises UGDH's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 1.75× lower at baseline in the lines without NTN4 | 0.077 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[LINC01564]] | B | LINC01564 activity raises UGDH's level | lines that do not express LINC01564 (24) vs lines expressing it (26) | 1.91× lower at baseline in the lines without LINC01564 | 0.085 | ⚠ within organs, on part of the lines; also absent: LINC03040, INAVA, CYP4F11; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises UGDH's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises UGDH's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IMMP1L]] | C | UGDH activity lowers IMMP1L's level | lines that do not express UGDH (3) vs lines expressing it (47) | 1.40× higher at baseline in the lines without UGDH | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, PYGB, TIMP1; maybe low, not absent; its own permutation p |
| [[PITX1-AS1]] | C | UGDH activity lowers PITX1-AS1's level | lines that do not express UGDH (3) vs lines expressing it (47) | 1.46× higher at baseline in the lines without UGDH | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, PYGB, TIMP1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.322). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.3, -26.6); signed map (16.2, -3.4). **Vector** length 127, 37.1% of its response variance represented; |z| ≥ 3 in 1,566 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.9 | +16.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +15.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +17.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.9 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +6.8 | +5.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.2 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +1.0 |
|  | [[RMC-6236 (drug)]] 5 µM |  | +3.1 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +8.0 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -5.7 | -4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.3 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.2 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -11.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | -3.9 | -6.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -7.4 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | -2.6 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | UDP-glucose 6-dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:39,498,755-39,528,311 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GDH, UDPGDH, UDP-GlcDH, UGD |
| Gene groups (HGNC) | Oxidoreductases |
| Hallmark sets | FATTY_ACID_METABOLISM, XENOBIOTIC_METABOLISM, ESTROGEN_RESPONSE_LATE |
| Reactome | 4 pathways, smallest: Formation of the active cofactor, UDP-glucuronate; Glucuronidation; Phase II - Conjugation of compounds |
| Matched by | ensembl_id |

**Function**, from UniProt [O60701](https://www.uniprot.org/uniprotkb/O60701) (UDP-glucose 6-dehydrogenase):

> Catalyzes the formation of UDP-alpha-D-glucuronate, a constituent of complex glycosaminoglycans. Required for the biosynthesis of chondroitin sulfate and heparan sulfate. Required for embryonic development via its role in the biosynthesis of glycosaminoglycans (By similarity). Required for proper brain and neuronal development.

**Summary**, from NCBI Gene [7358](https://www.ncbi.nlm.nih.gov/gene/7358):

> The protein encoded by this gene converts UDP-glucose to UDP-glucuronate and thereby participates in the biosynthesis of glycosaminoglycans such as hyaluronan, chondroitin sulfate, and heparan sulfate. These glycosylated compounds are common components of the extracellular matrix and likely play roles in signal transduction, cell migration, and cancer growth and metastasis. The expression of this gene is up-regulated by transforming growth factor beta and down-regulated by hypoxia. Alternative …

**Accessions** — [HGNC:12525](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12525) · Entrez [7358](https://www.ncbi.nlm.nih.gov/gene/7358) · UniProt [O60701](https://www.uniprot.org/uniprotkb/O60701) · Ensembl [ENSG00000109814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109814)

## Data

Gene col 3085: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3085); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3085, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3085]; `tensor/DDL_lfc|DDL_z.npy` [3085]; `embed/gene_vectors.npy` [3085]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3085 or target_col == 3085). Every well: [[UGDH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UGDH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
