---
symbol: "RPAP2"
type: "gene"
col: 4343
ensembl_id: "ENSG00000122484"
name: "RNA polymerase II associated protein 2"
location: "1p22.1"
module: 28
arm: "+"
pooled_cpm: 95.78
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# RPAP2

*RNA polymerase II associated protein 2* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.62× (z +17.5, q 0e+00, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.659× (z -10.3, q 2e-22, down in 33 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.676× (z -10.1, q 1e-21, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCAR1]] (+0.73, fdr 7e-06), [[ARL14EP]] (+0.67, fdr 3e-05), [[FBXW4]] (+0.67, fdr 1e-05); moves opposite to [[IGSF8]] (-0.62, fdr 5e-05), [[LMTK3]] (-0.62, fdr 1e-05), [[NXPH4]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TMEM92]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4343.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +17.5 | 0e+00 | 35/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +17.3 | 0e+00 | 46/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +10.2 | 2e-22 | 40/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +10.2 | 2e-22 | 37/48 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +7.2 | 7e-11 | 27/48 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.24×** | +5.5 | 4e-06 | 21/48 (NCI-H460, hTERT-HPNE, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.3 | 1e-05 | 24/48 (HEC-1-A, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | 1.17× | +4.0 | 0.005 | 15/47 (A-172, hTERT-HPNE, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.15× | +3.5 | 0.027 | 11/47 (NCI-H2030, SW480, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.14× | +3.4 | 0.032 | 10/48 (Hs 766T, H4, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.4 | 0.032 | 2/48 (NCI-H23, HCT15) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.14× | +3.3 | 0.043 | 14/48 (HEC-1-A, HCT15, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.09× | +3.1 | 0.084 | 8/48 (A549, NCI-H460, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.09× | +3.1 | 0.084 | 0/48 | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.09× | +3.1 | 0.084 | 2/48 (J82, Hs 766T) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4343.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.659×** | -10.3 | 2e-22 | 33/47 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.676×** | -10.1 | 1e-21 | 39/48 (C32, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.491×** | -9.6 | 1e-19 | 40/49 (C32, J82, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.552×** | -8.0 | 2e-13 | 27/48 (C32, AN3 CA, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.753×** | -7.3 | 3e-11 | 30/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.778×** | -6.5 | 9e-09 | 23/48 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.847× | -6.1 | 1e-07 | 22/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.797×** | -5.8 | 4e-07 | 26/48 (LoVo, SNU-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.818×** | -5.2 | 2e-05 | 23/49 (CHP-212, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.831×** | -4.8 | 1e-04 | 23/48 (C-33 A, LoVo, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.951× | -4.3 | 8e-04 | 0/50 | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.847× | -4.3 | 9e-04 | 21/48 (C-33 A, MIA PaCa-2, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | 0.850× | -4.2 | 0.001 | 22/49 (SK-MEL-2, NCI-H23, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.852× | -4.1 | 0.002 | 21/48 (C-33 A, NCI-H460, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~84% of this change | 0.860× | -3.9 | 0.004 | 20/48 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.867× | -3.7 | 0.008 | 13/48 (SNU-423, HOP62, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.821×** | -3.6 | 0.009 | 20/48 (COLO 205, NCI-H1792, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.844× | -3.1 | 0.051 | 13/48 (NCI-H460, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.886× | -3.1 | 0.051 | 9/48 (CHP-212, NCI-H2030, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.796×** | -3.1 | 0.055 | 19/46 (NCI-H1792, RPMI-7951, …) | two highest doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.892× | -2.9 | 0.075 | 13/48 (C32, LS 180, …) | inconsistent across doses |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 0.895× | -2.9 | 0.091 | 5/49 (NCI-H2030, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4343. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 108 | 4 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +18.3) | [[Digitoxin (drug)]] 5 µM 0.451× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.599× (z -8.9) |
| [[C32 (line)]] | wt | 193 | 0 | 8 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.285× (z -14.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.301× (z -13.9) |
| [[LoVo (line)]] | wt | 123 | 5 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +19.7) | [[Auranofin (drug)]] 5 µM 0.514× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 108 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.338× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[C-33 A (line)]] | alt | 191 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.368× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 118 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +15.5) | — |
| [[LS 180 (line)]] | wt | 105 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.7) | [[Digitoxin (drug)]] 5 µM 0.436× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[NCI-H23 (line)]] | alt | 129 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.46× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.458× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.561× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 107 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.219× (z -9.6) |
| [[J82 (line)]] | alt | 92.6 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.421× (z -11.3) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.241× (z -10.1) |
| [[PANC-1 (line)]] | alt | 73.4 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +15.0) | [[TAK-901 (drug)]] 5 µM 0.286× (z -9.9) |
| [[SNU-1 (line)]] | wt | 187 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.258× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 75.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -23.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.416× (z -9.8) |
| [[HT-29 (line)]] | alt | 65.5 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.8) | [[Auranofin (drug)]] 5 µM 0.422× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 150 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +15.6) | — |
| [[CFPAC-1 (line)]] | alt | 66.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +9.8) | — |
| [[HCT15 (line)]] | alt | 124 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +13.9) | — |
| [[HepG2_C3A (line)]] | wt | 76.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.335× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change |
| [[Hs 766T (line)]] | wt | 82.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +15.4) | — |
| [[hTERT-HPNE (line)]] | wt | 88.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.375× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[KATO III (line)]] | alt | 74.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.8) | — |
| [[NCI-H1573 (line)]] | alt | 110 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.8) | — |
| [[NCI-H2347 (line)]] | alt | 55.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.3) | — |
| [[RKO (line)]] | wt | 164 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0791× (z -33.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.541× (z -8.8) |
| [[SNU-423 (line)]] | alt | 84.4 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.421× (z -9.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.479× (z -8.6) |
| [[AN3 CA (line)]] | alt | 139 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0717× (z -9.8) |
| [[BT-474 (line)]] | alt | 91.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 42.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | — |
| [[HOP62 (line)]] | alt | 73.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.24× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 83.7 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.219× (z -8.9) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 97.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[SW 900 (line)]] | alt | 50.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.382× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW48 (line)]] | wt | 118 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.5) | — |
| [[A-172 (line)]] | wt | 62.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 87.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 108 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 89.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 99.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 70.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4343), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCAR1]] | +0.73 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.67 | +0.76 / +0.45 | both halves | 3e-05 |  |
| [[FBXW4]] | +0.67 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[C8orf33]] | +0.67 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[YTHDC2]] | +0.67 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[MTHFSD]] | +0.65 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[ZC3H8]] | +0.65 | +0.79 / +0.48 | both halves | 2e-05 | pathway: RNA polymerase II transcribes snRNA genes |
| [[ICE2]] | +0.65 | +0.67 / +0.55 | both halves | 1e-05 | pathway: RNA polymerase II transcribes snRNA genes; STRING 545 |
| [[GCFC2]] | +0.65 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[ZNF337-AS1]] | +0.64 | +0.68 / +0.39 | both halves | 6e-05 |  |
| [[ZNG1A]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[CPSF2]] | +0.63 | +0.60 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGSF8]] | -0.62 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[LMTK3]] | -0.62 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[NXPH4]] | -0.59 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[LPCAT4]] | -0.59 | -0.64 / -0.36 | both halves | 1e-04 |  |
| [[NPTN]] | -0.58 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[ITGA7]] | -0.58 | -0.31 / -0.61 | both halves | 2e-04 |  |
| [[TIMP2]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[BAIAP2-DT]] | -0.57 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[RADX]] | -0.57 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[EDA]] | -0.56 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[TMEM92]] | -0.56 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[AHDC1]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM92]] | B | TMEM92 activity lowers RPAP2's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.38× higher at baseline in the lines without TMEM92 | 0.022 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[KLRG1]] | B | KLRG1 activity raises RPAP2's level | lines that do not express KLRG1 (8) vs lines expressing it (42) | 1.46× lower at baseline in the lines without KLRG1 | 0.032 | ⚠ within organs, on part of the lines; also absent: DUXAP10, CD226, DUXAP8; maybe low, not absent |
| [[GALNT16]] | B | GALNT16 activity raises RPAP2's level | lines that do not express GALNT16 (8) vs lines expressing it (42) | 1.44× lower at baseline in the lines without GALNT16 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000237356, PRKAR2B, FRG1-DT; maybe low, not absent |
| [[SLC16A9]] | B | SLC16A9 activity raises RPAP2's level | lines that do not express SLC16A9 (18) vs lines expressing it (32) | 1.15× lower at baseline in the lines without SLC16A9 | 0.079 | ⚠ within organs, on part of the lines; also absent: BOC, TLCD4, KIF26A; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers RPAP2's level | compounds that target TOP1: 2 of 3 raise it (Doxorubicin, Topotecan) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PRKAR2B]] | B | PRKAR2B activity raises RPAP2's level | lines that do not express PRKAR2B (12) vs lines expressing it (38) | 1.30× lower at baseline in the lines without PRKAR2B | 0.098 | ⚠ within organs, on part of the lines; also absent: EML1, GALNT16, KATNAL2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.608). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-23.4, 16.5); signed map (14.6, -26.4). **Vector** length 127, 38.2% of its response variance represented; |z| ≥ 3 in 1,173 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.3 | +17.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.2 | +10.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +9.0 | +10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +17.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +7.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.2 | +2.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.4 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.1 | -6.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -8.1 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.0 | -10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.7 | -5.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -6.9 | -4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.7 | -8.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.7 | -0.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase II associated protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.1 — chr1:92,299,059-92,402,056 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13150, Rtr1; previously C1orf82 |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXW5](https://www.uniprot.org/uniprotkb/Q8IXW5) (Putative RNA polymerase II subunit B1 CTD phosphatase RPAP2):

> Protein phosphatase that displays CTD phosphatase activity and regulates transcription of snRNA genes. Recognizes and binds phosphorylated 'Ser-7' of the C-terminal heptapeptide repeat domain (CTD) of the largest RNA polymerase II subunit POLR2A, and mediates dephosphorylation of 'Ser-5' of the CTD, thereby promoting transcription of snRNA genes. Downstream of EIF2AK3/PERK, dephosphorylates ERN1, a sensor for the endoplasmic reticulum unfolded protein response (UPR), to abort failed ER-stress …

**Summary**, from NCBI Gene [79871](https://www.ncbi.nlm.nih.gov/gene/79871):

> Enables RNA polymerase II CTD heptapeptide repeat phosphatase activity. Involved in PERK-mediated unfolded protein response and snRNA transcription. Located in cytosol and nucleolus. Part of transcription preinitiation complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25791](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25791) · Entrez [79871](https://www.ncbi.nlm.nih.gov/gene/79871) · UniProt [Q8IXW5](https://www.uniprot.org/uniprotkb/Q8IXW5) · Ensembl [ENSG00000122484](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122484)

## Data

Gene col 4343: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4343); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4343, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4343]; `tensor/DDL_lfc|DDL_z.npy` [4343]; `embed/gene_vectors.npy` [4343]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4343 or target_col == 4343). Every well: [[RPAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
