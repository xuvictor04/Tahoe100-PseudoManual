---
symbol: "IFRD1"
type: "gene"
col: 122
ensembl_id: "ENSG00000006652"
name: "interferon related developmental regulator 1"
location: "7q31.1"
module: 93
arm: "+"
pooled_cpm: 179.45
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 4
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# IFRD1

*interferon related developmental regulator 1* — 7q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.37× (z +24.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.423× (z -9.8, q 3e-20, down in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Berbamine (drug)]] 0.05 µM: 0.746× (z -3.4, q 0.089, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SNU-1 0.101×, HepG2/C3A 0.248×, SNU-423 0.188×, A-427 0.253×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SW 1271 0.0648×, NCI-H2347 0.211×, HT-29 0.239×, SNU-423 0.211×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.237×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM53C]] (+0.78, fdr 7e-06), [[MYLIP]] (+0.68, fdr 7e-06), [[SPSB2]] (+0.67, fdr 1e-05); moves opposite to [[EFTUD2]] (-0.58, fdr 3e-05), [[BTBD1]] (-0.57, fdr 2e-05), [[TMEM209]] (-0.56, fdr 2e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 122.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.37×** | +24.4 | 0e+00 | 48/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.05×** | +13.1 | 1e-36 | 48/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.85×** | +12.3 | 2e-32 | 46/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.93×** | +12.1 | 1e-31 | 48/48 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.29×** | +9.7 | 4e-20 | 41/48 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +7.9 | 2e-13 | 41/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +7.6 | 3e-12 | 41/47 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +7.1 | 8e-11 | 38/49 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +6.3 | 1e-08 | 12/50 (HOP62, SW1417, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +6.3 | 2e-08 | 46/48 (KATO III, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.62×** | +5.9 | 2e-07 | 46/49 (SW48, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.63×** | +5.4 | 3e-06 | 43/48 (SHP-77, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.73×** | +4.8 | 8e-05 | 32/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.16×** | +4.7 | 9e-05 | 37/45 (LoVo, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.66×** | +4.4 | 4e-04 | 38/48 (KATO III, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.47×** | +4.4 | 4e-04 | 29/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.00×** | +4.2 | 7e-04 | 38/48 (SW48, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +4.2 | 7e-04 | 30/48 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +4.2 | 8e-04 | 30/48 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 122.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SNU-1 0.101×, HepG2/C3A 0.248×, SNU-423 0.188×, A-427 0.253×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SW 1271 0.0648×, NCI-H2347 0.211×, HT-29 0.239×, SNU-423 0.211×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.237×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.423×** | -9.8 | 3e-20 | 48/49 (SW 1271, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.420×** | -9.8 | 3e-20 | 42/44 (SNU-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.564×** | -6.2 | 1e-07 | 39/45 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Berbamine (drug)]] 0.05 µM |  | **0.746×** | -3.4 | 0.089 | 31/48 (Panc 03.27, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 122. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 173 | 13 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 12.4× (z +26.1) | — |
| [[SW48 (line)]] | wt | 189 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -8.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 199 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +27.1) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -10.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 153 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.27× (z +18.9) | — |
| [[SW1417 (line)]] | alt | 514 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -12.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 257 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -10.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 99.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +21.8) | — |
| [[SK-MEL-2 (line)]] | alt | 199 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +20.7) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -11.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 205 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -9.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 325 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -12.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 157 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -8.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 123 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.78× (z +18.2) | — |
| [[HS-578T (line)]] | alt | 160 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +19.5) | — |
| [[HT-29 (line)]] | alt | 258 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -13.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 133 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +16.2) | — |
| [[NCI-H23 (line)]] | alt | 124 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +21.2) | — |
| [[SNU-423 (line)]] | alt | 121 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.188× (z -13.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 213 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.17× (z +15.7) | — |
| [[A-172 (line)]] | wt | 103 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +20.3) | — |
| [[A-427 (line)]] | wt | 91.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.38× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -12.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 557 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.84× (z +17.9) | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -10.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 115 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +16.5) | — |
| [[HepG2_C3A (line)]] | wt | 217 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -13.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 95.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +22.2) | — |
| [[LOX-IMVI (line)]] | wt | 111 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +16.8) | — |
| [[LS 180 (line)]] | wt | 143 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 119 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.64× (z +21.7) | — |
| [[NCI-H2347 (line)]] | alt | 237 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -13.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 155 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -12.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 150 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +16.8) | — |
| [[A549 (line)]] | wt | 130 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +16.2) | — |
| [[AN3 CA (line)]] | alt | 206 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -9.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 138 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.52× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 163 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +21.4) | — |
| [[Panc 03.27 (line)]] | alt | 140 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +16.9) | — |
| [[SNU-1 (line)]] | wt | 117 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.101× (z -14.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 120 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.12× (z +20.9) | — |
| [[Hs 766T (line)]] | wt | 188 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -8.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 151 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.24× (z +20.3) | — |
| [[J82 (line)]] | alt | 129 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +14.9) | — |
| [[SHP-77 (line)]] | alt | 147 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.78× (z +10.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +10.2) | — |
| [[SW 1271 (line)]] | alt | 186 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0648× (z -13.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 158 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +17.3) | — |
| [[NCI-H2030 (line)]] | alt | 206 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +10.5) | — |
| [[SW 1088 (line)]] | alt | 232 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +11.2) | — |
| [[C-33 A (line)]] | alt | 140 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 157 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 122), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM53C]] | +0.78 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[MYLIP]] | +0.68 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[SPSB2]] | +0.67 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[DDIT3]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[ATF3]] | +0.65 | +0.74 / +0.63 | both halves | 7e-06 | STRING 632 |
| [[GTF2B]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[RSRC2]] | +0.63 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[BRD2]] | +0.61 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[POR]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[FAM222A]] | +0.59 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[DEDD2]] | +0.59 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[LRRC23]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFTUD2]] | -0.58 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[BTBD1]] | -0.57 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[TMEM209]] | -0.56 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[IPO9]] | -0.55 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[VPS16]] | -0.55 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[SYMPK]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 | same gene group |
| [[QSOX2]] | -0.54 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[COA1]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[RFT1]] | -0.53 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[POFUT1]] | -0.52 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[NUP155]] | -0.51 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[AAGAB]] | -0.51 | -0.44 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.762). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.7, -26.1); signed map (3.1, 17.1). **Vector** length 104, 43.0% of its response variance represented; |z| ≥ 3 in 1,186 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.6 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +7.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.0 | +1.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.2 | -0.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.0 | +0.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.5 | +3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.5 | +4.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.6 | -0.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.6 | +5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.4 | +12.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | +4.2 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -2.5 | -1.9 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | -2.5 | -2.2 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -2.5 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | interferon related developmental regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.1 — chr7:112,422,887-112,481,017 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PC4, TIS7 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Hallmark sets | MYOGENESIS, MTORC1_SIGNALING, MYC_TARGETS_V1 |
| Matched by | ensembl_id |

**Function**, from UniProt [O00458](https://www.uniprot.org/uniprotkb/O00458) (Interferon-related developmental regulator 1):

> Could play a role in regulating gene activity in the proliferative and/or differentiative pathways induced by NGF. May be an autocrine factor that attenuates or amplifies the initial ligand-induced signal (By similarity).

**Summary**, from NCBI Gene [3475](https://www.ncbi.nlm.nih.gov/gene/3475):

> This gene is an immediate early gene that encodes a protein related to interferon-gamma. This protein may function as a transcriptional co-activator/repressor that controls the growth and differentiation of specific cell types during embryonic development and tissue regeneration. Mutations in this gene are associated with sensory/motor neuropathy with ataxia. This gene may also be involved in modulating the pathogenesis of cystic fibrosis lung disease. Alternate splicing results in multiple …

**Accessions** — [HGNC:5456](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5456) · Entrez [3475](https://www.ncbi.nlm.nih.gov/gene/3475) · UniProt [O00458](https://www.uniprot.org/uniprotkb/O00458) · Ensembl [ENSG00000006652](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006652)

## Data

Gene col 122: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 122); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 122, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 122]; `tensor/DDL_lfc|DDL_z.npy` [122]; `embed/gene_vectors.npy` [122]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 122 or target_col == 122). Every well: [[IFRD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFRD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
