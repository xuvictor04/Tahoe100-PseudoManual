---
symbol: "TRIM11"
type: "gene"
col: 7803
ensembl_id: "ENSG00000154370"
name: "tripartite motif containing 11"
location: "1q42.13"
module: 3
arm: "+"
pooled_cpm: 21.66
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# TRIM11

*tripartite motif containing 11* — 1q42.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 1.75× (z +9.9, q 2e-20, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.485× (z -12.8, q 1e-34, down in 37 of 42 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (LOX-IMVI 0.101×, LoVo 0.162×, LS 180 0.141×, HS-578T 0.0845×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A498 0.253×, NCI-H1573 0.222×, HEC-1-A 0.263×, AsPC-1 0.279×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 0.393×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXL18]] (+0.67, fdr 1e-05), [[ATG101]] (+0.66, fdr 2e-05), [[TECPR1]] (+0.65, fdr 1e-05); moves opposite to [[CYB5D2]] (-0.65, fdr 3e-05), [[TAF9B]] (-0.64, fdr 3e-05), [[LEPROT]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SUCLG2-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7803.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **1.75×** | +9.9 | 2e-20 | 38/46 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +9.6 | 3e-19 | 39/47 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +8.4 | 8e-15 | 37/48 (HOP62, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +7.8 | 1e-12 | 36/47 (SW480, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +6.6 | 4e-09 | 27/48 (LOX-IMVI, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +6.2 | 5e-08 | 25/48 (HOP62, LoVo, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.73×** | +5.1 | 3e-05 | 22/45 (SW480, MIA PaCa-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +5.0 | 4e-05 | 20/47 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +4.8 | 1e-04 | 20/40 (SW 900, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~17% of this change | **1.27×** | +4.3 | 0.001 | 16/44 (SW1417, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.18× | +4.0 | 0.003 | 19/48 (C-33 A, NCI-H23, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.42×** | +3.9 | 0.004 | 14/46 (hTERT-HPNE, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.014 | 15/47 (NCI-H460, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.4 | 0.026 | 11/34 (NCI-H1792, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.041 | 10/46 (LoVo, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.041 | 8/47 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.041 | 13/48 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.094 | 11/45 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7803.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (LOX-IMVI 0.101×, LoVo 0.162×, LS 180 0.141×, HS-578T 0.0845×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A498 0.253×, NCI-H1573 0.222×, HEC-1-A 0.263×, AsPC-1 0.279×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 0.393×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.485×** | -12.8 | 1e-34 | 37/42 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.483×** | -12.4 | 1e-32 | 25/33 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.550×** | -9.8 | 3e-20 | 32/38 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.799×** | -5.6 | 3e-06 | 23/48 (Hs 766T, CHP-212, …) | rises with dose | low cells (technical?) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.864× | -3.6 | 0.033 | 10/48 (RKO, SHP-77, …) | all doses, flat |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.823×** | -3.4 | 0.055 | 10/47 (NCI-H2030, Panc 03.27, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.839× | -3.1 | 0.16 | 15/48 (HT-29, SW 1271, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.954× | -3.1 | 0.16 | 3/48 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.843× | -3.0 | 0.16 | 8/48 (Hs 766T, A498, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7803. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 26.5 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 13.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +11.7) ⚠ cell-cycle shift, explains ~98% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -10.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 25.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 25.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -10.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 26.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -13.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 18.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.61× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -10.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -9.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 29.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -13.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -9.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0845× (z -14.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -10.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 24.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -15.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 20.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -16.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 27.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 13.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +11.5) ⚠ cell-cycle shift, explains ~98% of this change | — |
| [[NCI-H2030 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -8.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -9.4) ⚠ cell-cycle shift, explains ~98% of this change |
| [[RPMI-7951 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -8.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7803), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXL18]] | +0.67 | +0.51 / +0.69 | both halves | 1e-05 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[ATG101]] | +0.66 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[TECPR1]] | +0.65 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[NR2F6]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[RBAK-RBAKDN]] | +0.64 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[ATG4B]] | +0.64 | +0.25 / +0.67 | both halves | 4e-04 |  |
| [[BRPF1]] | +0.64 | +0.42 / +0.71 | both halves | 4e-05 |  |
| [[NUDT22]] | +0.64 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[BAHD1]] | +0.64 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[RASSF7]] | +0.63 | +0.36 / +0.60 | both halves | 1e-04 |  |
| [[MRPL55]] | +0.62 | +0.34 / +0.64 | both halves | 1e-04 | STRING 485 |
| [[CCNQ]] | +0.62 | +0.32 / +0.63 | both halves | 2e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5D2]] | -0.65 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[TAF9B]] | -0.64 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[LEPROT]] | -0.62 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[PRKAR1A]] | -0.60 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[GALC]] | -0.60 | -0.37 / -0.56 | both halves | 9e-05 |  |
| [[ERLIN2]] | -0.59 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[TAF9]] | -0.59 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[DECR1]] | -0.59 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[ACADM]] | -0.58 | -0.25 / -0.60 | both halves | 4e-04 |  |
| [[ENOSF1]] | -0.57 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[TMX4]] | -0.57 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[CHRAC1]] | -0.56 | -0.31 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SUCLG2-DT]] | B | SUCLG2-DT activity strengthens TRIM11's drug response | lines that do not express SUCLG2-DT (7) vs lines expressing it (41) | the lines without SUCLG2-DT respond 0.79× as strongly (z diff +0.57); strongest at Panobinostat 5 µM: 0.90x vs 1.51x (z diff +3.4) | 0.080 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ANTXR1]] | B | ANTXR1 activity lowers TRIM11's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 1.21× higher at baseline in the lines without ANTXR1 | 0.084 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.654). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-3.8, 0.6); signed map (-34.5, 2.7). **Vector** length 97.1, 20.8% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.2 | +7.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.8 | +9.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.4 | +9.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +8.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.5 | +6.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.1 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +2.2 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.5 | -12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.4 | -9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | -12.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.1 | -2.3 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -2.1 | -2.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.13 — chr1:228,393,673-228,406,835 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNF92, BIA1 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; MicroRNA protein coding host genes; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96F44](https://www.uniprot.org/uniprotkb/Q96F44) (E3 ubiquitin-protein ligase TRIM11):

> E3 ubiquitin-protein ligase that promotes the degradation of insoluble ubiquitinated proteins, including insoluble PAX6, poly-Gln repeat expanded HTT and poly-Ala repeat expanded ARX (By similarity). Mediates PAX6 ubiquitination leading to proteasomal degradation, thereby modulating cortical neurogenesis (By similarity). May also inhibit PAX6 transcriptional activity, possibly in part by preventing the binding of PAX6 to its consensus sequences (By similarity). May contribute to the regulation …

**Summary**, from NCBI Gene [81559](https://www.ncbi.nlm.nih.gov/gene/81559):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. This protein localizes to the nucleus and the cytoplasm. Its function has not been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16281](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16281) · Entrez [81559](https://www.ncbi.nlm.nih.gov/gene/81559) · UniProt [Q96F44](https://www.uniprot.org/uniprotkb/Q96F44) · Ensembl [ENSG00000154370](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154370)

## Data

Gene col 7803: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7803); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7803, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7803]; `tensor/DDL_lfc|DDL_z.npy` [7803]; `embed/gene_vectors.npy` [7803]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7803 or target_col == 7803). Every well: [[TRIM11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
