---
symbol: "CALM1"
type: "gene"
col: 12637
ensembl_id: "ENSG00000198668"
name: "calmodulin 1"
location: "14q32.11"
module: 81
arm: "+"
pooled_cpm: 278.1
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# CALM1

*calmodulin 1* — 14q32.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.84× (z +11.6, q 4e-28, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Mebendazole (drug)]] 5 µM: 1.51× (z +3.4, q 0.038, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.410× (z -4.0, q 0.032, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MARCHF3]] (+0.65, fdr 1e-05), [[STC1]] (+0.63, fdr 1e-05), [[SH3BGRL3]] (+0.62, fdr 1e-05); moves opposite to [[SMAD1]] (-0.56, fdr 1e-04), [[MRRF]] (-0.54, fdr 2e-05), [[COMT]] (-0.53, fdr 2e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KRT15]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12637.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **3.84×** | +11.6 | 4e-28 | 49/49 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **3.42×** | +10.2 | 7e-22 | 44/44 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.29×** | +7.1 | 2e-10 | 47/48 (hTERT-HPNE, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.29×** | +6.9 | 1e-09 | 40/47 (MIA PaCa-2, HT-29, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **2.18×** | +6.7 | 3e-09 | 46/48 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.30×** | +6.6 | 3e-09 | 41/45 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.88×** | +5.4 | 5e-06 | 45/48 (SHP-77, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.52×** | +3.6 | 0.021 | 32/48 (HepG2/C3A, hTERT-HPNE, …) | all doses, stronger at high dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.51×** | +3.4 | 0.038 | 35/48 (NCI-H1792, CFPAC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.075 | 30/48 (MIA PaCa-2, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.077 | 28/48 (RKO, SK-MEL-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.46×** | +3.1 | 0.077 | 30/50 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.077 | 38/48 (SW1417, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12637.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.410×** | -4.0 | 0.032 | 40/49 (RKO, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.602×** | -3.8 | 0.032 | 42/50 (NCI-H460, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.433×** | -3.8 | 0.032 | 36/48 (LS 180, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.749×** | -3.4 | 0.095 | 40/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.498× | -3.1 | 0.20 | 37/50 (H4, A-172, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.61 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12637. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 151 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.98× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[COLO 205 (line)]] | alt | 110 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +15.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 255 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.15× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[A-427 (line)]] | wt | 210 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.296× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 106 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.47× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[AsPC-1 (line)]] | alt | 182 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[C32 (line)]] | wt | 239 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H1792 (line)]] | alt | 154 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +14.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 254 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | [[Trametinib (drug)]] 5 µM 0.280× (z -8.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SNU-423 (line)]] | alt | 163 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[A549 (line)]] | wt | 263 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[HCT15 (line)]] | alt | 275 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[Hs 766T (line)]] | wt | 157 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[HT-29 (line)]] | alt | 167 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 369 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.29× (z +8.7) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[J82 (line)]] | alt | 291 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[LoVo (line)]] | wt | 254 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.94× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[LS 180 (line)]] | wt | 341 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[Panc 03.27 (line)]] | alt | 252 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[PANC-1 (line)]] | alt | 208 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[RPMI-7951 (line)]] | alt | 161 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[SHP-77 (line)]] | alt | 188 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[SNU-1 (line)]] | wt | 185 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.27× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[SW1417 (line)]] | alt | 274 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[SW48 (line)]] | wt | 348 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[SW480 (line)]] | alt | 227 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.69× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[A498 (line)]] | wt | 153 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[C-33 A (line)]] | alt | 81.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.63× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[CFPAC-1 (line)]] | alt | 378 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[CHP-212 (line)]] | wt | 106 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.61× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[HEC-1-A (line)]] | alt | 249 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H2030 (line)]] | alt | 367 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H2347 (line)]] | alt | 415 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[RKO (line)]] | wt | 246 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 267 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[SW 900 (line)]] | alt | 212 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[A-172 (line)]] | wt | 431 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 596 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 288 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 169 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 790 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 328 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 543 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 342 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 457 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12637), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARCHF3]] | +0.65 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[STC1]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SH3BGRL3]] | +0.62 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[MYADM]] | +0.62 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[TIMP1]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |
| [[LRRC8C]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[PPFIBP1]] | +0.60 | +0.55 / +0.48 | both halves | 2e-05 | pathway: Neuronal System |
| [[RAC2]] | +0.60 | +0.48 / +0.53 | both halves | 2e-05 | same gene group; pathway: Beta-catenin independent WNT signaling |
| [[SMTN]] | +0.59 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[ZCCHC24]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[VIM]] | +0.58 | +0.64 / +0.38 | both halves | 6e-05 | pathway: Muscle contraction |
| [[ABTB3]] | +0.57 | +0.44 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMAD1]] | -0.56 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[MRRF]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[COMT]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 | pathway: Neuronal System |
| [[MTPAP]] | -0.51 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[TMEM268]] | -0.50 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[MAIP1]] | -0.50 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[LINC02904]] | -0.49 | -0.40 / -0.30 | both halves | 2e-04 |  |
| [[LUC7L2]] | -0.49 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[DUS3L]] | -0.49 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[ABCC6]] | -0.49 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[LARP1]] | -0.49 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[TMEM69]] | -0.48 | -0.46 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT15]] | B | KRT15 activity raises CALM1's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 1.50× lower at baseline in the lines without KRT15 | 0.060 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[KLF12]] | B | KLF12 activity raises CALM1's level | lines that do not express KLF12 (9) vs lines expressing it (41) | 1.66× lower at baseline in the lines without KLF12 | 0.074 | ⚠ within organs, on part of the lines; also absent: RHOBTB1, ZC3H12C, GNAI1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.2, 2.1); signed map (2.9, 48.7). **Vector** length 116, 54.2% of its response variance represented; |z| ≥ 3 in 1,032 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.7 | +7.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +3.5 | +5.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +3.4 | +6.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | +3.2 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.0 | +2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +1.9 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +2.5 | +2.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | -7.8 | +6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -7.0 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | -6.8 | +11.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -6.6 | +2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | +0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.2 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.0 | -1.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.9 | -3.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.5 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | calmodulin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.11 — chr14:90,396,502-90,408,268 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAMI, PHKD, DD132, PHKD1; previously CALML2 |
| Gene groups (HGNC) | Receptor ligands; EF-hand domain containing; Phosphorylase kinase subunits; UBR4 complex |
| Hallmark sets | COMPLEMENT |
| Reactome | 136 pathways, smallest: Cam-PDE 1 activation; Loss of phosphorylation of MECP2 at T308; Activation of RAC1 downstream of NMDARs |
| Matched by | ensembl_id |

**Function**, from UniProt [P0DP23](https://www.uniprot.org/uniprotkb/P0DP23) (Calmodulin-1):

> Calmodulin acts as part of a calcium signal transduction pathway by mediating the control of a large number of enzymes, ion channels, aquaporins and other proteins through calcium-binding. Calcium-binding is required for the activation of calmodulin. Among the enzymes to be stimulated by the calmodulin-calcium complex are a number of protein kinases, such as myosin light-chain kinases and calmodulin-dependent protein kinase type II (CaMK2), and phosphatases. Together with CCP110 and centrin, is …

**Summary**, from NCBI Gene [801](https://www.ncbi.nlm.nih.gov/gene/801):

> This gene encodes one of three calmodulin proteins which are members of the EF-hand calcium-binding protein family. Calcium-induced activation of calmodulin regulates and modulates the function of cardiac ion channels. Two pseudogenes have been identified on chromosome 7 and X. Multiple transcript variants encoding different isoforms have been found for this gene.A missense mutation in the CALM1 gene has been associated with ventricular tachycardia.[provided by RefSeq, May 2020]

**Accessions** — [HGNC:1442](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1442) · Entrez [801](https://www.ncbi.nlm.nih.gov/gene/801) · UniProt [P0DP23](https://www.uniprot.org/uniprotkb/P0DP23) · Ensembl [ENSG00000198668](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198668)

## Data

Gene col 12637: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12637); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12637, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12637]; `tensor/DDL_lfc|DDL_z.npy` [12637]; `embed/gene_vectors.npy` [12637]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12637 or target_col == 12637). Every well: [[CALM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CALM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
