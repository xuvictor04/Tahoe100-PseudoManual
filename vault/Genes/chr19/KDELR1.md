---
symbol: "KDELR1"
type: "gene"
col: 2604
ensembl_id: "ENSG00000105438"
name: "KDEL endoplasmic reticulum protein retention receptor 1"
location: "19q13.33"
module: 40
arm: "+"
pooled_cpm: 112.15
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# KDELR1

*KDEL endoplasmic reticulum protein retention receptor 1* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.57× (z +10.0, q 1e-20, up in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.33× (z +4.7, q 3e-04, up in 34 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 12 lines (PANC-1 3.76×, NCI-H460 3.57×, HEC-1-A 2.95×, A498 2.84×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 2.68×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.321× (z -18.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPA]] (+0.76, fdr 7e-06), [[NUCB2]] (+0.74, fdr 7e-06), [[SEZ6L2]] (+0.73, fdr 7e-06); moves opposite to [[COA7]] (-0.75, fdr 7e-06), [[TMEM185B]] (-0.72, fdr 7e-06), [[N6AMT1]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2604.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 12 lines (PANC-1 3.76×, NCI-H460 3.57×, HEC-1-A 2.95×, A498 2.84×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 2.68×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +10.0 | 1e-20 | 42/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +7.4 | 5e-11 | 46/49 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +6.2 | 1e-07 | 40/45 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.50×** | +4.8 | 3e-04 | 39/48 (AsPC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.7 | 3e-04 | 34/49 (NCI-H2347, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.044 | 38/48 (A-427, J82, …) | top dose only | position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | 1.33× | +3.0 | 0.20 | 30/48 (A-172, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2604.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.321×** | -18.9 | 0e+00 | 48/48 (SNU-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.360×** | -12.0 | 1e-30 | 48/48 (HOP62, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.434×** | -8.9 | 1e-16 | 44/48 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.700×** | -4.2 | 0.004 | 33/48 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.706×** | -4.1 | 0.005 | 35/48 (BT-474, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.719×** | -3.9 | 0.010 | 31/48 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.736×** | -3.6 | 0.025 | 30/48 (AsPC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.633×** | -3.4 | 0.052 | 30/48 (hTERT-HPNE, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.819×** | -3.3 | 0.055 | 26/48 (RPMI-7951, KATO III, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.755×** | -3.3 | 0.055 | 35/48 (SW1417, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.768×** | -3.1 | 0.097 | 28/47 (BT-474, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2604. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 95.6 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -21.4) |
| [[A498 (line)]] | wt | 168 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -10.5) |
| [[A549 (line)]] | wt | 152 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 97.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -19.5) |
| [[H4 (line)]] | wt | 165 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -16.4) |
| [[HEC-1-A (line)]] | alt | 141 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -11.2) |
| [[HT-29 (line)]] | alt | 183 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -23.2) |
| [[KATO III (line)]] | alt | 158 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.63× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -19.6) |
| [[LoVo (line)]] | wt | 123 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 93.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -15.7) |
| [[MIA PaCa-2 (line)]] | alt | 138 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -15.9) |
| [[NCI-H2347 (line)]] | alt | 133 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -19.2) |
| [[NCI-H460 (line)]] | wt | 69.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -15.8) |
| [[Panc 03.27 (line)]] | alt | 97.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -16.1) |
| [[SW480 (line)]] | alt | 104 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.57× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -13.6) |
| [[A-427 (line)]] | wt | 69.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 110 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -20.4) |
| [[COLO 205 (line)]] | alt | 97.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -18.8) |
| [[HCT15 (line)]] | alt | 188 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -15.4) |
| [[HS-578T (line)]] | alt | 157 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -15.5) |
| [[hTERT-HPNE (line)]] | wt | 154 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -16.1) |
| [[J82 (line)]] | alt | 111 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -17.8) |
| [[LS 180 (line)]] | wt | 165 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -18.4) |
| [[NCI-H1573 (line)]] | alt | 46.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 121 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -10.4) |
| [[PANC-1 (line)]] | alt | 53.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 131 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -19.8) |
| [[SK-MEL-2 (line)]] | alt | 79.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.78× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -9.9) |
| [[SNU-1 (line)]] | wt | 130 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0909× (z -24.4) |
| [[SW 900 (line)]] | alt | 114 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -15.7) |
| [[SW1417 (line)]] | alt | 196 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -15.0) |
| [[SW48 (line)]] | wt | 115 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -13.6) |
| [[A-172 (line)]] | wt | 78.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.388× (z -8.7) |
| [[AN3 CA (line)]] | alt | 91.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -9.3) |
| [[BT-474 (line)]] | alt | 88.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -11.7) |
| [[C-33 A (line)]] | alt | 111 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -9.4) |
| [[C32 (line)]] | wt | 95.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -8.5) |
| [[Hs 766T (line)]] | wt | 94.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -14.6) |
| [[NCI-H2030 (line)]] | alt | 113 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 73.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.3) |
| [[SHP-77 (line)]] | alt | 48.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 92.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -9.6) |
| [[SW 1271 (line)]] | alt | 82.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -8.7) |
| [[CHP-212 (line)]] | wt | 80.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 132 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2604), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPA]] | +0.76 | +0.83 / +0.66 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 702 |
| [[NUCB2]] | +0.74 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[SEZ6L2]] | +0.73 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[RAB6A]] | +0.73 | +0.74 / +0.74 | both halves | 7e-06 | pathway: Golgi-to-ER retrograde transport |
| [[IER3IP1]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[DPM1]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[GPR107]] | +0.71 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[MED26]] | +0.71 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.71 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[YIPF2]] | +0.71 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[SRP54]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[ALKBH5]] | +0.71 | +0.70 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COA7]] | -0.75 | -0.75 / -0.71 | both halves | 7e-06 |  |
| [[TMEM185B]] | -0.72 | -0.65 / -0.73 | both halves | 7e-06 |  |
| [[N6AMT1]] | -0.71 | -0.65 / -0.72 | both halves | 7e-06 |  |
| [[GPATCH4]] | -0.70 | -0.76 / -0.63 | both halves | 7e-06 |  |
| [[CMTR2]] | -0.67 | -0.74 / -0.56 | both halves | 1e-05 |  |
| [[RTL6]] | -0.67 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[MAPK1IP1L]] | -0.67 | -0.69 / -0.57 | both halves | 1e-05 |  |
| [[SLC35A4]] | -0.67 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.66 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[CHTOP]] | -0.66 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[ZNF480]] | -0.65 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[PPIL1]] | -0.64 | -0.61 / -0.63 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises KDELR1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises KDELR1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.778). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (5.1, -18.7); signed map (-42.9, 13.8). **Vector** length 89.9, 34.2% of its response variance represented; |z| ≥ 3 in 700 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -0.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -1.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.7 | -4.1 |
|  | [[Rifaximin (drug)]] 0.5 µM |  | +1.5 | +0.3 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | +1.5 | +1.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Rifaximin (drug)]] 5 µM |  | +1.3 | +0.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.3 | +0.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.7 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.5 | -12.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.7 | -4.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.4 | -8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.4 | -18.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.1 | -2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.9 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | KDEL endoplasmic reticulum protein retention receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,382,575-48,391,551 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ERD2.1, ERD2, HDEL |
| Gene groups (HGNC) | KDEL endoplasmic reticulum protein retention receptors |
| Reactome | 12 pathways, smallest: Assembly and Release of Dengue Virus Virions; COPI-dependent Golgi-to-ER retrograde traffic; COPI-mediated anterograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P24390](https://www.uniprot.org/uniprotkb/P24390) (ER lumen protein-retaining receptor 1):

> Receptor for the C-terminal sequence motif K-D-E-L that is present on endoplasmic reticulum resident proteins and that mediates their recycling from the Golgi back to the endoplasmic reticulum.

**Summary**, from NCBI Gene [10945](https://www.ncbi.nlm.nih.gov/gene/10945):

> Retention of resident soluble proteins in the lumen of the endoplasmic reticulum (ER) is achieved in both yeast and animal cells by their continual retrieval from the cis-Golgi, or a pre-Golgi compartment. Sorting of these proteins is dependent on a C-terminal tetrapeptide signal, usually lys-asp-glu-leu (KDEL) in animal cells, and his-asp-glu-leu (HDEL) in S. cerevisiae. This process is mediated by a receptor that recognizes, and binds the tetrapeptide-containing protein, and returns it to the …

**Accessions** — [HGNC:6304](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6304) · Entrez [10945](https://www.ncbi.nlm.nih.gov/gene/10945) · UniProt [P24390](https://www.uniprot.org/uniprotkb/P24390) · Ensembl [ENSG00000105438](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105438)

## Data

Gene col 2604: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2604); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2604, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2604]; `tensor/DDL_lfc|DDL_z.npy` [2604]; `embed/gene_vectors.npy` [2604]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2604 or target_col == 2604). Every well: [[KDELR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDELR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
