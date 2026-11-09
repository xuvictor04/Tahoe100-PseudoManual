---
symbol: "TMEM87A"
type: "gene"
col: 2404
ensembl_id: "ENSG00000103978"
name: "transmembrane protein 87A"
location: "15q15.1"
module: 156
arm: "+"
pooled_cpm: 209.46
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 17
n_dd_up_clean: 9
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# TMEM87A

*transmembrane protein 87A* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.00× (z +13.0, q 7e-36, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.440× (z -18.5, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL16]] (+0.69, fdr 7e-06), [[QRICH1]] (+0.66, fdr 7e-06), [[IGBP1]] (+0.64, fdr 7e-06); moves opposite to [[DBN1]] (-0.48, fdr 4e-05), [[RSC1A1]] (-0.48, fdr 1e-04), [[CDC42EP1]] (-0.48, fdr 1e-04).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2404.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.00×** | +13.0 | 7e-36 | 45/49 (COLO 205, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.39×** | +10.3 | 2e-22 | 43/48 (LoVo, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +9.6 | 2e-19 | 39/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +8.3 | 2e-14 | 35/48 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +7.4 | 1e-11 | 38/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +7.1 | 2e-10 | 30/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.24×** | +4.9 | 1e-04 | 30/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +4.7 | 1e-04 | 28/48 (HT-29, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +4.7 | 2e-04 | 25/48 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +4.4 | 7e-04 | 24/48 (COLO 205, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.081 | 19/48 (HEC-1-A, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2404.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.440×** | -18.5 | 0e+00 | 48/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.474×** | -16.9 | 0e+00 | 48/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.509×** | -15.3 | 0e+00 | 48/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.550×** | -13.5 | 3e-39 | 48/48 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.709×** | -11.0 | 6e-26 | 45/48 (LOX-IMVI, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.618×** | -10.5 | 1e-23 | 44/48 (hTERT-HPNE, H4, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.653×** | -9.6 | 6e-20 | 46/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.758×** | -8.8 | 8e-17 | 28/49 (RKO, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.485×** | -8.5 | 9e-16 | 48/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.688×** | -8.4 | 2e-15 | 46/49 (LOX-IMVI, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.770×** | -8.3 | 5e-15 | 31/48 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -6.6 | 2e-09 | 35/50 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.747×** | -6.3 | 1e-08 | 25/44 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.788×** | -5.2 | 1e-05 | 27/48 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.815×** | -4.6 | 2e-04 | 27/48 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.867× | -4.5 | 2e-04 | 15/48 (CFPAC-1, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2404. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 215 | 13 | 6 | [[Triamcinolone (drug)]] 5 µM 1.85× (z +10.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -18.9) |
| [[LoVo (line)]] | wt | 286 | 7 (2 ⚠) | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.82× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.320× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.647× (z -11.2) |
| [[SW480 (line)]] | alt | 229 | 7 (1 ⚠) | 5 | [[TAK-901 (drug)]] 5 µM 5.46× (z +16.7) | [[Belinostat (drug)]] 5 µM 0.536× (z -11.6) |
| [[PANC-1 (line)]] | alt | 242 | 6 (1 ⚠) | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.386× (z -15.9) |
| [[LOX-IMVI (line)]] | wt | 223 | 2 | 8 | [[TAK-901 (drug)]] 0.05 µM 2.73× (z +13.7) | [[Belinostat (drug)]] 5 µM 0.307× (z -17.0) |
| [[LS 180 (line)]] | wt | 227 | 4 (1 ⚠) | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.401× (z -12.7) |
| [[H4 (line)]] | wt | 239 | 1 | 7 | [[Clobetasol propionate (drug)]] 0.05 µM 2.49× (z +11.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 186 | 1 | 7 | [[TAK-901 (drug)]] 5 µM 4.51× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.459× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 268 | 1 | 6 | [[TAK-901 (drug)]] 5 µM 3.11× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.400× (z -14.4) |
| [[HOP62 (line)]] | alt | 170 | 1 | 6 | [[TAK-901 (drug)]] 5 µM 3.37× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -16.8) |
| [[C32 (line)]] | wt | 219 | 0 | 6 | — | [[Belinostat (drug)]] 5 µM 0.388× (z -12.7) |
| [[HT-29 (line)]] | alt | 270 | 3 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.11× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.518× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 250 | 1 | 5 | [[TAK-901 (drug)]] 5 µM 4.89× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.345× (z -14.6) |
| [[NCI-H2030 (line)]] | alt | 308 | 1 | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.361× (z -12.4) |
| [[RKO (line)]] | wt | 272 | 2 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.30× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -12.6) |
| [[A549 (line)]] | wt | 156 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 3.69× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -11.7) |
| [[BT-474 (line)]] | alt | 174 | 4 (1 ⚠) | 1 | [[TAK-901 (drug)]] 0.05 µM 2.90× (z +14.5) | [[Panobinostat (drug)]] 0.5 µM 0.514× (z -9.5) |
| [[HCT15 (line)]] | alt | 270 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.14× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.383× (z -11.3) |
| [[HS-578T (line)]] | alt | 165 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.368× (z -14.1) |
| [[KATO III (line)]] | alt | 229 | 1 | 4 | [[PH-797804 (drug)]] 5 µM 2.71× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.384× (z -15.9) |
| [[NCI-H1573 (line)]] | alt | 287 | 2 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.463× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 167 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.342× (z -14.8) |
| [[RPMI-7951 (line)]] | alt | 258 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.400× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 178 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.70× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.426× (z -11.8) |
| [[SNU-1 (line)]] | wt | 254 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.14× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.354× (z -11.6) |
| [[SW1417 (line)]] | alt | 210 | 2 | 3 | [[TAK-901 (drug)]] 0.05 µM 1.98× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.447× (z -11.4) |
| [[A-427 (line)]] | wt | 146 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 2.29× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | [[Panobinostat (drug)]] 5 µM 0.502× (z -9.8) |
| [[A498 (line)]] | wt | 213 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.459× (z -12.1) |
| [[COLO 205 (line)]] | alt | 290 | 2 | 2 | [[TAK-901 (drug)]] 5 µM 10.3× (z +17.2) | [[Panobinostat (drug)]] 0.5 µM 0.500× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 180 | 2 | 2 | [[TAK-901 (drug)]] 0.05 µM 2.06× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.550× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 192 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.365× (z -12.6) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.445× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 133 | 2 | 2 | [[TAK-901 (drug)]] 5 µM 6.75× (z +12.9) | [[Belinostat (drug)]] 5 µM 0.392× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 187 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 108 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.379× (z -13.9) |
| [[SW48 (line)]] | wt | 225 | 1 | 3 | [[TAK-901 (drug)]] 0.05 µM 3.28× (z +13.5) | [[Panobinostat (drug)]] 0.5 µM 0.416× (z -10.5) |
| [[A-172 (line)]] | wt | 158 | 0 | 3 | — | [[Panobinostat (drug)]] 0.05 µM 0.410× (z -12.8) |
| [[AsPC-1 (line)]] | alt | 253 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.427× (z -12.8) |
| [[C-33 A (line)]] | alt | 200 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 4.14× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.408× (z -11.2) |
| [[Hs 766T (line)]] | wt | 162 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 3.94× (z +9.2) | [[Belinostat (drug)]] 5 µM 0.424× (z -11.0) |
| [[SHP-77 (line)]] | alt | 185 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 4.08× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.430× (z -11.1) |
| [[SW 900 (line)]] | alt | 200 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -12.2) |
| [[J82 (line)]] | alt | 154 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -14.5) |
| [[SNU-423 (line)]] | alt | 144 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.502× (z -9.3) |
| [[CHP-212 (line)]] | wt | 213 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -9.4) |
| [[AN3 CA (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 293 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 187 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2404), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL16]] | +0.69 | +0.68 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[QRICH1]] | +0.66 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[IGBP1]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[VPS51]] | +0.63 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[UXT]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[CCDC12]] | +0.60 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[ODR4]] | +0.60 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[VPS39-DT]] | +0.58 | +0.54 / +0.42 | both halves | 4e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[NUP214]] | +0.57 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[ECSIT]] | +0.56 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[CWC25]] | +0.56 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[DCTN4]] | +0.54 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[ORC2]] | +0.54 | +0.56 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DBN1]] | -0.48 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[RSC1A1]] | -0.48 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[CDC42EP1]] | -0.48 | -0.61 / -0.35 | both halves | 1e-04 |  |
| [[CARD10]] | -0.47 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[ITPR3]] | -0.47 | -0.23 / -0.41 | both halves | 5e-04 |  |
| [[NOTCH2NLC]] | -0.47 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[RASSF3]] | -0.46 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[CSRP1]] | -0.45 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[RIPOR1]] | -0.45 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[SLC45A3]] | -0.45 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[EPB41L2]] | -0.45 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[AGRN]] | -0.44 | -0.39 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers TMEM87A's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises TMEM87A's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.612). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.7, -10.2); signed map (-5.1, -9.2). **Vector** length 111, 40.8% of its response variance represented; |z| ≥ 3 in 1,345 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.9 | -0.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +13.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +10.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.3 | +4.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.4 | +0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.3 | +1.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.1 | +3.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.3 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.3 | -11.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -5.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.2 | -9.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.0 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -8.5 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 87A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:42,210,447-42,273,534 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564G2022, ELKIN1 |
| Gene groups (HGNC) | 7TM uncharacterized proteins |
| Reactome | 4 pathways, smallest: RHOA GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBN3](https://www.uniprot.org/uniprotkb/Q8NBN3) (Golgi-pH regulating cation channel):

> Voltage- and pH-dependent, inwardly rectifying cation channel that mediates ion flux across the Golgi membrane, supporting luminal acidification necessary for normal Golgi morphology and function. Implicated in normal touch sensitivity through the generation of mechanically activated currents. Could also be involved in cell mechanosensitivity regulating cell adhesion and migration. May also be involved in retrograde transport from endosomes to the trans-Golgi network (TGN). Contributes to …

**Summary**, from NCBI Gene [25963](https://www.ncbi.nlm.nih.gov/gene/25963):

> Enables voltage-gated monoatomic anion channel activity. Involved in cellular response to mechanical stimulus; detection of mechanical stimulus involved in sensory perception of touch; and intracellular pH reduction. Acts upstream of or within retrograde transport, endosome to Golgi. Located in Golgi apparatus; plasma membrane; and ruffle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24522](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24522) · Entrez [25963](https://www.ncbi.nlm.nih.gov/gene/25963) · UniProt [Q8NBN3](https://www.uniprot.org/uniprotkb/Q8NBN3) · Ensembl [ENSG00000103978](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103978)

## Data

Gene col 2404: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2404); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2404, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2404]; `tensor/DDL_lfc|DDL_z.npy` [2404]; `embed/gene_vectors.npy` [2404]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2404 or target_col == 2404). Every well: [[TMEM87A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM87A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
