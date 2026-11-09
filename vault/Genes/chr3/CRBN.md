---
symbol: "CRBN"
type: "gene"
col: 3509
ensembl_id: "ENSG00000113851"
name: "cereblon"
location: "3p26.2"
module: 74
arm: "+"
pooled_cpm: 42.06
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 22
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# CRBN

*cereblon* — 3p26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.50× (z +8.7, q 2e-15, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.381× (z -20.7, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.575× (z -16.8, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM23]] (+0.75, fdr 7e-06), [[WDR48]] (+0.74, fdr 7e-06), [[ASB8]] (+0.72, fdr 7e-06); moves opposite to [[HCFC1]] (-0.59, fdr 2e-05), [[SUV39H2]] (-0.58, fdr 1e-05), [[CYCS]] (-0.57, fdr 4e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[WDR48]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3509.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +8.7 | 2e-15 | 39/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +7.2 | 2e-10 | 34/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +6.5 | 1e-08 | 28/47 (LS 180, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +6.2 | 1e-07 | 28/48 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.1 | 4e-05 | 20/47 (LS 180, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +5.1 | 4e-05 | 23/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.17× | +4.9 | 9e-05 | 21/48 (SW480, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +4.3 | 0.001 | 15/48 (HOP62, HT-29, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.007 | 14/47 (SK-MEL-2, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.008 | 14/48 (A-172, hTERT-HPNE, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.8 | 0.008 | 11/48 (AsPC-1, RPMI-7951, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.18× | +3.6 | 0.013 | 11/48 (SNU-1, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.017 | 15/48 (LOX-IMVI, A-427, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.019 | 12/47 (LoVo, SNU-1, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.18× | +3.5 | 0.019 | 8/48 (HS-578T, SW48, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.17× | +3.2 | 0.045 | 7/48 (AN3 CA, HepG2/C3A, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.11× | +3.1 | 0.054 | 7/48 (A498, CFPAC-1, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.15× | +3.0 | 0.078 | 7/48 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.16× | +2.9 | 0.100 | 8/48 (HEC-1-A, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3509.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.381×** | -20.7 | 0e+00 | 47/48 (SW1417, NCI-H1792, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.575×** | -16.8 | 0e+00 | 42/48 (RKO, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.401×** | -10.2 | 3e-22 | 45/48 (SW1417, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.424×** | -9.6 | 1e-19 | 41/48 (A549, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.440×** | -9.2 | 5e-18 | 41/48 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.566×** | -8.7 | 3e-16 | 43/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.469×** | -8.5 | 2e-15 | 39/48 (NCI-H2347, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.504×** | -7.7 | 1e-12 | 35/48 (Hs 766T, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.707×** | -7.1 | 6e-11 | 26/38 (SW480, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.724×** | -6.9 | 3e-10 | 24/47 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.735×** | -6.6 | 2e-09 | 28/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.738×** | -6.5 | 3e-09 | 25/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.725×** | -6.5 | 3e-09 | 30/48 (LoVo, SW 900, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.745×** | -6.3 | 1e-08 | 27/48 (SNU-423, SW480, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.708×** | -5.3 | 5e-06 | 23/48 (NCI-H460, SNU-423, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.712×** | -5.2 | 8e-06 | 29/48 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.857× | -4.7 | 1e-04 | 21/48 (A-172, HOP62, …) | top dose only |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.825×** | -3.9 | 0.003 | 20/48 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.710×** | -3.8 | 0.003 | 17/47 (H4, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Acetohexamide (drug)]] 5 µM |  | 0.909× | -2.9 | 0.080 | 6/48 (CFPAC-1, RKO, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3509. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 44.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -8.5) |
| [[CHP-212 (line)]] | wt | 66.6 | 0 | 4 (4 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0618× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 63.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 34.4 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.328× (z -13.0) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -10.3) |
| [[A-172 (line)]] | wt | 50.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -14.4) |
| [[CFPAC-1 (line)]] | alt | 32.3 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.341× (z -10.1) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -9.0) |
| [[Hs 766T (line)]] | wt | 35.9 | 0 | 3 (1 ⚠) | — | [[venetoclax (drug)]] 5 µM 0.0623× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 42.8 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -12.2) |
| [[SNU-423 (line)]] | alt | 72.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -14.6) |
| [[SW1417 (line)]] | alt | 64.6 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.352× (z -13.2) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -10.9) |
| [[SW480 (line)]] | alt | 46.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -9.6) |
| [[HS-578T (line)]] | alt | 46.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -12.6) |
| [[J82 (line)]] | alt | 38.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -10.8) |
| [[KATO III (line)]] | alt | 37.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.385× (z -8.6) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 43.2 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.272× (z -12.9) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -12.8) |
| [[LS 180 (line)]] | wt | 48.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.48× (z +11.4) | — |
| [[NCI-H1792 (line)]] | alt | 61.4 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.258× (z -13.0) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 63.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -12.8) |
| [[PANC-1 (line)]] | alt | 26.2 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.402× (z -10.2) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 40.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -15.3) |
| [[SK-MEL-2 (line)]] | alt | 63.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -13.3) |
| [[A498 (line)]] | wt | 21.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.329× (z -9.3) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 25.7 | 0 | 1 | — | [[Bestatin (drug)]] 0.05 µM 0.0787× (z -9.2) |
| [[C-33 A (line)]] | alt | 37.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[HCT15 (line)]] | alt | 54.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[HEC-1-A (line)]] | alt | 64.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.397× (z -9.4) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 24.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.319× (z -8.7) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 33.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.277× (z -12.0) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.326× (z -10.5) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 46.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 58.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -10.2) |
| [[SNU-1 (line)]] | wt | 50.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -8.7) |
| [[SW48 (line)]] | wt | 39.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[A-427 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3509), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM23]] | +0.75 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[WDR48]] | +0.74 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[ASB8]] | +0.72 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[ZNHIT3]] | +0.70 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[CCDC28A]] | +0.68 | +0.45 / +0.75 | both halves | 3e-05 |  |
| [[PLEKHM3]] | +0.67 | +0.42 / +0.75 | both halves | 4e-05 |  |
| [[ACOT8]] | +0.67 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[CIR1]] | +0.65 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[MRPL43]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[LINC00888-1]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[EZH1]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[HACL1]] | +0.63 | +0.41 / +0.66 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCFC1]] | -0.59 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[SUV39H2]] | -0.58 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[CYCS]] | -0.57 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[GATAD2A]] | -0.57 | -0.62 / -0.55 | both halves | 1e-05 | pathway: Potential therapeutics for SARS |
| [[HNRNPAB]] | -0.56 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[ELOVL6]] | -0.56 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[HCG18]] | -0.56 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[FSCN2]] | -0.55 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[PRDM15]] | -0.55 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[ARSB]] | -0.55 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[ASMTL-AS1]] | -0.54 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[MYO19]] | -0.54 | -0.51 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CRBN's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FSCN2]] | C | FSCN2 activity lowers CRBN's level | lines that do not express FSCN2 (4) vs lines expressing it (46) | 1.63× higher at baseline in the lines without FSCN2 | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000267174, ADCY7, ENSG00000229848; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WDR48]] | C | CRBN's natural level strengthens WDR48's drug response | CRBN's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.35; direction not clear | 0.024 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.659). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.9, -45.8); signed map (-16.7, 7.8). **Vector** length 123, 33.7% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +8.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.3 | +3.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +7.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +3.8 | +4.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.7 | +6.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.7 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +2.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.1 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -13.2 | -20.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.2 | -16.8 |
|  | [[EX229 (drug)]] 5 µM |  | -7.5 | -9.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.4 | -9.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.0 | -8.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.7 | -10.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.5 | -7.7 |

## What is on record

|  |  |
|---|---|
| Name | cereblon |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p26.2 — chr3:3,144,628-3,179,727 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRT2; previously MRT2A |
| Reactome | 3 pathways, smallest: Potential therapeutics for SARS; SARS-CoV Infections; Viral Infection Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96SW2](https://www.uniprot.org/uniprotkb/Q96SW2) (Protein cereblon):

> Substrate recognition component of a DCX (DDB1-CUL4-X-box) E3 protein ligase complex that mediates the ubiquitination and subsequent proteasomal degradation of target proteins, such as MEIS2, ILF2, GLUL, IKZF1 and CSNK1A1. Normal degradation of key regulatory proteins is required for normal limb outgrowth and expression of the fibroblast growth factor FGF8. Maintains presynaptic glutamate release and consequently cognitive functions, such as memory and learning, by negatively regulating …

**Summary**, from NCBI Gene [51185](https://www.ncbi.nlm.nih.gov/gene/51185):

> This gene encodes a protein related to the Lon protease protein family. In rodents and other mammals this gene product is found in the cytoplasm localized with a calcium channel membrane protein, and is thought to play a role in brain development. Mutations in this gene are associated with autosomal recessive nonsyndromic cognitive disability. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:30185](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30185) · Entrez [51185](https://www.ncbi.nlm.nih.gov/gene/51185) · UniProt [Q96SW2](https://www.uniprot.org/uniprotkb/Q96SW2) · Ensembl [ENSG00000113851](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113851)

## Data

Gene col 3509: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3509); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3509, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3509]; `tensor/DDL_lfc|DDL_z.npy` [3509]; `embed/gene_vectors.npy` [3509]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3509 or target_col == 3509). Every well: [[CRBN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRBN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
