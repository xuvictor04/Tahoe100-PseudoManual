---
symbol: "VDAC1"
type: "gene"
col: 13114
ensembl_id: "ENSG00000213585"
name: "voltage dependent anion channel 1"
location: "5q31.1"
module: 134
arm: "+"
pooled_cpm: 248.95
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# VDAC1

*voltage dependent anion channel 1* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.67× (z +11.4, q 2e-27, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.37× (z +3.8, q 0.016, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.516× (z -11.2, q 3e-26, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEKHA8]] (+0.63, fdr 1e-05), [[FAM210A]] (+0.61, fdr 1e-05), [[P4HA2]] (+0.60, fdr 7e-06); moves opposite to [[VPS72]] (-0.56, fdr 2e-05), [[LIPT1]] (-0.55, fdr 1e-05), [[ZNF140]] (-0.54, fdr 2e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13114.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.67×** | +11.4 | 2e-27 | 49/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +10.4 | 6e-23 | 43/44 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +6.6 | 7e-09 | 40/45 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **1.38×** | +3.9 | 0.015 | 36/48 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.016 | 37/48 (BT-474, AsPC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.81×** | +3.7 | 0.018 | 44/48 (CFPAC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.021 | 39/50 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.69×** | +3.3 | 0.069 | 38/47 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.086 | 38/48 (A498, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13114.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.516×** | -11.2 | 3e-26 | 46/48 (LOX-IMVI, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.612×** | -5.9 | 1e-06 | 42/48 (SK-MEL-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.674×** | -4.7 | 5e-04 | 39/48 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.703×** | -4.2 | 0.004 | 34/48 (SK-MEL-2, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.730×** | -3.8 | 0.019 | 33/48 (SK-MEL-2, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.554×** | -3.7 | 0.021 | 42/49 (BT-474, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.730×** | -3.6 | 0.025 | 31/48 (AsPC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 5 µM |  | 0.618× | -3.0 | 0.18 | 39/49 (CFPAC-1, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13114. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 336 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -17.8) |
| [[LOX-IMVI (line)]] | wt | 313 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -23.0) |
| [[SW480 (line)]] | alt | 206 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -10.0) |
| [[A498 (line)]] | wt | 227 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[AN3 CA (line)]] | alt | 240 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.90× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -9.1) |
| [[C-33 A (line)]] | alt | 270 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -15.8) |
| [[CFPAC-1 (line)]] | alt | 260 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -13.5) |
| [[HCT15 (line)]] | alt | 228 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -10.0) |
| [[HOP62 (line)]] | alt | 280 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -11.5) |
| [[LoVo (line)]] | wt | 251 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -9.3) |
| [[LS 180 (line)]] | wt | 248 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -16.1) |
| [[MIA PaCa-2 (line)]] | alt | 318 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 199 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 277 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 283 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -8.8) |
| [[A549 (line)]] | wt | 279 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[AsPC-1 (line)]] | alt | 237 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -17.8) |
| [[COLO 205 (line)]] | alt | 229 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -13.7) |
| [[Hs 766T (line)]] | wt | 264 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[HS-578T (line)]] | alt | 289 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -9.1) |
| [[HT-29 (line)]] | alt | 117 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +11.1) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 179 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H1792 (line)]] | alt | 248 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H23 (line)]] | alt | 269 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -14.9) |
| [[NCI-H2347 (line)]] | alt | 226 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +11.5) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[PANC-1 (line)]] | alt | 265 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[RPMI-7951 (line)]] | alt | 218 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -9.8) |
| [[SNU-423 (line)]] | alt | 288 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[BT-474 (line)]] | alt | 164 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -9.2) |
| [[CHP-212 (line)]] | wt | 230 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.348× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 347 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +8.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 261 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -10.9) |
| [[J82 (line)]] | alt | 279 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 194 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[RKO (line)]] | wt | 204 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -12.5) |
| [[SHP-77 (line)]] | alt | 97.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.27× (z +14.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 445 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -12.4) |
| [[SNU-1 (line)]] | wt | 197 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[SW1417 (line)]] | alt | 149 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[A-172 (line)]] | wt | 302 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 320 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 284 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 206 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 346 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 211 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13114), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHA8]] | +0.63 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[FAM210A]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[P4HA2]] | +0.60 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[TPI1]] | +0.59 | +0.59 / +0.63 | both halves | 7e-06 | STRING 561 |
| [[HK1]] | +0.58 | +0.64 / +0.57 | both halves | 8e-06 | STRING 998 |
| [[P4HA1]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[AK2]] | +0.58 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[CCDC47]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 | pathway: Protein localization |
| [[CACNB4]] | +0.57 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[CHSY1]] | +0.57 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[LNPK]] | +0.57 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[TENT4A]] | +0.56 | +0.60 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS72]] | -0.56 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[LIPT1]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[ZNF140]] | -0.54 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[GIGYF1]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[LARP7]] | -0.53 | -0.61 / -0.36 | both halves | 1e-04 |  |
| [[CHTOP]] | -0.53 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[ZNF214]] | -0.52 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[DEDD]] | -0.52 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ZNF502]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[ZNF776]] | -0.51 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[NECAP2]] | -0.51 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[ZNF19]] | -0.50 | -0.46 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises VDAC1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.660). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.3, -19.2); signed map (-39.8, 27.9). **Vector** length 83.7, 33.5% of its response variance represented; |z| ≥ 3 in 732 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +2.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.1 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +2.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.4 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[EX229 (drug)]] 0.05 µM |  | +2.1 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.9 | -11.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.0 | -0.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.0 | -3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.4 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | +1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.8 | +1.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.8 | +1.2 |

## What is on record

|  |  |
|---|---|
| Name | voltage dependent anion channel 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:133,971,871-134,004,975 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC111064, PORIN |
| Gene groups (HGNC) | Voltage dependent anion channels |
| Hallmark sets | MYC_TARGETS_V1, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 13 pathways, smallest: Mitochondrial calcium ion transport; PINK1-PRKN Mediated Mitophagy; Mitophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [P21796](https://www.uniprot.org/uniprotkb/P21796) (Non-selective voltage-gated ion channel VDAC1):

> Non-selective voltage-gated ion channel that mediates the transport of anions and cations through the mitochondrion outer membrane and plasma membrane. The channel at the outer mitochondrial membrane allows diffusion of small hydrophilic molecules; in the plasma membrane it is involved in cell volume regulation and apoptosis. It adopts an open conformation at low or zero membrane potential and a closed conformation at potentials above 30-40 mV. The open state has a weak anion selectivity …

**Summary**, from NCBI Gene [7416](https://www.ncbi.nlm.nih.gov/gene/7416):

> This gene encodes a voltage-dependent anion channel protein that is a major component of the outer mitochondrial membrane. The encoded protein facilitates the exchange of metabolites and ions across the outer mitochondrial membrane and may regulate mitochondrial functions. This protein also forms channels in the plasma membrane and may be involved in transmembrane electron transport. Alternate splicing results in multiple transcript variants. Multiple pseudogenes of this gene are found on …

**Accessions** — [HGNC:12669](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12669) · Entrez [7416](https://www.ncbi.nlm.nih.gov/gene/7416) · UniProt [P21796](https://www.uniprot.org/uniprotkb/P21796) · Ensembl [ENSG00000213585](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213585)

## Data

Gene col 13114: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13114); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13114, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13114]; `tensor/DDL_lfc|DDL_z.npy` [13114]; `embed/gene_vectors.npy` [13114]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13114 or target_col == 13114). Every well: [[VDAC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VDAC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
