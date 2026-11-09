---
symbol: "IQGAP1"
type: "gene"
col: 6434
ensembl_id: "ENSG00000140575"
name: "IQ motif containing GTPase activating protein 1"
location: "15q26.1"
module: 111
arm: "+"
pooled_cpm: 427.49
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# IQGAP1

*IQ motif containing GTPase activating protein 1* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.58× (z +11.3, q 8e-27, up in 41 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.21× (z +4.7, q 4e-04, up in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (PANC-1 2.79×, C-33 A 3.64×, SW1417 1.85×, NCI-H23 2.23×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 2.57×, A-427 2.70×, MIA PaCa-2 2.49×, C-33 A 3.32×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 2.90×, PANC-1 2.16×, C-33 A 4.01×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 1.68×, BT-474 1.44×); [[TAK-901 (drug)]] 5 µM in 1 line (BT-474 5.51×).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.636× (z -10.8, q 2e-24, down in 38 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.781× (z -8.7, q 1e-15, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAST]] (+0.71, fdr 7e-06), [[TPM3]] (+0.69, fdr 7e-06), [[AIDA]] (+0.66, fdr 7e-06); moves opposite to [[COIL]] (-0.60, fdr 1e-05), [[YTHDF2]] (-0.59, fdr 1e-05), [[ZCCHC3]] (-0.58, fdr 3e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6434.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (PANC-1 2.79×, C-33 A 3.64×, SW1417 1.85×, NCI-H23 2.23×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 2.57×, A-427 2.70×, MIA PaCa-2 2.49×, C-33 A 3.32×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 2.90×, PANC-1 2.16×, C-33 A 4.01×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 1.68×, BT-474 1.44×); [[TAK-901 (drug)]] 5 µM in 1 line (BT-474 5.51×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +11.3 | 8e-27 | 41/49 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +9.6 | 2e-19 | 39/44 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +6.1 | 2e-07 | 32/45 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.7 | 4e-04 | 26/48 (SW48, SW480, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.21×** | +4.6 | 6e-04 | 24/47 (H4, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +4.3 | 0.002 | 23/47 (SK-MEL-2, RPMI-7951, …) | rises with dose | low cells (technical?) |
| [[Artesunate (drug)]] 0.5 µM |  | 1.16× | +3.6 | 0.027 | 13/48 (hTERT-HPNE, A549, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.4 | 0.054 | 18/48 (SW480, SW48, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6434.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.636×** | -10.8 | 2e-24 | 38/47 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.781×** | -8.7 | 1e-15 | 29/48 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.747×** | -7.2 | 8e-11 | 36/48 (C32, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.838× | -6.2 | 8e-08 | 22/48 (NCI-H2347, RKO, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.804×** | -5.4 | 7e-06 | 27/48 (HEC-1-A, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.812×** | -5.2 | 2e-05 | 26/48 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.679×** | -5.0 | 4e-05 | 34/48 (MIA PaCa-2, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.763×** | -4.8 | 1e-04 | 37/48 (hTERT-HPNE, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.873× | -4.8 | 1e-04 | 20/49 (NCI-H1792, A549, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.699×** | -4.6 | 2e-04 | 29/49 (CFPAC-1, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.891× | -4.0 | 0.003 | 12/48 (A549, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -3.9 | 0.005 | 21/48 (SK-MEL-2, HEC-1-A, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | 0.856× | -3.9 | 0.005 | 20/48 (NCI-H23, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.858× | -3.8 | 0.006 | 20/48 (SNU-423, H4, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.754×** | -3.7 | 0.009 | 23/48 (LS 180, HOP62, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | **0.817×** | -3.6 | 0.012 | 25/49 (PANC-1, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.820×** | -3.5 | 0.015 | 26/48 (MIA PaCa-2, HT-29, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.868× | -3.3 | 0.026 | 18/47 (SW48, SW1417, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.876× | -3.3 | 0.031 | 9/48 (H4, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6434. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 467 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.80× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.572× (z -14.6) |
| [[KATO III (line)]] | alt | 444 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.04× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -18.4) |
| [[LS 180 (line)]] | wt | 463 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.73× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -19.0) |
| [[A-427 (line)]] | wt | 147 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 2.90× (z +14.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.611× (z -10.3) |
| [[C32 (line)]] | wt | 429 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.84× (z +10.3) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.494× (z -12.4) |
| [[NCI-H1792 (line)]] | alt | 515 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -15.6) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.531× (z -9.2) |
| [[PANC-1 (line)]] | alt | 398 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +20.8) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.572× (z -10.8) ⚠ toxic |
| [[SW48 (line)]] | wt | 246 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.49× (z +12.0) ⚠ toxic; transcription drop | [[TAK-901 (drug)]] 0.05 µM 0.516× (z -8.5) |
| [[BT-474 (line)]] | alt | 360 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.51× (z +15.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -13.1) ⚠ cell-cycle shift, explains ~5% of this change |
| [[C-33 A (line)]] | alt | 136 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +14.3) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 552 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.581× (z -13.7) |
| [[HOP62 (line)]] | alt | 531 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -12.7) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.550× (z -9.6) |
| [[LoVo (line)]] | wt | 503 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.624× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 430 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.49× (z +13.6) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.495× (z -11.0) |
| [[SK-MEL-2 (line)]] | alt | 319 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.81× (z +9.5) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.441× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.649× (z -9.9) |
| [[SW1417 (line)]] | alt | 300 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.85× (z +12.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 290 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.02× (z +11.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 716 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.466× (z -12.9) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.551× (z -10.5) |
| [[A498 (line)]] | wt | 555 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.79× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 270 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.651× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 475 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.80× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.654× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 249 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 406 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.82× (z +10.7) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.501× (z -12.0) ⚠ toxic |
| [[A549 (line)]] | wt | 650 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -14.8) ⚠ cell-cycle shift, explains ~5% of this change |
| [[AN3 CA (line)]] | alt | 253 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.90× (z +9.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 492 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.499× (z -10.5) ⚠ toxic |
| [[H4 (line)]] | wt | 402 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.606× (z -9.6) |
| [[HCT15 (line)]] | alt | 383 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.652× (z -8.8) ⚠ cell-cycle shift, explains ~5% of this change |
| [[HS-578T (line)]] | alt | 469 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.499× (z -11.2) ⚠ toxic |
| [[HT-29 (line)]] | alt | 492 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.660× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 621 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.570× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 401 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.538× (z -9.9) ⚠ toxic |
| [[NCI-H661 (line)]] | alt | 328 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.248× (z -10.9) |
| [[RKO (line)]] | wt | 290 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 202 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.95× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 315 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.79× (z +9.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 206 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 418 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 181 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 442 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 487 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 520 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 398 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 456 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 364 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 620 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 335 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 438 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 566 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 592 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6434), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAST]] | +0.71 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[TPM3]] | +0.69 | +0.70 / +0.65 | both halves | 7e-06 | pathway: RHOV GTPase cycle; STRING 564 |
| [[AIDA]] | +0.66 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[RHOA]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 | pathway: RHO GTPase Effectors; STRING 880 |
| [[ANXA2]] | +0.62 | +0.58 / +0.67 | both halves | 7e-06 | STRING 680 |
| [[RALB]] | +0.61 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[DIAPH1]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 | pathway: RHO GTPase Effectors; STRING 731 |
| [[APLP2]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[DYNC1H1]] | +0.60 | +0.46 / +0.66 | both halves | 3e-05 | pathway: RHO GTPase Effectors |
| [[TMOD3]] | +0.60 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[YWHAZ]] | +0.59 | +0.53 / +0.70 | both halves | 1e-05 | pathway: RHO GTPase Effectors |
| [[SPTAN1]] | +0.59 | +0.39 / +0.54 | both halves | 5e-05 | pathway: Cell-Cell communication; STRING 753 |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COIL]] | -0.60 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[YTHDF2]] | -0.59 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[ZCCHC3]] | -0.58 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[NAPEPLD]] | -0.57 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[THUMPD2]] | -0.57 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[HOXC8]] | -0.57 | -0.48 / -0.44 | both halves | 3e-05 | pathway: Cell-Cell communication |
| [[NCBP2AS2]] | -0.57 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[SETDB1]] | -0.56 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[ALKBH4]] | -0.55 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[MRPL32]] | -0.54 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[SMAD1]] | -0.54 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[MRPL44]] | -0.54 | -0.38 / -0.55 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | IQGAP1's natural level raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | IQGAP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64 | 0.390 over the table, 0.057 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | IQGAP1's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | IQGAP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63 | 0.412 over the table, 0.052 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | IQGAP1's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | IQGAP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.60 | 0.472 over the table, 0.074 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.721). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.8, 9.7); signed map (-10.2, 34.3). **Vector** length 160, 58.5% of its response variance represented; |z| ≥ 3 in 1,485 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *RHO GTPases activate PAKs* (reactome, mean cos +0.51 to 4); *G-protein beta:gamma signalling* (reactome, mean cos +0.50 to 4); *RHO GTPases activate PKNs* (reactome, mean cos +0.54 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.1 | +11.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +8.0 | +1.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.8 | +0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.7 | +9.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +5.6 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | +4.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +4.3 | +3.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | +3.7 | +2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +3.2 | +2.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -12.0 | -10.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.0 | -7.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -6.4 | -6.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.1 | -4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.3 | -4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.2 | -3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.9 | -3.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.6 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | IQ motif containing GTPase activating protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:90,388,242-90,502,239 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p195, KIAA0051, SAR1, HUMORFA01 |
| Gene groups (HGNC) | IQ motif containing GTPase activating protein family |
| Reactome | 33 pathways, smallest: Nephrin family interactions; RHO GTPases activate IQGAPs; Glucagon-like Peptide-1 (GLP1) regulates insulin secretion |
| Matched by | ensembl_id |

**Function**, from UniProt [P46940](https://www.uniprot.org/uniprotkb/P46940) (Ras GTPase-activating-like protein IQGAP1):

> Plays a crucial role in regulating the dynamics and assembly of the actin cytoskeleton. Recruited to the cell cortex by interaction with ILK which allows it to cooperate with its effector DIAPH1 to locally stabilize microtubules and allow stable insertion of caveolae into the plasma membrane (By similarity). Binds to activated CDC42 but does not stimulate its GTPase activity. Associates with calmodulin. May promote neurite outgrowth. May play a possible role in cell cycle regulation by …

**Summary**, from NCBI Gene [8826](https://www.ncbi.nlm.nih.gov/gene/8826):

> This gene encodes a member of the IQGAP family. The protein contains four IQ domains, one calponin homology domain, one Ras-GAP domain and one WW domain. It interacts with components of the cytoskeleton, with cell adhesion molecules, and with several signaling molecules to regulate cell morphology and motility. Expression of the protein is upregulated by gene amplification in two gastric cancer cell lines. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6110](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6110) · Entrez [8826](https://www.ncbi.nlm.nih.gov/gene/8826) · UniProt [P46940](https://www.uniprot.org/uniprotkb/P46940) · Ensembl [ENSG00000140575](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140575)

## Data

Gene col 6434: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6434); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6434, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6434]; `tensor/DDL_lfc|DDL_z.npy` [6434]; `embed/gene_vectors.npy` [6434]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6434 or target_col == 6434). Every well: [[IQGAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IQGAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
