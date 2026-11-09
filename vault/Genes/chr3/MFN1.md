---
symbol: "MFN1"
type: "gene"
col: 10052
ensembl_id: "ENSG00000171109"
name: "mitofusin 1"
location: "3q26.33"
module: 16
arm: "-"
pooled_cpm: 71.0
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# MFN1

*mitofusin 1* — 3q26.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +16.9, q 0e+00, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.615× (z -10.4, q 1e-22, down in 30 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.687× (z -8.4, q 2e-14, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZCCHC17]] (+0.67, fdr 7e-06), [[PIGN]] (+0.67, fdr 7e-06), [[SLC37A3]] (+0.67, fdr 7e-06); moves opposite to [[REPIN1]] (-0.70, fdr 7e-06), [[ZNF620]] (-0.68, fdr 1e-05), [[ZNF776]] (-0.67, fdr 7e-06).
> It sits in the **-** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10052.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +16.9 | 0e+00 | 41/49 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.73×** | +12.7 | 2e-34 | 44/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +11.1 | 3e-26 | 44/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +10.9 | 2e-25 | 45/48 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.42×** | +7.7 | 2e-12 | 33/48 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +5.4 | 6e-06 | 22/48 (BT-474, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +5.4 | 7e-06 | 26/48 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.26×** | +5.3 | 8e-06 | 26/48 (LS 180, HepG2/C3A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.27×** | +5.1 | 2e-05 | 26/48 (HT-29, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.24×** | +4.9 | 6e-05 | 28/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.23×** | +4.7 | 2e-04 | 24/50 (Panc 03.27, C-33 A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +4.2 | 0.001 | 20/48 (A-427, LS 180, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.9 | 0.004 | 15/48 (LoVo, NCI-H2030, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.017 | 12/49 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.021 | 15/48 (NCI-H2030, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.14× | +3.1 | 0.071 | 7/47 (HEC-1-A, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10052.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.615×** | -10.4 | 1e-22 | 30/45 (A-427, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.687×** | -8.4 | 2e-14 | 35/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.761×** | -6.3 | 4e-08 | 24/49 (RKO, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 0.838× | -5.6 | 3e-06 | 22/48 (AN3 CA, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.797×** | -5.3 | 1e-05 | 25/48 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.796×** | -5.1 | 3e-05 | 23/44 (HEC-1-A, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -4.8 | 1e-04 | 2/50 (SW 1271, CHP-212) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.819×** | -4.6 | 3e-04 | 25/48 (A-427, A-172, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | 0.843× | -4.0 | 0.004 | 21/48 (HS-578T, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.798×** | -3.4 | 0.032 | 13/48 (LOX-IMVI, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.872× | -3.2 | 0.074 | 8/47 (J82, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10052. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 56.7 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 89.8 | 4 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.54× (z +9.2) | [[Harringtonine (drug)]] 5 µM 0.434× (z -12.6) |
| [[LoVo (line)]] | wt | 57.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +14.5) | — |
| [[A-172 (line)]] | wt | 90.5 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.377× (z -12.1) |
| [[A-427 (line)]] | wt | 123 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.311× (z -14.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 53.3 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.324× (z -11.6) |
| [[BT-474 (line)]] | alt | 83.7 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.9) | [[Lonafarnib (drug)]] 5 µM 0.186× (z -9.4) ⚠ toxic |
| [[J82 (line)]] | alt | 78.9 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +13.3) | [[Harringtonine (drug)]] 5 µM 0.379× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 84.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.346× (z -12.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 97.4 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -11.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 86.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -12.5) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.236× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 81.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -12.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 47.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +10.7) | — |
| [[RKO (line)]] | wt | 80.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -23.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 100 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -13.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 87.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.394× (z -10.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 76.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +11.8) | — |
| [[A498 (line)]] | wt | 64.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.586× (z -9.7) ⚠ cell-cycle shift, explains ~61% of this change |
| [[AsPC-1 (line)]] | alt | 55.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 76.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -10.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 54.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +13.5) | — |
| [[CHP-212 (line)]] | wt | 56.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 5 µM 0.255× (z -10.0) |
| [[HCT15 (line)]] | alt | 51.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +12.0) | — |
| [[HS-578T (line)]] | alt | 115 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 63.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +13.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 91.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +19.5) | — |
| [[NCI-H1792 (line)]] | alt | 59.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 70.1 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +9.9) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[NCI-H460 (line)]] | wt | 47.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.430× (z -10.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 89.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -14.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 50.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +9.1) | — |
| [[C32 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 69.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 69.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 74.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10052), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC17]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[PIGN]] | +0.67 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[SLC37A3]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[SENP5]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[TOR1B]] | +0.66 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[RARS2]] | +0.65 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[TNPO3]] | +0.65 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[TMED4]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[GOLT1B]] | +0.65 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[GRB2]] | +0.64 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[PIGF]] | +0.64 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[PLEKHA8]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REPIN1]] | -0.70 | -0.73 / -0.61 | both halves | 7e-06 |  |
| [[ZNF620]] | -0.68 | -0.72 / -0.56 | both halves | 1e-05 |  |
| [[ZNF776]] | -0.67 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[ZNF480]] | -0.66 | -0.66 / -0.57 | both halves | 1e-05 |  |
| [[ZNF780A]] | -0.65 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[ZFHX2]] | -0.63 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[OCIAD1]] | -0.63 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[CCDC102A]] | -0.63 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[ZNF554]] | -0.63 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[ZNF606]] | -0.62 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[ZNF260]] | -0.62 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[CLK4]] | -0.61 | -0.53 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MFN1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-28.5, 11.2); signed map (-48.3, -4.5). **Vector** length 100.0, 25.0% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +16.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.5 | +4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +4.2 | +7.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.7 | +5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | +2.2 | +5.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.7 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.4 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.4 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -11.9 | -5.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -10.4 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -9.5 | -4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.1 | -5.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | mitofusin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.33 — chr3:179,347,709-179,394,936 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20693 |
| Gene groups (HGNC) | Mitofusin family |
| Reactome | 10 pathways, smallest: RHOT2 GTPase cycle; Miro GTPase Cycle; PINK1-PRKN Mediated Mitophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWA4](https://www.uniprot.org/uniprotkb/Q8IWA4) (Mitofusin-1):

> Mitochondrial outer membrane GTPase that mediates mitochondrial clustering and fusion. Membrane clustering requires GTPase activity. It may involve a major rearrangement of the coiled coil domains. Mitochondria are highly dynamic organelles, and their morphology is determined by the equilibrium between mitochondrial fusion and fission events. Overexpression induces the formation of mitochondrial networks (in vitro). Has low GTPase activity.

**Summary**, from NCBI Gene [55669](https://www.ncbi.nlm.nih.gov/gene/55669):

> The protein encoded by this gene is a mediator of mitochondrial fusion. This protein and mitofusin 2 are homologs of the Drosophila protein fuzzy onion (Fzo). They are mitochondrial membrane proteins that interact with each other to facilitate mitochondrial targeting. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18262](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18262) · Entrez [55669](https://www.ncbi.nlm.nih.gov/gene/55669) · UniProt [Q8IWA4](https://www.uniprot.org/uniprotkb/Q8IWA4) · Ensembl [ENSG00000171109](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171109)

## Data

Gene col 10052: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10052); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10052, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10052]; `tensor/DDL_lfc|DDL_z.npy` [10052]; `embed/gene_vectors.npy` [10052]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10052 or target_col == 10052). Every well: [[MFN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
