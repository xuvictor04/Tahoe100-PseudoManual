---
symbol: "GDAP1"
type: "gene"
col: 2453
ensembl_id: "ENSG00000104381"
name: "ganglioside induced differentiation associated protein 1"
location: "8q21.11"
module: 16
arm: "+"
pooled_cpm: 19.16
n_lines_expressing: 44
n_dd_up: 46
n_dd_down: 12
n_dd_up_clean: 38
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 8
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# GDAP1

*ganglioside induced differentiation associated protein 1* — 8q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 46 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.91× (z +36.6, q 0e+00, up in 39 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.649× (z -5.8, q 4e-06, down in 21 of 41 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMYM4]] (+0.73, fdr 7e-06), [[ZBED9]] (+0.72, fdr 7e-06), [[FNBP1P1]] (+0.72, fdr 1e-05); moves opposite to [[EEF1AKMT4]] (-0.70, fdr 7e-06), [[KIAA1958]] (-0.67, fdr 1e-05), [[HEBP1]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ZNF793]] → it (grade B ⚠); 8 go from it, the strongest it → [[TRAM2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 46 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2453.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.91×** | +36.6 | 0e+00 | 39/39 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.23×** | +24.5 | 0e+00 | 39/39 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **5.01×** | +20.7 | 0e+00 | 38/40 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.91×** | +14.3 | 4e-44 | 36/41 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.76×** | +13.6 | 7e-40 | 37/40 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.74×** | +13.4 | 3e-39 | 35/41 (A498, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.97×** | +12.8 | 2e-35 | 36/42 (NCI-H2347, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +12.4 | 2e-33 | 18/22 (NCI-H1573, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.44×** | +11.9 | 5e-31 | 26/32 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +11.3 | 6e-28 | 23/40 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.45×** | +11.1 | 9e-27 | 20/27 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.19×** | +10.4 | 7e-24 | 35/41 (A498, RKO, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.87×** | +8.4 | 2e-15 | 29/40 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.91×** | +8.3 | 3e-15 | 20/33 (A498, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +7.8 | 2e-13 | 26/42 (A498, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.90×** | +7.2 | 2e-11 | 27/40 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +6.5 | 3e-09 | 18/42 (NCI-H1573, SW1417, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +6.0 | 8e-08 | 14/40 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +5.8 | 2e-07 | 20/41 (RKO, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2453.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.649×** | -5.8 | 4e-06 | 21/41 (C-33 A, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.665×** | -5.5 | 1e-05 | 17/41 (LOX-IMVI, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Infigratinib (drug)]] 5 µM |  | **0.508×** | -4.7 | 4e-04 | 18/39 (HOP62, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.705×** | -4.7 | 4e-04 | 17/39 (LOX-IMVI, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.707×** | -4.7 | 4e-04 | 16/41 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.718×** | -4.5 | 8e-04 | 12/41 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.802×** | -4.2 | 0.002 | 18/42 (CFPAC-1, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.737×** | -4.1 | 0.003 | 13/41 (C-33 A, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.745×** | -4.0 | 0.005 | 16/42 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.774×** | -3.3 | 0.052 | 14/41 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.710×** | -3.3 | 0.053 | 10/38 (LOX-IMVI, A549, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.843× | -3.3 | 0.053 | 7/42 (RPMI-7951, PANC-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.645×** | -3.1 | 0.090 | 14/36 (C32, A549, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2453. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 5.39 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +17.0) | — |
| [[NCI-H460 (line)]] | wt | 9.39 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.63× (z +18.9) | — |
| [[LoVo (line)]] | wt | 14.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.96× (z +17.5) | — |
| [[NCI-H2347 (line)]] | alt | 9.91 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.26× (z +15.2) | — |
| [[SW480 (line)]] | alt | 40.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +21.0) | — |
| [[A549 (line)]] | wt | 20.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +13.5) | — |
| [[HS-578T (line)]] | alt | 5.51 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +13.1) | — |
| [[NCI-H1573 (line)]] | alt | 32.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +18.4) | — |
| [[PANC-1 (line)]] | alt | 8.25 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +17.4) | — |
| [[RKO (line)]] | wt | 12.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.5× (z +17.5) | — |
| [[A-427 (line)]] | wt | 21.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.76× (z +11.1) | — |
| [[C-33 A (line)]] | alt | 32.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +9.8) | [[Digitoxin (drug)]] 0.5 µM 0.189× (z -9.2) |
| [[C32 (line)]] | wt | 25.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 5.63 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.44× (z +13.8) | — |
| [[LOX-IMVI (line)]] | wt | 45.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +15.3) | — |
| [[NCI-H2030 (line)]] | alt | 24.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.91× (z +17.3) | — |
| [[RPMI-7951 (line)]] | alt | 9.91 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.92× (z +11.8) | — |
| [[SHP-77 (line)]] | alt | 263 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +14.9) | — |
| [[SK-MEL-2 (line)]] | alt | 19.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.95× (z +17.0) | — |
| [[SW 900 (line)]] | alt | 9.99 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.63× (z +11.3) | — |
| [[BT-474 (line)]] | alt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.30× (z +12.6) | — |
| [[CHP-212 (line)]] | wt | 8.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +8.6) | — |
| [[H4 (line)]] | wt | 8.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.9× (z +11.0) | — |
| [[HCT15 (line)]] | alt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +13.7) | — |
| [[HepG2_C3A (line)]] | wt | 6.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 15.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +12.5) | — |
| [[J82 (line)]] | alt | 6.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.50 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0512× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 10.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.06× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 22.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +13.3) | — |
| [[SNU-423 (line)]] | alt | 5.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +8.5) | — |
| [[SW48 (line)]] | wt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.81× (z +10.9) | — |
| [[A-172 (line)]] | wt | 4.66 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.59 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2453), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM4]] | +0.73 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[ZBED9]] | +0.72 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[FNBP1P1]] | +0.72 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[ZNF620]] | +0.72 | +0.79 / +0.59 | both halves | 7e-06 |  |
| [[ZNF268]] | +0.68 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[LYRM2]] | +0.68 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[ZSCAN30]] | +0.67 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | +0.67 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[ZNF260]] | +0.66 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[PABIR1]] | +0.65 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[TASOR]] | +0.65 | +0.74 / +0.43 | both halves | 3e-05 |  |
| [[ZNF252P-1]] | +0.64 | +0.74 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF1AKMT4]] | -0.70 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[KIAA1958]] | -0.67 | -0.70 / -0.52 | both halves | 1e-05 |  |
| [[HEBP1]] | -0.67 | -0.67 / -0.49 | both halves | 1e-05 |  |
| [[UQCRH]] | -0.67 | -0.70 / -0.55 | both halves | 1e-05 |  |
| [[STK32C]] | -0.65 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.64 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[TAF5]] | -0.64 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[KYAT1]] | -0.64 | -0.70 / -0.36 | both halves | 9e-05 |  |
| [[MPG]] | -0.63 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[SLC37A3]] | -0.62 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[DCUN1D2]] | -0.61 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[SLC25A5]] | -0.61 | -0.50 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF793]] | B | ZNF793 activity raises GDAP1's level | lines that do not express ZNF793 (22) vs lines expressing it (28) | 1.96× lower at baseline in the lines without ZNF793 | 0.083 | ⚠ within organs, on part of the lines; also absent: PEG10, MAP6, ZNF570 |
| [[ZNF518B]] | B | ZNF518B activity lowers GDAP1's level | lines that do not express ZNF518B (16) vs lines expressing it (34) | 1.28× higher at baseline in the lines without ZNF518B | 0.084 | ⚠ within organs, on part of the lines; also absent: EHD3, KCNG1, TUB |
| [[DGKE]] | B | DGKE activity lowers GDAP1's level | lines that do not express DGKE (12) vs lines expressing it (38) | 1.43× higher at baseline in the lines without DGKE | 0.089 | ⚠ within organs, on part of the lines; also absent: TNFRSF1B, TNFRSF10D, HHEX; maybe low, not absent; its own permutation p |
| [[TOP2A]] | B | TOP2A activity lowers GDAP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.2% of all compounds | 0.095 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRAM2-AS1]] | B | GDAP1 activity raises TRAM2-AS1's level | lines that do not express GDAP1 (6) vs lines expressing it (44) | 1.48× lower at baseline in the lines without GDAP1 | 0.048 | ⚠ within organs, on part of the lines; also absent: HHAT, PHC1, LINC00888; maybe low, not absent |
| [[TEX9]] | B | GDAP1 activity raises TEX9's level | lines that do not express GDAP1 (6) vs lines expressing it (44) | 2.41× lower at baseline in the lines without GDAP1 | 0.050 | ⚠ within organs, on part of the lines; also absent: HHAT, PHC1, LINC00888; maybe low, not absent |
| [[CASTOR3P]] | B | GDAP1 activity raises CASTOR3P's level | lines that do not express GDAP1 (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without GDAP1 | 0.054 | ⚠ within organs, on part of the lines; also absent: HHAT, PHC1, LINC00888; maybe low, not absent |
| [[ATP6AP1L]] | B | GDAP1 activity raises ATP6AP1L's level | lines that do not express GDAP1 (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without GDAP1 | 0.057 | ⚠ within organs, on part of the lines; also absent: HHAT, PHC1, LINC00888; maybe low, not absent |
| [[ZMYM4]] | B | GDAP1 activity raises ZMYM4's level | lines that do not express GDAP1 (6) vs lines expressing it (44) | 1.69× lower at baseline in the lines without GDAP1 | 0.061 | ⚠ within organs, on part of the lines; also absent: HHAT, PHC1, LINC00888; maybe low, not absent |
| [[ZKSCAN2]] | B | GDAP1 activity raises ZKSCAN2's level | lines that do not express GDAP1 (6) vs lines expressing it (44) | 1.43× lower at baseline in the lines without GDAP1 | 0.085 | ⚠ within organs, on part of the lines; also absent: HHAT, PHC1, LINC00888; maybe low, not absent |
| [[PBX2]] | B | GDAP1 activity raises PBX2's level | lines that do not express GDAP1 (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without GDAP1 | 0.096 | ⚠ within organs, on part of the lines; also absent: HHAT, PHC1, LINC00888; maybe low, not absent |
| [[TCTN1]] | C | GDAP1 activity raises TCTN1's level | lines that do not express GDAP1 (6) vs lines expressing it (44) | 2.34× lower at baseline in the lines without GDAP1 | 0.030 | ⚠ within organs, on part of the lines; also absent: HHAT, PHC1, LINC00888; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.724). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-27.8, 12.8); signed map (5.0, -26.4). **Vector** length 89.3, 19.8% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.5 | +20.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +24.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +36.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.0 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +11.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +7.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +6.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +5.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +4.3 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +0.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.7 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -5.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.3 | +10.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -2.2 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.8 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +3.7 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.6 | -3.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ganglioside induced differentiation associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.11 — chr8:74,320,613-74,518,007 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CMT4, CMT2K; previously CMT4A |
| Reactome | 2 pathways, smallest: Class I peroxisomal membrane protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TB36](https://www.uniprot.org/uniprotkb/Q8TB36) (Ganglioside-induced differentiation-associated protein 1):

> Regulates the mitochondrial network by promoting mitochondrial fission.

**Summary**, from NCBI Gene [54332](https://www.ncbi.nlm.nih.gov/gene/54332):

> This gene encodes a member of the ganglioside-induced differentiation-associated protein family, which may play a role in a signal transduction pathway during neuronal development. Mutations in this gene have been associated with various forms of Charcot-Marie-Tooth Disease and neuropathy. Two transcript variants encoding different isoforms and a noncoding variant have been identified for this gene. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:15968](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15968) · Entrez [54332](https://www.ncbi.nlm.nih.gov/gene/54332) · UniProt [Q8TB36](https://www.uniprot.org/uniprotkb/Q8TB36) · Ensembl [ENSG00000104381](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104381)

## Data

Gene col 2453: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2453); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2453, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2453]; `tensor/DDL_lfc|DDL_z.npy` [2453]; `embed/gene_vectors.npy` [2453]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2453 or target_col == 2453). Every well: [[GDAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GDAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
