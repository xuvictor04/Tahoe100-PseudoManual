---
symbol: "NKIRAS1"
type: "gene"
col: 12482
ensembl_id: "ENSG00000197885"
name: "NFKB inhibitor interacting Ras like 1"
location: "3p24.2"
module: 46
arm: "+"
pooled_cpm: 20.16
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# NKIRAS1

*NFKB inhibitor interacting Ras like 1* — 3p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.15× (z +23.9, q 0e+00, up in 47 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Valdecoxib (drug)]] 0.5 µM in 1 line (AN3 CA 0.0700×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.195×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HCT15 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[OTS514 (drug)]] 5 µM in 1 line (SHP-77 0.0952×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF821]] (+0.68, fdr 1e-05), [[HOXB-AS3]] (+0.65, fdr 1e-05), [[LINC00938]] (+0.59, fdr 2e-04); moves opposite to [[HAUS7]] (-0.59, fdr 5e-05), [[GNB1L]] (-0.57, fdr 3e-04), [[EP400P1]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12482.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +23.9 | 0e+00 | 47/47 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +20.7 | 0e+00 | 40/47 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.78×** | +12.8 | 4e-35 | 35/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +10.9 | 2e-25 | 31/44 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +10.7 | 1e-24 | 38/47 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.65×** | +10.7 | 2e-24 | 32/48 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +10.6 | 3e-24 | 35/46 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +9.2 | 3e-18 | 26/47 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +8.8 | 7e-17 | 30/48 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +8.7 | 2e-16 | 33/48 (J82, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +8.5 | 8e-16 | 28/47 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +8.4 | 3e-15 | 26/48 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +8.3 | 5e-15 | 28/46 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +8.2 | 1e-14 | 26/48 (HS-578T, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +8.1 | 2e-14 | 24/47 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +8.1 | 2e-14 | 32/48 (NCI-H1792, J82, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +7.2 | 2e-11 | 28/47 (NCI-H1792, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12482.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Valdecoxib (drug)]] 0.5 µM in 1 line (AN3 CA 0.0700×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.195×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HCT15 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[OTS514 (drug)]] 5 µM in 1 line (SHP-77 0.0952×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.866× | -3.2 | 0.47 | 6/48 (CHP-212, C-33 A, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.870× | -3.1 | 0.47 | 9/47 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.908× | -3.0 | 0.47 | 5/48 (NCI-H2347, Panc 03.27, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12482. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.2 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.63× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +12.2) | — |
| [[HOP62 (line)]] | alt | 22.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +15.5) | — |
| [[SW1417 (line)]] | alt | 34.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +11.1) | — |
| [[A-172 (line)]] | wt | 17.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 13.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +11.1) | — |
| [[HCT15 (line)]] | alt | 26.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[J82 (line)]] | alt | 13.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +11.3) | — |
| [[LoVo (line)]] | wt | 23.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +15.3) | — |
| [[NCI-H460 (line)]] | wt | 17.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 22.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +9.6) | — |
| [[A498 (line)]] | wt | 15.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 33.4 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0700× (z -11.0) |
| [[C-33 A (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[HEC-1-A (line)]] | alt | 28.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +11.5) | — |
| [[HS-578T (line)]] | alt | 14.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 25.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 21.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +12.9) | — |
| [[Panc 03.27 (line)]] | alt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.3) | — |
| [[RKO (line)]] | wt | 23.4 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.297× (z -8.6) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 34.3 | 0 | 1 | — | [[OTS514 (drug)]] 5 µM 0.0952× (z -9.4) |
| [[SW480 (line)]] | alt | 18.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +11.9) | — |
| [[A-427 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12482), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF821]] | +0.68 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[HOXB-AS3]] | +0.65 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[LINC00938]] | +0.59 | +0.51 / +0.31 | both halves | 2e-04 |  |
| [[NAA38]] | +0.58 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[TSTD3]] | +0.57 | +0.54 / +0.28 | both halves | 3e-04 |  |
| [[CHMP3-AS1]] | +0.57 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[PRRG4]] | +0.57 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[HOXC9]] | +0.57 | +0.31 / +0.35 | both halves | 2e-04 |  |
| [[RBMS3-AS3]] | +0.57 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[SPEN-AS1]] | +0.57 | +0.52 / +0.37 | both halves | 9e-05 |  |
| [[C2CD5-AS1]] | +0.56 | +0.43 / +0.41 | both halves | 4e-05 |  |
| [[HOXA-AS2]] | +0.56 | +0.48 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAUS7]] | -0.59 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[GNB1L]] | -0.57 | -0.57 / -0.28 | both halves | 3e-04 |  |
| [[EP400P1]] | -0.56 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[SLC39A3]] | -0.55 | -0.45 / -0.25 | both halves | 4e-04 |  |
| [[RPUSD1]] | -0.54 | -0.35 / -0.30 | both halves | 2e-04 |  |
| [[EEFSEC]] | -0.53 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[C13orf46]] | -0.53 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[SCART1]] | -0.53 | -0.44 / -0.27 | both halves | 3e-04 |  |
| [[PITPNB]] | -0.52 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[TRAPPC9]] | -0.52 | -0.26 / -0.43 | both halves | 4e-04 |  |
| [[IQCH]] | -0.51 | -0.10 / -0.48 | ⚠ not reproduced | 0.003 |  |
| [[YWHAB]] | -0.50 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[RNGTT]] | -0.50 | -0.49 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.542). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-0.6, 26.2); signed map (38.8, -3.4). **Vector** length 57.4, 8.66% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +23.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.4 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +2.8 | +12.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +2.6 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.5 | +8.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | +8.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.3 | +10.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | -1.7 | +1.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -2.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.0 | -2.4 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -0.9 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | NFKB inhibitor interacting Ras like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.2 — chr3:23,889,951-23,946,591 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KBRAS1, kappaB-Ras1 |
| Gene groups (HGNC) | RAS type GTPase family |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 27 pathways, smallest: RIP-mediated NFkB activation via ZBP1; ZBP1(DAI) mediated induction of type I IFNs; TRAF6 mediated NF-kB activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYS0](https://www.uniprot.org/uniprotkb/Q9NYS0) (NF-kappa-B inhibitor-interacting Ras-like protein 1):

> Atypical Ras-like protein that acts as a potent regulator of NF-kappa-B activity by preventing the degradation of NF-kappa-B inhibitor beta (NFKBIB) by most signals, explaining why NFKBIB is more resistant to degradation. May act by blocking phosphorylation of NFKBIB and mediating cytoplasmic retention of p65/RELA NF-kappa-B subunit. It is unclear whether it acts as a GTPase. Both GTP- and GDP-bound forms block phosphorylation of NFKBIB.

**Summary**, from NCBI Gene [28512](https://www.ncbi.nlm.nih.gov/gene/28512):

> Predicted to enable GTPase activating protein binding activity. Predicted to be involved in Ral protein signal transduction. Predicted to act upstream of or within lung alveolus development; regulation of tumor necrosis factor-mediated signaling pathway; and surfactant homeostasis. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17899](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17899) · Entrez [28512](https://www.ncbi.nlm.nih.gov/gene/28512) · UniProt [Q9NYS0](https://www.uniprot.org/uniprotkb/Q9NYS0) · Ensembl [ENSG00000197885](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197885)

## Data

Gene col 12482: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12482); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12482, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12482]; `tensor/DDL_lfc|DDL_z.npy` [12482]; `embed/gene_vectors.npy` [12482]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12482 or target_col == 12482). Every well: [[NKIRAS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NKIRAS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
