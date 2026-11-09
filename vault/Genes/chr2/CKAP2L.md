---
symbol: "CKAP2L"
type: "gene"
col: 9825
ensembl_id: "ENSG00000169607"
name: "cytoskeleton associated protein 2L"
location: "2q14.1"
module: 22
arm: "+"
pooled_cpm: 58.56
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 18
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CKAP2L

*cytoskeleton associated protein 2L* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.96× (z +13.5, q 7e-39, up in 36 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Mebendazole (drug)]] 5 µM: 1.35× (z +4.3, q 0.001, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.422× (z -17.2, q 0e+00, down in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~56% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.713× (z -6.7, q 2e-09, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGO1]] (+0.91, fdr 7e-06), [[NDC80]] (+0.91, fdr 7e-06), [[MKI67]] (+0.90, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9825.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.96×** | +13.5 | 7e-39 | 36/48 (NCI-H2030, PANC-1, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **4.46×** | +11.4 | 9e-28 | 44/48 (PANC-1, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **2.12×** | +10.6 | 7e-24 | 39/48 (NCI-H2347, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.57×** | +6.6 | 7e-09 | 29/48 (PANC-1, NCI-H2030, …) | all doses, flat | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.38×** | +6.5 | 8e-09 | 37/48 (NCI-H2347, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.51×** | +6.1 | 1e-07 | 31/48 (hTERT-HPNE, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.50×** | +5.9 | 2e-07 | 29/48 (KATO III, hTERT-HPNE, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.37×** | +4.6 | 3e-04 | 28/48 (hTERT-HPNE, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.36×** | +4.6 | 3e-04 | 25/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +4.5 | 4e-04 | 25/48 (hTERT-HPNE, PANC-1, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.35×** | +4.3 | 0.001 | 25/48 (hTERT-HPNE, SHP-77, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.33×** | +4.2 | 0.001 | 27/47 (HOP62, SW 900, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +4.2 | 0.001 | 22/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.72×** | +4.2 | 0.001 | 23/48 (hTERT-HPNE, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.31×** | +3.9 | 0.003 | 21/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.007 | 21/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.18× | +3.4 | 0.019 | 20/48 (HT-29, NCI-H2347, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.022 | 17/47 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.054 | 16/48 (HOP62, HEC-1-A, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.22×** | +2.9 | 0.094 | 17/47 (HOP62, SW 900, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9825.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.422×** | -17.2 | 0e+00 | 47/48 (A498, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.464×** | -11.2 | 1e-26 | 41/48 (LOX-IMVI, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.593×** | -7.6 | 5e-12 | 40/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.713×** | -6.7 | 2e-09 | 35/48 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **0.419×** | -6.6 | 4e-09 | 35/45 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.664×** | -6.0 | 2e-07 | 35/48 (J82, SW480, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.672×** | -5.6 | 2e-06 | 28/48 (RKO, A549, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.687×** | -5.5 | 3e-06 | 33/48 (NCI-H2030, SW480, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.540×** | -4.7 | 2e-04 | 24/48 (A498, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.732×** | -4.5 | 3e-04 | 25/48 (H4, A498, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.648×** | -4.5 | 3e-04 | 26/48 (SW480, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **0.673×** | -4.3 | 8e-04 | 26/48 (HCT15, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.764×** | -3.9 | 0.004 | 23/48 (LoVo, SW1417, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.774×** | -3.7 | 0.008 | 21/48 (LOX-IMVI, A-172, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -3.6 | 0.010 | 2/48 (HOP62, CHP-212) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.842× | -3.4 | 0.021 | 17/48 (HCT15, Hs 766T, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.852× | -3.3 | 0.028 | 22/48 (H4, SNU-1, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.850× | -3.3 | 0.032 | 20/48 (A498, A-172, …) | top dose only |  |
| [[palbociclib (drug)]] 5 µM |  | **0.656×** | -3.2 | 0.039 | 17/47 (SNU-1, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.851× | -3.2 | 0.041 | 14/48 (Hs 766T, CHP-212, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.665×** | -3.1 | 0.051 | 16/48 (SW480, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.682×** | -2.9 | 0.086 | 17/48 (KATO III, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +1.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9825. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 55.1 | 5 (5 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 8.56× (z +12.3) ⚠ cell-cycle shift, explains ~83% of this change | [[Selinexor (drug)]] 5 µM 0.201× (z -13.1) ⚠ cell-cycle shift, explains ~56% of this change |
| [[A498 (line)]] | wt | 60.4 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.144× (z -21.3) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.395× (z -10.4) |
| [[HOP62 (line)]] | alt | 131 | 3 (3 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.382× (z -11.7) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -11.7) |
| [[PANC-1 (line)]] | alt | 58.5 | 5 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +19.3) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.486× (z -11.1) ⚠ cell-cycle shift, explains ~56% of this change |
| [[H4 (line)]] | wt | 65.3 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.180× (z -12.0) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.240× (z -10.2) |
| [[HS-578T (line)]] | alt | 81.6 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +18.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 58.3 | 0 | 5 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.139× (z -10.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -9.9) |
| [[A-172 (line)]] | wt | 80.3 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.237× (z -16.5) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.458× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 60.9 | 0 | 4 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.218× (z -15.4) ⚠ cell-cycle shift, explains ~56% of this change |
| [[NCI-H2347 (line)]] | alt | 46.8 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +17.1) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.438× (z -10.4) ⚠ cell-cycle shift, explains ~56% of this change |
| [[A549 (line)]] | wt | 57.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.333× (z -12.2) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -9.3) |
| [[C32 (line)]] | wt | 51.8 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.319× (z -10.7) ⚠ cell-cycle shift, explains ~56% of this change |
| [[CFPAC-1 (line)]] | alt | 46.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.371× (z -10.6) ⚠ cell-cycle shift, explains ~56% of this change |
| [[KATO III (line)]] | alt | 34.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.49× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.330× (z -10.6) ⚠ cell-cycle shift, explains ~56% of this change |
| [[LS 180 (line)]] | wt | 55.9 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.141× (z -16.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[MIA PaCa-2 (line)]] | alt | 59.4 | 0 | 3 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0556× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 52.9 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +20.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 57.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 0.5 µM 0.343× (z -9.6) ⚠ cell-cycle shift, explains ~73% of this change |
| [[A-427 (line)]] | wt | 62.6 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.272× (z -14.0) ⚠ cell-cycle shift, explains ~56% of this change |
| [[HCT15 (line)]] | alt | 71.5 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.218× (z -12.9) ⚠ cell-cycle shift, explains ~56% of this change |
| [[HT-29 (line)]] | alt | 39.0 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.286× (z -11.7) ⚠ cell-cycle shift, explains ~56% of this change |
| [[J82 (line)]] | alt | 105 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 33.5 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.338× (z -11.0) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 57.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 43.5 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.297× (z -13.1) ⚠ cell-cycle shift, explains ~56% of this change |
| [[Panc 03.27 (line)]] | alt | 55.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.451× (z -8.5) ⚠ cell-cycle shift, explains ~56% of this change |
| [[RKO (line)]] | wt | 34.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 23.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 33.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 62.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.391× (z -8.8) ⚠ cell-cycle shift, explains ~56% of this change |
| [[NCI-H1573 (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.244× (z -11.3) ⚠ cell-cycle shift, explains ~56% of this change |
| [[SK-MEL-2 (line)]] | alt | 76.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.419× (z -10.0) ⚠ cell-cycle shift, explains ~56% of this change |
| [[SNU-423 (line)]] | alt | 48.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 49.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9825), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGO1]] | +0.91 | +0.87 / +0.90 | both halves | 7e-06 | STRING 747 |
| [[NDC80]] | +0.91 | +0.87 / +0.92 | both halves | 7e-06 | STRING 465 |
| [[MKI67]] | +0.90 | +0.88 / +0.90 | both halves | 7e-06 | STRING 594 |
| [[KNL1]] | +0.90 | +0.86 / +0.90 | both halves | 7e-06 | STRING 474 |
| [[TPX2]] | +0.89 | +0.88 / +0.89 | both halves | 7e-06 | STRING 756 |
| [[KIF23]] | +0.89 | +0.87 / +0.88 | both halves | 7e-06 | STRING 693 |
| [[CENPF]] | +0.89 | +0.85 / +0.89 | both halves | 7e-06 | STRING 737 |
| [[KIF4A]] | +0.89 | +0.92 / +0.84 | both halves | 7e-06 | STRING 843 |
| [[NCAPG]] | +0.88 | +0.88 / +0.87 | both halves | 7e-06 | STRING 864 |
| [[CKAP2]] | +0.88 | +0.86 / +0.87 | both halves | 7e-06 |  |
| [[KIF11]] | +0.88 | +0.87 / +0.88 | both halves | 7e-06 | STRING 806 |
| [[GTSE1]] | +0.88 | +0.90 / +0.85 | both halves | 7e-06 | STRING 736 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises CKAP2L's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.83× lower at baseline in the lines without PIMREG | 0.036 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[PIMREG]] | B | PIMREG activity strengthens CKAP2L's drug response | lines that do not express PIMREG (6) vs lines expressing it (42) | the lines without PIMREG respond 0.64× as strongly (z diff +1.60); rises at some drug-doses, falls at others (34% from rises): Idarubicin (hydrochloride) 5 µM: 1.09x vs 0.64x (z diff +4.6); Harringtonine 5 µM: 1.43x vs 2.13x (z diff +3.0); Selinexor 0.05 µM: 0.74x vs 0.57x (z diff +1.9) | 0.074 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises CKAP2L's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PBK]] | C | PBK activity raises CKAP2L's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.46× lower at baseline in the lines without PBK | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[FAM72D]] | C | FAM72D activity raises CKAP2L's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.11× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises CKAP2L's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.59× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[DIAPH3]] | C | DIAPH3 activity raises CKAP2L's level | lines that do not express DIAPH3 (3) vs lines expressing it (47) | 2.14× lower at baseline in the lines without DIAPH3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[ACBD7]] | C | ACBD7 activity raises CKAP2L's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.60× lower at baseline in the lines without ACBD7 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.918). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.0, -55.9); signed map (-49.7, -43.9). **Vector** length 157, 57.5% of its response variance represented; |z| ≥ 3 in 1,374 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.73 to 60); *DREAM G2/M down* (control, mean cos +0.81 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.71 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.0 | +13.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +6.6 | +10.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.8 | +11.4 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +5.8 | +6.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +5.0 | +6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | -0.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.0 | +3.7 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.0 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +4.2 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.6 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -11.2 | -17.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -9.6 | -11.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.1 | -6.0 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | -6.3 | -7.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | -6.2 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -5.5 |
|  | [[EX229 (drug)]] 5 µM |  | -5.4 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -3.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.3 | -3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | cytoskeleton associated protein 2L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:112,736,349-112,764,664 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40629, radmis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYA6](https://www.uniprot.org/uniprotkb/Q8IYA6) (Cytoskeleton-associated protein 2-like):

> Microtubule-associated protein required for mitotic spindle formation and cell-cycle progression in neural progenitor cells.

**Summary**, from NCBI Gene [150468](https://www.ncbi.nlm.nih.gov/gene/150468):

> The protein encoded by this gene is thought to be a mitotic spindle protein important to neural stem or progenitor cells. Mutations in this gene have been associated with spindle organization defects, including mitotic spindle defects, lagging chromosomes, and chromatin bridges. There is evidence that mutations in this gene are associated with Filippi syndrome, characterized by growth defects, microcephaly, intellectual disability, facial feature defects, and syndactyly. There is a pseudogene …

**Accessions** — [HGNC:26877](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26877) · Entrez [150468](https://www.ncbi.nlm.nih.gov/gene/150468) · UniProt [Q8IYA6](https://www.uniprot.org/uniprotkb/Q8IYA6) · Ensembl [ENSG00000169607](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169607)

## Data

Gene col 9825: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9825); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9825, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9825]; `tensor/DDL_lfc|DDL_z.npy` [9825]; `embed/gene_vectors.npy` [9825]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9825 or target_col == 9825). Every well: [[CKAP2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CKAP2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
