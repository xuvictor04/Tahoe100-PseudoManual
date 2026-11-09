---
symbol: "GUSBP2-1"
type: "gene"
col: 16479
ensembl_id: "ENSG00000290474"
name: ""
location: ""
module: 17
arm: "+"
pooled_cpm: 14.93
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 31
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# GUSBP2-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.56× (z +5.7, q 7e-06, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (21 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.371× (z -12.7, q 2e-34, down in 40 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.409× (z -11.5, q 5e-28, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF559]] (+0.66, fdr 8e-06), [[ZNF322]] (+0.63, fdr 1e-05), [[GTF3C2]] (+0.63, fdr 1e-05); moves opposite to [[RELL2]] (-0.63, fdr 4e-05), [[GLS]] (-0.60, fdr 1e-05), [[HOMER1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16479.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.56×** | +5.7 | 7e-06 | 26/47 (CFPAC-1, RKO, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +4.4 | 0.004 | 20/45 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.026 | 21/46 (PANC-1, SW48, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.14 | 11/47 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.28× | +3.2 | 0.14 | 16/46 (NCI-H1792, MIA PaCa-2, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.19× | +3.2 | 0.14 | 7/47 (COLO 205, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.17 | 9/47 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 21 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16479.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.371×** | -12.7 | 2e-34 | 40/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.409×** | -11.5 | 5e-28 | 40/46 (LoVo, CFPAC-1, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.432×** | -10.8 | 7e-25 | 31/45 (SW480, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.419×** | -10.7 | 9e-25 | 41/46 (A-172, SNU-423, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.421×** | -10.7 | 2e-24 | 35/45 (SNU-423, RKO, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.561×** | -10.5 | 1e-23 | 35/46 (HOP62, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.447×** | -10.4 | 3e-23 | 34/46 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.473×** | -9.6 | 4e-20 | 40/46 (MIA PaCa-2, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.491×** | -9.1 | 4e-18 | 36/45 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.608×** | -9.0 | 1e-17 | 32/45 (SHP-77, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.486×** | -8.9 | 2e-17 | 35/47 (Panc 03.27, C-33 A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **0.538×** | -8.0 | 8e-14 | 30/42 (HOP62, RPMI-7951, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.570×** | -6.9 | 2e-10 | 31/43 (MIA PaCa-2, COLO 205, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.588×** | -6.8 | 4e-10 | 30/46 (Panc 03.27, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.598×** | -6.6 | 2e-09 | 27/46 (HOP62, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.628×** | -6.0 | 9e-08 | 26/46 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.612×** | -6.0 | 9e-08 | 28/47 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.756×** | -3.6 | 0.008 | 16/46 (SW 1088, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.585×** | -3.6 | 0.008 | 15/45 (HOP62, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.597×** | -3.4 | 0.013 | 16/47 (SNU-423, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.56 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16479. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 26.0 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -15.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 21.4 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 9.86 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.112× (z -14.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -10.1) |
| [[SW480 (line)]] | alt | 16.5 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0851× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[CFPAC-1 (line)]] | alt | 20.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -11.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.186× (z -9.9) |
| [[J82 (line)]] | alt | 27.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 17.8 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.134× (z -11.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 16.2 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.105× (z -12.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -9.4) |
| [[A498 (line)]] | wt | 11.7 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.154× (z -12.0) |
| [[A549 (line)]] | wt | 12.5 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.178× (z -9.8) |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -12.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[Panc 03.27 (line)]] | alt | 23.0 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -12.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -10.0) |
| [[PANC-1 (line)]] | alt | 6.42 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.217× (z -9.3) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.223× (z -9.1) |
| [[C-33 A (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -11.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 18.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +8.8) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[H4 (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.130× (z -8.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[Hs 766T (line)]] | wt | 6.56 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0565× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[LoVo (line)]] | wt | 18.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.281× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 15.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -9.8) |
| [[RKO (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -9.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[RPMI-7951 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0932× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[SHP-77 (line)]] | alt | 22.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -15.8) |
| [[SK-MEL-2 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.203× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~41% of this change |
| [[SNU-1 (line)]] | wt | 9.62 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0603× (z -9.1) |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0802× (z -10.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW48 (line)]] | wt | 19.0 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.103× (z -8.9) |
| [[A-427 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16479), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF559]] | +0.66 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[ZNF322]] | +0.63 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[GTF3C2]] | +0.63 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[ZNF573]] | +0.61 | +0.40 / +0.67 | both halves | 4e-05 |  |
| [[ZNF594-DT]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[IMMP1L]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[METTL14]] | +0.60 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[ZNF45]] | +0.58 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[ZNF112]] | +0.57 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[SETDB1]] | +0.57 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[MED9]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[THOC1]] | +0.57 | +0.53 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RELL2]] | -0.63 | -0.70 / -0.41 | both halves | 4e-05 |  |
| [[GLS]] | -0.60 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[HOMER1]] | -0.57 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[SLC9A1]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[TEX14]] | -0.54 | -0.49 / -0.54 | both halves | 2e-05 |  |
| [[RELT]] | -0.53 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[KCTD5]] | -0.53 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[SPTBN5]] | -0.52 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[UBR4]] | -0.52 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[LINC00910]] | -0.51 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[CYCS]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[DDX5]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-31.1, -5.8); signed map (-16.4, -18.7). **Vector** length 60.2, 10.5% of its response variance represented; |z| ≥ 3 in 1,126 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | -2.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | -0.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +3.8 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.3 | -8.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.6 | -10.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -10.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -11.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | -6.0 |

## What is on record

> [!warning] No registry record
> GUSBP2-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16479: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16479); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16479, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16479]; `tensor/DDL_lfc|DDL_z.npy` [16479]; `embed/gene_vectors.npy` [16479]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16479 or target_col == 16479). Every well: [[GUSBP2-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GUSBP2-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
