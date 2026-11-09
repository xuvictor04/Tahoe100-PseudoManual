---
symbol: "CCNG2"
type: "gene"
col: 6230
ensembl_id: "ENSG00000138764"
name: "cyclin G2"
location: "4q21.1"
module: 69
arm: "+"
pooled_cpm: 94.17
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 27
n_dd_up_clean: 8
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# CCNG2

*cyclin G2* — 4q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.77× (z +14.5, q 1e-44, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (15 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.441× (z -14.6, q 1e-45, down in 46 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.419× (z -8.1, q 4e-14, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM117A]] (+0.69, fdr 2e-05), [[OGA]] (+0.69, fdr 7e-06), [[OSER1-DT]] (+0.68, fdr 3e-05); moves opposite to [[EIF2B3]] (-0.68, fdr 7e-06), [[LETM1]] (-0.67, fdr 7e-06), [[CTPS1]] (-0.66, fdr 7e-06).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF563]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6230.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.77×** | +14.5 | 1e-44 | 45/48 (LS 180, LoVo, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **2.03×** | +12.7 | 3e-34 | 48/49 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +11.5 | 3e-28 | 36/49 (A498, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.87×** | +11.2 | 6e-27 | 44/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.37×** | +8.1 | 9e-14 | 40/49 (LoVo, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.55×** | +7.8 | 5e-13 | 41/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.26×** | +5.8 | 6e-07 | 23/48 (NCI-H1792, SW1417, …) | inconsistent across doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **1.33×** | +5.2 | 2e-05 | 27/48 (SW1417, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +5.1 | 2e-05 | 26/49 (SW1417, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.003 | 21/49 (NCI-H460, NCI-H2347, …) | top dose only | plate-row cell shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.15× | +3.5 | 0.021 | 15/48 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.21×** | +3.5 | 0.022 | 22/48 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.3 | 0.046 | 22/48 (HOP62, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.0 | 0.10 | 21/48 (NCI-H1792, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 15 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6230.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.441×** | -14.6 | 1e-45 | 46/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.499×** | -11.9 | 3e-30 | 37/43 (A-427, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.581×** | -9.7 | 7e-20 | 41/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.595×** | -9.3 | 3e-18 | 41/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.597×** | -9.2 | 5e-18 | 43/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.611×** | -8.8 | 2e-16 | 36/49 (A-427, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.419×** | -8.1 | 4e-14 | 42/48 (Panc 03.27, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.635×** | -7.8 | 5e-13 | 35/47 (NCI-H1573, H4, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.471×** | -7.0 | 1e-10 | 38/48 (SW 900, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.498×** | -6.5 | 4e-09 | 38/48 (SW48, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.698×** | -6.4 | 9e-09 | 28/48 (HCT15, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.697×** | -6.1 | 7e-08 | 35/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.729×** | -5.6 | 8e-07 | 34/48 (CFPAC-1, NCI-H1573, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.554×** | -5.5 | 2e-06 | 27/45 (NCI-H1792, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.556×** | -5.5 | 2e-06 | 32/48 (BT-474, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.769×** | -4.7 | 9e-05 | 28/48 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.621×** | -4.4 | 3e-04 | 26/48 (NCI-H2347, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.739×** | -3.8 | 0.003 | 23/48 (PANC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.826×** | -3.4 | 0.017 | 18/48 (NCI-H460, HepG2/C3A, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.837× | -3.1 | 0.038 | 17/49 (RPMI-7951, NCI-H1573, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.716×** | -3.1 | 0.041 | 12/49 (CFPAC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.831×** | -3.1 | 0.042 | 17/48 (LoVo, SW48, …) | all doses, stronger at high dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.888× | -3.0 | 0.062 | 9/48 (RPMI-7951, COLO 205, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.794×** | -2.9 | 0.070 | 15/49 (NCI-H23, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.851× | -2.9 | 0.080 | 18/48 (NCI-H2030, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.57 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6230. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 210 | 2 | 12 (11 ⚠) | [[Selinexor (drug)]] 5 µM 2.05× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.114× (z -22.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -17.3) |
| [[SW 900 (line)]] | alt | 114 | 2 | 8 (7 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.69× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -10.9) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.386× (z -9.8) |
| [[LoVo (line)]] | wt | 68.5 | 7 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.51× (z +12.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.325× (z -11.0) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 292 | 0 | 8 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.390× (z -13.3) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HT-29 (line)]] | alt | 61.7 | 6 | 1 | [[Selinexor (drug)]] 0.05 µM 3.18× (z +11.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.409× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 113 | 3 (3 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +25.5) ⚠ cell-cycle shift, explains ~61% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[A-427 (line)]] | wt | 101 | 1 | 5 (4 ⚠) | [[GSK1059615 (drug)]] 5 µM 5.27× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0527× (z -30.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.385× (z -9.7) |
| [[HCT15 (line)]] | alt | 201 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[A498 (line)]] | wt | 61.7 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +14.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.259× (z -12.1) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 204 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +14.5) | [[Digitoxin (drug)]] 5 µM 0.399× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 281 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HEC-1-A (line)]] | alt | 86.3 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +13.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.460× (z -8.6) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 95.2 | 3 | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.72× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[NCI-H460 (line)]] | wt | 62.2 | 4 (2 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.05× (z +11.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.353× (z -11.2) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 97.1 | 2 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.330× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[Panc 03.27 (line)]] | alt | 149 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.397× (z -10.6) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.208× (z -9.4) |
| [[PANC-1 (line)]] | alt | 36.1 | 3 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +11.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.379× (z -9.8) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 50.4 | 1 | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.28× (z +10.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.353× (z -9.3) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 195 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0573× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[COLO 205 (line)]] | alt | 42.9 | 2 | 1 | [[Selinexor (drug)]] 5 µM 2.96× (z +10.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -13.9) |
| [[MIA PaCa-2 (line)]] | alt | 64.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.147× (z -17.1) |
| [[NCI-H2030 (line)]] | alt | 143 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H23 (line)]] | alt | 69.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SK-MEL-2 (line)]] | alt | 67.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +14.0) ⚠ cell-cycle shift, explains ~61% of this change | [[Dinaciclib (drug)]] 5 µM 0.163× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW1417 (line)]] | alt | 76.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +17.2) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +10.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.393× (z -10.3) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 60.4 | 2 | 0 | [[Selinexor (drug)]] 5 µM 2.53× (z +9.6) | — |
| [[C32 (line)]] | wt | 121 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[J82 (line)]] | alt | 46.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +12.2) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +9.8) | — |
| [[KATO III (line)]] | alt | 50.6 | 1 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.28× (z +9.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.285× (z -9.9) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 37.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +10.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.291× (z -9.3) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 107 | 1 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.27× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.379× (z -9.2) ⚠ cell-cycle shift, explains ~64% of this change |
| [[SHP-77 (line)]] | alt | 48.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.3) | — |
| [[SW480 (line)]] | alt | 55.9 | 2 | 0 | [[Selinexor (drug)]] 5 µM 2.10× (z +11.2) | — |
| [[A549 (line)]] | wt | 45.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +8.5) | — |
| [[H4 (line)]] | wt | 126 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.206× (z -11.2) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 43.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +9.8) | — |
| [[RKO (line)]] | wt | 47.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 58.3 | 1 | 0 | [[Selinexor (drug)]] 5 µM 4.09× (z +12.2) | — |
| [[SW 1271 (line)]] | alt | 113 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.175× (z -8.9) |
| [[SW48 (line)]] | wt | 80.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.301× (z -8.8) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 189 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 81.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 108 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 168 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6230), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM117A]] | +0.69 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[OGA]] | +0.69 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[OSER1-DT]] | +0.68 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[CERT1]] | +0.68 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[CDKN1B]] | +0.67 | +0.60 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 570 |
| [[CREBRF]] | +0.67 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[HBP1]] | +0.66 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[TSC22D4]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[CCDC115]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[UBXN7]] | +0.65 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[CLK1]] | +0.65 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[ATOSA]] | +0.63 | +0.58 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2B3]] | -0.68 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[LETM1]] | -0.67 | -0.64 / -0.71 | both halves | 7e-06 |  |
| [[CTPS1]] | -0.66 | -0.65 / -0.72 | both halves | 7e-06 |  |
| [[NAA15]] | -0.62 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[TCOF1]] | -0.62 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[DDX21]] | -0.61 | -0.58 / -0.67 | both halves | 8e-06 |  |
| [[NOM1]] | -0.61 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | -0.60 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[URB2]] | -0.60 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[PSMD1]] | -0.59 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[PUS1]] | -0.59 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[POLR1A]] | -0.59 | -0.56 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF563]] | B | ZNF563 activity raises CCNG2's level | lines that do not express ZNF563 (9) vs lines expressing it (41) | 1.45× lower at baseline in the lines without ZNF563 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZNF442, ZNF433, ENSG00000269755 |
| [[ZNF433]] | B | ZNF433 activity raises CCNG2's level | lines that do not express ZNF433 (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without ZNF433 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF563, ZNF442 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.5, -41.6); signed map (-11.7, 8.8). **Vector** length 152, 51.4% of its response variance represented; |z| ≥ 3 in 1,582 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +17.4 | +14.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.6 | +11.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +11.4 | +11.2 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +8.7 | +12.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +7.2 | +7.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.5 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.1 | +2.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.9 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -12.9 | -14.6 |
|  | [[EX229 (drug)]] 5 µM |  | -7.1 | -6.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.9 | -8.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.7 | -7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -6.3 | -5.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.5 | -5.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.7 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | cyclin G2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.1 — chr4:77,157,207-77,433,388 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cyclins |
| Hallmark sets | HYPOXIA, ADIPOGENESIS |
| Reactome | 2 pathways, smallest: FOXO-mediated transcription of cell cycle genes; FOXO-mediated transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16589](https://www.uniprot.org/uniprotkb/Q16589) (Cyclin-G2):

> May play a role in growth regulation and in negative regulation of cell cycle progression.

**Summary**, from NCBI Gene [901](https://www.ncbi.nlm.nih.gov/gene/901):

> The eukaryotic cell cycle is governed by cyclin-dependent protein kinases (CDKs) whose activities are regulated by cyclins and CDK inhibitors. The 8 species of cyclins reported in mammals, cyclins A through H, share a conserved amino acid sequence of about 90 residues called the cyclin box. The amino acid sequence of cyclin G is well conserved among mammals. The nucleotide sequence of cyclin G1 and cyclin G2 are 53% identical. Unlike cyclin G1, cyclin G2 contains a C-terminal PEST protein …

**Accessions** — [HGNC:1593](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1593) · Entrez [901](https://www.ncbi.nlm.nih.gov/gene/901) · UniProt [Q16589](https://www.uniprot.org/uniprotkb/Q16589) · Ensembl [ENSG00000138764](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138764)

## Data

Gene col 6230: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6230); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6230, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6230]; `tensor/DDL_lfc|DDL_z.npy` [6230]; `embed/gene_vectors.npy` [6230]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6230 or target_col == 6230). Every well: [[CCNG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
