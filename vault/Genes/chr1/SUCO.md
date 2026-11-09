---
symbol: "SUCO"
type: "gene"
col: 1731
ensembl_id: "ENSG00000094975"
name: "SUN domain containing ossification factor"
location: "1q24.3"
module: 56
arm: "+"
pooled_cpm: 244.95
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 14
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# SUCO

*SUN domain containing ossification factor* — 1q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.47× (z +6.0, q 1e-06, up in 42 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (BT-474 3.70×, LoVo 3.82×, COLO 205 2.66×, HT-29 2.05×, …; ⚠ cell-cycle shift, explains ~25% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (BT-474 3.09×, NCI-H460 2.48×, HepG2/C3A 2.43×); [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 2.69×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (C32 4.87×).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.423× (z -10.5, q 6e-23, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.670× (z -4.9, q 1e-04, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM263]] (+0.80, fdr 7e-06), [[COG6]] (+0.80, fdr 7e-06), [[PJA2]] (+0.78, fdr 7e-06); moves opposite to [[ITPA]] (-0.66, fdr 7e-06), [[SLC25A13]] (-0.64, fdr 7e-06), [[PRRC2B]] (-0.64, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CREG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1731.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (BT-474 3.70×, LoVo 3.82×, COLO 205 2.66×, HT-29 2.05×, …; ⚠ cell-cycle shift, explains ~25% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (BT-474 3.09×, NCI-H460 2.48×, HepG2/C3A 2.43×); [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 2.69×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (C32 4.87×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.47×** | +6.0 | 1e-06 | 42/49 (C32, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.24×** | +3.7 | 0.073 | 27/48 (BT-474, LoVo, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 1.30× | +3.4 | 0.14 | 30/48 (BT-474, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | 1.62× | +3.2 | 0.17 | 27/48 (BT-474, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | 1.59× | +3.1 | 0.21 | 32/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.39× | +3.0 | 0.23 | 29/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1731.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.423×** | -10.5 | 6e-23 | 41/44 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.485×** | -9.2 | 1e-17 | 44/49 (COLO 205, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.616×** | -5.7 | 3e-06 | 33/45 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.652×** | -5.2 | 3e-05 | 39/47 (HT-29, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.670×** | -4.9 | 1e-04 | 37/48 (NCI-H2347, J82, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.709×** | -4.3 | 0.001 | 40/48 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.780×** | -3.9 | 0.007 | 31/48 (A498, RKO, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.754×** | -3.6 | 0.025 | 34/48 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.755×** | -3.5 | 0.025 | 34/49 (RPMI-7951, LoVo, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.760×** | -3.5 | 0.030 | 33/49 (LoVo, A-172, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.773×** | -3.3 | 0.059 | 34/48 (RKO, LoVo, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.782×** | -3.1 | 0.089 | 32/48 (H4, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.784×** | -3.1 | 0.092 | 30/49 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.785×** | -3.0 | 0.094 | 29/48 (A549, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1731. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 186 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +19.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 306 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.7) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 5 µM 0.257× (z -15.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 172 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +16.2) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 5 µM 0.238× (z -13.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 175 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.0) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 311 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -11.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 412 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -11.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 409 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -16.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 259 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.87× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.383× (z -10.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 282 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.4) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -16.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 214 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 242 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.359× (z -9.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 260 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -9.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 221 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 238 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -9.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 508 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -12.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 260 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.385× (z -8.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 245 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -11.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 333 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -11.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 316 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -10.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 163 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.454× (z -9.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 303 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -9.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 273 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 337 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 266 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 192 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -8.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 184 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.408× (z -9.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 275 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -10.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 243 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -13.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 301 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.8) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SW480 (line)]] | alt | 169 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.445× (z -8.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 279 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 145 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 373 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 242 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 257 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 150 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 160 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 260 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 173 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 198 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 287 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 102 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1731), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM263]] | +0.80 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[COG6]] | +0.80 | +0.80 / +0.74 | both halves | 7e-06 |  |
| [[PJA2]] | +0.78 | +0.81 / +0.74 | both halves | 7e-06 |  |
| [[SRP54]] | +0.78 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.78 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.78 | +0.80 / +0.67 | both halves | 7e-06 |  |
| [[COPB1]] | +0.77 | +0.80 / +0.67 | both halves | 7e-06 |  |
| [[ERLEC1]] | +0.77 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.75 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[SEC31A]] | +0.75 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[TTC3]] | +0.74 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[LMAN1]] | +0.74 | +0.75 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITPA]] | -0.66 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[SLC25A13]] | -0.64 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[PRRC2B]] | -0.64 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[UTP20]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[DHX37]] | -0.62 | -0.66 / -0.58 | both halves | 8e-06 |  |
| [[GPATCH4]] | -0.61 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[CUEDC1]] | -0.60 | -0.59 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREG2]] | B | CREG2 activity raises SUCO's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.38× lower at baseline in the lines without CREG2 | 0.045 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[AGR2]] | B | AGR2 activity raises SUCO's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.21× lower at baseline in the lines without AGR2 | 0.048 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.822). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.3, -33.9); signed map (-51.0, 11.0). **Vector** length 117, 48.5% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.66 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.69 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.69 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | -0.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | -0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | -2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -0.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.7 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +0.3 |
|  | [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | +2.2 | +2.3 |
|  | [[Silodosin (drug)]] 5 µM |  | +2.2 | +1.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -5.9 | +2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.8 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -5.6 | +1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.5 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.3 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | SUN domain containing ossification factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.3 — chr1:172,532,349-172,611,833 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CH1, SLP1, OPT; previously C1orf9 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBS9](https://www.uniprot.org/uniprotkb/Q9UBS9) (SUN domain-containing ossification factor):

> Required for bone modeling during late embryogenesis. Regulates type I collagen synthesis in osteoblasts during their postnatal maturation (By similarity).

**Summary**, from NCBI Gene [51430](https://www.ncbi.nlm.nih.gov/gene/51430):

> Predicted to be involved in positive regulation of collagen biosynthetic process; positive regulation of osteoblast differentiation; and regulation of bone remodeling. Predicted to be located in rough endoplasmic reticulum. Predicted to be active in cytoplasm and membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1240](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1240) · Entrez [51430](https://www.ncbi.nlm.nih.gov/gene/51430) · UniProt [Q9UBS9](https://www.uniprot.org/uniprotkb/Q9UBS9) · Ensembl [ENSG00000094975](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000094975)

## Data

Gene col 1731: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1731); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1731, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1731]; `tensor/DDL_lfc|DDL_z.npy` [1731]; `embed/gene_vectors.npy` [1731]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1731 or target_col == 1731). Every well: [[SUCO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUCO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
