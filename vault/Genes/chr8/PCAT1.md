---
symbol: "PCAT1"
type: "gene"
col: 14803
ensembl_id: "ENSG00000253438"
name: "prostate cancer associated transcript 1"
location: "8q24.21"
module: 8
arm: "+"
pooled_cpm: 64.09
n_lines_expressing: 39
n_dd_up: 13
n_dd_down: 30
n_dd_up_clean: 12
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 30
direction_downstream: 21
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PCAT1

*prostate cancer associated transcript 1* — 8q24.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.97× (z +15.2, q 0e+00, up in 24 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.525× (z -14.3, q 1e-43, down in 30 of 37 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.406× (z -14.1, q 7e-43, down in 30 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POU5F1B]] (+0.93, fdr 7e-06, ⚠ read-through risk), [[SAMD12-AS1]] (+0.66, fdr 7e-06), [[KLHL2P1]] (+0.58, fdr 5e-05), [[TAFA2]] (+0.57, fdr 4e-05); moves opposite to [[PGBD1]] (-0.54, fdr 3e-05), [[MPP2]] (-0.54, fdr 4e-05), [[NBPF3]] (-0.49, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[TNFSF15]] → it (grade B ⚠); 21 go from it, the strongest it → [[SLC44A3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14803.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +15.2 | 0e+00 | 24/37 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.63×** | +7.7 | 3e-12 | 20/37 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.0 | 3e-07 | 13/39 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.40×** | +5.3 | 1e-05 | 21/36 (LS 180, A498, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +5.3 | 1e-05 | 21/36 (NCI-H1573, HEC-1-A, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.8 | 2e-04 | 16/37 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.010 | 19/37 (HEC-1-A, HCT15, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.26×** | +3.7 | 0.015 | 17/36 (HEC-1-A, NCI-H2030, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.022 | 14/36 (NCI-H2030, LoVo, …) | rises with dose |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.022 | 12/36 (BT-474, LS 180, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.052 | 9/38 (NCI-H2030, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.068 | 16/36 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.2 | 0.068 | 13/37 (HEC-1-A, LoVo, …) | two highest doses |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.084 | 10/37 (LS 180, NCI-H1573, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.084 | 8/36 (NCI-H2030, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14803.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.525×** | -14.3 | 1e-43 | 30/37 (HT-29, NCI-H1573, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.406×** | -14.1 | 7e-43 | 30/36 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.447×** | -12.6 | 2e-34 | 30/37 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.452×** | -12.0 | 6e-31 | 31/37 (A498, HT-29, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.477×** | -11.6 | 4e-29 | 30/37 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.525×** | -10.1 | 5e-22 | 31/36 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.526×** | -9.7 | 3e-20 | 30/36 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.545×** | -9.5 | 1e-19 | 30/37 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.558×** | -9.1 | 4e-18 | 29/36 (HT-29, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.604×** | -7.9 | 2e-13 | 28/36 (SHP-77, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.616×** | -7.6 | 2e-12 | 24/37 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.630×** | -7.2 | 2e-11 | 24/36 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.652×** | -6.7 | 9e-10 | 25/36 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.449×** | -6.6 | 2e-09 | 25/38 (HT-29, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.743×** | -6.6 | 2e-09 | 23/37 (A498, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.660×** | -6.3 | 1e-08 | 20/37 (A498, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.512×** | -5.5 | 1e-06 | 20/35 (Panc 03.27, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.568×** | -4.6 | 1e-04 | 22/38 (HT-29, NCI-H1573, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.744×** | -4.5 | 2e-04 | 20/36 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.715×** | -3.7 | 0.004 | 10/37 (SHP-77, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.795×** | -3.4 | 0.013 | 10/37 (LoVo, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14803. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 337 | 0 | 19 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0863× (z -30.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0668× (z -23.6) |
| [[LoVo (line)]] | wt | 70.0 | 2 | 10 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +13.5) | [[Panobinostat (drug)]] 5 µM 0.137× (z -21.5) |
| [[NCI-H1573 (line)]] | alt | 140 | 1 | 11 (6 ⚠) | [[Belumosudil (drug)]] 5 µM 2.95× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.0860× (z -28.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.160× (z -15.2) |
| [[A498 (line)]] | wt | 105 | 2 (1 ⚠) | 9 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -28.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.177× (z -15.3) |
| [[LS 180 (line)]] | wt | 59.4 | 3 (1 ⚠) | 8 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -14.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.232× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 168 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -14.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.155× (z -14.9) |
| [[C32 (line)]] | wt | 121 | 0 | 7 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.161× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 163 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -19.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.151× (z -15.0) |
| [[KATO III (line)]] | alt | 85.6 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -19.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.183× (z -14.9) |
| [[COLO 205 (line)]] | alt | 108 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.107× (z -15.6) |
| [[HEC-1-A (line)]] | alt | 43.5 | 5 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -10.5) |
| [[SW1417 (line)]] | alt | 106 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -16.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.226× (z -12.3) |
| [[A-172 (line)]] | wt | 40.7 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +12.3) | [[Belinostat (drug)]] 5 µM 0.190× (z -11.5) |
| [[A-427 (line)]] | wt | 65.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.290× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 147 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.131× (z -13.6) |
| [[SW48 (line)]] | wt | 123 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -13.1) |
| [[BT-474 (line)]] | alt | 106 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -14.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HCT15 (line)]] | alt | 48.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 40.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.92× (z +9.8) | [[Adagrasib (drug)]] 0.05 µM 0.569× (z -13.0) ⚠ position not correctable |
| [[NCI-H2030 (line)]] | alt | 90.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -17.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.315× (z -8.6) |
| [[RKO (line)]] | wt | 48.1 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +11.7) | [[Belinostat (drug)]] 0.5 µM 0.299× (z -9.7) |
| [[SHP-77 (line)]] | alt | 73.8 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -11.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[CHP-212 (line)]] | wt | 37.5 | 0 | 2 (1 ⚠) | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0721× (z -9.2) |
| [[H4 (line)]] | wt | 41.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -12.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[J82 (line)]] | alt | 29.2 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.257× (z -10.3) |
| [[SW480 (line)]] | alt | 41.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.29× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 74.0 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0650× (z -10.9) |
| [[C-33 A (line)]] | alt | 50.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.174× (z -9.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HepG2_C3A (line)]] | wt | 19.5 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0411× (z -14.2) |
| [[Hs 766T (line)]] | wt | 38.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.240× (z -8.5) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 51.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -11.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SK-MEL-2 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0631× (z -10.3) ⚠ toxic |
| [[A549 (line)]] | wt | 15.5 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.1 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 15.4 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.5 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 24.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14803), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POU5F1B]] | +0.93 | +0.90 / +0.90 | both halves | 7e-06 | ⚠ **readthrough risk**: POU5F1B lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[SAMD12-AS1]] | +0.66 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[KLHL2P1]] | +0.58 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[TAFA2]] | +0.57 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[SLC44A3-AS1]] | +0.56 | +0.62 / +0.30 | both halves | 2e-04 |  |
| [[STS]] | +0.56 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[STEAP2-AS1]] | +0.56 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[STPG2]] | +0.55 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[RGS6]] | +0.54 | +0.59 / +0.38 | both halves | 6e-05 |  |
| [[CA3]] | +0.54 | +0.38 / +0.47 | both halves | 7e-05 |  |
| [[PLUT]] | +0.53 | +0.52 / +0.33 | both halves | 1e-04 | same gene group |
| [[LINC02343]] | +0.52 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[PITX1-AS1]] | +0.51 | +0.39 / +0.48 | both halves | 5e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGBD1]] | -0.54 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[MPP2]] | -0.54 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[NBPF3]] | -0.49 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[KATNAL1]] | -0.48 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[CLTCL1]] | -0.48 | -0.43 / -0.24 | both halves | 5e-04 |  |
| [[PKD1L1-AS1]] | -0.48 | -0.45 / -0.26 | both halves | 4e-04 |  |
| [[ZNF559]] | -0.46 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[WRAP73]] | -0.46 | -0.29 / -0.32 | both halves | 3e-04 |  |
| [[ZNF8-DT]] | -0.46 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[ZNF559-ZNF177]] | -0.46 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[IMMP1L]] | -0.46 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[MRNIP]] | -0.46 | -0.29 / -0.35 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 28, C 2. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFSF15]] | B | TNFSF15 activity raises PCAT1's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 3.13× lower at baseline in the lines without TNFSF15 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[GRHL2]] | B | GRHL2 activity raises PCAT1's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 2.92× lower at baseline in the lines without GRHL2 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[FAAH2]] | B | FAAH2 activity raises PCAT1's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.45× lower at baseline in the lines without FAAH2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[CCSER1]] | B | CCSER1 activity raises PCAT1's level | lines that do not express CCSER1 (20) vs lines expressing it (30) | 2.35× lower at baseline in the lines without CCSER1 | 0.008 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |
| [[CRACDL]] | B | CRACDL activity raises PCAT1's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 2.55× lower at baseline in the lines without CRACDL | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[GPR87]] | B | GPR87 activity raises PCAT1's level | lines that do not express GPR87 (36) vs lines expressing it (14) | 2.34× lower at baseline in the lines without GPR87 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1 |
| [[SYK]] | B | SYK activity raises PCAT1's level | lines that do not express SYK (30) vs lines expressing it (20) | 2.94× lower at baseline in the lines without SYK | 0.015 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises PCAT1's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.35× lower at baseline in the lines without SLC44A3-AS1 | 0.017 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[STEAP4]] | B | STEAP4 activity raises PCAT1's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.62× lower at baseline in the lines without STEAP4 | 0.020 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[SLC28A3]] | B | SLC28A3 activity raises PCAT1's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 1.88× lower at baseline in the lines without SLC28A3 | 0.020 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[TMEM125]] | B | TMEM125 activity raises PCAT1's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 2.81× lower at baseline in the lines without TMEM125 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[TMC5]] | B | TMC5 activity raises PCAT1's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 2.71× lower at baseline in the lines without TMC5 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 19, C 2. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3-AS1]] | B | PCAT1 activity raises SLC44A3-AS1's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 3.09× lower at baseline in the lines without PCAT1 | 0.004 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[ATXN7L3-AS1]] | B | PCAT1 activity raises ATXN7L3-AS1's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 1.42× lower at baseline in the lines without PCAT1 | 0.024 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[CCSER1]] | B | PCAT1 activity raises CCSER1's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 3.47× lower at baseline in the lines without PCAT1 | 0.027 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[CRACDL]] | B | PCAT1 activity raises CRACDL's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 3.03× lower at baseline in the lines without PCAT1 | 0.029 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[TNFSF15]] | B | PCAT1 activity raises TNFSF15's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 2.99× lower at baseline in the lines without PCAT1 | 0.030 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[PLEKHG1]] | B | PCAT1 activity raises PLEKHG1's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 3.25× lower at baseline in the lines without PCAT1 | 0.031 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[KLHL2P1]] | B | PCAT1 activity strengthens KLHL2P1's drug response | lines that do not express PCAT1 (10) vs lines expressing it (35) | the lines without PCAT1 respond 0.64× as strongly (z diff +1.14); strongest at Ouabain (Octahydrate) 5 µM: 0.78x vs 0.29x (z diff +3.4) | 0.032 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[DNAAF9]] | B | PCAT1 activity lowers DNAAF9's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 2.41× higher at baseline in the lines without PCAT1 | 0.044 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[FAAH2]] | B | PCAT1 activity raises FAAH2's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 3.47× lower at baseline in the lines without PCAT1 | 0.049 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[SYK]] | B | PCAT1 activity raises SYK's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 3.85× lower at baseline in the lines without PCAT1 | 0.051 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[SAMD12]] | B | PCAT1 activity raises SAMD12's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 2.89× lower at baseline in the lines without PCAT1 | 0.057 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[C3orf18]] | B | PCAT1 activity lowers C3orf18's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 1.63× higher at baseline in the lines without PCAT1 | 0.058 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.517). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.8, 53.8); signed map (58.6, 0.1). **Vector** length 106, 29.0% of its response variance represented; |z| ≥ 3 in 1,277 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.6 | +15.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.1 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.6 | +2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.5 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.7 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +1.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +5.3 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.9 | -7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.4 | -9.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.3 | -14.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.2 | -4.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -4.6 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.9 | -2.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.8 | -3.3 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.7 | +0.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | prostate cancer associated transcript 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q24.21 — chr8:126,556,323-127,419,050 (+) |
| Ensembl biotype | lncRNA |
| Also known as | PCAT-1, PCA1, PiHL |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100750225](https://www.ncbi.nlm.nih.gov/gene/100750225):

> This gene produces a long non-coding RNA that promotes cell proliferation and is upregulated in prostate, colorectal, and other cancers. This RNA negatively regulates the BRCA2 tumor suppressor protein and positively regulates Myc oncoprotein. It contains binding sites for microRNAs, and may act as a sponge for microRNAs that regulate cell growth pathways. [provided by RefSeq, Dec 2017]

**Accessions** — [HGNC:43022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43022) · Entrez [100750225](https://www.ncbi.nlm.nih.gov/gene/100750225) · Ensembl [ENSG00000253438](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253438)

## Data

Gene col 14803: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14803); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14803, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14803]; `tensor/DDL_lfc|DDL_z.npy` [14803]; `embed/gene_vectors.npy` [14803]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14803 or target_col == 14803). Every well: [[PCAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
