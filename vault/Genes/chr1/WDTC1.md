---
symbol: "WDTC1"
type: "gene"
col: 6655
ensembl_id: "ENSG00000142784"
name: "WD and tetratricopeptide repeats 1"
location: "1p36.11"
module: 145
arm: "+"
pooled_cpm: 31.0
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 24
n_dd_up_clean: 5
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# WDTC1

*WD and tetratricopeptide repeats 1* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.26× (z +7.9, q 1e-12, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.393× (z -22.5, q 0e+00, down in 44 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.373× (z -12.5, q 4e-33, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCP11L2]] (+0.64, fdr 1e-05), [[HDAC5]] (+0.64, fdr 9e-06), [[MTURN]] (+0.62, fdr 1e-05); moves opposite to [[COX10]] (-0.64, fdr 1e-05), [[PHF14]] (-0.59, fdr 1e-05), [[NOP16]] (-0.57, fdr 2e-05).
> It is in [[Module 145]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MRTO4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6655.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +7.9 | 1e-12 | 22/47 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +7.8 | 1e-12 | 28/47 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +6.8 | 2e-09 | 21/36 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.28×** | +5.9 | 6e-07 | 23/45 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +5.6 | 2e-06 | 20/48 (HOP62, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +4.7 | 2e-04 | 9/48 (HEC-1-A, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.6 | 0.026 | 14/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.16× | +3.4 | 0.040 | 8/47 (SW480, SW 900, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.044 | 6/47 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.13 | 7/47 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.09× | +3.0 | 0.14 | 3/48 (PANC-1, Panc 03.27, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6655.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.393×** | -22.5 | 0e+00 | 44/48 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.373×** | -12.5 | 4e-33 | 40/47 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.609×** | -12.0 | 9e-31 | 29/47 (Hs 766T, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.388×** | -11.9 | 9e-31 | 40/48 (SW480, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.388×** | -11.9 | 9e-31 | 38/48 (SW480, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.398×** | -11.6 | 4e-29 | 39/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.459×** | -9.8 | 7e-21 | 34/46 (MIA PaCa-2, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.705×** | -8.4 | 2e-15 | 30/48 (SNU-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.742×** | -7.2 | 3e-11 | 25/48 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.741×** | -6.8 | 5e-10 | 26/48 (SW48, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.755×** | -6.8 | 6e-10 | 27/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.761×** | -6.6 | 2e-09 | 26/47 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.595×** | -6.5 | 3e-09 | 23/45 (A498, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.677×** | -6.0 | 8e-08 | 20/48 (SW1417, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.780×** | -6.0 | 8e-08 | 23/47 (LOX-IMVI, SNU-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.781×** | -5.5 | 1e-06 | 19/47 (A-172, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[EX229 (drug)]] 0.5 µM |  | **0.721×** | -5.0 | 2e-05 | 18/48 (SW480, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6655. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 27.2 | 0 | 5 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.158× (z -14.3) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.0863× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 37.3 | 2 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +17.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.321× (z -12.9) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.195× (z -9.7) |
| [[SNU-1 (line)]] | wt | 42.1 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.204× (z -9.9) |
| [[SW480 (line)]] | alt | 45.5 | 0 | 4 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.328× (z -15.2) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.294× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 18.0 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0977× (z -14.6) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 30.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.301× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 41.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -9.8) |
| [[C32 (line)]] | wt | 35.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.355× (z -8.7) |
| [[LoVo (line)]] | wt | 25.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.398× (z -8.6) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 19.0 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -10.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 34.1 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.292× (z -10.6) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 33.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.349× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~98% of this change |
| [[A549 (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.251× (z -10.2) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 32.7 | 0 | 1 | — | [[Ligustrazine (drug)]] 5 µM 0.0713× (z -10.7) |
| [[HOP62 (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.377× (z -9.3) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 38.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -12.0) |
| [[HS-578T (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.391× (z -9.3) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 41.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.247× (z -12.7) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 34.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.355× (z -9.7) |
| [[KATO III (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.357× (z -9.1) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.279× (z -13.1) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 22.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.239× (z -13.9) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 31.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.336× (z -8.7) |
| [[PANC-1 (line)]] | alt | 31.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.359× (z -12.6) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 41.4 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0911× (z -10.3) ⚠ toxic |
| [[SW1417 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.286× (z -10.1) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 28.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.195× (z -9.1) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6655), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCP11L2]] | +0.64 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[HDAC5]] | +0.64 | +0.57 / +0.70 | both halves | 9e-06 |  |
| [[MTURN]] | +0.62 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[FOXO4]] | +0.62 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[CBX7]] | +0.61 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[CTDSP2]] | +0.60 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[CASTOR2]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[WDR48]] | +0.60 | +0.45 / +0.68 | both halves | 3e-05 | same gene group |
| [[CREBL2]] | +0.59 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[FBXL20]] | +0.59 | +0.45 / +0.68 | both halves | 3e-05 | pathway: Neddylation |
| [[ELF2]] | +0.58 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[UBXN6]] | +0.58 | +0.41 / +0.64 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX10]] | -0.64 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[PHF14]] | -0.59 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[NOP16]] | -0.57 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[UTP20]] | -0.56 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[PUM3]] | -0.55 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[LTV1]] | -0.54 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[NOP56]] | -0.54 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[TSR1]] | -0.54 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[NOC3L]] | -0.54 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[NIP7]] | -0.53 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[THADA]] | -0.53 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[PNO1]] | -0.52 | -0.51 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers WDTC1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MRTO4]] | C | WDTC1's natural level strengthens MRTO4's drug response | WDTC1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.21; direction not clear | 0.064 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.0, -46.3); signed map (-17.2, 9.9). **Vector** length 106, 25.0% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.5 | +7.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +6.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +5.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +4.7 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.0 | +2.4 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | +1.7 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.4 | -22.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.9 | -12.5 |
|  | [[EX229 (drug)]] 5 µM |  | -7.6 | -11.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.5 | -11.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.3 | -11.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.6 | -9.8 |

## What is on record

|  |  |
|---|---|
| Name | WD and tetratricopeptide repeats 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:27,234,632-27,308,636 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1037, ADP, DCAF9 |
| Gene groups (HGNC) | WD repeat domain containing; DDB1 and CUL4 associated factors; Tetratricopeptide repeat domain containing |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5D0](https://www.uniprot.org/uniprotkb/Q8N5D0) (WD and tetratricopeptide repeats protein 1):

> May function as a substrate receptor for CUL4-DDB1 E3 ubiquitin-protein ligase complex.

**Summary**, from NCBI Gene [23038](https://www.ncbi.nlm.nih.gov/gene/23038):

> Predicted to enable enzyme inhibitor activity; histone binding activity; and histone deacetylase binding activity. Predicted to be involved in negative regulation of fatty acid biosynthetic process. Predicted to act upstream of or within several processes, including cellular response to insulin stimulus; glucose metabolic process; and negative regulation of transcription by RNA polymerase II. Predicted to be located in nucleoplasm. Predicted to be part of Cul4-RING E3 ubiquitin ligase complex. …

**Accessions** — [HGNC:29175](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29175) · Entrez [23038](https://www.ncbi.nlm.nih.gov/gene/23038) · UniProt [Q8N5D0](https://www.uniprot.org/uniprotkb/Q8N5D0) · Ensembl [ENSG00000142784](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142784)

## Data

Gene col 6655: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6655); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6655, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6655]; `tensor/DDL_lfc|DDL_z.npy` [6655]; `embed/gene_vectors.npy` [6655]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6655 or target_col == 6655). Every well: [[WDTC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDTC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
