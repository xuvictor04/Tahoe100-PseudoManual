---
symbol: "CCNE1"
type: "gene"
col: 2554
ensembl_id: "ENSG00000105173"
name: "cyclin E1"
location: "19q12"
module: 6
arm: "+"
pooled_cpm: 5.89
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CCNE1

*cyclin E1* — 19q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (21 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.67× (z +17.5, q 0e+00, up in 45 of 47 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 2.45× (z +10.1, q 4e-22, up in 35 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.701× (z -4.0, q 0.031, down in 13 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.5 µM in 1 line (A-172 0.0312×); [[Entrectinib (drug)]] 5 µM in 1 line (A-172 0.0487×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.104×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.0691×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAQR4]] (+0.69, fdr 1e-05), [[GPRIN1]] (+0.68, fdr 1e-05), [[MYO9B]] (+0.61, fdr 4e-05); moves opposite to [[AIMP1]] (-0.60, fdr 2e-05), [[OCIAD1]] (-0.59, fdr 7e-05), [[RAD52]] (-0.56, fdr 5e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 21 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2554.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **4.67×** | +17.5 | 0e+00 | 45/47 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **4.55×** | +17.2 | 0e+00 | 45/46 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **4.31×** | +16.6 | 0e+00 | 46/47 (A498, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.04×** | +11.5 | 3e-28 | 25/41 (A498, A549, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.45×** | +10.1 | 4e-22 | 35/43 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +10.1 | 4e-22 | 25/41 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.07×** | +8.3 | 1e-14 | 27/45 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **2.17×** | +8.1 | 3e-14 | 7/15 (CFPAC-1, PANC-1, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **2.09×** | +8.0 | 5e-14 | 16/33 (NCI-H2030, J82, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **2.01×** | +7.6 | 1e-12 | 21/35 (SHP-77, CFPAC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.90×** | +7.3 | 2e-11 | 11/25 (SW480, LoVo, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.86×** | +7.0 | 9e-11 | 30/47 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.82×** | +6.8 | 4e-10 | 21/40 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.66×** | +5.8 | 3e-07 | 19/47 (PANC-1, J82, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +5.7 | 5e-07 | 19/46 (H4, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +4.3 | 5e-04 | 15/45 (HT-29, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +4.2 | 8e-04 | 17/46 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.14×** | +4.0 | 0.001 | 5/45 (HS-578T, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.020 | 6/46 (SNU-423, HT-29, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.023 | 7/41 (NCI-H1792, HS-578T, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2554.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.5 µM in 1 line (A-172 0.0312×); [[Entrectinib (drug)]] 5 µM in 1 line (A-172 0.0487×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.104×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.0691×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.701×** | -4.0 | 0.031 | 13/46 (COLO 205, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.737× | -3.5 | 0.14 | 5/46 (A-427, Hs 766T, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.678× | -3.3 | 0.14 | 9/46 (A-427, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | 0.701× | -3.3 | 0.14 | 7/45 (NCI-H1573, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.748× | -3.2 | 0.14 | 8/47 (SW1417, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.92 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2554. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.96 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.39× (z +16.0) | — |
| [[A-172 (line)]] | wt | 6.65 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0312× (z -13.3) |
| [[PANC-1 (line)]] | alt | 4.09 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.80× (z +8.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A549 (line)]] | wt | 7.14 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.46× (z +12.4) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[H4 (line)]] | wt | 6.55 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0531× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 4.72 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0691× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 9.17 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0836× (z -10.2) ⚠ toxic |
| [[RKO (line)]] | wt | 12.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2554), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAQR4]] | +0.69 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[GPRIN1]] | +0.68 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.61 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[TPST2]] | +0.61 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[GINS2]] | +0.60 | +0.43 / +0.62 | both halves | 3e-05 | pathway: DNA Replication |
| [[KCNC4]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[RECQL4]] | +0.58 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[PGP]] | +0.56 | +0.32 / +0.58 | both halves | 1e-04 |  |
| [[BRI3BP]] | +0.56 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[FANCE]] | +0.56 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[SPATA33]] | +0.56 | +0.32 / +0.57 | both halves | 1e-04 |  |
| [[TMEM201]] | +0.56 | +0.42 / +0.49 | both halves | 4e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AIMP1]] | -0.60 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[OCIAD1]] | -0.59 | -0.38 / -0.60 | both halves | 7e-05 |  |
| [[RAD52]] | -0.56 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[ANXA4]] | -0.56 | -0.54 / -0.40 | both halves | 4e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[C1orf43]] | -0.55 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[CPNE1]] | -0.55 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[TRMT13]] | -0.55 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[PUS10]] | -0.54 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[ZC3H6]] | -0.54 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[VPS13C]] | -0.54 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[CCDC25]] | -0.53 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[CCAR1]] | -0.53 | -0.37 / -0.45 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.449). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-0.4, 15.8); signed map (-40.2, -7.6). **Vector** length 73.8, 13.3% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +5.2 | +17.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.7 | +16.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.6 | +17.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.7 | +10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +8.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.0 | +3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[vincristine (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.3 | +1.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | +1.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.1 | -2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -1.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | cyclin E1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q12 — chr19:29,811,991-29,824,312 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CCNE |
| Gene groups (HGNC) | Cyclins |
| Hallmark sets | UV_RESPONSE_UP, IL2_STAT5_SIGNALING, E2F_TARGETS |
| Reactome | 40 pathways, smallest: Phosphorylation of proteins involved in G1/S transition by active Cyclin E:Cdk2 complexes; PTK6 Regulates Cell Cycle; RHOBTB3 ATPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P24864](https://www.uniprot.org/uniprotkb/P24864) (G1/S-specific cyclin-E1):

> Essential for the control of the cell cycle at the G1/S (start) transition.

**Summary**, from NCBI Gene [898](https://www.ncbi.nlm.nih.gov/gene/898):

> The protein encoded by this gene belongs to the highly conserved cyclin family, whose members are characterized by a dramatic periodicity in protein abundance through the cell cycle. Cyclins function as regulators of CDK kinases. Different cyclins exhibit distinct expression and degradation patterns which contribute to the temporal coordination of each mitotic event. This cyclin forms a complex with and functions as a regulatory subunit of CDK2, whose activity is required for cell cycle G1/S …

**Accessions** — [HGNC:1589](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1589) · Entrez [898](https://www.ncbi.nlm.nih.gov/gene/898) · UniProt [P24864](https://www.uniprot.org/uniprotkb/P24864) · Ensembl [ENSG00000105173](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105173)

## Data

Gene col 2554: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2554); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2554, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2554]; `tensor/DDL_lfc|DDL_z.npy` [2554]; `embed/gene_vectors.npy` [2554]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2554 or target_col == 2554). Every well: [[CCNE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
