---
symbol: "PGPEP1"
type: "gene"
col: 5074
ensembl_id: "ENSG00000130517"
name: "pyroglutamyl-peptidase I"
location: "19p13.11"
module: 3
arm: "+"
pooled_cpm: 33.51
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 37
n_dd_up_clean: 15
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PGPEP1

*pyroglutamyl-peptidase I* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.67× (z +6.5, q 6e-08, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.351× (z -18.4, q 0e+00, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YPEL3]] (+0.73, fdr 7e-06), [[UBE2B]] (+0.71, fdr 7e-06), [[PHLDB3]] (+0.68, fdr 7e-06); moves opposite to [[ZMYND11]] (-0.66, fdr 1e-05), [[PSME3]] (-0.65, fdr 7e-06), [[UTP20]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5074.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +6.5 | 6e-08 | 34/46 (HS-578T, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +5.3 | 3e-05 | 26/46 (SHP-77, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +4.9 | 2e-04 | 23/46 (HOP62, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.60×** | +4.2 | 0.003 | 22/45 (HEC-1-A, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.40×** | +4.2 | 0.003 | 28/45 (SW1417, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +4.2 | 0.003 | 25/46 (LoVo, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +3.9 | 0.007 | 19/46 (HEC-1-A, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.009 | 25/45 (SW1417, hTERT-HPNE, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +3.8 | 0.009 | 17/46 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.22×** | +3.6 | 0.017 | 21/46 (HEC-1-A, HCT15, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.017 | 17/46 (LS 180, RPMI-7951, …) | rises with dose |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.021 | 13/46 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.037 | 16/46 (LOX-IMVI, A498, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.3 | 0.038 | 14/45 (A549, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.047 | 17/46 (A-427, LoVo, …) | rises with dose |  |
| [[Ixazomib (drug)]] 5 µM |  | **1.59×** | +3.0 | 0.081 | 13/45 (LOX-IMVI, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.082 | 14/46 (H4, PANC-1, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5074.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.351×** | -18.4 | 0e+00 | 39/45 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.396×** | -16.3 | 0e+00 | 38/46 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.283×** | -15.7 | 0e+00 | 40/44 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.343×** | -12.8 | 3e-35 | 39/46 (SNU-423, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.412×** | -11.0 | 5e-26 | 40/46 (SW1417, Panc 03.27, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.432×** | -10.4 | 2e-23 | 39/46 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.252×** | -8.9 | 3e-17 | 40/45 (SW480, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.509×** | -8.3 | 5e-15 | 33/45 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.299×** | -7.8 | 3e-13 | 40/47 (SNU-423, SW 900, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.555×** | -7.3 | 2e-11 | 38/46 (SW480, SW 900, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.553×** | -7.0 | 1e-10 | 30/45 (SNU-423, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.570×** | -6.9 | 2e-10 | 34/46 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.581×** | -6.4 | 5e-09 | 28/46 (SNU-423, SW480, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.704×** | -6.1 | 4e-08 | 26/46 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.615×** | -5.8 | 3e-07 | 26/44 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.626×** | -5.5 | 2e-06 | 24/45 (LOX-IMVI, AN3 CA, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.655×** | -5.2 | 6e-06 | 30/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.467×** | -4.9 | 2e-05 | 27/44 (MIA PaCa-2, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5074. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 88.5 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0655× (z -30.2) |
| [[SW480 (line)]] | alt | 49.5 | 0 | 11 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -21.1) |
| [[MIA PaCa-2 (line)]] | alt | 38.1 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -21.2) |
| [[NCI-H1792 (line)]] | alt | 22.9 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0626× (z -16.5) |
| [[NCI-H460 (line)]] | wt | 15.1 | 0 | 8 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0898× (z -14.6) |
| [[SW 900 (line)]] | alt | 42.3 | 0 | 8 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.147× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 47.7 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -15.5) |
| [[PANC-1 (line)]] | alt | 33.4 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -18.8) |
| [[CFPAC-1 (line)]] | alt | 46.1 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -14.9) |
| [[HEC-1-A (line)]] | alt | 48.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -17.3) |
| [[HT-29 (line)]] | alt | 45.2 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -17.2) |
| [[COLO 205 (line)]] | alt | 47.9 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -15.9) |
| [[KATO III (line)]] | alt | 37.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 53.0 | 0 | 4 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 26.5 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 28.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -13.9) |
| [[hTERT-HPNE (line)]] | wt | 32.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 24.8 | 0 | 3 (1 ⚠) | — | [[TAK-901 (drug)]] 0.05 µM 0.173× (z -8.9) |
| [[LS 180 (line)]] | wt | 80.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -16.3) |
| [[A549 (line)]] | wt | 19.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -18.1) |
| [[CHP-212 (line)]] | wt | 56.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0845× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.109× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 19.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -15.5) |
| [[NCI-H2347 (line)]] | alt | 41.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -15.1) |
| [[SW1417 (line)]] | alt | 51.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -16.2) |
| [[A-172 (line)]] | wt | 51.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -14.0) |
| [[A498 (line)]] | wt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -10.3) |
| [[HCT15 (line)]] | alt | 60.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.221× (z -10.0) |
| [[HOP62 (line)]] | alt | 16.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -9.2) |
| [[HS-578T (line)]] | alt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -10.1) |
| [[LoVo (line)]] | wt | 47.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 12.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 19.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -9.0) |
| [[RKO (line)]] | wt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.5) |
| [[SHP-77 (line)]] | alt | 18.7 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.170× (z -9.4) |
| [[SW 1271 (line)]] | alt | 52.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -8.7) |
| [[A-427 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.32 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5074), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YPEL3]] | +0.73 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[UBE2B]] | +0.71 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[PHLDB3]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[CBFA2T2]] | +0.68 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[PHF1]] | +0.67 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[MINDY2]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[GABARAPL2]] | +0.66 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[COMMD6]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[MKNK2]] | +0.65 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[TNNI3]] | +0.64 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[CIAO2B]] | +0.64 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[LMBR1L]] | +0.64 | +0.59 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND11]] | -0.66 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[PSME3]] | -0.65 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[UTP20]] | -0.64 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[CPSF2]] | -0.63 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[TASOR]] | -0.63 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[ABCF2]] | -0.62 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[DARS2]] | -0.62 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[PPP2CA]] | -0.61 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[ARSB]] | -0.61 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[DNAJC11]] | -0.60 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[PSME3IP1]] | -0.60 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[ZMPSTE24]] | -0.60 | -0.56 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PGPEP1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.677). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (2.7, -48.2); signed map (-24.9, 13.6). **Vector** length 130, 42.8% of its response variance represented; |z| ≥ 3 in 1,298 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.2 | +5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.8 | +6.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.4 | +4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.3 | +3.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +1.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.8 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +3.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.4 | +2.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.1 | -10.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -16.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.6 | -11.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -12.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -15.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -6.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.8 | -5.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -8.9 |

## What is on record

|  |  |
|---|---|
| Name | pyroglutamyl-peptidase I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,340,598-18,369,950 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PGP-I, Pcp, PGP, PGPI |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXJ5](https://www.uniprot.org/uniprotkb/Q9NXJ5) (Pyroglutamyl-peptidase 1):

> Removes 5-oxoproline from various penultimate amino acid residues except L-proline.

**Summary**, from NCBI Gene [54858](https://www.ncbi.nlm.nih.gov/gene/54858):

> The gene encodes a cysteine protease and member of the peptidase C15 family of proteins. The encoded protein cleaves amino terminal pyroglutamate residues from protein substrates including thyrotropin-releasing hormone and other neuropeptides. Expression of this gene may be downregulated in colorectal cancer, while activity of the encoded protein may be negatively correlated with cancer progression in colorectal cancer patients. Activity of the encoded protease may also be altered in other …

**Accessions** — [HGNC:13568](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13568) · Entrez [54858](https://www.ncbi.nlm.nih.gov/gene/54858) · UniProt [Q9NXJ5](https://www.uniprot.org/uniprotkb/Q9NXJ5) · Ensembl [ENSG00000130517](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130517)

## Data

Gene col 5074: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5074); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5074, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5074]; `tensor/DDL_lfc|DDL_z.npy` [5074]; `embed/gene_vectors.npy` [5074]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5074 or target_col == 5074). Every well: [[PGPEP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGPEP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
