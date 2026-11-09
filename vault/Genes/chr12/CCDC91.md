---
symbol: "CCDC91"
type: "gene"
col: 4402
ensembl_id: "ENSG00000123106"
name: "coiled-coil domain containing 91"
location: "12p11.22"
module: 74
arm: "+"
pooled_cpm: 202.9
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 31
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# CCDC91

*coiled-coil domain containing 91* — 12p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 0.05 µM: 1.33× (z +5.1, q 2e-04, up in 36 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.407× (z -23.9, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMARCC1]] (+0.54, fdr 2e-04), [[CHMP1B]] (+0.52, fdr 2e-04), [[ZBTB20]] (+0.51, fdr 4e-04); moves opposite to [[EED]] (-0.59, fdr 1e-05), [[INTS6L]] (-0.59, fdr 1e-05), [[POLH]] (-0.52, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4402.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | **1.33×** | +5.1 | 2e-04 | 36/45 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +4.5 | 0.002 | 29/45 (A-172, SW480, …) | rises with dose |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.23×** | +3.9 | 0.014 | 28/46 (NCI-H1573, J82, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.16× | +3.9 | 0.014 | 10/46 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.22×** | +3.8 | 0.020 | 25/47 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +3.3 | 0.070 | 19/46 (SW 900, CFPAC-1, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.21×** | +3.3 | 0.070 | 18/46 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.078 | 19/46 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +3.2 | 0.082 | 19/46 (NCI-H2347, RPMI-7951, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.084 | 24/46 (LS 180, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.1 | 0.085 | 21/46 (NCI-H1573, BT-474, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.18× | +3.0 | 0.11 | 17/45 (RPMI-7951, hTERT-HPNE, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4402.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.407×** | -23.9 | 0e+00 | 47/47 (SNU-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.398×** | -17.3 | 0e+00 | 46/46 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.459×** | -14.1 | 9e-43 | 41/46 (C32, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.511×** | -12.6 | 2e-34 | 42/46 (PANC-1, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.507×** | -12.3 | 1e-32 | 40/48 (NCI-H23, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.514×** | -12.0 | 2e-31 | 43/45 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.574×** | -10.4 | 1e-23 | 37/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.393×** | -9.2 | 3e-18 | 46/46 (HEC-1-A, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.509×** | -9.0 | 9e-18 | 45/46 (NCI-H23, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.437×** | -8.1 | 2e-14 | 45/46 (HEC-1-A, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.452×** | -7.8 | 3e-13 | 40/46 (HEC-1-A, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.660×** | -7.4 | 8e-12 | 44/46 (LoVo, NCI-H23, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.488×** | -7.0 | 8e-11 | 41/46 (HEC-1-A, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.501×** | -6.8 | 5e-10 | 42/46 (HEC-1-A, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.697×** | -6.3 | 1e-08 | 26/43 (A-427, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[EX229 (drug)]] 0.5 µM |  | **0.654×** | -5.7 | 4e-07 | 42/47 (NCI-H23, A498, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.679×** | -5.2 | 6e-06 | 38/46 (NCI-H23, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.629×** | -4.5 | 1e-04 | 33/45 (AsPC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.819×** | -3.7 | 0.004 | 24/46 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 5 µM |  | 0.878× | -3.4 | 0.012 | 8/47 (hTERT-HPNE, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4402. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 301 | 0 | 16 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -27.4) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -23.5) |
| [[NCI-H23 (line)]] | alt | 413 | 0 | 15 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -22.8) |
| [[C32 (line)]] | wt | 306 | 0 | 12 (9 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -21.8) |
| [[MIA PaCa-2 (line)]] | alt | 321 | 0 | 12 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.114× (z -29.2) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -19.8) |
| [[NCI-H460 (line)]] | wt | 129 | 0 | 12 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -18.6) |
| [[A498 (line)]] | wt | 168 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -20.3) |
| [[HEC-1-A (line)]] | alt | 198 | 0 | 10 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.338× (z -17.7) ⚠ unreliable plate only · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -17.5) |
| [[LoVo (line)]] | wt | 286 | 0 | 10 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -20.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -16.3) |
| [[SK-MEL-2 (line)]] | alt | 344 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -16.3) |
| [[HT-29 (line)]] | alt | 277 | 0 | 8 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.283× (z -17.3) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -15.2) |
| [[SW480 (line)]] | alt | 185 | 0 | 8 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.310× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -10.6) |
| [[C-33 A (line)]] | alt | 167 | 0 | 7 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -12.7) |
| [[HOP62 (line)]] | alt | 369 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -19.3) |
| [[A-427 (line)]] | wt | 198 | 1 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.77× (z +8.6) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.0492× (z -43.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 151 | 0 | 6 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.207× (z -19.3) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -18.9) |
| [[LOX-IMVI (line)]] | wt | 310 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -28.3) |
| [[LS 180 (line)]] | wt | 175 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -19.2) |
| [[NCI-H2030 (line)]] | alt | 193 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -18.1) |
| [[RKO (line)]] | wt | 266 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -20.7) |
| [[J82 (line)]] | alt | 203 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -17.0) |
| [[NCI-H1573 (line)]] | alt | 233 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.317× (z -15.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -15.8) |
| [[NCI-H1792 (line)]] | alt | 251 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -15.6) |
| [[NCI-H2347 (line)]] | alt | 128 | 2 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.6) ⚠ cell-cycle shift, explains ~65% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.376× (z -12.9) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.630× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 156 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -16.2) |
| [[SNU-1 (line)]] | wt | 169 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -28.5) |
| [[SW 900 (line)]] | alt | 292 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -15.9) |
| [[SW1417 (line)]] | alt | 148 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.277× (z -16.0) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -13.0) |
| [[A-172 (line)]] | wt | 131 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +8.7) ⚠ cell-cycle shift, explains ~65% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -16.7) |
| [[RPMI-7951 (line)]] | alt | 206 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -12.8) |
| [[SW 1271 (line)]] | alt | 361 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.200× (z -12.6) ⚠ unreliable plate only · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -9.8) |
| [[BT-474 (line)]] | alt | 141 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.309× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -8.9) |
| [[HS-578T (line)]] | alt | 197 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -18.0) |
| [[SHP-77 (line)]] | alt | 210 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -21.6) |
| [[SNU-423 (line)]] | alt | 121 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.326× (z -11.9) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -10.4) |
| [[SW48 (line)]] | wt | 165 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.159× (z -16.5) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -13.6) |
| [[A549 (line)]] | wt | 219 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -19.5) |
| [[HepG2_C3A (line)]] | wt | 120 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -11.9) |
| [[COLO 205 (line)]] | alt | 95.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.305× (z -10.2) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 149 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -13.0) |
| [[HCT15 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.230× (z -12.7) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 151 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -11.6) |
| [[NCI-H661 (line)]] | alt | 140 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -10.1) |
| [[SW 1088 (line)]] | alt | 126 | 0 | 1 | — | [[Carbamazepine (drug)]] 0.05 µM 0.0662× (z -10.5) |
| [[AN3 CA (line)]] | alt | 30.8 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 195 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4402), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCC1]] | +0.54 | +0.32 / +0.60 | both halves | 2e-04 |  |
| [[CHMP1B]] | +0.52 | +0.30 / +0.58 | both halves | 2e-04 |  |
| [[ZBTB20]] | +0.51 | +0.25 / +0.61 | both halves | 4e-04 |  |
| [[ATE1]] | +0.51 | +0.46 / +0.71 | both halves | 3e-05 |  |
| [[ATP9B]] | +0.49 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[SNX19]] | +0.49 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[LYPLAL1]] | +0.49 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[BCAS3]] | +0.49 | +0.25 / +0.53 | both halves | 4e-04 |  |
| [[ZNF37BP]] | +0.48 | +0.40 / +0.49 | both halves | 4e-05 |  |
| [[COMMD10]] | +0.48 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[JPX]] | +0.48 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[DIS3L2]] | +0.48 | +0.64 / +0.32 | both halves | 1e-04 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EED]] | -0.59 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[INTS6L]] | -0.59 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[POLH]] | -0.52 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[CRLS1]] | -0.51 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[APAF1]] | -0.51 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[LNX2]] | -0.49 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[EAF2]] | -0.49 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[SLC15A2]] | -0.48 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[SRP54-AS1]] | -0.48 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[PRCP]] | -0.47 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[LRRC40]] | -0.46 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[DDB2]] | -0.46 | -0.43 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.314). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.0, -30.4); signed map (-8.2, 12.3). **Vector** length 125, 46.6% of its response variance represented; |z| ≥ 3 in 1,538 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.4 | +2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.7 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.5 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | -0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.8 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.3 | +1.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +4.0 | +3.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.7 | -17.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -8.2 | -9.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.7 | -9.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -14.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.6 | -8.1 |
|  | [[EX229 (drug)]] 5 µM |  | -7.5 | -7.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.4 | -7.8 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 91 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.22 — chr12:28,133,249-28,581,511 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p56, FLJ11088, DKFZp779L1558 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6B0](https://www.uniprot.org/uniprotkb/Q7Z6B0) (Coiled-coil domain-containing protein 91):

> Involved in the regulation of membrane traffic through the trans-Golgi network (TGN). Functions in close cooperation with the GGAs in the sorting of hydrolases to lysosomes.

**Summary**, from NCBI Gene [55297](https://www.ncbi.nlm.nih.gov/gene/55297):

> Predicted to enable identical protein binding activity. Involved in Golgi to lysosome transport. Located in trans-Golgi network. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24855](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24855) · Entrez [55297](https://www.ncbi.nlm.nih.gov/gene/55297) · UniProt [Q7Z6B0](https://www.uniprot.org/uniprotkb/Q7Z6B0) · Ensembl [ENSG00000123106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123106)

## Data

Gene col 4402: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4402); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4402, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4402]; `tensor/DDL_lfc|DDL_z.npy` [4402]; `embed/gene_vectors.npy` [4402]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4402 or target_col == 4402). Every well: [[CCDC91 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC91.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
