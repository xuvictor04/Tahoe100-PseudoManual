---
symbol: "TPM1"
type: "gene"
col: 6407
ensembl_id: "ENSG00000140416"
name: "tropomyosin 1"
location: "15q22.2"
module: 197
arm: "+"
pooled_cpm: 165.11
n_lines_expressing: 47
n_dd_up: 11
n_dd_down: 22
n_dd_up_clean: 7
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 9
direction_downstream: 4
tags: ["gene", "module/197"]
generated_by: "tahoemap"
---

# TPM1

*tropomyosin 1* — 15q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.94× (z +22.2, q 0e+00, up in 44 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.31× (z +4.2, q 0.004, up in 21 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.660× (z -9.5, q 1e-18, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYLK]] (+0.67, fdr 7e-06), [[ACTR3]] (+0.64, fdr 1e-05), [[CDH2]] (+0.62, fdr 7e-06); moves opposite to [[IL17RA]] (-0.64, fdr 1e-05), [[NUDT22]] (-0.58, fdr 2e-04), [[PRKRIP1]] (-0.56, fdr 2e-05).
> It is in [[Module 197]], a single-armed module (Nervous system development).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[KIRREL3]] → it (grade B ⚠); 4 go from it, the strongest it → [[THBS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6407.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.94×** | +22.2 | 0e+00 | 44/46 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.60×** | +19.9 | 0e+00 | 39/40 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +14.1 | 4e-43 | 40/42 (C-33 A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +4.2 | 0.004 | 21/45 (C32, NCI-H1792, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.9 | 0.012 | 1/47 (HOP62) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.031 | 17/45 (KATO III, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.038 | 19/46 (HOP62, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.16× | +3.4 | 0.042 | 18/46 (A498, NCI-H1792, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.20× | +3.4 | 0.045 | 21/45 (RKO, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.20×** | +3.3 | 0.057 | 19/47 (H4, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.057 | 21/44 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.057 | 19/45 (C32, HS-578T, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.060 | 19/45 (A498, NCI-H1792, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.060 | 11/45 (A549, A-172, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.071 | 12/45 (BT-474, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6407.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -9.5 | 1e-18 | 31/46 (LoVo, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.604×** | -8.2 | 1e-13 | 35/45 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.624×** | -7.6 | 4e-12 | 34/45 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.654×** | -6.9 | 9e-10 | 37/45 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.664×** | -6.6 | 4e-09 | 30/45 (LoVo, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.667×** | -6.6 | 5e-09 | 32/45 (LoVo, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.614×** | -6.2 | 6e-08 | 32/45 (A498, A549, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.695×** | -5.9 | 3e-07 | 28/45 (LoVo, A498, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.543×** | -5.2 | 2e-05 | 25/42 (A498, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.738×** | -4.9 | 5e-05 | 31/45 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.744×** | -4.8 | 9e-05 | 27/45 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.812×** | -4.7 | 1e-04 | 23/45 (A498, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.762×** | -4.4 | 5e-04 | 24/45 (LoVo, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.762×** | -4.4 | 5e-04 | 23/45 (LoVo, J82, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.766×** | -4.3 | 7e-04 | 25/45 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.829×** | -4.3 | 7e-04 | 23/45 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.719×** | -3.8 | 0.005 | 19/45 (LoVo, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.799×** | -3.5 | 0.012 | 19/44 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.667×** | -3.4 | 0.018 | 17/45 (LoVo, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.757×** | -3.2 | 0.038 | 16/46 (A498, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.685×** | -3.2 | 0.038 | 15/45 (A498, J82, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.831×** | -3.0 | 0.072 | 20/45 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6407. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 269 | 0 | 20 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -32.5) |
| [[A498 (line)]] | wt | 374 | 3 (3 ⚠) | 6 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +17.4) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.429× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 623 | 1 (1 ⚠) | 8 (5 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +8.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -16.3) |
| [[A549 (line)]] | wt | 353 | 3 (3 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +14.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -11.0) |
| [[PANC-1 (line)]] | alt | 324 | 2 (2 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +9.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -14.2) |
| [[J82 (line)]] | alt | 380 | 1 (1 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +8.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.288× (z -10.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 218 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -18.0) |
| [[CFPAC-1 (line)]] | alt | 356 | 4 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +13.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -9.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HepG2_C3A (line)]] | wt | 201 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -11.9) |
| [[HOP62 (line)]] | alt | 239 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +13.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -10.7) |
| [[LS 180 (line)]] | wt | 190 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -13.7) |
| [[HS-578T (line)]] | alt | 310 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +12.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.375× (z -8.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H1573 (line)]] | alt | 47.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.43× (z +16.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 106 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.10× (z +17.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 77.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -9.1) |
| [[SNU-423 (line)]] | alt | 324 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.51× (z +12.5) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.229× (z -8.8) |
| [[A-172 (line)]] | wt | 304 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -11.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[BT-474 (line)]] | alt | 158 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.356× (z -10.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.426× (z -8.8) |
| [[C-33 A (line)]] | alt | 49.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.68× (z +16.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 50.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.36× (z +12.1) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 139 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +10.3) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.198× (z -10.8) |
| [[HT-29 (line)]] | alt | 130 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +9.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 257 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +11.1) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.293× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 65.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 143 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +15.2) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 57.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -8.8) |
| [[SW 900 (line)]] | alt | 48.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.18× (z +12.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 54.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.03× (z +9.2) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 66.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -13.3) |
| [[HEC-1-A (line)]] | alt | 67.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +10.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 86.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 90.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 50.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.35× (z +13.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 53.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 59.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +11.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 62.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.67× (z +15.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 49.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.56× (z +13.1) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 301 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -10.1) |
| [[SW 1271 (line)]] | alt | 71.3 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.101× (z -9.0) |
| [[SW1417 (line)]] | alt | 90.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 51.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.26× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 29.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 328 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 50.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6407), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYLK]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 857 |
| [[ACTR3]] | +0.64 | +0.52 / +0.62 | both halves | 1e-05 | STRING 413 |
| [[CDH2]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[MYH9]] | +0.61 | +0.50 / +0.62 | both halves | 1e-05 | STRING 765 |
| [[NUAK2]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[THBS1]] | +0.60 | +0.46 / +0.59 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[CDK6]] | +0.60 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[PLCB4]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[CCDC50]] | +0.56 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[COL12A1]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[CRIM1]] | +0.55 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[PLS3]] | +0.55 | +0.37 / +0.59 | both halves | 8e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL17RA]] | -0.64 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[NUDT22]] | -0.58 | -0.32 / -0.65 | both halves | 2e-04 |  |
| [[PRKRIP1]] | -0.56 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[EEF1AKMT4]] | -0.55 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[ITPKA]] | -0.53 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[POM121C]] | -0.52 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[TMEM101]] | -0.51 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[MRPS12]] | -0.50 | -0.24 / -0.54 | both halves | 5e-04 |  |
| [[ISCA1]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[GAN]] | -0.50 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[TMEM258]] | -0.49 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[FASTKD1]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIRREL3]] | B | KIRREL3 activity raises TPM1's level | lines that do not express KIRREL3 (36) vs lines expressing it (14) | 2.76× lower at baseline in the lines without KIRREL3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN |
| [[GPR176]] | B | GPR176 activity raises TPM1's level | lines that do not express GPR176 (18) vs lines expressing it (32) | 2.21× lower at baseline in the lines without GPR176 | 0.007 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, AFAP1L1 |
| [[AMIGO2]] | B | AMIGO2 activity raises TPM1's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 2.46× lower at baseline in the lines without AMIGO2 | 0.014 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers TPM1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MXRA5]] | B | MXRA5 activity raises TPM1's level | lines that do not express MXRA5 (34) vs lines expressing it (16) | 2.64× lower at baseline in the lines without MXRA5 | 0.046 | ⚠ within organs, on part of the lines; also absent: IRAG2, VCAM1, LINC02476 |
| [[CDH2]] | B | CDH2 activity raises TPM1's level | lines that do not express CDH2 (22) vs lines expressing it (28) | 2.41× lower at baseline in the lines without CDH2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ARMCX1, DKK3, RFTN1 |
| [[KIRREL3]] | B | KIRREL3 activity strengthens TPM1's drug response | lines that do not express KIRREL3 (33) vs lines expressing it (13) | the lines without KIRREL3 respond 0.72× as strongly (z diff +1.67); strongest at Ixazomib citrate 5 µM: 0.63x vs 0.37x (z diff +4.0) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN; target measured in part of the lines; artifact flags |
| [[P3H2]] | B | P3H2 activity raises TPM1's level | lines that do not express P3H2 (28) vs lines expressing it (22) | 1.93× lower at baseline in the lines without P3H2 | 0.077 | ⚠ within organs, on part of the lines; also absent: P3H2-AS1, SRGN, SPOCK1 |
| [[MYLK]] | B | MYLK activity raises TPM1's level | lines that do not express MYLK (20) vs lines expressing it (30) | 2.13× lower at baseline in the lines without MYLK | 0.085 | ⚠ within organs, on part of the lines; also absent: ADAMTS2, COL4A1, CPEB1 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THBS1]] | C | TPM1 activity raises THBS1's level | lines that do not express TPM1 (3) vs lines expressing it (47) | 8.74× lower at baseline in the lines without TPM1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, SSUH2, XIRP2; maybe low, not absent; its own permutation p |
| [[DST]] | C | TPM1 activity lowers DST's level | lines that do not express TPM1 (3) vs lines expressing it (47) | 2.80× higher at baseline in the lines without TPM1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, SSUH2, XIRP2; maybe low, not absent; its own permutation p |
| [[MYH9]] | C | TPM1 activity raises MYH9's level | lines that do not express TPM1 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without TPM1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, SSUH2, XIRP2; maybe low, not absent; its own permutation p |
| [[CDH2]] | C | TPM1 activity raises CDH2's level | lines that do not express TPM1 (3) vs lines expressing it (47) | 4.23× lower at baseline in the lines without TPM1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, SSUH2, XIRP2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 197]] — Nervous system development; 16 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.4, 15.4); signed map (45.7, 18.6). **Vector** length 120, 37.2% of its response variance represented; |z| ≥ 3 in 1,356 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.8 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +22.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +19.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | -4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.6 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.3 | +3.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.2 | +3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -9.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.0 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.7 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.5 | -8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -4.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.1 | -4.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.4 | -3.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.9 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | tropomyosin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.2 — chr15:63,042,620-63,071,915 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C15orf13, CMH3 |
| Gene groups (HGNC) | Tropomyosins |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 3 pathways, smallest: Striated Muscle Contraction; Smooth Muscle Contraction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [P09493](https://www.uniprot.org/uniprotkb/P09493) (Tropomyosin alpha-1 chain):

> Binds to actin filaments in muscle and non-muscle cells. Plays a central role, in association with the troponin complex, in the calcium dependent regulation of vertebrate striated muscle contraction. Smooth muscle contraction is regulated by interaction with caldesmon. In non-muscle cells is implicated in stabilizing cytoskeleton actin filaments.

**Summary**, from NCBI Gene [7168](https://www.ncbi.nlm.nih.gov/gene/7168):

> This gene is a member of the tropomyosin family of highly conserved, widely distributed actin-binding proteins involved in the contractile system of striated and smooth muscles and the cytoskeleton of non-muscle cells. Tropomyosin is composed of two alpha-helical chains arranged as a coiled-coil. It is polymerized end to end along the two grooves of actin filaments and provides stability to the filaments. The encoded protein is one type of alpha helical chain that forms the predominant …

**Accessions** — [HGNC:12010](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12010) · Entrez [7168](https://www.ncbi.nlm.nih.gov/gene/7168) · UniProt [P09493](https://www.uniprot.org/uniprotkb/P09493) · Ensembl [ENSG00000140416](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140416)

## Data

Gene col 6407: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6407); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6407, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6407]; `tensor/DDL_lfc|DDL_z.npy` [6407]; `embed/gene_vectors.npy` [6407]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6407 or target_col == 6407). Every well: [[TPM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
