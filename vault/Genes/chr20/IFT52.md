---
symbol: "IFT52"
type: "gene"
col: 2064
ensembl_id: "ENSG00000101052"
name: "intraflagellar transport 52"
location: "20q13.12"
module: 30
arm: "+"
pooled_cpm: 27.97
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# IFT52

*intraflagellar transport 52* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.01× (z +24.8, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.808× (z -6.4, q 1e-07, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAL1]] (+0.70, fdr 7e-06), [[USP30]] (+0.69, fdr 7e-06), [[SKIC3]] (+0.68, fdr 1e-05); moves opposite to [[E2F3]] (-0.64, fdr 1e-05), [[PIGW]] (-0.61, fdr 3e-05), [[EPM2A]] (-0.58, fdr 4e-04).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2064.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.01×** | +24.8 | 0e+00 | 44/47 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.87×** | +23.8 | 0e+00 | 47/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.54×** | +21.1 | 0e+00 | 47/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +12.2 | 3e-32 | 29/46 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +11.9 | 2e-30 | 35/47 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +7.5 | 5e-12 | 17/35 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +7.4 | 9e-12 | 30/47 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +6.6 | 3e-09 | 24/44 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +5.8 | 6e-07 | 21/47 (LoVo, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.30×** | +5.6 | 9e-07 | 16/47 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.18× | +4.8 | 9e-05 | 16/47 (CFPAC-1, RKO, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.22×** | +4.6 | 2e-04 | 16/47 (SNU-423, HOP62, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +4.5 | 3e-04 | 20/43 (HCT15, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | 1.20× | +4.1 | 0.002 | 16/47 (PANC-1, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.19× | +3.9 | 0.003 | 9/47 (SW480, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.005 | 7/46 (KATO III, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.7 | 0.006 | 10/47 (SK-MEL-2, LS 180, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.010 | 13/47 (C-33 A, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +3.6 | 0.011 | 10/47 (HT-29, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.022 | 11/47 (PANC-1, A-427, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.034 | 6/47 (NCI-H2347, HS-578T, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.2 | 0.038 | 8/47 (RKO, LOX-IMVI, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.046 | 10/46 (C-33 A, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2064.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.808×** | -6.4 | 1e-07 | 24/47 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **0.754×** | -6.1 | 3e-07 | 20/46 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.802×** | -4.9 | 1e-04 | 20/47 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.657×** | -4.9 | 1e-04 | 17/46 (HOP62, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **0.825×** | -4.3 | 0.002 | 15/46 (H4, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **0.778×** | -4.0 | 0.006 | 14/47 (HCT15, SNU-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.855× | -3.5 | 0.038 | 17/47 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.852× | -3.4 | 0.040 | 18/47 (RKO, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.864× | -3.3 | 0.060 | 13/47 (NCI-H460, SW480, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.854× | -3.3 | 0.060 | 10/46 (H4, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.896× | -3.1 | 0.085 | 6/47 (HCT15, NCI-H460, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.866× | -3.0 | 0.10 | 7/46 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | 0.873× | -3.0 | 0.10 | 18/46 (A-172, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2064. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 15.6 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.50× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 25.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.65× (z +12.1) | — |
| [[RKO (line)]] | wt | 19.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +11.7) | — |
| [[SW1417 (line)]] | alt | 50.7 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.56× (z +15.8) | — |
| [[SW480 (line)]] | alt | 29.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.56× (z +16.8) | — |
| [[AsPC-1 (line)]] | alt | 12.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.34× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 29.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.39× (z +14.2) | — |
| [[Hs 766T (line)]] | wt | 37.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.05× (z +11.5) | — |
| [[KATO III (line)]] | alt | 24.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.52× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 11.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.9× (z +12.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.29× (z +11.3) | — |
| [[NCI-H2347 (line)]] | alt | 19.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.65× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 24.9 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.72× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -10.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 32.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.48× (z +11.4) | — |
| [[A498 (line)]] | wt | 32.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.74× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 29.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.91× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 22.8 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.84× (z +8.5) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.465× (z -8.5) |
| [[J82 (line)]] | alt | 33.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.98× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 15.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 23.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.47× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 33.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.37× (z +10.8) | — |
| [[A-172 (line)]] | wt | 27.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.389× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[A-427 (line)]] | wt | 47.3 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +8.5) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[COLO 205 (line)]] | alt | 18.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.63× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 27.8 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.188× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 33.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.25× (z +8.5) | — |
| [[A549 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.42 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2064), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAL1]] | +0.70 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[USP30]] | +0.69 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[SKIC3]] | +0.68 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[TSC2]] | +0.68 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[NPHP1]] | +0.67 | +0.58 / +0.50 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 413 |
| [[PLD3]] | +0.67 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[IFT172]] | +0.66 | +0.49 / +0.57 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 997 |
| [[STAM2]] | +0.66 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[TBCE]] | +0.65 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PKN1]] | +0.64 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[CRYZL1]] | +0.64 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[TBCB]] | +0.64 | +0.45 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[E2F3]] | -0.64 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[PIGW]] | -0.61 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[EPM2A]] | -0.58 | -0.48 / -0.25 | both halves | 4e-04 |  |
| [[DGKH]] | -0.58 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[PTPRG]] | -0.58 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ENOX2]] | -0.58 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[SNRPB]] | -0.58 | -0.56 / -0.66 | both halves | 1e-05 |  |
| [[ZNF876P]] | -0.57 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[SATB2]] | -0.56 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[MSRA]] | -0.56 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[C10orf88B]] | -0.56 | -0.53 / -0.27 | both halves | 3e-04 |  |
| [[SPOPL-DT]] | -0.55 | -0.47 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.676). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.4, -3.8); signed map (-34.2, -2.0). **Vector** length 95.5, 21.7% of its response variance represented; |z| ≥ 3 in 958 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +24.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.3 | +21.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.1 | +23.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +3.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.9 | -0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -7.8 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.0 | -6.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.8 | -1.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | -4.9 | -6.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.9 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | +3.7 |

## What is on record

|  |  |
|---|---|
| Name | intraflagellar transport 52 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:43,590,937-43,647,299 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-53, NGD5, dJ1028D15.1, NGD2; previously C20orf9 |
| Gene groups (HGNC) | IFT-B1 complex |
| Reactome | 6 pathways, smallest: Intraflagellar transport; Hedgehog 'off' state; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y366](https://www.uniprot.org/uniprotkb/Q9Y366) (Intraflagellar transport protein 52 homolog):

> Involved in ciliogenesis as part of a complex involved in intraflagellar transport (IFT), the bi-directional movement of particles required for the assembly, maintenance and functioning of primary cilia. Required for the anterograde transport of IFT88.

**Summary**, from NCBI Gene [51098](https://www.ncbi.nlm.nih.gov/gene/51098):

> This gene encodes a conserved proline-rich protein that is a component of the intraflagellar transport-B (IFT-B) core complex. The encoded protein is essential for the integrity of the IFT-B core complex, and for biosynthesis and maintenance of cilia. Mutations in this gene are associated with ciliopathy that affects the skeleton. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:15901](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15901) · Entrez [51098](https://www.ncbi.nlm.nih.gov/gene/51098) · UniProt [Q9Y366](https://www.uniprot.org/uniprotkb/Q9Y366) · Ensembl [ENSG00000101052](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101052)

## Data

Gene col 2064: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2064); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2064, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2064]; `tensor/DDL_lfc|DDL_z.npy` [2064]; `embed/gene_vectors.npy` [2064]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2064 or target_col == 2064). Every well: [[IFT52 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFT52.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
