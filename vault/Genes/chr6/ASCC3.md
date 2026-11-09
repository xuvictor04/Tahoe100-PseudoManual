---
symbol: "ASCC3"
type: "gene"
col: 3344
ensembl_id: "ENSG00000112249"
name: "activating signal cointegrator 1 complex subunit 3"
location: "6q16.3"
module: 62
arm: "+"
pooled_cpm: 302.36
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# ASCC3

*activating signal cointegrator 1 complex subunit 3* — 6q16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.60× (z +12.0, q 2e-30, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.532× (z -14.5, q 3e-45, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.785× (z -8.2, q 5e-14, down in 28 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTCHD4]] (+0.56, fdr 4e-05), [[ACTA2]] (+0.53, fdr 3e-05), [[ZMAT3]] (+0.51, fdr 5e-05); moves opposite to [[ZNF823]] (-0.46, fdr 1e-04), [[RAD9A]] (-0.43, fdr 4e-05), [[PAK4]] (-0.43, fdr 1e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PINCR]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZNG1A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3344.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.60×** | +12.0 | 2e-30 | 47/49 (NCI-H460, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +7.9 | 6e-13 | 32/48 (RKO, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +7.6 | 7e-12 | 32/48 (PANC-1, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +7.3 | 3e-11 | 37/48 (LS 180, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +5.8 | 6e-07 | 27/48 (SNU-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +5.8 | 8e-07 | 26/48 (SW48, RKO, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.54×** | +5.4 | 5e-06 | 37/48 (HOP62, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.22×** | +4.4 | 8e-04 | 23/45 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.20× | +4.4 | 8e-04 | 23/48 (MIA PaCa-2, SNU-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.16× | +3.5 | 0.025 | 14/47 (SNU-1, HOP62, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.15× | +3.3 | 0.056 | 14/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.2 | 0.071 | 20/48 (SNU-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.080 | 16/48 (SNU-1, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3344.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.532×** | -14.5 | 3e-45 | 41/44 (hTERT-HPNE, J82, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.552×** | -14.2 | 1e-43 | 42/49 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.785×** | -8.2 | 5e-14 | 28/49 (NCI-H1792, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.731×** | -7.5 | 8e-12 | 39/48 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.734×** | -7.4 | 2e-11 | 29/48 (A549, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.748×** | -7.0 | 3e-10 | 36/48 (hTERT-HPNE, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.751×** | -6.9 | 5e-10 | 31/48 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.775×** | -5.9 | 3e-07 | 31/47 (NCI-H1573, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -4.1 | 0.002 | 21/48 (NCI-H2030, NCI-H1573, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~9% of this change | 0.840× | -4.0 | 0.003 | 23/47 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.856× | -3.7 | 0.010 | 17/48 (CFPAC-1, H4, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.744×** | -3.7 | 0.010 | 26/48 (RPMI-7951, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.896× | -3.7 | 0.010 | 8/48 (AsPC-1, NCI-H1792, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.864× | -3.5 | 0.020 | 17/48 (CFPAC-1, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.867× | -3.4 | 0.022 | 17/48 (C32, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.867× | -3.4 | 0.022 | 14/48 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.802×** | -3.2 | 0.045 | 23/48 (A-427, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.876× | -3.2 | 0.047 | 14/48 (BT-474, J82, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.882× | -3.0 | 0.072 | 9/48 (COLO 205, CFPAC-1, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.879× | -3.0 | 0.081 | 17/48 (C32, NCI-H1573, …) | top dose only |  |
| [[DTP3 (drug)]] 5 µM |  | **0.792×** | -2.9 | 0.086 | 15/48 (Hs 766T, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.820×** | -2.9 | 0.096 | 14/48 (NCI-H2030, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3344. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 376 | 14 (9 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.55× (z +16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.80× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -12.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 335 | 9 (4 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.54× (z +14.8) | [[Auranofin (drug)]] 5 µM 0.499× (z -10.5) |
| [[A-172 (line)]] | wt | 371 | 3 (1 ⚠) | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.91× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.491× (z -10.7) |
| [[LS 180 (line)]] | wt | 292 | 6 (4 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.71× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 504 | 3 (1 ⚠) | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.95× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -24.0) |
| [[PANC-1 (line)]] | alt | 358 | 4 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.26× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.458× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -12.7) |
| [[RKO (line)]] | wt | 407 | 7 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 4.80× (z +19.6) | [[Auranofin (drug)]] 5 µM 0.434× (z -10.4) |
| [[A549 (line)]] | wt | 346 | 3 (1 ⚠) | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.62× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -22.8) |
| [[C32 (line)]] | wt | 385 | 2 (1 ⚠) | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.34× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 591 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -13.6) |
| [[SW48 (line)]] | wt | 270 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 3.35× (z +13.5) | — |
| [[A498 (line)]] | wt | 303 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.59× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.528× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.572× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 501 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.98× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.382× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 293 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +20.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.70× (z +14.7) | — |
| [[NCI-H1573 (line)]] | alt | 267 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.421× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 194 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +17.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.19× (z +14.6) | — |
| [[BT-474 (line)]] | alt | 495 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -13.7) |
| [[C-33 A (line)]] | alt | 423 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -8.8) |
| [[H4 (line)]] | wt | 341 | 2 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.94× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.63× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.343× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.416× (z -10.5) |
| [[HOP62 (line)]] | alt | 282 | 0 | 4 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.444× (z -12.6) ⚠ transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.652× (z -9.3) |
| [[J82 (line)]] | alt | 319 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -16.4) |
| [[LOX-IMVI (line)]] | wt | 484 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.92× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.439× (z -11.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 335 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -13.5) |
| [[AN3 CA (line)]] | alt | 368 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.331× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -9.2) |
| [[HT-29 (line)]] | alt | 283 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +16.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.57× (z +14.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.542× (z -8.8) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 394 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.40× (z +16.1) | — |
| [[CFPAC-1 (line)]] | alt | 192 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.535× (z -10.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 324 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -12.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 260 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.482× (z -12.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 242 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.04× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 324 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 313 | 2 | 0 | [[Atazanavir (sulfate) (drug)]] 5 µM 1.93× (z +13.6) | — |
| [[Panc 03.27 (line)]] | alt | 151 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.333× (z -14.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 336 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.425× (z -11.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 282 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.19× (z +11.3) | — |
| [[A-427 (line)]] | wt | 279 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.22× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 259 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.427× (z -12.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 290 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.459× (z -8.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 309 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.647× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 274 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.90× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 303 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.586× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 245 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.212× (z -10.7) |
| [[SW480 (line)]] | alt | 177 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 1.58× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 292 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 287 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 345 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 132 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3344), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTCHD4]] | +0.56 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[ACTA2]] | +0.53 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[ZMAT3]] | +0.51 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[PURPL]] | +0.50 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[RRM2B]] | +0.48 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[SPATA18]] | +0.48 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[PINCR]] | +0.47 | +0.36 / +0.44 | both halves | 1e-04 |  |
| [[TMEM131]] | +0.47 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[RB1]] | +0.47 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[CEP85L]] | +0.47 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[AEN]] | +0.46 | +0.37 / +0.47 | both halves | 8e-05 |  |
| [[TIGAR]] | +0.46 | +0.45 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF823]] | -0.46 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[RAD9A]] | -0.43 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[PAK4]] | -0.43 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[DNMT3B]] | -0.42 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[SLC8B1]] | -0.42 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[TAF6L]] | -0.41 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[FOXK1]] | -0.41 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[TECR]] | -0.40 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[SLC35D2]] | -0.39 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[KIAA1671]] | -0.39 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[CDC42EP4]] | -0.39 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[LMBR1L]] | -0.39 | -0.28 / -0.44 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PINCR]] | B | PINCR activity strengthens ASCC3's drug response | lines that do not express PINCR (29) vs lines expressing it (20) | the lines without PINCR respond 0.79× as strongly (z diff +1.30); rises at some drug-doses, falls at others (56% from rises): Panobinostat 5 µM: 0.86x vs 0.63x (z diff +4.0); PH-797804 5 µM: 1.63x vs 2.64x (z diff +3.0); TAK-901 5 µM: 2.33x vs 4.18x (z diff +2.5) | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[PINCR]] | B | PINCR activity raises ASCC3's level | lines that do not express PINCR (29) vs lines expressing it (21) | 1.25× lower at baseline in the lines without PINCR | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[FBXO22]] | C | FBXO22's natural level strengthens ASCC3's drug response | FBXO22's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.44; direction not clear | 0.013 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[AEN]] | C | AEN's natural level strengthens ASCC3's drug response | AEN's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.59; direction not clear | 0.091 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[TP53]] | C | TP53 activity strengthens ASCC3's drug response | recorded loss-of-function mutation of TP53 in 32 lines vs 17 not recorded | the TP53-altered lines respond 0.74× as strongly (z diff +1.34); rises at some drug-doses, falls at others (69% from rises): Panobinostat 5 µM: 0.85x vs 0.63x (z diff +3.6); PH-797804 5 µM: 1.59x vs 2.90x (z diff +3.6); TAK-901 5 µM: 2.27x vs 4.87x (z diff +3.4) | 0.471 over the table, 0.023 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNG1A]] | C | ASCC3's natural level weakens ZNG1A's drug response | ASCC3's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.20; direction not clear | 0.096 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.478). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.5, 37.3); signed map (43.2, -24.6). **Vector** length 130, 46.3% of its response variance represented; |z| ≥ 3 in 1,473 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.1 | +4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.5 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.4 | +5.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.1 | +12.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +0.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +4.0 | +0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.8 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | -1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +1.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.2 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -3.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.4 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -4.2 | -1.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.6 | -3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | activating signal cointegrator 1 complex subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.3 — chr6:100,508,194-100,881,372 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNAH, ASC1p200, dJ121G13.4, dJ467N11.1; previously HELIC1 |
| Gene groups (HGNC) | Activating signal cointegrator 1 complex; DexD/H helicases |
| Reactome | 7 pathways, smallest: ALKBH3 mediated reversal of alkylation damage; Reversal of alkylation damage by DNA dioxygenases; DNA Damage Reversal |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3C0](https://www.uniprot.org/uniprotkb/Q8N3C0) (Activating signal cointegrator 1 complex subunit 3):

> ATPase involved both in DNA repair and rescue of stalled ribosomes. 3'-5' DNA helicase involved in repair of alkylated DNA: promotes DNA unwinding to generate single-stranded substrate needed for ALKBH3, enabling ALKBH3 to process alkylated N3-methylcytosine (3mC) within double-stranded regions. Also involved in activation of the ribosome quality control (RQC) pathway, a pathway that degrades nascent peptide chains during problematic translation. Drives the splitting of stalled ribosomes that …

**Summary**, from NCBI Gene [10973](https://www.ncbi.nlm.nih.gov/gene/10973):

> This gene encodes a protein that belongs to a family of helicases that are involved in the ATP-dependent unwinding of nucleic acid duplexes. The encoded protein is the largest subunit of the activating signal cointegrator 1 complex that is involved in DNA repair and resistance to alkylation damage. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:18697](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18697) · Entrez [10973](https://www.ncbi.nlm.nih.gov/gene/10973) · UniProt [Q8N3C0](https://www.uniprot.org/uniprotkb/Q8N3C0) · Ensembl [ENSG00000112249](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112249)

## Data

Gene col 3344: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3344); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3344, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3344]; `tensor/DDL_lfc|DDL_z.npy` [3344]; `embed/gene_vectors.npy` [3344]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3344 or target_col == 3344). Every well: [[ASCC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASCC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
