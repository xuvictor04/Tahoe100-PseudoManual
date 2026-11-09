---
symbol: "PNPO"
type: "gene"
col: 2947
ensembl_id: "ENSG00000108439"
name: "pyridoxamine 5'-phosphate oxidase"
location: "17q21.32"
module: 25
arm: "+"
pooled_cpm: 9.48
n_lines_expressing: 49
n_dd_up: 35
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# PNPO

*pyridoxamine 5'-phosphate oxidase* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.24× (z +20.5, q 0e+00, up in 30 of 31 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.04× (z +11.2, q 3e-27, up in 32 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.662× (z -4.7, q 0.002, down in 20 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 2 lines (LS 180 0.189×, J82 0.148×; ⚠ cell-cycle shift, explains ~52% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (A-172 0.104×, SHP-77 0.0996×; ⚠ toxic; transcription drop); [[Saquinavir (drug)]] 0.5 µM in 1 line (A549 0.0561×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0738×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBBP9]] (+0.73, fdr 7e-06), [[GSS]] (+0.71, fdr 7e-06), [[ALG10B]] (+0.70, fdr 7e-06); moves opposite to [[RPLP2]] (-0.74, fdr 7e-06), [[RPL18]] (-0.74, fdr 7e-06, ⚠ RPL18 in the vector space only through flagged drug-doses), [[RPL36]] (-0.73, fdr 7e-06), [[RPS29]] (-0.73, fdr 7e-06).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2947.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **6.24×** | +20.5 | 0e+00 | 30/31 (SW480, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **5.79×** | +18.9 | 0e+00 | 16/16 (A498, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **5.09×** | +16.8 | 0e+00 | 26/26 (SW480, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +11.2 | 3e-27 | 32/40 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.02×** | +7.5 | 5e-12 | 31/44 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.02×** | +7.5 | 5e-12 | 29/41 (NCI-H460, HEC-1-A, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.95×** | +7.4 | 1e-11 | 31/46 (HOP62, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.93×** | +7.3 | 2e-11 | 34/45 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.92×** | +7.3 | 2e-11 | 28/46 (HOP62, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +7.2 | 2e-11 | 25/46 (J82, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.58×** | +7.2 | 3e-11 | 27/41 (A-427, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.95×** | +7.1 | 5e-11 | 20/37 (KATO III, A-172, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.93×** | +7.0 | 9e-11 | 27/41 (A498, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +5.9 | 2e-07 | 21/40 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.68×** | +5.8 | 3e-07 | 25/45 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.62×** | +5.3 | 5e-06 | 19/45 (A-427, HOP62, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +5.1 | 1e-05 | 17/43 (SNU-423, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +5.1 | 1e-05 | 21/45 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **2.09×** | +4.3 | 5e-04 | 16/43 (NCI-H460, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.004 | 14/47 (A-172, HS-578T, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.010 | 18/43 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.82×** | +3.5 | 0.012 | 5/46 (A498, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.74×** | +3.2 | 0.025 | 5/41 (KATO III, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +2.9 | 0.073 | 5/46 (SW1417, A498, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.64×** | +2.9 | 0.073 | 4/43 (A498, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2947.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 2 lines (LS 180 0.189×, J82 0.148×; ⚠ cell-cycle shift, explains ~52% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (A-172 0.104×, SHP-77 0.0996×; ⚠ toxic; transcription drop); [[Saquinavir (drug)]] 0.5 µM in 1 line (A549 0.0561×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0738×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.662×** | -4.7 | 0.002 | 20/45 (LS 180, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.682×** | -4.1 | 0.012 | 14/43 (SW48, Hs 766T, …) | inconsistent across doses |  |
| [[Bergenin (drug)]] 0.5 µM |  | 0.737× | -3.5 | 0.10 | 13/43 (NCI-H460, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.743× | -3.4 | 0.10 | 14/46 (SW1417, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.750× | -3.3 | 0.12 | 20/44 (HepG2/C3A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.77 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2947. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 20.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 29.4 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Bortezomib (drug)]] 0.05 µM 0.189× (z -10.4) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HEC-1-A (line)]] | alt | 17.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.13× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HOP62 (line)]] | alt | 4.38 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.1× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 22.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.46× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SNU-423 (line)]] | alt | 7.53 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.0× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW480 (line)]] | alt | 11.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.86× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A549 (line)]] | wt | 6.74 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 14.3× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Saquinavir (drug)]] 0.5 µM 0.0561× (z -11.2) |
| [[HS-578T (line)]] | alt | 5.27 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.4× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[J82 (line)]] | alt | 7.87 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.99× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Bortezomib (drug)]] 0.05 µM 0.148× (z -8.6) ⚠ cell-cycle shift, explains ~52% of this change |
| [[PANC-1 (line)]] | alt | 5.35 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.13× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW1417 (line)]] | alt | 18.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-172 (line)]] | wt | 6.40 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -9.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 6.27 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.76× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 9.21 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.02× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LOX-IMVI (line)]] | wt | 5.66 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0738× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 5.57 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.1× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 6.96 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 18.9× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 8.04 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.09× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2347 (line)]] | alt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 6.26 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.63× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SHP-77 (line)]] | alt | 9.16 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0996× (z -9.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2947), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP9]] | +0.73 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[GSS]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[ALG10B]] | +0.70 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[FH]] | +0.69 | +0.79 / +0.60 | both halves | 7e-06 | STRING 437 |
| [[COX11]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[GUF1]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[VARS1]] | +0.66 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[SNX17]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[DARS2]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[ALG10]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[MBNL3]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[SIGMAR1]] | +0.65 | +0.53 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 18 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 6 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPLP2]] | -0.74 | -0.70 / -0.74 | both halves | 7e-06 |  |
| [[RPL18]] ⚠ | -0.74 | -0.67 / -0.69 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36]] | -0.73 | -0.68 / -0.69 | both halves | 7e-06 |  |
| [[RPL36AL]] ⚠ | -0.73 | -0.75 / -0.63 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS29]] | -0.73 | -0.66 / -0.73 | both halves | 7e-06 |  |
| [[RPL35A]] | -0.73 | -0.67 / -0.72 | both halves | 7e-06 |  |
| [[RPL9]] ⚠ | -0.72 | -0.62 / -0.71 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[TPT1]] | -0.72 | -0.65 / -0.74 | both halves | 7e-06 |  |
| [[RPS13]] ⚠ | -0.72 | -0.63 / -0.70 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL37A]] ⚠ | -0.71 | -0.61 / -0.68 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG6]] | -0.70 | -0.50 / -0.71 | both halves | 1e-05 |  |
| [[RPS27A]] ⚠ | -0.70 | -0.59 / -0.68 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS21]] | -0.69 | -0.67 / -0.70 | both halves | 7e-06 |  |
| [[RPS27]] | -0.69 | -0.60 / -0.70 | both halves | 7e-06 |  |
| [[RPS19]] | -0.69 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[RPL31]] | -0.69 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[COMMD6]] | -0.69 | -0.73 / -0.63 | both halves | 7e-06 |  |
| [[RPLP1]] | -0.69 | -0.61 / -0.72 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PNPO's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ENDOV]] | C | ENDOV's natural level strengthens PNPO's drug response | ENDOV's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.05; direction not clear | 0.047 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.660). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-44.9, -26.0); signed map (-18.0, -40.6). **Vector** length 83.4, 17.4% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +7.9 | +20.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +7.9 | +18.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +7.5 | +16.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.6 | +7.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.9 | +7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +4.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.4 | +2.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.3 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | -2.9 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -3.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.4 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.1 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -0.0 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.7 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | +0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | pyridoxamine 5'-phosphate oxidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:47,941,506-47,949,308 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PDXPO |
| Gene groups (HGNC) | Flavoproteins; Oxidoreductases |
| Reactome | 3 pathways, smallest: Vitamin B6 activation to pyridoxal phosphate; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVS9](https://www.uniprot.org/uniprotkb/Q9NVS9) (Pyridoxine-5'-phosphate oxidase):

> Catalyzes the oxidation of either pyridoxine 5'-phosphate (PNP) or pyridoxamine 5'-phosphate (PMP) into pyridoxal 5'-phosphate (PLP).

**Summary**, from NCBI Gene [55163](https://www.ncbi.nlm.nih.gov/gene/55163):

> The enzyme encoded by this gene catalyzes the terminal, rate-limiting step in the synthesis of pyridoxal 5'-phosphate, also known as vitamin B6. Vitamin B6 is a required co-factor for enzymes involved in both homocysteine metabolism and synthesis of neurotransmitters such as catecholamine. Mutations in this gene result in pyridoxamine 5'-phosphate oxidase (PNPO) deficiency, a form of neonatal epileptic encephalopathy. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:30260](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30260) · Entrez [55163](https://www.ncbi.nlm.nih.gov/gene/55163) · UniProt [Q9NVS9](https://www.uniprot.org/uniprotkb/Q9NVS9) · Ensembl [ENSG00000108439](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108439)

## Data

Gene col 2947: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2947); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2947, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2947]; `tensor/DDL_lfc|DDL_z.npy` [2947]; `embed/gene_vectors.npy` [2947]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2947 or target_col == 2947). Every well: [[PNPO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNPO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
