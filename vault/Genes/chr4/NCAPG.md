---
symbol: "NCAPG"
type: "gene"
col: 3084
ensembl_id: "ENSG00000109805"
name: "non-SMC condensin I complex subunit G"
location: "4p15.31"
module: 22
arm: "+"
pooled_cpm: 59.41
n_lines_expressing: 49
n_dd_up: 31
n_dd_down: 22
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# NCAPG

*non-SMC condensin I complex subunit G* — 4p15.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (22 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.23× (z +16.4, q 0e+00, up in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~85% of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.34× (z +4.5, q 3e-04, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.601× (z -10.2, q 9e-22, down in 33 of 47 measured lines) ⚠ cell-cycle shift, explains ~92% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.666× (z -6.1, q 1e-07, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF11]] (+0.97, fdr 7e-06), [[MKI67]] (+0.94, fdr 7e-06), [[CDK1]] (+0.94, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 23 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3084.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **2.23×** | +16.4 | 0e+00 | 36/47 (PANC-1, NCI-H2347, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **2.05×** | +10.5 | 4e-23 | 41/47 (PANC-1, RKO, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.68×** | +7.9 | 6e-13 | 31/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.33×** | +6.0 | 3e-07 | 36/47 (NCI-H23, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.45×** | +5.6 | 2e-06 | 29/46 (PANC-1, KATO III, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.45×** | +5.6 | 2e-06 | 29/47 (PANC-1, KATO III, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.42×** | +5.3 | 7e-06 | 22/46 (PANC-1, H4, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.39×** | +4.8 | 1e-04 | 20/41 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +4.7 | 2e-04 | 26/47 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.47×** | +4.6 | 2e-04 | 20/47 (C32, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +4.6 | 2e-04 | 21/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.36×** | +4.6 | 2e-04 | 25/46 (AsPC-1, SW 900, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.35×** | +4.6 | 2e-04 | 20/46 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.35×** | +4.6 | 2e-04 | 25/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.34×** | +4.5 | 3e-04 | 23/47 (Hs 766T, HOP62, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.31×** | +4.1 | 0.001 | 17/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.010 | 17/47 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.022 | 13/47 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.022 | 14/47 (HEC-1-A, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.040 | 11/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **1.20×** | +2.8 | 0.090 | 13/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.20×** | +2.8 | 0.090 | 13/47 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **1.20×** | +2.8 | 0.093 | 10/47 (LS 180, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3084.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.601×** | -10.2 | 9e-22 | 33/47 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.485×** | -8.6 | 1e-15 | 39/47 (LS 180, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.504×** | -7.2 | 9e-11 | 33/47 (HCT15, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.639×** | -6.7 | 2e-09 | 37/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.666×** | -6.1 | 1e-07 | 33/47 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **0.480×** | -5.8 | 8e-07 | 27/43 (A-427, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.690×** | -5.6 | 2e-06 | 26/47 (NCI-H2030, SW1417, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.691×** | -5.5 | 2e-06 | 27/47 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.766×** | -5.4 | 3e-06 | 30/47 (HCT15, RKO, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.614×** | -5.2 | 1e-05 | 30/47 (SW480, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[palbociclib (drug)]] 5 µM |  | **0.592×** | -4.1 | 0.002 | 21/46 (Hs 766T, LS 180, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.592×** | -4.1 | 0.002 | 21/47 (HEC-1-A, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **0.824×** | -3.9 | 0.003 | 23/47 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.726×** | -3.8 | 0.006 | 23/47 (A498, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **0.826×** | -3.8 | 0.006 | 22/47 (CHP-212, LOX-IMVI, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.731×** | -3.4 | 0.026 | 18/47 (SW 1271, SHP-77, …) | all doses, flat | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.800×** | -3.3 | 0.026 | 19/47 (RKO, LoVo, …) | top dose only |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.851× | -3.3 | 0.033 | 17/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.812×** | -3.1 | 0.053 | 16/47 (NCI-H2347, BT-474, …) | all doses, flat | position effect removed |
| [[Rapamycin (drug)]] 0.05 µM |  | **0.820×** | -3.0 | 0.081 | 13/47 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.691×** | -2.9 | 0.092 | 17/45 (LS 180, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.87 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3084. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 91.2 | 0 | 7 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.154× (z -13.7) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.221× (z -11.5) |
| [[PANC-1 (line)]] | alt | 51.5 | 7 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +22.6) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[A-172 (line)]] | wt | 71.6 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.229× (z -14.8) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.392× (z -9.7) |
| [[A498 (line)]] | wt | 52.7 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0477× (z -33.6) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.445× (z -9.4) |
| [[C32 (line)]] | wt | 55.1 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +16.0) ⚠ cell-cycle shift, explains ~85% of this change | [[Selinexor (drug)]] 5 µM 0.312× (z -10.6) ⚠ cell-cycle shift, explains ~92% of this change |
| [[LS 180 (line)]] | wt | 41.6 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.171× (z -14.8) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.294× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 109 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.367× (z -10.5) |
| [[LoVo (line)]] | wt | 40.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.3) ⚠ cell-cycle shift, explains ~85% of this change | [[Selinexor (drug)]] 5 µM 0.416× (z -9.3) ⚠ cell-cycle shift, explains ~92% of this change |
| [[LOX-IMVI (line)]] | wt | 40.3 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +11.7) ⚠ cell-cycle shift, explains ~85% of this change | [[Selinexor (drug)]] 5 µM 0.296× (z -11.2) ⚠ cell-cycle shift, explains ~92% of this change |
| [[NCI-H2347 (line)]] | alt | 68.9 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +21.2) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[RKO (line)]] | wt | 59.3 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.22× (z +20.2) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[A549 (line)]] | wt | 43.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +15.5) ⚠ cell-cycle shift, explains ~85% of this change | [[Selinexor (drug)]] 5 µM 0.350× (z -10.7) ⚠ cell-cycle shift, explains ~92% of this change |
| [[CFPAC-1 (line)]] | alt | 47.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +11.9) ⚠ cell-cycle shift, explains ~85% of this change | [[Selinexor (drug)]] 5 µM 0.423× (z -8.5) ⚠ cell-cycle shift, explains ~92% of this change |
| [[HS-578T (line)]] | alt | 38.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +13.6) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[KATO III (line)]] | alt | 39.8 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.44× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 52.6 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.346× (z -11.5) ⚠ cell-cycle shift, explains ~92% of this change |
| [[Panc 03.27 (line)]] | alt | 43.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +18.8) ⚠ cell-cycle shift, explains ~85% of this change | [[Selinexor (drug)]] 5 µM 0.370× (z -9.8) ⚠ cell-cycle shift, explains ~92% of this change |
| [[SW48 (line)]] | wt | 59.8 | 0 | 2 (1 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.303× (z -9.7) |
| [[A-427 (line)]] | wt | 122 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.239× (z -16.9) ⚠ cell-cycle shift, explains ~92% of this change |
| [[AN3 CA (line)]] | alt | 163 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.229× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[BT-474 (line)]] | alt | 43.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.251× (z -9.2) |
| [[HCT15 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.302× (z -10.1) ⚠ cell-cycle shift, explains ~92% of this change |
| [[HOP62 (line)]] | alt | 70.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +13.1) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[Hs 766T (line)]] | wt | 46.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.383× (z -8.6) ⚠ cell-cycle shift, explains ~92% of this change |
| [[HT-29 (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.326× (z -10.2) ⚠ cell-cycle shift, explains ~92% of this change |
| [[hTERT-HPNE (line)]] | wt | 27.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +9.4) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[J82 (line)]] | alt | 113 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +17.4) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[NCI-H1792 (line)]] | alt | 24.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +10.5) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[NCI-H2030 (line)]] | alt | 55.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +20.9) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[SNU-1 (line)]] | wt | 69.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -11.3) ⚠ cell-cycle shift, explains ~85% of this change |
| [[SNU-423 (line)]] | alt | 52.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.9) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[SW 900 (line)]] | alt | 73.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +10.2) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[SW1417 (line)]] | alt | 44.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +12.9) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[C-33 A (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 84.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3084), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF11]] | +0.97 | +0.96 / +0.97 | both halves | 7e-06 | STRING 975 |
| [[MKI67]] | +0.94 | +0.94 / +0.93 | both halves | 7e-06 | STRING 908 |
| [[CDK1]] | +0.94 | +0.95 / +0.92 | both halves | 7e-06 | pathway: Condensation of Prometaphase Chromosomes; STRING 981 |
| [[KIF15]] | +0.93 | +0.93 / +0.92 | both halves | 7e-06 | STRING 919 |
| [[TPX2]] | +0.93 | +0.93 / +0.92 | both halves | 7e-06 | STRING 949 |
| [[KNL1]] | +0.93 | +0.92 / +0.93 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 652 |
| [[NCAPH]] | +0.93 | +0.94 / +0.93 | both halves | 7e-06 | same gene group; pathway: Condensation of Prometaphase Chromosomes; STRING 999 |
| [[KIF23]] | +0.92 | +0.93 / +0.91 | both halves | 7e-06 | STRING 949 |
| [[RACGAP1]] | +0.92 | +0.89 / +0.93 | both halves | 7e-06 | STRING 864 |
| [[KIF4A]] | +0.92 | +0.94 / +0.90 | both halves | 7e-06 | STRING 934 |
| [[NUSAP1]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | STRING 931 |
| [[BIRC5]] | +0.92 | +0.94 / +0.87 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 876 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 4, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises NCAPG's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.49× lower at baseline in the lines without PIMREG | 0.004 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises NCAPG's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.17× lower at baseline in the lines without E2F8 | 0.035 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[MYBL1]] | B | MYBL1 activity raises NCAPG's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.83× lower at baseline in the lines without MYBL1 | 0.085 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[HYLS1]] | B | HYLS1 activity raises NCAPG's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 1.88× lower at baseline in the lines without HYLS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises NCAPG's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.75× lower at baseline in the lines without AURKB | 0.022 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises NCAPG's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.79× lower at baseline in the lines without PBK | 0.023 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises NCAPG's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.92× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent genes |
| [[C21orf58]], [[SKA3]] | C | C21orf58, SKA3 activity raises NCAPG's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 2.87× lower at baseline in the lines without C21orf58, SKA3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CDC20]] | C | CDC20 activity raises NCAPG's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.72× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[NDC80]] | C | NDC80 activity raises NCAPG's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.27× lower at baseline in the lines without NDC80 | 0.090 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[MYLK2]] | C | MYLK2 activity raises NCAPG's level | lines that do not express MYLK2 (3) vs lines expressing it (47) | 2.89× lower at baseline in the lines without MYLK2 | 0.093 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, NDC80, SMARCD3; maybe low, not absent |
| [[TP53]] | C | TP53 activity strengthens NCAPG's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 16 not recorded | the TP53-altered lines respond 0.88× as strongly (z diff +0.36); strongest at Selinexor 5 µM: 0.66x vs 0.31x (z diff +4.2) | 0.907 over the table, 0.084 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.939). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.7, -54.3); signed map (-48.1, -44.0). **Vector** length 163, 60.6% of its response variance represented; |z| ≥ 3 in 1,362 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.75 to 60); *DREAM G2/M down* (control, mean cos +0.81 to 28); *E2F targets* (hallmark, mean cos +0.73 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +6.8 | +16.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +5.3 | +10.5 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | +5.0 | +6.0 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~91% of this change | +4.4 | +4.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.1 | +4.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.6 | +4.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +3.3 | +4.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +3.2 | +3.6 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | +3.0 | +2.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +3.0 | +2.8 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | -9.2 | -7.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | -9.1 | -10.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | -9.1 | -8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.0 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -6.4 | -5.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -5.0 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.7 | -3.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | non-SMC condensin I complex subunit G |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.31 — chr4:17,810,979-17,844,865 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12450, hCAP-G, CAP-G, YCG1 |
| Gene groups (HGNC) | Condensin I subunits; Armadillo like helical domain containing |
| Reactome | 5 pathways, smallest: Condensation of Prometaphase Chromosomes; Mitotic Prometaphase; M Phase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BPX3](https://www.uniprot.org/uniprotkb/Q9BPX3) (Condensin complex subunit 3):

> Regulatory subunit of the condensin complex, a complex required for conversion of interphase chromatin into mitotic-like condense chromosomes. The condensin complex probably introduces positive supercoils into relaxed DNA in the presence of type I topoisomerases and converts nicked DNA into positive knotted forms in the presence of type II topoisomerases.

**Summary**, from NCBI Gene [64151](https://www.ncbi.nlm.nih.gov/gene/64151):

> This gene encodes a subunit of the condensin complex, which is responsible for the condensation and stabilization of chromosomes during mitosis and meiosis. Phosphorylation of the encoded protein activates the condensin complex. There are pseudogenes for this gene on chromosomes 8 and 15. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:24304](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24304) · Entrez [64151](https://www.ncbi.nlm.nih.gov/gene/64151) · UniProt [Q9BPX3](https://www.uniprot.org/uniprotkb/Q9BPX3) · Ensembl [ENSG00000109805](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109805)

## Data

Gene col 3084: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3084); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3084, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3084]; `tensor/DDL_lfc|DDL_z.npy` [3084]; `embed/gene_vectors.npy` [3084]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3084 or target_col == 3084). Every well: [[NCAPG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCAPG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
