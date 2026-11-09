---
symbol: "HAUS3"
type: "gene"
col: 13198
ensembl_id: "ENSG00000214367"
name: "HAUS augmin like complex subunit 3"
location: "4p16.3"
module: 3
arm: "+"
pooled_cpm: 15.92
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# HAUS3

*HAUS augmin like complex subunit 3* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.94× (z +25.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.649× (z -8.0, q 4e-13, down in 23 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pentagastrin (drug)]] 5 µM: 0.872× (z -3.6, q 0.028, down in 7 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (LOX-IMVI 0.126×, HEC-1-A 0.170×, A-172 0.189×, KATO III 0.211×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (J82 0.154×, A-172 0.149×, A549 0.182×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (J82 0.312×, LS 180 0.229×; ⚠ toxic; transcription drop); [[Pemetrexed (drug)]] 0.05 µM in 1 line (SW48 0.0651×); [[Harringtonine (drug)]] 0.05 µM in 1 line (Hs 766T 0.164×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (SNU-1 0.0957×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC127]] (+0.64, fdr 1e-05), [[WIPF2]] (+0.61, fdr 3e-05), [[GPATCH11]] (+0.61, fdr 3e-04); moves opposite to [[ADCK1]] (-0.59, fdr 8e-05), [[EPM2A]] (-0.56, fdr 7e-05), [[LYRM1]] (-0.54, fdr 3e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC16A2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13198.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.94×** | +25.5 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.20×** | +21.6 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.85×** | +19.4 | 0e+00 | 46/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +9.3 | 2e-18 | 25/47 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +9.1 | 1e-17 | 32/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +9.0 | 3e-17 | 34/42 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +7.4 | 8e-12 | 23/47 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +6.4 | 1e-08 | 23/48 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +6.1 | 5e-08 | 21/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +5.8 | 3e-07 | 19/48 (NCI-H2347, HOP62, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +5.8 | 4e-07 | 17/47 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +5.3 | 4e-06 | 18/46 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +5.2 | 7e-06 | 10/48 (HT-29, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.66×** | +4.9 | 4e-05 | 14/45 (HOP62, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.29×** | +4.7 | 1e-04 | 15/46 (RKO, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.008 | 16/48 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.025 | 7/46 (NCI-H23, LS 180, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13198.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (LOX-IMVI 0.126×, HEC-1-A 0.170×, A-172 0.189×, KATO III 0.211×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (J82 0.154×, A-172 0.149×, A549 0.182×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (J82 0.312×, LS 180 0.229×; ⚠ toxic; transcription drop); [[Pemetrexed (drug)]] 0.05 µM in 1 line (SW48 0.0651×); [[Harringtonine (drug)]] 0.05 µM in 1 line (Hs 766T 0.164×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (SNU-1 0.0957×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.649×** | -8.0 | 4e-13 | 23/39 (J82, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.628×** | -8.0 | 4e-13 | 21/33 (J82, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.660×** | -7.4 | 2e-11 | 20/31 (LOX-IMVI, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.768×** | -4.9 | 1e-04 | 16/47 (AsPC-1, KATO III, …) | inconsistent across doses |  |
| [[Pentagastrin (drug)]] 5 µM |  | 0.872× | -3.6 | 0.028 | 7/48 (A-427, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **0.825×** | -3.6 | 0.028 | 16/45 (A-427, HCT15, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.826×** | -3.6 | 0.028 | 13/47 (NCI-H661, SW 900, …) | inconsistent across doses |  |
| [[Adenine (drug)]] 5 µM |  | 0.890× | -3.1 | 0.14 | 4/48 (HOP62, NCI-H661, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13198. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 20.0 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.68× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -13.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 18.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.63× (z +15.2) | — |
| [[A498 (line)]] | wt | 15.4 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.63× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.316× (z -9.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 15.1 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 5.17× (z +9.8) | [[Harringtonine (drug)]] 0.05 µM 0.164× (z -9.9) |
| [[J82 (line)]] | alt | 25.6 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.47× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -14.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 17.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.35× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -10.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 18.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.41× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.126× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 19.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.32× (z +10.2) | [[Lonafarnib (drug)]] 5 µM 0.0851× (z -10.9) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 10.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.05× (z +12.1) | — |
| [[PANC-1 (line)]] | alt | 14.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.39× (z +10.6) | — |
| [[RKO (line)]] | wt | 16.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +11.0) | — |
| [[A549 (line)]] | wt | 11.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.28× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -9.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 22.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.61× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 15.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.91× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 17.9 | 0 | 2 (1 ⚠) | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.189× (z -8.8) |
| [[SNU-1 (line)]] | wt | 16.1 | 0 | 2 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0957× (z -9.5) |
| [[A-427 (line)]] | wt | 15.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.36× (z +9.5) | — |
| [[AsPC-1 (line)]] | alt | 15.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.76× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 17.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.15× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 28.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.236× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -13.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 8.57 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0919× (z -8.6) |
| [[LS 180 (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -9.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 12.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.76× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 13.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.38× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 13.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.36× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -8.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 15.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.91× (z +8.9) | — |
| [[SW48 (line)]] | wt | 13.6 | 0 | 1 | — | [[Pemetrexed (drug)]] 0.05 µM 0.0651× (z -10.0) |
| [[AN3 CA (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13198), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC127]] | +0.64 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[WIPF2]] | +0.61 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[GPATCH11]] | +0.61 | +0.28 / +0.65 | both halves | 3e-04 |  |
| [[ISCA2]] | +0.59 | +0.23 / +0.54 | both halves | 5e-04 |  |
| [[CDKN2D]] | +0.59 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[MAP1S]] | +0.58 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[FANCE]] | +0.57 | +0.28 / +0.48 | both halves | 3e-04 |  |
| [[SIVA1]] | +0.57 | +0.35 / +0.45 | both halves | 1e-04 |  |
| [[DSN1]] | +0.57 | +0.41 / +0.58 | both halves | 4e-05 | pathway: Mitotic Prometaphase |
| [[TRAPPC4]] | +0.56 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[ZYG11B]] | +0.56 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[SNAP29]] | +0.56 | +0.40 / +0.45 | both halves | 5e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADCK1]] | -0.59 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[EPM2A]] | -0.56 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[LYRM1]] | -0.54 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[GABPB1-AS1]] | -0.54 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[DLGAP1]] | -0.54 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[GNAL]] | -0.53 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[PITX1-AS1]] | -0.53 | -0.18 / -0.50 | ⚠ one half (not replicated) | 1e-03 |  |
| [[ARRDC3-AS1]] | -0.53 | -0.21 / -0.47 | both halves | 7e-04 |  |
| [[LINC01088]] | -0.52 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[HDDC2]] | -0.52 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[CLDN16]] | -0.52 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[LINC00534]] | -0.51 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[STARD4-AS1]] | -0.51 | -0.31 / -0.39 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A2]] | B | SLC16A2 activity raises HAUS3's level | lines that do not express SLC16A2 (14) vs lines expressing it (36) | 1.14× lower at baseline in the lines without SLC16A2 | 0.099 | ⚠ within organs, on part of the lines; also absent: SLC2A3, LOXL2, ENSG00000234405 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.487). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-49.4, 16.9); signed map (-27.7, 12.5). **Vector** length 74.3, 13.2% of its response variance represented; |z| ≥ 3 in 1,005 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +21.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.4 | +25.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.6 | +19.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +9.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.1 | +5.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.6 | +4.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +5.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.3 | +1.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.3 | -8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.9 | -8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.8 | -7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | +0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | HAUS augmin like complex subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:2,227,464-2,242,133 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4701, IT1, dgt3; previously C4orf15 |
| Gene groups (HGNC) | HAUS augmin like complex |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68CZ6](https://www.uniprot.org/uniprotkb/Q68CZ6) (HAUS augmin-like complex subunit 3):

> Contributes to mitotic spindle assembly, maintenance of centrosome integrity and completion of cytokinesis as part of the HAUS augmin-like complex.

**Summary**, from NCBI Gene [79441](https://www.ncbi.nlm.nih.gov/gene/79441):

> This gene encodes a component of the HAUS augmin-like protein complex, which plays a key role in cytokinesis and mitosis. Disruption of the encoded protein causes mitotic defects resulting from fragmentation of centrosomes and microtubule destabilization. This gene shares its 5' exons with some transcripts from overlapping GeneID: 353497, which encodes a DNA polymerase. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:28719](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28719) · Entrez [79441](https://www.ncbi.nlm.nih.gov/gene/79441) · UniProt [Q68CZ6](https://www.uniprot.org/uniprotkb/Q68CZ6) · Ensembl [ENSG00000214367](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214367)

## Data

Gene col 13198: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13198); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13198, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13198]; `tensor/DDL_lfc|DDL_z.npy` [13198]; `embed/gene_vectors.npy` [13198]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13198 or target_col == 13198). Every well: [[HAUS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAUS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
