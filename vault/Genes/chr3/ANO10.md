---
symbol: "ANO10"
type: "gene"
col: 8375
ensembl_id: "ENSG00000160746"
name: "anoctamin 10"
location: "3p22.1-p21.33"
module: 40
arm: "+"
pooled_cpm: 118.76
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 22
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# ANO10

*anoctamin 10* — 3p22.1-p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.05 µM: 1.78× (z +14.4, q 5e-44, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.393× (z -33.0, q 0e+00, down in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.307× (z -15.5, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGTB]] (+0.74, fdr 7e-06), [[DYM]] (+0.68, fdr 1e-05), [[AAK1]] (+0.67, fdr 1e-05); moves opposite to [[CHTOP]] (-0.63, fdr 1e-05), [[SERTAD4]] (-0.63, fdr 1e-05), [[HNRNPL]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HACE1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8375.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM |  | **1.78×** | +14.4 | 5e-44 | 47/49 (LS 180, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.65×** | +12.5 | 2e-33 | 46/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.42×** | +12.4 | 6e-33 | 28/48 (PANC-1, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.61×** | +11.9 | 1e-30 | 37/48 (LS 180, NCI-H1573, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +9.7 | 3e-20 | 33/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +9.6 | 7e-20 | 35/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +7.4 | 1e-11 | 32/48 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.37×** | +7.4 | 1e-11 | 31/48 (HT-29, LS 180, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +7.2 | 4e-11 | 28/48 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.31×** | +6.7 | 1e-09 | 29/48 (HT-29, H4, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +6.2 | 2e-08 | 37/49 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **1.52×** | +5.5 | 2e-06 | 28/45 (LS 180, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +5.5 | 2e-06 | 17/48 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.50×** | +5.3 | 5e-06 | 30/48 (HOP62, A498, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +5.3 | 5e-06 | 24/48 (SW1417, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +5.2 | 7e-06 | 20/49 (C32, CFPAC-1, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.38×** | +4.2 | 7e-04 | 19/48 (A498, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.8 | 0.004 | 19/48 (HT-29, SNU-423, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.16× | +3.6 | 0.008 | 12/49 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.031 | 6/49 (A498, HS-578T, …) | rises with dose | plate-row cell shift |
| [[Tomivosertib (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.035 | 12/48 (HOP62, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8375.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.393×** | -33.0 | 0e+00 | 46/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.491×** | -16.4 | 0e+00 | 41/45 (SW1417, J82, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.511×** | -16.2 | 0e+00 | 40/48 (A498, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.528×** | -16.0 | 0e+00 | 42/48 (LS 180, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.526×** | -15.5 | 0e+00 | 36/44 (SK-MEL-2, SW1417, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.307×** | -15.5 | 0e+00 | 44/49 (NCI-H2347, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.543×** | -15.3 | 0e+00 | 43/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.546×** | -15.2 | 0e+00 | 40/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.559×** | -14.5 | 0e+00 | 43/49 (NCI-H2347, SW1417, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.426×** | -11.1 | 4e-27 | 36/48 (HOP62, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.640×** | -10.8 | 3e-25 | 35/47 (HepG2/C3A, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.663×** | -10.3 | 3e-23 | 35/48 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.673×** | -9.9 | 2e-21 | 34/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.694×** | -9.1 | 2e-18 | 37/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.799×** | -8.0 | 6e-14 | 33/48 (SW1417, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.789×** | -5.9 | 1e-07 | 28/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.795×** | -5.3 | 3e-06 | 28/47 (LS 180, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **0.819×** | -5.0 | 1e-05 | 25/48 (LoVo, RPMI-7951, …) | rises with dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.881× | -3.2 | 0.032 | 5/47 (A498, LS 180, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.885× | -3.0 | 0.062 | 11/49 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.891× | -2.9 | 0.071 | 6/48 (COLO 205, hTERT-HPNE, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.885× | -2.9 | 0.074 | 17/47 (SW1417, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8375. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 71.3 | 4 (2 ⚠) | 13 (12 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.25× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -20.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.420× (z -11.1) |
| [[PANC-1 (line)]] | alt | 86.0 | 5 (2 ⚠) | 12 (11 ⚠) | [[Selinexor (drug)]] 5 µM 1.81× (z +14.1) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Selinexor (drug)]] 0.05 µM 2.03× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -40.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.373× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 119 | 2 (1 ⚠) | 12 (10 ⚠) | [[Selinexor (drug)]] 0.5 µM 1.98× (z +9.6) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Selinexor (drug)]] 0.05 µM 1.96× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -34.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.197× (z -11.9) |
| [[LS 180 (line)]] | wt | 103 | 6 (4 ⚠) | 8 (7 ⚠) | [[Selinexor (drug)]] 5 µM 2.28× (z +14.0) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Selinexor (drug)]] 0.05 µM 2.82× (z +12.4) | [[Digitoxin (drug)]] 5 µM 0.274× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.230× (z -9.2) |
| [[SW1417 (line)]] | alt | 186 | 4 (2 ⚠) | 10 (8 ⚠) | [[Selinexor (drug)]] 5 µM 1.59× (z +9.9) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Selinexor (drug)]] 0.05 µM 1.91× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.626× (z -10.0) |
| [[HOP62 (line)]] | alt | 142 | 1 (1 ⚠) | 12 (10 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.05× (z +10.5) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -35.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.190× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 73.9 | 3 (2 ⚠) | 10 (9 ⚠) | [[Selinexor (drug)]] 5 µM 1.84× (z +11.3) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Selinexor (drug)]] 0.05 µM 2.12× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -27.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.277× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 173 | 1 (1 ⚠) | 12 (10 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.08× (z +11.1) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.226× (z -11.9) |
| [[A-172 (line)]] | wt | 137 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -26.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.255× (z -9.6) |
| [[HS-578T (line)]] | alt | 274 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -36.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.232× (z -9.6) |
| [[A498 (line)]] | wt | 200 | 1 (1 ⚠) | 9 (8 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.44× (z +13.5) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -29.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.243× (z -11.3) |
| [[J82 (line)]] | alt | 174 | 0 | 9 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -27.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[LoVo (line)]] | wt | 104 | 2 (1 ⚠) | 7 (6 ⚠) | [[Selinexor (drug)]] 5 µM 1.88× (z +10.3) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Selinexor (drug)]] 0.05 µM 2.14× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.254× (z -16.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.211× (z -9.5) |
| [[SNU-1 (line)]] | wt | 127 | 0 | 8 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -13.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[C32 (line)]] | wt | 191 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -22.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HT-29 (line)]] | alt | 55.4 | 3 (2 ⚠) | 4 (4 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.75× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -11.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[KATO III (line)]] | alt | 81.5 | 2 (1 ⚠) | 5 (5 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.32× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.222× (z -15.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[RPMI-7951 (line)]] | alt | 171 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -21.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.169× (z -10.8) |
| [[A549 (line)]] | wt | 110 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -24.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.228× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 153 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.04× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.572× (z -11.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.287× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 105 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -23.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[Panc 03.27 (line)]] | alt | 130 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.177× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 179 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -19.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW480 (line)]] | alt | 90.1 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.317× (z -15.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.503× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 89.4 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -16.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 143 | 1 (1 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.58× (z +9.5) ⚠ cell-cycle shift, explains ~62% of this change | [[Harringtonine (drug)]] 5 µM 0.511× (z -9.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.661× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 58.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -13.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[BT-474 (line)]] | alt | 76.4 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.400× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[MIA PaCa-2 (line)]] | alt | 57.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.44× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -9.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H1792 (line)]] | alt | 82.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -30.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.156× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 86.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -10.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[COLO 205 (line)]] | alt | 49.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.281× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[H4 (line)]] | wt | 76.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.86× (z +8.8) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 0.5 µM 0.181× (z -14.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Hs 766T (line)]] | wt | 104 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -13.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[hTERT-HPNE (line)]] | wt | 194 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -15.1) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 109 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -27.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[RKO (line)]] | wt | 120 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.428× (z -9.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 123 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -20.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW 900 (line)]] | alt | 95.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.34× (z +8.7) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -9.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[AN3 CA (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -21.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[C-33 A (line)]] | alt | 149 | 1 | 0 | [[Osimertinib (mesylate) (drug)]] 5 µM 2.12× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.401× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW48 (line)]] | wt | 90.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.346× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[CHP-212 (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 97.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 158 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8375), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGTB]] | +0.74 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[DYM]] | +0.68 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[AAK1]] | +0.67 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[RAB6A]] | +0.66 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[COG5]] | +0.66 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[SCAI]] | +0.66 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[MPZL1]] | +0.64 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[SS18L1]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.63 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[ATP7B]] | +0.63 | +0.64 / +0.49 | both halves | 1e-05 | pathway: Ion channel transport |
| [[UBE2Q2P2]] | +0.63 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[SLC25A29]] | +0.61 | +0.66 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHTOP]] | -0.63 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[SERTAD4]] | -0.63 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[HNRNPL]] | -0.60 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[HNRNPUL1]] | -0.60 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[BCLAF1]] | -0.59 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[ZNF776]] | -0.58 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[MED12]] | -0.58 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[DDX39B]] | -0.57 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[SRSF10]] | -0.57 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[SRRM2]] | -0.57 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[EP300]] | -0.56 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[PCF11]] | -0.56 | -0.59 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HACE1]] | C | HACE1 activity raises ANO10's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 2.14× lower at baseline in the lines without HACE1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (2.6, -20.8); signed map (-44.5, 6.7). **Vector** length 146, 52.2% of its response variance represented; |z| ≥ 3 in 1,730 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +9.3 | +12.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +9.3 | +11.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +8.8 | +6.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | +8.6 | +7.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.5 | +7.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +7.0 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.0 | +3.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +5.9 | +5.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +5.1 | +12.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.0 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -11.1 | -33.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -9.9 | -15.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.2 | -16.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -8.3 | -15.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.2 | -11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.1 | -8.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -5.5 | -5.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.2 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | anoctamin 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.1-p21.33 — chr3:43,354,859-43,691,594 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10375, MGC47890, SCAR10; previously TMEM16K |
| Gene groups (HGNC) | Anoctamins |
| Reactome | 8 pathways, smallest: Induction of Cell-Cell Fusion; Late SARS-CoV-2 Infection Events; Stimuli-sensing channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NW15](https://www.uniprot.org/uniprotkb/Q9NW15) (Anoctamin-10):

> Does not exhibit calcium-activated chloride channel (CaCC) activity. Can inhibit the activity of ANO1.

**Summary**, from NCBI Gene [55129](https://www.ncbi.nlm.nih.gov/gene/55129):

> The transmembrane protein encoded by this gene belongs to the anoctamin family of calcium-activated chloride channels, also known as the transmembrane 16 family. The encoded protein contains eight transmembrane domains with cytosolic N- and C-termini. Defects in this gene may cause autosomal recessive spinocerebellar ataxia-10. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:25519](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25519) · Entrez [55129](https://www.ncbi.nlm.nih.gov/gene/55129) · UniProt [Q9NW15](https://www.uniprot.org/uniprotkb/Q9NW15) · Ensembl [ENSG00000160746](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160746)

## Data

Gene col 8375: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8375); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8375, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8375]; `tensor/DDL_lfc|DDL_z.npy` [8375]; `embed/gene_vectors.npy` [8375]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8375 or target_col == 8375). Every well: [[ANO10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANO10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
