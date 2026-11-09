---
symbol: "HMGA2"
type: "gene"
col: 7421
ensembl_id: "ENSG00000149948"
name: "high mobility group AT-hook 2"
location: "12q14.3"
module: 147
arm: "+"
pooled_cpm: 370.17
n_lines_expressing: 41
n_dd_up: 13
n_dd_down: 63
n_dd_up_clean: 13
n_dd_down_clean: 54
in_vector_space: true
direction_upstream: 19
direction_downstream: 21
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# HMGA2

*high mobility group AT-hook 2* — 12q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[BAY1125976 (drug)]] 5 µM: 1.91× (z +4.1, q 0.013, up in 29 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 63 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.136× (z -23.7, q 0e+00, down in 39 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELK3]] (+0.76, fdr 7e-06), [[SPRY4-AS1]] (+0.76, fdr 7e-06), [[HMGA2-AS1]] (+0.76, fdr 7e-06, ⚠ same locus), [[NPAS2]] (+0.74, fdr 7e-06); moves opposite to [[GBP2]] (-0.61, fdr 7e-06), [[GPRC5B]] (-0.60, fdr 8e-06), [[ZSCAN31]] (-0.57, fdr 1e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[RPSAP52]] → it (grade B ⚠); 21 go from it, the strongest it → [[CD59]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7421.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[BAY1125976 (drug)]] 5 µM |  | **1.91×** | +4.1 | 0.013 | 29/39 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Econazole (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.013 | 21/39 (LOX-IMVI, Hs 766T, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.42×** | +4.0 | 0.013 | 21/39 (RPMI-7951, Hs 766T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.023 | 20/39 (RPMI-7951, LOX-IMVI, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.023 | 19/39 (AsPC-1, LOX-IMVI, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.023 | 23/39 (RKO, CFPAC-1, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.34×** | +3.6 | 0.031 | 25/40 (Panc 03.27, LOX-IMVI, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.040 | 16/39 (LOX-IMVI, RPMI-7951, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.35×** | +3.4 | 0.040 | 22/39 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.058 | 18/39 (Hs 766T, LOX-IMVI, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.070 | 19/39 (Hs 766T, LOX-IMVI, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.094 | 15/39 (RPMI-7951, AsPC-1, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.099 | 18/39 (LOX-IMVI, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 64 in all, 10 with an alert ⚠; shown: the 15 strongest. 63 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7421.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.136×** | -23.7 | 0e+00 | 39/39 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.251×** | -23.1 | 0e+00 | 37/39 (hTERT-HPNE, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.151×** | -22.4 | 0e+00 | 39/39 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.163×** | -21.5 | 0e+00 | 39/39 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.301×** | -15.1 | 0e+00 | 39/41 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.334×** | -12.5 | 9e-34 | 33/39 (hTERT-HPNE, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.476×** | -12.4 | 2e-33 | 34/40 (hTERT-HPNE, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.361×** | -12.1 | 1e-31 | 37/40 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.395×** | -11.7 | 6e-30 | 37/40 (Hs 766T, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.454×** | -11.5 | 1e-28 | 37/39 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.388×** | -10.8 | 2e-25 | 34/38 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.406×** | -10.2 | 6e-23 | 36/39 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.432×** | -9.9 | 1e-21 | 33/39 (hTERT-HPNE, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.433×** | -9.9 | 2e-21 | 31/39 (hTERT-HPNE, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.425×** | -9.6 | 4e-20 | 38/39 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7421. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 1,901 | 0 | 42 (11 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0155× (z -35.0) |
| [[SW48 (line)]] | wt | 1,330 | 0 | 29 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0315× (z -26.9) |
| [[SW 900 (line)]] | alt | 1,451 | 0 | 28 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0682× (z -27.1) |
| [[hTERT-HPNE (line)]] | wt | 2,331 | 0 | 25 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0131× (z -31.1) |
| [[NCI-H1792 (line)]] | alt | 923 | 0 | 24 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0957× (z -25.1) |
| [[HEC-1-A (line)]] | alt | 393 | 0 | 22 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0662× (z -22.2) |
| [[Hs 766T (line)]] | wt | 350 | 5 | 16 | [[Clobetasol propionate (drug)]] 5 µM 3.16× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.0811× (z -19.2) |
| [[NCI-H460 (line)]] | wt | 125 | 0 | 20 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -21.5) |
| [[A549 (line)]] | wt | 317 | 0 | 19 | — | [[Homoharringtonine (drug)]] 5 µM 0.0880× (z -23.9) |
| [[HS-578T (line)]] | alt | 735 | 0 | 19 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0331× (z -23.3) |
| [[H4 (line)]] | wt | 234 | 0 | 17 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0865× (z -15.9) |
| [[RPMI-7951 (line)]] | alt | 436 | 1 | 16 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 3.27× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -24.0) |
| [[LOX-IMVI (line)]] | wt | 667 | 2 | 14 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 2.63× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.0540× (z -26.9) |
| [[NCI-H1573 (line)]] | alt | 123 | 0 | 15 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -14.5) |
| [[PANC-1 (line)]] | alt | 413 | 0 | 15 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -27.5) |
| [[A-427 (line)]] | wt | 764 | 0 | 14 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0626× (z -28.7) |
| [[RKO (line)]] | wt | 792 | 0 | 14 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -19.2) |
| [[AsPC-1 (line)]] | alt | 449 | 0 | 13 | — | [[Panobinostat (drug)]] 5 µM 0.0615× (z -19.4) |
| [[C32 (line)]] | wt | 221 | 0 | 13 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 389 | 0 | 12 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0942× (z -17.5) |
| [[AN3 CA (line)]] | alt | 975 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -21.5) |
| [[CFPAC-1 (line)]] | alt | 246 | 0 | 9 | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -13.4) |
| [[SNU-423 (line)]] | alt | 588 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -19.2) |
| [[SW 1088 (line)]] | alt | 650 | 0 | 8 | — | [[Panobinostat (drug)]] 5 µM 0.0342× (z -12.5) |
| [[SW480 (line)]] | alt | 133 | 0 | 8 | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -22.9) |
| [[HepG2_C3A (line)]] | wt | 202 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -20.1) |
| [[NCI-H2030 (line)]] | alt | 205 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -18.8) |
| [[Panc 03.27 (line)]] | alt | 163 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.101× (z -15.3) |
| [[SK-MEL-2 (line)]] | alt | 297 | 2 (1 ⚠) | 3 | [[Niclosamide (olamine) (drug)]] 5 µM 2.29× (z +9.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -15.6) |
| [[SW1417 (line)]] | alt | 136 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -15.2) |
| [[SW 1271 (line)]] | alt | 433 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -11.9) |
| [[C-33 A (line)]] | alt | 147 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -13.2) |
| [[HT-29 (line)]] | alt | 144 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -17.4) |
| [[KATO III (line)]] | alt | 104 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -17.8) |
| [[LS 180 (line)]] | wt | 132 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -19.6) |
| [[NCI-H2347 (line)]] | alt | 94.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.195× (z -10.7) |
| [[CHP-212 (line)]] | wt | 219 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -8.6) |
| [[HCT15 (line)]] | alt | 131 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -10.0) |
| [[A-172 (line)]] | wt | 28.1 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 68.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 26.4 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 58.9 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 71.9 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 91.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 420 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 348 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.5 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 32.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7421), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELK3]] | +0.76 | +0.78 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[SPRY4-AS1]] | +0.76 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[HMGA2-AS1]] | +0.76 | +0.74 / +0.74 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[NPAS2]] | +0.74 | +0.77 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SPRY4]] | +0.74 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[RPSAP52]] | +0.73 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[CLMP]] | +0.72 | +0.68 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[PITPNC1]] | +0.71 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[LINC02454]] | +0.70 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[NT5E]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[PHC2]] | +0.68 | +0.73 / +0.72 | both halves | 7e-06 | pathway: Cellular Senescence |
| [[MAP4K4]] | +0.68 | +0.70 / +0.64 | both halves | 7e-06 | pathway: Cellular Senescence |
| [[AKAP12]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBP2]] | -0.61 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[GPRC5B]] | -0.60 | -0.57 / -0.58 | both halves | 8e-06 |  |
| [[ZSCAN31]] | -0.57 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[EPB41]] | -0.57 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[NPEPPS]] | -0.56 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[KIAA1522]] | -0.55 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[MICA]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[FRK]] | -0.52 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[PLAAT3]] | -0.52 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[GALM]] | -0.52 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[PSME1]] | -0.51 | -0.46 / -0.43 | both halves | 4e-05 |  |
| [[RAB30]] | -0.51 | -0.52 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 17, C 2. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPSAP52]] | B | RPSAP52 activity raises HMGA2's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 5.43× lower at baseline in the lines without RPSAP52 | 1e-04 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[MSRB3]] | B | MSRB3 activity raises HMGA2's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 3.03× lower at baseline in the lines without MSRB3 | 0.006 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[HAS2]] | B | HAS2 activity raises HMGA2's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 3.40× lower at baseline in the lines without HAS2 | 0.006 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[AKAP12]] | B | AKAP12 activity raises HMGA2's level | lines that do not express AKAP12 (18) vs lines expressing it (32) | 3.22× lower at baseline in the lines without AKAP12 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: ADAMTS18, IGF2BP1, CLEC2B |
| [[ARHGAP22]] | B | ARHGAP22 activity raises HMGA2's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 3.21× lower at baseline in the lines without ARHGAP22 | 0.022 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[TMEM156]] | B | TMEM156 activity raises HMGA2's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 2.58× lower at baseline in the lines without TMEM156 | 0.041 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[NLRP3]] | B | NLRP3 activity raises HMGA2's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 2.29× lower at baseline in the lines without NLRP3 | 0.049 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |
| [[UBASH3B]] | B | UBASH3B activity raises HMGA2's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 3.39× lower at baseline in the lines without UBASH3B | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[MIR100HG]] | B | MIR100HG activity raises HMGA2's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 2.76× lower at baseline in the lines without MIR100HG | 0.057 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[HTR7]] | B | HTR7 activity raises HMGA2's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 2.50× lower at baseline in the lines without HTR7 | 0.059 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[MAP2K1]] | B | MAP2K1 activity raises HMGA2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 11.5% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ETV1]] | B | ETV1 activity raises HMGA2's level | lines that do not express ETV1 (11) vs lines expressing it (39) | 3.26× lower at baseline in the lines without ETV1 | 0.082 | ⚠ within organs, on part of the lines; also absent: LINC02454, KATNAL1, CCDC136 |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 20, C 1. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD59]] | B | HMGA2 activity raises CD59's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 1.53× lower at baseline in the lines without HMGA2 | 0.003 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[EVA1C]] | B | HMGA2 activity raises EVA1C's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 2.44× lower at baseline in the lines without HMGA2 | 0.007 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[UBASH3B]] | B | HMGA2 activity raises UBASH3B's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 2.92× lower at baseline in the lines without HMGA2 | 0.008 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[C11orf91]] | B | HMGA2 activity raises C11orf91's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without HMGA2 | 0.015 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[RPSAP52]] | B | HMGA2 activity raises RPSAP52's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 4.34× lower at baseline in the lines without HMGA2 | 0.029 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[ITGA2]] | B | HMGA2 activity raises ITGA2's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 2.59× lower at baseline in the lines without HMGA2 | 0.033 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[MIR100HG]] | B | HMGA2 activity raises MIR100HG's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 3.64× lower at baseline in the lines without HMGA2 | 0.044 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[HAS2]] | B | HMGA2 activity raises HAS2's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 4.13× lower at baseline in the lines without HMGA2 | 0.047 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[TMEM156]] | B | HMGA2 activity raises TMEM156's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 3.90× lower at baseline in the lines without HMGA2 | 0.049 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[EMP1]] | B | HMGA2 activity raises EMP1's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 2.08× lower at baseline in the lines without HMGA2 | 0.056 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[IGF2BP2]] | B | HMGA2 activity raises IGF2BP2's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 2.53× lower at baseline in the lines without HMGA2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| cells under [[Vemurafenib (drug)]] 5 µM | B | HMGA2 activity raises the cells' numbers under Vemurafenib 5 µM (protects the cells) | lines that do not express HMGA2 (9) vs lines expressing it (39) | the lines without HMGA2: 0.88× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.864). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.9, 6.8); signed map (10.7, 46.7). **Vector** length 139, 51.8% of its response variance represented; |z| ≥ 3 in 2,373 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | -0.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.4 | +4.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +4.4 | +4.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.0 | +3.8 |
| fall | [[Trametinib (drug)]] 5 µM |  | -13.0 | -15.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -12.5 | -11.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -11.8 | -10.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -11.6 | -11.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -11.1 | -10.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -10.9 | -12.1 |

## What is on record

|  |  |
|---|---|
| Name | high mobility group AT-hook 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.3 — chr12:65,824,460-65,966,291 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BABL, LIPO; previously HMGIC |
| Gene groups (HGNC) | Canonical high mobility group |
| Reactome | 5 pathways, smallest: Formation of Senescence-Associated Heterochromatin Foci (SAHF); DNA Damage/Telomere Stress Induced Senescence; Cellular Senescence |
| Matched by | ensembl_id |

**Function**, from UniProt [P52926](https://www.uniprot.org/uniprotkb/P52926) (High mobility group protein HMGI-C):

> Functions as a transcriptional regulator. Functions in cell cycle regulation through CCNA2. Plays an important role in chromosome condensation during the meiotic G2/M transition of spermatocytes. Plays a role in postnatal myogenesis, is involved in satellite cell activation (By similarity). Positively regulates IGF2 expression through PLAG1 and in a PLAG1-independent manner.

**Summary**, from NCBI Gene [8091](https://www.ncbi.nlm.nih.gov/gene/8091):

> This gene encodes a protein that belongs to the non-histone chromosomal high mobility group (HMG) protein family. HMG proteins function as architectural factors and are essential components of the enhancesome. This protein contains structural DNA-binding domains and may act as a transcriptional regulating factor. Identification of the deletion, amplification, and rearrangement of this gene that are associated with myxoid liposarcoma suggests a role in adipogenesis and mesenchymal …

**Accessions** — [HGNC:5009](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5009) · Entrez [8091](https://www.ncbi.nlm.nih.gov/gene/8091) · UniProt [P52926](https://www.uniprot.org/uniprotkb/P52926) · Ensembl [ENSG00000149948](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149948)

## Data

Gene col 7421: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7421); `tables/drug_effects.parquet` (77 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7421, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7421]; `tensor/DDL_lfc|DDL_z.npy` [7421]; `embed/gene_vectors.npy` [7421]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7421 or target_col == 7421). Every well: [[HMGA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
