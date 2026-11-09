---
symbol: "MBNL2"
type: "gene"
col: 6346
ensembl_id: "ENSG00000139793"
name: "muscleblind like splicing regulator 2"
location: "13q32.1"
module: 110
arm: "+"
pooled_cpm: 293.17
n_lines_expressing: 46
n_dd_up: 15
n_dd_down: 27
n_dd_up_clean: 14
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# MBNL2

*muscleblind like splicing regulator 2* — 13q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.43× (z +6.8, q 4e-09, up in 32 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.607× (z -12.6, q 1e-33, down in 33 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTEN]] (+0.59, fdr 1e-05), [[CYP39A1]] (+0.58, fdr 1e-05), [[RHOXF1]] (+0.58, fdr 1e-05); moves opposite to [[ZNF710]] (-0.63, fdr 9e-06), [[CORO2B]] (-0.59, fdr 1e-05), [[CLMP]] (-0.58, fdr 1e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC02454]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GNAI1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6346.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +6.8 | 4e-09 | 32/43 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.46×** | +6.8 | 4e-09 | 32/46 (NCI-H23, A-172, …) | all doses, flat | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.32×** | +6.0 | 3e-07 | 30/44 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +5.8 | 8e-07 | 25/44 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +5.7 | 1e-06 | 27/44 (NCI-H23, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +5.7 | 1e-06 | 27/44 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +5.5 | 2e-06 | 28/43 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.32×** | +5.5 | 3e-06 | 28/45 (NCI-H23, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +5.4 | 4e-06 | 29/44 (NCI-H23, PANC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.32×** | +5.3 | 8e-06 | 27/45 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.32×** | +5.0 | 3e-05 | 28/44 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +4.2 | 0.002 | 19/45 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.71×** | +4.0 | 0.003 | 17/46 (NCI-H23, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.24×** | +3.9 | 0.004 | 23/44 (NCI-H23, NCI-H2347, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.17× | +3.9 | 0.004 | 14/44 (SNU-423, PANC-1, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.6 | 0.012 | 16/44 (SNU-1, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6346.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.607×** | -12.6 | 1e-33 | 33/45 (A498, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.534×** | -12.3 | 2e-32 | 38/44 (PANC-1, SHP-77, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.582×** | -10.7 | 3e-24 | 35/45 (COLO 205, KATO III, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.574×** | -10.1 | 7e-22 | 33/41 (Panc 03.27, SW480, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.596×** | -9.8 | 2e-20 | 34/43 (HepG2/C3A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.603×** | -9.6 | 1e-19 | 31/40 (Panc 03.27, KATO III, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.656×** | -8.3 | 8e-15 | 31/44 (NCI-H2347, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.700×** | -7.0 | 2e-10 | 33/44 (MIA PaCa-2, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.722×** | -6.4 | 9e-09 | 31/44 (A498, PANC-1, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.728×** | -6.2 | 3e-08 | 31/44 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.456×** | -5.8 | 3e-07 | 34/44 (A498, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.757×** | -5.5 | 2e-06 | 28/44 (HepG2/C3A, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.757×** | -5.5 | 2e-06 | 27/44 (KATO III, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.775×** | -4.8 | 6e-05 | 26/44 (NCI-H460, NCI-H1792, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.788×** | -4.7 | 1e-04 | 26/44 (SNU-423, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[EX229 (drug)]] 5 µM |  | **0.532×** | -4.7 | 1e-04 | 23/44 (A498, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.573×** | -4.1 | 0.001 | 20/44 (PANC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.712×** | -4.1 | 0.001 | 22/44 (A498, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.801×** | -4.0 | 0.001 | 22/43 (NCI-H460, SNU-1, …) | all doses, flat | low cells (technical?) |
| [[EX229 (drug)]] 0.5 µM |  | **0.713×** | -4.0 | 0.001 | 23/45 (A498, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.597×** | -3.8 | 0.003 | 24/44 (SW1417, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.618×** | -3.6 | 0.008 | 17/44 (SW1417, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.750×** | -3.4 | 0.012 | 19/44 (RKO, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.843× | -3.4 | 0.015 | 19/43 (PANC-1, MIA PaCa-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6346. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 591 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -17.4) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -11.9) |
| [[KATO III (line)]] | alt | 1,019 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 578 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.471× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 139 | 9 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.96× (z +18.8) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 0.5 µM 2.70× (z +9.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.349× (z -8.8) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 321 | 4 | 5 (2 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.20× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.303× (z -17.0) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.471× (z -10.7) |
| [[SHP-77 (line)]] | alt | 487 | 0 | 9 (9 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.253× (z -16.7) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 155 | 0 | 7 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.241× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[5-Azacytidine (drug)]] 5 µM 0.279× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 164 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.372× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.473× (z -10.1) |
| [[A498 (line)]] | wt | 447 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -18.4) |
| [[HT-29 (line)]] | alt | 613 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[SW480 (line)]] | alt | 323 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -9.1) |
| [[A-172 (line)]] | wt | 473 | 1 | 4 (3 ⚠) | [[Trametinib (drug)]] 5 µM 2.14× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -13.9) |
| [[LS 180 (line)]] | wt | 608 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[MIA PaCa-2 (line)]] | alt | 512 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -14.8) |
| [[SNU-1 (line)]] | wt | 276 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.3) ⚠ cell-cycle shift, explains ~93% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -9.1) |
| [[SNU-423 (line)]] | alt | 299 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -11.6) |
| [[BT-474 (line)]] | alt | 305 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -10.7) |
| [[COLO 205 (line)]] | alt | 1,135 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.407× (z -9.0) |
| [[HOP62 (line)]] | alt | 175 | 3 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.53× (z +13.4) ⚠ position not correctable · without an alert: [[Ponatinib (drug)]] 5 µM 2.65× (z +8.8) | — |
| [[J82 (line)]] | alt | 270 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +15.0) ⚠ cell-cycle shift, explains ~93% of this change | — |
| [[LoVo (line)]] | wt | 216 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[NCI-H1792 (line)]] | alt | 171 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.304× (z -13.2) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.453× (z -8.8) |
| [[SW 900 (line)]] | alt | 217 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.460× (z -8.8) |
| [[SW1417 (line)]] | alt | 241 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -14.5) |
| [[C32 (line)]] | wt | 277 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -13.3) |
| [[Hs 766T (line)]] | wt | 619 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[NCI-H2347 (line)]] | alt | 125 | 1 | 1 | [[Cobimetinib (drug)]] 5 µM 2.27× (z +8.7) | [[Harringtonine (drug)]] 0.5 µM 0.370× (z -11.0) |
| [[SW48 (line)]] | wt | 151 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.253× (z -12.5) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -9.4) |
| [[A549 (line)]] | wt | 135 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 167 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.479× (z -8.7) |
| [[CHP-212 (line)]] | wt | 557 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -13.2) |
| [[H4 (line)]] | wt | 158 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.292× (z -11.7) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 299 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[HEC-1-A (line)]] | alt | 196 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.377× (z -10.6) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 118 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.254× (z -13.5) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 167 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -8.8) |
| [[A-427 (line)]] | wt | 17.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 153 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.3 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 135 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 147 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 69.6 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 20.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 444 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6346), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*33 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTEN]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[CYP39A1]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[RHOXF1]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ABHD4]] | +0.51 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[UBR2]] | +0.51 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[MTUS1]] | +0.50 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[CPEB3]] | +0.50 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[PTPN13]] | +0.50 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[AR]] | +0.50 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[BTN3A2]] | +0.50 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[MAPRE2]] | +0.49 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[ERP29]] | +0.49 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*67 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF710]] | -0.63 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[CORO2B]] | -0.59 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[CLMP]] | -0.58 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[KIAA1549L]] | -0.57 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[STK10]] | -0.56 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[NT5E]] | -0.56 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[TUBB6]] | -0.56 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[LINC02454]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[ZBED4]] | -0.54 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[ARHGAP22]] | -0.54 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[LINC00941]] | -0.53 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[LRWD1]] | -0.53 | -0.53 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02454]] | B | LINC02454 activity lowers MBNL2's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 2.20× higher at baseline in the lines without LINC02454 | 0.013 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers MBNL2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GPR161]] | B | GPR161 activity lowers MBNL2's level | lines that do not express GPR161 (6) vs lines expressing it (44) | 3.34× higher at baseline in the lines without GPR161 | 0.057 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PPP2R3A, NKAIN1 |
| [[LINC02454]] | B | LINC02454 activity weakens MBNL2's drug response | lines that do not express LINC02454 (11) vs lines expressing it (35) | the lines without LINC02454 respond 1.58× as strongly (z diff -2.29); strongest at Dinaciclib 0.5 µM: 0.30x vs 0.65x (z diff -6.0) | 0.068 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAI1]] | C | MBNL2 activity lowers GNAI1's level | lines that do not express MBNL2 (4) vs lines expressing it (46) | 2.06× higher at baseline in the lines without MBNL2 | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM102A, NINJ1, MYD88 |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction -0.618). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.5, 8.0); signed map (49.6, -13.9). **Vector** length 130, 43.0% of its response variance represented; |z| ≥ 3 in 1,663 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.8 | +5.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +5.7 | +6.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.7 | +6.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.6 | +5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.4 | +3.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.6 | -12.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -6.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.2 | -2.8 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -4.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.9 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.9 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | muscleblind like splicing regulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.1 — chr13:97,221,434-97,394,120 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MBLL, MBLL39 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; Muscleblind like splicing regulator family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VZF2](https://www.uniprot.org/uniprotkb/Q5VZF2) (Muscleblind-like protein 2):

> Mediates pre-mRNA alternative splicing regulation. Acts either as activator or repressor of splicing on specific pre-mRNA targets. Inhibits cardiac troponin-T (TNNT2) pre-mRNA exon inclusion but induces insulin receptor (IR) pre-mRNA exon inclusion in muscle. Antagonizes the alternative splicing activity pattern of CELF proteins. RNA-binding protein that binds to 5'ACACCC-3' core sequence, termed zipcode, within the 3'UTR of ITGA3. Binds to CUG triplet repeat expansion in myotonic dystrophy …

**Summary**, from NCBI Gene [10150](https://www.ncbi.nlm.nih.gov/gene/10150):

> This gene is a member of the muscleblind protein family which was initially described in Drosophila melanogaster. This gene encodes a C3H-type zinc finger protein that modulates alternative splicing of pre-mRNAs. Muscleblind proteins bind specifically to expanded dsCUG RNA but not to normal size CUG repeats and may thereby play a role in the pathophysiology of myotonic dystrophy. Several alternatively spliced transcript variants have been described but the full-length natures of only some have …

**Accessions** — [HGNC:16746](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16746) · Entrez [10150](https://www.ncbi.nlm.nih.gov/gene/10150) · UniProt [Q5VZF2](https://www.uniprot.org/uniprotkb/Q5VZF2) · Ensembl [ENSG00000139793](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139793)

## Data

Gene col 6346: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6346); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6346, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6346]; `tensor/DDL_lfc|DDL_z.npy` [6346]; `embed/gene_vectors.npy` [6346]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6346 or target_col == 6346). Every well: [[MBNL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MBNL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
