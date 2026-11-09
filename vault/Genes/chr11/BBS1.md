---
symbol: "BBS1"
type: "gene"
col: 10499
ensembl_id: "ENSG00000174483"
name: "Bardet-Biedl syndrome 1"
location: "11q13.2"
module: 64
arm: "+"
pooled_cpm: 22.38
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# BBS1

*Bardet-Biedl syndrome 1* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.53× (z +11.8, q 2e-29, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.499× (z -13.1, q 1e-36, down in 38 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.731× (z -8.7, q 8e-16, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INTU]] (+0.63, fdr 7e-06), [[ZC3HC1]] (+0.63, fdr 7e-06), [[LMAN2L]] (+0.63, fdr 1e-05); moves opposite to [[TBC1D4]] (-0.61, fdr 1e-05), [[CTBP2]] (-0.54, fdr 1e-05), [[GFOD1]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10499.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +11.8 | 2e-29 | 35/47 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.73×** | +10.2 | 4e-22 | 34/48 (PANC-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +7.8 | 1e-12 | 27/47 (PANC-1, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.44×** | +7.2 | 8e-11 | 23/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.28×** | +6.8 | 9e-10 | 26/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +6.6 | 3e-09 | 25/48 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.38×** | +6.4 | 1e-08 | 27/48 (A549, SHP-77, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +6.2 | 4e-08 | 26/48 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.32×** | +5.2 | 1e-05 | 17/43 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +5.0 | 4e-05 | 20/48 (AsPC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.29×** | +4.9 | 4e-05 | 15/48 (A549, HOP62, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.26×** | +4.5 | 3e-04 | 12/48 (A549, BT-474, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.9 | 0.004 | 0/48 | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.19× | +3.4 | 0.028 | 5/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.033 | 13/48 (BT-474, A-427, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.2 | 0.045 | 10/48 (LoVo, MIA PaCa-2, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.045 | 8/48 (HCT15, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.058 | 6/48 (Panc 03.27, AsPC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.063 | 5/48 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +2.9 | 0.098 | 13/48 (HOP62, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10499.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.499×** | -13.1 | 1e-36 | 38/45 (LOX-IMVI, COLO 205, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.731×** | -8.7 | 8e-16 | 30/48 (SW480, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -8.0 | 2e-13 | 28/48 (LOX-IMVI, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.710×** | -6.7 | 2e-09 | 24/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 5 µM |  | **0.658×** | -4.3 | 0.002 | 11/44 (COLO 205, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.805×** | -4.1 | 0.004 | 20/48 (BT-474, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.807×** | -4.1 | 0.004 | 18/47 (H4, NCI-H661, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.765×** | -3.8 | 0.012 | 13/47 (H4, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | 0.843× | -3.4 | 0.049 | 20/41 (A-427, CHP-212, …) | inconsistent across doses | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.726×** | -3.3 | 0.051 | 14/45 (Hs 766T, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Flutamide (drug)]] 5 µM |  | 0.846× | -3.3 | 0.051 | 10/47 (NCI-H661, LS 180, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.801×** | -3.1 | 0.087 | 11/47 (Hs 766T, SW48, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.896× | -3.1 | 0.094 | 11/48 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10499. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 23.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[hTERT-HPNE (line)]] | wt | 19.5 | 0 | 2 (2 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0530× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 21.4 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.195× (z -11.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -10.4) |
| [[PANC-1 (line)]] | alt | 26.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +12.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.346× (z -10.6) ⚠ toxic |
| [[SW480 (line)]] | alt | 32.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.413× (z -9.4) ⚠ toxic |
| [[A498 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.247× (z -9.4) ⚠ toxic |
| [[BT-474 (line)]] | alt | 32.4 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.371× (z -8.6) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.146× (z -10.7) ⚠ toxic |
| [[HCT15 (line)]] | alt | 36.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.180× (z -10.7) |
| [[J82 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.263× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 14.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.140× (z -12.8) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 27.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 17.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 16.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +12.3) | — |
| [[NCI-H460 (line)]] | wt | 18.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.217× (z -10.6) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 31.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -9.5) |
| [[SW 900 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10499), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTU]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ZC3HC1]] | +0.63 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[LMAN2L]] | +0.63 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[MAU2]] | +0.62 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[GAS8]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[DNAJC7]] | +0.62 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[C19orf44]] | +0.61 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[RUFY1]] | +0.61 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[EFCAB7]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[WDR73]] | +0.60 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[RBSN]] | +0.60 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TMEM254]] | +0.60 | +0.48 / +0.63 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D4]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[CTBP2]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[GFOD1]] | -0.50 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[L3MBTL3]] | -0.50 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[CHD7]] | -0.47 | -0.42 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.634). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-28.8, 1.4); signed map (-11.8, -17.9). **Vector** length 86.6, 17.3% of its response variance represented; |z| ≥ 3 in 1,004 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.0 | +10.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.7 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +11.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +4.0 | +6.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +2.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +3.1 |
|  | [[Resveratrol (drug)]] 5 µM |  | +1.2 | -0.2 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | +1.1 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.4 | -8.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.6 | -13.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.8 | -6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -8.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | +0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -3.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.5 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | Bardet-Biedl syndrome 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,510,606-66,533,613 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23590 |
| Gene groups (HGNC) | BBSome |
| Reactome | 5 pathways, smallest: BBSome-mediated cargo-targeting to cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFJ9](https://www.uniprot.org/uniprotkb/Q8NFJ9) (BBSome complex member BBS1):

> The BBSome complex is thought to function as a coat complex required for sorting of specific membrane proteins to the primary cilia. The BBSome complex is required for ciliogenesis but is dispensable for centriolar satellite function. This ciliogenic function is mediated in part by the Rab8 GDP/GTP exchange factor, which localizes to the basal body and contacts the BBSome. Rab8(GTP) enters the primary cilium and promotes extension of the ciliary membrane. Firstly the BBSome associates with the …

**Summary**, from NCBI Gene [582](https://www.ncbi.nlm.nih.gov/gene/582):

> Mutations in this gene have been observed in patients with the major form (type 1) of Bardet-Biedl syndrome. The encoded protein may play a role in eye, limb, cardiac and reproductive system development. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:966](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:966) · Entrez [582](https://www.ncbi.nlm.nih.gov/gene/582) · UniProt [Q8NFJ9](https://www.uniprot.org/uniprotkb/Q8NFJ9) · Ensembl [ENSG00000174483](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174483)

## Data

Gene col 10499: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10499); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10499, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10499]; `tensor/DDL_lfc|DDL_z.npy` [10499]; `embed/gene_vectors.npy` [10499]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10499 or target_col == 10499). Every well: [[BBS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BBS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
