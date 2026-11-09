---
symbol: "MYSM1"
type: "gene"
col: 8539
ensembl_id: "ENSG00000162601"
name: "Myb like, SWIRM and MPN domains 1"
location: "1p32.1"
module: 163
arm: "+"
pooled_cpm: 131.37
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# MYSM1

*Myb like, SWIRM and MPN domains 1* — 1p32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.21× (z +19.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.678× (z -6.7, q 1e-08, down in 38 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (H4 0.252×, NCI-H1573 0.390×, C-33 A 0.337×, NCI-H1792 0.400×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (KATO III 0.369×, RKO 0.446×, SNU-423 0.470×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 0.480×, SHP-77 0.465×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[AZD1390 (drug)]] 5 µM in 1 line (CHP-212 0.0568×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOSR1]] (+0.68, fdr 2e-05), [[ICE2]] (+0.65, fdr 7e-06), [[ZNF621]] (+0.63, fdr 3e-05); moves opposite to [[CCNY]] (-0.68, fdr 1e-05), [[RNF38]] (-0.67, fdr 1e-05), [[UBE2G1]] (-0.65, fdr 1e-05).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BRSK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8539.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.21×** | +19.3 | 0e+00 | 48/48 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +10.5 | 4e-23 | 46/48 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +10.2 | 5e-22 | 47/48 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +4.9 | 1e-04 | 32/48 (BT-474, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 0.004 | 27/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +4.0 | 0.005 | 29/49 (NCI-H23, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.013 | 27/48 (BT-474, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.6 | 0.018 | 25/48 (SW 900, NCI-H2347, …) | inconsistent across doses |  |
| [[Baicalin (drug)]] 5 µM |  | 1.16× | +3.6 | 0.018 | 10/49 (MIA PaCa-2, KATO III, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.027 | 26/49 (SK-MEL-2, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.035 | 28/48 (NCI-H460, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8539.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (H4 0.252×, NCI-H1573 0.390×, C-33 A 0.337×, NCI-H1792 0.400×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (KATO III 0.369×, RKO 0.446×, SNU-423 0.470×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 0.480×, SHP-77 0.465×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[AZD1390 (drug)]] 5 µM in 1 line (CHP-212 0.0568×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.678×** | -6.7 | 1e-08 | 38/49 (A498, SHP-77, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.669×** | -6.4 | 4e-08 | 34/45 (KATO III, RKO, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.777×** | -4.2 | 0.005 | 28/44 (H4, NCI-H1573, …) | all doses, flat | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.861× | -3.7 | 0.034 | 13/48 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.819×** | -3.5 | 0.061 | 24/48 (SW1417, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.827×** | -3.3 | 0.092 | 22/48 (H4, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.832× | -3.1 | 0.14 | 22/48 (AsPC-1, NCI-H23, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.838× | -3.1 | 0.14 | 21/48 (A-172, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.839× | -3.1 | 0.14 | 22/48 (AsPC-1, PANC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.841× | -3.0 | 0.15 | 22/48 (RKO, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8539. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 89.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +14.2) | — |
| [[NCI-H1573 (line)]] | alt | 133 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.390× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 99.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.5) | — |
| [[A498 (line)]] | wt | 136 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.480× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 161 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +17.8) | — |
| [[HT-29 (line)]] | alt | 113 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +18.4) | — |
| [[LOX-IMVI (line)]] | wt | 140 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.456× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[NCI-H460 (line)]] | wt | 102 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +15.8) | — |
| [[AsPC-1 (line)]] | alt | 160 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +15.7) | — |
| [[COLO 205 (line)]] | alt | 138 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +14.8) | — |
| [[H4 (line)]] | wt | 227 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HOP62 (line)]] | alt | 126 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.463× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HS-578T (line)]] | alt | 154 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +13.5) | — |
| [[J82 (line)]] | alt | 87.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +15.1) | — |
| [[KATO III (line)]] | alt | 117 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.369× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 116 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[NCI-H23 (line)]] | alt | 182 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +17.0) | — |
| [[NCI-H2347 (line)]] | alt | 86.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.2) | — |
| [[Panc 03.27 (line)]] | alt | 124 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +11.8) | — |
| [[SHP-77 (line)]] | alt | 121 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.465× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SK-MEL-2 (line)]] | alt | 122 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +19.7) | — |
| [[SNU-423 (line)]] | alt | 135 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.470× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 112 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.9) | — |
| [[SW480 (line)]] | alt | 148 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.9) | — |
| [[A549 (line)]] | wt | 87.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.3) | — |
| [[C-33 A (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[CFPAC-1 (line)]] | alt | 140 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +15.7) | — |
| [[CHP-212 (line)]] | wt | 68.8 | 0 | 1 | — | [[AZD1390 (drug)]] 5 µM 0.0568× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 116 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.8) | — |
| [[HepG2_C3A (line)]] | wt | 128 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 42.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.3) | — |
| [[hTERT-HPNE (line)]] | wt | 139 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.2) | — |
| [[LoVo (line)]] | wt | 134 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 160 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 127 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +14.2) | — |
| [[PANC-1 (line)]] | alt | 184 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +15.7) | — |
| [[RKO (line)]] | wt | 187 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.446× (z -8.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 160 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.1) | — |
| [[SNU-1 (line)]] | wt | 121 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 145 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.0) | — |
| [[A-427 (line)]] | wt | 95.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 102 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 132 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8539), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOSR1]] | +0.68 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[ICE2]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ZNF621]] | +0.63 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[MATN1-AS1]] | +0.62 | +0.63 / +0.38 | both halves | 7e-05 |  |
| [[RPL7L1]] | +0.62 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[ZNF829]] | +0.62 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[FCF1]] | +0.62 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[TRMT13]] | +0.62 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ARCN1]] | +0.61 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[HELQ]] | +0.61 | +0.61 / +0.37 | both halves | 8e-05 |  |
| [[CD163L1]] | +0.61 | +0.69 / +0.46 | both halves | 2e-05 |  |
| [[NCBP2]] | +0.61 | +0.53 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNY]] | -0.68 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[RNF38]] | -0.67 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[UBE2G1]] | -0.65 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[STRN]] | -0.65 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[ABHD12]] | -0.63 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[MFSD14B]] | -0.63 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[SRPK2]] | -0.61 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[METRN]] | -0.61 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[DCUN1D4]] | -0.61 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[PPP4R1]] | -0.61 | -0.63 / -0.46 | both halves | 2e-05 |  |
| [[RANBP9]] | -0.61 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[NPEPPS]] | -0.60 | -0.56 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BRSK1]] | B | BRSK1 activity raises MYSM1's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 1.13× lower at baseline in the lines without BRSK1 | 0.093 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction -0.806). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.9, -6.6); signed map (10.3, -28.3). **Vector** length 94.1, 28.5% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.2 | +10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +19.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.0 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.2 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +0.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | +0.9 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -4.4 | -3.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.8 | -2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | -3.4 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | Myb like, SWIRM and MPN domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.1 — chr1:58,643,440-58,700,090 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1915 |
| Gene groups (HGNC) | Myb/SANT domain containing; JAMM/MPN+ metallopeptidase family |
| Reactome | 2 pathways, smallest: Metalloprotease DUBs; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VVJ2](https://www.uniprot.org/uniprotkb/Q5VVJ2) (Deubiquitinase MYSM1):

> Metalloprotease with deubiquitinase activity that plays important regulator roles in hematopoietic stem cell function, blood cell production and immune response. Participates in the normal programming of B-cell responses to antigen after the maturation process (By similarity). Within the cytoplasm, plays critical roles in the repression of innate immunity and autoimmunity. Removes 'Lys-63'-linked polyubiquitins from TRAF3 and TRAF6 complexes (By similarity). Attenuates NOD2-mediated …

**Summary**, from NCBI Gene [114803](https://www.ncbi.nlm.nih.gov/gene/114803):

> Enables deubiquitinase activity; histone binding activity; and transcription coactivator activity. Involved in chromatin remodeling; positive regulation of transcription by RNA polymerase II; and regulation of hemopoiesis. Located in nucleolus and nucleoplasm. Part of protein-containing complex. Implicated in diabetic retinopathy. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29401](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29401) · Entrez [114803](https://www.ncbi.nlm.nih.gov/gene/114803) · UniProt [Q5VVJ2](https://www.uniprot.org/uniprotkb/Q5VVJ2) · Ensembl [ENSG00000162601](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162601)

## Data

Gene col 8539: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8539); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8539, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8539]; `tensor/DDL_lfc|DDL_z.npy` [8539]; `embed/gene_vectors.npy` [8539]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8539 or target_col == 8539). Every well: [[MYSM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYSM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
