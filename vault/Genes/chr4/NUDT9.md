---
symbol: "NUDT9"
type: "gene"
col: 9965
ensembl_id: "ENSG00000170502"
name: "nudix hydrolase 9"
location: "4q22.1"
module: 64
arm: "+"
pooled_cpm: 21.38
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 21
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# NUDT9

*nudix hydrolase 9* — 4q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.73× (z +17.1, q 0e+00, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.783× (z -7.7, q 9e-12, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TYW3]] (+0.71, fdr 7e-06), [[FECH]] (+0.69, fdr 7e-06), [[ZNF780A]] (+0.68, fdr 7e-06); moves opposite to [[LINC01128]] (-0.62, fdr 1e-05), [[RELL1]] (-0.61, fdr 1e-05), [[ODF2]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9965.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +17.1 | 0e+00 | 38/47 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.03×** | +15.7 | 0e+00 | 42/48 (C32, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +14.2 | 2e-43 | 28/35 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.86×** | +13.7 | 2e-40 | 35/48 (A498, NCI-H2347, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +13.4 | 1e-38 | 34/43 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.86×** | +13.1 | 2e-37 | 43/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +11.5 | 1e-28 | 34/48 (SK-MEL-2, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.68×** | +11.4 | 2e-28 | 31/47 (A498, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +9.7 | 1e-20 | 33/47 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.69×** | +9.5 | 1e-19 | 29/48 (A498, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.01×** | +8.1 | 4e-14 | 27/48 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +7.7 | 4e-13 | 23/37 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +7.7 | 8e-13 | 25/47 (SK-MEL-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.81×** | +6.8 | 3e-10 | 25/45 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.40×** | +6.3 | 9e-09 | 22/48 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.41×** | +5.4 | 3e-06 | 16/48 (A498, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +5.1 | 1e-05 | 15/48 (LS 180, C32, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.23×** | +4.6 | 1e-04 | 19/48 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +4.4 | 4e-04 | 15/48 (NCI-H1573, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9965.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.783×** | -7.7 | 9e-12 | 26/48 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.792×** | -5.2 | 6e-05 | 19/48 (SW480, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.804×** | -4.7 | 5e-04 | 15/46 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.744×** | -3.4 | 0.085 | 9/46 (SW480, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.874× | -3.0 | 0.28 | 13/46 (LS 180, SNU-1, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9965. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 34.8 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.15× (z +10.4) | — |
| [[A-172 (line)]] | wt | 18.6 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.72× (z +10.4) | — |
| [[A498 (line)]] | wt | 31.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.66× (z +15.5) | — |
| [[A549 (line)]] | wt | 14.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 40.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.87× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 20.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.0) | — |
| [[A-427 (line)]] | wt | 31.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -10.6) |
| [[HOP62 (line)]] | alt | 14.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.21× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -12.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 30.2 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.209× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -9.0) |
| [[C-33 A (line)]] | alt | 28.4 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.157× (z -11.7) |
| [[C32 (line)]] | wt | 19.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.18× (z +13.7) | — |
| [[HT-29 (line)]] | alt | 21.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.155× (z -9.4) ⚠ transcription drop; cell-cycle shift, explains ~6% of this change |
| [[LOX-IMVI (line)]] | wt | 12.0 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.04× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 17.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +9.7) | — |
| [[NCI-H460 (line)]] | wt | 18.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +9.3) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -10.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.128× (z -9.0) |
| [[SHP-77 (line)]] | alt | 30.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 28.6 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.24× (z +10.3) ⚠ toxic | — |
| [[SW480 (line)]] | alt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9965), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYW3]] | +0.71 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[FECH]] | +0.69 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[ZNF780A]] | +0.68 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[PLRG1]] | +0.68 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[TCTN1]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[CUL5]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[DNAJC7]] | +0.68 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[DDX1]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[MTA3]] | +0.67 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[ZFP37]] | +0.66 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[COPS5]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[FUNDC1]] | +0.65 | +0.72 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01128]] | -0.62 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[RELL1]] | -0.61 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[ODF2]] | -0.58 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[ASF1B]] | -0.57 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[SRGAP2B]] | -0.57 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.57 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[TAF5]] | -0.57 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[NARF]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[SNX25]] | -0.55 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[TMEM41A]] | -0.55 | -0.46 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.798). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-22.9, 4.4); signed map (8.1, -31.9). **Vector** length 95.8, 20.9% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.2 | +15.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.8 | +11.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +17.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.2 | +9.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +9.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | +13.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.9 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +4.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -7.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.0 | -5.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.7 | -3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | nudix hydrolase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.1 — chr4:87,422,573-87,459,455 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3037 |
| Gene groups (HGNC) | Nudix hydrolase family |
| Hallmark sets | DNA_REPAIR |
| Reactome | 4 pathways, smallest: Phosphate bond hydrolysis by NUDT proteins; Purine catabolism; Nucleotide catabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BW91](https://www.uniprot.org/uniprotkb/Q9BW91) (ADP-ribose pyrophosphatase):

> Hydrolyzes ADP-ribose (ADPR) to AMP and ribose 5'-phosphate. Has also a weak phosphohydrolase activity against NADH and FAD (in vitro).

**Summary**, from NCBI Gene [53343](https://www.ncbi.nlm.nih.gov/gene/53343):

> The protein encoded by this gene belongs to the Nudix hydrolase family. Nudix boxes are found in a family of diverse enzymes that catalyze the hydrolysis of nucleoside diphosphate derivatives. This enzyme is an ADP-ribose pyrophosphatase that catalyzes the hydrolysis of ADP-ribose to AMP and ribose-5-P. It requires divalent metal ions and an intact Nudix motif for enzymatic activity. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided …

**Accessions** — [HGNC:8056](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8056) · Entrez [53343](https://www.ncbi.nlm.nih.gov/gene/53343) · UniProt [Q9BW91](https://www.uniprot.org/uniprotkb/Q9BW91) · Ensembl [ENSG00000170502](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170502)

## Data

Gene col 9965: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9965); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9965, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9965]; `tensor/DDL_lfc|DDL_z.npy` [9965]; `embed/gene_vectors.npy` [9965]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9965 or target_col == 9965). Every well: [[NUDT9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
