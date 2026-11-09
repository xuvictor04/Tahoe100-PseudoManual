---
symbol: "UMAD1"
type: "gene"
col: 13298
ensembl_id: "ENSG00000219545"
name: "UBAP1-MVB12-associated (UMA) domain containing 1"
location: "7p21.3"
module: 24
arm: "+"
pooled_cpm: 178.89
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 23
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# UMAD1

*UBAP1-MVB12-associated (UMA) domain containing 1* — 7p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.36× (z +5.5, q 2e-05, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.409× (z -16.0, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.625× (z -8.4, q 5e-15, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MICU1]] (+0.67, fdr 1e-05), [[IFT43]] (+0.64, fdr 7e-06), [[NPC2]] (+0.60, fdr 1e-05); moves opposite to [[GPR63]] (-0.52, fdr 3e-05), [[SLC35F2]] (-0.50, fdr 3e-05), [[KCTD12]] (-0.49, fdr 2e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13298.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +5.5 | 2e-05 | 29/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.20×** | +4.7 | 8e-04 | 22/48 (J82, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +4.5 | 0.001 | 27/48 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.56×** | +4.1 | 0.005 | 36/50 (AsPC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.54×** | +4.1 | 0.006 | 29/49 (BT-474, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.048 | 29/49 (NCI-H460, BT-474, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.20×** | +3.3 | 0.066 | 22/48 (NCI-H460, BT-474, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.22×** | +3.3 | 0.066 | 22/48 (C32, HepG2/C3A, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.28× | +3.1 | 0.11 | 21/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.20× | +3.0 | 0.12 | 17/48 (NCI-H1573, H4, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.20× | +3.0 | 0.12 | 23/47 (AsPC-1, C32, …) | rises with dose |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | 1.27× | +3.0 | 0.12 | 23/48 (NCI-H1573, BT-474, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13298.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.409×** | -16.0 | 0e+00 | 47/49 (KATO III, H4, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.441×** | -13.3 | 6e-38 | 39/44 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.492×** | -11.7 | 2e-29 | 41/45 (KATO III, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.550×** | -9.7 | 4e-20 | 42/47 (NCI-H1792, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.585×** | -8.7 | 3e-16 | 40/47 (CFPAC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.625×** | -8.4 | 5e-15 | 43/48 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.693×** | -6.5 | 5e-09 | 31/48 (A498, SNU-423, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **0.693×** | -6.5 | 5e-09 | 39/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.505×** | -6.4 | 1e-08 | 32/38 (AsPC-1, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.686×** | -6.1 | 5e-08 | 32/48 (SNU-423, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.710×** | -6.1 | 5e-08 | 41/48 (SNU-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.710×** | -6.1 | 5e-08 | 31/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.792×** | -5.9 | 2e-07 | 27/48 (RPMI-7951, Hs 766T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.776×** | -4.5 | 3e-04 | 29/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.637×** | -4.2 | 0.001 | 27/45 (H4, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.793×** | -4.1 | 0.001 | 29/47 (MIA PaCa-2, H4, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.781×** | -4.1 | 0.002 | 29/47 (C32, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.831×** | -3.3 | 0.030 | 21/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.703×** | -3.3 | 0.030 | 27/48 (SNU-1, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.785×** | -3.1 | 0.053 | 25/48 (MIA PaCa-2, H4, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.885× | -3.1 | 0.054 | 13/49 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.828×** | -3.0 | 0.054 | 24/47 (H4, NCI-H460, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.726×** | -3.0 | 0.065 | 21/48 (A498, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.730×** | -2.9 | 0.075 | 20/48 (SK-MEL-2, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 0.5 µM |  | 0.849× | -2.9 | 0.075 | 15/48 (LOX-IMVI, A498, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13298. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 229 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -18.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.336× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 307 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.499× (z -9.0) |
| [[SNU-423 (line)]] | alt | 190 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -15.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.458× (z -9.2) |
| [[C32 (line)]] | wt | 146 | 1 (1 ⚠) | 7 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.36× (z +8.9) ⚠ cell-cycle shift, explains ~88% of this change | [[Harringtonine (drug)]] 0.5 µM 0.314× (z -12.8) |
| [[PANC-1 (line)]] | alt | 205 | 5 (4 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +15.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 1.98× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 181 | 0 | 7 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.283× (z -14.5) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.353× (z -13.1) |
| [[A-427 (line)]] | wt | 164 | 3 (3 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[CFPAC-1 (line)]] | alt | 113 | 0 | 6 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.294× (z -12.6) ⚠ toxic |
| [[KATO III (line)]] | alt | 364 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -22.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H460 (line)]] | wt | 160 | 2 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +14.9) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.367× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[RPMI-7951 (line)]] | alt | 197 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.209× (z -9.4) |
| [[SW480 (line)]] | alt | 248 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -22.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.403× (z -14.4) |
| [[H4 (line)]] | wt | 362 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.407× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 150 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.558× (z -10.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.522× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 153 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.300× (z -12.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.356× (z -12.0) |
| [[A-172 (line)]] | wt | 155 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.415× (z -10.5) |
| [[LoVo (line)]] | wt | 214 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 180 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.387× (z -11.0) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 225 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +13.2) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.325× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[Panc 03.27 (line)]] | alt | 181 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW 900 (line)]] | alt | 197 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW1417 (line)]] | alt | 207 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.480× (z -9.0) |
| [[A549 (line)]] | wt | 170 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -12.9) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.473× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 172 | 0 | 3 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.125× (z -12.5) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 202 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HOP62 (line)]] | alt | 139 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.339× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.495× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 118 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -11.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.363× (z -9.1) |
| [[HT-29 (line)]] | alt | 167 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[J82 (line)]] | alt | 102 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.78× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.389× (z -9.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 250 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SK-MEL-2 (line)]] | alt | 197 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-1 (line)]] | wt | 96.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.294× (z -10.8) |
| [[AN3 CA (line)]] | alt | 184 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[C-33 A (line)]] | alt | 98.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -9.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LOX-IMVI (line)]] | wt | 127 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.359× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW 1271 (line)]] | alt | 331 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 103 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 161 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 223 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13298), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICU1]] | +0.67 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[IFT43]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[NPC2]] | +0.60 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[UXT]] | +0.59 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[ZNHIT1]] | +0.59 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[WDR83OS]] ⚠ | +0.58 | +0.66 / +0.47 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PFDN5]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[WDR19]] | +0.57 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[KATNIP]] | +0.57 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[ALKBH7]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[TNKS]] | +0.56 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[MED31]] | +0.55 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[EMC3]] | +0.55 | +0.59 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR63]] | -0.52 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[SLC35F2]] | -0.50 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[KCTD12]] | -0.49 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[DUSP7]] | -0.49 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[HEATR3]] | -0.49 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[TMSB15B]] | -0.48 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[DDAH1]] | -0.48 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[P2RX5]] | -0.47 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[SEPTIN11]] | -0.47 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[RIOX2]] | -0.46 | -0.50 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers UMAD1's level | compounds that target MTOR: 3 of 8 raise it (Bimiralisib, GSK1059615, Sapanisertib) | 38% of the class's compounds vs 2.0% of all compounds | 0.088 | ⚠ off-target possible; 3 compounds |
| [[POLR2J4]] | C | POLR2J4's natural level strengthens UMAD1's drug response | POLR2J4's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.39; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[BBS9]] | C | BBS9's natural level strengthens UMAD1's drug response | BBS9's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.34; direction not clear | 0.089 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | UMAD1's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | UMAD1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.61 | 0.452 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.421). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-26.8, -11.9); signed map (-19.4, 2.7). **Vector** length 110, 40.7% of its response variance represented; |z| ≥ 3 in 1,390 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.1 | -0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +1.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~88% of this change | +4.5 | +3.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.5 | -3.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.6 | +1.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.6 | +4.1 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.5 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -11.3 | -5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.7 | -3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.4 | -11.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.2 | -6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -6.0 | -13.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.6 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -6.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | UBAP1-MVB12-associated (UMA) domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.3 — chr7:7,640,711-7,968,020 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RPA3-AS1, RPA3OS |
| Matched by | ensembl_id |

UniProt [C9J7I0](https://www.uniprot.org/uniprotkb/C9J7I0) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48955](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48955) · Entrez [729852](https://www.ncbi.nlm.nih.gov/gene/729852) · UniProt [C9J7I0](https://www.uniprot.org/uniprotkb/C9J7I0) · Ensembl [ENSG00000219545](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000219545)

## Data

Gene col 13298: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13298); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13298, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13298]; `tensor/DDL_lfc|DDL_z.npy` [13298]; `embed/gene_vectors.npy` [13298]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13298 or target_col == 13298). Every well: [[UMAD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UMAD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
