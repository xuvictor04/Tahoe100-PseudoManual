---
symbol: "SRGAP1"
type: "gene"
col: 12306
ensembl_id: "ENSG00000196935"
name: "SLIT-ROBO Rho GTPase activating protein 1"
location: "12q14.2"
module: 120
arm: "+"
pooled_cpm: 286.81
n_lines_expressing: 48
n_dd_up: 21
n_dd_down: 20
n_dd_up_clean: 18
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# SRGAP1

*SLIT-ROBO Rho GTPase activating protein 1* — 12q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.61× (z +8.6, q 5e-15, up in 29 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.524× (z -11.8, q 3e-29, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MARCHF4]] (+0.69, fdr 7e-06), [[DDAH1]] (+0.68, fdr 7e-06), [[RASAL2]] (+0.68, fdr 7e-06); moves opposite to [[PLXNB3]] (-0.53, fdr 3e-05), [[SREBF1]] (-0.53, fdr 2e-05), [[PLEKHA2]] (-0.53, fdr 3e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DAW1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12306.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +8.6 | 5e-15 | 29/46 (PANC-1, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +7.5 | 2e-11 | 33/46 (A-172, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.51×** | +7.4 | 2e-11 | 34/46 (BT-474, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +7.1 | 1e-10 | 28/46 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.48×** | +7.1 | 1e-10 | 31/46 (C32, RPMI-7951, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.09×** | +7.0 | 3e-10 | 32/47 (PANC-1, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +6.2 | 4e-08 | 27/46 (C-33 A, Hs 766T, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.43×** | +6.2 | 5e-08 | 29/45 (C32, SW 900, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.74×** | +5.2 | 1e-05 | 30/46 (NCI-H2030, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.34×** | +5.2 | 1e-05 | 27/45 (RPMI-7951, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +4.8 | 8e-05 | 29/46 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +4.1 | 0.002 | 25/46 (C32, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.003 | 25/46 (SW 900, C32, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Rapamycin (drug)]] 5 µM |  | 1.17× | +3.9 | 0.003 | 15/46 (A-172, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +3.9 | 0.003 | 24/45 (A-172, BT-474, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.7 | 0.008 | 21/47 (C32, SW 900, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.6 | 0.009 | 24/46 (C32, SW 900, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.020 | 20/47 (A-172, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12306.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.524×** | -11.8 | 3e-29 | 39/46 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.542×** | -11.1 | 2e-26 | 40/46 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.563×** | -10.5 | 3e-23 | 36/46 (AsPC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -8.8 | 2e-16 | 30/47 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.623×** | -8.6 | 7e-16 | 32/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.686×** | -6.6 | 4e-09 | 31/45 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.692×** | -6.5 | 8e-09 | 25/43 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.709×** | -6.3 | 2e-08 | 32/46 (NCI-H2030, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.741×** | -5.1 | 3e-05 | 28/44 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.779×** | -4.6 | 3e-04 | 25/46 (NCI-H23, HOP62, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.788×** | -4.4 | 6e-04 | 24/46 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.802×** | -4.0 | 0.003 | 26/47 (HOP62, A-172, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.808×** | -3.9 | 0.004 | 24/46 (LS 180, HOP62, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.665×** | -3.9 | 0.004 | 25/46 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.809×** | -3.7 | 0.007 | 23/46 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Vandetanib (drug)]] 5 µM |  | **0.827×** | -3.5 | 0.018 | 21/46 (BT-474, KATO III, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.829×** | -3.4 | 0.019 | 18/46 (BT-474, hTERT-HPNE, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.836× | -3.3 | 0.028 | 21/46 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.713×** | -3.2 | 0.033 | 21/46 (LOX-IMVI, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.739×** | -2.9 | 0.099 | 20/46 (LoVo, NCI-H460, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12306. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 870 | 0 | 23 (10 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.107× (z -25.9) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -25.9) |
| [[NCI-H23 (line)]] | alt | 387 | 0 | 22 (8 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.549× (z -22.4) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -14.8) |
| [[NCI-H2030 (line)]] | alt | 676 | 1 | 14 (8 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -21.7) |
| [[NCI-H460 (line)]] | wt | 778 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -25.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -19.8) |
| [[NCI-H1792 (line)]] | alt | 704 | 0 | 12 (5 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.595× (z -16.4) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.198× (z -14.3) |
| [[C32 (line)]] | wt | 107 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 4.98× (z +13.4) | — |
| [[J82 (line)]] | alt | 428 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -18.3) |
| [[AsPC-1 (line)]] | alt | 348 | 2 | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.20× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.257× (z -16.5) |
| [[LOX-IMVI (line)]] | wt | 524 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -18.1) |
| [[A-172 (line)]] | wt | 129 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +12.1) | — |
| [[LoVo (line)]] | wt | 279 | 1 | 7 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.59× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.413× (z -11.8) |
| [[PANC-1 (line)]] | alt | 270 | 5 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +21.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.82× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.394× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -11.4) |
| [[HOP62 (line)]] | alt | 170 | 0 | 7 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.594× (z -19.7) ⚠ position not correctable · without an alert: [[Ponatinib (drug)]] 5 µM 0.333× (z -12.0) |
| [[KATO III (line)]] | alt | 213 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -14.0) |
| [[A498 (line)]] | wt | 262 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -13.4) |
| [[BT-474 (line)]] | alt | 139 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.67× (z +11.2) | — |
| [[C-33 A (line)]] | alt | 137 | 5 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.75× (z +16.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.79× (z +14.5) | — |
| [[HS-578T (line)]] | alt | 214 | 2 | 3 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.63× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -12.4) |
| [[A-427 (line)]] | wt | 433 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.482× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 320 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -13.8) |
| [[HepG2_C3A (line)]] | wt | 393 | 1 | 3 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.88× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.280× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.317× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 442 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.302× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 146 | 4 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.00× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 234 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 10.9× (z +10.9) | — |
| [[HT-29 (line)]] | alt | 113 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.80× (z +11.3) | [[Selinexor (drug)]] 5 µM 0.548× (z -9.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 92.9 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.78× (z +12.5) | — |
| [[A549 (line)]] | wt | 421 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -15.5) |
| [[SK-MEL-2 (line)]] | alt | 87.6 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.03× (z +10.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 145 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.436× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 134 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 157 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -12.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 159 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.11× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 77.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H661 (line)]] | alt | 164 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 81.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.78× (z +8.5) | — |
| [[SW48 (line)]] | wt | 228 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.380× (z -8.7) |
| [[AN3 CA (line)]] | alt | 149 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 85.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.8 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 200 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 229 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 238 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 114 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 62.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12306), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARCHF4]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[DDAH1]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[RASAL2]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[CCN1]] | +0.65 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[ABL2]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 | same gene group; pathway: RAC1 GTPase cycle |
| [[SFTA1P]] | +0.63 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[EGFR]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[FJX1]] | +0.62 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[KIFC3]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[NAV3]] | +0.62 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[LINC00707]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[CCN2]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLXNB3]] | -0.53 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[SREBF1]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PLEKHA2]] | -0.53 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[C20orf96]] | -0.52 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[LNPK]] | -0.52 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ATPAF1]] | -0.52 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[SRP54-AS1]] | -0.52 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[CRY2]] | -0.52 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[TFG]] | -0.52 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[FBXO7]] | -0.52 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[VDAC3]] | -0.52 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[LINC00674]] | -0.52 | -0.50 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DAW1]] | B | DAW1 activity raises SRGAP1's level | lines that do not express DAW1 (34) vs lines expressing it (16) | 2.06× lower at baseline in the lines without DAW1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NEFL, OLR1, ENSG00000255227 |
| [[THSD4]] | B | THSD4 activity raises SRGAP1's level | lines that do not express THSD4 (18) vs lines expressing it (32) | 1.66× lower at baseline in the lines without THSD4 | 0.0998 | ⚠ within organs, on part of the lines; also absent: NR2E3, EDN1, CLDN1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.846). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.8, 11.9); signed map (13.4, 41.2). **Vector** length 140, 47.7% of its response variance represented; |z| ≥ 3 in 1,973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.7 | +1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +8.0 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.8 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.2 | +8.6 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +7.0 | +5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.0 | +3.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +5.6 | +3.1 |
| fall | [[venetoclax (drug)]] 5 µM |  | -4.6 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.5 | -4.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -1.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.7 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.7 | -1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | SLIT-ROBO Rho GTPase activating protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.2 — chr12:63,843,761-64,162,217 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1304, ARHGAP13 |
| Gene groups (HGNC) | F-BAR domain containing; AH/BAR family Rho GTPase activating proteins; SH3 domain containing |
| Reactome | 10 pathways, smallest: Inactivation of CDC42 and RAC1; RHOA GTPase cycle; CDC42 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6B7](https://www.uniprot.org/uniprotkb/Q7Z6B7) (SLIT-ROBO Rho GTPase-activating protein 1):

> GTPase-activating protein for RhoA and Cdc42 small GTPases. Together with CDC42 seems to be involved in the pathway mediating the repulsive signaling of Robo and Slit proteins in neuronal migration. SLIT2, probably through interaction with ROBO1, increases the interaction of SRGAP1 with ROBO1 and inactivates CDC42.

**Summary**, from NCBI Gene [57522](https://www.ncbi.nlm.nih.gov/gene/57522):

> The protein encoded by this gene is a GTPase activator, working with the GTPase CDC42 to negatively regulate neuronal migration. The encoded protein interacts with the transmembrane receptor ROBO1 to inactivate CDC42. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:17382](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17382) · Entrez [57522](https://www.ncbi.nlm.nih.gov/gene/57522) · UniProt [Q7Z6B7](https://www.uniprot.org/uniprotkb/Q7Z6B7) · Ensembl [ENSG00000196935](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196935)

## Data

Gene col 12306: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12306); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12306, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12306]; `tensor/DDL_lfc|DDL_z.npy` [12306]; `embed/gene_vectors.npy` [12306]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12306 or target_col == 12306). Every well: [[SRGAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRGAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
