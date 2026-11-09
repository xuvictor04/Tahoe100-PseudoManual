---
symbol: "ETS1"
type: "gene"
col: 5628
ensembl_id: "ENSG00000134954"
name: "ETS proto-oncogene 1, transcription factor"
location: "11q24.3"
module: 116
arm: "+"
pooled_cpm: 214.46
n_lines_expressing: 39
n_dd_up: 26
n_dd_down: 28
n_dd_up_clean: 21
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 19
direction_downstream: 22
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# ETS1

*ETS proto-oncogene 1, transcription factor* — 11q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.55× (z +23.1, q 0e+00, up in 34 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.388× (z -16.5, q 0e+00, down in 31 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRMD6]] (+0.74, fdr 7e-06), [[EGFR]] (+0.73, fdr 7e-06), [[PALM2AKAP2]] (+0.68, fdr 7e-06); moves opposite to [[UBE4B]] (-0.60, fdr 1e-05), [[NFATC3]] (-0.60, fdr 2e-05), [[CDC42SE2]] (-0.57, fdr 1e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[ADTRP]] → it (grade B ⚠); 22 go from it, the strongest it → [[ACTN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5628.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.55×** | +23.1 | 0e+00 | 34/37 (A549, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **11.8×** | +22.5 | 0e+00 | 37/38 (PANC-1, A549, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.04×** | +19.4 | 0e+00 | 34/37 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.60×** | +16.0 | 0e+00 | 32/37 (A549, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.37×** | +15.0 | 0e+00 | 33/37 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.99×** | +12.6 | 2e-34 | 35/37 (HS-578T, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.71×** | +9.4 | 5e-19 | 30/37 (A549, SNU-1, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.65×** | +8.7 | 2e-16 | 31/37 (HT-29, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.65×** | +8.7 | 2e-16 | 29/36 (NCI-H1573, HT-29, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.63×** | +8.2 | 2e-14 | 30/36 (HT-29, KATO III, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.36×** | +7.5 | 2e-12 | 26/38 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +7.3 | 1e-11 | 26/35 (A549, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.47×** | +6.7 | 7e-10 | 25/37 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.38×** | +5.6 | 9e-07 | 25/36 (HT-29, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +5.5 | 2e-06 | 20/37 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +5.2 | 7e-06 | 23/37 (HT-29, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.36×** | +4.9 | 3e-05 | 19/36 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.61×** | +4.4 | 4e-04 | 24/37 (SW480, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5628.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.388×** | -16.5 | 0e+00 | 31/37 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.532×** | -15.6 | 0e+00 | 35/38 (RKO, J82, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.412×** | -15.5 | 0e+00 | 31/37 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.520×** | -11.0 | 6e-26 | 33/37 (hTERT-HPNE, A498, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.570×** | -9.8 | 1e-20 | 30/37 (J82, LOX-IMVI, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.606×** | -8.7 | 2e-16 | 32/37 (NCI-H23, J82, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.608×** | -8.3 | 6e-15 | 25/36 (J82, hTERT-HPNE, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.647×** | -7.6 | 2e-12 | 27/37 (LOX-IMVI, A549, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.681×** | -6.7 | 1e-09 | 27/38 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.682×** | -6.7 | 1e-09 | 26/37 (NCI-H2030, RKO, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.684×** | -6.4 | 9e-09 | 26/39 (hTERT-HPNE, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.729×** | -5.5 | 2e-06 | 28/37 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.566×** | -5.2 | 9e-06 | 24/36 (RKO, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.767×** | -4.6 | 1e-04 | 22/37 (LOX-IMVI, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.829×** | -4.6 | 1e-04 | 18/37 (J82, HOP62, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.788×** | -4.2 | 0.001 | 23/37 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.832×** | -4.0 | 0.002 | 18/37 (SW480, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **0.797×** | -4.0 | 0.002 | 19/37 (CFPAC-1, PANC-1, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.652×** | -3.9 | 0.003 | 19/37 (NCI-H23, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.731×** | -3.9 | 0.003 | 19/37 (RPMI-7951, HEC-1-A, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5628. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 244 | 3 | 18 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +16.4) | [[Adagrasib (drug)]] 0.05 µM 0.485× (z -26.0) ⚠ position not correctable · without an alert: [[Ponatinib (drug)]] 5 µM 0.240× (z -14.6) |
| [[SW480 (line)]] | alt | 104 | 14 (2 ⚠) | 7 | [[TAK-901 (drug)]] 5 µM 10.3× (z +13.3) | [[Binimetinib (drug)]] 0.05 µM 0.527× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 324 | 15 (4 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 7.28× (z +18.8) | [[Panobinostat (drug)]] 5 µM 0.254× (z -12.9) |
| [[RKO (line)]] | wt | 478 | 2 | 14 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 8.38× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -24.2) |
| [[A549 (line)]] | wt | 186 | 9 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +25.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -11.2) |
| [[HT-29 (line)]] | alt | 63.7 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +17.8) | — |
| [[hTERT-HPNE (line)]] | wt | 532 | 4 | 9 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 14.2× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -15.2) |
| [[LOX-IMVI (line)]] | wt | 601 | 3 | 10 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 9.70× (z +14.4) | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -23.0) |
| [[A498 (line)]] | wt | 227 | 7 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +23.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 155 | 9 (2 ⚠) | 3 | [[Harringtonine (drug)]] 0.5 µM 4.07× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 143 | 0 | 11 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -17.6) |
| [[PANC-1 (line)]] | alt | 255 | 7 | 4 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +22.7) | [[Ponatinib (drug)]] 5 µM 0.454× (z -9.1) |
| [[HS-578T (line)]] | alt | 189 | 6 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +19.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -14.7) |
| [[J82 (line)]] | alt | 721 | 1 | 9 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.02× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -26.1) |
| [[KATO III (line)]] | alt | 125 | 9 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 4.08× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 477 | 6 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +14.8) | [[Panobinostat (drug)]] 5 µM 0.305× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 184 | 5 | 4 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.04× (z +16.4) | [[Panobinostat (drug)]] 5 µM 0.237× (z -15.2) |
| [[SW 900 (line)]] | alt | 184 | 6 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.58× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.317× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 234 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +25.5) | [[Panobinostat (drug)]] 5 µM 0.328× (z -11.7) |
| [[HOP62 (line)]] | alt | 314 | 5 | 3 | [[TAK-901 (drug)]] 5 µM 21.1× (z +16.2) | [[Panobinostat (drug)]] 5 µM 0.344× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 272 | 5 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 20.0× (z +15.9) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.270× (z -13.3) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.376× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 351 | 5 | 3 | [[TAK-901 (drug)]] 5 µM 19.6× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -10.6) |
| [[SNU-1 (line)]] | wt | 94.0 | 8 | 0 | [[Harringtonine (drug)]] 0.5 µM 9.99× (z +16.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 177 | 7 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.80× (z +19.6) | — |
| [[SNU-423 (line)]] | alt | 472 | 2 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.0× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -16.0) |
| [[A-172 (line)]] | wt | 300 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +14.6) | [[Panobinostat (drug)]] 0.5 µM 0.327× (z -9.7) |
| [[H4 (line)]] | wt | 307 | 2 | 4 | [[TAK-901 (drug)]] 5 µM 18.7× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.277× (z -10.5) |
| [[Hs 766T (line)]] | wt | 345 | 3 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 19.8× (z +15.8) | [[Panobinostat (drug)]] 5 µM 0.346× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 336 | 3 | 3 | [[TAK-901 (drug)]] 5 µM 15.0× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -16.6) |
| [[NCI-H460 (line)]] | wt | 111 | 5 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 5.63× (z +13.6) | — |
| [[C32 (line)]] | wt | 135 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +11.6) | — |
| [[SW1417 (line)]] | alt | 112 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.6) | — |
| [[SW 1271 (line)]] | alt | 304 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 117 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 27.5× (z +13.4) | — |
| [[A-427 (line)]] | wt | 47.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 30.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.7 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 37.1 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 16.7 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 29.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 385 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5628), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRMD6]] | +0.74 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[EGFR]] | +0.73 | +0.73 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 545 |
| [[PALM2AKAP2]] | +0.68 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[RFTN1]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[BNC1]] | +0.63 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[STARD13]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[RUNX1]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 | pathway: Differentiation of T cells; STRING 999 |
| [[ANXA5]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ASAP1]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[NABP1]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[CYTOR]] | +0.60 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[MIR4435-2HG]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE4B]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[NFATC3]] | -0.60 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[CDC42SE2]] | -0.57 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[CC2D1A]] | -0.54 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[RAD9A]] | -0.54 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[HOXB6]] | -0.54 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[ZFP14]] | -0.53 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[PPP2R5E]] | -0.53 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ATPAF2]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[NDUFAF7]] | -0.52 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[EGFL8]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[NR2F6]] | -0.51 | -0.37 / -0.53 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 16, C 3. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADTRP]] | B | ADTRP activity raises ETS1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 4.30× lower at baseline in the lines without ADTRP | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[CCBE1]] | B | CCBE1 activity raises ETS1's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 3.51× lower at baseline in the lines without CCBE1 | 0.016 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[RUNX1]] | B | RUNX1 activity raises ETS1's level | lines that do not express RUNX1 (5) vs lines expressing it (45) | 5.19× lower at baseline in the lines without RUNX1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent |
| [[CD59]] | B | CD59 activity raises ETS1's level | lines that do not express CD59 (7) vs lines expressing it (43) | 3.01× lower at baseline in the lines without CD59 | 0.025 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[AKAP12]] | B | AKAP12 activity raises ETS1's level | lines that do not express AKAP12 (18) vs lines expressing it (32) | 3.02× lower at baseline in the lines without AKAP12 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: ADAMTS18, IGF2BP1, CLEC2B |
| [[TOP2A]] | B | TOP2A activity raises ETS1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HRH1]] | B | HRH1 activity raises ETS1's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 4.84× lower at baseline in the lines without HRH1 | 0.038 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[MGLL]] | B | MGLL activity raises ETS1's level | lines that do not express MGLL (14) vs lines expressing it (36) | 2.47× lower at baseline in the lines without MGLL | 0.038 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[PDCD1LG2]] | B | PDCD1LG2 activity raises ETS1's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 3.05× lower at baseline in the lines without PDCD1LG2 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |
| [[FGF5]] | B | FGF5 activity raises ETS1's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 3.04× lower at baseline in the lines without FGF5 | 0.049 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702 |
| [[NAV3]] | B | NAV3 activity raises ETS1's level | lines that do not express NAV3 (16) vs lines expressing it (34) | 3.08× lower at baseline in the lines without NAV3 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12 |
| [[LINC00707]] | B | LINC00707 activity raises ETS1's level | lines that do not express LINC00707 (26) vs lines expressing it (24) | 2.91× lower at baseline in the lines without LINC00707 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000285845, ENSG00000285743, LINP1 |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 20, C 2. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACTN1]] | B | ETS1 activity raises ACTN1's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 1.98× lower at baseline in the lines without ETS1 | 0.008 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[ATP13A3]] | B | ETS1 activity raises ATP13A3's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 1.98× lower at baseline in the lines without ETS1 | 0.019 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[MSANTD3]] | B | ETS1 activity raises MSANTD3's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 2.26× lower at baseline in the lines without ETS1 | 0.029 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[ASAP1]] | B | ETS1 activity raises ASAP1's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 1.64× lower at baseline in the lines without ETS1 | 0.036 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[TP53BP2]] | B | ETS1 activity raises TP53BP2's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 1.89× lower at baseline in the lines without ETS1 | 0.036 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[ZBTB38]] | B | ETS1 activity raises ZBTB38's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 2.07× lower at baseline in the lines without ETS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[CAPN2]] | B | ETS1 activity raises CAPN2's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 1.88× lower at baseline in the lines without ETS1 | 0.042 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[CD44]] | B | ETS1 activity raises CD44's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 5.24× lower at baseline in the lines without ETS1 | 0.044 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[PALM2AKAP2]] | B | ETS1 activity raises PALM2AKAP2's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 3.84× lower at baseline in the lines without ETS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[NOCT]] | B | ETS1 activity raises NOCT's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 1.66× lower at baseline in the lines without ETS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[ANXA5]] | B | ETS1 activity raises ANXA5's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 1.67× lower at baseline in the lines without ETS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[ABL2]] | B | ETS1 activity raises ABL2's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 2.31× lower at baseline in the lines without ETS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.0, 10.6); signed map (12.5, 41.0). **Vector** length 139, 50.5% of its response variance represented; |z| ≥ 3 in 1,742 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.5 | +19.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.1 | +23.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.9 | +15.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.2 | +22.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.7 | +9.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +7.0 | +8.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.5 | +7.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.9 | +6.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.7 | +5.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -8.4 | -7.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -6.7 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.8 | -4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.8 | -8.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | -4.7 | -3.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.9 | -2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.8 | -6.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | ETS proto-oncogene 1, transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.3 — chr11:128,458,761-128,587,558 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10768, ETS-1; previously EWSR2 |
| Gene groups (HGNC) | ETS transcription factor family |
| Hallmark sets | ALLOGRAFT_REJECTION, KRAS_SIGNALING_UP, HYPOXIA |
| Reactome | 6 pathways, smallest: Oncogene Induced Senescence; Differentiation of naive CD4+ T cells to T helper 2 cells (Th2 cells); Differentiation of T cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P14921](https://www.uniprot.org/uniprotkb/P14921) (Protein C-ets-1):

> Transcription factor. Directly controls the expression of cytokine and chemokine genes in a wide variety of different cellular contexts. May control the differentiation, survival and proliferation of lymphoid cells. May also regulate angiogenesis through regulation of expression of genes controlling endothelial cell migration and invasion.; [Isoform Ets-1 p27]: Acts as a dominant-negative for isoform c-ETS-1A.

**Summary**, from NCBI Gene [2113](https://www.ncbi.nlm.nih.gov/gene/2113):

> This gene encodes a member of the ETS family of transcription factors, which are defined by the presence of a conserved ETS DNA-binding domain that recognizes the core consensus DNA sequence GGAA/T in target genes. These proteins function either as transcriptional activators or repressors of numerous genes, and are involved in stem cell development, cell senescence and death, and tumorigenesis. Alternatively spliced transcript variants encoding different isoforms have been described for this …

**Accessions** — [HGNC:3488](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3488) · Entrez [2113](https://www.ncbi.nlm.nih.gov/gene/2113) · UniProt [P14921](https://www.uniprot.org/uniprotkb/P14921) · Ensembl [ENSG00000134954](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134954)

## Data

Gene col 5628: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5628); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5628, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5628]; `tensor/DDL_lfc|DDL_z.npy` [5628]; `embed/gene_vectors.npy` [5628]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5628 or target_col == 5628). Every well: [[ETS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ETS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
