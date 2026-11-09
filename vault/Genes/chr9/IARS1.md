---
symbol: "IARS1"
type: "gene"
col: 12175
ensembl_id: "ENSG00000196305"
name: "isoleucyl-tRNA synthetase 1"
location: "9q22.31"
module: 63
arm: "+"
pooled_cpm: 256.24
n_lines_expressing: 50
n_dd_up: 44
n_dd_down: 12
n_dd_up_clean: 40
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# IARS1

*isoleucyl-tRNA synthetase 1* — 9q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (4 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 1.67× (z +11.1, q 1e-25, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.581× (z -8.1, q 2e-13, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPA9]] (+0.89, fdr 7e-06), [[XPOT]] (+0.89, fdr 7e-06), [[MTHFD2]] (+0.87, fdr 7e-06); moves opposite to [[H2AJ]] (-0.52, fdr 1e-05), [[POLR2L]] (-0.50, fdr 2e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ASNSP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12175.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **1.67×** | +11.1 | 1e-25 | 46/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +10.3 | 9e-23 | 44/47 (COLO 205, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.95×** | +10.3 | 9e-23 | 46/48 (LOX-IMVI, C32, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.44×** | +10.0 | 1e-21 | 40/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **3.35×** | +9.8 | 1e-20 | 46/49 (RKO, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.81×** | +9.2 | 4e-18 | 46/48 (SW 900, COLO 205, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **1.78×** | +8.9 | 4e-17 | 45/48 (SHP-77, C32, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +8.5 | 1e-15 | 40/48 (C32, Panc 03.27, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.78×** | +8.4 | 3e-15 | 45/48 (C32, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.41×** | +7.4 | 6e-12 | 36/49 (SK-MEL-2, COLO 205, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.40×** | +7.3 | 1e-11 | 38/48 (LOX-IMVI, LoVo, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.59×** | +7.2 | 2e-11 | 41/48 (LOX-IMVI, SHP-77, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.59×** | +7.2 | 3e-11 | 41/47 (C32, SHP-77, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.58×** | +7.1 | 5e-11 | 40/48 (Panc 03.27, C-33 A, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.30×** | +5.7 | 4e-07 | 30/49 (SNU-1, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.00×** | +5.6 | 6e-07 | 39/48 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.97×** | +5.5 | 1e-06 | 40/48 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12175.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.581×** | -8.1 | 2e-13 | 33/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.639×** | -7.0 | 8e-10 | 38/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.731×** | -6.8 | 3e-09 | 31/48 (PANC-1, KATO III, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.649×** | -6.2 | 7e-08 | 36/47 (LoVo, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.779×** | -5.5 | 5e-06 | 28/48 (HT-29, COLO 205, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.710×** | -5.3 | 8e-06 | 33/48 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.755×** | -4.4 | 9e-04 | 30/49 (RPMI-7951, NCI-H23, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.826×** | -4.1 | 0.002 | 24/49 (RKO, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.773×** | -4.0 | 0.003 | 26/49 (HT-29, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.773×** | -4.0 | 0.003 | 26/48 (HS-578T, Panc 03.27, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.801×** | -3.5 | 0.028 | 26/48 (SW 1088, NCI-H1573, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.859× | -3.3 | 0.048 | 19/48 (H4, KATO III, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.861× | -3.2 | 0.052 | 16/48 (HT-29, NCI-H2347, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.815×** | -3.2 | 0.058 | 21/47 (LOX-IMVI, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12175. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 311 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -24.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.259× (z -17.6) |
| [[SW480 (line)]] | alt | 350 | 5 (2 ⚠) | 4 (1 ⚠) | [[Artesunate (drug)]] 5 µM 1.92× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -15.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -9.7) |
| [[LoVo (line)]] | wt | 381 | 2 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.40× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -14.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.289× (z -13.5) |
| [[HT-29 (line)]] | alt | 447 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -19.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.279× (z -13.0) |
| [[Panc 03.27 (line)]] | alt | 115 | 7 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.51× (z +12.1) ⚠ toxic · without an alert: [[5-Azacytidine (drug)]] 5 µM 3.02× (z +11.1) | — |
| [[A498 (line)]] | wt | 436 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.40× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -15.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -12.8) |
| [[C32 (line)]] | wt | 116 | 6 (1 ⚠) | 0 | [[Artesunate (drug)]] 5 µM 2.79× (z +12.7) | — |
| [[KATO III (line)]] | alt | 475 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -19.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.146× (z -17.9) |
| [[SHP-77 (line)]] | alt | 201 | 6 (1 ⚠) | 0 | [[Artesunate (drug)]] 5 µM 2.13× (z +12.7) | — |
| [[SNU-1 (line)]] | wt | 389 | 2 | 4 (2 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.49× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.370× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.402× (z -9.0) |
| [[COLO 205 (line)]] | alt | 156 | 5 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 7.53× (z +15.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.55× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 167 | 5 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.06× (z +10.7) ⚠ unreliable plate only · without an alert: [[5-Azacytidine (drug)]] 5 µM 2.86× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 264 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +10.5) | — |
| [[A-172 (line)]] | wt | 216 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.65× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.257× (z -12.1) |
| [[H4 (line)]] | wt | 276 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -15.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.367× (z -9.8) |
| [[RKO (line)]] | wt | 850 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.64× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -16.9) |
| [[AsPC-1 (line)]] | alt | 112 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.74× (z +10.1) ⚠ toxic · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.49× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 260 | 3 (1 ⚠) | 0 | [[Artesunate (drug)]] 5 µM 2.23× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 132 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.80× (z +11.1) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 8.98× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 216 | 3 (1 ⚠) | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.40× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 324 | 3 (1 ⚠) | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.39× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 181 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 7.13× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 216 | 3 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.32× (z +8.8) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 150 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.06× (z +10.8) | — |
| [[SW48 (line)]] | wt | 455 | 2 | 1 (1 ⚠) | [[Artesunate (drug)]] 0.5 µM 2.49× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.363× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 219 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -13.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[BT-474 (line)]] | alt | 124 | 2 | 0 | [[Artesunate (drug)]] 5 µM 2.12× (z +9.8) | — |
| [[J82 (line)]] | alt | 336 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.09× (z +9.5) | [[Selinexor (drug)]] 5 µM 0.599× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 302 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -18.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.339× (z -12.5) |
| [[C-33 A (line)]] | alt | 237 | 1 | 0 | [[5-Azacytidine (drug)]] 5 µM 2.79× (z +10.3) | — |
| [[HCT15 (line)]] | alt | 341 | 1 | 0 | [[Artesunate (drug)]] 5 µM 2.31× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 181 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -10.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.07× (z +9.6) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 144 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.11× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 220 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.78× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 179 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 176 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 261 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 225 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 171 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 338 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 305 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12175), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPA9]] | +0.89 | +0.88 / +0.89 | both halves | 7e-06 | same gene group; pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 541 |
| [[XPOT]] | +0.89 | +0.87 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 654 |
| [[MTHFD2]] | +0.87 | +0.86 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[AARS1]] | +0.87 | +0.84 / +0.88 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 980 |
| [[YARS1]] | +0.87 | +0.83 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 966 |
| [[PSAT1]] | +0.86 | +0.85 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 440 |
| [[MARS1]] | +0.85 | +0.86 / +0.83 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 999 |
| [[GARS1]] | +0.84 | +0.86 / +0.83 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 970 |
| [[ASNS]] | +0.83 | +0.84 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 804 |
| [[NARS1]] | +0.83 | +0.74 / +0.82 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 965 |
| [[TARS1]] | +0.82 | +0.79 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 913 |
| [[PHGDH]] | +0.81 | +0.83 / +0.79 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H2AJ]] | -0.52 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[POLR2L]] | -0.50 | -0.47 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASNSP1]] | B | ASNSP1 activity raises IARS1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.31× lower at baseline in the lines without ASNSP1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[PSAT1]] | B | PSAT1 activity raises IARS1's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.73× lower at baseline in the lines without PSAT1 | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[SMAD3]] | B | SMAD3 activity lowers IARS1's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 1.34× higher at baseline in the lines without SMAD3 | 0.036 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[ULBP1]] | B | ULBP1 activity raises IARS1's level | lines that do not express ULBP1 (15) vs lines expressing it (35) | 1.32× lower at baseline in the lines without ULBP1 | 0.052 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ANK2]] | B | ANK2 activity raises IARS1's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.31× lower at baseline in the lines without ANK2 | 0.066 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[MTHFD2]] | C | MTHFD2's natural level weakens IARS1's drug response | MTHFD2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.68, reverse -0.05; direction clear | 0.015 | ⚠ tissue can mimic it; precision caveat |
| [[COX7A2L]] | C | COX7A2L's natural level weakens IARS1's drug response | COX7A2L's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.12; direction not clear | 0.046 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[XPOT]] | C | XPOT's natural level weakens IARS1's drug response | XPOT's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.28; direction not clear | 0.064 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TXNDC12]] | C | TXNDC12's natural level weakens IARS1's drug response | TXNDC12's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.05; direction not clear | 0.074 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.893). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.4, 47.5); signed map (-13.7, 24.2). **Vector** length 166, 68.3% of its response variance represented; |z| ≥ 3 in 1,826 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.74 to 16); *mTORC1 signaling* (hallmark, mean cos +0.70 to 20); *Response of EIF2AK1 (HRI) to heme deficiency* (reactome, mean cos +0.69 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +12.1 | +10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.2 | +8.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +8.5 | +7.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +8.4 | +7.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +8.3 | +10.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +7.7 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +7.3 | +5.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -10.6 | -8.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.9 | -7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -8.5 | -6.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -7.8 | -6.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.2 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.1 | -5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -5.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.0 | -4.4 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | isoleucyl-tRNA synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.31 — chr9:92,210,207-92,293,854 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ILRS; previously IARS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class I; MicroRNA protein coding host genes; Small nucleolar RNA protein coding host genes |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, MYC_TARGETS_V1 |
| Reactome | 7 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; Transcriptional and post-translational regulation of MITF-M expression and activity |
| Matched by | ensembl_id |

**Function**, from UniProt [P41252](https://www.uniprot.org/uniprotkb/P41252) (Isoleucine--tRNA ligase, cytoplasmic):

> Catalyzes the specific attachment of an amino acid to its cognate tRNA in a 2 step reaction: the amino acid (AA) is first activated by ATP to form AA-AMP and then transferred to the acceptor end of the tRNA.

**Summary**, from NCBI Gene [3376](https://www.ncbi.nlm.nih.gov/gene/3376):

> Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Isoleucine-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family and has been identified as a target of autoantibodies in the autoimmune disease polymyositis/dermatomyositis. Alternatively …

**Accessions** — [HGNC:5330](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5330) · Entrez [3376](https://www.ncbi.nlm.nih.gov/gene/3376) · UniProt [P41252](https://www.uniprot.org/uniprotkb/P41252) · Ensembl [ENSG00000196305](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196305)

## Data

Gene col 12175: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12175); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12175, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12175]; `tensor/DDL_lfc|DDL_z.npy` [12175]; `embed/gene_vectors.npy` [12175]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12175 or target_col == 12175). Every well: [[IARS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IARS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
