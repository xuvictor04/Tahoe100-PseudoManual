---
symbol: "EHMT2"
type: "gene"
col: 12859
ensembl_id: "ENSG00000204371"
name: "euchromatic histone lysine methyltransferase 2"
location: "6p21.33"
module: 17
arm: "+"
pooled_cpm: 21.61
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 24
n_dd_up_clean: 22
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# EHMT2

*euchromatic histone lysine methyltransferase 2* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.92× (z +10.3, q 4e-22, up in 31 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.91× (z +10.2, q 8e-22, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.453× (z -17.6, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALAD]] (+0.78, fdr 7e-06), [[THYN1]] (+0.73, fdr 7e-06), [[RHOT1]] (+0.73, fdr 7e-06); moves opposite to [[LINC01829]] (-0.66, fdr 2e-05), [[GCNT4]] (-0.65, fdr 3e-05), [[CA3]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12859.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +10.3 | 4e-22 | 31/43 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +10.2 | 8e-22 | 38/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +9.9 | 7e-21 | 26/33 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.86×** | +9.8 | 1e-20 | 34/48 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +9.6 | 1e-19 | 35/47 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.83×** | +9.5 | 2e-19 | 42/48 (J82, C32, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.41×** | +7.6 | 2e-12 | 35/48 (RKO, AsPC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +5.4 | 5e-06 | 24/47 (KATO III, J82, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +4.3 | 0.001 | 17/48 (RKO, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.67×** | +4.2 | 0.001 | 19/44 (SW48, NCI-H23, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.004 | 16/47 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.004 | 14/48 (MIA PaCa-2, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **1.30×** | +3.8 | 0.006 | 17/39 (SW1417, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.011 | 12/48 (NCI-H2347, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.17× | +3.6 | 0.011 | 11/48 (H4, LOX-IMVI, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | **1.54×** | +3.6 | 0.011 | 14/45 (NCI-H23, J82, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.011 | 21/48 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.014 | 13/47 (NCI-H23, HepG2/C3A, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.018 | 12/47 (AsPC-1, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12859.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.453×** | -17.6 | 0e+00 | 45/48 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.484×** | -11.4 | 1e-27 | 36/48 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.516×** | -10.4 | 5e-23 | 40/47 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.534×** | -9.5 | 4e-19 | 35/46 (AN3 CA, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.564×** | -9.0 | 3e-17 | 34/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.562×** | -8.7 | 3e-16 | 36/48 (SK-MEL-2, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.598×** | -8.1 | 5e-14 | 32/48 (NCI-H23, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.710×** | -7.6 | 2e-12 | 26/48 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.644×** | -6.9 | 3e-10 | 28/46 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.753×** | -6.3 | 2e-08 | 29/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.672×** | -6.2 | 2e-08 | 26/47 (HT-29, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.662×** | -6.1 | 5e-08 | 29/48 (MIA PaCa-2, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.698×** | -5.7 | 7e-07 | 24/47 (HT-29, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.720×** | -5.2 | 1e-05 | 22/48 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.588×** | -4.4 | 5e-04 | 16/46 (SW480, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.822×** | -4.4 | 5e-04 | 19/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12859. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.4 | 0 | 6 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.263× (z -10.6) |
| [[AN3 CA (line)]] | alt | 64.7 | 0 | 4 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0319× (z -16.4) |
| [[MIA PaCa-2 (line)]] | alt | 28.0 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0919× (z -23.5) |
| [[SW480 (line)]] | alt | 19.4 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +10.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.299× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 37.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 16.3 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -12.8) |
| [[SNU-1 (line)]] | wt | 34.6 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.110× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 23.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -12.6) |
| [[SW1417 (line)]] | alt | 28.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -11.8) |
| [[C-33 A (line)]] | alt | 38.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -12.6) |
| [[C32 (line)]] | wt | 20.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -11.4) |
| [[CHP-212 (line)]] | wt | 26.0 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0753× (z -9.2) ⚠ transcription drop |
| [[HepG2_C3A (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -10.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 16.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -9.8) |
| [[HS-578T (line)]] | alt | 18.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -8.8) |
| [[HT-29 (line)]] | alt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 21.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -9.1) |
| [[LS 180 (line)]] | wt | 32.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 7.70 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0527× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 36.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 32.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -12.9) |
| [[RKO (line)]] | wt | 21.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 22.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -9.0) |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.161× (z -9.4) |
| [[A-172 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12859), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALAD]] | +0.78 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[THYN1]] | +0.73 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[RHOT1]] | +0.73 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[THRA]] | +0.71 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[MRPS31P4]] | +0.68 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[TTC5]] | +0.68 | +0.52 / +0.69 | both halves | 1e-05 | pathway: Regulation of TP53 Activity |
| [[NDUFB10]] | +0.67 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[IRAK1BP1]] | +0.66 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[RAB4A]] | +0.66 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[SPATA6]] | +0.66 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[TNRC6A]] | +0.65 | +0.63 / +0.76 | both halves | 7e-06 | pathway: Cellular Senescence |
| [[TMEM185A]] | +0.65 | +0.61 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01829]] | -0.66 | -0.46 / -0.62 | both halves | 2e-05 |  |
| [[GCNT4]] | -0.65 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[CA3]] | -0.63 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[GPATCH2L]] | -0.63 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[ZNF800]] | -0.62 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[PDK1-AS1]] | -0.62 | -0.40 / -0.64 | both halves | 5e-05 |  |
| [[NIPAL1]] | -0.60 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[SPON1-AS1]] | -0.59 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[S100A11]] | -0.59 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[ZNF341-AS1]] | -0.59 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[RAB22A]] | -0.58 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[MCF2]] | -0.58 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises EHMT2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | B | ABL1 activity lowers EHMT2's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 5.3% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LUCAT1]] | B | LUCAT1 activity lowers EHMT2's level | lines that do not express LUCAT1 (8) vs lines expressing it (42) | 1.71× higher at baseline in the lines without LUCAT1 | 0.075 | ⚠ within organs, on part of the lines; also absent: TBILA, C3orf52, SPAG16 |
| [[BCAM]] | B | BCAM activity raises EHMT2's level | lines that do not express BCAM (8) vs lines expressing it (42) | 1.64× lower at baseline in the lines without BCAM | 0.078 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[SLC44A2]] | C | SLC44A2 activity raises EHMT2's level | lines that do not express SLC44A2 (4) vs lines expressing it (46) | 1.96× lower at baseline in the lines without SLC44A2 | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC45, CLSPN, AURKB; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.753). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-1.6, -8.9); signed map (-27.9, -10.3). **Vector** length 117, 32.2% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +6.3 | +7.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.8 | +9.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.8 | +10.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.5 | +9.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.3 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +3.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.1 | +5.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.2 | -17.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -9.8 | -9.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -8.6 | -8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.7 | -6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -5.7 | -5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.2 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -5.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | euchromatic histone lysine methyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,879,759-31,897,698 (-) |
| Ensembl biotype | protein_coding |
| Also known as | G9A, Em:AF134726.3, NG36/G9a, KMT1C; previously C6orf30, BAT8 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Histone lysine methyltransferases; SET domain containing |
| Reactome | 19 pathways, smallest: Regulation of TP53 Activity through Methylation; Regulation of endogenous retroelements by the Human Silencing Hub (HUSH) complex; ERCC6 (CSB) and EHMT2 (G9a) positively regulate rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96KQ7](https://www.uniprot.org/uniprotkb/Q96KQ7) (Histone-lysine N-methyltransferase EHMT2):

> Histone methyltransferase that specifically mono- and dimethylates 'Lys-9' of histone H3 (H3K9me1 and H3K9me2, respectively) in euchromatin. H3K9me represents a specific tag for epigenetic transcriptional repression by recruiting HP1 proteins to methylated histones. Also mediates monomethylation of 'Lys-56' of histone H3 (H3K56me1) in G1 phase, leading to promote interaction between histone H3 and PCNA and regulating DNA replication. Also weakly methylates 'Lys-27' of histone H3 (H3K27me). Also …

**Summary**, from NCBI Gene [10919](https://www.ncbi.nlm.nih.gov/gene/10919):

> This gene encodes a methyltransferase that methylates lysine residues of histone H3. Methylation of H3 at lysine 9 by this protein results in recruitment of additional epigenetic regulators and repression of transcription. This gene was initially thought to be two different genes, NG36 and G9a, adjacent to each other in the HLA locus. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:14129](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14129) · Entrez [10919](https://www.ncbi.nlm.nih.gov/gene/10919) · UniProt [Q96KQ7](https://www.uniprot.org/uniprotkb/Q96KQ7) · Ensembl [ENSG00000204371](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204371)

## Data

Gene col 12859: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12859); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12859, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12859]; `tensor/DDL_lfc|DDL_z.npy` [12859]; `embed/gene_vectors.npy` [12859]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12859 or target_col == 12859). Every well: [[EHMT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EHMT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
