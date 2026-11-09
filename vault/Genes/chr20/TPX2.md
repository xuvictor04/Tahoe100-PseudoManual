---
symbol: "TPX2"
type: "gene"
col: 1528
ensembl_id: "ENSG00000088325"
name: "TPX2 microtubule nucleation factor"
location: "20q11.21"
module: 22
arm: "+"
pooled_cpm: 184.9
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 18
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# TPX2

*TPX2 microtubule nucleation factor* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.70× (z +10.5, q 6e-23, up in 34 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.78× (z +4.2, q 9e-04, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (14 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.544× (z -12.0, q 2e-30, down in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~90% of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.795× (z -4.5, q 4e-04, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF4A]] (+0.96, fdr 7e-06), [[BIRC5]] (+0.96, fdr 7e-06), [[TOP2A]] (+0.95, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MYBL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 20 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1528.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.70×** | +10.5 | 6e-23 | 34/48 (NCI-H2030, A549, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **2.09×** | +10.3 | 2e-22 | 43/49 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.90×** | +9.0 | 5e-17 | 44/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.95×** | +9.0 | 5e-17 | 43/48 (PANC-1, NCI-H2030, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.92×** | +8.7 | 3e-16 | 39/44 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~99% of this change | **1.75×** | +7.8 | 8e-13 | 40/48 (HT-29, SW 900, …) | all doses, flat | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.58×** | +6.4 | 1e-08 | 34/48 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.64×** | +6.4 | 1e-08 | 32/45 (A-172, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.39×** | +6.4 | 1e-08 | 39/49 (NCI-H2030, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.38×** | +6.3 | 2e-08 | 41/48 (NCI-H23, HT-29, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **2.33×** | +6.2 | 4e-08 | 36/47 (J82, C32, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~85% of this change | **1.50×** | +5.4 | 3e-06 | 37/47 (NCI-H23, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.46×** | +5.3 | 5e-06 | 34/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.43×** | +5.0 | 2e-05 | 33/48 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.42×** | +4.8 | 5e-05 | 38/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +4.2 | 9e-04 | 23/48 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.001 | 30/48 (LoVo, H4, …) | rises with dose |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.001 | 25/48 (HT-29, HEC-1-A, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.32×** | +3.9 | 0.003 | 26/47 (HOP62, LOX-IMVI, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.32×** | +3.9 | 0.003 | 29/49 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.010 | 22/48 (HOP62, SW 900, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.015 | 23/48 (HOP62, Hs 766T, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.019 | 21/47 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.019 | 22/48 (SW 900, NCI-H460, …) | all doses, flat |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.24×** | +2.9 | 0.065 | 19/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 1.16× | +2.8 | 0.089 | 7/49 (NCI-H1792, AsPC-1, …) | top dose only |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | **1.22×** | +2.8 | 0.094 | 18/48 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.22×** | +2.8 | 0.094 | 17/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1528.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.544×** | -12.0 | 2e-30 | 45/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.481×** | -10.2 | 4e-22 | 45/48 (H4, A498, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.549×** | -6.7 | 3e-09 | 38/48 (A-172, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.643×** | -6.2 | 9e-08 | 41/49 (Hs 766T, A549, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~64% of this change | **0.449×** | -5.8 | 6e-07 | 34/45 (SW48, SHP-77, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.671×** | -5.6 | 2e-06 | 30/48 (A498, H4, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.795×** | -4.5 | 4e-04 | 30/48 (HCT15, HT-29, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.732×** | -4.4 | 9e-04 | 26/49 (H4, A-172, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.752×** | -4.0 | 0.004 | 28/48 (A-172, HOP62, …) | top dose only |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.672×** | -4.0 | 0.004 | 28/48 (A-427, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.756×** | -3.9 | 0.004 | 32/48 (NCI-H2347, LOX-IMVI, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.822×** | -3.9 | 0.004 | 25/49 (H4, SNU-1, …) | two highest doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.822×** | -3.9 | 0.004 | 23/48 (A498, H4, …) | top dose only |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.758×** | -3.7 | 0.008 | 23/48 (A-172, NCI-H1573, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.697×** | -3.6 | 0.012 | 29/48 (SNU-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.844× | -3.4 | 0.025 | 23/48 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.851× | -3.2 | 0.043 | 20/49 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.856× | -3.1 | 0.056 | 19/48 (NCI-H2030, SK-MEL-2, …) | rises with dose |  |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 0.857× | -3.1 | 0.057 | 18/49 (NCI-H2347, RKO, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.858× | -3.1 | 0.058 | 20/48 (H4, A498, …) | two highest doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.859× | -3.0 | 0.060 | 14/48 (HT-29, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.809×** | -3.0 | 0.069 | 22/48 (NCI-H2030, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.847× | -2.9 | 0.083 | 18/48 (HCT15, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +1.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1528. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 157 | 4 (4 ⚠) | 7 (5 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.43× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | [[Selinexor (drug)]] 5 µM 0.284× (z -17.2) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.508× (z -9.2) |
| [[A498 (line)]] | wt | 196 | 2 (2 ⚠) | 6 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | [[Selinexor (drug)]] 5 µM 0.193× (z -24.8) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.420× (z -13.1) |
| [[H4 (line)]] | wt | 219 | 0 | 7 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.118× (z -19.7) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.273× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 174 | 1 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.220× (z -16.8) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.414× (z -9.8) |
| [[PANC-1 (line)]] | alt | 330 | 7 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +16.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 288 | 3 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +13.9) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.409× (z -13.4) ⚠ cell-cycle shift, explains ~90% of this change |
| [[A549 (line)]] | wt | 145 | 3 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +18.7) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.383× (z -12.5) ⚠ cell-cycle shift, explains ~90% of this change |
| [[SNU-1 (line)]] | wt | 213 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0755× (z -15.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 149 | 3 (2 ⚠) | 1 (1 ⚠) | [[Docetaxel (drug)]] 0.05 µM 3.52× (z +9.4) ⚠ transcription drop; cell-cycle shift, explains ~99% of this change · without an alert: [[Docetaxel (drug)]] 5 µM 2.30× (z +8.8) | [[Selinexor (drug)]] 5 µM 0.380× (z -10.3) ⚠ cell-cycle shift, explains ~90% of this change |
| [[LS 180 (line)]] | wt | 108 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.232× (z -13.3) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.339× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 219 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +18.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 195 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | [[Selinexor (drug)]] 5 µM 0.497× (z -8.7) ⚠ cell-cycle shift, explains ~90% of this change |
| [[RKO (line)]] | wt | 209 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +18.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 270 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.181× (z -24.1) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.449× (z -11.3) |
| [[C32 (line)]] | wt | 111 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.307× (z -11.5) ⚠ cell-cycle shift, explains ~90% of this change |
| [[NCI-H460 (line)]] | wt | 110 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.377× (z -13.1) ⚠ cell-cycle shift, explains ~90% of this change |
| [[Panc 03.27 (line)]] | alt | 134 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +14.4) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.386× (z -12.0) ⚠ cell-cycle shift, explains ~90% of this change |
| [[SW1417 (line)]] | alt | 333 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.547× (z -9.1) ⚠ cell-cycle shift, explains ~90% of this change |
| [[SW48 (line)]] | wt | 151 | 0 | 3 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.247× (z -10.5) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.426× (z -9.0) |
| [[HCT15 (line)]] | alt | 183 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.355× (z -10.8) ⚠ cell-cycle shift, explains ~90% of this change |
| [[HS-578T (line)]] | alt | 143 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +14.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 98.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.294× (z -11.6) ⚠ cell-cycle shift, explains ~90% of this change |
| [[J82 (line)]] | alt | 390 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 198 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.06× (z +12.5) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[LoVo (line)]] | wt | 81.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | [[Selinexor (drug)]] 5 µM 0.460× (z -9.8) ⚠ cell-cycle shift, explains ~90% of this change |
| [[AsPC-1 (line)]] | alt | 61.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CFPAC-1 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.445× (z -9.4) ⚠ cell-cycle shift, explains ~90% of this change |
| [[COLO 205 (line)]] | alt | 65.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.157× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 242 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.437× (z -9.2) ⚠ cell-cycle shift, explains ~90% of this change |
| [[MIA PaCa-2 (line)]] | alt | 196 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | — |
| [[NCI-H1792 (line)]] | alt | 73.5 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.37× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 191 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +12.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 242 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 207 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.386× (z -12.5) ⚠ cell-cycle shift, explains ~90% of this change |
| [[SNU-423 (line)]] | alt | 168 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 144 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW480 (line)]] | alt | 221 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | — |
| [[AN3 CA (line)]] | alt | 285 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 164 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 97.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 176 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 60.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 352 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1528), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF4A]] | +0.96 | +0.96 / +0.96 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 965 |
| [[BIRC5]] | +0.96 | +0.94 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 952 |
| [[TOP2A]] | +0.95 | +0.96 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 942 |
| [[KIF11]] | +0.94 | +0.95 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 965 |
| [[DLGAP5]] | +0.94 | +0.93 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 978 |
| [[PRC1]] | +0.94 | +0.95 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 999 |
| [[MKI67]] | +0.94 | +0.92 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 954 |
| [[KIF23]] | +0.94 | +0.93 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 906 |
| [[NCAPG]] | +0.93 | +0.93 / +0.92 | both halves | 7e-06 | STRING 949 |
| [[ARHGAP11A]] | +0.93 | +0.93 / +0.91 | both halves | 7e-06 | STRING 553 |
| [[BUB1]] | +0.93 | +0.92 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 958 |
| [[NDC80]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 788 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYBL1]] | B | MYBL1 activity raises TPX2's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.90× lower at baseline in the lines without MYBL1 | 0.014 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[PIMREG]] | B | PIMREG activity raises TPX2's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.33× lower at baseline in the lines without PIMREG | 0.021 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[FAM72B]] | B | FAM72B activity raises TPX2's level | lines that do not express FAM72B (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without FAM72B | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC02798, SRGAP2C, ZNF512B; its own permutation p |
| [[AURKB]] | C | AURKB activity raises TPX2's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.72× lower at baseline in the lines without AURKB | 0.020 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises TPX2's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.80× lower at baseline in the lines without PBK | 0.023 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[DIAPH3]] | C | DIAPH3 activity raises TPX2's level | lines that do not express DIAPH3 (3) vs lines expressing it (47) | 2.81× lower at baseline in the lines without DIAPH3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises TPX2's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.68× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[SKA3]] | C | SKA3 activity raises TPX2's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 2.58× lower at baseline in the lines without SKA3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.969). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.6, -55.4); signed map (-49.3, -43.5). **Vector** length 161, 71.6% of its response variance represented; |z| ≥ 3 in 1,685 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitotic Prometaphase* (reactome, mean cos +0.75 to 48); *E2F targets* (hallmark, mean cos +0.75 to 46); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.75 to 41).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.4 | +10.5 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | +5.9 | +6.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +5.5 | +6.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.5 | +9.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~99% of this change | +4.4 | +7.8 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.4 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +3.1 | +3.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.9 | +3.4 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +2.8 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | -0.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | -10.2 | -12.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | -10.0 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -9.1 | -4.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -9.0 | -10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.8 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.7 | -1.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | -5.0 | -3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.2 | -2.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.7 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | TPX2 microtubule nucleation factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21 — chr20:31,739,271-31,801,805 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p100, DIL-2, HCA519, FLS353; previously C20orf2, C20orf1 |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 8 pathways, smallest: AURKA Activation by TPX2; Regulation of TP53 Activity through Phosphorylation; Regulation of TP53 Activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULW0](https://www.uniprot.org/uniprotkb/Q9ULW0) (Targeting protein for Xklp2):

> Spindle assembly factor required for normal assembly of mitotic spindles. Required for normal assembly of microtubules during apoptosis. Required for chromatin and/or kinetochore dependent microtubule nucleation. Mediates AURKA localization to spindle microtubules. Activates AURKA by promoting its autophosphorylation at 'Thr-288' and protects this residue against dephosphorylation. TPX2 is inactivated upon binding to importin-alpha. At the onset of mitosis, GOLGA2 interacts with importin-alpha, …

**Summary**, from NCBI Gene [22974](https://www.ncbi.nlm.nih.gov/gene/22974):

> Enables several functions, including importin-alpha family protein binding activity; protein kinase binding activity; and protein serine/threonine kinase activator activity. Involved in activation of protein kinase activity; microtubule cytoskeleton organization; and negative regulation of microtubule depolymerization. Located in intercellular bridge; nucleoplasm; and spindle. Is active in spindle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:1249](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1249) · Entrez [22974](https://www.ncbi.nlm.nih.gov/gene/22974) · UniProt [Q9ULW0](https://www.uniprot.org/uniprotkb/Q9ULW0) · Ensembl [ENSG00000088325](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088325)

## Data

Gene col 1528: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1528); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1528, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1528]; `tensor/DDL_lfc|DDL_z.npy` [1528]; `embed/gene_vectors.npy` [1528]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1528 or target_col == 1528). Every well: [[TPX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
