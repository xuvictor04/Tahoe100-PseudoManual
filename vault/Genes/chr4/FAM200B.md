---
symbol: "FAM200B"
type: "gene"
col: 14148
ensembl_id: "ENSG00000237765"
name: "zinc finger BED-type containing 11"
location: "4p15.32"
module: 68
arm: "+"
pooled_cpm: 11.31
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# FAM200B

*zinc finger BED-type containing 11* — 4p15.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.36× (z +13.2, q 5e-37, up in 33 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +8.2, q 2e-14, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.583× (z -5.9, q 2e-06, down in 27 of 47 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.717× (z -3.6, q 0.052, down in 16 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 2 lines (LOX-IMVI 0.144×, NCI-H460 0.282×; ⚠ cell-cycle shift, explains ~27% of this change); [[Bortezomib (drug)]] 0.05 µM in 2 lines (NCI-H460 0.246×, H4 0.0786×; ⚠ cell-cycle shift, explains ~34% of this change); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (H4 0.0873×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLN5]] (+0.80, fdr 7e-06), [[HHLA3]] (+0.71, fdr 7e-06), [[ETFRF1]] (+0.70, fdr 7e-06); moves opposite to [[GTF2E2]] (-0.69, fdr 3e-05), [[HERC2P2]] (-0.68, fdr 1e-05), [[HERC2P9]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TFAP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14148.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.36×** | +13.2 | 5e-37 | 33/34 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.27×** | +12.7 | 3e-34 | 39/45 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.15×** | +12.0 | 5e-31 | 19/21 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +9.2 | 8e-18 | 25/28 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.24×** | +8.5 | 3e-15 | 34/46 (A-172, J82, …) | rises with dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +8.2 | 2e-14 | 35/46 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +7.7 | 1e-12 | 33/44 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +7.4 | 9e-12 | 34/48 (NCI-H2347, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +7.3 | 1e-11 | 33/40 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.57×** | +4.9 | 4e-05 | 20/40 (Panc 03.27, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.002 | 17/47 (C32, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.9 | 0.005 | 15/39 (SK-MEL-2, SW 900, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.42×** | +3.8 | 0.006 | 19/46 (A-172, C32, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.006 | 20/47 (NCI-H23, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.008 | 18/47 (SNU-423, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.010 | 18/46 (NCI-H2347, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.60×** | +3.1 | 0.054 | 13/41 (SW 900, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.60×** | +3.1 | 0.054 | 5/44 (HCT15, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.1 | 0.054 | 10/47 (A-172, C32, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.58×** | +3.0 | 0.062 | 8/44 (SW48, LS 180, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.062 | 14/45 (HS-578T, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.69×** | +3.0 | 0.068 | 8/40 (A-427, PANC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14148.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 2 lines (LOX-IMVI 0.144×, NCI-H460 0.282×; ⚠ cell-cycle shift, explains ~27% of this change); [[Bortezomib (drug)]] 0.05 µM in 2 lines (NCI-H460 0.246×, H4 0.0786×; ⚠ cell-cycle shift, explains ~34% of this change); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (H4 0.0873×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.583×** | -5.9 | 2e-06 | 27/47 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.625×** | -4.9 | 3e-04 | 22/45 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.717×** | -3.6 | 0.052 | 16/47 (SK-MEL-2, SW 1271, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.537×** | -3.6 | 0.053 | 11/36 (NCI-H460, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.567× | -3.2 | 0.13 | 13/43 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14148. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 21.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +14.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.58× (z +9.5) | — |
| [[H4 (line)]] | wt | 11.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +10.2) ⚠ cell-cycle shift, explains ~37% of this change | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0873× (z -9.0) |
| [[HS-578T (line)]] | alt | 14.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.83× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 15.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +8.5) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.246× (z -9.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HOP62 (line)]] | alt | 11.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +11.5) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[J82 (line)]] | alt | 13.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +9.5) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SNU-423 (line)]] | alt | 12.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.03× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 14.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +9.9) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[A498 (line)]] | wt | 14.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +10.4) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[A549 (line)]] | wt | 10.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.17× (z +10.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 8.66 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +9.7) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[CFPAC-1 (line)]] | alt | 10.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +8.5) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[LOX-IMVI (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.144× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1573 (line)]] | alt | 13.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 8.70 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.29× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 6.81 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +8.6) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[A-427 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14148), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLN5]] | +0.80 | +0.83 / +0.68 | both halves | 7e-06 |  |
| [[HHLA3]] | +0.71 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[ETFRF1]] | +0.70 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[LINC00240]] | +0.70 | +0.76 / +0.47 | both halves | 2e-05 |  |
| [[TRAM2-AS1]] | +0.70 | +0.76 / +0.51 | both halves | 1e-05 |  |
| [[SMIM19]] | +0.69 | +0.77 / +0.46 | both halves | 2e-05 |  |
| [[AK9]] | +0.69 | +0.75 / +0.50 | both halves | 1e-05 |  |
| [[RBMS3-AS3]] | +0.68 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[LGALSL-DT]] | +0.68 | +0.73 / +0.41 | both halves | 4e-05 |  |
| [[TTC32]] | +0.68 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[THAP2]] | +0.68 | +0.77 / +0.48 | both halves | 2e-05 |  |
| [[FAM200A]] | +0.67 | +0.76 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2E2]] | -0.69 | -0.72 / -0.46 | both halves | 3e-05 |  |
| [[HERC2P2]] | -0.68 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[HERC2P9]] | -0.68 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[HERC2]] | -0.66 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[HERC2P3]] | -0.66 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[CTNNBL1]] | -0.65 | -0.72 / -0.42 | both halves | 4e-05 |  |
| [[EPS15L1]] | -0.63 | -0.67 / -0.38 | both halves | 6e-05 |  |
| [[LPCAT1]] | -0.62 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[STRAP]] | -0.62 | -0.66 / -0.46 | both halves | 2e-05 |  |
| [[TBC1D24]] | -0.62 | -0.66 / -0.36 | both halves | 1e-04 |  |
| [[ERI3]] | -0.61 | -0.67 / -0.40 | both halves | 5e-05 |  |
| [[TCOF1]] | -0.61 | -0.54 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TFAP2A]] | B | TFAP2A activity raises FAM200B's level | lines that do not express TFAP2A (5) vs lines expressing it (45) | 1.35× lower at baseline in the lines without TFAP2A | 0.015 | ⚠ within organs, on part of the lines; also absent: FAM111A, PRNP, TRIM34 |
| [[DRAM1]] | B | DRAM1 activity raises FAM200B's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 1.39× lower at baseline in the lines without DRAM1 | 0.025 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises FAM200B's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CLEC2D]] | C | CLEC2D activity raises FAM200B's level | lines that do not express CLEC2D (3) vs lines expressing it (47) | 1.91× lower at baseline in the lines without CLEC2D | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IMPG2, GSTM2, ENSG00000286952; maybe low, not absent; its own permutation p |
| [[TP53]] | C | TP53 activity raises FAM200B's level | lines that do not express TP53 (3) vs lines expressing it (47) | 1.63× lower at baseline in the lines without TP53 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF483, AGK, MCM2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.778). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (2.2, 12.6); signed map (21.5, -14.7). **Vector** length 78.2, 16.2% of its response variance represented; |z| ≥ 3 in 755 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +10.1 | +12.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.0 | +7.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +7.0 | +8.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.4 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +13.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +2.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.1 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.9 | -4.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -0.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger BED-type containing 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.32 — chr4:15,681,662-15,690,447 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C4orf53; previously FAM200B |
| Gene groups (HGNC) | Zinc fingers BED-type |
| Matched by | ensembl_id |

UniProt [P0CF97](https://www.uniprot.org/uniprotkb/P0CF97) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27740](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27740) · Entrez [285550](https://www.ncbi.nlm.nih.gov/gene/285550) · UniProt [P0CF97](https://www.uniprot.org/uniprotkb/P0CF97) · Ensembl [ENSG00000237765](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237765)

## Data

Gene col 14148: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14148); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14148, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14148]; `tensor/DDL_lfc|DDL_z.npy` [14148]; `embed/gene_vectors.npy` [14148]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14148 or target_col == 14148). Every well: [[FAM200B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM200B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
