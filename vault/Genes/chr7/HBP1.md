---
symbol: "HBP1"
type: "gene"
col: 2678
ensembl_id: "ENSG00000105856"
name: "HMG-box transcription factor 1"
location: "7q22.3"
module: 69
arm: "+"
pooled_cpm: 135.35
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 35
n_dd_up_clean: 11
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# HBP1

*HMG-box transcription factor 1* — 7q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 3.24× (z +13.0, q 4e-36, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.162× (z -20.1, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.181× (z -9.9, q 6e-21, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CREBRF]] (+0.82, fdr 8e-06), [[KLHL24]] (+0.79, fdr 7e-06), [[ATOSA]] (+0.77, fdr 1e-05); moves opposite to [[PDSS1]] (-0.61, fdr 1e-05), [[AGK]] (-0.61, fdr 1e-05), [[EIF2B3]] (-0.61, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NR4A2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2678.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.24×** | +13.0 | 4e-36 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +10.1 | 2e-21 | 42/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.18×** | +8.7 | 9e-16 | 42/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.10×** | +8.2 | 4e-14 | 44/48 (LOX-IMVI, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.85×** | +6.8 | 1e-09 | 36/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +6.2 | 5e-08 | 33/48 (A498, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.73×** | +5.8 | 5e-07 | 43/49 (HT-29, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +5.5 | 2e-06 | 37/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.58×** | +5.1 | 2e-05 | 32/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.06×** | +4.2 | 0.002 | 34/49 (A-427, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.87×** | +3.6 | 0.014 | 37/49 (NCI-H23, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.78×** | +3.4 | 0.038 | 32/48 (MIA PaCa-2, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.51×** | +3.2 | 0.070 | 30/48 (NCI-H460, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.094 | 23/48 (HT-29, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2678.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.162×** | -20.1 | 0e+00 | 48/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.293×** | -13.1 | 1e-36 | 44/44 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.318×** | -12.7 | 1e-34 | 48/49 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.181×** | -9.9 | 6e-21 | 48/48 (RPMI-7951, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.421×** | -9.6 | 1e-19 | 46/48 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.430×** | -9.3 | 9e-19 | 47/48 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.200×** | -9.3 | 9e-19 | 48/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.444×** | -9.0 | 2e-17 | 46/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.215×** | -8.9 | 4e-17 | 48/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.217×** | -8.8 | 5e-17 | 48/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.237×** | -8.3 | 4e-15 | 47/48 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.446×** | -8.3 | 6e-15 | 41/45 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.649×** | -6.8 | 6e-10 | 44/48 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.592×** | -5.8 | 3e-07 | 42/48 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.615×** | -5.4 | 3e-06 | 42/48 (CFPAC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[EX229 (drug)]] 0.5 µM |  | **0.537×** | -4.8 | 7e-05 | 44/49 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.472×** | -4.3 | 5e-04 | 37/47 (hTERT-HPNE, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.681×** | -4.0 | 0.002 | 36/48 (SW48, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.607×** | -3.8 | 0.004 | 35/48 (NCI-H23, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.635×** | -3.5 | 0.015 | 36/48 (NCI-H23, SNU-423, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.740×** | -3.3 | 0.023 | 32/48 (SW480, SW 1088, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.745×** | -3.3 | 0.030 | 30/48 (LoVo, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.56 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2678. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 126 | 9 (2 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 10.5× (z +20.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0744× (z -22.2) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.102× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 168 | 0 | 13 (8 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.128× (z -21.4) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.170× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 189 | 3 (1 ⚠) | 9 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.10× (z +12.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.124× (z -18.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.103× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 175 | 1 | 11 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +10.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.131× (z -21.9) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.132× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 196 | 2 (1 ⚠) | 9 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.30× (z +12.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.121× (z -17.5) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0868× (z -10.6) |
| [[SW 900 (line)]] | alt | 181 | 3 (1 ⚠) | 8 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.58× (z +11.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.144× (z -15.2) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.109× (z -9.1) |
| [[A549 (line)]] | wt | 137 | 1 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.122× (z -19.1) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.105× (z -10.7) |
| [[BT-474 (line)]] | alt | 118 | 7 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.29× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-733 (drug)]] 5 µM 0.153× (z -8.6) |
| [[SNU-423 (line)]] | alt | 192 | 1 | 9 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-733 (drug)]] 5 µM 0.153× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 149 | 0 | 8 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0617× (z -23.7) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.0620× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 158 | 1 | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +9.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.115× (z -19.6) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0996× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 230 | 2 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.32× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.185× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 139 | 4 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.83× (z +15.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.205× (z -11.9) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.116× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 99.1 | 2 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.94× (z +12.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.108× (z -20.5) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.160× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 163 | 1 | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.186× (z -13.8) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 171 | 2 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0911× (z -17.8) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.109× (z -8.6) |
| [[C-33 A (line)]] | alt | 67.5 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.34× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HT-29 (line)]] | alt | 130 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.71× (z +10.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.223× (z -12.2) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 110 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +9.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.254× (z -11.5) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 75.1 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.45× (z +18.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.223× (z -12.8) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 143 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.179× (z -13.6) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0590× (z -11.7) |
| [[SW480 (line)]] | alt | 94.9 | 2 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +10.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.151× (z -17.5) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.156× (z -9.0) |
| [[A498 (line)]] | wt | 186 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +14.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.123× (z -14.9) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0834× (z -9.2) |
| [[C32 (line)]] | wt | 269 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.117× (z -17.7) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.121× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 91.7 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +9.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.238× (z -10.3) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.0860× (z -9.2) |
| [[Hs 766T (line)]] | wt | 147 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.162× (z -15.4) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 110 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.53× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H661 (line)]] | alt | 153 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.150× (z -10.2) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.0430× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 137 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 114 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +11.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.248× (z -10.9) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 197 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.169× (z -11.0) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 139 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -9.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LoVo (line)]] | wt | 112 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.86× (z +10.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.168× (z -14.1) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 110 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.36× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.123× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[RKO (line)]] | wt | 81.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +8.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.116× (z -13.5) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 94.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.75× (z +10.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0848× (z -14.6) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 108 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.259× (z -11.8) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 127 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.126× (z -13.1) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.0602× (z -9.3) |
| [[HCT15 (line)]] | alt | 161 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HOP62 (line)]] | alt | 124 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.30× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.180× (z -11.8) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 130 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.162× (z -15.3) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 143 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.239× (z -12.1) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 99.7 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.103× (z -14.6) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 139 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0727× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[CHP-212 (line)]] | wt | 135 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.160× (z -10.2) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 82.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.110× (z -15.0) ⚠ unreliable plate only |
| [[NCI-H596 (line)]] | alt | 150 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.0674× (z -10.6) |
| [[SHP-77 (line)]] | alt | 56.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.167× (z -12.0) ⚠ unreliable plate only |
| [[NCI-H2122 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 192 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2678), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CREBRF]] | +0.82 | +0.57 / +0.86 | both halves | 8e-06 |  |
| [[KLHL24]] | +0.79 | +0.66 / +0.79 | both halves | 7e-06 |  |
| [[ATOSA]] | +0.77 | +0.54 / +0.78 | both halves | 1e-05 |  |
| [[YPEL5]] | +0.76 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[UBXN7]] | +0.75 | +0.64 / +0.79 | both halves | 7e-06 |  |
| [[TBC1D15]] | +0.73 | +0.55 / +0.77 | both halves | 1e-05 |  |
| [[TCP11L2]] | +0.73 | +0.60 / +0.79 | both halves | 7e-06 |  |
| [[PIK3CA]] | +0.72 | +0.58 / +0.76 | both halves | 7e-06 |  |
| [[KDM6A]] | +0.71 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[TMEM59]] | +0.71 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[JMY]] | +0.69 | +0.45 / +0.74 | both halves | 3e-05 |  |
| [[PCMTD1]] | +0.69 | +0.61 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDSS1]] | -0.61 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[AGK]] | -0.61 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[EIF2B3]] | -0.61 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[PINX1]] | -0.58 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[MPHOSPH6]] | -0.57 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[LYAR]] | -0.56 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[EEFSEC]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[PDCD11]] | -0.55 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[SNRPD1]] | -0.55 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[ACSF3]] | -0.55 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[FARSB]] | -0.53 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[RRP1B]] | -0.53 | -0.41 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR4A2]] | B | NR4A2 activity raises HBP1's level | lines that do not express NR4A2 (7) vs lines expressing it (43) | 1.43× lower at baseline in the lines without NR4A2 | 0.0997 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.877). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.5, -44.4); signed map (-14.1, 9.9). **Vector** length 125, 57.2% of its response variance represented; |z| ≥ 3 in 1,670 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +10.9 | +2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.5 | +0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | -0.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +4.7 | -12.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +4.3 | +0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | -1.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +3.2 | +1.5 |
|  | [[IQ 1 (drug)]] 5 µM |  | +3.0 | +0.6 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +3.0 | +2.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -20.9 | -20.1 |
|  | [[EX229 (drug)]] 5 µM |  | -13.3 | -9.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -12.4 | -9.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -11.3 | -8.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -11.3 | -8.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -10.2 | -8.8 |

## What is on record

|  |  |
|---|---|
| Name | HMG-box transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.3 — chr7:107,168,961-107,202,522 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [O60381](https://www.uniprot.org/uniprotkb/O60381) (HMG box-containing protein 1):

> Transcriptional repressor that binds to the promoter region of target genes. Plays a role in the regulation of the cell cycle and of the Wnt pathway. Binds preferentially to the sequence 5'-TTCATTCATTCA-3'. Binding to the histone H1.0 promoter is enhanced by interaction with RB1. Disrupts the interaction between DNA and TCF4.

**Summary**, from NCBI Gene [26959](https://www.ncbi.nlm.nih.gov/gene/26959):

> Predicted to enable DNA-binding transcription repressor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in negative regulation of lipid transport; negative regulation of reactive oxygen species biosynthetic process; and negative regulation of transcription by RNA polymerase II. Located in nuclear speck. Biomarker of osteoarthritis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23200](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23200) · Entrez [26959](https://www.ncbi.nlm.nih.gov/gene/26959) · UniProt [O60381](https://www.uniprot.org/uniprotkb/O60381) · Ensembl [ENSG00000105856](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105856)

## Data

Gene col 2678: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2678); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2678, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2678]; `tensor/DDL_lfc|DDL_z.npy` [2678]; `embed/gene_vectors.npy` [2678]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2678 or target_col == 2678). Every well: [[HBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
