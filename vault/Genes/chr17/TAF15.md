---
symbol: "TAF15"
type: "gene"
col: 15667
ensembl_id: "ENSG00000270647"
name: "TATA-box binding protein associated factor 15"
location: "17q12"
module: 28
arm: "+"
pooled_cpm: 335.84
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# TAF15

*TATA-box binding protein associated factor 15* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.47× (z +12.3, q 6e-32, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.748× (z -6.4, q 7e-08, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INTS8]] (+0.59, fdr 1e-05), [[RAD52]] (+0.57, fdr 1e-05), [[PRPSAP2]] (+0.56, fdr 1e-05); moves opposite to [[FASTKD5]] (-0.58, fdr 1e-05), [[BAIAP2-DT]] (-0.54, fdr 1e-05), [[CAP1]] (-0.48, fdr 4e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15667.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +12.3 | 6e-32 | 33/48 (RKO, COLO 205, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +10.1 | 1e-21 | 43/49 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +5.7 | 3e-06 | 28/45 (NCI-H2347, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +5.3 | 2e-05 | 26/44 (A-427, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.9 | 1e-04 | 25/48 (PANC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.7 | 2e-04 | 25/50 (HT-29, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.23×** | +4.6 | 4e-04 | 26/48 (RKO, AsPC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.20× | +4.1 | 0.003 | 24/48 (RKO, AsPC-1, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.009 | 29/48 (PANC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.018 | 26/48 (SHP-77, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.027 | 27/48 (MIA PaCa-2, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.16× | +3.2 | 0.064 | 16/49 (HepG2/C3A, COLO 205, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.064 | 20/48 (MIA PaCa-2, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.10 | 11/48 (KATO III, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15667.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.748×** | -6.4 | 7e-08 | 30/48 (C-33 A, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.765×** | -5.9 | 8e-07 | 33/48 (PANC-1, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -5.6 | 4e-06 | 0/50 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.641×** | -5.2 | 3e-05 | 34/49 (SHP-77, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.795×** | -5.1 | 4e-05 | 26/48 (SW480, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.801×** | -4.9 | 8e-05 | 29/48 (HCT15, C32, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | **0.826×** | -4.2 | 0.002 | 25/48 (C-33 A, HCT15, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.736×** | -3.6 | 0.026 | 25/48 (SK-MEL-2, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -3.4 | 0.042 | 20/48 (HCT15, NCI-H2030, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.860× | -3.3 | 0.048 | 20/48 (C-33 A, HCT15, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.899× | -3.3 | 0.048 | 12/48 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.866× | -3.2 | 0.070 | 17/48 (A-172, KATO III, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15667. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 157 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +20.7) | — |
| [[SW480 (line)]] | alt | 391 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +14.1) | [[Digitoxin (drug)]] 0.5 µM 0.530× (z -12.3) |
| [[C-33 A (line)]] | alt | 470 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.501× (z -10.8) |
| [[HT-29 (line)]] | alt | 479 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +14.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 413 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 414 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +14.9) | — |
| [[NCI-H2347 (line)]] | alt | 286 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 438 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.71× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +9.9) | — |
| [[RKO (line)]] | wt | 320 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +28.0) | — |
| [[LoVo (line)]] | wt | 318 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +12.9) | — |
| [[LOX-IMVI (line)]] | wt | 352 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 344 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +14.0) | — |
| [[SHP-77 (line)]] | alt | 257 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.550× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 440 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.663× (z -10.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.381× (z -8.8) |
| [[A-427 (line)]] | wt | 406 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.83× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 312 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.66× (z +8.8) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 306 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +19.4) | — |
| [[CFPAC-1 (line)]] | alt | 168 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +14.2) | — |
| [[CHP-212 (line)]] | wt | 330 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -9.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[COLO 205 (line)]] | alt | 271 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +21.8) | — |
| [[H4 (line)]] | wt | 265 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 477 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.512× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 539 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.74× (z +10.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 187 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.0) | — |
| [[KATO III (line)]] | alt | 520 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.58× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 403 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.652× (z -9.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1573 (line)]] | alt | 186 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +12.3) | — |
| [[NCI-H23 (line)]] | alt | 327 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 285 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +14.0) | — |
| [[SW 900 (line)]] | alt | 216 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +8.7) | — |
| [[A-172 (line)]] | wt | 294 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 356 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 383 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 317 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 183 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 315 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 228 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 248 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 280 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 286 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 381 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 329 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 304 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 272 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 359 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 302 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 424 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15667), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS8]] | +0.59 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[RAD52]] | +0.57 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[PRPSAP2]] | +0.56 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[CCAR1]] | +0.56 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[RPAP2]] | +0.55 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[ZC3H6]] | +0.55 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[GIGYF2]] | +0.54 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[LSM14A]] | +0.54 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[UPF3B]] | +0.54 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[EXOSC8]] | +0.53 | +0.52 / +0.48 | both halves | 2e-05 | pathway: Affinity selection of immunoglobulins |
| [[ZC3H7A]] | +0.53 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[GOLGA1]] | +0.53 | +0.58 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FASTKD5]] | -0.58 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[BAIAP2-DT]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[CAP1]] | -0.48 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[TPRG1L]] | -0.48 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[SLC35C1]] | -0.48 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[PRDX1]] | -0.48 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[PHF13]] | -0.47 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[PI4K2A]] | -0.47 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[BAK1]] | -0.47 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[GALNT4]] | -0.45 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[MTPN]] | -0.45 | -0.55 / -0.37 | both halves | 7e-05 |  |
| [[HTRA2]] | -0.44 | -0.39 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TAF15's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.495). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.0, 17.6); signed map (7.4, -15.9). **Vector** length 149, 49.6% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +12.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +4.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +4.8 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +4.8 | +4.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.7 | +3.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.8 | +3.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.8 | +3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.5 | +1.8 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -9.8 | -5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.8 | -6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -6.1 | -1.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -6.1 | -3.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -3.1 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:35,809,482-35,864,615 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hTAFII68, RBP56, Npl3; previously TAF2N |
| Gene groups (HGNC) | Zinc fingers RANBP2-type; RNA binding motif containing; FET protein family |
| Reactome | 19 pathways, smallest: HIV Transcription Initiation; RNA Polymerase II HIV Promoter Escape; RNA Polymerase II Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92804](https://www.uniprot.org/uniprotkb/Q92804) (TATA-binding protein-associated factor 2N):

> RNA and ssDNA-binding protein that may play specific roles during transcription initiation at distinct promoters. Binds to ssRNA containing the consensus sequence 5'-AGGUAA-3'. Can enter the pre-initiation complex together with the RNA polymerase II (Pol II).

**Summary**, from NCBI Gene [8148](https://www.ncbi.nlm.nih.gov/gene/8148):

> This gene encodes a member of the TET family of RNA-binding proteins. The encoded protein plays a role in RNA polymerase II gene transcription as a component of a distinct subset of multi-subunit transcription initiation factor TFIID complexes. Translocations involving this gene play a role in acute leukemia and extraskeletal myxoid chondrosarcoma, and mutations in this gene may play a role in amyotrophic lateral sclerosis. Alternatively spliced transcript variants encoding multiple isoforms …

**Accessions** — [HGNC:11547](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11547) · Entrez [8148](https://www.ncbi.nlm.nih.gov/gene/8148) · UniProt [Q92804](https://www.uniprot.org/uniprotkb/Q92804) · Ensembl [ENSG00000270647](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000270647)

## Data

Gene col 15667: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15667); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15667, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15667]; `tensor/DDL_lfc|DDL_z.npy` [15667]; `embed/gene_vectors.npy` [15667]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15667 or target_col == 15667). Every well: [[TAF15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
