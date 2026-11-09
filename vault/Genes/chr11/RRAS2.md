---
symbol: "RRAS2"
type: "gene"
col: 5479
ensembl_id: "ENSG00000133818"
name: "RAS related 2"
location: "11p15.2"
module: 163
arm: "+"
pooled_cpm: 142.56
n_lines_expressing: 48
n_dd_up: 24
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# RRAS2

*RAS related 2* — 11p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.08× (z +12.9, q 3e-35, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.492× (z -12.6, q 2e-33, down in 41 of 47 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A-427 0.203×, NCI-H2347 0.218×, HEC-1-A 0.275×, Hs 766T 0.180×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (AN3 CA 0.0929×, NCI-H2347 0.225×, SW1417 0.222×, J82 0.375×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.308×, SNU-423 0.353×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGPP1]] (+0.57, fdr 1e-05), [[SPON1-AS1]] (+0.57, fdr 3e-05, ⚠ read-through risk), [[PROSER2]] (+0.54, fdr 3e-05), [[CYTH3]] (+0.51, fdr 1e-05); moves opposite to [[RLIM]] (-0.50, fdr 2e-05), [[SF3B1]] (-0.48, fdr 3e-05), [[KIAA0586]] (-0.44, fdr 1e-04).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PROSER2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5479.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.08×** | +12.9 | 3e-35 | 44/46 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.68×** | +9.2 | 1e-17 | 39/46 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.65×** | +8.8 | 2e-16 | 42/46 (SNU-423, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.42×** | +8.7 | 4e-16 | 40/47 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +8.0 | 1e-13 | 30/46 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +7.3 | 3e-11 | 36/46 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.49×** | +7.0 | 2e-10 | 38/46 (CFPAC-1, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.7 | 7e-07 | 24/47 (NCI-H23, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.36×** | +5.2 | 1e-05 | 28/45 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.34×** | +5.1 | 2e-05 | 33/46 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.78×** | +4.7 | 1e-04 | 28/47 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.31×** | +4.7 | 1e-04 | 29/46 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.66×** | +4.1 | 0.002 | 31/46 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.32×** | +3.9 | 0.003 | 26/45 (NCI-H1573, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.9 | 0.003 | 19/46 (SNU-423, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.005 | 21/46 (hTERT-HPNE, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.012 | 23/45 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.52×** | +3.4 | 0.018 | 23/47 (LoVo, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5479.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A-427 0.203×, NCI-H2347 0.218×, HEC-1-A 0.275×, Hs 766T 0.180×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (AN3 CA 0.0929×, NCI-H2347 0.225×, SW1417 0.222×, J82 0.375×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.308×, SNU-423 0.353×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.492×** | -12.6 | 2e-33 | 41/47 (AN3 CA, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.493×** | -12.0 | 7e-31 | 36/42 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.651×** | -7.0 | 4e-10 | 25/43 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.707×** | -6.2 | 1e-07 | 30/46 (SW 1271, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.834× | -3.2 | 0.14 | 19/46 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.839× | -3.1 | 0.16 | 17/46 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.835× | -3.1 | 0.16 | 20/46 (NCI-H2347, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5479. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 62.8 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -14.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 143 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.427× (z -12.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 207 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -11.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 189 | 1 (1 ⚠) | 3 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.04× (z +8.5) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.364× (z -11.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 242 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -13.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 90.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +14.8) | — |
| [[SNU-423 (line)]] | alt | 197 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.353× (z -11.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 169 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.492× (z -9.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 142 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.96× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +11.7) | — |
| [[CFPAC-1 (line)]] | alt | 147 | 2 | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.00× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -8.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 179 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -16.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 187 | 1 (1 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.50× (z +8.6) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.180× (z -15.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 69.2 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.03× (z +15.4) | — |
| [[LOX-IMVI (line)]] | wt | 221 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.299× (z -11.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 155 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.2) | — |
| [[NCI-H2347 (line)]] | alt | 258 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -17.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 128 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +11.8) | — |
| [[SW1417 (line)]] | alt | 203 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -15.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 128 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -17.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 149 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -9.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 47.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +10.5) | — |
| [[H4 (line)]] | wt | 118 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 238 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -9.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 95.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 111 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 162 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -8.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 124 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +14.8) | — |
| [[SNU-1 (line)]] | wt | 210 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -11.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -9.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 157 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0929× (z -18.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.388× (z -9.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -10.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 127 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 65.5 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.74× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 215 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -12.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 182 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -11.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 82.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.4) | — |
| [[SW 1271 (line)]] | alt | 169 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0736× (z -14.2) ⚠ transcription drop |
| [[C32 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 98.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5479), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGPP1]] | +0.57 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SPON1-AS1]] | +0.57 | +0.45 / +0.66 | both halves | 3e-05 | ⚠ **readthrough risk**: SPON1-AS1 lies 4.2 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[PROSER2]] | +0.54 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[CYTH3]] | +0.51 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[TSC22D2]] | +0.51 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[HINT1]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[PGM5P2]] | +0.51 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[PROSER2-AS1]] | +0.50 | +0.31 / +0.52 | both halves | 2e-04 |  |
| [[MIR193BHG]] | +0.49 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[RNF38]] | +0.49 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[MARCHF5]] | +0.48 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[PGM5P2-1]] | +0.48 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[FAM241A]] | +0.46 | +0.38 / +0.46 | both halves | 6e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RLIM]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[SF3B1]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[KIAA0586]] | -0.44 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[CCDC7]] | -0.43 | -0.26 / -0.46 | both halves | 3e-04 |  |
| [[INTS3]] | -0.43 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[SF3A3]] | -0.42 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[EXTL2]] | -0.42 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[FOS]] | -0.42 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[DBT]] | -0.41 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[ARCN1]] | -0.41 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[RBM22]] | -0.41 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[LINC01473]] | -0.41 | -0.35 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PROSER2]] | B | PROSER2 activity raises RRAS2's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 1.70× lower at baseline in the lines without PROSER2 | 0.003 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.442). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.9, 37.0); signed map (10.3, 21.0). **Vector** length 93.4, 28.4% of its response variance represented; |z| ≥ 3 in 1,111 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +7.0 | +8.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.6 | +5.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.3 | +5.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.3 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +5.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.4 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +3.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -1.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.1 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -1.8 | -2.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.5 | -3.1 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | RAS related 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.2 — chr11:14,277,922-14,364,506 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TC21 |
| Gene groups (HGNC) | RAS type GTPase family |
| Reactome | 4 pathways, smallest: RND1 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [P62070](https://www.uniprot.org/uniprotkb/P62070) (Ras-related protein R-Ras2):

> GTP-binding protein with GTPase activity, involved in the regulation of MAPK signaling pathway and thereby controlling multiple cellular processes. Regulates craniofacial development.

**Summary**, from NCBI Gene [22800](https://www.ncbi.nlm.nih.gov/gene/22800):

> This gene encodes a member of the R-Ras subfamily of Ras-like small GTPases. The encoded protein associates with the plasma membrane and may function as a signal transducer. This protein may play an important role in activating signal transduction pathways that control cell proliferation. Mutations in this gene are associated with the growth of certain tumors. Pseudogenes of this gene are found on chromosomes 1 and 2. Alternate splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:17271](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17271) · Entrez [22800](https://www.ncbi.nlm.nih.gov/gene/22800) · UniProt [P62070](https://www.uniprot.org/uniprotkb/P62070) · Ensembl [ENSG00000133818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133818)

## Data

Gene col 5479: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5479); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5479, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5479]; `tensor/DDL_lfc|DDL_z.npy` [5479]; `embed/gene_vectors.npy` [5479]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5479 or target_col == 5479). Every well: [[RRAS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRAS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
