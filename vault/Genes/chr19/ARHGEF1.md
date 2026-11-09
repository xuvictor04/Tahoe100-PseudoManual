---
symbol: "ARHGEF1"
type: "gene"
col: 1167
ensembl_id: "ENSG00000076928"
name: "Rho guanine nucleotide exchange factor 1"
location: "19q13.2"
module: 2
arm: "+"
pooled_cpm: 45.65
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 24
n_dd_up_clean: 1
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ARHGEF1

*Rho guanine nucleotide exchange factor 1* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.33× (z +4.4, q 0.007, up in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 2.80×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SW48 4.20×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2030 2.81×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.447× (z -17.4, q 0e+00, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAPGEF3]] (+0.69, fdr 7e-06), [[PPP4C]] (+0.65, fdr 7e-06), [[RER1]] (+0.63, fdr 7e-06); moves opposite to [[RBM43]] (-0.54, fdr 4e-05), [[ATG10]] (-0.53, fdr 1e-05), [[REL]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1167.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 2.80×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SW48 4.20×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2030 2.81×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +4.4 | 0.007 | 24/48 (SW1417, NCI-H2347, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1167.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.447×** | -17.4 | 0e+00 | 33/47 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.453×** | -12.1 | 3e-31 | 37/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.443×** | -12.0 | 1e-30 | 44/48 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.622×** | -10.3 | 2e-22 | 39/48 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.538×** | -9.5 | 3e-19 | 40/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.564×** | -8.8 | 2e-16 | 37/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.578×** | -8.4 | 4e-15 | 37/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.597×** | -7.9 | 2e-13 | 38/48 (H4, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.603×** | -7.7 | 6e-13 | 35/48 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.718×** | -7.2 | 5e-11 | 31/48 (J82, SW48, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.437×** | -6.6 | 2e-09 | 36/49 (Panc 03.27, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.657×** | -6.4 | 6e-09 | 30/46 (KATO III, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -6.4 | 6e-09 | 31/47 (HOP62, SW 900, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -5.5 | 1e-06 | 28/49 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.706×** | -5.3 | 4e-06 | 33/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.758×** | -4.2 | 8e-04 | 25/48 (SK-MEL-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1167. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 80.6 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -15.6) |
| [[HOP62 (line)]] | alt | 42.9 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -12.3) |
| [[J82 (line)]] | alt | 49.3 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -16.8) |
| [[NCI-H1573 (line)]] | alt | 47.4 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -15.2) |
| [[PANC-1 (line)]] | alt | 31.3 | 0 | 6 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.271× (z -13.2) |
| [[SW48 (line)]] | wt | 131 | 1 | 4 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 4.20× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -12.6) |
| [[A-172 (line)]] | wt | 79.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 54.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0665× (z -24.0) |
| [[COLO 205 (line)]] | alt | 54.1 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.182× (z -11.5) |
| [[H4 (line)]] | wt | 65.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -17.0) |
| [[A549 (line)]] | wt | 75.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -17.7) |
| [[HS-578T (line)]] | alt | 44.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.324× (z -10.1) |
| [[KATO III (line)]] | alt | 70.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -16.2) |
| [[NCI-H2030 (line)]] | alt | 38.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.81× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -9.8) |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -12.1) |
| [[Hs 766T (line)]] | wt | 37.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -11.4) |
| [[HT-29 (line)]] | alt | 72.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -19.1) |
| [[LOX-IMVI (line)]] | wt | 51.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.371× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 32.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0809× (z -20.1) |
| [[NCI-H2347 (line)]] | alt | 43.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -13.3) |
| [[Panc 03.27 (line)]] | alt | 47.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -16.7) |
| [[SW 900 (line)]] | alt | 39.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -13.0) |
| [[A-427 (line)]] | wt | 22.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -10.7) |
| [[C32 (line)]] | wt | 42.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +11.0) | — |
| [[CFPAC-1 (line)]] | alt | 39.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -10.8) |
| [[HCT15 (line)]] | alt | 62.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 45.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -11.2) |
| [[LS 180 (line)]] | wt | 40.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 33.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -13.9) |
| [[NCI-H23 (line)]] | alt | 42.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.278× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 32.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.418× (z -8.9) |
| [[RKO (line)]] | wt | 53.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -13.5) |
| [[RPMI-7951 (line)]] | alt | 57.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -8.5) |
| [[SHP-77 (line)]] | alt | 37.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 24.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -9.0) |
| [[SW1417 (line)]] | alt | 30.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -11.1) |
| [[A498 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1167), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAPGEF3]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[PPP4C]] | +0.65 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[RER1]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[FBRSL1]] | +0.63 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[DPP9]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[EPN1]] | +0.61 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[EHBP1L1]] | +0.61 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[WDR55]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[PLEKHG5]] | +0.60 | +0.67 / +0.55 | both halves | 1e-05 | same gene group; pathway: Cell death signalling via NRAGE, NRIF and NADE; STRING 505 |
| [[GAK]] | +0.59 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[MIER2]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ARHGAP4]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 | pathway: RHOA GTPase cycle |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM43]] | -0.54 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[ATG10]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[REL]] | -0.52 | -0.43 / -0.58 | both halves | 4e-05 |  |
| [[TLR3]] | -0.51 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[NR1D2]] | -0.50 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[SIRT1]] | -0.50 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[DENND4C]] | -0.49 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[ZNF292]] | -0.49 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[DNAJC27]] | -0.49 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[MTUS1-DT]] | -0.49 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[MARCKS]] | -0.49 | -0.39 / -0.47 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.600). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (8.4, -26.5); signed map (-50.1, 1.2). **Vector** length 93.6, 23.3% of its response variance represented; |z| ≥ 3 in 1,175 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.8 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.3 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.5 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | -2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +2.8 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +2.0 | +1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +1.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.2 | -7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.9 | -12.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.7 | -2.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.4 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:41,883,173-41,930,150 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P115-RHOGEF, SUB1.5, LBCL2 |
| Gene groups (HGNC) | Dbl family Rho GEFs |
| Reactome | 13 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; RHOB GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92888](https://www.uniprot.org/uniprotkb/Q92888) (Rho guanine nucleotide exchange factor 1):

> Seems to play a role in the regulation of RhoA GTPase by guanine nucleotide-binding alpha-12 (GNA12) and alpha-13 (GNA13) subunits. Acts as a GTPase-activating protein (GAP) for GNA12 and GNA13, and as guanine nucleotide exchange factor (GEF) for RhoA GTPase. Activated G alpha 13/GNA13 stimulates the RhoGEF activity through interaction with the RGS-like domain. This GEF activity is inhibited by binding to activated GNA12. Mediates angiotensin-2-induced RhoA activation. In lymphoid follicles, …

**Summary**, from NCBI Gene [9138](https://www.ncbi.nlm.nih.gov/gene/9138):

> Rho GTPases play a fundamental role in numerous cellular processes that are initiated by extracellular stimuli that work through G protein coupled receptors. The encoded protein may form complex with G proteins and stimulate Rho-dependent signals. Multiple alternatively spliced transcript variants have been found for this gene, but the full-length nature of some variants has not been defined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:681](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:681) · Entrez [9138](https://www.ncbi.nlm.nih.gov/gene/9138) · UniProt [Q92888](https://www.uniprot.org/uniprotkb/Q92888) · Ensembl [ENSG00000076928](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076928)

## Data

Gene col 1167: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1167); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1167, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1167]; `tensor/DDL_lfc|DDL_z.npy` [1167]; `embed/gene_vectors.npy` [1167]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1167 or target_col == 1167). Every well: [[ARHGEF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
