---
symbol: "DNAJA1"
type: "gene"
col: 1451
ensembl_id: "ENSG00000086061"
name: "DnaJ heat shock protein family (Hsp40) member A1"
location: "9p21.1"
module: 60
arm: "+"
pooled_cpm: 189.88
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# DNAJA1

*DnaJ heat shock protein family (Hsp40) member A1* — 9p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (18 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 5.68× (z +18.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.671× (z -4.3, q 0.011, down in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.291×); [[Ponatinib (drug)]] 5 µM in 1 line (KATO III 0.412×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.358×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBB]] (+0.69, fdr 7e-06), [[HSPA1B]] (+0.65, fdr 7e-06), [[HSPH1]] (+0.59, fdr 1e-05); moves opposite to [[PMS2P1]] (-0.53, fdr 3e-05), [[SUMF2]] (-0.51, fdr 2e-05), [[VPS16]] (-0.50, fdr 5e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 18 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1451.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **5.68×** | +18.6 | 0e+00 | 48/48 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.35×** | +12.9 | 8e-36 | 48/48 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.17×** | +12.4 | 8e-33 | 48/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.93×** | +8.9 | 5e-17 | 39/48 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.14×** | +8.2 | 4e-14 | 41/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.22×** | +8.1 | 7e-14 | 46/48 (KATO III, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.06×** | +7.7 | 9e-13 | 41/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.99×** | +7.3 | 1e-11 | 43/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.04×** | +7.3 | 1e-11 | 44/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.94×** | +6.8 | 5e-10 | 46/47 (COLO 205, SHP-77, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.19×** | +6.5 | 4e-09 | 44/45 (SNU-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.82×** | +6.4 | 6e-09 | 42/48 (PANC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.57×** | +4.9 | 5e-05 | 37/48 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.84×** | +4.6 | 1e-04 | 42/49 (SW1417, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.09×** | +4.1 | 0.001 | 40/47 (KATO III, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **2.08×** | +4.1 | 0.001 | 41/48 (HOP62, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.019 | 34/48 (HOP62, NCI-H460, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.054 | 34/48 (KATO III, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1451.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.291×); [[Ponatinib (drug)]] 5 µM in 1 line (KATO III 0.412×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.358×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.671×** | -4.3 | 0.011 | 39/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.717× | -3.5 | 0.11 | 43/48 (HEC-1-A, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.741× | -3.2 | 0.25 | 34/48 (HCT15, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.746× | -3.1 | 0.25 | 29/48 (A498, HS-578T, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1451. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 102 | 12 (8 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.61× (z +14.4) | — |
| [[PANC-1 (line)]] | alt | 188 | 9 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.95× (z +14.1) | — |
| [[CFPAC-1 (line)]] | alt | 156 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +14.8) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.71× (z +14.0) | — |
| [[KATO III (line)]] | alt | 220 | 6 (2 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 6.24× (z +18.5) | [[Ponatinib (drug)]] 5 µM 0.412× (z -8.9) |
| [[SW1417 (line)]] | alt | 204 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.48× (z +16.3) | — |
| [[A498 (line)]] | wt | 268 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.92× (z +13.2) | — |
| [[COLO 205 (line)]] | alt | 150 | 6 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 8.20× (z +12.7) ⚠ toxic; cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.24× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 215 | 6 | 0 | [[Auranofin (drug)]] 5 µM 11.9× (z +22.8) | — |
| [[HS-578T (line)]] | alt | 158 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.21× (z +13.0) | — |
| [[hTERT-HPNE (line)]] | wt | 125 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +14.7) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Auranofin (drug)]] 5 µM 8.34× (z +14.7) | — |
| [[LS 180 (line)]] | wt | 176 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.85× (z +13.5) | — |
| [[AsPC-1 (line)]] | alt | 333 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +15.4) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.38× (z +11.2) | — |
| [[Hs 766T (line)]] | wt | 224 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.64× (z +15.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 146 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 11.0× (z +19.1) | — |
| [[SNU-423 (line)]] | alt | 130 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.93× (z +18.9) | — |
| [[A-172 (line)]] | wt | 166 | 4 | 0 | [[Auranofin (drug)]] 5 µM 8.74× (z +19.0) | — |
| [[BT-474 (line)]] | alt | 242 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 12.1× (z +25.9) | — |
| [[C32 (line)]] | wt | 80.5 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 21.0× (z +18.4) | — |
| [[HepG2_C3A (line)]] | wt | 196 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.62× (z +11.1) | — |
| [[HOP62 (line)]] | alt | 115 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 15.1× (z +20.2) | — |
| [[HT-29 (line)]] | alt | 211 | 4 | 0 | [[Auranofin (drug)]] 5 µM 9.32× (z +21.0) | — |
| [[NCI-H2347 (line)]] | alt | 208 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.72× (z +12.3) | — |
| [[Panc 03.27 (line)]] | alt | 214 | 4 | 0 | [[Auranofin (drug)]] 5 µM 6.09× (z +16.2) | — |
| [[SW480 (line)]] | alt | 164 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.3× (z +20.5) | — |
| [[A-427 (line)]] | wt | 186 | 2 | 1 | [[Auranofin (drug)]] 5 µM 6.53× (z +15.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.358× (z -8.6) |
| [[J82 (line)]] | alt | 252 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.33× (z +11.2) | — |
| [[LoVo (line)]] | wt | 290 | 3 | 0 | [[Auranofin (drug)]] 5 µM 7.37× (z +17.5) | — |
| [[LOX-IMVI (line)]] | wt | 205 | 3 | 0 | [[Auranofin (drug)]] 5 µM 9.40× (z +18.8) | — |
| [[NCI-H2030 (line)]] | alt | 127 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.55× (z +10.4) | — |
| [[RKO (line)]] | wt | 219 | 3 | 0 | [[Auranofin (drug)]] 5 µM 9.71× (z +19.2) | — |
| [[RPMI-7951 (line)]] | alt | 146 | 3 | 0 | [[Auranofin (drug)]] 5 µM 6.79× (z +15.3) | — |
| [[SK-MEL-2 (line)]] | alt | 233 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.63× (z +13.1) | — |
| [[SNU-1 (line)]] | wt | 158 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.20× (z +16.9) | — |
| [[SW 900 (line)]] | alt | 194 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.37× (z +15.3) | — |
| [[A549 (line)]] | wt | 201 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.89× (z +8.9) | — |
| [[CHP-212 (line)]] | wt | 193 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.59× (z +8.9) | — |
| [[H4 (line)]] | wt | 131 | 2 | 0 | [[Auranofin (drug)]] 5 µM 7.46× (z +14.6) | — |
| [[HCT15 (line)]] | alt | 198 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.53× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 131 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +12.2) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.93× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 120 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +15.6) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.61× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 132 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.41× (z +12.7) | — |
| [[SW48 (line)]] | wt | 212 | 2 | 0 | [[Auranofin (drug)]] 5 µM 6.61× (z +15.6) | — |
| [[AN3 CA (line)]] | alt | 162 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.62× (z +11.7) | — |
| [[C-33 A (line)]] | alt | 275 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.71× (z +15.4) | — |
| [[NCI-H23 (line)]] | alt | 414 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.97× (z +10.1) | — |
| [[NCI-H596 (line)]] | alt | 172 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.291× (z -11.8) |
| [[SW 1271 (line)]] | alt | 173 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.46× (z +10.8) | — |
| [[NCI-H2122 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 170 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1451), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBB]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[HSPA1B]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 | pathway: HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; STRING 984 |
| [[HSPH1]] | +0.59 | +0.62 / +0.55 | both halves | 1e-05 | STRING 948 |
| [[HSP90AA1]] | +0.59 | +0.65 / +0.57 | both halves | 1e-05 | pathway: HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; STRING 989 |
| [[PSMA4]] | +0.58 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[HSPA1A]] | +0.57 | +0.43 / +0.62 | both halves | 3e-05 | pathway: HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; STRING 956 |
| [[BAG3]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 | STRING 490 |
| [[HSP90AA2P]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[GLA]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[BRD2]] | +0.56 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[RNASEL]] | +0.54 | +0.47 / +0.54 | both halves | 2e-05 | pathway: HALLMARK_APOPTOSIS |
| [[SFXN5]] | +0.53 | +0.56 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P1]] | -0.53 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[SUMF2]] | -0.51 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[VPS16]] | -0.50 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[ENOPH1]] | -0.50 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[ARHGAP1]] | -0.49 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[BTF3L4]] | -0.48 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[TMEM175]] | -0.47 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[NDUFV1]] | -0.47 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[GANAB]] | -0.47 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[ILKAP]] | -0.46 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[SUGP2]] | -0.46 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ARL6IP6]] | -0.46 | -0.34 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-18.3, -10.7); signed map (-24.6, -27.9). **Vector** length 110, 50.2% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Chaperone Mediated Autophagy* (reactome, mean cos +0.52 to 4); *Aggrephagy* (reactome, mean cos +0.55 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.3 | +18.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.6 | +8.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.4 | +6.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.2 | +12.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.8 | +12.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.0 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +0.1 |
|  | [[Abiraterone acetate (drug)]] 0.05 µM |  | +2.7 | +0.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.2 | +0.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | +1.5 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.0 | -0.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.7 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | +1.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.1 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.1 | -2.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.1 — chr9:33,025,273-33,039,907 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPF4, hdj-2, dj-2, NEDD7; previously HSJ2 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Hallmark sets | APOPTOSIS, UV_RESPONSE_UP |
| Reactome | 4 pathways, smallest: Mitochondrial unfolded protein response (UPRmt); HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [P31689](https://www.uniprot.org/uniprotkb/P31689) (DnaJ homolog subfamily A member 1):

> Co-chaperone for HSPA8/Hsc70. Stimulates ATP hydrolysis, but not the folding of unfolded proteins mediated by HSPA1A (in vitro). Plays a role in protein transport into mitochondria via its role as co-chaperone. Functions as a co-chaperone for HSPA1B and negatively regulates the translocation of BAX from the cytosol to mitochondria in response to cellular stress, thereby protecting cells against apoptosis. Promotes apoptosis in response to cellular stress mediated by exposure to anisomycin or UV.

**Summary**, from NCBI Gene [3301](https://www.ncbi.nlm.nih.gov/gene/3301):

> This gene encodes a member of the DnaJ family of proteins, which act as heat shock protein 70 cochaperones. Heat shock proteins facilitate protein folding, trafficking, prevention of aggregation, and proteolytic degradation. Members of this family are characterized by a highly conserved N-terminal J domain, a glycine/phenylalanine-rich region, four CxxCxGxG zinc finger repeats, and a C-terminal substrate-binding domain. The J domain mediates the interaction with heat shock protein 70 to recruit …

**Accessions** — [HGNC:5229](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5229) · Entrez [3301](https://www.ncbi.nlm.nih.gov/gene/3301) · UniProt [P31689](https://www.uniprot.org/uniprotkb/P31689) · Ensembl [ENSG00000086061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086061)

## Data

Gene col 1451: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1451); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1451, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1451]; `tensor/DDL_lfc|DDL_z.npy` [1451]; `embed/gene_vectors.npy` [1451]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1451 or target_col == 1451). Every well: [[DNAJA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
