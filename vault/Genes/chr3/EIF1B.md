---
symbol: "EIF1B"
type: "gene"
col: 3588
ensembl_id: "ENSG00000114784"
name: "eukaryotic translation initiation factor 1B"
location: "3p22.1"
module: 20
arm: "-"
pooled_cpm: 28.8
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# EIF1B

*eukaryotic translation initiation factor 1B* — 3p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 3.21× (z +9.0, q 2e-16, up in 47 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.51× (z +4.5, q 5e-04, up in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 5 lines (SW480 4.37×, HEC-1-A 4.22×, BT-474 7.79×, PANC-1 3.43×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Homoharringtonine (drug)]] 5 µM in 4 lines (hTERT-HPNE 5.74×, AsPC-1 3.42×, PANC-1 2.62×, HEC-1-A 2.51×; ⚠ cell-cycle shift, explains ~74% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 3.93×, SW1417 3.75×; ⚠ cell-cycle shift, explains ~36% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.359× (z -4.1, q 0.022, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bisoprolol (hemifumarate) (drug)]] 5 µM in 1 line (AN3 CA 0.0685×); [[Cobimetinib (drug)]] 5 µM in 1 line (AN3 CA 0.0685×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF1]] (+0.80, fdr 7e-06), [[ERVK3-1]] (+0.73, fdr 7e-06), [[CROCCP2-1]] (+0.73, fdr 7e-06); moves opposite to [[NUP155]] (-0.70, fdr 7e-06), [[RPSA]] (-0.70, fdr 7e-06), [[EMC1]] (-0.69, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 12 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3588.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 5 lines (SW480 4.37×, HEC-1-A 4.22×, BT-474 7.79×, PANC-1 3.43×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Homoharringtonine (drug)]] 5 µM in 4 lines (hTERT-HPNE 5.74×, AsPC-1 3.42×, PANC-1 2.62×, HEC-1-A 2.51×; ⚠ cell-cycle shift, explains ~74% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 3.93×, SW1417 3.75×; ⚠ cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.21×** | +9.0 | 2e-16 | 47/47 (SW480, HEC-1-A, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.66×** | +7.5 | 2e-11 | 47/48 (SW480, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.83×** | +6.6 | 9e-09 | 36/47 (hTERT-HPNE, AsPC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.34×** | +6.5 | 9e-09 | 45/47 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +5.0 | 7e-05 | 38/47 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.88×** | +4.8 | 1e-04 | 38/47 (SW480, BT-474, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.83×** | +4.5 | 5e-04 | 33/48 (PANC-1, AsPC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.79×** | +4.5 | 5e-04 | 38/47 (PANC-1, hTERT-HPNE, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.5 | 5e-04 | 40/48 (MIA PaCa-2, J82, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.79×** | +4.3 | 8e-04 | 32/43 (NCI-H2030, SW480, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.66×** | +3.8 | 0.008 | 21/36 (NCI-H2030, HepG2/C3A, …) | two highest doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.65×** | +3.7 | 0.010 | 33/48 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~70% of this change | **1.55×** | +3.4 | 0.032 | 24/46 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +3.1 | 0.081 | 24/47 (NCI-H2030, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3588.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bisoprolol (hemifumarate) (drug)]] 5 µM in 1 line (AN3 CA 0.0685×); [[Cobimetinib (drug)]] 5 µM in 1 line (AN3 CA 0.0685×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.359×** | -4.1 | 0.022 | 30/48 (A-427, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.428× | -3.4 | 0.19 | 29/47 (SK-MEL-2, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.740× | -3.3 | 0.22 | 31/48 (LoVo, C-33 A, …) | all doses, flat |  |
| [[Folic acid (drug)]] 5 µM |  | 0.752× | -3.1 | 0.29 | 26/48 (AsPC-1, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3588. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.4 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.37× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[AN3 CA (line)]] | alt | 32.2 | 0 | 2 | — | [[Bisoprolol (hemifumarate) (drug)]] 5 µM 0.0685× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 33.7 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.22× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 21.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +9.5) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[AsPC-1 (line)]] | alt | 28.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +10.0) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[BT-474 (line)]] | alt | 13.6 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 7.79× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 33.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +11.9) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[LoVo (line)]] | wt | 25.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.30× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW1417 (line)]] | alt | 43.7 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +8.6) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A-172 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3588), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 11 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF1]] | +0.80 | +0.79 / +0.80 | both halves | 7e-06 | STRING 924 |
| [[ERVK3-1]] | +0.73 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | +0.73 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[COX17]] | +0.72 | +0.65 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR |
| [[GABARAPL2]] | +0.72 | +0.56 / +0.81 | both halves | 1e-05 |  |
| [[INAFM1]] | +0.72 | +0.65 / +0.79 | both halves | 7e-06 |  |
| [[LRCH3]] | +0.70 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[NACA4P]] ⚠ | +0.70 | +0.61 / +0.79 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[NKAP]] | +0.70 | +0.56 / +0.84 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | +0.70 | +0.59 / +0.77 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM258]] | +0.70 | +0.50 / +0.77 | both halves | 1e-05 |  |
| [[TERF2IP]] | +0.69 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[CDKN1C]] | +0.67 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[PNRC1]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP155]] | -0.70 | -0.60 / -0.75 | both halves | 7e-06 |  |
| [[RPSA]] | -0.70 | -0.65 / -0.71 | both halves | 7e-06 | STRING 799 |
| [[EMC1]] | -0.69 | -0.54 / -0.82 | both halves | 1e-05 |  |
| [[PAICS]] | -0.69 | -0.61 / -0.73 | both halves | 7e-06 |  |
| [[PRPF8]] | -0.67 | -0.67 / -0.67 | both halves | 7e-06 |  |
| [[HNRNPA3]] | -0.66 | -0.59 / -0.76 | both halves | 7e-06 |  |
| [[DLAT]] | -0.66 | -0.67 / -0.58 | both halves | 7e-06 |  |
| [[PRKDC]] | -0.66 | -0.55 / -0.73 | both halves | 1e-05 |  |
| [[SLC25A10]] | -0.66 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[MTHFD1]] | -0.65 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[ARF3]] | -0.65 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[DHX15]] | -0.64 | -0.64 / -0.72 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.760). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.8, -29.6); signed map (-15.5, 4.7). **Vector** length 89.1, 30.1% of its response variance represented; |z| ≥ 3 in 679 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.9 | +9.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.9 | +7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.8 | +6.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.1 | +4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +2.6 | +6.6 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +0.5 |
|  | [[Resveratrol (drug)]] 5 µM |  | +1.7 | +1.1 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.7 | +1.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.2 | -4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.7 | -3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.0 | +1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | -4.9 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | -4.3 | +4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | +1.6 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.1 — chr3:40,309,707-40,312,424 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GC20 |
| Hallmark sets | DNA_REPAIR |
| Matched by | ensembl_id |

**Function**, from UniProt [O60739](https://www.uniprot.org/uniprotkb/O60739) (Eukaryotic translation initiation factor 1b):

> Probably involved in translation.

**Summary**, from NCBI Gene [10289](https://www.ncbi.nlm.nih.gov/gene/10289):

> Enables RNA binding activity. Predicted to be involved in regulation of translational initiation. Predicted to be part of eukaryotic 43S preinitiation complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30792](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30792) · Entrez [10289](https://www.ncbi.nlm.nih.gov/gene/10289) · UniProt [O60739](https://www.uniprot.org/uniprotkb/O60739) · Ensembl [ENSG00000114784](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114784)

## Data

Gene col 3588: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3588); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3588, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3588]; `tensor/DDL_lfc|DDL_z.npy` [3588]; `embed/gene_vectors.npy` [3588]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3588 or target_col == 3588). Every well: [[EIF1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
