---
symbol: "POLR3A"
type: "gene"
col: 7298
ensembl_id: "ENSG00000148606"
name: "RNA polymerase III subunit A"
location: "10q22.3"
module: 12
arm: "+"
pooled_cpm: 49.34
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 4
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# POLR3A

*RNA polymerase III subunit A* — 10q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.95× (z +18.5, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.638× (z -12.5, q 3e-33, down in 34 of 47 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (LoVo 0.115×, A-172 0.0931×, NCI-H2030 0.238×, PANC-1 0.351×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (KATO III 0.0868×, RKO 0.168×, SW48 0.105×, C32 0.212×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.151×, NCI-H23 0.173×, PANC-1 0.386×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.312×); [[γ-Oryzanol (drug)]] 0.5 µM in 1 line (NCI-H661 0.0845×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHX57]] (+0.76, fdr 7e-06), [[DDX55]] (+0.72, fdr 7e-06), [[REXO4]] (+0.70, fdr 7e-06); moves opposite to [[YPEL5]] (-0.62, fdr 1e-05), [[GNAS]] (-0.62, fdr 1e-05), [[TXNDC16]] (-0.61, fdr 4e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZFP82]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7298.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +18.5 | 0e+00 | 44/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.86×** | +17.3 | 0e+00 | 45/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.85×** | +17.1 | 0e+00 | 46/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.52×** | +13.4 | 6e-39 | 39/49 (PANC-1, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.28×** | +12.0 | 4e-31 | 34/48 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +10.3 | 1e-22 | 39/48 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +8.8 | 2e-16 | 31/48 (HS-578T, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +8.5 | 2e-15 | 32/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +8.3 | 7e-15 | 27/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +7.9 | 1e-13 | 33/48 (PANC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.28×** | +6.9 | 3e-10 | 24/48 (PANC-1, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.26×** | +6.0 | 7e-08 | 24/47 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.43×** | +5.2 | 1e-05 | 22/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +5.1 | 1e-05 | 20/48 (SNU-423, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.20×** | +5.1 | 2e-05 | 17/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.41×** | +5.0 | 2e-05 | 17/48 (SW480, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +4.6 | 1e-04 | 20/48 (NCI-H1573, HEC-1-A, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.25×** | +4.4 | 3e-04 | 12/48 (PANC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7298.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (LoVo 0.115×, A-172 0.0931×, NCI-H2030 0.238×, PANC-1 0.351×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (KATO III 0.0868×, RKO 0.168×, SW48 0.105×, C32 0.212×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.151×, NCI-H23 0.173×, PANC-1 0.386×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.312×); [[γ-Oryzanol (drug)]] 0.5 µM in 1 line (NCI-H661 0.0845×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.638×** | -12.5 | 3e-33 | 34/47 (RKO, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.636×** | -12.1 | 2e-31 | 31/42 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.659×** | -10.8 | 9e-25 | 32/45 (KATO III, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.816×** | -5.5 | 6e-06 | 22/47 (J82, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.878× | -5.1 | 5e-05 | 21/48 (A498, LOX-IMVI, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -4.9 | 1e-04 | 20/48 (NCI-H460, SW1417, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.847× | -4.6 | 3e-04 | 20/47 (BT-474, KATO III, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.891× | -3.9 | 0.008 | 13/48 (SW1417, RKO, …) | two highest doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.887× | -3.2 | 0.075 | 18/48 (RKO, SNU-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.890× | -3.1 | 0.096 | 21/48 (RKO, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7298. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 53.5 | 3 | 3 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.02× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -14.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 70.2 | 3 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.06× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.351× (z -15.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 48.4 | 3 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.82× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.0931× (z -23.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 65.3 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.384× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 40.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.09× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -10.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 81.0 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -20.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 69.7 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.90× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.509× (z -11.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 39.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.28× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -11.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 23.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.32× (z +9.7) | — |
| [[C32 (line)]] | wt | 45.0 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.40× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -14.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 38.7 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.34× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.115× (z -24.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 39.7 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.55× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 35.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.99× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 55.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -19.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 54.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.66× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -11.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 68.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.16× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -16.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 50.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -9.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 50.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.88× (z +10.7) | — |
| [[KATO III (line)]] | alt | 39.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0868× (z -21.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 46.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.312× (z -13.7) |
| [[A549 (line)]] | wt | 46.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -11.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 80.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -10.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 60.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -11.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 39.7 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.31× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 61.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -11.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 52.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 1.96× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 50.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.31× (z +9.4) | — |
| [[J82 (line)]] | alt | 33.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.280× (z -12.3) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 49.2 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.301× (z -8.8) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 43.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.80× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 63.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 40.9 | 0 | 1 | — | [[γ-Oryzanol (drug)]] 0.5 µM 0.0845× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 54.4 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.158× (z -10.0) ⚠ toxic |
| [[BT-474 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 48.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7298), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX57]] | +0.76 | +0.67 / +0.73 | both halves | 7e-06 | STRING 467 |
| [[DDX55]] | +0.72 | +0.65 / +0.68 | both halves | 7e-06 | STRING 489 |
| [[REXO4]] | +0.70 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[NUDCD3]] | +0.68 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[TAF1A]] | +0.67 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[MIEF1]] | +0.67 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[VTA1]] | +0.66 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[MRPS23]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[EIF3M]] | +0.65 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[RMND1]] | +0.65 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[MPHOSPH10]] | +0.65 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[CINP]] | +0.65 | +0.62 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YPEL5]] | -0.62 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[GNAS]] | -0.62 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.61 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[KDM6A]] | -0.60 | -0.49 / -0.65 | both halves | 1e-05 | STRING 511 |
| [[FMR1]] | -0.58 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[HMGN2]] | -0.57 | -0.41 / -0.43 | both halves | 4e-05 | STRING 651 |
| [[STAG2]] | -0.57 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[ANKRD10]] | -0.56 | -0.50 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFP82]] | B | ZFP82 activity raises POLR3A's level | lines that do not express ZFP82 (20) vs lines expressing it (30) | 1.09× lower at baseline in the lines without ZFP82 | 0.063 | ⚠ within organs, on part of the lines; also absent: UBE2Q2P13, TUB, MIR130AHG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.401). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-32.5, -7.8); signed map (-16.0, -21.9). **Vector** length 106, 26.7% of its response variance represented; |z| ≥ 3 in 1,156 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.7 | +13.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.8 | +12.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.6 | +8.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.9 | +7.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +4.6 | +6.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.8 | +5.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +4.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.5 | +4.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.5 | -5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.5 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.4 | -12.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | -3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.9 | -12.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -1.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.2 | -1.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase III subunit A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.3 — chr10:77,953,148-78,029,522 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPC1, RPC155, hRPC155, C160 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Reactome | 10 pathways, smallest: RNA Polymerase III Chain Elongation; RNA Polymerase III Transcription Termination; RNA Polymerase III Transcription Initiation From Type 2 Promoter |
| Matched by | ensembl_id |

**Function**, from UniProt [O14802](https://www.uniprot.org/uniprotkb/O14802) (DNA-directed RNA polymerase III subunit RPC1):

> Catalytic core component of RNA polymerase III (Pol III), a DNA-dependent RNA polymerase which synthesizes small non-coding RNAs using the four ribonucleoside triphosphates as substrates. Synthesizes 5S rRNA, snRNAs, tRNAs and miRNAs from at least 500 distinct genomic loci. Pol III-mediated transcription cycle proceeds through transcription initiation, transcription elongation and transcription termination stages. During transcription initiation, Pol III is recruited to DNA promoters type I, II …

**Summary**, from NCBI Gene [11128](https://www.ncbi.nlm.nih.gov/gene/11128):

> The protein encoded by this gene is the catalytic component of RNA polymerase III, which synthesizes small RNAs. The encoded protein also acts as a sensor to detect foreign DNA and trigger an innate immune response. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:30074](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30074) · Entrez [11128](https://www.ncbi.nlm.nih.gov/gene/11128) · UniProt [O14802](https://www.uniprot.org/uniprotkb/O14802) · Ensembl [ENSG00000148606](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148606)

## Data

Gene col 7298: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7298); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7298, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7298]; `tensor/DDL_lfc|DDL_z.npy` [7298]; `embed/gene_vectors.npy` [7298]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7298 or target_col == 7298). Every well: [[POLR3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
