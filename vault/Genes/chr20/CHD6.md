---
symbol: "CHD6"
type: "gene"
col: 4492
ensembl_id: "ENSG00000124177"
name: "chromodomain helicase DNA binding protein 6"
location: "20q12"
module: 46
arm: "+"
pooled_cpm: 166.91
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 22
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# CHD6

*chromodomain helicase DNA binding protein 6* — 20q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.53× (z +9.4, q 3e-18, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.521× (z -14.8, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLK2]] (+0.67, fdr 1e-05), [[CREB3L4]] (+0.64, fdr 1e-05), [[HFE]] (+0.62, fdr 2e-05); moves opposite to [[R3HDM4]] (-0.60, fdr 4e-05), [[MTG1]] (-0.53, fdr 4e-05), [[FAM118A]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4492.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.53×** | +9.4 | 3e-18 | 41/49 (HT-29, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +7.7 | 4e-12 | 29/49 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.03×** | +7.2 | 2e-10 | 41/48 (C32, SW1417, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.2 | 2e-05 | 27/48 (hTERT-HPNE, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +4.7 | 2e-04 | 24/48 (KATO III, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.5 | 5e-04 | 26/50 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.0 | 0.005 | 20/48 (J82, HEC-1-A, …) | top dose only | composition shift |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.13× | +3.8 | 0.012 | 12/48 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.7 | 0.012 | 20/48 (C32, HepG2/C3A, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.7 | 0.013 | 0/50 | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.031 | 21/49 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.22×** | +3.4 | 0.037 | 23/48 (PANC-1, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 1.11× | +3.3 | 0.043 | 10/48 (A549, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.19× | +3.3 | 0.045 | 20/50 (SW480, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.045 | 23/47 (HT-29, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.16× | +3.2 | 0.053 | 19/47 (HT-29, J82, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.053 | 10/48 (CFPAC-1, SW1417, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.10× | +3.1 | 0.063 | 14/48 (SW1417, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.20×** | +3.1 | 0.067 | 18/47 (SW48, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.14× | +2.9 | 0.090 | 10/48 (SW48, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4492.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.521×** | -14.8 | 0e+00 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.553×** | -13.5 | 9e-39 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.556×** | -12.8 | 2e-35 | 37/44 (NCI-H1792, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.516×** | -12.7 | 6e-35 | 43/49 (A-427, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.574×** | -12.6 | 3e-34 | 44/48 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.597×** | -10.8 | 2e-25 | 38/45 (A-427, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.627×** | -10.6 | 3e-24 | 43/48 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.653×** | -9.7 | 3e-20 | 38/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.701×** | -8.1 | 5e-14 | 31/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.708×** | -7.5 | 3e-12 | 37/47 (HepG2/C3A, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.724×** | -7.1 | 8e-11 | 30/47 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.556×** | -6.0 | 1e-07 | 40/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.796×** | -5.2 | 9e-06 | 27/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.601×** | -5.2 | 9e-06 | 33/48 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.812×** | -4.8 | 7e-05 | 26/48 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.749×** | -4.7 | 9e-05 | 35/49 (NCI-H1792, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.635×** | -4.6 | 1e-04 | 35/48 (SNU-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.760×** | -4.4 | 3e-04 | 29/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.646×** | -4.4 | 3e-04 | 36/48 (MIA PaCa-2, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.875× | -4.3 | 4e-04 | 16/49 (HT-29, H4, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.654×** | -4.3 | 4e-04 | 31/48 (MIA PaCa-2, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.770×** | -4.2 | 5e-04 | 28/48 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.848× | -3.8 | 0.004 | 18/48 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.873× | -3.1 | 0.042 | 12/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4492. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 182 | 0 | 16 (12 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.275× (z -19.8) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.368× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 187 | 1 | 12 (8 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.362× (z -13.7) |
| [[SW480 (line)]] | alt | 267 | 2 | 10 (7 ⚠) | [[PH-797804 (drug)]] 5 µM 3.00× (z +9.0) | [[Auranofin (drug)]] 5 µM 0.324× (z -20.7) |
| [[PANC-1 (line)]] | alt | 107 | 0 | 9 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.434× (z -13.8) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.510× (z -11.1) |
| [[SW1417 (line)]] | alt | 353 | 2 | 7 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 3.60× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.446× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.522× (z -11.1) |
| [[J82 (line)]] | alt | 258 | 2 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +14.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.49× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.497× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.549× (z -10.2) |
| [[SNU-1 (line)]] | wt | 222 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.497× (z -8.9) |
| [[C32 (line)]] | wt | 268 | 1 | 6 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 5.46× (z +10.5) | [[Auranofin (drug)]] 5 µM 0.349× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 188 | 3 (2 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.444× (z -12.0) |
| [[HOP62 (line)]] | alt | 120 | 1 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.426× (z -13.9) |
| [[Hs 766T (line)]] | wt | 214 | 0 | 7 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.342× (z -14.2) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.487× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 193 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -26.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.439× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 238 | 0 | 7 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.366× (z -14.6) |
| [[SW 900 (line)]] | alt | 189 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.426× (z -12.7) |
| [[HepG2_C3A (line)]] | wt | 236 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.418× (z -10.9) |
| [[A-172 (line)]] | wt | 160 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.403× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.459× (z -12.6) |
| [[A549 (line)]] | wt | 131 | 2 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.34× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.434× (z -11.8) |
| [[HT-29 (line)]] | alt | 156 | 2 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.62× (z +9.7) | [[Auranofin (drug)]] 5 µM 0.471× (z -10.7) |
| [[LoVo (line)]] | wt | 114 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 3.90× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.512× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 115 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.477× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.520× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 207 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.505× (z -9.5) |
| [[SNU-423 (line)]] | alt | 218 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.513× (z -9.4) |
| [[RKO (line)]] | wt | 151 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +10.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.340× (z -13.0) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 240 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.280× (z -17.0) |
| [[A-427 (line)]] | wt | 151 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.05× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -17.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 251 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.445× (z -10.8) |
| [[HS-578T (line)]] | alt | 132 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.492× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 135 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -13.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 163 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.16× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.534× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 125 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +11.5) | [[Auranofin (drug)]] 5 µM 0.406× (z -12.3) |
| [[Panc 03.27 (line)]] | alt | 162 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.484× (z -9.9) |
| [[SW48 (line)]] | wt | 131 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.278× (z -13.3) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.381× (z -10.0) |
| [[A498 (line)]] | wt | 72.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +14.6) | — |
| [[H4 (line)]] | wt | 136 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HCT15 (line)]] | alt | 191 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.370× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.398× (z -10.5) |
| [[KATO III (line)]] | alt | 135 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.23× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 143 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.352× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1573 (line)]] | alt | 93.8 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.452× (z -9.1) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SHP-77 (line)]] | alt | 185 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.472× (z -9.8) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 0.493× (z -9.2) |
| [[CHP-212 (line)]] | wt | 189 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.285× (z -10.0) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 222 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 94.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 115 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4492), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLK2]] | +0.67 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[CREB3L4]] | +0.64 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[HFE]] | +0.62 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ZNF362]] | +0.60 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[CDKN2C]] | +0.60 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[CILK1]] | +0.60 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[NCOA2]] | +0.59 | +0.42 / +0.47 | both halves | 4e-05 | pathway: Cellular response to chemical stress |
| [[FRS2]] | +0.59 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[PRPF40A]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[RPRD2]] | +0.57 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[WDFY3]] | +0.56 | +0.27 / +0.50 | both halves | 3e-04 |  |
| [[JADE2]] | +0.56 | +0.44 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[R3HDM4]] | -0.60 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[MTG1]] | -0.53 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[FAM118A]] | -0.53 | -0.41 / -0.31 | both halves | 2e-04 |  |
| [[TMEM241]] | -0.52 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[SLC25A32]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[TPCN2]] | -0.52 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[ST6GALNAC4]] | -0.52 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[EPN2]] | -0.51 | -0.51 / -0.24 | both halves | 4e-04 |  |
| [[TXNL4A]] | -0.51 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[TMEM104]] | -0.50 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[TRABD]] | -0.50 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[PPP1R12C]] | -0.50 | -0.36 / -0.38 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CHD6's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.597). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.8, 14.8); signed map (27.4, -22.4). **Vector** length 127, 44.0% of its response variance represented; |z| ≥ 3 in 1,366 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.9 | +7.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +10.3 | +9.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +8.1 | +7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +5.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.9 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +3.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.4 | +2.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -9.4 | -14.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -8.6 | -13.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -7.4 | -9.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.4 | -10.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.3 | -12.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.2 | -6.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.5 | -4.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.4 | -4.2 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | chromodomain helicase DNA binding protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q12 — chr20:41,402,083-41,618,384 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1335, FLJ22369, dJ620E11.1, CHD5, RIGB |
| Gene groups (HGNC) | Myb/SANT domain containing; SNF2 related family |
| Reactome | 10 pathways, smallest: NFE2L2 regulating anti-oxidant/detoxification enzymes; CHD6, CHD7, CHD8, CHD9 subfamily; Nuclear events mediated by NFE2L2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TD26](https://www.uniprot.org/uniprotkb/Q8TD26) (ATP-dependent chromatin remodeler CHD6):

> ATP-dependent chromatin-remodeling factor. Regulates transcription by disrupting nucleosomes in a largely non-sliding manner which strongly increases the accessibility of chromatin; nucleosome disruption requires ATP. Activates transcription of specific genes in response to oxidative stress through interaction with NFE2L2.; (Microbial infection) Acts as a transcriptional repressor of different viruses including influenza virus or papillomavirus. During influenza virus infection, the viral …

**Summary**, from NCBI Gene [84181](https://www.ncbi.nlm.nih.gov/gene/84181):

> This gene encodes a member of the SNF2/RAD54 helicase protein family. The encoded protein contains two chromodomains, a helicase domain, and an ATPase domain. Several multi-subunit protein complexes remodel chromatin to allow patterns of cell type-specific gene expression, and the encoded protein is thought to be a core member of one or more of these chromatin remodeling complexes. The encoded protein may function as a transcriptional repressor and is involved in the cellular repression of …

**Accessions** — [HGNC:19057](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19057) · Entrez [84181](https://www.ncbi.nlm.nih.gov/gene/84181) · UniProt [Q8TD26](https://www.uniprot.org/uniprotkb/Q8TD26) · Ensembl [ENSG00000124177](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124177)

## Data

Gene col 4492: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4492); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4492, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4492]; `tensor/DDL_lfc|DDL_z.npy` [4492]; `embed/gene_vectors.npy` [4492]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4492 or target_col == 4492). Every well: [[CHD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
