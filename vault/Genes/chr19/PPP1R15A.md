---
symbol: "PPP1R15A"
type: "gene"
col: 1477
ensembl_id: "ENSG00000087074"
name: "protein phosphatase 1 regulatory subunit 15A"
location: "19q13.2"
module: 93
arm: "+"
pooled_cpm: 227.0
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 13
n_dd_up_clean: 22
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# PPP1R15A

*protein phosphatase 1 regulatory subunit 15A* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 12.1× (z +33.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Carbidopa (monohydrate) (drug)]] 0.05 µM: 0.570× (z -5.4, q 5e-05, down in 47 of 49 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.585× (z -5.1, q 6e-05, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RSRC2]] (+0.68, fdr 7e-06), [[MAFF]] (+0.67, fdr 7e-06), [[ATF3]] (+0.64, fdr 7e-06); moves opposite to [[NUP93]] (-0.58, fdr 2e-05), [[TMEM248]] (-0.57, fdr 1e-05), [[WDR5]] (-0.57, fdr 4e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CRYM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1477.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **12.1×** | +33.0 | 0e+00 | 48/48 (AsPC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **8.54×** | +19.6 | 0e+00 | 47/48 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.25×** | +17.4 | 0e+00 | 47/48 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **4.23×** | +13.7 | 1e-40 | 47/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.31×** | +11.4 | 7e-28 | 48/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **3.04×** | +10.6 | 4e-24 | 46/48 (A-427, SW480, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.82×** | +9.9 | 5e-21 | 48/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.64×** | +8.9 | 6e-17 | 46/47 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.28×** | +8.3 | 8e-15 | 48/49 (NCI-H1573, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.24×** | +7.6 | 1e-12 | 41/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.13×** | +7.2 | 3e-11 | 46/48 (SK-MEL-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.04×** | +6.5 | 3e-09 | 43/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.03×** | +6.5 | 4e-09 | 41/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.88×** | +5.8 | 3e-07 | 46/48 (A498, HCT15, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.60×** | +4.5 | 3e-04 | 38/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.57×** | +4.0 | 0.003 | 31/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +3.8 | 0.005 | 34/48 (A-427, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.12×** | +3.7 | 0.006 | 29/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1477.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.570×** | -5.4 | 5e-05 | 47/49 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.578×** | -5.2 | 5e-05 | 47/49 (SNU-423, Hs 766T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.585×** | -5.1 | 6e-05 | 43/48 (LOX-IMVI, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.608×** | -4.8 | 3e-04 | 36/48 (LOX-IMVI, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.599×** | -4.7 | 3e-04 | 34/48 (AsPC-1, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~11% here); position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.712×** | -4.5 | 7e-04 | 44/48 (SW480, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.654×** | -4.1 | 0.004 | 33/48 (LOX-IMVI, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.744×** | -3.9 | 0.007 | 42/48 (SHP-77, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.676×** | -3.6 | 0.019 | 30/48 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.503×** | -3.4 | 0.034 | 37/49 (AsPC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.708×** | -3.2 | 0.076 | 30/48 (LOX-IMVI, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.720×** | -3.1 | 0.080 | 30/48 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[Pemetrexed (drug)]] 0.5 µM |  | **0.726×** | -3.1 | 0.094 | 36/47 (A549, J82, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1477. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 159 | 15 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +26.4) | — |
| [[KATO III (line)]] | alt | 311 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.21× (z +26.5) | — |
| [[AsPC-1 (line)]] | alt | 273 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +37.1) | — |
| [[LoVo (line)]] | wt | 202 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +32.0) | — |
| [[LOX-IMVI (line)]] | wt | 317 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +20.5) | — |
| [[NCI-H1573 (line)]] | alt | 178 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +26.1) | — |
| [[SW 900 (line)]] | alt | 241 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.5× (z +34.2) | — |
| [[BT-474 (line)]] | alt | 182 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +25.0) | — |
| [[LS 180 (line)]] | wt | 184 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.2× (z +29.1) | — |
| [[PANC-1 (line)]] | alt | 117 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +31.5) | — |
| [[RKO (line)]] | wt | 290 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +19.2) | — |
| [[SW480 (line)]] | alt | 166 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +19.5) | — |
| [[A-427 (line)]] | wt | 118 | 7 | 0 | [[Auranofin (drug)]] 5 µM 8.42× (z +18.8) | — |
| [[HEC-1-A (line)]] | alt | 317 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +28.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 151 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +25.9) | — |
| [[SK-MEL-2 (line)]] | alt | 147 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.85× (z +24.9) | — |
| [[SNU-1 (line)]] | wt | 255 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +22.5) | — |
| [[SW48 (line)]] | wt | 125 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +21.4) | — |
| [[A-172 (line)]] | wt | 188 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +26.6) | — |
| [[A498 (line)]] | wt | 262 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.4× (z +31.0) | — |
| [[A549 (line)]] | wt | 367 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +27.4) | — |
| [[C32 (line)]] | wt | 179 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.9× (z +26.1) | — |
| [[H4 (line)]] | wt | 292 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +21.6) | — |
| [[J82 (line)]] | alt | 260 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +29.9) | — |
| [[NCI-H1792 (line)]] | alt | 217 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +25.3) | — |
| [[SNU-423 (line)]] | alt | 240 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +30.4) | — |
| [[SW1417 (line)]] | alt | 490 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +23.3) | — |
| [[HepG2_C3A (line)]] | wt | 176 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.24× (z +23.1) | — |
| [[Hs 766T (line)]] | wt | 188 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +26.5) | — |
| [[HS-578T (line)]] | alt | 306 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +32.2) | — |
| [[HT-29 (line)]] | alt | 380 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.85× (z +26.1) | — |
| [[NCI-H2030 (line)]] | alt | 219 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +20.9) | — |
| [[NCI-H2347 (line)]] | alt | 250 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +22.3) | — |
| [[Panc 03.27 (line)]] | alt | 222 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.57× (z +23.8) | — |
| [[AN3 CA (line)]] | alt | 124 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +18.7) | — |
| [[HOP62 (line)]] | alt | 206 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +26.1) | — |
| [[hTERT-HPNE (line)]] | wt | 270 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.1× (z +35.2) | — |
| [[NCI-H23 (line)]] | alt | 107 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.48× (z +20.9) | — |
| [[RPMI-7951 (line)]] | alt | 374 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.49× (z +23.6) | — |
| [[C-33 A (line)]] | alt | 128 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.56× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 387 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +23.7) | — |
| [[CHP-212 (line)]] | wt | 152 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +16.1) | — |
| [[COLO 205 (line)]] | alt | 200 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.8× (z +20.4) | — |
| [[HCT15 (line)]] | alt | 250 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +17.1) | — |
| [[SHP-77 (line)]] | alt | 101 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +13.9) | — |
| [[SW 1088 (line)]] | alt | 217 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +15.9) | — |
| [[SW 1271 (line)]] | alt | 191 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +16.2) | — |
| [[NCI-H2122 (line)]] | alt | 348 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 238 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 117 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1477), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSRC2]] | +0.68 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MAFF]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 418 |
| [[ATF3]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 896 |
| [[NFKBIB]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[SQSTM1]] | +0.60 | +0.55 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[RNF103-CHMP3]] | +0.60 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ATF4]] | +0.60 | +0.65 / +0.57 | both halves | 1e-05 | pathway: Response of EIF2AK1 (HRI) to heme deficiency; STRING 979 |
| [[MED29]] | +0.60 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[GADD45B]] | +0.58 | +0.61 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 642 |
| [[JUN]] | +0.57 | +0.67 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA; STRING 680 |
| [[BRD2]] | +0.57 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[LURAP1L-AS1]] | +0.57 | +0.55 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP93]] | -0.58 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[TMEM248]] | -0.57 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[WDR5]] | -0.57 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[TUFM]] | -0.55 | -0.52 / -0.41 | both halves | 4e-05 | STRING 498 |
| [[COLGALT1]] | -0.55 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[ELAVL1]] | -0.54 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[MFSD14B]] | -0.54 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[RPA1]] | -0.54 | -0.42 / -0.49 | both halves | 4e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[MED14]] | -0.54 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[CASP2]] | -0.53 | -0.48 / -0.42 | both halves | 4e-05 | same gene group |
| [[ATP5F1B]] | -0.53 | -0.44 / -0.46 | both halves | 3e-05 | STRING 490 |
| [[BRI3BP]] | -0.53 | -0.48 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRYM]] | B | CRYM activity raises PPP1R15A's level | lines that do not express CRYM (12) vs lines expressing it (38) | 1.60× lower at baseline in the lines without CRYM | 0.011 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |
| [[LACC1]] | B | LACC1 activity raises PPP1R15A's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.67× lower at baseline in the lines without LACC1 | 0.021 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[SLFN5]] | B | SLFN5 activity raises PPP1R15A's level | lines that do not express SLFN5 (11) vs lines expressing it (39) | 1.43× lower at baseline in the lines without SLFN5 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.451). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.6, -3.9); signed map (14.8, -3.0). **Vector** length 113, 51.0% of its response variance represented; |z| ≥ 3 in 1,384 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.2 | +10.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.1 | +7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.5 | +13.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +17.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.6 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.6 | +4.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +3.5 | +0.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.3 | -0.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.9 | -3.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.3 | -4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | +9.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | +6.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.4 | +0.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.1 | -1.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.9 | +1.0 |
|  | [[vincristine (drug)]] 0.05 µM |  | -2.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 15A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:48,872,212-48,876,059 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GADD34 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Hallmark sets | TGF_BETA_SIGNALING, KRAS_SIGNALING_UP, HYPOXIA, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY, MTORC1_SIGNALING |
| Reactome | 7 pathways, smallest: Response of EIF2AK1 (HRI) to heme deficiency; Downregulation of TGF-beta receptor signaling; TGF-beta receptor signaling activates SMADs |
| Matched by | ensembl_id |

**Function**, from UniProt [O75807](https://www.uniprot.org/uniprotkb/O75807) (Protein phosphatase 1 regulatory subunit 15A):

> Recruits the serine/threonine-protein phosphatase PPP1CA to prevents excessive phosphorylation of the translation initiation factor eIF-2A/EIF2S1, thereby reversing the shut-off of protein synthesis initiated by stress-inducible kinases and facilitating recovery of cells from stress. Down-regulates the TGF-beta signaling pathway by promoting dephosphorylation of TGFB1 by PP1. May promote apoptosis by inducing p53/TP53 phosphorylation on 'Ser-15'. Plays an essential role in autophagy by tuning …

**Summary**, from NCBI Gene [23645](https://www.ncbi.nlm.nih.gov/gene/23645):

> This gene is a member of a group of genes whose transcript levels are increased following stressful growth arrest conditions and treatment with DNA-damaging agents. The induction of this gene by ionizing radiation occurs in certain cell lines regardless of p53 status, and its protein response is correlated with apoptosis following ionizing radiation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14375](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14375) · Entrez [23645](https://www.ncbi.nlm.nih.gov/gene/23645) · UniProt [O75807](https://www.uniprot.org/uniprotkb/O75807) · Ensembl [ENSG00000087074](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087074)

## Data

Gene col 1477: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1477); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1477, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1477]; `tensor/DDL_lfc|DDL_z.npy` [1477]; `embed/gene_vectors.npy` [1477]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1477 or target_col == 1477). Every well: [[PPP1R15A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R15A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
