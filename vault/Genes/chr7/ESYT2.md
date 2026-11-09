---
symbol: "ESYT2"
type: "gene"
col: 3953
ensembl_id: "ENSG00000117868"
name: "extended synaptotagmin 2"
location: "7q36.3"
module: 106
arm: "+"
pooled_cpm: 435.5
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 41
n_dd_up_clean: 16
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# ESYT2

*extended synaptotagmin 2* — 7q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.34× (z +4.7, q 0.002, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (20 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.554× (z -13.2, q 3e-37, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DENND3]] (+0.64, fdr 7e-06), [[DYNC2I1]] (+0.62, fdr 1e-05, ⚠ same locus), [[SSBP2]] (+0.61, fdr 1e-05), [[P4HA1]] (+0.61, fdr 1e-05); moves opposite to [[ZNF346]] (-0.55, fdr 2e-05), [[RBM12B]] (-0.53, fdr 1e-04), [[FBXO30]] (-0.53, fdr 3e-04).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TBC1D8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3953.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +4.7 | 0.002 | 29/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.67×** | +4.3 | 0.005 | 38/48 (HT-29, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.014 | 27/48 (NCI-H1573, H4, …) | all doses, flat |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.027 | 29/49 (AsPC-1, HT-29, …) | top dose only | plate-row cell shift |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.37×** | +3.6 | 0.032 | 35/48 (LoVo, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.033 | 28/49 (H4, NCI-H1573, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.033 | 24/48 (NCI-H1573, H4, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.033 | 26/47 (H4, SW48, …) | rises with dose | low cells (technical?) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.033 | 26/48 (NCI-H1573, H4, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.25×** | +3.4 | 0.033 | 24/47 (H4, HOP62, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.033 | 31/48 (AsPC-1, HEC-1-A, …) | rises with dose | plate-row cell shift |
| [[Budesonide (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.033 | 25/48 (H4, Hs 766T, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.035 | 24/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.040 | 26/48 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.045 | 27/48 (AsPC-1, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lapatinib ditosylate (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.056 | 29/48 (Hs 766T, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.056 | 26/48 (AsPC-1, NCI-H1573, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 23 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3953.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.554×** | -13.2 | 3e-37 | 43/49 (SW1417, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.450×** | -12.7 | 2e-34 | 44/49 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.451×** | -12.2 | 8e-32 | 43/47 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.457×** | -11.9 | 1e-30 | 39/44 (LoVo, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.479×** | -10.8 | 4e-25 | 39/45 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.603×** | -8.0 | 1e-13 | 35/48 (NCI-H1792, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.635×** | -7.2 | 5e-11 | 37/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.639×** | -7.1 | 9e-11 | 42/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.656×** | -6.7 | 2e-09 | 37/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.685×** | -6.0 | 1e-07 | 35/48 (NCI-H2347, RPMI-7951, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.693×** | -5.8 | 3e-07 | 35/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.779×** | -5.6 | 1e-06 | 32/48 (SW48, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.715×** | -5.1 | 1e-05 | 30/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.725×** | -5.1 | 1e-05 | 35/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.797×** | -5.1 | 2e-05 | 28/48 (SW1417, CFPAC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.733×** | -4.6 | 1e-04 | 30/48 (HT-29, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.739×** | -4.6 | 1e-04 | 29/48 (HCT15, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.761×** | -4.3 | 4e-04 | 28/48 (A498, hTERT-HPNE, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.758×** | -4.2 | 6e-04 | 37/48 (SW480, NCI-H1792, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.756×** | -4.0 | 0.002 | 34/48 (C32, HOP62, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.623×** | -3.9 | 0.002 | 32/48 (LoVo, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.776×** | -3.6 | 0.006 | 28/48 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.801×** | -3.5 | 0.009 | 28/48 (HS-578T, HCT15, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 5 µM |  | 0.856× | -3.5 | 0.010 | 16/48 (Hs 766T, HT-29, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.784×** | -3.4 | 0.010 | 27/48 (NCI-H1573, LoVo, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3953. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 611 | 0 | 12 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -17.6) |
| [[HS-578T (line)]] | alt | 400 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -17.3) |
| [[HT-29 (line)]] | alt | 551 | 1 | 8 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 804 | 5 (2 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +14.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 775 | 1 | 7 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.394× (z -11.7) |
| [[Hs 766T (line)]] | wt | 821 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 494 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -19.3) |
| [[LoVo (line)]] | wt | 704 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.339× (z -15.7) |
| [[SW1417 (line)]] | alt | 547 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -21.8) |
| [[SW480 (line)]] | alt | 595 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -16.0) |
| [[MIA PaCa-2 (line)]] | alt | 573 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 265 | 4 | 2 (1 ⚠) | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 2.58× (z +9.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.357× (z -10.1) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.510× (z -9.7) |
| [[SW48 (line)]] | wt | 762 | 2 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.428× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 333 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.387× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 381 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 404 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -11.9) |
| [[RPMI-7951 (line)]] | alt | 507 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -12.7) |
| [[A498 (line)]] | wt | 451 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -10.4) |
| [[A549 (line)]] | wt | 371 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -14.5) |
| [[C32 (line)]] | wt | 1,031 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HCT15 (line)]] | alt | 400 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.283× (z -11.6) |
| [[HOP62 (line)]] | alt | 376 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 396 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -13.8) |
| [[LS 180 (line)]] | wt | 612 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -11.6) |
| [[SNU-423 (line)]] | alt | 370 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -10.0) |
| [[SW 900 (line)]] | alt | 396 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -10.1) |
| [[A-172 (line)]] | wt | 297 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HEC-1-A (line)]] | alt | 341 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 279 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.471× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[PANC-1 (line)]] | alt | 254 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.438× (z -10.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.623× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 291 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 134 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[BT-474 (line)]] | alt | 352 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[C-33 A (line)]] | alt | 278 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[CHP-212 (line)]] | wt | 268 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[H4 (line)]] | wt | 308 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[hTERT-HPNE (line)]] | wt | 348 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.284× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 255 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 1088 (line)]] | alt | 655 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW 1271 (line)]] | alt | 428 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -10.3) |
| [[AN3 CA (line)]] | alt | 239 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 205 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 642 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 508 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 115 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 178 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3953), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND3]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[DYNC2I1]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 | STRING 717; ⚠ same locus (26.3 kb: neighbours can correlate without regulation) |
| [[SSBP2]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[P4HA1]] | +0.61 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[TPCN1]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[AP3S1]] | +0.60 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[LINC00598]] | +0.59 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[TSC22D3]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[PER1]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[MT1X]] | +0.58 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[EFNA3]] | +0.57 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[FAM13A]] | +0.57 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[PLAG1]] | +0.57 | +0.62 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF346]] | -0.55 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[RBM12B]] | -0.53 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[FBXO30]] | -0.53 | -0.61 / -0.28 | both halves | 3e-04 |  |
| [[ANKAR]] | -0.51 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[TRMT11]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[TTC6]] | -0.49 | -0.58 / -0.31 | both halves | 2e-04 |  |
| [[DOCK10]] | -0.49 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[ITGB1-DT]] | -0.49 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[PRTFDC1]] | -0.49 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[SETD4]] | -0.49 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[EIF5]] | -0.48 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[RASGRP3]] | -0.48 | -0.47 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBC1D8]] | B | TBC1D8 activity raises ESYT2's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 1.78× lower at baseline in the lines without TBC1D8 | 0.011 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[PAG1]] | B | PAG1 activity raises ESYT2's level | lines that do not express PAG1 (15) vs lines expressing it (35) | 1.47× lower at baseline in the lines without PAG1 | 0.037 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3 |
| [[NR3C1]] | B | NR3C1 activity raises ESYT2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[TLR2]] | B | TLR2 activity strengthens ESYT2's drug response | lines that do not express TLR2 (26) vs lines expressing it (23) | the lines without TLR2 respond 0.70× as strongly (z diff +2.19); strongest at Homoharringtonine 0.5 µM: 0.70x vs 0.44x (z diff +3.3) | 0.049 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA; target measured in part of the lines; artifact flags |
| [[RPS6KA2]] | B | RPS6KA2 activity raises ESYT2's level | lines that do not express RPS6KA2 (6) vs lines expressing it (44) | 1.96× lower at baseline in the lines without RPS6KA2 | 0.066 | ⚠ within organs, on part of the lines; also absent: RAB20, FAM102A, LINC02100 |
| [[MT1F]] | B | MT1F activity raises ESYT2's level | lines that do not express MT1F (17) vs lines expressing it (33) | 1.34× lower at baseline in the lines without MT1F | 0.071 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[TOP2A]] | B | TOP2A activity raises ESYT2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CLMN]] | B | CLMN activity raises ESYT2's level | lines that do not express CLMN (7) vs lines expressing it (43) | 1.86× lower at baseline in the lines without CLMN | 0.076 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[PDLIM1]] | B | PDLIM1 activity strengthens ESYT2's drug response | lines that do not express PDLIM1 (11) vs lines expressing it (38) | the lines without PDLIM1 respond 0.57× as strongly (z diff +2.54); strongest at Idarubicin (hydrochloride) 5 µM: 0.82x vs 0.53x (z diff +4.9) | 0.097 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1; target measured in part of the lines; artifact flags |
| [[PAG1]] | B | PAG1 activity strengthens ESYT2's drug response | lines that do not express PAG1 (15) vs lines expressing it (34) | the lines without PAG1 respond 0.67× as strongly (z diff +2.17); strongest at Idarubicin (hydrochloride) 5 µM: 0.70x vs 0.53x (z diff +3.0) | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3; target measured in part of the lines; artifact flags |
| [[DYNC2I1]] | C | DYNC2I1's natural level strengthens ESYT2's drug response | DYNC2I1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.33; direction not clear | 0.027 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.6, 11.4); signed map (12.7, 32.2). **Vector** length 135, 56.3% of its response variance represented; |z| ≥ 3 in 1,863 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Betamethasone dipropionate (drug)]] 5 µM |  | +6.4 | +3.5 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +6.4 | +4.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +6.3 | +3.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +6.0 | +2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +5.8 | -6.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +5.8 | +3.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.0 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.8 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.8 | -5.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.7 | -4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.4 | -2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.0 | -3.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.5 | -3.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | extended synaptotagmin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.3 — chr7:158,730,995-158,830,253 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1228, CHR2SYT; previously FAM62B |
| Gene groups (HGNC) | Extended synaptotagmins |
| Reactome | 2 pathways, smallest: Glycosphingolipid transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [A0FGR8](https://www.uniprot.org/uniprotkb/A0FGR8) (Extended synaptotagmin-2):

> Tethers the endoplasmic reticulum to the cell membrane and promotes the formation of appositions between the endoplasmic reticulum and the cell membrane. Binds glycerophospholipids in a barrel-like domain and may play a role in cellular lipid transport. Plays a role in FGF signaling via its role in the rapid internalization of FGFR1 that has been activated by FGF1 binding; this occurs most likely via the AP-2 complex. Promotes the localization of SACM1L at endoplasmic reticulum-plasma membrane …

**Summary**, from NCBI Gene [57488](https://www.ncbi.nlm.nih.gov/gene/57488):

> Enables several functions, including identical protein binding activity; phosphatidylinositol binding activity; and phospholipid binding activity. Predicted to be involved in endocytosis; endoplasmic reticulum-plasma membrane tethering; and lipid transport. Located in cytoplasmic side of plasma membrane; endoplasmic reticulum membrane; and endoplasmic reticulum-plasma membrane contact site. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:22211](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22211) · Entrez [57488](https://www.ncbi.nlm.nih.gov/gene/57488) · UniProt [A0FGR8](https://www.uniprot.org/uniprotkb/A0FGR8) · Ensembl [ENSG00000117868](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117868)

## Data

Gene col 3953: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3953); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3953, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3953]; `tensor/DDL_lfc|DDL_z.npy` [3953]; `embed/gene_vectors.npy` [3953]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3953 or target_col == 3953). Every well: [[ESYT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ESYT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
