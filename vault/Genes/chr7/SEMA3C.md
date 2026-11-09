---
symbol: "SEMA3C"
type: "gene"
col: 1106
ensembl_id: "ENSG00000075223"
name: "semaphorin 3C"
location: "7q21.11"
module: 66
arm: "+"
pooled_cpm: 231.3
n_lines_expressing: 42
n_dd_up: 29
n_dd_down: 10
n_dd_up_clean: 25
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# SEMA3C

*semaphorin 3C* — 7q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.80× (z +12.0, q 2e-30, up in 35 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.496× (z -14.3, q 1e-43, down in 30 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TGFB2]] (+0.67, fdr 7e-06), [[ALCAM]] (+0.65, fdr 7e-06), [[AHR]] (+0.62, fdr 7e-06); moves opposite to [[IL17RA]] (-0.60, fdr 1e-05), [[FLYWCH1]] (-0.56, fdr 1e-05), [[SLC30A6]] (-0.56, fdr 1e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NFIB]] → it (grade B ⚠); 2 go from it, the strongest it → [[NDUFAF7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1106.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.80×** | +12.0 | 2e-30 | 35/40 (C32, RKO, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.27×** | +11.4 | 2e-27 | 32/40 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +9.5 | 3e-19 | 24/40 (HOP62, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +8.3 | 2e-14 | 25/40 (HOP62, SNU-423, …) | two highest doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +8.1 | 7e-14 | 28/41 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +7.3 | 3e-11 | 25/41 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.0 | 2e-07 | 22/37 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +5.8 | 4e-07 | 23/40 (SNU-423, A-172, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.16×** | +5.8 | 4e-07 | 25/41 (HOP62, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +5.7 | 5e-07 | 27/40 (hTERT-HPNE, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **1.53×** | +5.7 | 8e-07 | 27/42 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **2.07×** | +5.5 | 2e-06 | 29/42 (MIA PaCa-2, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +5.4 | 3e-06 | 21/38 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +5.4 | 3e-06 | 25/40 (SNU-423, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +5.3 | 5e-06 | 25/40 (BT-474, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.87×** | +4.7 | 9e-05 | 27/40 (A-172, SNU-423, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.26×** | +4.6 | 1e-04 | 24/40 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.33×** | +4.2 | 1e-03 | 23/41 (A-172, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +3.9 | 0.003 | 22/40 (SW48, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1106.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.496×** | -14.3 | 1e-43 | 30/41 (NCI-H1792, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.522×** | -9.4 | 2e-18 | 32/40 (NCI-H1573, J82, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.550×** | -8.1 | 1e-13 | 32/40 (NCI-H1573, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.596×** | -7.5 | 1e-11 | 27/40 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.473×** | -5.6 | 2e-06 | 27/37 (NCI-H1792, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.700×** | -5.1 | 3e-05 | 26/40 (HEC-1-A, NCI-H1573, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.723×** | -4.7 | 2e-04 | 25/40 (NCI-H2030, RKO, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.4 | 0.041 | 20/40 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.791×** | -3.4 | 0.043 | 19/40 (A498, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.727×** | -3.3 | 0.058 | 21/41 (NCI-H1573, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.804×** | -3.2 | 0.083 | 15/40 (LoVo, SW 900, …) | top dose only |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.861× | -3.1 | 0.100 | 12/40 (LS 180, NCI-H661, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1106. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 1,193 | 0 | 25 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.184× (z -15.9) |
| [[A-172 (line)]] | wt | 210 | 18 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.18× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 5 µM 4.64× (z +14.1) | — |
| [[C32 (line)]] | wt | 75.7 | 16 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 7.11× (z +15.9) | — |
| [[HOP62 (line)]] | alt | 104 | 12 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.89× (z +25.9) | [[Ixazomib citrate (drug)]] 5 µM 0.350× (z -10.0) |
| [[SNU-423 (line)]] | alt | 120 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.50× (z +22.9) | — |
| [[A549 (line)]] | wt | 260 | 7 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 280 | 9 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.15× (z +18.1) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.98× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 96.5 | 9 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.16× (z +12.5) | — |
| [[A498 (line)]] | wt | 165 | 5 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -11.1) |
| [[RKO (line)]] | wt | 99.4 | 6 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +15.3) | [[Selinexor (drug)]] 5 µM 0.336× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 124 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.69× (z +19.7) | — |
| [[LoVo (line)]] | wt | 152 | 4 | 2 | [[Harringtonine (drug)]] 5 µM 6.76× (z +17.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -11.3) |
| [[SW 900 (line)]] | alt | 185 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.30× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -10.8) |
| [[SW48 (line)]] | wt | 112 | 6 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.50× (z +12.6) | — |
| [[BT-474 (line)]] | alt | 334 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -11.9) |
| [[KATO III (line)]] | alt | 95.1 | 4 | 1 | [[Harringtonine (drug)]] 5 µM 4.22× (z +12.2) | [[Vandetanib (drug)]] 5 µM 0.384× (z -8.5) |
| [[A-427 (line)]] | wt | 1,224 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.404× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~47% of this change |
| [[C-33 A (line)]] | alt | 203 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -13.8) |
| [[HS-578T (line)]] | alt | 182 | 3 | 1 | [[Tucidinostat (drug)]] 5 µM 2.51× (z +10.4) | [[Ixazomib citrate (drug)]] 5 µM 0.323× (z -9.0) |
| [[HT-29 (line)]] | alt | 168 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +18.9) | — |
| [[J82 (line)]] | alt | 277 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.0) | [[Ixazomib citrate (drug)]] 5 µM 0.264× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 383 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.1) | [[Bortezomib (drug)]] 0.05 µM 0.313× (z -10.6) |
| [[H4 (line)]] | wt | 88.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.25× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 3.29× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 158 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.50× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 5 µM 2.30× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -12.3) |
| [[NCI-H1792 (line)]] | alt | 269 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.19× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -18.0) |
| [[NCI-H23 (line)]] | alt | 463 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -16.4) |
| [[NCI-H2347 (line)]] | alt | 112 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 2.37× (z +10.5) | [[Ixazomib citrate (drug)]] 5 µM 0.306× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 171 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 2.07× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -14.4) |
| [[PANC-1 (line)]] | alt | 257 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 191 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.39× (z +9.7) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.305× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 654 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -16.9) |
| [[AsPC-1 (line)]] | alt | 273 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 67.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -11.1) |
| [[Hs 766T (line)]] | wt | 173 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.244× (z -9.6) |
| [[LS 180 (line)]] | wt | 133 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -10.5) |
| [[NCI-H661 (line)]] | alt | 734 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 97.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.3) | — |
| [[SW 1271 (line)]] | alt | 370 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -10.7) |
| [[AN3 CA (line)]] | alt | 32.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 741 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.7 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 47.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 17.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 33.5 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 39.2 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 18.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1106), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGFB2]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[ALCAM]] | +0.65 | +0.58 / +0.66 | both halves | 7e-06 | STRING 471 |
| [[AHR]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[ABLIM1]] | +0.62 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[OLR1]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[KLHL5]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[PHLDB2]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[DSEL]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[CDH2]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 | STRING 512 |
| [[CHML]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[DIO2]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ARID5B]] | +0.56 | +0.56 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL17RA]] | -0.60 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[FLYWCH1]] | -0.56 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[SLC30A6]] | -0.56 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[ZFAND2A]] | -0.56 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[QPCTL]] | -0.54 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[PKD1P6]] | -0.54 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[RARS2]] | -0.54 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[CCDC32]] | -0.53 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[PCYT1A]] | -0.52 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[PMM1]] | -0.52 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[SCNM1]] | -0.52 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[PPP1R26-AS1]] | -0.52 | -0.45 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFIB]] | B | NFIB activity raises SEMA3C's level | lines that do not express NFIB (7) vs lines expressing it (43) | 3.67× lower at baseline in the lines without NFIB | 0.070 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CDH2]] | B | CDH2 activity strengthens SEMA3C's drug response | lines that do not express CDH2 (16) vs lines expressing it (25) | the lines without CDH2 respond 0.79× as strongly (z diff +1.33); strongest at Dinaciclib 0.5 µM: 1.19x vs 2.10x (z diff +4.1) | 0.081 | ⚠ within organs, on part of the lines; also absent: ARMCX1, DKK3, RFTN1; target measured in part of the lines; artifact flags |
| [[MAN1A1]] | B | MAN1A1 activity lowers SEMA3C's level | lines that do not express MAN1A1 (20) vs lines expressing it (30) | 1.68× higher at baseline in the lines without MAN1A1 | 0.088 | ⚠ within organs, on part of the lines; also absent: BDKRB2, TMEM200A, EVA1A |
| [[PSMB5]] | B | PSMB5 activity raises SEMA3C's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers SEMA3C's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDUFAF7]] | B | SEMA3C activity lowers NDUFAF7's level | lines that do not express SEMA3C (8) vs lines expressing it (42) | 1.24× higher at baseline in the lines without SEMA3C | 0.022 | ⚠ within organs, on part of the lines; also absent: IKZF2, ANTXR2 |
| [[PKD1P6]] | B | SEMA3C activity lowers PKD1P6's level | lines that do not express SEMA3C (8) vs lines expressing it (42) | 1.41× higher at baseline in the lines without SEMA3C | 0.067 | ⚠ within organs, on part of the lines; also absent: IKZF2, ANTXR2 |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.646). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.1, 20.1); signed map (47.2, 19.6). **Vector** length 138, 41.5% of its response variance represented; |z| ≥ 3 in 1,697 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.1 | +12.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.0 | +11.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.4 | +8.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.3 | +3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +6.8 | +5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.1 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.8 | +2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.7 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.7 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.3 | -14.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -9.1 | -8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -8.2 | -9.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -7.0 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.9 | -7.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.7 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.6 | -1.4 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -2.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | semaphorin 3C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.11 — chr7:80,742,538-80,922,359 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SemE; previously SEMAE |
| Gene groups (HGNC) | I-set domain containing; Semaphorins |
| Hallmark sets | PEROXISOME |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99985](https://www.uniprot.org/uniprotkb/Q99985) (Semaphorin-3C):

> Binds to plexin family members and plays an important role in the regulation of developmental processes. Required for normal cardiovascular development during embryogenesis. Functions as attractant for growing axons, and thereby plays an important role in axon growth and axon guidance (By similarity).

**Summary**, from NCBI Gene [10512](https://www.ncbi.nlm.nih.gov/gene/10512):

> This gene encodes a secreted glycoprotein that belongs to the semaphorin class 3 family of neuronal guidance cues. The encoded protein contains an N-terminal sema domain, integrin and immunoglobulin-like domains, and a C-terminal basic domain. Homodimerization and proteolytic cleavage of the C-terminal propeptide are necessary for the function of the encoded protein. It binds a neuropilin co-receptor before forming a heterotrimeric complex with an associated plexin. An increase in the …

**Accessions** — [HGNC:10725](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10725) · Entrez [10512](https://www.ncbi.nlm.nih.gov/gene/10512) · UniProt [Q99985](https://www.uniprot.org/uniprotkb/Q99985) · Ensembl [ENSG00000075223](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075223)

## Data

Gene col 1106: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1106); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1106, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1106]; `tensor/DDL_lfc|DDL_z.npy` [1106]; `embed/gene_vectors.npy` [1106]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1106 or target_col == 1106). Every well: [[SEMA3C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEMA3C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
