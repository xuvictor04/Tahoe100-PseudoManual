---
symbol: "CDK6"
type: "gene"
col: 2668
ensembl_id: "ENSG00000105810"
name: "cyclin dependent kinase 6"
location: "7q21.2"
module: 197
arm: "+"
pooled_cpm: 320.66
n_lines_expressing: 46
n_dd_up: 10
n_dd_down: 22
n_dd_up_clean: 6
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/197"]
generated_by: "tahoemap"
---

# CDK6

*cyclin dependent kinase 6* — 7q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.94× (z +14.7, q 0e+00, up in 32 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.476× (z -16.4, q 0e+00, down in 38 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENC1]] (+0.71, fdr 7e-06), [[DDAH1]] (+0.69, fdr 7e-06), [[PLCB4]] (+0.69, fdr 7e-06); moves opposite to [[KCTD7]] (-0.64, fdr 9e-06), [[RAB6A]] (-0.62, fdr 1e-05), [[ZFPL1]] (-0.61, fdr 1e-05).
> It is in [[Module 197]], a single-armed module (Nervous system development).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ANAPC1P4]] → it (grade C ⚠); 3 go from it, the strongest it → cells under [[Pentoxifylline (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2668.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +14.7 | 0e+00 | 32/44 (A498, SW 900, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +11.5 | 3e-28 | 29/44 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +9.9 | 8e-21 | 32/45 (HOP62, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.64×** | +9.8 | 2e-20 | 37/44 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +9.4 | 4e-19 | 32/41 (NCI-H1792, HOP62, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +9.1 | 9e-18 | 33/40 (NCI-H1573, HOP62, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +6.9 | 4e-10 | 27/44 (A498, A549, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.75×** | +6.5 | 7e-09 | 26/45 (J82, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.22×** | +4.2 | 0.002 | 21/43 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +4.1 | 0.002 | 24/43 (A549, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 1.20× | +4.0 | 0.003 | 19/45 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.19× | +3.9 | 0.004 | 18/44 (J82, SK-MEL-2, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.19× | +3.9 | 0.005 | 18/44 (CFPAC-1, A549, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.8 | 0.005 | 20/44 (SNU-423, A-172, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.17× | +3.5 | 0.015 | 16/45 (MIA PaCa-2, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2668.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.476×** | -16.4 | 0e+00 | 38/44 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.499×** | -15.4 | 0e+00 | 39/44 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.649×** | -9.6 | 2e-19 | 33/44 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.698×** | -7.6 | 3e-12 | 32/43 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.777×** | -7.4 | 1e-11 | 27/45 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.762×** | -6.0 | 2e-07 | 27/44 (SK-MEL-2, NCI-H460, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.612×** | -5.7 | 1e-06 | 32/44 (SW1417, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.781×** | -5.4 | 4e-06 | 27/44 (A-172, SW1417, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.787×** | -5.3 | 8e-06 | 24/44 (SW480, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.797×** | -5.0 | 3e-05 | 24/44 (LS 180, KATO III, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.791×** | -4.9 | 6e-05 | 22/44 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.671×** | -4.6 | 2e-04 | 29/44 (LOX-IMVI, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.671×** | -4.6 | 2e-04 | 25/44 (SW1417, SW 1271, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.682×** | -4.4 | 4e-04 | 25/44 (SW1417, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.702×** | -4.1 | 0.002 | 30/44 (SW1417, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.816×** | -4.0 | 0.002 | 20/44 (RKO, H4, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.841× | -3.8 | 0.004 | 18/45 (KATO III, RKO, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.729×** | -3.6 | 0.008 | 25/45 (RKO, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.795×** | -3.6 | 0.009 | 23/44 (LOX-IMVI, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.796×** | -3.6 | 0.009 | 21/44 (LOX-IMVI, SW1417, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2668. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 495 | 9 (5 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +20.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.59× (z +17.7) | [[Panobinostat (drug)]] 5 µM 0.313× (z -16.0) |
| [[LOX-IMVI (line)]] | wt | 751 | 4 (2 ⚠) | 8 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.00× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.97× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.280× (z -21.7) |
| [[KATO III (line)]] | alt | 721 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.174× (z -22.0) |
| [[A549 (line)]] | wt | 230 | 8 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 4.29× (z +17.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -12.5) |
| [[HT-29 (line)]] | alt | 213 | 4 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +13.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.03× (z +10.3) | [[Ixazomib citrate (drug)]] 5 µM 0.530× (z -9.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.557× (z -8.9) |
| [[HOP62 (line)]] | alt | 238 | 7 (4 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 4.33× (z +17.0) | [[Panobinostat (drug)]] 0.5 µM 0.402× (z -10.5) |
| [[H4 (line)]] | wt | 364 | 7 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +14.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.85× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.449× (z -8.8) |
| [[HS-578T (line)]] | alt | 201 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +16.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.69× (z +15.4) | — |
| [[NCI-H460 (line)]] | wt | 361 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -13.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -11.8) |
| [[A498 (line)]] | wt | 435 | 5 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 3.45× (z +20.5) | [[Panobinostat (drug)]] 0.5 µM 0.399× (z -15.2) |
| [[LS 180 (line)]] | wt | 368 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.263× (z -21.4) |
| [[J82 (line)]] | alt | 309 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +20.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.61× (z +13.2) | [[Selinexor (drug)]] 5 µM 0.520× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.628× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 90.3 | 5 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.29× (z +13.1) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.420× (z -9.1) ⚠ cell-cycle shift, explains ~4% of this change |
| [[Panc 03.27 (line)]] | alt | 348 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 3.22× (z +15.5) | [[Panobinostat (drug)]] 5 µM 0.305× (z -15.7) |
| [[RKO (line)]] | wt | 297 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.389× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.477× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 476 | 0 | 6 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.257× (z -12.0) |
| [[SW 900 (line)]] | alt | 154 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.98× (z +18.3) | — |
| [[SW480 (line)]] | alt | 667 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -24.8) |
| [[HepG2_C3A (line)]] | wt | 278 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.297× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 312 | 0 | 5 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.550× (z -19.0) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -15.3) |
| [[NCI-H1792 (line)]] | alt | 321 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 2.63× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.30× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -12.2) |
| [[A-427 (line)]] | wt | 382 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.26× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.408× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 449 | 1 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.356× (z -14.1) |
| [[Hs 766T (line)]] | wt | 554 | 1 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.10× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.270× (z -15.9) |
| [[NCI-H1573 (line)]] | alt | 113 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.52× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 2.73× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 361 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -11.5) |
| [[PANC-1 (line)]] | alt | 334 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -15.2) |
| [[RPMI-7951 (line)]] | alt | 231 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.17× (z +13.6) | — |
| [[SNU-423 (line)]] | alt | 222 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +18.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.23× (z +16.4) | — |
| [[SW1417 (line)]] | alt | 268 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.403× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 237 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.392× (z -11.2) |
| [[C32 (line)]] | wt | 202 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 2.83× (z +10.6) | — |
| [[HEC-1-A (line)]] | alt | 140 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.399× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 247 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.09× (z +9.3) | — |
| [[LoVo (line)]] | wt | 309 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -12.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.572× (z -8.7) |
| [[AN3 CA (line)]] | alt | 397 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -8.8) |
| [[COLO 205 (line)]] | alt | 235 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.54× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 161 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.63× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +10.1) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 55.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 27.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 201 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 78.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 292 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 346 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 536 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 171 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2668), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENC1]] | +0.71 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[DDAH1]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[PLCB4]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[FAT1]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[CDH2]] | +0.68 | +0.67 / +0.59 | both halves | 7e-06 | STRING 509 |
| [[ZNF462]] | +0.65 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[CRIM1]] | +0.64 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[GNG12]] | +0.63 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[SLC39A10]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SEPTIN11]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[TPM1]] | +0.60 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[NAB1]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD7]] | -0.64 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[RAB6A]] | -0.62 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[ZFPL1]] | -0.61 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[TBC1D20]] | -0.61 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[MKNK2]] | -0.61 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[IL17RA]] | -0.61 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[TULP3]] | -0.60 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[ALKBH7]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[GUK1]] | -0.60 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[QPCTL]] | -0.59 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[SDHAP2]] | -0.59 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[PLD3]] | -0.59 | -0.60 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANAPC1P4]] | C | ANAPC1P4 activity raises CDK6's level | lines that do not express ANAPC1P4 (4) vs lines expressing it (46) | 2.13× lower at baseline in the lines without ANAPC1P4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP19, MIR4435-2HG, MSX1; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Pentoxifylline (drug)]] 0.5 µM | C | CDK6 activity raises the cells' numbers under Pentoxifylline 0.5 µM (protects the cells) | lines that do not express CDK6 (4) vs lines expressing it (44) | the lines without CDK6: 0.77× the cells of the other lines | 0.060 | ⚠ few lines (4 vs 46); across organs; also absent: FCHSD1, CDK6-AS1, PLS3 |
| [[SEPTIN11]] | C | CDK6 activity lowers SEPTIN11's level | lines that do not express CDK6 (4) vs lines expressing it (46) | 2.09× higher at baseline in the lines without CDK6 | 0.080 | ⚠ few lines (4 vs 46); across organs; also absent: FCHSD1, CDK6-AS1, PLS3 |
| [[ROCK2]] | C | CDK6 activity weakens ROCK2's drug response | lines that do not express CDK6 (4) vs lines expressing it (45) | the lines without CDK6 respond 1.63× as strongly (z diff -2.27); strongest at Homoharringtonine 0.5 µM: 1.92x vs 1.26x (z diff -6.9) | 0.081 | ⚠ few lines (4 vs 46); across organs; also absent: FCHSD1, CDK6-AS1, PLS3; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 197]] — Nervous system development; 16 genes; every member is in the + arm (projection on the module's main direction 0.743). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.7, 14.6); signed map (22.5, 19.0). **Vector** length 148, 48.8% of its response variance represented; |z| ≥ 3 in 1,672 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.5 | +11.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.5 | +14.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.9 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.8 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +9.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.4 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +0.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.1 | +1.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.0 | -7.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.5 | -5.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -5.3 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.1 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.1 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.8 | -6.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.8 | -3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.4 | -1.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.1 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.2 — chr7:92,604,921-92,836,573 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PLSTIRE |
| Gene groups (HGNC) | Cyclin dependent kinases |
| Hallmark sets | HEDGEHOG_SIGNALING, ANDROGEN_RESPONSE |
| Reactome | 24 pathways, smallest: Diseases of Cellular Senescence; Diseases of cellular response to stress; Evasion of Oncogene Induced Senescence Due to Defective p16INK4A binding to CDK4 and CDK6 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00534](https://www.uniprot.org/uniprotkb/Q00534) (Cyclin-dependent kinase 6):

> Serine/threonine-protein kinase involved in the control of the cell cycle and differentiation; promotes G1/S transition. Phosphorylates pRB/RB1 and NPM1. Interacts with D-type G1 cyclins during interphase at G1 to form a pRB/RB1 kinase and controls the entrance into the cell cycle. Involved in initiation and maintenance of cell cycle exit during cell differentiation; prevents cell proliferation and negatively regulates cell differentiation, but is required for the proliferation of specific cell …

**Summary**, from NCBI Gene [1021](https://www.ncbi.nlm.nih.gov/gene/1021):

> The protein encoded by this gene is a member of the CMGC family of serine/threonine protein kinases. This kinase is a catalytic subunit of the protein kinase complex that is important for cell cycle G1 phase progression and G1/S transition. The activity of this kinase first appears in mid-G1 phase, which is controlled by the regulatory subunits including D-type cyclins and members of INK4 family of CDK inhibitors. This kinase, as well as CDK4, has been shown to phosphorylate, and thus regulate …

**Accessions** — [HGNC:1777](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1777) · Entrez [1021](https://www.ncbi.nlm.nih.gov/gene/1021) · UniProt [Q00534](https://www.uniprot.org/uniprotkb/Q00534) · Ensembl [ENSG00000105810](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105810)

## Data

Gene col 2668: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2668); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2668, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2668]; `tensor/DDL_lfc|DDL_z.npy` [2668]; `embed/gene_vectors.npy` [2668]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2668 or target_col == 2668). Every well: [[CDK6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
