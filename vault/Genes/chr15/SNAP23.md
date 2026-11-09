---
symbol: "SNAP23"
type: "gene"
col: 1703
ensembl_id: "ENSG00000092531"
name: "synaptosome associated protein 23"
location: "15q15.1-q15.2"
module: 25
arm: "+"
pooled_cpm: 50.49
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SNAP23

*synaptosome associated protein 23* — 15q15.1-q15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 5.04× (z +43.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.779× (z -6.8, q 7e-09, down in 26 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.807× (z -5.8, q 2e-06, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VAMP7]] (+0.60, fdr 1e-05), [[RTF2]] (+0.59, fdr 1e-05), [[NUCB1]] (+0.59, fdr 3e-05); moves opposite to [[RPP25]] (-0.61, fdr 5e-05), [[JADE1]] (-0.51, fdr 4e-05), [[OBI1]] (-0.49, fdr 4e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1703.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **5.04×** | +43.8 | 0e+00 | 48/48 (HOP62, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +16.3 | 0e+00 | 43/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.77×** | +14.5 | 1e-45 | 39/48 (CFPAC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +14.4 | 1e-44 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +13.4 | 5e-39 | 33/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +13.2 | 9e-38 | 40/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +12.9 | 6e-36 | 33/39 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +11.1 | 7e-27 | 31/48 (CFPAC-1, A498, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.17×** | +11.0 | 3e-26 | 32/45 (KATO III, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +9.7 | 1e-20 | 33/48 (CFPAC-1, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.40×** | +8.3 | 4e-15 | 25/44 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +7.6 | 1e-12 | 25/48 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.66×** | +7.2 | 3e-11 | 31/49 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.39×** | +6.4 | 6e-09 | 26/49 (CFPAC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +6.1 | 3e-08 | 21/49 (A-172, PANC-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +5.6 | 9e-07 | 13/49 (SNU-1, RKO, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 1.16× | +4.1 | 0.002 | 14/48 (J82, SW480, …) | inconsistent across doses |  |
| [[Trimetrexate (drug)]] 5 µM |  | 1.11× | +3.9 | 0.003 | 1/49 (A498) | top dose only |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.003 | 13/48 (AsPC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.005 | 9/49 (SK-MEL-2, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1703.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.779×** | -6.8 | 7e-09 | 26/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.807×** | -5.8 | 2e-06 | 25/48 (NCI-H1573, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.686×** | -5.3 | 1e-05 | 20/48 (RKO, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **0.822×** | -5.3 | 1e-05 | 23/48 (hTERT-HPNE, NCI-H2030, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.721×** | -4.6 | 4e-04 | 13/48 (AsPC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.848× | -4.5 | 7e-04 | 16/48 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.849× | -4.4 | 7e-04 | 17/48 (HS-578T, LoVo, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.866× | -3.9 | 0.006 | 12/48 (A498, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.856× | -3.9 | 0.006 | 15/47 (A-172, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.870× | -3.8 | 0.008 | 9/49 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.907× | -3.8 | 0.008 | 11/48 (RPMI-7951, CFPAC-1, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.872× | -3.7 | 0.009 | 11/48 (LoVo, A498, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.770×** | -3.7 | 0.009 | 17/48 (NCI-H460, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.913× | -3.5 | 0.018 | 8/48 (A-427, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.882× | -3.4 | 0.025 | 11/49 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.894× | -3.1 | 0.073 | 5/49 (LS 180, A498, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.895× | -3.0 | 0.073 | 12/48 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[venetoclax (drug)]] 0.05 µM |  | 0.889× | -3.0 | 0.073 | 4/49 (NCI-H2122, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1703. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 51.1 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.09× (z +18.3) | — |
| [[CFPAC-1 (line)]] | alt | 60.5 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.75× (z +23.9) | — |
| [[A-172 (line)]] | wt | 53.0 | 4 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 10.3× (z +26.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.449× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 45.2 | 5 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.44× (z +23.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 39.7 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 12.3× (z +22.7) | — |
| [[SNU-423 (line)]] | alt | 40.2 | 5 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 11.7× (z +23.9) | — |
| [[A498 (line)]] | wt | 65.2 | 4 | 0 | [[Auranofin (drug)]] 5 µM 4.00× (z +17.3) | — |
| [[KATO III (line)]] | alt | 55.6 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.99× (z +18.2) | — |
| [[Panc 03.27 (line)]] | alt | 46.6 | 4 | 0 | [[Auranofin (drug)]] 5 µM 8.69× (z +22.1) | — |
| [[SW480 (line)]] | alt | 39.1 | 4 | 0 | [[Auranofin (drug)]] 5 µM 7.07× (z +25.7) | — |
| [[COLO 205 (line)]] | alt | 57.2 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.07× (z +9.4) | [[Harringtonine (drug)]] 5 µM 0.330× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 33.4 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.21× (z +14.3) | — |
| [[HOP62 (line)]] | alt | 42.7 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 19.3× (z +32.8) | — |
| [[RKO (line)]] | wt | 94.6 | 3 | 0 | [[Auranofin (drug)]] 5 µM 7.33× (z +21.6) | — |
| [[SW1417 (line)]] | alt | 49.0 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.43× (z +16.0) | — |
| [[AsPC-1 (line)]] | alt | 74.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.38× (z +13.7) | — |
| [[C32 (line)]] | wt | 36.9 | 2 | 0 | [[Auranofin (drug)]] 5 µM 19.4× (z +25.0) | — |
| [[Hs 766T (line)]] | wt | 77.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.35× (z +13.5) | — |
| [[HS-578T (line)]] | alt | 55.4 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.96× (z +13.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.388× (z -9.3) ⚠ cell-cycle shift, explains ~6% of this change |
| [[J82 (line)]] | alt | 47.6 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.71× (z +10.0) | — |
| [[LoVo (line)]] | wt | 65.1 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.82× (z +17.4) | — |
| [[LS 180 (line)]] | wt | 40.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.02× (z +13.6) | — |
| [[NCI-H2030 (line)]] | alt | 57.9 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.09× (z +15.2) | — |
| [[NCI-H2347 (line)]] | alt | 31.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.52× (z +12.9) | — |
| [[NCI-H460 (line)]] | wt | 37.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.74× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.427× (z -9.3) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 64.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 12.1× (z +22.8) | — |
| [[A-427 (line)]] | wt | 28.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.96× (z +13.9) | — |
| [[AN3 CA (line)]] | alt | 50.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.12× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 35.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 19.4× (z +25.2) | — |
| [[C-33 A (line)]] | alt | 37.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.70× (z +9.1) | — |
| [[H4 (line)]] | wt | 63.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.00× (z +13.0) | — |
| [[HCT15 (line)]] | alt | 52.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.84× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 60.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.8× (z +25.1) | — |
| [[hTERT-HPNE (line)]] | wt | 64.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.20× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 62.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.55× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 45.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.80× (z +21.3) | — |
| [[RPMI-7951 (line)]] | alt | 83.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.89× (z +22.8) | — |
| [[SHP-77 (line)]] | alt | 39.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.51× (z +17.7) | — |
| [[SNU-1 (line)]] | wt | 56.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.14× (z +13.9) | — |
| [[SW 900 (line)]] | alt | 44.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.57× (z +19.2) | — |
| [[SW48 (line)]] | wt | 30.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.55× (z +9.7) | — |
| [[A549 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1703), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAMP7]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 999 |
| [[RTF2]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[NUCB1]] | +0.59 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[CRELD1]] | +0.57 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[ST13]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CRIPT]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[SUDS3]] | +0.55 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[UFD1]] | +0.54 | +0.32 / +0.61 | both halves | 2e-04 |  |
| [[UBFD1]] | +0.54 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[CRYZ]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[GFM2]] | +0.54 | +0.39 / +0.55 | both halves | 6e-05 |  |
| [[ARPC3]] | +0.54 | +0.62 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP25]] | -0.61 | -0.40 / -0.64 | both halves | 5e-05 |  |
| [[JADE1]] | -0.51 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[OBI1]] | -0.49 | -0.25 / -0.57 | both halves | 4e-04 |  |
| [[TMEM250]] | -0.49 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[NFYC]] | -0.49 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[PHACTR4]] | -0.49 | -0.29 / -0.60 | both halves | 3e-04 |  |
| [[MTFP1]] | -0.48 | -0.20 / -0.60 | ⚠ one half (not replicated) | 8e-04 |  |
| [[NOP56]] | -0.48 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[WDR75]] | -0.48 | -0.29 / -0.54 | both halves | 2e-04 |  |
| [[EXOSC9]] | -0.48 | -0.28 / -0.62 | both halves | 3e-04 |  |
| [[SLC12A2-DT]] | -0.47 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[LSM6]] | -0.47 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[ZCCHC3]] | -0.47 | -0.31 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.199). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-23.6, -12.8); signed map (-31.0, -28.5). **Vector** length 113, 28.6% of its response variance represented; |z| ≥ 3 in 1,209 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +13.0 | +43.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.2 | +13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.1 | +12.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.4 | +14.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.8 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.3 | +11.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.0 | +6.4 |
|  | [[Infigratinib (drug)]] 5 µM |  | +3.0 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +5.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.8 | -6.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.7 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -4.5 | -4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -1.6 |
|  | [[EX229 (drug)]] 5 µM |  | -4.2 | -3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.8 | -5.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.8 | -4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | synaptosome associated protein 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1-q15.2 — chr15:42,491,233-42,545,356 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SNAP23A, SNAP23B, HsT17016 |
| Gene groups (HGNC) | SNAREs |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 21 pathways, smallest: RHOF GTPase cycle; RHOJ GTPase cycle; RHOQ GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O00161](https://www.uniprot.org/uniprotkb/O00161) (Synaptosomal-associated protein 23):

> SNAREs (soluble N-ethylmaleimide-sensitive factor-attachment protein receptors) are essential proteins for intracellular membrane fusion. SNAREs localized on opposing membranes assemble to form a trans-SNARE complex, an extended, parallel four-helix bundle whose assembly releases energy that drives membrane fusion. The core SNARE complex typically consists of four alpha-helical domains, three from target membrane SNAREs (t-SNAREs) and one from a vesicle SNARE (v-SNARE). SNAP23 is a t-SNARE …

**Summary**, from NCBI Gene [8773](https://www.ncbi.nlm.nih.gov/gene/8773):

> Specificity of vesicular transport is regulated, in part, by the interaction of a vesicle-associated membrane protein termed synaptobrevin/VAMP with a target compartment membrane protein termed syntaxin. These proteins, together with SNAP25 (synaptosome-associated protein of 25 kDa), form a complex which serves as a binding site for the general membrane fusion machinery. Synaptobrevin/VAMP and syntaxin are believed to be involved in vesicular transport in most, if not all cells, while SNAP25 is …

**Accessions** — [HGNC:11131](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11131) · Entrez [8773](https://www.ncbi.nlm.nih.gov/gene/8773) · UniProt [O00161](https://www.uniprot.org/uniprotkb/O00161) · Ensembl [ENSG00000092531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092531)

## Data

Gene col 1703: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1703); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1703, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1703]; `tensor/DDL_lfc|DDL_z.npy` [1703]; `embed/gene_vectors.npy` [1703]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1703 or target_col == 1703). Every well: [[SNAP23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNAP23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
