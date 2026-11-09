---
symbol: "FBH1"
type: "gene"
col: 5562
ensembl_id: "ENSG00000134452"
name: "F-box DNA helicase 1"
location: "10p15.1"
module: 52
arm: "+"
pooled_cpm: 55.0
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# FBH1

*F-box DNA helicase 1* — 10p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.33× (z +16.2, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.556× (z -11.2, q 2e-26, down in 37 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.760× (z -5.2, q 1e-05, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 0.289×, H4 0.122×, hTERT-HPNE 0.214×, SHP-77 0.233×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (RKO 0.133×, SW48 0.0844×, LoVo 0.372×, HT-29 0.328×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (hTERT-HPNE 0.138×, LOX-IMVI 0.300×, J82 0.328×; ⚠ toxic; transcription drop); [[Pralsetinib (drug)]] 5 µM in 1 line (Hs 766T 0.0479×); [[venetoclax (drug)]] 5 µM in 1 line (COLO 205 0.0663×); [[Auranofin (drug)]] 5 µM in 1 line (A-172 0.443×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFYVE21]] (+0.70, fdr 7e-06), [[SENP5]] (+0.66, fdr 1e-05), [[PDCD6]] (+0.66, fdr 9e-06); moves opposite to [[CHIC1]] (-0.64, fdr 1e-05), [[ZNF711]] (-0.63, fdr 1e-05), [[RPS6KA6]] (-0.63, fdr 2e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5562.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.33×** | +16.2 | 0e+00 | 46/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.27×** | +15.6 | 0e+00 | 45/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +12.6 | 2e-34 | 39/48 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.94×** | +12.6 | 2e-34 | 46/48 (SW480, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +6.2 | 6e-08 | 35/48 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.0 | 2e-07 | 28/49 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.1 | 0.14 | 14/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | 1.36× | +3.1 | 0.14 | 12/49 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5562.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 0.289×, H4 0.122×, hTERT-HPNE 0.214×, SHP-77 0.233×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (RKO 0.133×, SW48 0.0844×, LoVo 0.372×, HT-29 0.328×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (hTERT-HPNE 0.138×, LOX-IMVI 0.300×, J82 0.328×; ⚠ toxic; transcription drop); [[Pralsetinib (drug)]] 5 µM in 1 line (Hs 766T 0.0479×); [[venetoclax (drug)]] 5 µM in 1 line (COLO 205 0.0663×); [[Auranofin (drug)]] 5 µM in 1 line (A-172 0.443×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.556×** | -11.2 | 2e-26 | 37/48 (RKO, SW48, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.567×** | -9.8 | 3e-20 | 31/45 (hTERT-HPNE, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.613×** | -8.9 | 8e-17 | 30/43 (SW480, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.732×** | -6.0 | 3e-07 | 27/48 (hTERT-HPNE, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.746×** | -5.4 | 9e-06 | 25/48 (AN3 CA, A-427, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.760×** | -5.2 | 1e-05 | 29/48 (A-172, NCI-H23, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.775×** | -4.9 | 8e-05 | 25/48 (A-172, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.818×** | -3.8 | 0.008 | 20/48 (LoVo, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Bendamustine (drug)]] 5 µM |  | 0.837× | -3.2 | 0.073 | 17/47 (HepG2/C3A, CHP-212, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~72% of this change | 0.852× | -3.1 | 0.12 | 17/47 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5562. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 75.9 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.25× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.443× (z -9.0) |
| [[A549 (line)]] | wt | 57.6 | 4 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.380× (z -9.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 53.1 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.04× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -15.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 67.9 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.59× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 55.3 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.26× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 41.7 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +14.5) | — |
| [[RKO (line)]] | wt | 87.2 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.36× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -21.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 46.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.24× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 82.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.95× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.398× (z -8.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 57.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +11.0) | — |
| [[COLO 205 (line)]] | alt | 44.3 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 3.60× (z +9.7) | [[venetoclax (drug)]] 5 µM 0.0663× (z -10.8) |
| [[Hs 766T (line)]] | wt | 36.3 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +10.0) | [[Pralsetinib (drug)]] 5 µM 0.0479× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 65.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -14.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 60.7 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -11.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 56.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 54.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.08× (z +12.0) | — |
| [[SHP-77 (line)]] | alt | 39.5 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.04× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.233× (z -11.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 59.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.39× (z +9.5) | — |
| [[AsPC-1 (line)]] | alt | 62.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.353× (z -8.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 50.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.56× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 54.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 49.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.86× (z +10.2) | — |
| [[A-427 (line)]] | wt | 51.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 50.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.138× (z -9.4) ⚠ cell-cycle shift, explains ~49% of this change |
| [[BT-474 (line)]] | alt | 51.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -9.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 25.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +9.2) | — |
| [[CHP-212 (line)]] | wt | 59.6 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.177× (z -8.9) |
| [[H4 (line)]] | wt | 40.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -13.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 69.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 56.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -8.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 63.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -10.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 64.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 42.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -9.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 42.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.42× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 97.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -11.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 52.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 52.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -10.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 44.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0844× (z -15.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5562), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE21]] | +0.70 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[SENP5]] | +0.66 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[PDCD6]] | +0.66 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[ZMYND19]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[PITPNA]] | +0.63 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[USP20]] | +0.62 | +0.38 / +0.66 | both halves | 6e-05 |  |
| [[TUSC2]] | +0.62 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[SOCS7]] | +0.62 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[SHPK]] | +0.61 | +0.35 / +0.69 | both halves | 1e-04 |  |
| [[CCM2]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ADCK5]] | +0.61 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[SETD3]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHIC1]] | -0.64 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[ZNF711]] | -0.63 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[RPS6KA6]] | -0.63 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[SYNE1]] | -0.62 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[LINC02428]] | -0.62 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[ATF7IP]] | -0.62 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[ZFHX2]] | -0.62 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[CC2D2A]] | -0.62 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[CYP2U1]] | -0.61 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[BTN2A2]] | -0.60 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[ZNF260]] | -0.59 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[ZNF155]] | -0.59 | -0.57 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FBH1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PPP1R3B-DT]] | B | PPP1R3B-DT activity lowers FBH1's level | lines that do not express PPP1R3B-DT (5) vs lines expressing it (45) | 1.25× higher at baseline in the lines without PPP1R3B-DT | 0.060 | ⚠ within organs, on part of the lines; also absent: KNDC1; maybe low, not absent; its own permutation p |
| [[CLIC2]] | B | CLIC2 activity lowers FBH1's level | lines that do not express CLIC2 (14) vs lines expressing it (36) | 1.14× higher at baseline in the lines without CLIC2 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers FBH1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.602). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-14.5, 0.3); signed map (-45.9, -0.1). **Vector** length 83.1, 18.8% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +6.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +16.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +15.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +6.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.1 | +12.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.4 | +2.7 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -7.0 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.4 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.7 | -9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.5 | +0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -5.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.1 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -0.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | F-box DNA helicase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.1 — chr10:5,890,203-5,937,594 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14590, Fbx18; previously FBXO18 |
| Gene groups (HGNC) | F-boxes other; Helicases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFZ0](https://www.uniprot.org/uniprotkb/Q8NFZ0) (F-box DNA helicase 1):

> 3'-5' DNA helicase and substrate-recognition component of the SCF(FBH1) E3 ubiquitin ligase complex that plays a key role in response to stalled/damaged replication forks. Involved in genome maintenance by acting as an anti-recombinogenic helicase and preventing extensive strand exchange during homologous recombination: promotes RAD51 filament dissolution from stalled forks, thereby inhibiting homologous recombination and preventing excessive recombination. Also promotes cell death and DNA …

**Summary**, from NCBI Gene [84893](https://www.ncbi.nlm.nih.gov/gene/84893):

> This gene encodes a member of the F-box protein family, members of which are characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into three classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein …

**Accessions** — [HGNC:13620](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13620) · Entrez [84893](https://www.ncbi.nlm.nih.gov/gene/84893) · UniProt [Q8NFZ0](https://www.uniprot.org/uniprotkb/Q8NFZ0) · Ensembl [ENSG00000134452](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134452)

## Data

Gene col 5562: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5562); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5562, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5562]; `tensor/DDL_lfc|DDL_z.npy` [5562]; `embed/gene_vectors.npy` [5562]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5562 or target_col == 5562). Every well: [[FBH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
