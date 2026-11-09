---
symbol: "ACVR2B"
type: "gene"
col: 3579
ensembl_id: "ENSG00000114739"
name: "activin A receptor type 2B"
location: "3p22.2"
module: 69
arm: "+"
pooled_cpm: 30.02
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 35
n_dd_up_clean: 3
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# ACVR2B

*activin A receptor type 2B* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[GSK1059615 (drug)]] 0.5 µM: 1.36× (z +5.2, q 1e-04, up in 14 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.394× (z -22.0, q 0e+00, down in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.597× (z -17.2, q 0e+00, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COQ8A]] (+0.58, fdr 1e-05), [[SYF2]] (+0.57, fdr 4e-04), [[UBXN7]] (+0.57, fdr 3e-05); moves opposite to [[CAPZA1]] (-0.47, fdr 6e-04), [[AP1B1]] (-0.46, fdr 4e-05), [[MAGT1]] (-0.45, fdr 6e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3579.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.36×** | +5.2 | 1e-04 | 14/48 (SW480, PANC-1, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.61×** | +5.0 | 2e-04 | 18/47 (A-427, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 1.19× | +4.2 | 0.006 | 8/48 (SNU-423, NCI-H2347, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.18× | +4.0 | 0.010 | 14/47 (KATO III, C32, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.010 | 11/48 (A-172, CHP-212, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.18× | +3.7 | 0.022 | 8/48 (NCI-H2030, J82, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.11× | +3.6 | 0.023 | 8/48 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +3.6 | 0.023 | 9/47 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 1.17× | +3.5 | 0.033 | 13/47 (A-172, HepG2/C3A, …) | inconsistent across doses |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.14× | +3.1 | 0.10 | 2/48 (KATO III, NCI-H460) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.34× | +3.1 | 0.11 | 1/48 (SW480) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 19 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3579.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.394×** | -22.0 | 0e+00 | 46/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.411×** | -21.0 | 0e+00 | 45/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.457×** | -18.5 | 0e+00 | 46/47 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.477×** | -17.4 | 0e+00 | 37/46 (SW480, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.597×** | -17.2 | 0e+00 | 34/47 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.483×** | -17.2 | 0e+00 | 45/47 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.492×** | -16.1 | 0e+00 | 25/38 (LoVo, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.537×** | -14.7 | 0e+00 | 37/47 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.575×** | -12.5 | 3e-34 | 32/48 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.567×** | -12.4 | 2e-33 | 33/43 (LoVo, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.611×** | -11.2 | 2e-27 | 35/47 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.615×** | -11.0 | 2e-26 | 34/48 (RKO, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.643×** | -10.4 | 1e-23 | 33/47 (LOX-IMVI, HEC-1-A, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.737×** | -10.2 | 1e-22 | 29/48 (NCI-H2030, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.666×** | -9.6 | 4e-20 | 35/47 (NCI-H2030, LOX-IMVI, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.432×** | -8.8 | 6e-17 | 35/47 (SW480, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.595×** | -8.7 | 7e-17 | 35/48 (SW480, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.434×** | -8.7 | 8e-17 | 32/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.437×** | -8.7 | 1e-16 | 30/46 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.440×** | -8.6 | 2e-16 | 31/48 (SW480, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.697×** | -8.5 | 5e-16 | 27/48 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.489×** | -7.5 | 2e-12 | 28/47 (HEC-1-A, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.720×** | -7.3 | 7e-12 | 26/48 (C-33 A, SW48, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.671×** | -6.7 | 4e-10 | 24/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.758×** | -6.2 | 1e-08 | 24/48 (NCI-H23, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.562×** | -6.0 | 3e-08 | 26/46 (SW48, A498, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.63 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3579. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 79.3 | 0 | 12 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -18.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.377× (z -13.4) |
| [[SW480 (line)]] | alt | 44.9 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -25.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.438× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 27.4 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -13.7) |
| [[NCI-H1573 (line)]] | alt | 23.3 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0901× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.316× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 33.2 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -21.9) |
| [[NCI-H2347 (line)]] | alt | 36.2 | 0 | 7 (7 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.305× (z -13.3) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 61.2 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.479× (z -10.1) |
| [[SNU-423 (line)]] | alt | 35.4 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -18.2) |
| [[A549 (line)]] | wt | 32.9 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[HOP62 (line)]] | alt | 29.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -13.1) |
| [[SW1417 (line)]] | alt | 37.5 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[A-172 (line)]] | wt | 23.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0573× (z -23.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.234× (z -11.8) |
| [[C-33 A (line)]] | alt | 48.0 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.259× (z -11.3) ⚠ cell-cycle shift, explains ~43% of this change |
| [[LOX-IMVI (line)]] | wt | 33.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[NCI-H1792 (line)]] | alt | 40.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.410× (z -11.5) |
| [[SHP-77 (line)]] | alt | 43.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0793× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[HepG2_C3A (line)]] | wt | 55.3 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -12.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[J82 (line)]] | alt | 30.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[LoVo (line)]] | wt | 24.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0836× (z -21.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[NCI-H2030 (line)]] | alt | 29.3 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -12.1) ⚠ cell-cycle shift, explains ~49% of this change |
| [[Panc 03.27 (line)]] | alt | 31.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.6) |
| [[SNU-1 (line)]] | wt | 40.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -10.6) |
| [[SW48 (line)]] | wt | 46.7 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.208× (z -11.1) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 23.6 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.258× (z -10.3) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 17.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -13.5) |
| [[HCT15 (line)]] | alt | 68.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[MIA PaCa-2 (line)]] | alt | 17.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -13.9) |
| [[PANC-1 (line)]] | alt | 14.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[RKO (line)]] | wt | 39.1 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.181× (z -13.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -13.3) |
| [[C32 (line)]] | wt | 21.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -9.1) |
| [[CHP-212 (line)]] | wt | 44.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0860× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 19.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -11.9) |
| [[HS-578T (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[HT-29 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.238× (z -9.7) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 16.4 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0816× (z -12.5) |
| [[KATO III (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[LS 180 (line)]] | wt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[RPMI-7951 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[SW 1271 (line)]] | alt | 61.2 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0761× (z -9.8) |
| [[SW 900 (line)]] | alt | 21.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.238× (z -8.8) |
| [[AN3 CA (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3579), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COQ8A]] | +0.58 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[SYF2]] | +0.57 | +0.26 / +0.68 | both halves | 4e-04 |  |
| [[UBXN7]] | +0.57 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[JMY]] | +0.57 | +0.34 / +0.62 | both halves | 1e-04 |  |
| [[KLHL24]] | +0.55 | +0.35 / +0.62 | both halves | 1e-04 |  |
| [[BCL7A]] | +0.55 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[TFAP4]] | +0.54 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[FRAT2]] | +0.54 | +0.30 / +0.61 | both halves | 2e-04 |  |
| [[BRWD1]] | +0.52 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ZBTB44]] | +0.51 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[TSNARE1]] | +0.51 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[UBN2]] | +0.50 | +0.32 / +0.58 | both halves | 2e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPZA1]] | -0.47 | -0.22 / -0.38 | both halves | 6e-04 |  |
| [[AP1B1]] | -0.46 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[MAGT1]] | -0.45 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[ACTR3]] | -0.45 | -0.25 / -0.38 | both halves | 4e-04 |  |
| [[FAM91A1]] | -0.43 | -0.23 / -0.41 | both halves | 5e-04 |  |
| [[CLTC]] | -0.43 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[ACTR2]] | -0.43 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[ARPC4]] | -0.42 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[ACADVL]] | -0.41 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[HSD17B12]] | -0.41 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[EMC1]] | -0.41 | -0.20 / -0.44 | ⚠ not reproduced | 8e-04 |  |
| [[RAB10]] | -0.40 | -0.10 / -0.49 | ⚠ not reproduced | 0.003 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.476). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.8, -45.3); signed map (-14.6, 8.7). **Vector** length 84.3, 19.0% of its response variance represented; |z| ≥ 3 in 1,262 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.8 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +5.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.7 | +0.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.7 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | -0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +3.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.3 | -18.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.0 | -8.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.7 | -8.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.6 | -8.7 |
|  | [[EX229 (drug)]] 5 µM |  | -4.5 | -8.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.4 | -8.6 |

## What is on record

|  |  |
|---|---|
| Name | activin A receptor type 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:38,453,890-38,493,142 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ActR-IIB |
| Gene groups (HGNC) | Type 2 receptor serine/threonine kinases; BMP receptors |
| Reactome | 5 pathways, smallest: Regulation of signaling by NODAL; Signaling by NODAL; Signaling by Activin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13705](https://www.uniprot.org/uniprotkb/Q13705) (Activin receptor type-2B):

> Transmembrane serine/threonine kinase activin type-2 receptor forming an activin receptor complex with activin type-1 serine/threonine kinase receptors (ACVR1, ACVR1B or ACVR1c). Transduces the activin signal from the cell surface to the cytoplasm and is thus regulating many physiological and pathological processes including neuronal differentiation and neuronal survival, hair follicle development and cycling, FSH production by the pituitary gland, wound healing, extracellular matrix …

**Summary**, from NCBI Gene [93](https://www.ncbi.nlm.nih.gov/gene/93):

> Activins are dimeric growth and differentiation factors which belong to the transforming growth factor-beta (TGF-beta) superfamily of structurally related signaling proteins. Activins signal through a heteromeric complex of receptor serine kinases which include at least two type I (I and IB) and two type II (II and IIB) receptors. These receptors are all transmembrane proteins, composed of a ligand-binding extracellular domain with cysteine-rich region, a transmembrane domain, and a cytoplasmic …

**Accessions** — [HGNC:174](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:174) · Entrez [93](https://www.ncbi.nlm.nih.gov/gene/93) · UniProt [Q13705](https://www.uniprot.org/uniprotkb/Q13705) · Ensembl [ENSG00000114739](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114739)

## Data

Gene col 3579: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3579); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3579, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3579]; `tensor/DDL_lfc|DDL_z.npy` [3579]; `embed/gene_vectors.npy` [3579]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3579 or target_col == 3579). Every well: [[ACVR2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACVR2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
