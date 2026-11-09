---
symbol: "SRP14"
type: "gene"
col: 6389
ensembl_id: "ENSG00000140319"
name: "signal recognition particle 14"
location: "15q22"
module: 60
arm: "+"
pooled_cpm: 92.92
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# SRP14

*signal recognition particle 14* — 15q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.67× (z +11.5, q 8e-28, up in 48 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.85× (z +4.6, q 5e-04, up in 35 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.247×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOD1]] (+0.63, fdr 1e-05), [[PSMB4]] (+0.60, fdr 1e-05), [[TMEM59]] (+0.59, fdr 3e-05); moves opposite to [[ENTR1]] (-0.67, fdr 9e-06), [[KLF16]] (-0.60, fdr 4e-05), [[CEP83]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6389.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **4.67×** | +11.5 | 8e-28 | 48/48 (HOP62, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.97×** | +9.9 | 1e-20 | 44/44 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.73×** | +6.9 | 8e-10 | 40/45 (HOP62, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +4.6 | 5e-04 | 35/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +4.6 | 5e-04 | 42/47 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.4 | 8e-04 | 35/49 (A-172, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.73×** | +4.1 | 0.004 | 43/48 (HOP62, NCI-H2030, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.68×** | +3.9 | 0.007 | 37/47 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +3.3 | 0.056 | 34/48 (SNU-423, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **1.55×** | +3.3 | 0.061 | 32/48 (PANC-1, KATO III, …) | top dose only | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.247×; ⚠ cell-cycle shift, explains ~0% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6389. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 86.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +8.7) | — |
| [[A549 (line)]] | wt | 73.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.80× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HOP62 (line)]] | alt | 69.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.54× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 60.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.61× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[AsPC-1 (line)]] | alt | 54.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.19× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[C32 (line)]] | wt | 92.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 87.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.96× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[J82 (line)]] | alt | 122 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[KATO III (line)]] | alt | 165 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LoVo (line)]] | wt | 113 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.00× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LOX-IMVI (line)]] | wt | 89.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.05× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 127 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1573 (line)]] | alt | 91.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.36× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 70.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.38× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H460 (line)]] | wt | 43.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.62× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 103 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[RPMI-7951 (line)]] | alt | 155 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SNU-423 (line)]] | alt | 91.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.90× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW 900 (line)]] | alt | 119 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 65.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[AN3 CA (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.44× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[CFPAC-1 (line)]] | alt | 109 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[COLO 205 (line)]] | alt | 121 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[H4 (line)]] | wt | 71.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HCT15 (line)]] | alt | 92.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HEC-1-A (line)]] | alt | 105 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[Hs 766T (line)]] | wt | 89.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HS-578T (line)]] | alt | 56.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.55× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HT-29 (line)]] | alt | 95.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 214 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[Panc 03.27 (line)]] | alt | 94.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[RKO (line)]] | wt | 145 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SHP-77 (line)]] | alt | 61.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.00× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 112 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SNU-1 (line)]] | wt | 92.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW48 (line)]] | wt | 99.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW480 (line)]] | alt | 56.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.69× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-427 (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 151 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 109 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 67.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6389), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOD1]] | +0.63 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[PSMB4]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[TMEM59]] | +0.59 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[NDUFA4]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[HSPB1]] | +0.58 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[ATP6V0E1]] | +0.56 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[FTL]] | +0.56 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[ATP6V1G1]] | +0.56 | +0.46 / +0.57 | both halves | 3e-05 | STRING 428 |
| [[ARPC3]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[HSBP1]] | +0.53 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[ST13]] | +0.53 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[MYL6B]] | +0.53 | +0.55 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENTR1]] | -0.67 | -0.57 / -0.67 | both halves | 9e-06 |  |
| [[KLF16]] | -0.60 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[CEP83]] | -0.58 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[RRP9]] | -0.53 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[THOP1]] | -0.53 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[RBFA]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[PUS1]] | -0.52 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[CPNE7]] | -0.52 | -0.49 / -0.53 | both halves | 2e-05 |  |
| [[CLUH]] | -0.52 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[RIOK1]] | -0.51 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[EEFSEC]] | -0.50 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[TRIM65]] | -0.50 | -0.57 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.377). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-17.3, -11.1); signed map (-23.7, -25.9). **Vector** length 55.4, 18.2% of its response variance represented; |z| ≥ 3 in 528 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.7 | +2.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +4.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | -0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +1.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -1.9 | +11.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | +0.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | signal recognition particle 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22 — chr15:40,035,690-40,039,181 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ALURBP, MGC14326 |
| Gene groups (HGNC) | Signal recognition particle |
| Hallmark sets | PANCREAS_BETA_CELLS |
| Reactome | 4 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P37108](https://www.uniprot.org/uniprotkb/P37108) (Signal recognition particle 14 kDa protein):

> Component of the signal recognition particle (SRP) complex, a ribonucleoprotein complex that mediates the cotranslational targeting of secretory and membrane proteins to the endoplasmic reticulum (ER). SRP9 together with SRP14 and the Alu portion of the SRP RNA, constitutes the elongation arrest domain of SRP. The complex of SRP9 and SRP14 is required for SRP RNA binding.

**Summary**, from NCBI Gene [6727](https://www.ncbi.nlm.nih.gov/gene/6727):

> Enables RNA binding activity. Involved in protein targeting to ER. Located in nucleus. Part of signal recognition particle, endoplasmic reticulum targeting. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11299](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11299) · Entrez [6727](https://www.ncbi.nlm.nih.gov/gene/6727) · UniProt [P37108](https://www.uniprot.org/uniprotkb/P37108) · Ensembl [ENSG00000140319](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140319)

## Data

Gene col 6389: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6389); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6389, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6389]; `tensor/DDL_lfc|DDL_z.npy` [6389]; `embed/gene_vectors.npy` [6389]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6389 or target_col == 6389). Every well: [[SRP14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRP14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
