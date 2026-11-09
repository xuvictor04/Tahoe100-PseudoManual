---
symbol: "LRP8"
type: "gene"
col: 8050
ensembl_id: "ENSG00000157193"
name: "LDL receptor related protein 8"
location: "1p32.3"
module: 5
arm: "+"
pooled_cpm: 37.52
n_lines_expressing: 48
n_dd_up: 21
n_dd_down: 41
n_dd_up_clean: 15
n_dd_down_clean: 39
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# LRP8

*LDL receptor related protein 8* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.72× (z +12.3, q 8e-32, up in 30 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.83× (z +7.7, q 1e-12, up in 32 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.359× (z -18.6, q 0e+00, down in 35 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LETM1]] (+0.68, fdr 7e-06), [[TTL]] (+0.67, fdr 7e-06), [[ACACA]] (+0.66, fdr 7e-06); moves opposite to [[SNX2]] (-0.64, fdr 7e-06), [[CIR1]] (-0.62, fdr 7e-06), [[DNAJC27]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8050.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +12.3 | 8e-32 | 30/34 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.45×** | +11.4 | 7e-28 | 33/42 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.50×** | +10.8 | 5e-25 | 29/38 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.10×** | +9.5 | 3e-19 | 35/45 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.83×** | +7.7 | 1e-12 | 32/45 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +7.7 | 2e-12 | 27/45 (NCI-H1792, AsPC-1, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.46×** | +6.8 | 7e-10 | 32/46 (HS-578T, HOP62, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.70×** | +6.7 | 1e-09 | 31/45 (SW480, AsPC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +5.2 | 1e-05 | 26/45 (HEC-1-A, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Berbamine (drug)]] 5 µM |  | **1.32×** | +5.0 | 3e-05 | 23/47 (HS-578T, A549, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.40×** | +4.2 | 0.001 | 21/44 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.40×** | +4.1 | 0.002 | 18/44 (NCI-H1792, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +4.1 | 0.002 | 18/44 (LoVo, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.81×** | +4.0 | 0.003 | 16/39 (SW480, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.004 | 17/46 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.75×** | +3.7 | 0.007 | 14/43 (NCI-H1792, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.71×** | +3.6 | 0.012 | 17/43 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.70×** | +3.5 | 0.013 | 13/45 (NCI-H1792, A498, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.68×** | +3.5 | 0.016 | 11/43 (NCI-H1792, A498, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.072 | 10/46 (SNU-423, HS-578T, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +2.9 | 0.099 | 12/45 (SW48, HOP62, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 2 with an alert ⚠; shown: the 15 strongest. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8050.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.359×** | -18.6 | 0e+00 | 35/45 (SW48, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.326×** | -13.8 | 6e-41 | 39/46 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.485×** | -13.1 | 5e-37 | 41/46 (A498, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.534×** | -8.0 | 1e-13 | 29/45 (SW48, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.555×** | -7.5 | 5e-12 | 30/46 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.593×** | -6.9 | 6e-10 | 30/46 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.586×** | -6.9 | 6e-10 | 28/46 (SW48, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.391×** | -6.3 | 2e-08 | 28/46 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **0.719×** | -6.0 | 1e-07 | 30/46 (HT-29, A-427, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[NG25 (drug)]] 5 µM |  | **0.415×** | -5.9 | 2e-07 | 30/44 (LoVo, SNU-1, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.689×** | -5.7 | 7e-07 | 24/46 (SW480, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.705×** | -5.3 | 5e-06 | 19/46 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.663×** | -5.3 | 6e-06 | 23/46 (SW48, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.668×** | -5.0 | 2e-05 | 21/44 (SW480, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.730×** | -4.4 | 3e-04 | 24/46 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8050. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 63.2 | 0 | 22 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0977× (z -19.7) |
| [[LoVo (line)]] | wt | 62.6 | 0 | 19 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0651× (z -19.1) |
| [[SW480 (line)]] | alt | 56.5 | 1 | 18 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.70× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -15.9) |
| [[SW48 (line)]] | wt | 368 | 0 | 18 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0587× (z -31.9) |
| [[BT-474 (line)]] | alt | 44.4 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -17.6) |
| [[A-172 (line)]] | wt | 43.4 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -16.0) |
| [[MIA PaCa-2 (line)]] | alt | 31.5 | 0 | 7 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.441× (z -17.7) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.254× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 48.5 | 2 (2 ⚠) | 4 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.25× (z +9.2) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -14.9) |
| [[PANC-1 (line)]] | alt | 26.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -24.0) |
| [[RKO (line)]] | wt | 56.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0796× (z -20.8) |
| [[A-427 (line)]] | wt | 29.8 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.0984× (z -16.6) |
| [[A498 (line)]] | wt | 43.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.125× (z -17.1) |
| [[LS 180 (line)]] | wt | 70.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 30.3 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 5.14× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Selinexor (drug)]] 5 µM 0.206× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 14.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.6× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SNU-1 (line)]] | wt | 62.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0867× (z -17.4) |
| [[AsPC-1 (line)]] | alt | 28.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0755× (z -21.8) |
| [[HOP62 (line)]] | alt | 17.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.35× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A549 (line)]] | wt | 14.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.80× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 20.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.4) |
| [[HT-29 (line)]] | alt | 90.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -14.4) |
| [[J82 (line)]] | alt | 49.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -13.0) |
| [[C-33 A (line)]] | alt | 37.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -9.1) |
| [[C32 (line)]] | wt | 14.2 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0861× (z -9.1) |
| [[HCT15 (line)]] | alt | 31.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -11.3) |
| [[HS-578T (line)]] | alt | 33.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 16.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2030 (line)]] | alt | 35.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -13.2) |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0968× (z -19.0) |
| [[SHP-77 (line)]] | alt | 45.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -11.0) |
| [[SK-MEL-2 (line)]] | alt | 30.4 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.339× (z -9.0) |
| [[SW 900 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -9.6) |
| [[SW1417 (line)]] | alt | 36.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -13.1) |
| [[AN3 CA (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.81 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.09 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8050), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LETM1]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[TTL]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[ACACA]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 | pathway: Metabolism of vitamins and cofactors |
| [[MACROH2A1]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[TXN]] | +0.64 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[HNRNPAB]] | +0.64 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[EIPR1]] | +0.63 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[GATAD2A]] | +0.63 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[FAM20B]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[TMTC4]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[SLFNL1-AS1]] | +0.61 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[CTPS1]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX2]] | -0.64 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[CIR1]] | -0.62 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[DNAJC27]] | -0.62 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[SECISBP2L]] | -0.62 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.62 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[EXOC1]] | -0.61 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[SAP18]] | -0.61 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[THAP1]] | -0.61 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[PPIL4]] | -0.61 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[ZNF44]] | -0.60 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[ASB8]] | -0.59 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[ANKRA2]] | -0.59 | -0.67 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises LRP8's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BICDL1]] | B | BICDL1 activity weakens LRP8's drug response | lines that do not express BICDL1 (11) vs lines expressing it (35) | the lines without BICDL1 respond 0.97× as strongly (z diff +0.00); strongest at Dinaciclib 0.05 µM: 4.36x vs 1.81x (z diff -3.5) | 0.057 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.556). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-4.7, -35.4); signed map (-19.1, -48.7). **Vector** length 147, 49.4% of its response variance represented; |z| ≥ 3 in 1,573 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.6 | +9.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.0 | +7.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.6 | +5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +10.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.5 | +6.7 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +4.8 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +7.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.1 | +3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.6 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.6 | -13.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.2 | -13.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.3 | -5.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.7 | -7.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.2 | -6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.8 | -5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.3 | -4.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.0 | -5.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.7 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | LDL receptor related protein 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:53,242,364-53,328,469 (-) |
| Ensembl biotype | protein_coding |
| Also known as | APOER2, MCI1, LRP-8, HSZ75190 |
| Gene groups (HGNC) | Low density lipoprotein receptors |
| Reactome | 8 pathways, smallest: Platelet sensitization by LDL; Retinoid metabolism and transport; Metabolism of fat-soluble vitamins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14114](https://www.uniprot.org/uniprotkb/Q14114) (Low-density lipoprotein receptor-related protein 8):

> Cell surface receptor for Reelin (RELN) and apolipoprotein E (apoE)-containing ligands. LRP8 participates in transmitting the extracellular Reelin signal to intracellular signaling processes, by binding to DAB1 on its cytoplasmic tail (By similarity). Reelin acts via both the VLDL receptor (VLDLR) and LRP8 to regulate DAB1 tyrosine phosphorylation and microtubule function in neurons (By similarity). LRP8 has higher affinity for Reelin than VLDLR (By similarity). LRP8 is thus a key component of …

**Summary**, from NCBI Gene [7804](https://www.ncbi.nlm.nih.gov/gene/7804):

> This gene encodes a member of the low density lipoprotein receptor (LDLR) family. Low density lipoprotein receptors are cell surface proteins that play roles in both signal transduction and receptor-mediated endocytosis of specific ligands for lysosomal degradation. The encoded protein plays a critical role in the migration of neurons during development by mediating Reelin signaling, and also functions as a receptor for the cholesterol transport protein apolipoprotein E. Expression of this gene …

**Accessions** — [HGNC:6700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6700) · Entrez [7804](https://www.ncbi.nlm.nih.gov/gene/7804) · UniProt [Q14114](https://www.uniprot.org/uniprotkb/Q14114) · Ensembl [ENSG00000157193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157193)

## Data

Gene col 8050: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8050); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8050, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8050]; `tensor/DDL_lfc|DDL_z.npy` [8050]; `embed/gene_vectors.npy` [8050]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8050 or target_col == 8050). Every well: [[LRP8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRP8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
