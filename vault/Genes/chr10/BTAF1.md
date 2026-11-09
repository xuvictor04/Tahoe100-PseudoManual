---
symbol: "BTAF1"
type: "gene"
col: 1748
ensembl_id: "ENSG00000095564"
name: "B-TFIID TATA-box binding protein associated factor 1"
location: "10q23.32"
module: 105
arm: "+"
pooled_cpm: 220.45
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 10
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# BTAF1

*B-TFIID TATA-box binding protein associated factor 1* — 10q23.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.16× (z +10.4, q 1e-22, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.704× (z -4.6, q 0.003, down in 30 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 0.751× (z -3.9, q 0.015, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AK2]] (+0.70, fdr 7e-06), [[CRYBB2P1]] (+0.69, fdr 7e-06), [[CRYBB2P1-1]] (+0.69, fdr 9e-06); moves opposite to [[TRIM47]] (-0.69, fdr 7e-06), [[NUP62]] (-0.65, fdr 1e-05), [[TOPORS]] (-0.63, fdr 7e-06).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02656]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1748.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.16×** | +10.4 | 1e-22 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.09×** | +10.0 | 6e-21 | 49/49 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.93×** | +8.9 | 8e-17 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +8.9 | 1e-16 | 43/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.70×** | +7.2 | 7e-11 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.73×** | +7.1 | 1e-10 | 44/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +5.6 | 2e-06 | 30/45 (LoVo, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +5.6 | 2e-06 | 43/48 (MIA PaCa-2, PANC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +5.0 | 4e-05 | 40/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.91×** | +4.6 | 3e-04 | 28/38 (A-172, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.40×** | +4.5 | 3e-04 | 32/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.39×** | +4.4 | 5e-04 | 32/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.83×** | +4.3 | 9e-04 | 38/48 (HOP62, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +4.0 | 0.002 | 35/48 (PANC-1, LS 180, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.48×** | +3.8 | 0.006 | 36/48 (PANC-1, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.014 | 29/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.019 | 36/48 (COLO 205, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.54×** | +3.1 | 0.067 | 28/48 (NCI-H1573, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1748.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.704×** | -4.6 | 0.003 | 30/44 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.719×** | -4.3 | 0.005 | 39/47 (RKO, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.743×** | -4.0 | 0.011 | 28/49 (NCI-H2347, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.751×** | -3.9 | 0.015 | 39/48 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.777×** | -3.4 | 0.065 | 34/47 (COLO 205, AsPC-1, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.779×** | -3.4 | 0.065 | 33/48 (HOP62, AsPC-1, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.707×** | -3.3 | 0.065 | 38/48 (MIA PaCa-2, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.784×** | -3.3 | 0.065 | 33/48 (AN3 CA, CFPAC-1, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.785×** | -3.3 | 0.065 | 28/48 (H4, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -3.2 | 0.067 | 2/50 (MIA PaCa-2, NCI-H23) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.795×** | -3.1 | 0.099 | 31/48 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.800× | -3.0 | 0.12 | 30/48 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1748. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 297 | 9 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.69× (z +17.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 5.49× (z +17.5) | — |
| [[SW480 (line)]] | alt | 195 | 9 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +15.4) | — |
| [[HOP62 (line)]] | alt | 263 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.13× (z +13.0) | — |
| [[NCI-H1573 (line)]] | alt | 245 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.94× (z +14.0) | — |
| [[LoVo (line)]] | wt | 201 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +14.0) | — |
| [[NCI-H1792 (line)]] | alt | 227 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.78× (z +14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +13.9) | — |
| [[PANC-1 (line)]] | alt | 221 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +14.9) | — |
| [[SNU-1 (line)]] | wt | 287 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +9.1) | — |
| [[A-427 (line)]] | wt | 162 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.71× (z +10.2) | — |
| [[A549 (line)]] | wt | 223 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.18× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 224 | 3 | 0 | [[Digitoxin (drug)]] 0.5 µM 2.99× (z +10.3) | — |
| [[KATO III (line)]] | alt | 153 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +12.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 245 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.77× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.47× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 224 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +10.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +9.9) | — |
| [[BT-474 (line)]] | alt | 174 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 149 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 203 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.78× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 210 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -11.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 131 | 0 | 2 (2 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.162× (z -10.1) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 420 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 289 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -8.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 286 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 186 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.34× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 183 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.63× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 176 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.13× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 247 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -9.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 250 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 182 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0726× (z -11.5) |
| [[SW48 (line)]] | wt | 269 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +9.2) | — |
| [[A-172 (line)]] | wt | 167 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 188 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 310 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 291 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 234 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 273 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 206 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 202 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 161 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 194 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 283 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 247 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 282 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 213 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1748), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AK2]] | +0.70 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[CRYBB2P1]] | +0.69 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[CRYBB2P1-1]] | +0.69 | +0.75 / +0.57 | both halves | 9e-06 |  |
| [[PDIA6]] | +0.67 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[PDK1]] | +0.66 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[STRAP]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[HDAC3]] | +0.66 | +0.84 / +0.48 | both halves | 2e-05 |  |
| [[NUP58]] | +0.65 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[FAM210A]] | +0.64 | +0.70 / +0.58 | both halves | 8e-06 |  |
| [[TMED7]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.62 | +0.76 / +0.48 | both halves | 2e-05 |  |
| [[FAM234B]] | +0.62 | +0.70 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM47]] | -0.69 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[NUP62]] | -0.65 | -0.67 / -0.57 | both halves | 1e-05 |  |
| [[TOPORS]] | -0.63 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[ZFP36L2]] | -0.61 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[MRFAP1L1]] | -0.60 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[NME6]] | -0.60 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[EID2]] | -0.58 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[THG1L]] | -0.58 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[BPTF]] | -0.57 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[KLF11]] | -0.57 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[TBCC]] | -0.57 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[UBQLN2]] | -0.57 | -0.63 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02656]] | C | LINC02656 activity raises BTAF1's level | lines that do not express LINC02656 (4) vs lines expressing it (46) | 1.22× lower at baseline in the lines without LINC02656 | 0.056 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02649, MAP3K8, ENSG00000250842; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.9, -21.2); signed map (-40.1, 24.5). **Vector** length 94.7, 39.0% of its response variance represented; |z| ≥ 3 in 1,064 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.9 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | -4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | -4.6 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.7 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +0.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.7 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -10.2 | -1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.2 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.3 | -0.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.8 | +7.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | +0.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -0.8 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | B-TFIID TATA-box binding protein associated factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.32 — chr10:91,923,770-92,031,437 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAFII170, TAF172, MOT1, TAF-172, TAF(II)170 |
| Gene groups (HGNC) | SNF2 related family; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O14981](https://www.uniprot.org/uniprotkb/O14981) (TATA-binding protein-associated factor 172):

> Regulates transcription in association with TATA binding protein (TBP). Removes TBP from the TATA box in an ATP-dependent manner.

**Summary**, from NCBI Gene [9044](https://www.ncbi.nlm.nih.gov/gene/9044):

> This gene encodes a TAF (TATA box-binding protein-associated factor), which associates with TBP (TATA box-binding protein) to form the B-TFIID complex that is required for transcription initiation of genes by RNA polymerase II. This TAF has DNA-dependent ATPase activity, which drives the dissociation of TBP from DNA, freeing the TBP to associate with other TATA boxes or TATA-less promoters. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:17307](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17307) · Entrez [9044](https://www.ncbi.nlm.nih.gov/gene/9044) · UniProt [O14981](https://www.uniprot.org/uniprotkb/O14981) · Ensembl [ENSG00000095564](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095564)

## Data

Gene col 1748: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1748); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1748, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1748]; `tensor/DDL_lfc|DDL_z.npy` [1748]; `embed/gene_vectors.npy` [1748]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1748 or target_col == 1748). Every well: [[BTAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
