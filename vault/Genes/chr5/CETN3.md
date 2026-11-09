---
symbol: "CETN3"
type: "gene"
col: 7694
ensembl_id: "ENSG00000153140"
name: "centrin 3"
location: "5q14.3"
module: 28
arm: "+"
pooled_cpm: 24.24
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# CETN3

*centrin 3* — 5q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.14× (z +11.1, q 5e-26, up in 31 of 34 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (SW480 3.72×, NCI-H2347 3.44×, NCI-H460 4.01×, PANC-1 3.00×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (MIA PaCa-2 5.57×, SW480 3.50×, PANC-1 3.01×, KATO III 4.25×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.310× (z -11.8, q 3e-29, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUPT20H]] (+0.67, fdr 7e-06), [[CEP63]] (+0.65, fdr 1e-05), [[EBAG9]] (+0.64, fdr 7e-06); moves opposite to [[VAC14]] (-0.53, fdr 2e-05), [[MROH1]] (-0.52, fdr 2e-05), [[NUTM2A-AS1]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7694.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (SW480 3.72×, NCI-H2347 3.44×, NCI-H460 4.01×, PANC-1 3.00×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (MIA PaCa-2 5.57×, SW480 3.50×, PANC-1 3.01×, KATO III 4.25×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.14×** | +11.1 | 5e-26 | 31/34 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.00×** | +11.1 | 5e-26 | 42/44 (SW480, NCI-H2347, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.63×** | +4.6 | 1e-03 | 25/40 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.49×** | +4.0 | 0.008 | 27/46 (HOP62, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7694.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.310×** | -11.8 | 3e-29 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.336×** | -11.0 | 1e-25 | 45/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.406×** | -9.1 | 2e-17 | 39/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.423×** | -8.7 | 7e-16 | 42/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.475×** | -7.5 | 8e-12 | 40/48 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.512×** | -6.4 | 2e-08 | 36/48 (SW 1088, HCT15, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.590×** | -5.3 | 9e-06 | 30/48 (PANC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.617×** | -4.9 | 8e-05 | 27/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.405×** | -4.8 | 1e-04 | 34/47 (A-427, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.462×** | -4.1 | 0.003 | 32/46 (C-33 A, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.682×** | -3.9 | 0.006 | 22/47 (SNU-1, HepG2/C3A, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.484×** | -3.8 | 0.006 | 23/48 (A-427, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.781×** | -3.4 | 0.027 | 24/47 (hTERT-HPNE, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.711×** | -3.3 | 0.039 | 20/45 (A549, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.732×** | -3.1 | 0.065 | 19/47 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7694. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 34.8 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Digitoxin (drug)]] 0.5 µM 0.152× (z -15.6) |
| [[SW480 (line)]] | alt | 26.5 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Digitoxin (drug)]] 0.5 µM 0.172× (z -13.7) |
| [[A-427 (line)]] | wt | 53.1 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -12.6) |
| [[HOP62 (line)]] | alt | 31.4 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Digitoxin (drug)]] 5 µM 0.149× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.235× (z -9.8) |
| [[LS 180 (line)]] | wt | 17.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.76× (z +8.7) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.157× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 32.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.57× (z +10.3) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.245× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 21.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.167× (z -12.0) |
| [[A498 (line)]] | wt | 29.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HepG2_C3A (line)]] | wt | 16.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Roxadustat (drug)]] 0.05 µM 0.106× (z -9.1) |
| [[KATO III (line)]] | alt | 18.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.25× (z +8.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.0770× (z -16.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 29.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -11.6) |
| [[SNU-1 (line)]] | wt | 25.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -9.7) |
| [[SW 900 (line)]] | alt | 26.1 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -9.0) |
| [[A-172 (line)]] | wt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A549 (line)]] | wt | 17.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[CFPAC-1 (line)]] | alt | 21.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 13.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.80× (z +8.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 27.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.219× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -9.4) |
| [[LoVo (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -11.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 25.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2347 (line)]] | alt | 39.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[RKO (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 17.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0974× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.161× (z -9.6) |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -9.0) |
| [[AN3 CA (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7694), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUPT20H]] | +0.67 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[CEP63]] | +0.65 | +0.75 / +0.55 | both halves | 1e-05 | same gene group; STRING 624 |
| [[EBAG9]] | +0.64 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[NSMCE1]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[NUDCD2]] | +0.62 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[TPR]] | +0.62 | +0.56 / +0.69 | both halves | 1e-05 | STRING 945 |
| [[HIRIP3]] | +0.61 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[KIAA0586]] | +0.60 | +0.64 / +0.57 | both halves | 1e-05 | STRING 448 |
| [[SPDL1]] | +0.60 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[AGGF1]] | +0.60 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[NDUFA5]] | +0.60 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[IFT74]] | +0.59 | +0.66 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAC14]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[MROH1]] | -0.52 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[NUTM2A-AS1]] | -0.52 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[C1orf216]] | -0.51 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[GALNS]] | -0.49 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[RPUSD4]] | -0.48 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[CORO7]] | -0.47 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[TMEM11-DT]] | -0.47 | -0.43 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-29.6, 2.9); signed map (6.2, -24.8). **Vector** length 68.1, 15.3% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.9 | -2.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.6 | -3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | -4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +0.3 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | +1.0 | -0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.6 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.3 | -7.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.0 | -6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +2.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.4 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -4.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | centrin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.3 — chr5:90,392,257-90,409,766 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CEN3 |
| Gene groups (HGNC) | EF-hand domain containing; Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O15182](https://www.uniprot.org/uniprotkb/O15182) (Centrin-3):

> Plays a fundamental role in microtubule-organizing center structure and function.; As a component of the TREX-2 complex, involved in the export of mRNAs to the cytoplasm through the nuclear pores.

**Summary**, from NCBI Gene [1070](https://www.ncbi.nlm.nih.gov/gene/1070):

> The protein encoded by this gene contains four EF-hand calcium binding domains, and is a member of the centrin protein family. Centrins are evolutionarily conserved proteins similar to the CDC31 protein of S. cerevisiae. Yeast CDC31 is located at the centrosome of interphase and mitotic cells, where it plays a fundamental role in centrosome duplication and separation. Multiple forms of the proteins similar to the yeast centrin have been identified in human and other mammalian cells, some of …

**Accessions** — [HGNC:1868](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1868) · Entrez [1070](https://www.ncbi.nlm.nih.gov/gene/1070) · UniProt [O15182](https://www.uniprot.org/uniprotkb/O15182) · Ensembl [ENSG00000153140](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153140)

## Data

Gene col 7694: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7694); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7694, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7694]; `tensor/DDL_lfc|DDL_z.npy` [7694]; `embed/gene_vectors.npy` [7694]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7694 or target_col == 7694). Every well: [[CETN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CETN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
