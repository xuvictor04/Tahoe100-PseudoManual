---
symbol: "KDM3A"
type: "gene"
col: 3694
ensembl_id: "ENSG00000115548"
name: "lysine demethylase 3A"
location: "2p11.2"
module: 79
arm: "+"
pooled_cpm: 329.78
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 19
n_dd_up_clean: 8
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# KDM3A

*lysine demethylase 3A* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.17× (z +9.6, q 3e-19, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.267× (z -15.9, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.663× (z -5.1, q 3e-05, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MXI1]] (+0.84, fdr 7e-06), [[SAP30-DT]] (+0.82, fdr 7e-06), [[P4HA1]] (+0.81, fdr 7e-06); moves opposite to [[MAK16]] (-0.63, fdr 7e-06), [[UTP20]] (-0.63, fdr 1e-05), [[ABCE1]] (-0.62, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLEKHA2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3694.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.17×** | +9.6 | 3e-19 | 43/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +8.5 | 4e-15 | 40/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.63×** | +6.1 | 2e-07 | 38/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.28×** | +5.4 | 1e-05 | 44/48 (A-427, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +5.3 | 1e-05 | 5/50 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **2.20×** | +5.1 | 2e-05 | 42/48 (COLO 205, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +5.1 | 2e-05 | 36/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +3.9 | 0.006 | 32/49 (NCI-H23, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.72×** | +3.5 | 0.025 | 36/48 (LoVo, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.090 | 26/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Terfenadine (drug)]] 5 µM |  | 1.19× | +3.1 | 0.11 | 23/48 (A-172, Panc 03.27, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 1.27× | +3.0 | 0.12 | 24/48 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3694.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.267×** | -15.9 | 0e+00 | 44/44 (A-427, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.292×** | -15.4 | 0e+00 | 48/49 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.433×** | -9.7 | 9e-20 | 42/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.494×** | -8.5 | 4e-15 | 47/47 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.553×** | -7.1 | 1e-10 | 37/47 (LOX-IMVI, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.663×** | -5.1 | 3e-05 | 42/48 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.775×** | -4.5 | 6e-04 | 36/48 (HepG2/C3A, NCI-H1792, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.700×** | -4.5 | 6e-04 | 36/48 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.726×** | -4.0 | 0.004 | 39/49 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.729×** | -3.9 | 0.005 | 37/48 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.743×** | -3.7 | 0.011 | 36/49 (NCI-H2030, HT-29, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.747×** | -3.6 | 0.013 | 40/48 (NCI-H2030, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.762×** | -3.4 | 0.030 | 31/48 (KATO III, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.765×** | -3.3 | 0.033 | 31/48 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.768×** | -3.3 | 0.036 | 36/48 (HCT15, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.761×** | -3.3 | 0.036 | 27/48 (A-172, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.777×** | -3.1 | 0.056 | 30/48 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.784×** | -3.0 | 0.077 | 32/48 (NCI-H460, HOP62, …) | inconsistent across doses | position effect removed |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.787×** | -3.0 | 0.082 | 30/49 (NCI-H2030, A-172, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.845× | -3.0 | 0.086 | 19/48 (NCI-H2347, NCI-H661, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3694. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 248 | 7 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 11.0× (z +23.9) | [[Dinaciclib (drug)]] 5 µM 0.291× (z -11.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 269 | 6 (2 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.67× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +14.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.387× (z -10.6) ⚠ toxic |
| [[KATO III (line)]] | alt | 363 | 3 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.98× (z +12.5) | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -12.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 479 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 473 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.17× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -16.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 383 | 3 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -16.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 252 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.54× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -10.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 266 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.348× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 385 | 3 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -16.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 257 | 3 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.15× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -11.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 319 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.27× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.228× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 463 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -21.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 370 | 2 (1 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.95× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -20.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 396 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -16.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 296 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.77× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -11.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 338 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -12.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 221 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.70× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.395× (z -9.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 553 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 283 | 1 (1 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.74× (z +9.4) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.214× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 560 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -13.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 387 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -19.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 401 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -11.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 353 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -13.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 432 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -15.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 255 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -11.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 381 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -13.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 441 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.247× (z -10.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 474 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -13.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 318 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.291× (z -11.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 281 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 358 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -13.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 395 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -17.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 269 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -13.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 288 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.72× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -12.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 310 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -12.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 298 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -12.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 417 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -11.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 267 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -10.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 202 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -8.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 367 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 271 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 185 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +9.4) | — |
| [[RKO (line)]] | wt | 322 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -9.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 329 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.385× (z -11.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 431 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -14.8) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 407 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 374 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 271 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3694), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXI1]] | +0.84 | +0.83 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[SAP30-DT]] | +0.82 | +0.84 / +0.74 | both halves | 7e-06 |  |
| [[P4HA1]] | +0.81 | +0.83 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[PDK3]] | +0.78 | +0.85 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[ANKRD37]] | +0.77 | +0.81 / +0.67 | both halves | 7e-06 |  |
| [[WDR45B]] | +0.76 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.76 | +0.82 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[RBPJ]] | +0.76 | +0.77 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[KDM4B]] | +0.76 | +0.78 / +0.71 | both halves | 7e-06 | pathway: Chromatin modifying enzymes; STRING 837 |
| [[INSIG2]] | +0.76 | +0.78 / +0.73 | both halves | 7e-06 |  |
| [[HILPDA]] | +0.75 | +0.82 / +0.66 | both halves | 7e-06 |  |
| [[FAM13A]] | +0.74 | +0.77 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAK16]] | -0.63 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[UTP20]] | -0.63 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[ABCE1]] | -0.62 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[COA7]] | -0.61 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[PRORP]] | -0.61 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[ARMC6]] | -0.61 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[GPATCH4]] | -0.61 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[ANAPC7]] | -0.61 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[ZNF195]] | -0.60 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[DHX37]] | -0.60 | -0.61 / -0.58 | both halves | 8e-06 |  |
| [[GNL3L]] | -0.60 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[RRP15]] | -0.59 | -0.56 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHA2]] | C | PLEKHA2 activity raises KDM3A's level | lines that do not express PLEKHA2 (4) vs lines expressing it (45) | 1.35× lower at baseline in the lines without PLEKHA2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: LSMEM2, ENSG00000285868; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.874). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.5, -16.8); signed map (-35.1, 23.6). **Vector** length 133, 56.5% of its response variance represented; |z| ≥ 3 in 1,267 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *glycolysis* (hallmark, mean cos +0.70 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.4 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | +1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.5 | +0.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.5 | +1.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.4 | +1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | -0.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.9 | -3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -8.8 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.7 | -0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.5 | -8.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.7 | -0.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.5 | -1.4 |
|  | [[EX229 (drug)]] 5 µM |  | -3.3 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | +0.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | lysine demethylase 3A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:86,440,647-86,492,716 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TSGA, KIAA0742, JHMD2A; previously JMJD1, JMJD1A |
| Gene groups (HGNC) | Lysine demethylase 3 family |
| Hallmark sets | HYPOXIA |
| Reactome | 6 pathways, smallest: HDMs demethylate histones; NR1H3 & NR1H2 regulate gene expression linked to cholesterol transport and efflux; NR1H2 and NR1H3-mediated signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4C1](https://www.uniprot.org/uniprotkb/Q9Y4C1) (Lysine-specific demethylase 3A):

> Histone demethylase that specifically demethylates 'Lys-9' of histone H3, thereby playing a central role in histone code. Preferentially demethylates mono- and dimethylated H3 'Lys-9' residue, with a preference for dimethylated residue, while it has weak or no activity on trimethylated H3 'Lys-9'. Demethylation of Lys residue generates formaldehyde and succinate. Involved in hormone-dependent transcriptional activation, by participating in recruitment to androgen-receptor target genes, …

**Summary**, from NCBI Gene [55818](https://www.ncbi.nlm.nih.gov/gene/55818):

> Enables histone H3K9me/H3K9me2 demethylase activity; iron ion binding activity; and nuclear androgen receptor binding activity. Involved in androgen receptor signaling pathway; formaldehyde biosynthetic process; and positive regulation of DNA-templated transcription. Located in nucleoplasm. Implicated in cervical cancer and colon cancer. Biomarker of Ewing sarcoma; hepatocellular carcinoma; nasopharynx carcinoma; and prostate cancer. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20815](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20815) · Entrez [55818](https://www.ncbi.nlm.nih.gov/gene/55818) · UniProt [Q9Y4C1](https://www.uniprot.org/uniprotkb/Q9Y4C1) · Ensembl [ENSG00000115548](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115548)

## Data

Gene col 3694: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3694); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3694, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3694]; `tensor/DDL_lfc|DDL_z.npy` [3694]; `embed/gene_vectors.npy` [3694]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3694 or target_col == 3694). Every well: [[KDM3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDM3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
