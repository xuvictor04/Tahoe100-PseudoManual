---
symbol: "ROCK2"
type: "gene"
col: 5545
ensembl_id: "ENSG00000134318"
name: "Rho associated coiled-coil containing protein kinase 2"
location: "2p25.1"
module: 179
arm: "-"
pooled_cpm: 282.51
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# ROCK2

*Rho associated coiled-coil containing protein kinase 2* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.29× (z +9.6, q 5e-19, up in 29 of 48 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.41× (z +8.8, q 5e-16, up in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (NCI-H2347 2.04×, CHP-212 4.63×, SHP-77 1.80×, C32 2.17×, …; ⚠ cell-cycle shift, explains ~32% of this change); [[Harringtonine (drug)]] 5 µM in 8 lines (C32 3.39×, A-172 1.93×, NCI-H2347 2.14×, PANC-1 1.72×, …); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RPMI-7951 2.33×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (A549 1.90×).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.684× (z -9.7, q 2e-19, down in 39 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 0.793× (z -4.4, q 0.002, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (SW480 0.428×, A549 0.435×, LS 180 0.447×, HT-29 0.403×, …; ⚠ cell-cycle shift, explains ~9% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 4 lines (SW480 0.405×, SNU-1 0.337×, NCI-H460 0.545×, KATO III 0.335×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.255×, A-427 0.351×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SW480 0.653×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC42BPA]] (+0.60, fdr 1e-05), [[WWC3]] (+0.59, fdr 1e-05), [[ZNF69]] (+0.59, fdr 1e-05); moves opposite to [[TBC1D22A-DT]] (-0.64, fdr 7e-06), [[GPR107]] (-0.64, fdr 7e-06), [[ZFPL1]] (-0.63, fdr 7e-06).
> It sits in the **-** arm of [[Module 179]] (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[UTRN]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5545.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (NCI-H2347 2.04×, CHP-212 4.63×, SHP-77 1.80×, C32 2.17×, …; ⚠ cell-cycle shift, explains ~32% of this change); [[Harringtonine (drug)]] 5 µM in 8 lines (C32 3.39×, A-172 1.93×, NCI-H2347 2.14×, PANC-1 1.72×, …); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RPMI-7951 2.33×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (A549 1.90×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.29×** | +9.6 | 5e-19 | 29/48 (NCI-H2347, CHP-212, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +8.8 | 5e-16 | 33/48 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.25×** | +6.0 | 4e-07 | 29/48 (C-33 A, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.24×** | +5.7 | 1e-06 | 28/48 (NCI-H2347, C-33 A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +5.1 | 5e-05 | 22/48 (C-33 A, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +4.6 | 5e-04 | 23/48 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.15× | +3.7 | 0.020 | 11/49 (SW1417, A549, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | 1.14× | +3.4 | 0.042 | 20/47 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.13× | +3.4 | 0.047 | 6/48 (HepG2/C3A, A549, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 5 µM |  | 1.09× | +3.1 | 0.10 | 0/49 | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.12× | +3.0 | 0.13 | 8/48 (SW1417, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5545.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (SW480 0.428×, A549 0.435×, LS 180 0.447×, HT-29 0.403×, …; ⚠ cell-cycle shift, explains ~9% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 4 lines (SW480 0.405×, SNU-1 0.337×, NCI-H460 0.545×, KATO III 0.335×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.255×, A-427 0.351×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SW480 0.653×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.684×** | -9.7 | 2e-19 | 39/47 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.818×** | -7.5 | 1e-11 | 26/49 (SW480, A549, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.793×** | -4.4 | 0.002 | 29/48 (NCI-H460, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.875× | -3.6 | 0.053 | 15/48 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.878× | -3.4 | 0.055 | 18/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.879× | -3.4 | 0.055 | 17/48 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.883× | -3.3 | 0.076 | 12/48 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.884× | -3.3 | 0.076 | 14/48 (A549, SW48, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.881× | -3.2 | 0.095 | 12/48 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.890× | -3.1 | 0.12 | 14/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.852× | -3.0 | 0.12 | 13/48 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5545. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 458 | 0 | 12 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -24.1) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.653× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 140 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +14.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.14× (z +10.8) | — |
| [[A549 (line)]] | wt | 361 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +11.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 1.90× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -16.9) ⚠ cell-cycle shift, explains ~9% of this change |
| [[HepG2_C3A (line)]] | wt | 729 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -14.0) ⚠ cell-cycle shift, explains ~9% of this change |
| [[KATO III (line)]] | alt | 458 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.12× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -13.5) ⚠ cell-cycle shift, explains ~9% of this change |
| [[LS 180 (line)]] | wt | 456 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -15.2) ⚠ cell-cycle shift, explains ~9% of this change |
| [[SW1417 (line)]] | alt | 692 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -12.4) ⚠ cell-cycle shift, explains ~9% of this change |
| [[LoVo (line)]] | wt | 326 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.18× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -9.2) ⚠ cell-cycle shift, explains ~9% of this change |
| [[BT-474 (line)]] | alt | 164 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +11.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[C-33 A (line)]] | alt | 278 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.93× (z +10.8) ⚠ cell-cycle shift, explains ~21% of this change | [[Dinaciclib (drug)]] 5 µM 0.255× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 136 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.39× (z +15.0) | — |
| [[HEC-1-A (line)]] | alt | 238 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 1.64× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -11.4) ⚠ cell-cycle shift, explains ~9% of this change |
| [[HT-29 (line)]] | alt | 497 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -15.0) ⚠ cell-cycle shift, explains ~9% of this change |
| [[PANC-1 (line)]] | alt | 270 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +13.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.72× (z +10.8) | — |
| [[SNU-1 (line)]] | wt | 307 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.337× (z -14.3) ⚠ toxic |
| [[A-172 (line)]] | wt | 251 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 1.93× (z +11.8) | — |
| [[A-427 (line)]] | wt | 413 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.351× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 483 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.491× (z -9.6) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 124 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +14.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[H4 (line)]] | wt | 129 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 186 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.568× (z -9.7) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 266 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.515× (z -11.7) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 207 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.464× (z -11.5) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 249 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.545× (z -12.8) ⚠ toxic |
| [[RKO (line)]] | wt | 264 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +9.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[RPMI-7951 (line)]] | alt | 211 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 320 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +14.3) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 183 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.89× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 205 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +11.3) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A498 (line)]] | wt | 175 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 273 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 315 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 312 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 173 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 170 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 204 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 312 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 320 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 238 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5545), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42BPA]] | +0.60 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[WWC3]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ZNF69]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[CDK6]] | +0.59 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[BAZ1B]] | +0.59 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[EEA1]] | +0.59 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[DSP]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SPEN]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 | pathway: RHOBTB GTPase Cycle |
| [[TIGD2]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[TJP1]] | +0.56 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[SLK]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 | pathway: RHOA GTPase cycle; STRING 514 |
| [[CPT1A]] | +0.55 | +0.60 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D22A-DT]] | -0.64 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[GPR107]] | -0.64 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[ZFPL1]] | -0.63 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | -0.63 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[KHDC4]] | -0.62 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[NDUFAF7]] | -0.62 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[KCTD7]] | -0.61 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[CUL7]] | -0.60 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[C1orf52]] | -0.59 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[CDC26]] | -0.59 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[DPM1]] | -0.59 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[TMEM39A]] | -0.58 | -0.58 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UTRN]] | C | UTRN activity lowers ROCK2's level | lines that do not express UTRN (3) vs lines expressing it (47) | 1.94× higher at baseline in the lines without UTRN | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |
| [[CDK6]] | C | CDK6 activity weakens ROCK2's drug response | lines that do not express CDK6 (4) vs lines expressing it (45) | the lines without CDK6 respond 1.63× as strongly (z diff -2.27); strongest at Homoharringtonine 0.5 µM: 1.92x vs 1.26x (z diff -6.9) | 0.081 | ⚠ few lines (4 vs 46); across organs; also absent: FCHSD1, CDK6-AS1, PLS3; target measured in part of the lines; artifact flags |
| [[TACC1]] | C | TACC1 activity lowers ROCK2's level | lines that do not express TACC1 (3) vs lines expressing it (47) | 1.77× higher at baseline in the lines without TACC1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLEC2D, TNNI3K, COL21A1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **-** arm (projection on the module's main direction -0.776). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (5.1, -20.6); signed map (10.7, -9.5). **Vector** length 142, 44.5% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +8.2 | +5.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.9 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +7.0 | +6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +6.8 | +9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.7 | +5.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.3 | +2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.5 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +2.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +3.2 | +3.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.9 | -9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -4.7 | -7.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.8 | -2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.7 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.7 | -3.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.0 | -3.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.9 | -2.2 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.8 | -2.3 |
|  | [[Gallic acid (drug)]] 5 µM |  | -2.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | Rho associated coiled-coil containing protein kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:11,179,759-11,348,330 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Rho associated coiled-coil containing protein kinase family |
| Reactome | 28 pathways, smallest: RHO GTPases Activate ROCKs; Sema4D induced cell migration and growth-cone collapse; RHOBTB1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O75116](https://www.uniprot.org/uniprotkb/O75116) (Rho-associated protein kinase 2):

> Protein kinase which is a key regulator of actin cytoskeleton and cell polarity. Involved in regulation of smooth muscle contraction, actin cytoskeleton organization, stress fiber and focal adhesion formation, neurite retraction, cell adhesion and motility via phosphorylation of ADD1, BRCA2, CNN1, EZR, DPYSL2, EP300, MSN, MYL9/MLC2, NPM1, RDX, PPP1R12A and VIM. Phosphorylates SORL1 and IRF4. Acts as a negative regulator of VEGF-induced angiogenic endothelial cell activation. Positively …

**Summary**, from NCBI Gene [9475](https://www.ncbi.nlm.nih.gov/gene/9475):

> The protein encoded by this gene is a serine/threonine kinase that regulates cytokinesis, smooth muscle contraction, the formation of actin stress fibers and focal adhesions, and the activation of the c-fos serum response element. This protein, which is an isozyme of ROCK1 is a target for the small GTPase Rho. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10252](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10252) · Entrez [9475](https://www.ncbi.nlm.nih.gov/gene/9475) · UniProt [O75116](https://www.uniprot.org/uniprotkb/O75116) · Ensembl [ENSG00000134318](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134318)

## Data

Gene col 5545: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5545); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5545, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5545]; `tensor/DDL_lfc|DDL_z.npy` [5545]; `embed/gene_vectors.npy` [5545]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5545 or target_col == 5545). Every well: [[ROCK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ROCK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
