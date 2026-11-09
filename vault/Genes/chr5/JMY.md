---
symbol: "JMY"
type: "gene"
col: 7623
ensembl_id: "ENSG00000152409"
name: "junction mediating and regulatory protein, p53 cofactor"
location: "5q14.1"
module: 69
arm: "+"
pooled_cpm: 89.73
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 39
n_dd_up_clean: 10
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# JMY

*junction mediating and regulatory protein, p53 cofactor* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.52× (z +9.3, q 1e-17, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (12 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.220× (z -24.4, q 0e+00, down in 47 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.193× (z -13.9, q 2e-41, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCP11L2]] (+0.79, fdr 7e-06), [[KLHL24]] (+0.76, fdr 1e-05), [[CREBRF]] (+0.73, fdr 1e-05); moves opposite to [[INTS7]] (-0.58, fdr 1e-05), [[IPO9]] (-0.56, fdr 1e-05), [[RNGTT]] (-0.52, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GABARAPL1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7623.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +9.3 | 1e-17 | 34/48 (COLO 205, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +6.7 | 6e-09 | 29/47 (COLO 205, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.27×** | +5.3 | 2e-05 | 26/47 (SNU-1, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +4.9 | 1e-04 | 25/47 (C32, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.34×** | +4.8 | 2e-04 | 32/47 (SW480, LOX-IMVI, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.73×** | +4.7 | 3e-04 | 27/48 (SNU-423, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.4 | 0.001 | 23/46 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.30×** | +4.3 | 0.001 | 28/49 (SW480, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.002 | 24/48 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.004 | 23/47 (LOX-IMVI, A-427, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.016 | 20/47 (SNU-1, SW48, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.18× | +3.6 | 0.016 | 19/47 (HT-29, A-172, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.023 | 19/47 (SW480, SNU-1, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.045 | 20/46 (SNU-1, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7623.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.220×** | -24.4 | 0e+00 | 47/47 (NCI-H2347, HT-29, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.193×** | -13.9 | 2e-41 | 47/47 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.220×** | -12.8 | 4e-35 | 46/47 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.230×** | -12.4 | 5e-33 | 46/47 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.471×** | -12.1 | 9e-32 | 39/48 (A-427, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.241×** | -12.0 | 3e-31 | 46/47 (HT-29, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.467×** | -11.8 | 4e-30 | 36/43 (SW48, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Belzutifan (drug)]] 5 µM |  | **0.273×** | -10.9 | 5e-26 | 44/45 (NCI-H2347, A498, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.296×** | -10.2 | 7e-23 | 44/47 (NCI-H2347, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.551×** | -9.1 | 8e-18 | 44/47 (SW 900, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.599×** | -7.9 | 1e-13 | 38/46 (SW480, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.616×** | -7.2 | 3e-11 | 28/44 (AN3 CA, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.448×** | -7.1 | 4e-11 | 43/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.670×** | -6.1 | 5e-08 | 35/47 (SW48, SW480, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.488×** | -6.0 | 6e-08 | 27/38 (Panc 03.27, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.699×** | -5.8 | 3e-07 | 33/48 (HT-29, NCI-H1573, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.556×** | -5.2 | 6e-06 | 39/48 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.739×** | -4.9 | 3e-05 | 35/48 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.583×** | -4.8 | 4e-05 | 37/47 (LOX-IMVI, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.757×** | -4.5 | 2e-04 | 31/47 (NCI-H1573, HT-29, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.763×** | -4.3 | 3e-04 | 33/47 (HT-29, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7623. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 171 | 1 | 12 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.150× (z -23.7) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.114× (z -14.2) |
| [[HT-29 (line)]] | alt | 207 | 0 | 11 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0907× (z -23.4) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.0963× (z -11.9) |
| [[SW480 (line)]] | alt | 79.9 | 2 (1 ⚠) | 8 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.07× (z +9.2) ⚠ toxic · without an alert: [[5-Azacytidine (drug)]] 5 µM 1.91× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.244× (z -18.5) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.178× (z -11.8) |
| [[A498 (line)]] | wt | 99.1 | 0 | 9 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.193× (z -17.2) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.123× (z -11.4) |
| [[SW1417 (line)]] | alt | 106 | 1 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.177× (z -18.9) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.177× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 88.8 | 0 | 7 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.153× (z -21.1) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.131× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 57.1 | 2 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.228× (z -14.9) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.383× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 87.0 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.233× (z -15.3) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0909× (z -13.2) |
| [[SNU-1 (line)]] | wt | 136 | 2 (1 ⚠) | 4 (3 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.15× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.116× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[EX229 (drug)]] 5 µM 0.139× (z -9.2) |
| [[A-427 (line)]] | wt | 75.9 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[venetoclax (drug)]] 5 µM 0.196× (z -9.1) |
| [[SW48 (line)]] | wt | 155 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0491× (z -23.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[EX229 (drug)]] 0.05 µM 0.268× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 47.1 | 0 | 4 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.263× (z -11.8) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.302× (z -10.0) |
| [[COLO 205 (line)]] | alt | 90.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[HS-578T (line)]] | alt | 68.7 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.262× (z -13.0) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.154× (z -9.5) |
| [[LoVo (line)]] | wt | 214 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-733 (drug)]] 5 µM 0.147× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 103 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.209× (z -15.9) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.169× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 68.1 | 0 | 4 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.168× (z -16.4) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.130× (z -9.8) |
| [[PANC-1 (line)]] | alt | 62.8 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.223× (z -14.4) ⚠ unreliable plate only · without an alert: [[Belzutifan (drug)]] 5 µM 0.167× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 73.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Abemaciclib (drug)]] 5 µM 0.155× (z -8.8) |
| [[SNU-423 (line)]] | alt | 91.0 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.220× (z -14.3) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.147× (z -9.5) |
| [[SW 900 (line)]] | alt | 102 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.251× (z -12.6) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.296× (z -10.5) |
| [[A549 (line)]] | wt | 59.3 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.189× (z -16.1) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.173× (z -8.9) |
| [[C32 (line)]] | wt | 68.2 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 6.35× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.222× (z -14.1) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 99.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.123× (z -15.9) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 82.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +11.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.346× (z -9.7) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 70.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.170× (z -12.8) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 126 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.177× (z -11.0) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.0786× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 65.4 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.146× (z -17.3) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.113× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[HOP62 (line)]] | alt | 53.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +9.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.164× (z -12.9) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 81.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[LS 180 (line)]] | wt | 120 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.256× (z -9.4) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 101 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.183× (z -15.8) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.172× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 97.3 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.174× (z -13.7) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 69.5 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.223× (z -14.8) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.170× (z -9.1) |
| [[SHP-77 (line)]] | alt | 87.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SW 1271 (line)]] | alt | 123 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0576× (z -14.4) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 97.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0989× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[BT-474 (line)]] | alt | 85.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.226× (z -11.6) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.270× (z -11.2) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 65.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.225× (z -12.4) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.216× (z -9.3) ⚠ unreliable plate only |
| [[NCI-H661 (line)]] | alt | 53.4 | 0 | 1 | — | [[EX229 (drug)]] 0.05 µM 0.0639× (z -9.6) |
| [[RKO (line)]] | wt | 81.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.186× (z -14.0) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 72.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.223× (z -11.3) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 7.02 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7623), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCP11L2]] | +0.79 | +0.60 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[KLHL24]] | +0.76 | +0.57 / +0.83 | both halves | 1e-05 |  |
| [[CREBRF]] | +0.73 | +0.55 / +0.80 | both halves | 1e-05 |  |
| [[RB1CC1]] | +0.72 | +0.46 / +0.80 | both halves | 2e-05 | **novel candidate** |
| [[UBN2]] | +0.71 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[UBXN7]] | +0.70 | +0.47 / +0.77 | both halves | 2e-05 |  |
| [[HBP1]] | +0.69 | +0.45 / +0.74 | both halves | 3e-05 |  |
| [[TBC1D15]] | +0.67 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[DNAJB9]] | +0.66 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[WDR48]] | +0.65 | +0.46 / +0.74 | both halves | 3e-05 |  |
| [[PIK3CA]] | +0.65 | +0.46 / +0.70 | both halves | 2e-05 |  |
| [[MKRN1]] | +0.65 | +0.45 / +0.73 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS7]] | -0.58 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[IPO9]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[RNGTT]] | -0.52 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[TAF1B]] | -0.52 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[HARS1]] | -0.52 | -0.47 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABARAPL1]] | C | GABARAPL1 activity raises JMY's level | lines that do not express GABARAPL1 (3) vs lines expressing it (47) | 2.68× lower at baseline in the lines without GABARAPL1 | 0.021 | ⚠ few lines (3 vs 47); across organs; also absent: GPR137B, ERO1B, TEX14; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.797). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.5, -44.8); signed map (-14.1, 9.7). **Vector** length 149, 52.3% of its response variance represented; |z| ≥ 3 in 1,575 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +9.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.0 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.9 | +4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +1.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.9 | +3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.8 | +2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.6 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -17.8 | -24.4 |
|  | [[EX229 (drug)]] 5 µM |  | -12.8 | -12.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -12.1 | -13.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -10.7 | -12.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -10.7 | -12.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -9.7 | -7.1 |

## What is on record

|  |  |
|---|---|
| Name | junction mediating and regulatory protein, p53 cofactor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:79,236,131-79,327,211 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37870, WHAMM2 |
| Gene groups (HGNC) | Wiskott-Aldrich Syndrome protein family |
| Reactome | 3 pathways, smallest: Regulation of TP53 Activity through Methylation; Regulation of TP53 Activity; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N9B5](https://www.uniprot.org/uniprotkb/Q8N9B5) (Junction-mediating and -regulatory protein):

> Acts both as a nuclear p53/TP53-cofactor and a cytoplasmic regulator of actin dynamics depending on conditions. In nucleus, acts as a cofactor that increases p53/TP53 response via its interaction with p300/EP300. Increases p53/TP53-dependent transcription and apoptosis, suggesting an important role in p53/TP53 stress response such as DNA damage. In cytoplasm, acts as a nucleation-promoting factor for both branched and unbranched actin filaments. Activates the Arp2/3 complex to induce branched …

**Summary**, from NCBI Gene [133746](https://www.ncbi.nlm.nih.gov/gene/133746):

> Enables microtubule binding activity. Involved in cellular response to starvation. Located in autophagosome membrane; cell leading edge; and cytoplasmic vesicle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28916](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28916) · Entrez [133746](https://www.ncbi.nlm.nih.gov/gene/133746) · UniProt [Q8N9B5](https://www.uniprot.org/uniprotkb/Q8N9B5) · Ensembl [ENSG00000152409](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152409)

## Data

Gene col 7623: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7623); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7623, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7623]; `tensor/DDL_lfc|DDL_z.npy` [7623]; `embed/gene_vectors.npy` [7623]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7623 or target_col == 7623). Every well: [[JMY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JMY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
