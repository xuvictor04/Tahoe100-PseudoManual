---
symbol: "MREG"
type: "gene"
col: 3973
ensembl_id: "ENSG00000118242"
name: "melanoregulin"
location: "2q35"
module: 20
arm: "+"
pooled_cpm: 29.97
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# MREG

*melanoregulin* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.42× (z +13.0, q 4e-36, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.454× (z -18.8, q 0e+00, down in 36 of 45 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Triamcinolone (drug)]] 5 µM: 0.862× (z -3.5, q 0.025, down in 13 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (MIA PaCa-2 0.106×, NCI-H1573 0.172×, CFPAC-1 0.240×, A549 0.122×, …; ⚠ cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (RKO 0.0779×, C32 0.145×; ⚠ cell-cycle shift, explains ~25% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 0.156×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Auranofin (drug)]] 5 µM in 1 line (CFPAC-1 0.375×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PECR]] (+0.60, fdr 1e-05, ⚠ same locus), [[CDC123]] (+0.48, fdr 2e-04), [[RPL6]] (+0.46, fdr 2e-04), [[CDYL]] (+0.46, fdr 1e-04); moves opposite to [[TOM1L2]] (-0.52, fdr 3e-05), [[RPS6KB2]] (-0.48, fdr 2e-05), [[SAP30]] (-0.47, fdr 3e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAM83B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3973.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.42×** | +13.0 | 4e-36 | 34/47 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.45×** | +8.8 | 5e-16 | 31/46 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +7.1 | 2e-10 | 27/45 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +6.1 | 2e-07 | 18/46 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.33×** | +4.7 | 2e-04 | 18/45 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.32×** | +4.7 | 3e-04 | 15/47 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +4.2 | 0.002 | 16/42 (BT-474, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.28×** | +4.1 | 0.002 | 18/45 (KATO III, LoVo, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.30×** | +4.1 | 0.002 | 17/44 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +3.9 | 0.006 | 15/45 (BT-474, LOX-IMVI, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.056 | 9/42 (PANC-1, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.21×** | +3.2 | 0.056 | 13/45 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.21×** | +3.2 | 0.070 | 18/46 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3973.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (MIA PaCa-2 0.106×, NCI-H1573 0.172×, CFPAC-1 0.240×, A549 0.122×, …; ⚠ cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (RKO 0.0779×, C32 0.145×; ⚠ cell-cycle shift, explains ~25% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 0.156×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Auranofin (drug)]] 5 µM in 1 line (CFPAC-1 0.375×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.454×** | -18.8 | 0e+00 | 36/45 (MIA PaCa-2, NCI-H1573, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.438×** | -13.9 | 2e-41 | 36/46 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.573×** | -9.4 | 1e-18 | 29/45 (RKO, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.614×** | -8.2 | 3e-14 | 30/44 (SW480, C-33 A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.657×** | -7.1 | 2e-10 | 27/44 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.667×** | -6.6 | 5e-09 | 19/31 (LoVo, A549, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~76% of this change | **0.761×** | -4.6 | 3e-04 | 21/41 (LS 180, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.784×** | -4.1 | 0.003 | 19/45 (SNU-1, SW480, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.862× | -3.5 | 0.025 | 13/46 (H4, NCI-H1573, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.864× | -3.5 | 0.027 | 15/46 (RKO, CFPAC-1, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.819×** | -3.4 | 0.040 | 12/47 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.775× | -3.1 | 0.10 | 12/43 (SW48, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | 0.882× | -3.0 | 0.11 | 9/46 (PANC-1, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3973. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 76.0 | 1 | 11 (10 ⚠) | [[TAK-901 (drug)]] 5 µM 7.29× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -17.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.375× (z -8.7) |
| [[RKO (line)]] | wt | 35.8 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0779× (z -14.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A549 (line)]] | wt | 40.7 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -17.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H1573 (line)]] | alt | 134 | 2 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 34.8× (z +13.6) | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -18.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW480 (line)]] | alt | 25.0 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.156× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 13.8 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +11.6) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H23 (line)]] | alt | 49.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -15.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[LoVo (line)]] | wt | 23.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -16.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H2347 (line)]] | alt | 61.5 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.63× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -11.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-427 (line)]] | wt | 25.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -14.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[C32 (line)]] | wt | 104 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -16.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HepG2_C3A (line)]] | wt | 53.1 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.8× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 14.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -9.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H2030 (line)]] | alt | 67.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -14.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H460 (line)]] | wt | 11.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -13.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[RPMI-7951 (line)]] | alt | 14.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -9.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[AsPC-1 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -10.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[BT-474 (line)]] | alt | 53.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 17.9× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0897× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HOP62 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.227× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -9.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[LS 180 (line)]] | wt | 32.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.320× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[MIA PaCa-2 (line)]] | alt | 23.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -20.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[Panc 03.27 (line)]] | alt | 27.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 17.5× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 33.4 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.56× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -12.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SNU-1 (line)]] | wt | 15.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0565× (z -10.8) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SW 900 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A498 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.40 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.17 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3973), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PECR]] | +0.60 | +0.65 / +0.54 | both halves | 1e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[CDC123]] | +0.48 | +0.56 / +0.30 | both halves | 2e-04 |  |
| [[RPL6]] | +0.46 | +0.53 / +0.30 | both halves | 2e-04 |  |
| [[CDYL]] | +0.46 | +0.50 / +0.36 | both halves | 1e-04 |  |
| [[TMEM154]] | +0.45 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[LRRC8D]] | +0.44 | +0.35 / +0.43 | both halves | 1e-04 |  |
| [[TATDN2]] | +0.44 | +0.56 / +0.35 | both halves | 1e-04 |  |
| [[FAM83B]] | +0.43 | +0.46 / +0.37 | both halves | 7e-05 |  |
| [[GTF2F2]] | +0.43 | +0.48 / +0.35 | both halves | 1e-04 |  |
| [[EIF3H]] | +0.43 | +0.55 / +0.25 | both halves | 4e-04 |  |
| [[LCP1]] | +0.42 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[CYRIB]] | +0.42 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[CD276]] | +0.42 | +0.36 / +0.40 | both halves | 1e-04 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOM1L2]] | -0.52 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[RPS6KB2]] | -0.48 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[SAP30]] | -0.47 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[RFX1]] | -0.47 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[RBX1]] | -0.47 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[RASSF1]] | -0.46 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[TMEM91]] | -0.46 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[DLEU2]] | -0.44 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[FAM193A]] | -0.44 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[YY1]] | -0.43 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[PCNT]] | -0.43 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[CEP350]] | -0.43 | -0.43 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83B]] | B | FAM83B activity raises MREG's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 1.72× lower at baseline in the lines without FAM83B | 0.016 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[INAVA]] | B | INAVA activity raises MREG's level | lines that do not express INAVA (29) vs lines expressing it (21) | 1.69× lower at baseline in the lines without INAVA | 0.088 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.311). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (8.7, -44.8); signed map (-16.7, -49.3). **Vector** length 99.3, 22.3% of its response variance represented; |z| ≥ 3 in 1,168 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.7 | +13.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.5 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.9 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +1.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +0.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -5.5 | -18.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.8 | -13.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -4.1 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.7 | -9.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -3.3 | -8.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -3.4 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | -1.4 | -2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | melanoregulin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:215,942,584-216,034,096 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10116, DSU, WDT2 |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N565](https://www.uniprot.org/uniprotkb/Q8N565) (Melanoregulin):

> Probably functions as a cargo-recognition protein that couples cytoplasmic vesicles to the transport machinery. Plays a role in hair pigmentation, a process that involves shedding of melanosome-containing vesicles from melanocytes, followed by phagocytosis of the melanosome-containing vesicles by keratinocytes. Functions on melanosomes as receptor for RILP and the complex formed by RILP and DCTN1, and thereby contributes to retrograde melanosome transport from the cell periphery to the center. …

**Summary**, from NCBI Gene [55686](https://www.ncbi.nlm.nih.gov/gene/55686):

> Predicted to enable phosphatidylinositol binding activity. Predicted to be involved in melanocyte differentiation; melanosome transport; and phagosome maturation. Predicted to act upstream of or within developmental pigmentation. Predicted to be located in late endosome membrane and melanosome membrane. Predicted to be part of protein-containing complex. Predicted to be active in melanosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25478](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25478) · Entrez [55686](https://www.ncbi.nlm.nih.gov/gene/55686) · UniProt [Q8N565](https://www.uniprot.org/uniprotkb/Q8N565) · Ensembl [ENSG00000118242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118242)

## Data

Gene col 3973: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3973); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3973, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3973]; `tensor/DDL_lfc|DDL_z.npy` [3973]; `embed/gene_vectors.npy` [3973]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3973 or target_col == 3973). Every well: [[MREG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MREG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
