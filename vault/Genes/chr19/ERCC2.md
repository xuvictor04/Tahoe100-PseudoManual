---
symbol: "ERCC2"
type: "gene"
col: 2515
ensembl_id: "ENSG00000104884"
name: "ERCC excision repair 2, TFIIH core complex helicase subunit"
location: "19q13.32"
module: 2
arm: "+"
pooled_cpm: 11.05
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ERCC2

*ERCC excision repair 2, TFIIH core complex helicase subunit* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.67× (z +20.2, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.922× (z -5.9, q 2e-06, down in 8 of 48 measured lines) ⚠ position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 2 lines (NCI-H23 0.0677×, A-172 0.112×); [[Homoharringtonine (drug)]] 5 µM in 1 line (J82 0.229×; ⚠ cell-cycle shift, explains ~30% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SNU-1 0.0812×); [[Flutamide (drug)]] 0.5 µM in 1 line (C-33 A 0.177×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPM1F]] (+0.72, fdr 7e-06), [[TRABD]] (+0.71, fdr 1e-05), [[E2F4]] (+0.66, fdr 8e-06); moves opposite to [[PPP2R3C]] (-0.61, fdr 3e-04), [[PLEKHF2]] (-0.60, fdr 4e-05), [[RBM43]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2515.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.67×** | +20.2 | 0e+00 | 43/47 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.42×** | +18.2 | 0e+00 | 44/47 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.32×** | +17.3 | 0e+00 | 43/47 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +10.0 | 2e-21 | 32/47 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +9.5 | 4e-19 | 12/16 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +8.4 | 4e-15 | 20/45 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +7.9 | 2e-13 | 18/36 (SNU-423, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +6.8 | 8e-10 | 12/48 (HOP62, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.45×** | +5.5 | 2e-06 | 12/43 (NCI-H460, A-172, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +5.0 | 3e-05 | 11/47 (HOP62, SW 900, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.54×** | +4.7 | 1e-04 | 10/39 (SNU-1, SW 900, …) | two highest doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.7 | 1e-04 | 11/48 (SNU-1, LOX-IMVI, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +4.5 | 3e-04 | 9/47 (SW 900, SNU-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.26×** | +4.3 | 6e-04 | 9/24 (SNU-423, J82, …) | all doses, stronger at high dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.004 | 9/46 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | 1.19× | +3.7 | 0.009 | 6/43 (HT-29, SW 900, …) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.032 | 4/43 (LS 180, SNU-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.049 | 3/42 (BT-474, SW48, …) | inconsistent across doses |  |
| [[MK-8353 (drug)]] 5 µM |  | **1.31×** | +2.9 | 0.092 | 0/43 | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2515.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 2 lines (NCI-H23 0.0677×, A-172 0.112×); [[Homoharringtonine (drug)]] 5 µM in 1 line (J82 0.229×; ⚠ cell-cycle shift, explains ~30% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SNU-1 0.0812×); [[Flutamide (drug)]] 0.5 µM in 1 line (C-33 A 0.177×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -5.9 | 2e-06 | 8/48 (MIA PaCa-2, BT-474, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.855× | -4.6 | 0.001 | 18/44 (J82, HEC-1-A, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.796×** | -4.5 | 0.001 | 16/45 (A-427, J82, …) | top dose only | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.816×** | -4.2 | 0.004 | 17/44 (HEC-1-A, SNU-1, …) | rises with dose |  |
| [[Oleic acid (drug)]] 0.05 µM |  | 0.842× | -3.3 | 0.088 | 4/48 (NCI-H460, A549, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -3.3 | 0.088 | 16/44 (RKO, SW48, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.856× | -3.2 | 0.088 | 4/47 (SHP-77, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.856× | -3.2 | 0.088 | 2/48 (KATO III, COLO 205) | inconsistent across doses | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | 0.896× | -3.2 | 0.088 | 6/46 (Hs 766T, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2515. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 26.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.39× (z +11.9) | — |
| [[SNU-1 (line)]] | wt | 21.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0812× (z -10.5) |
| [[A-172 (line)]] | wt | 6.46 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.112× (z -9.3) |
| [[C-33 A (line)]] | alt | 17.5 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.177× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 24.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +9.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -15.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 8.13 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0677× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 6.88 | 0 | 1 | — | [[Hydroxyfasudil (drug)]] 5 µM 0.0656× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 9.97 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.106× (z -8.8) ⚠ toxic |
| [[SW480 (line)]] | alt | 11.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +8.7) | — |
| [[A-427 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2515), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPM1F]] | +0.72 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[TRABD]] | +0.71 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[E2F4]] | +0.66 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[POLRMT]] | +0.65 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[TBC1D24]] | +0.63 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[RRP1B]] | +0.62 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[NF2]] | +0.62 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[NOC2L]] | +0.62 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[C20orf27]] | +0.61 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[ATAD3A]] | +0.61 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ARHGAP8]] | +0.61 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[RNF123]] | +0.61 | +0.46 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP2R3C]] | -0.61 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[PLEKHF2]] | -0.60 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[RBM43]] | -0.60 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[PHYH]] | -0.60 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[C3orf38]] | -0.59 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[ZNF563]] | -0.58 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[ERCC6L2-AS1]] | -0.58 | -0.42 / -0.25 | both halves | 4e-04 |  |
| [[DNAJC27]] | -0.57 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[N4BP2L1]] | -0.57 | -0.41 / -0.31 | both halves | 2e-04 |  |
| [[ATF5]] | -0.57 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[ZNF341-AS1]] | -0.56 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[TCEAL4]] | -0.56 | -0.42 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-5.7, -25.7); signed map (-42.6, -9.7). **Vector** length 68.3, 10.4% of its response variance represented; |z| ≥ 3 in 1,004 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.4 | +20.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +9.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +17.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.9 | +18.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +7.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +4.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.1 | +1.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.0 | +5.5 |
|  | [[vincristine (drug)]] 5 µM |  | +1.9 | +4.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -3.7 | -4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -2.3 | -4.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -1.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | ERCC excision repair 2, TFIIH core complex helicase subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,349,837-45,370,918 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MAG, EM9, MGC102762, MGC126218, MGC126219; previously XPD |
| Gene groups (HGNC) | DEAH-box helicases; Xeroderma pigmentosum complementation groups; ERCC excision repair associated; General transcription factor IIH complex subunits |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, DNA_REPAIR |
| Reactome | 43 pathways, smallest: Cytosolic iron-sulfur cluster assembly; RNA Pol II CTD phosphorylation and interaction with CE during HIV infection; RNA Pol II CTD phosphorylation and interaction with CE |
| Matched by | ensembl_id |

**Function**, from UniProt [P18074](https://www.uniprot.org/uniprotkb/P18074) (General transcription and DNA repair factor IIH helicase subunit XPD):

> ATP-dependent 5'-3' DNA helicase. Component of the general transcription and DNA repair factor IIH (TFIIH) core complex, not absolutely essential for minimal transcription in vitro. Required for transcription-coupled nucleotide excision repair (NER) of damaged DNA; recognizes damaged bases. Sequestered in chromatin on UV-damaged DNA. When complexed to CDK-activating kinase (CAK), involved in transcription by RNA polymerase II. In NER, TFIIH acts by opening DNA around the lesion to allow the …

**Summary**, from NCBI Gene [2068](https://www.ncbi.nlm.nih.gov/gene/2068):

> The nucleotide excision repair pathway is a mechanism to repair damage to DNA. The protein encoded by this gene is involved in transcription-coupled nucleotide excision repair and is an integral member of the basal transcription factor BTF2/TFIIH complex. The gene product has ATP-dependent DNA helicase activity and belongs to the RAD3/XPD subfamily of helicases. Defects in this gene can result in three different disorders, the cancer-prone syndrome xeroderma pigmentosum complementation group D, …

**Accessions** — [HGNC:3434](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3434) · Entrez [2068](https://www.ncbi.nlm.nih.gov/gene/2068) · UniProt [P18074](https://www.uniprot.org/uniprotkb/P18074) · Ensembl [ENSG00000104884](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104884)

## Data

Gene col 2515: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2515); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2515, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2515]; `tensor/DDL_lfc|DDL_z.npy` [2515]; `embed/gene_vectors.npy` [2515]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2515 or target_col == 2515). Every well: [[ERCC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERCC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
