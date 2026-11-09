---
symbol: "HDAC9"
type: "gene"
col: 529
ensembl_id: "ENSG00000048052"
name: "histone deacetylase 9"
location: "7p21.1"
module: 125
arm: "+"
pooled_cpm: 282.67
n_lines_expressing: 41
n_dd_up: 30
n_dd_down: 38
n_dd_up_clean: 24
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 7
direction_downstream: 6
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# HDAC9

*histone deacetylase 9* — 7p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 13.5× (z +69.2, q 0e+00, up in 38 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.378× (z -18.3, q 0e+00, down in 33 of 39 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.584× (z -10.1, q 6e-22, down in 29 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLA2G4C]] (+0.77, fdr 7e-06), [[C12orf50]] (+0.73, fdr 7e-06), [[TRAF1]] (+0.72, fdr 7e-06); moves opposite to [[ABHD12]] (-0.66, fdr 1e-05), [[CPD]] (-0.64, fdr 1e-05), [[RPA1]] (-0.63, fdr 1e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PPP1R1C]] → it (grade B ⚠); 6 go from it, the strongest it → [[DUSP16]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 529.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **13.5×** | +69.2 | 0e+00 | 38/39 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.86×** | +36.2 | 0e+00 | 38/39 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **5.56×** | +31.0 | 0e+00 | 35/39 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.21×** | +14.9 | 0e+00 | 32/39 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.90×** | +12.1 | 1e-31 | 34/39 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.57×** | +9.3 | 2e-18 | 27/40 (NCI-H460, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.44×** | +6.9 | 4e-10 | 26/39 (AsPC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.44×** | +6.6 | 3e-09 | 26/38 (KATO III, SW 900, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.42×** | +6.5 | 4e-09 | 27/40 (SW1417, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +6.5 | 5e-09 | 24/39 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.37×** | +5.9 | 2e-07 | 26/39 (KATO III, SW 900, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.36×** | +5.7 | 5e-07 | 22/40 (LoVo, NCI-H460, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +5.7 | 6e-07 | 19/39 (AsPC-1, PANC-1, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.33×** | +5.0 | 3e-05 | 23/38 (NCI-H460, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.29×** | +4.8 | 5e-05 | 20/38 (KATO III, SW 900, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.61×** | +4.7 | 1e-04 | 24/38 (SW480, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +4.6 | 1e-04 | 18/39 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 3e-04 | 18/38 (KATO III, SW 900, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 529.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.378×** | -18.3 | 0e+00 | 33/39 (LOX-IMVI, RKO, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.400×** | -17.2 | 0e+00 | 35/39 (RKO, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.403×** | -17.1 | 0e+00 | 37/39 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.651×** | -11.4 | 6e-28 | 30/40 (SNU-1, RKO, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.552×** | -10.7 | 8e-25 | 26/36 (SNU-1, A-172, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.584×** | -10.1 | 6e-22 | 29/39 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.613×** | -9.2 | 3e-18 | 29/40 (SNU-1, RKO, …) | rises with dose | composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.470×** | -7.4 | 1e-11 | 31/38 (LOX-IMVI, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.717×** | -6.2 | 3e-08 | 24/39 (SNU-423, NCI-H1573, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.710×** | -6.2 | 4e-08 | 24/40 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.721×** | -6.1 | 4e-08 | 24/39 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.717×** | -6.0 | 9e-08 | 22/39 (A-427, RKO, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.735×** | -5.8 | 3e-07 | 21/39 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.738×** | -5.7 | 5e-07 | 23/39 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.749×** | -5.4 | 2e-06 | 23/39 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.751×** | -5.4 | 3e-06 | 21/39 (NCI-H1792, Panc 03.27, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.818×** | -5.3 | 3e-06 | 21/39 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.756×** | -5.3 | 5e-06 | 20/39 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.764×** | -5.0 | 1e-05 | 22/39 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.770×** | -4.9 | 3e-05 | 21/39 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -4.9 | 3e-05 | 20/39 (Panc 03.27, NCI-H1573, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.776×** | -4.8 | 5e-05 | 20/39 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.777×** | -4.7 | 5e-05 | 21/39 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.51 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 529. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 382 | 5 | 15 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +40.5) | [[Panobinostat (drug)]] 0.5 µM 0.291× (z -13.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.414× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 205 | 4 | 12 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 19.6× (z +39.7) | [[Panobinostat (drug)]] 0.5 µM 0.278× (z -12.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.336× (z -10.3) |
| [[A-427 (line)]] | wt | 480 | 6 | 9 (9 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +28.2) | [[Dinaciclib (drug)]] 0.05 µM 0.284× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 249 | 8 (1 ⚠) | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +33.6) | [[Panobinostat (drug)]] 5 µM 0.158× (z -16.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.261× (z -11.7) |
| [[SNU-423 (line)]] | alt | 933 | 2 | 13 (9 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.41× (z +36.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -20.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.417× (z -10.7) |
| [[A-172 (line)]] | wt | 693 | 8 (1 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +44.4) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -23.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[RKO (line)]] | wt | 1,284 | 3 | 11 (10 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +23.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -24.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.397× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 694 | 3 | 10 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +39.0) | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -20.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.493× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 614 | 5 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +48.3) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.369× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 646 | 5 (1 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +35.5) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[H4 (line)]] | wt | 681 | 5 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +35.0) | [[Belinostat (drug)]] 5 µM 0.243× (z -12.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.354× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 89.1 | 8 | 2 | [[Homoharringtonine (drug)]] 5 µM 30.0× (z +41.3) | [[Clobetasol propionate (drug)]] 5 µM 0.354× (z -8.9) |
| [[PANC-1 (line)]] | alt | 215 | 5 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 23.8× (z +43.2) | [[Digitoxin (drug)]] 5 µM 0.302× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.391× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 463 | 5 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +41.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -13.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-1 (line)]] | wt | 1,443 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0822× (z -32.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.151× (z -25.2) |
| [[Panc 03.27 (line)]] | alt | 339 | 3 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +23.8) | [[Panobinostat (drug)]] 5 µM 0.219× (z -14.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.363× (z -9.9) |
| [[SW480 (line)]] | alt | 77.0 | 4 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +36.5) | [[Belinostat (drug)]] 5 µM 0.191× (z -15.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.311× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 261 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.55× (z +24.9) | [[Belinostat (drug)]] 5 µM 0.257× (z -10.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 257 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +33.3) | — |
| [[HEC-1-A (line)]] | alt | 103 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.81× (z +26.6) | [[Panobinostat (drug)]] 5 µM 0.301× (z -11.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HS-578T (line)]] | alt | 293 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.0× (z +39.2) | — |
| [[hTERT-HPNE (line)]] | wt | 372 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 37.2× (z +42.8) | [[Belinostat (drug)]] 5 µM 0.291× (z -10.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 141 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +36.6) | [[Belinostat (drug)]] 0.5 µM 0.330× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 119 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 18.8× (z +34.9) | [[Dinaciclib (drug)]] 5 µM 0.137× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[NCI-H2347 (line)]] | alt | 221 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +27.8) | [[Panobinostat (drug)]] 0.5 µM 0.432× (z -8.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[C32 (line)]] | wt | 180 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 44.3× (z +40.8) | — |
| [[CFPAC-1 (line)]] | alt | 358 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.66× (z +33.9) | [[Belinostat (drug)]] 5 µM 0.423× (z -9.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Hs 766T (line)]] | wt | 317 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +40.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -12.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LoVo (line)]] | wt | 88.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +36.6) | — |
| [[SHP-77 (line)]] | alt | 236 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.374× (z -9.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 172 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +22.2) | [[Belinostat (drug)]] 5 µM 0.331× (z -9.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HOP62 (line)]] | alt | 117 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 50.6× (z +40.1) | — |
| [[SW 900 (line)]] | alt | 159 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +33.7) | — |
| [[SW 1271 (line)]] | alt | 297 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.5× (z +20.8) | — |
| [[C-33 A (line)]] | alt | 115 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +11.7) | — |
| [[NCI-H2030 (line)]] | alt | 390 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +26.2) | — |
| [[NCI-H661 (line)]] | alt | 1,203 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -12.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 1088 (line)]] | alt | 402 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +17.9) | — |
| [[CHP-212 (line)]] | wt | 73.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.05× (z +10.3) | — |
| [[A549 (line)]] | wt | 18.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 38.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 40.1 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 33.6 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 22.0 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 31.9 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 63.1 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 17.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 529), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLA2G4C]] | +0.77 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[C12orf50]] | +0.73 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[TRAF1]] | +0.72 | +0.67 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[LINC00944]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[LINC01828]] | +0.71 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[CRYM]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[PPP1R1C]] | +0.67 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[RIPK2-DT]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[MSANTD3]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[RNF103-CHMP3]] | +0.66 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[KIAA1217]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[GPR158]] | +0.65 | +0.63 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD12]] | -0.66 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[CPD]] | -0.64 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[RPA1]] | -0.63 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[METTL9]] | -0.62 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[TM9SF2]] | -0.62 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[SETD3]] | -0.61 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[WDR5]] | -0.61 | -0.62 / -0.50 | both halves | 1e-05 | pathway: Differentiation of T cells |
| [[SDHAP4]] | -0.61 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[SMARCD2]] | -0.61 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[NUDT21]] | -0.60 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[SEPTIN7P14]] | -0.60 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[VPS26B]] | -0.60 | -0.52 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R1C]] | B | PPP1R1C activity lowers HDAC9's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 1.44× higher at baseline in the lines without PPP1R1C | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[LINC01776]] | B | LINC01776 activity raises HDAC9's level | lines that do not express LINC01776 (29) vs lines expressing it (21) | 3.37× lower at baseline in the lines without LINC01776 | 0.051 | ⚠ within organs, on part of the lines; also absent: LINC01010, PHACTR1, NOG |
| [[DLX2]] | B | DLX2 activity raises HDAC9's level | lines that do not express DLX2 (8) vs lines expressing it (42) | 2.57× lower at baseline in the lines without DLX2 | 0.078 | ⚠ within organs, on part of the lines; also absent: LINC01145-1, SCHIP1, NPHS1; maybe low, not absent |
| [[ADTRP]] | B | ADTRP activity raises HDAC9's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 3.11× lower at baseline in the lines without ADTRP | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[NR3C1]] | B | NR3C1 activity lowers HDAC9's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[SFTA1P]] | B | SFTA1P activity raises HDAC9's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 1.90× lower at baseline in the lines without SFTA1P | 0.084 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1 |
| [[OXTR]] | B | OXTR activity lowers HDAC9's level | lines that do not express OXTR (5) vs lines expressing it (45) | 1.86× higher at baseline in the lines without OXTR | 0.090 | ⚠ within organs, on part of the lines; also absent: IPCEF1, SSUH2, OPN3; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUSP16]] | B | HDAC9 activity lowers DUSP16's level | lines that do not express HDAC9 (9) vs lines expressing it (41) | 2.36× higher at baseline in the lines without HDAC9 | 0.068 | ⚠ within organs, on part of the lines; also absent: CCDC88A, ETS1, AFAP1L1 |
| [[ABCA13]] | B | HDAC9 activity raises ABCA13's level | lines that do not express HDAC9 (9) vs lines expressing it (41) | 2.05× lower at baseline in the lines without HDAC9 | 0.090 | ⚠ within organs, on part of the lines; also absent: CCDC88A, ETS1, AFAP1L1 |
| [[CDKN2B]] | B | HDAC9 activity raises CDKN2B's level | lines that do not express HDAC9 (9) vs lines expressing it (41) | 1.30× lower at baseline in the lines without HDAC9 | 0.094 | ⚠ within organs, on part of the lines; also absent: CCDC88A, ETS1, AFAP1L1 |
| [[GPR158]] | B | HDAC9 activity raises GPR158's level | lines that do not express HDAC9 (9) vs lines expressing it (41) | 1.81× lower at baseline in the lines without HDAC9 | 0.097 | ⚠ within organs, on part of the lines; also absent: CCDC88A, ETS1, AFAP1L1 |
| [[COPS8]] | B | HDAC9 activity raises COPS8's level | lines that do not express HDAC9 (9) vs lines expressing it (41) | 1.41× lower at baseline in the lines without HDAC9 | 0.099 | ⚠ within organs, on part of the lines; also absent: CCDC88A, ETS1, AFAP1L1 |
| [[ETS1]] | C | HDAC9 activity raises ETS1's level | lines that do not express HDAC9 (9) vs lines expressing it (41) | 5.09× lower at baseline in the lines without HDAC9 | 0.069 | ⚠ within organs, on part of the lines; also absent: CCDC88A, ETS1, AFAP1L1; co-absent with the target |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.760). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.3, 5.4); signed map (38.4, 21.4). **Vector** length 142, 46.1% of its response variance represented; |z| ≥ 3 in 1,908 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +13.9 | +36.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +12.5 | +69.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +11.4 | +31.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +11.3 | +14.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +9.1 | +12.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.2 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.3 | +5.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.2 | +6.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -6.2 | -4.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -6.1 | -6.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -5.1 | -4.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -5.1 | -5.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -5.1 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | histone deacetylase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.1 — chr7:18,086,949-19,002,416 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0744, HDAC, MITR, HD7, HDAC7B |
| Gene groups (HGNC) | Histone deacetylases, class IIA |
| Hallmark sets | ALLOGRAFT_REJECTION, KRAS_SIGNALING_UP |
| Reactome | 14 pathways, smallest: Notch-HLH transcription pathway; NOTCH signaling regulates gene expression in endothelial stalk cells; NOTCH1 Intracellular Domain Regulates Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKV0](https://www.uniprot.org/uniprotkb/Q9UKV0) (Histone deacetylase 9):

> Responsible for the deacetylation of lysine residues on the N-terminal part of the core histones (H2A, H2B, H3 and H4). Histone deacetylation gives a tag for epigenetic repression and plays an important role in transcriptional regulation, cell cycle progression and developmental events. Represses MEF2-dependent transcription.; Isoform 3 lacks active site residues and therefore is catalytically inactive. Represses MEF2-dependent transcription by recruiting HDAC1 and/or HDAC3. Seems to inhibit …

**Summary**, from NCBI Gene [9734](https://www.ncbi.nlm.nih.gov/gene/9734):

> Histones play a critical role in transcriptional regulation, cell cycle progression, and developmental events. Histone acetylation/deacetylation alters chromosome structure and affects transcription factor access to DNA. The protein encoded by this gene has sequence homology to members of the histone deacetylase family. This gene is orthologous to the Xenopus and mouse MITR genes. The MITR protein lacks the histone deacetylase catalytic domain. It represses MEF2 activity through recruitment of …

**Accessions** — [HGNC:14065](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14065) · Entrez [9734](https://www.ncbi.nlm.nih.gov/gene/9734) · UniProt [Q9UKV0](https://www.uniprot.org/uniprotkb/Q9UKV0) · Ensembl [ENSG00000048052](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000048052)

## Data

Gene col 529: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 529); `tables/drug_effects.parquet` (92 rows, flagged included); `relations/gene_relations.parquet` (col_a == 529, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 529]; `tensor/DDL_lfc|DDL_z.npy` [529]; `embed/gene_vectors.npy` [529]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 529 or target_col == 529). Every well: [[HDAC9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDAC9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
