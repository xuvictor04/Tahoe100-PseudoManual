---
symbol: "BRD2"
type: "gene"
col: 12837
ensembl_id: "ENSG00000204256"
name: "bromodomain containing 2"
location: "6p21.32"
module: 93
arm: "+"
pooled_cpm: 295.74
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# BRD2

*bromodomain containing 2* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.84× (z +32.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.583× (z -9.2, q 1e-17, down in 40 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.745× (z -5.0, q 7e-05, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM53C]] (+0.67, fdr 1e-05), [[RSRC2]] (+0.66, fdr 7e-06), [[HEXIM1]] (+0.65, fdr 7e-06); moves opposite to [[ELAVL1]] (-0.61, fdr 1e-05), [[NUDT21]] (-0.58, fdr 2e-05), [[CPSF6]] (-0.56, fdr 4e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12837.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.84×** | +32.6 | 0e+00 | 48/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.18×** | +19.8 | 0e+00 | 48/48 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.72×** | +16.5 | 0e+00 | 48/48 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +10.4 | 4e-23 | 37/47 (COLO 205, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.77×** | +9.8 | 2e-20 | 45/48 (AsPC-1, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.71×** | +9.2 | 5e-18 | 43/48 (HEC-1-A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.59×** | +7.9 | 3e-13 | 46/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +7.1 | 1e-10 | 42/48 (SNU-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.47×** | +6.6 | 3e-09 | 39/48 (SNU-1, NCI-H460, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +6.1 | 5e-08 | 39/48 (RPMI-7951, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +5.6 | 1e-06 | 40/48 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +5.4 | 2e-06 | 36/45 (HEC-1-A, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.37×** | +5.4 | 2e-06 | 38/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +5.2 | 6e-06 | 33/47 (SHP-77, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.35×** | +5.1 | 2e-05 | 32/48 (SNU-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +4.9 | 4e-05 | 32/48 (HCT15, SNU-1, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.36×** | +4.8 | 4e-05 | 38/47 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +4.1 | 0.001 | 28/48 (HCT15, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.023 | 25/49 (C32, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.062 | 20/48 (LS 180, HCT15, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.40×** | +3.0 | 0.062 | 25/48 (LOX-IMVI, RKO, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12837.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.583×** | -9.2 | 1e-17 | 40/49 (A-427, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.599×** | -8.4 | 9e-15 | 33/44 (SNU-1, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.620×** | -7.6 | 7e-12 | 42/45 (HT-29, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.745×** | -5.0 | 7e-05 | 38/48 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.773×** | -4.4 | 0.001 | 32/48 (CFPAC-1, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.646×** | -3.9 | 0.009 | 35/49 (AsPC-1, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.803×** | -3.7 | 0.016 | 25/48 (LOX-IMVI, CFPAC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.801×** | -3.7 | 0.016 | 30/48 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.808×** | -3.7 | 0.016 | 26/48 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.819×** | -3.4 | 0.035 | 25/48 (HEC-1-A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.820×** | -3.3 | 0.046 | 28/48 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 0.876× | -3.2 | 0.068 | 9/48 (A-172, BT-474, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.838× | -3.0 | 0.11 | 21/48 (NCI-H23, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12837. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 312 | 13 (7 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +25.9) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -15.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 192 | 12 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +25.7) | — |
| [[AsPC-1 (line)]] | alt | 249 | 8 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.23× (z +37.1) | [[Dinaciclib (drug)]] 5 µM 0.454× (z -10.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 448 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +22.2) | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -13.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 287 | 7 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +28.3) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 325 | 5 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -13.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 470 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +26.9) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -12.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 232 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.78× (z +32.8) | [[Panobinostat (drug)]] 5 µM 0.503× (z -9.1) |
| [[HS-578T (line)]] | alt | 276 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +24.5) | — |
| [[SW1417 (line)]] | alt | 377 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +29.4) | [[Dinaciclib (drug)]] 5 µM 0.516× (z -9.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 170 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.27× (z +38.4) | — |
| [[HOP62 (line)]] | alt | 323 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +26.8) | [[Dinaciclib (drug)]] 0.5 µM 0.473× (z -9.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 305 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +24.8) | — |
| [[KATO III (line)]] | alt | 346 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +28.7) | [[Dinaciclib (drug)]] 0.5 µM 0.486× (z -10.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 376 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +23.0) | [[Dinaciclib (drug)]] 5 µM 0.417× (z -10.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 315 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +22.5) | — |
| [[NCI-H1573 (line)]] | alt | 317 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +20.4) | — |
| [[PANC-1 (line)]] | alt | 352 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +28.8) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -11.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 336 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +28.4) | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -11.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 373 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 194 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +25.8) | — |
| [[A-427 (line)]] | wt | 290 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.87× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -17.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 255 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +22.4) | — |
| [[C32 (line)]] | wt | 280 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.22× (z +27.6) | — |
| [[Hs 766T (line)]] | wt | 173 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +22.3) | — |
| [[HT-29 (line)]] | alt | 300 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +23.5) | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -13.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 305 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +25.0) | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -10.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 219 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +24.8) | — |
| [[HepG2_C3A (line)]] | wt | 304 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +17.0) | [[Dinaciclib (drug)]] 0.05 µM 0.448× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 241 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +27.7) | — |
| [[NCI-H23 (line)]] | alt | 473 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +25.7) | [[Dinaciclib (drug)]] 0.5 µM 0.540× (z -9.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 395 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +22.3) | [[Dinaciclib (drug)]] 0.5 µM 0.470× (z -8.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 291 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +16.0) | — |
| [[SK-MEL-2 (line)]] | alt | 197 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +28.2) | [[Dinaciclib (drug)]] 5 µM 0.436× (z -9.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 242 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +18.2) | — |
| [[A549 (line)]] | wt | 189 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +22.7) | — |
| [[AN3 CA (line)]] | alt | 250 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +14.5) | — |
| [[H4 (line)]] | wt | 301 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -8.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 455 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.14× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 417 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +21.7) | — |
| [[SHP-77 (line)]] | alt | 170 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.5) | — |
| [[C-33 A (line)]] | alt | 300 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.32× (z +10.2) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -11.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 296 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.8) | — |
| [[SW 1088 (line)]] | alt | 244 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +12.7) | — |
| [[SW 900 (line)]] | alt | 247 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +19.7) | — |
| [[CHP-212 (line)]] | wt | 236 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.2) | — |
| [[SW 1271 (line)]] | alt | 334 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +12.1) | — |
| [[NCI-H2122 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 283 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 265 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12837), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM53C]] | +0.67 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[RSRC2]] | +0.66 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[HEXIM1]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 | STRING 560 |
| [[RBBP6]] | +0.64 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[IFRD1]] | +0.61 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ZNF335]] | +0.61 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[PBDC1]] | +0.61 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[DYNLL1]] | +0.60 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[IRF7]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[MAD2L1BP]] | +0.59 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[C14orf119]] | +0.59 | +0.36 / +0.61 | both halves | 9e-05 |  |
| [[SERTAD1]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELAVL1]] | -0.61 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[NUDT21]] | -0.58 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[CPSF6]] | -0.56 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[MAPK9]] | -0.55 | -0.29 / -0.59 | both halves | 3e-04 |  |
| [[MAPK1]] | -0.54 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[PABIR2]] | -0.54 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[ENOPH1]] | -0.54 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[NUP93]] | -0.54 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[RPA1]] | -0.54 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[PIGK]] | -0.53 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[MFSD14B]] | -0.53 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[RCN2]] | -0.52 | -0.53 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises BRD2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.653). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (26.1, -29.3); signed map (4.6, 15.1). **Vector** length 123, 47.6% of its response variance represented; |z| ≥ 3 in 1,319 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.6 | +9.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.5 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.5 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.2 | +7.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.8 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | -0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.5 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.0 | +4.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +2.8 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -8.1 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.0 | -7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.7 | -9.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.9 | -3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.6 | -8.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.9 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.4 | -3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.1 | -1.4 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -2.8 | -2.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | bromodomain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:32,968,594-32,981,505 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA9001, RING3, D6S113E, NAT, FSHRG1; previously BRD2-IT1 |
| Gene groups (HGNC) | Bromodomain and extra-terminal domain family; Bromodomain containing |
| Reactome | 2 pathways, smallest: RUNX3 regulates p14-ARF; Transcriptional regulation by RUNX3 |
| Matched by | ensembl_id |

**Function**, from UniProt [P25440](https://www.uniprot.org/uniprotkb/P25440) (Bromodomain-containing protein 2):

> Chromatin reader protein that specifically recognizes and binds histone H4 acetylated at 'Lys-5' and 'Lys-12' (H4K5ac and H4K12ac, respectively), thereby controlling gene expression and remodeling chromatin structures. Recruits transcription factors and coactivators to target gene sites, and activates RNA polymerase II machinery for transcriptional elongation. Plays a key role in genome compartmentalization via its association with CTCF and cohesin: recruited to chromatin by CTCF and promotes …

**Summary**, from NCBI Gene [6046](https://www.ncbi.nlm.nih.gov/gene/6046):

> This gene encodes a transcriptional regulator that belongs to the BET (bromodomains and extra terminal domain) family of proteins. This protein associates with transcription complexes and with acetylated chromatin during mitosis, and it selectively binds to the acetylated lysine-12 residue of histone H4 via its two bromodomains. The gene maps to the major histocompatability complex (MHC) class II region on chromosome 6p21.3, but sequence comparison suggests that the protein is not involved in …

**Accessions** — [HGNC:1103](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1103) · Entrez [6046](https://www.ncbi.nlm.nih.gov/gene/6046) · UniProt [P25440](https://www.uniprot.org/uniprotkb/P25440) · Ensembl [ENSG00000204256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204256)

## Data

Gene col 12837: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12837); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12837, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12837]; `tensor/DDL_lfc|DDL_z.npy` [12837]; `embed/gene_vectors.npy` [12837]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12837 or target_col == 12837). Every well: [[BRD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
