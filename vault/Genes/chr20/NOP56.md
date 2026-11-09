---
symbol: "NOP56"
type: "gene"
col: 2124
ensembl_id: "ENSG00000101361"
name: "NOP56 ribonucleoprotein"
location: "20p13"
module: 5
arm: "+"
pooled_cpm: 71.76
n_lines_expressing: 50
n_dd_up: 48
n_dd_down: 2
n_dd_up_clean: 25
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NOP56

*NOP56 ribonucleoprotein* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 48 drug-doses (23 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.82× (z +13.7, q 6e-40, up in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 3.17× (z +11.1, q 3e-26, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Anethole trithione (drug)]] 0.5 µM: 0.628× (z -4.5, q 0.003, down in 42 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (SW 1271 0.0599×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPATCH4]] (+0.76, fdr 7e-06), [[NIP7]] (+0.73, fdr 7e-06), [[MRTO4]] (+0.72, fdr 7e-06); moves opposite to [[PJA2]] (-0.72, fdr 7e-06), [[FKBP8]] (-0.66, fdr 7e-06), [[TM9SF2]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 23 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 48 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2124.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.82×** | +13.7 | 6e-40 | 41/48 (C32, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **4.23×** | +13.3 | 5e-38 | 47/47 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.17×** | +11.1 | 3e-26 | 45/48 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **3.18×** | +10.7 | 2e-24 | 48/48 (C32, AsPC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.82×** | +10.0 | 3e-21 | 46/48 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.59×** | +9.1 | 6e-18 | 47/48 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.98×** | +9.0 | 2e-17 | 41/48 (CFPAC-1, A549, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **2.53×** | +8.9 | 4e-17 | 47/49 (NCI-H1792, HS-578T, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **2.25×** | +7.8 | 6e-13 | 37/48 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.22×** | +7.6 | 1e-12 | 47/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **2.13×** | +7.3 | 2e-11 | 41/48 (H4, SW 900, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.06×** | +6.9 | 2e-10 | 40/48 (HOP62, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **2.06×** | +6.9 | 2e-10 | 37/48 (SW1417, H4, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change | **2.06×** | +6.7 | 1e-09 | 36/43 (A549, NCI-H1792, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **2.03×** | +6.3 | 2e-08 | 37/45 (NCI-H1792, NCI-H1573, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.58×** | +6.0 | 9e-08 | 41/48 (CFPAC-1, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.71×** | +5.1 | 7e-06 | 35/48 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +4.9 | 2e-05 | 39/48 (A549, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.60×** | +4.3 | 3e-04 | 31/48 (NCI-H1792, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +4.3 | 4e-04 | 32/48 (HOP62, A549, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **2.29×** | +3.7 | 0.005 | 30/48 (A549, NCI-H460, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.17×** | +3.4 | 0.012 | 29/48 (A549, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **2.13×** | +3.3 | 0.015 | 28/48 (A549, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.11×** | +3.3 | 0.017 | 28/48 (NCI-H460, A549, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.95×** | +3.2 | 0.025 | 26/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **2.03×** | +3.1 | 0.029 | 22/48 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.92×** | +3.1 | 0.031 | 24/48 (A-427, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2124.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (SW 1271 0.0599×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.628×** | -4.5 | 0.003 | 42/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.739×** | -4.1 | 0.012 | 37/48 (A-427, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Anethole trithione (drug)]] 0.05 µM |  | 0.728× | -3.1 | 0.23 | 24/48 (LOX-IMVI, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.680× | -3.1 | 0.23 | 21/50 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.711× | -3.1 | 0.23 | 26/48 (LoVo, SW480, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.83 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2124. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 48.8 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +21.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 13.7× (z +16.6) | — |
| [[CFPAC-1 (line)]] | alt | 54.7 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +16.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.63× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 45.7 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +11.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.53× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 29.1 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +19.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.82× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 43.8 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +12.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.86× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 61.5 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +11.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.64× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 60.6 | 5 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.89× (z +11.7) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 5.37× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 50.0 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +10.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.78× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 65.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.35× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 57.4 | 4 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.69× (z +11.6) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 2.44× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 71.1 | 4 (4 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.73× (z +11.1) ⚠ toxic | — |
| [[SW1417 (line)]] | alt | 66.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.89× (z +8.8) | — |
| [[A549 (line)]] | wt | 61.2 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +12.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[Hs 766T (line)]] | wt | 38.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.94× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 47.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +11.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.59× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 41.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.90× (z +14.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.70× (z +9.4) | — |
| [[KATO III (line)]] | alt | 80.8 | 3 (3 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 9.20× (z +14.1) ⚠ toxic | — |
| [[LS 180 (line)]] | wt | 69.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +11.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.85× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 49.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.21× (z +10.4) | — |
| [[SW 900 (line)]] | alt | 58.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +12.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.79× (z +8.9) | — |
| [[A498 (line)]] | wt | 42.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +12.5) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[COLO 205 (line)]] | alt | 56.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.83× (z +11.4) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[H4 (line)]] | wt | 39.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +10.1) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[HEC-1-A (line)]] | alt | 75.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.9) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[J82 (line)]] | alt | 87.8 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.78× (z +11.1) ⚠ toxic | — |
| [[NCI-H1573 (line)]] | alt | 25.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +12.8) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[RPMI-7951 (line)]] | alt | 65.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +9.9) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SHP-77 (line)]] | alt | 103 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.92× (z +10.0) | — |
| [[SW480 (line)]] | alt | 145 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.27× (z +11.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.98× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 82.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 8.96× (z +12.8) ⚠ toxic | — |
| [[LoVo (line)]] | wt | 73.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +10.5) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 81.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.72× (z +11.8) ⚠ toxic | — |
| [[PANC-1 (line)]] | alt | 98.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.64× (z +8.5) ⚠ toxic | — |
| [[SK-MEL-2 (line)]] | alt | 90.8 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.59× (z +8.6) | — |
| [[SW 1271 (line)]] | alt | 76.1 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0599× (z -9.2) |
| [[A-172 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 81.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 136 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 160 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 130 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2124), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH4]] | +0.76 | +0.81 / +0.68 | both halves | 7e-06 |  |
| [[NIP7]] | +0.73 | +0.78 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 934 |
| [[MRTO4]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 941 |
| [[PPRC1]] | +0.70 | +0.65 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[PUS1]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 566 |
| [[NOP2]] | +0.66 | +0.61 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 969 |
| [[DHX37]] | +0.66 | +0.72 / +0.50 | both halves | 1e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 943 |
| [[NOP16]] | +0.66 | +0.61 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 462 |
| [[UTP20]] | +0.64 | +0.76 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 997 |
| [[TTC27]] | +0.64 | +0.69 / +0.49 | both halves | 1e-05 | same gene group |
| [[RRS1]] | +0.63 | +0.64 / +0.67 | both halves | 7e-06 | STRING 848 |
| [[EIF3J]] | +0.63 | +0.74 / +0.57 | both halves | 8e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PJA2]] | -0.72 | -0.81 / -0.59 | both halves | 7e-06 |  |
| [[FKBP8]] | -0.66 | -0.69 / -0.63 | both halves | 7e-06 |  |
| [[TM9SF2]] | -0.65 | -0.72 / -0.63 | both halves | 7e-06 |  |
| [[ARL3]] | -0.65 | -0.72 / -0.38 | both halves | 7e-05 |  |
| [[ALDH6A1]] | -0.64 | -0.57 / -0.62 | both halves | 9e-06 |  |
| [[VAMP7]] | -0.64 | -0.69 / -0.53 | both halves | 1e-05 |  |
| [[LAPTM4A]] | -0.63 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[MOSPD3]] | -0.60 | -0.71 / -0.41 | both halves | 4e-05 |  |
| [[PPP1R2]] | -0.60 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[CCNG1]] | -0.59 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[GTF2IP4]] | -0.59 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[MAPK3]] | -0.59 | -0.64 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NOP56's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.666). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.5, -36.3); signed map (-0.7, -46.1). **Vector** length 87.5, 37.4% of its response variance represented; |z| ≥ 3 in 1,334 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.0 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +11.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.9 | +4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +3.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | -5.2 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change | -5.1 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | -4.8 | +6.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.8 | +4.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | NOP56 ribonucleoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:2,652,593-2,658,393 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SCA36; previously NOL5A |
| Gene groups (HGNC) | U3 small nucleolar ribonucleoprotein; MicroRNA protein coding host genes; Small nucleolar RNA protein coding host genes |
| Hallmark sets | MYC_TARGETS_V2, UNFOLDED_PROTEIN_RESPONSE, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 8 pathways, smallest: Association of TriC/CCT with target proteins during biosynthesis; rRNA modification in the nucleus and cytosol; Chaperonin-mediated protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [O00567](https://www.uniprot.org/uniprotkb/O00567) (Nucleolar protein 56):

> Involved in the early to middle stages of 60S ribosomal subunit biogenesis. Required for the biogenesis of box C/D snoRNAs such U3, U8 and U14 snoRNAs. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements …

**Summary**, from NCBI Gene [10528](https://www.ncbi.nlm.nih.gov/gene/10528):

> Nop56p is a yeast nucleolar protein that is part of a complex with the nucleolar proteins Nop58p and fibrillarin. Nop56p is required for assembly of the 60S ribosomal subunit and is involved in pre-rRNA processing. The protein encoded by this gene is similar in sequence to Nop56p and is also found in the nucleolus. Expansion of a GGCCTG repeat from 3-8 copies to 1500-2500 copies in an intron of this gene results in spinocerebellar ataxia 36. Multiple transcript variants encoding several …

**Accessions** — [HGNC:15911](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15911) · Entrez [10528](https://www.ncbi.nlm.nih.gov/gene/10528) · UniProt [O00567](https://www.uniprot.org/uniprotkb/O00567) · Ensembl [ENSG00000101361](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101361)

## Data

Gene col 2124: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2124); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2124, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2124]; `tensor/DDL_lfc|DDL_z.npy` [2124]; `embed/gene_vectors.npy` [2124]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2124 or target_col == 2124). Every well: [[NOP56 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOP56.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
