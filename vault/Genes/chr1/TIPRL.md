---
symbol: "TIPRL"
type: "gene"
col: 6684
ensembl_id: "ENSG00000143155"
name: "TOR signaling pathway regulator"
location: "1q24.2"
module: 50
arm: "+"
pooled_cpm: 63.58
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# TIPRL

*TOR signaling pathway regulator* — 1q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.82× (z +9.8, q 4e-20, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.32× (z +3.3, q 0.072, up in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (A-172 3.68×, NCI-H460 3.67×, NCI-H1573 2.50×, SW 900 2.87×, …; ⚠ cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (A-172 3.12×, NCI-H460 3.14×, NCI-H1573 2.76×; ⚠ cell-cycle shift, explains ~25% of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (NCI-H460 3.57×, NCI-H1573 3.13×, A-172 2.74×; ⚠ cell-cycle shift, explains ~38% of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.402× (z -5.5, q 2e-05, down in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Folic acid (drug)]] 5 µM in 1 line (NCI-H661 0.218×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NKAP]] (+0.69, fdr 7e-06), [[RBMX2]] (+0.67, fdr 7e-06), [[GATAD1]] (+0.66, fdr 7e-06); moves opposite to [[PPIA]] (-0.68, fdr 1e-05), [[MATN3]] (-0.66, fdr 1e-05), [[CTSZ]] (-0.64, fdr 7e-06).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6684.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (A-172 3.68×, NCI-H460 3.67×, NCI-H1573 2.50×, SW 900 2.87×, …; ⚠ cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (A-172 3.12×, NCI-H460 3.14×, NCI-H1573 2.76×; ⚠ cell-cycle shift, explains ~25% of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (NCI-H460 3.57×, NCI-H1573 3.13×, A-172 2.74×; ⚠ cell-cycle shift, explains ~38% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.82×** | +9.8 | 4e-20 | 44/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.97×** | +7.6 | 1e-11 | 45/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.68×** | +6.0 | 3e-07 | 39/48 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +5.5 | 7e-06 | 39/47 (Hs 766T, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.43×** | +4.0 | 0.006 | 26/43 (A-172, RPMI-7951, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.77×** | +3.8 | 0.012 | 31/49 (MIA PaCa-2, A-172, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.35×** | +3.5 | 0.035 | 27/48 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **1.35×** | +3.3 | 0.058 | 25/47 (NCI-H23, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.072 | 23/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.34×** | +3.2 | 0.082 | 24/45 (RKO, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~77% of this change | **1.31×** | +3.1 | 0.087 | 26/48 (SW 900, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.30× | +3.1 | 0.10 | 27/48 (HOP62, CFPAC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6684.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Folic acid (drug)]] 5 µM in 1 line (NCI-H661 0.218×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.402×** | -5.5 | 2e-05 | 40/48 (RPMI-7951, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.505×** | -4.1 | 0.010 | 32/49 (SNU-1, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.789×** | -3.9 | 0.020 | 33/48 (SK-MEL-2, A-427, …) | all doses, flat | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.763× | -3.1 | 0.23 | 29/48 (COLO 205, A549, …) | all doses, flat | position effect removed |
| [[Anethole trithione (drug)]] 0.05 µM |  | 0.769× | -3.0 | 0.23 | 25/48 (MIA PaCa-2, SW480, …) | all doses, flat | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | 0.770× | -3.0 | 0.23 | 19/48 (A498, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6684. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 104 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +19.0) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H1573 (line)]] | alt | 57.8 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.5) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H460 (line)]] | wt | 82.8 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +17.1) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[LoVo (line)]] | wt | 36.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.0) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[PANC-1 (line)]] | alt | 89.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.5) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[SW 900 (line)]] | alt | 74.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +11.6) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[A498 (line)]] | wt | 99.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.1) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[A549 (line)]] | wt | 67.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +10.5) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[BT-474 (line)]] | alt | 53.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +8.9) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[C32 (line)]] | wt | 61.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.1) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[HEC-1-A (line)]] | alt | 51.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.8) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[HS-578T (line)]] | alt | 62.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.6) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 48.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +10.3) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H2347 (line)]] | alt | 63.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +8.5) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H661 (line)]] | alt | 68.5 | 0 | 1 | — | [[Folic acid (drug)]] 5 µM 0.218× (z -9.7) |
| [[SNU-423 (line)]] | alt | 49.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.7) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[A-427 (line)]] | wt | 94.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 71.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 73.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 51.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6684), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKAP]] | +0.69 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[GATAD1]] | +0.66 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[CEP290]] | +0.65 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | +0.64 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[TTBK2]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[RP9]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[FRA10AC1]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SMIM29]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[RNF166]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ATF4]] | +0.60 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[UPF3B]] | +0.60 | +0.65 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIA]] | -0.68 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[MATN3]] | -0.66 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[CTSZ]] | -0.64 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[ARHGEF7]] | -0.64 | -0.71 / -0.65 | both halves | 7e-06 |  |
| [[SELENON]] | -0.61 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[LAMP1]] | -0.60 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[NOP9]] | -0.60 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[ATP2A2]] | -0.59 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[EMC1]] | -0.59 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[DDOST]] | -0.59 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[RNPS1]] | -0.59 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[NAGA]] | -0.58 | -0.54 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction -0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.4, -11.9); signed map (-17.2, -9.2). **Vector** length 89.4, 28.3% of its response variance represented; |z| ≥ 3 in 633 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +7.5 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +6.3 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +6.1 | +7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | -6.2 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -1.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.9 | -4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.8 | -5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | -5.7 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | +0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | TOR signaling pathway regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.2 — chr1:168,178,962-168,202,109 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3794, dJ69E11.3, TIP41, TIPRL1 |
| Gene groups (HGNC) | Protein phosphatase 2 modulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [O75663](https://www.uniprot.org/uniprotkb/O75663) (TIP41-like protein):

> May be a allosteric regulator of serine/threonine-protein phosphatase 2A (PP2A). Isoform 1 inhibits catalytic activity of the PP2A(D) core complex in vitro. The PP2A(C):TIPRL complex does not show phosphatase activity. Acts as a negative regulator of serine/threonine-protein phosphatase 4 probably by inhibiting the formation of the active PPP4C:PPP4R2 complex; the function is proposed to implicate it in DNA damage response by promoting H2AX phosphorylated on Ser-140 (gamma-H2AX). May play a …

**Summary**, from NCBI Gene [261726](https://www.ncbi.nlm.nih.gov/gene/261726):

> TIPRL is an inhibitory regulator of protein phosphatase-2A (PP2A) (see PPP2CA; MIM 176915), PP4 (see PPP4C; MIM 602035), and PP6 (see PPP6C; MIM 612725) (McConnell et al., 2007 [PubMed 17384681]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:30231](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30231) · Entrez [261726](https://www.ncbi.nlm.nih.gov/gene/261726) · UniProt [O75663](https://www.uniprot.org/uniprotkb/O75663) · Ensembl [ENSG00000143155](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143155)

## Data

Gene col 6684: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6684); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6684, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6684]; `tensor/DDL_lfc|DDL_z.npy` [6684]; `embed/gene_vectors.npy` [6684]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6684 or target_col == 6684). Every well: [[TIPRL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIPRL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
