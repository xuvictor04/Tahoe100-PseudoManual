---
symbol: "ATXN7L3"
type: "gene"
col: 1487
ensembl_id: "ENSG00000087152"
name: "ataxin 7 like 3"
location: "17q21.31"
module: 2
arm: "+"
pooled_cpm: 23.06
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ATXN7L3

*ataxin 7 like 3* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.40× (z +7.3, q 2e-10, up in 26 of 45 measured lines) ⚠ transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.42× (z +5.3, q 3e-05, up in 22 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 4.69×, NCI-H460 2.29×; ⚠ cell-cycle shift, explains ~76% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 3.39×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 2.40×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.687× (z -11.4, q 4e-27, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIER2]] (+0.58, fdr 1e-05), [[PNMA1]] (+0.53, fdr 4e-05), [[BNIP2]] (+0.52, fdr 8e-05); moves opposite to [[HELZ]] (-0.49, fdr 3e-05), [[MIR181A2HG]] (-0.48, fdr 7e-05), [[ACP6]] (-0.47, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1487.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 4.69×, NCI-H460 2.29×; ⚠ cell-cycle shift, explains ~76% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 3.39×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 2.40×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +7.3 | 2e-10 | 26/45 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.42×** | +5.3 | 3e-05 | 22/45 (HOP62, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.8 | 3e-04 | 17/47 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.004 | 15/47 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.0 | 0.006 | 11/36 (NCI-H460, J82, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.20× | +3.9 | 0.010 | 15/47 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.7 | 0.016 | 0/48 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.20× | +3.7 | 0.016 | 16/45 (KATO III, A549, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.3 | 0.058 | 14/47 (RKO, C32, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.17× | +3.3 | 0.059 | 5/48 (LOX-IMVI, HCT15, …) | inconsistent across doses |  |
| [[Gemfibrozil (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.11 | 8/48 (NCI-H23, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1487.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -11.4 | 4e-27 | 33/48 (A-172, SW1417, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.632×** | -9.4 | 1e-18 | 32/46 (A-172, NCI-H23, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.707×** | -7.1 | 2e-10 | 24/47 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.760×** | -5.7 | 2e-06 | 24/47 (A498, C32, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.801×** | -4.6 | 4e-04 | 24/48 (SK-MEL-2, A-172, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.808×** | -4.6 | 4e-04 | 17/46 (KATO III, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.823×** | -4.2 | 0.002 | 14/48 (H4, CFPAC-1, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.825×** | -4.1 | 0.003 | 16/47 (A498, HOP62, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.721×** | -3.7 | 0.015 | 10/32 (NCI-H1573, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -3.6 | 0.015 | 17/48 (A-172, LoVo, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.887× | -3.6 | 0.015 | 13/48 (AsPC-1, LoVo, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.851× | -3.5 | 0.026 | 9/48 (HT-29, A498, …) | rises with dose |  |
| [[Sulfisoxazole (drug)]] 5 µM |  | 0.900× | -3.2 | 0.063 | 5/48 (SW1417, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.859× | -3.0 | 0.100 | 15/37 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | 0.906× | -3.0 | 0.100 | 4/48 (COLO 205, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1487. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 24.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -16.9) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -15.6) |
| [[Hs 766T (line)]] | wt | 14.8 | 0 | 2 (1 ⚠) | — | [[NG25 (drug)]] 5 µM 0.0420× (z -9.6) |
| [[LoVo (line)]] | wt | 24.7 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.357× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 24.4 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0715× (z -11.5) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 19.9 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 19.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.3) ⚠ cell-cycle shift, explains ~76% of this change | [[Dinaciclib (drug)]] 5 µM 0.368× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change |
| [[SK-MEL-2 (line)]] | alt | 27.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -9.3) |
| [[SW48 (line)]] | wt | 22.5 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0959× (z -12.3) |
| [[A-427 (line)]] | wt | 20.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[A498 (line)]] | wt | 40.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -9.6) |
| [[AN3 CA (line)]] | alt | 20.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0767× (z -8.7) |
| [[BT-474 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -9.7) ⚠ cell-cycle shift, explains ~76% of this change |
| [[H4 (line)]] | wt | 22.8 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.193× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 28.2 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0673× (z -14.4) |
| [[HS-578T (line)]] | alt | 20.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -12.6) |
| [[HT-29 (line)]] | alt | 34.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.362× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change |
| [[LOX-IMVI (line)]] | wt | 25.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.134× (z -8.5) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0813× (z -17.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 14.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +14.2) ⚠ cell-cycle shift, explains ~76% of this change | — |
| [[SW1417 (line)]] | alt | 28.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -10.2) |
| [[SW480 (line)]] | alt | 20.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change | — |
| [[A549 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1487), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIER2]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[PNMA1]] | +0.53 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[BNIP2]] | +0.52 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[FASTKD5]] | +0.52 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[TAOK2]] | +0.52 | +0.52 / +0.46 | both halves | 2e-05 | STRING 452 |
| [[SGTA]] | +0.52 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[SCYL1]] | +0.52 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[WDR55]] | +0.52 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[PPP1R12C]] | +0.52 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[PITPNM1]] | +0.52 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[C6orf47]] | +0.51 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[DNAJC14]] | +0.51 | +0.40 / +0.55 | both halves | 5e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HELZ]] | -0.49 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[MIR181A2HG]] | -0.48 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[ACP6]] | -0.47 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[NAP1L1]] | -0.44 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[FOXP4-AS1]] | -0.44 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[MCCC1]] | -0.43 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[ANXA4]] | -0.43 | -0.38 / -0.24 | both halves | 4e-04 |  |
| [[RMDN1]] | -0.43 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[NDUFC1]] | -0.43 | -0.37 / -0.28 | both halves | 3e-04 |  |
| [[MAP4K3-DT]] | -0.43 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[PPP2R3C]] | -0.42 | -0.33 / -0.28 | both halves | 3e-04 |  |
| [[SELENOF]] | -0.42 | -0.30 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ATXN7L3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.468). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.9, -54.9); signed map (-9.1, 28.2). **Vector** length 81.0, 14.4% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.2 | +7.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +2.9 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +2.3 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -11.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.6 | -5.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | -3.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.0 | -4.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | ataxin 7 like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:44,191,805-44,200,113 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761G2113 |
| Gene groups (HGNC) | SAGA complex; Ataxin 7 family |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14CW9](https://www.uniprot.org/uniprotkb/Q14CW9) (Ataxin-7-like protein 3):

> Component of the transcription regulatory histone acetylation (HAT) complex SAGA, a multiprotein complex that activates transcription by remodeling chromatin and mediating histone acetylation and deubiquitination. Within the SAGA complex, participates in a subcomplex that specifically deubiquitinates both histones H2A and H2B. The SAGA complex is recruited to specific gene promoters by activators such as MYC, where it is required for transcription. Required for nuclear receptor-mediated …

**Summary**, from NCBI Gene [56970](https://www.ncbi.nlm.nih.gov/gene/56970):

> Enables transcription coactivator activity. Involved in positive regulation of DNA-templated transcription and regulation of transcription by RNA polymerase II. Located in nucleus. Part of DUBm complex and SAGA complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25416](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25416) · Entrez [56970](https://www.ncbi.nlm.nih.gov/gene/56970) · UniProt [Q14CW9](https://www.uniprot.org/uniprotkb/Q14CW9) · Ensembl [ENSG00000087152](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087152)

## Data

Gene col 1487: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1487); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1487, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1487]; `tensor/DDL_lfc|DDL_z.npy` [1487]; `embed/gene_vectors.npy` [1487]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1487 or target_col == 1487). Every well: [[ATXN7L3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATXN7L3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
