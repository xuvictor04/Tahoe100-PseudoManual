---
symbol: "CALU"
type: "gene"
col: 4900
ensembl_id: "ENSG00000128595"
name: "calumenin"
location: "7q32.1"
module: 42
arm: "+"
pooled_cpm: 390.5
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 21
n_dd_up_clean: 4
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# CALU

*calumenin* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.94× (z +11.8, q 1e-29, up in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.65× (z +9.0, q 5e-17, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.297× (z -30.5, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[P4HB]] (+0.82, fdr 7e-06), [[PDIA4]] (+0.79, fdr 7e-06), [[SEC22B]] (+0.79, fdr 7e-06); moves opposite to [[SDSL]] (-0.66, fdr 1e-05), [[RNF146]] (-0.65, fdr 7e-06), [[RPP38]] (-0.62, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SPARC]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4900.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +11.8 | 1e-29 | 44/49 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +11.2 | 7e-27 | 40/44 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +9.0 | 5e-17 | 46/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.43×** | +5.9 | 5e-07 | 31/45 (A-172, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +5.6 | 2e-06 | 39/49 (SK-MEL-2, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.8 | 1e-04 | 0/50 | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.17× | +4.0 | 0.005 | 16/49 (RPMI-7951, HS-578T, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.9 | 0.006 | 30/48 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.6 | 0.020 | 20/38 (HS-578T, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.049 | 30/48 (CFPAC-1, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.049 | 27/48 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.0 | 0.12 | 13/49 (C32, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4900.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.297×** | -30.5 | 0e+00 | 48/48 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.304×** | -20.3 | 0e+00 | 47/48 (A498, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.376×** | -17.4 | 0e+00 | 44/48 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.438×** | -14.7 | 0e+00 | 45/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.480×** | -12.1 | 1e-31 | 48/48 (A-172, H4, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.647×** | -7.4 | 8e-12 | 35/47 (SW 900, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.744×** | -7.4 | 8e-12 | 35/48 (RPMI-7951, A-427, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.748×** | -7.3 | 2e-11 | 34/48 (A549, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.768×** | -6.6 | 2e-09 | 26/49 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.717×** | -5.9 | 2e-07 | 41/48 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.708×** | -5.7 | 8e-07 | 41/47 (A-172, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.755×** | -5.0 | 3e-05 | 30/48 (AsPC-1, NCI-H2030, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.749×** | -4.9 | 3e-05 | 33/48 (LoVo, SNU-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.751×** | -4.9 | 4e-05 | 31/48 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | 0.841× | -4.4 | 5e-04 | 22/48 (A549, HOP62, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.790×** | -4.0 | 0.002 | 32/47 (AsPC-1, Panc 03.27, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.822×** | -3.5 | 0.015 | 23/48 (SW 1088, Hs 766T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4900. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 847 | 4 (4 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +17.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -24.1) |
| [[A-172 (line)]] | wt | 374 | 3 (3 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +17.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -23.2) |
| [[A549 (line)]] | wt | 313 | 1 (1 ⚠) | 8 | [[Dinaciclib (drug)]] 5 µM 2.16× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -20.6) |
| [[C32 (line)]] | wt | 857 | 4 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +15.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.15× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -13.7) |
| [[HEC-1-A (line)]] | alt | 204 | 4 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.46× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.85× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -20.7) |
| [[HOP62 (line)]] | alt | 694 | 3 (3 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +15.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -38.2) |
| [[A-427 (line)]] | wt | 194 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -18.9) |
| [[A498 (line)]] | wt | 867 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 1.76× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -35.4) |
| [[CFPAC-1 (line)]] | alt | 294 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.51× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -18.4) |
| [[RPMI-7951 (line)]] | alt | 643 | 2 (1 ⚠) | 6 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.03× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -28.2) |
| [[SNU-423 (line)]] | alt | 277 | 3 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.26× (z +9.6) | [[Harringtonine (drug)]] 0.5 µM 0.325× (z -13.3) |
| [[AsPC-1 (line)]] | alt | 549 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -28.1) |
| [[H4 (line)]] | wt | 706 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 1.98× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -31.3) |
| [[hTERT-HPNE (line)]] | wt | 837 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -21.7) |
| [[LoVo (line)]] | wt | 439 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -18.0) |
| [[NCI-H2030 (line)]] | alt | 382 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 1.94× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -34.0) |
| [[NCI-H460 (line)]] | wt | 292 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -20.9) |
| [[PANC-1 (line)]] | alt | 313 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +13.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -20.8) |
| [[SK-MEL-2 (line)]] | alt | 398 | 5 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +19.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.07× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.591× (z -12.2) |
| [[HT-29 (line)]] | alt | 368 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -23.9) |
| [[NCI-H2347 (line)]] | alt | 506 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 1.75× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -29.6) |
| [[Panc 03.27 (line)]] | alt | 260 | 3 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.37× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.05× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -23.9) |
| [[SW 900 (line)]] | alt | 564 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -23.8) |
| [[SW1417 (line)]] | alt | 408 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -27.1) |
| [[LOX-IMVI (line)]] | wt | 201 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.45× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -14.7) |
| [[NCI-H1792 (line)]] | alt | 412 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -15.0) |
| [[SNU-1 (line)]] | wt | 317 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +10.7) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.142× (z -20.2) |
| [[SW 1088 (line)]] | alt | 1,144 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -18.0) |
| [[BT-474 (line)]] | alt | 242 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -22.2) |
| [[HepG2_C3A (line)]] | wt | 195 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -15.2) |
| [[Hs 766T (line)]] | wt | 488 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -21.4) |
| [[J82 (line)]] | alt | 416 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -28.2) |
| [[KATO III (line)]] | alt | 336 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -26.0) |
| [[SHP-77 (line)]] | alt | 167 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.11× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.581× (z -9.1) |
| [[SW48 (line)]] | wt | 381 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.23× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -22.2) |
| [[C-33 A (line)]] | alt | 235 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.590× (z -8.8) |
| [[HCT15 (line)]] | alt | 344 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -15.4) |
| [[LS 180 (line)]] | wt | 181 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -18.4) |
| [[NCI-H661 (line)]] | alt | 418 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -17.8) |
| [[AN3 CA (line)]] | alt | 171 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.79× (z +12.9) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 234 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 242 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -14.4) |
| [[RKO (line)]] | wt | 436 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -21.5) |
| [[SW 1271 (line)]] | alt | 410 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -15.5) |
| [[SW480 (line)]] | alt | 213 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -12.9) |
| [[MIA PaCa-2 (line)]] | alt | 234 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 188 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -15.2) |
| [[COLO 205 (line)]] | alt | 260 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 306 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 341 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4900), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P4HB]] | +0.82 | +0.81 / +0.79 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation; STRING 872 |
| [[PDIA4]] | +0.79 | +0.77 / +0.73 | both halves | 7e-06 | STRING 660 |
| [[SEC22B]] | +0.79 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[HSP90B1]] | +0.77 | +0.77 / +0.72 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation; STRING 773 |
| [[KDELR2]] | +0.77 | +0.80 / +0.77 | both halves | 7e-06 |  |
| [[SEC61A1]] | +0.76 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[TMED9]] | +0.75 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[LMAN1]] | +0.74 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[KDELR3]] | +0.74 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[DAP]] | +0.73 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[SEC31A]] | +0.73 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[SEC13]] | +0.72 | +0.80 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDSL]] | -0.66 | -0.67 / -0.56 | both halves | 1e-05 |  |
| [[RNF146]] | -0.65 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[RPP38]] | -0.62 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[TRIM47]] | -0.62 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[CMTR2]] | -0.61 | -0.57 / -0.64 | both halves | 9e-06 |  |
| [[FBXW4]] | -0.61 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[FDX2]] | -0.61 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[ITPA]] | -0.61 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[PBDC1]] | -0.61 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[POLR3C]] | -0.61 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[MRPL38]] | -0.61 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[TLK2]] | -0.61 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPARC]] | B | SPARC activity raises CALU's level | lines that do not express SPARC (34) vs lines expressing it (16) | 1.65× lower at baseline in the lines without SPARC | 0.092 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.846). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.8, -31.3); signed map (-53.1, 7.9). **Vector** length 172, 69.4% of its response variance represented; |z| ≥ 3 in 1,620 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.66 to 11); *Asparagine N-linked glycosylation* (reactome, mean cos +0.50 to 23); *Maturation of DENV proteins* (reactome, mean cos +0.63 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.0 | +9.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +8.3 | +2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +8.0 | +1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.8 | +2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.7 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.9 | +1.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +4.3 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +2.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -15.1 | -14.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -14.4 | -20.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -13.7 | -12.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.3 | -17.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -10.8 | -30.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -8.7 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.8 | -7.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.9 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | calumenin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.1 — chr7:128,739,292-128,773,400 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | CREC family |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 6 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs); Platelet degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [O43852](https://www.uniprot.org/uniprotkb/O43852) (Calumenin):

> Involved in regulation of vitamin K-dependent carboxylation of multiple N-terminal glutamate residues. Seems to inhibit gamma-carboxylase GGCX. Binds 7 calcium ions with a low affinity (By similarity).

**Summary**, from NCBI Gene [813](https://www.ncbi.nlm.nih.gov/gene/813):

> The product of this gene is a calcium-binding protein localized in the endoplasmic reticulum (ER) and it is involved in such ER functions as protein folding and sorting. This protein belongs to a family of multiple EF-hand proteins (CERC) that include reticulocalbin, ERC-55, and Cab45 and the product of this gene. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:1458](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1458) · Entrez [813](https://www.ncbi.nlm.nih.gov/gene/813) · UniProt [O43852](https://www.uniprot.org/uniprotkb/O43852) · Ensembl [ENSG00000128595](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128595)

## Data

Gene col 4900: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4900); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4900, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4900]; `tensor/DDL_lfc|DDL_z.npy` [4900]; `embed/gene_vectors.npy` [4900]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4900 or target_col == 4900). Every well: [[CALU — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CALU.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
