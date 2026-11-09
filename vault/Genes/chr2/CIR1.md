---
symbol: "CIR1"
type: "gene"
col: 6174
ensembl_id: "ENSG00000138433"
name: "corepressor of RBPJ and splicing regulator"
location: "2q31.1"
module: 74
arm: "+"
pooled_cpm: 119.65
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# CIR1

*corepressor of RBPJ and splicing regulator* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.79× (z +9.7, q 8e-20, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.350× (z -17.6, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.433× (z -7.3, q 3e-11, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM23]] (+0.87, fdr 7e-06), [[SYF2]] (+0.86, fdr 7e-06), [[EAPP]] (+0.83, fdr 7e-06); moves opposite to [[UBE2G2]] (-0.72, fdr 7e-06), [[NUP188]] (-0.71, fdr 7e-06), [[TTL]] (-0.67, fdr 7e-06).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6174.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +9.7 | 8e-20 | 42/48 (NCI-H1573, A549, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.03×** | +9.7 | 8e-20 | 45/49 (LoVo, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.33×** | +6.8 | 2e-09 | 27/48 (A549, NCI-H23, …) | two highest doses | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.98×** | +6.0 | 3e-07 | 37/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.64×** | +4.3 | 0.002 | 34/47 (AsPC-1, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.50×** | +4.0 | 0.007 | 35/48 (A498, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.28×** | +3.9 | 0.007 | 24/48 (NCI-H2030, BT-474, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.013 | 28/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.033 | 22/48 (A-172, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6174.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.350×** | -17.6 | 0e+00 | 48/48 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.409×** | -14.4 | 1e-44 | 42/44 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.509×** | -11.3 | 2e-27 | 44/49 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.584×** | -8.3 | 1e-14 | 37/45 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.433×** | -7.3 | 3e-11 | 45/48 (AsPC-1, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.459×** | -6.8 | 8e-10 | 43/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.488×** | -6.3 | 3e-08 | 46/48 (CFPAC-1, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.504×** | -6.0 | 1e-07 | 38/48 (NCI-H1792, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.511×** | -5.9 | 3e-07 | 41/48 (SW 1271, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.747×** | -4.7 | 1e-04 | 29/47 (SNU-423, AsPC-1, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **0.748×** | -4.7 | 2e-04 | 30/47 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.642×** | -4.3 | 7e-04 | 32/48 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.854× | -3.7 | 0.009 | 21/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.804×** | -3.7 | 0.010 | 27/48 (AsPC-1, NCI-H460, …) | two highest doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.779×** | -3.4 | 0.025 | 24/48 (AsPC-1, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.820×** | -3.3 | 0.029 | 25/48 (LS 180, HEC-1-A, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.834× | -3.0 | 0.068 | 20/49 (SW 900, LS 180, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.715×** | -2.9 | 0.084 | 20/47 (AsPC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.741×** | -2.9 | 0.084 | 19/48 (SK-MEL-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Volasertib (drug)]] 0.5 µM |  | **0.741×** | -2.9 | 0.084 | 16/48 (NCI-H460, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6174. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 145 | 0 | 6 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.208× (z -18.1) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 175 | 0 | 6 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.227× (z -18.6) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.272× (z -8.5) |
| [[A498 (line)]] | wt | 173 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -13.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 121 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +12.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.51× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.293× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 127 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -18.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 104 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.70× (z +8.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.287× (z -16.2) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 130 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.432× (z -9.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 115 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.46× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.152× (z -20.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 90.9 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.88× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.298× (z -13.2) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 127 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -10.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 190 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.372× (z -11.5) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.239× (z -8.7) |
| [[SW 900 (line)]] | alt | 163 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -16.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 144 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.71× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -9.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 167 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -12.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 96.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.64× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.289× (z -13.7) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 107 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.386× (z -10.9) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 137 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 126 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.214× (z -17.7) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 124 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 107 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.24× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.403× (z -9.5) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 91.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.96× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.334× (z -13.8) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 138 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.78× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -14.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 148 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -10.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 166 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.274× (z -17.3) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 68.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -11.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 118 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.250× (z -16.2) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 83.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.54× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.332× (z -10.1) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 108 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.61× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -9.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 148 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.292× (z -13.2) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 85.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.31× (z +10.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.347× (z -9.0) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 169 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.191× (z -10.1) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.0482× (z -9.7) |
| [[SW48 (line)]] | wt | 90.6 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.191× (z -12.3) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 128 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.55× (z +8.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.357× (z -13.8) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 74.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.327× (z -8.8) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 94.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -9.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -9.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.218× (z -13.7) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -12.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.201× (z -16.5) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 72.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.399× (z -10.0) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 131 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.307× (z -10.5) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 122 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 106 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 170 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6174), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM23]] | +0.87 | +0.84 / +0.85 | both halves | 7e-06 |  |
| [[SYF2]] | +0.86 | +0.82 / +0.87 | both halves | 7e-06 | STRING 626 |
| [[EAPP]] | +0.83 | +0.76 / +0.87 | both halves | 7e-06 |  |
| [[FRG1]] | +0.79 | +0.67 / +0.80 | both halves | 7e-06 | STRING 901 |
| [[MPHOSPH8]] | +0.77 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[PPIL4]] | +0.77 | +0.81 / +0.70 | both halves | 7e-06 |  |
| [[AKAP9]] | +0.76 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.75 | +0.67 / +0.80 | both halves | 7e-06 |  |
| [[SLU7]] | +0.75 | +0.68 / +0.80 | both halves | 7e-06 | STRING 547 |
| [[CWC15]] | +0.75 | +0.74 / +0.74 | both halves | 7e-06 | STRING 861 |
| [[IK]] | +0.73 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[ASB8]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2G2]] | -0.72 | -0.67 / -0.74 | both halves | 7e-06 |  |
| [[NUP188]] | -0.71 | -0.62 / -0.71 | both halves | 7e-06 |  |
| [[TTL]] | -0.67 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[TFDP1]] | -0.67 | -0.70 / -0.63 | both halves | 7e-06 |  |
| [[VMA21]] | -0.66 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[PSME3]] | -0.65 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[MACROH2A1]] | -0.65 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[SIGMAR1]] | -0.65 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[WDR77]] | -0.65 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[CTPS1]] | -0.63 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[ARHGAP4]] | -0.63 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[EFTUD2]] | -0.63 | -0.52 / -0.66 | both halves | 1e-05 | STRING 800 |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.848). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.3, -45.8); signed map (-13.1, 5.9). **Vector** length 163, 59.3% of its response variance represented; |z| ≥ 3 in 1,092 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +9.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.9 | +9.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +5.9 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +5.7 | +6.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +6.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.5 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +1.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +4.2 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -17.5 | -17.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -8.8 | -6.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -8.6 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -8.6 | -6.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.4 | -7.3 |
|  | [[EX229 (drug)]] 5 µM |  | -8.2 | -6.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.0 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | corepressor of RBPJ and splicing regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:174,348,022-174,395,712 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CIR; previously CIR1 |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86X95](https://www.uniprot.org/uniprotkb/Q86X95) (Corepressor of RBPJ and splicing regulator):

> May modulate splice site selection during alternative splicing of pre-mRNAs (By similarity). Regulates transcription and acts as corepressor for RBPJ. Recruits RBPJ to the Sin3-histone deacetylase complex (HDAC). Required for RBPJ-mediated repression of transcription.

**Summary**, from NCBI Gene [9541](https://www.ncbi.nlm.nih.gov/gene/9541):

> Enables histone deacetylase binding activity; protein kinase binding activity; and transcription corepressor activity. Acts upstream of or within negative regulation of transcription by RNA polymerase II. Located in centrosome and nuclear speck. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24217](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24217) · Entrez [9541](https://www.ncbi.nlm.nih.gov/gene/9541) · UniProt [Q86X95](https://www.uniprot.org/uniprotkb/Q86X95) · Ensembl [ENSG00000138433](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138433)

## Data

Gene col 6174: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6174); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6174, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6174]; `tensor/DDL_lfc|DDL_z.npy` [6174]; `embed/gene_vectors.npy` [6174]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6174 or target_col == 6174). Every well: [[CIR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CIR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
