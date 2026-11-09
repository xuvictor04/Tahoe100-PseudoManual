---
symbol: "RC3H1"
type: "gene"
col: 5769
ensembl_id: "ENSG00000135870"
name: "ring finger and CCCH-type domains 1"
location: "1q25.1"
module: 231
arm: "+"
pooled_cpm: 187.28
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/231"]
generated_by: "tahoemap"
---

# RC3H1

*ring finger and CCCH-type domains 1* — 1q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.66× (z +12.7, q 4e-34, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.725× (z -8.1, q 4e-13, down in 27 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.828× (z -4.6, q 7e-04, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H1573 0.328×, SW 900 0.320×, SW48 0.246×, NCI-H460 0.440×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (C32 0.320×, A-172 0.419×, NCI-H1573 0.421×, A-427 0.495×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H460 0.334×, A-427 0.324×, AN3 CA 0.167×; ⚠ toxic; transcription drop); [[Adagrasib (drug)]] 0.5 µM in 1 line (SW 1088 0.141×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATOSA]] (+0.61, fdr 1e-05), [[CDK19]] (+0.59, fdr 1e-05), [[CERT1]] (+0.59, fdr 1e-05); moves opposite to [[RIOK1]] (-0.57, fdr 2e-05), [[B3GNTL1]] (-0.56, fdr 2e-05), [[CMSS1]] (-0.54, fdr 1e-05).
> It is in [[Module 231]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → cells under [[Ponatinib (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5769.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +12.7 | 4e-34 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +12.2 | 8e-32 | 34/48 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +9.4 | 6e-19 | 26/49 (A498, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +7.9 | 3e-13 | 38/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +7.8 | 7e-13 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +7.7 | 9e-13 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +7.3 | 3e-11 | 35/48 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +7.2 | 4e-11 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.04×** | +7.2 | 4e-11 | 32/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +6.6 | 2e-09 | 34/48 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +6.3 | 1e-08 | 35/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +6.0 | 1e-07 | 29/48 (A498, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +5.7 | 6e-07 | 29/48 (SW480, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.25×** | +5.6 | 8e-07 | 26/48 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +5.1 | 1e-05 | 29/48 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.5 | 2e-04 | 24/50 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5769.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H1573 0.328×, SW 900 0.320×, SW48 0.246×, NCI-H460 0.440×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (C32 0.320×, A-172 0.419×, NCI-H1573 0.421×, A-427 0.495×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H460 0.334×, A-427 0.324×, AN3 CA 0.167×; ⚠ toxic; transcription drop); [[Adagrasib (drug)]] 0.5 µM in 1 line (SW 1088 0.141×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.725×** | -8.1 | 4e-13 | 27/49 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.731×** | -7.6 | 9e-12 | 32/44 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.729×** | -6.6 | 9e-09 | 34/45 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.828×** | -4.6 | 7e-04 | 23/48 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 0.726× | -3.2 | 0.14 | 21/45 (AN3 CA, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.885× | -3.1 | 0.20 | 11/48 (COLO 205, CFPAC-1, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.880× | -3.0 | 0.20 | 10/48 (HCT15, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5769. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 224 | 11 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +15.4) | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -17.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 164 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +25.0) | — |
| [[SW480 (line)]] | alt | 189 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +15.5) | — |
| [[LoVo (line)]] | wt | 184 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +14.3) | — |
| [[BT-474 (line)]] | alt | 264 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.482× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 159 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +10.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 206 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +13.8) | — |
| [[NCI-H1573 (line)]] | alt | 205 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.328× (z -16.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 129 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +14.5) | — |
| [[PANC-1 (line)]] | alt | 127 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +12.0) | — |
| [[RKO (line)]] | wt | 155 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +13.5) | — |
| [[SHP-77 (line)]] | alt | 142 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 146 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 163 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.471× (z -10.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 216 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.320× (z -15.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 177 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -15.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 249 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -14.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 210 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -14.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 214 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -14.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 216 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -14.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 258 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.454× (z -9.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 188 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +14.2) | — |
| [[LS 180 (line)]] | wt | 206 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 109 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.54× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 189 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +11.2) | — |
| [[A549 (line)]] | wt | 181 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +16.0) | — |
| [[AsPC-1 (line)]] | alt | 238 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.494× (z -9.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 267 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.499× (z -8.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 152 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 142 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 118 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +8.6) | — |
| [[KATO III (line)]] | alt | 177 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 226 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.489× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 174 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.1) | — |
| [[SW 1088 (line)]] | alt | 133 | 0 | 1 | — | [[Adagrasib (drug)]] 0.5 µM 0.141× (z -8.7) |
| [[C-33 A (line)]] | alt | 164 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 312 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 195 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 131 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5769), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATOSA]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[CDK19]] | +0.59 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[CERT1]] | +0.59 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[BMPR2]] | +0.57 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[SOS1]] | +0.55 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[VAMP8]] | +0.55 | +0.44 / +0.37 | both halves | 8e-05 |  |
| [[ACOX1]] | +0.54 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[BBX]] | +0.54 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[SYNRG]] | +0.53 | +0.51 / +0.35 | both halves | 1e-04 |  |
| [[ARID4B]] | +0.53 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[KDM2A]] | +0.53 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[YPEL5]] | +0.53 | +0.40 / +0.49 | both halves | 5e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIOK1]] | -0.57 | -0.46 / -0.48 | both halves | 2e-05 | STRING 572 |
| [[B3GNTL1]] | -0.56 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[CMSS1]] | -0.54 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[TAF1A]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[COA1]] | -0.53 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[CEP83]] | -0.53 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[TMEM177]] | -0.53 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[EIF2B3]] | -0.52 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[SNHG17]] | -0.52 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[POLR1B]] | -0.51 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[TMEM241]] | -0.51 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[NLE1]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Ponatinib (drug)]] 0.05 µM | C | RC3H1's natural level lowers the cells' numbers under Ponatinib 0.05 µM (makes them more sensitive) | RC3H1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.081 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Digitoxin (drug)]] 0.05 µM | C | RC3H1's natural level raises the cells' numbers under Digitoxin 0.05 µM (protects the cells) | RC3H1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.68 | 0.287 over the table, 0.062 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Menadione (drug)]] 0.5 µM | C | RC3H1's natural level raises the cells' numbers under Menadione 0.5 µM (protects the cells) | RC3H1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62 | 0.421 over the table, 0.083 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 231]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.775). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-10.4, -44.4); signed map (-10.5, 10.1). **Vector** length 88.6, 24.9% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +9.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +5.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +1.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +0.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.1 | +0.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | -2.9 | -3.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -4.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ring finger and CCCH-type domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.1 — chr1:173,931,084-174,022,357 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA2025, roquin, RP5-1198E17.5, RNF198 |
| Gene groups (HGNC) | Ring finger proteins; Zinc fingers CCCH-type; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TC82](https://www.uniprot.org/uniprotkb/Q5TC82) (Roquin-1):

> Post-transcriptional repressor of mRNAs containing a conserved stem loop motif, called constitutive decay element (CDE), which is often located in the 3'-UTR, as in HMGXB3, ICOS, IER3, NFKBID, NFKBIZ, PPP1R10, TNF, TNFRSF4 and in many more mRNAs. Cleaves translationally inactive mRNAs harboring a stem-loop (SL), often located in their 3'-UTRs, during the early phase of inflammation in a helicase UPF1-independent manner (By similarity). Binds to CDE and promotes mRNA deadenylation and …

**Summary**, from NCBI Gene [149041](https://www.ncbi.nlm.nih.gov/gene/149041):

> This gene encodes a protein containing RING-type and C3H1-type zinc finger motifs. The encoded protein recognizes and binds to a constitutive decay element (CDE) in the 3' UTR of mRNAs, leading to mRNA deadenylation and degradation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:29434](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29434) · Entrez [149041](https://www.ncbi.nlm.nih.gov/gene/149041) · UniProt [Q5TC82](https://www.uniprot.org/uniprotkb/Q5TC82) · Ensembl [ENSG00000135870](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135870)

## Data

Gene col 5769: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5769); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5769, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5769]; `tensor/DDL_lfc|DDL_z.npy` [5769]; `embed/gene_vectors.npy` [5769]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5769 or target_col == 5769). Every well: [[RC3H1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RC3H1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
