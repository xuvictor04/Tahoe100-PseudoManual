---
symbol: "ACAD8"
type: "gene"
col: 7529
ensembl_id: "ENSG00000151498"
name: "acyl-CoA dehydrogenase family member 8"
location: "11q25"
module: 2
arm: "+"
pooled_cpm: 6.95
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ACAD8

*acyl-CoA dehydrogenase family member 8* — 11q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.28× (z +19.3, q 0e+00, up in 46 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H1573 0.153×, LS 180 0.105×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1573 0.304×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SHP-77 0.122×; ⚠ toxic; cell-cycle shift, explains ~12% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (SW480 0.239×).
> Its strongest partners by |cos| (64 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 38 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LZTR1]] (+0.53, fdr 3e-05), [[VPS26B]] (+0.52, fdr 9e-05, ⚠ same locus), [[UCKL1]] (+0.51, fdr 2e-04), [[ADCK5]] (+0.49, fdr 1e-04); moves opposite to [[DKK2]] (-0.56, fdr 5e-04), [[FER1L6]] (-0.47, fdr 0.003, ⚠ not reproduced), [[DNM3]] (-0.46, fdr 9e-04, ⚠ not reproduced), [[LINC02981]] (-0.45, fdr 9e-05), [[ZFPM2]] (-0.45, fdr 5e-04).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7529.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.28×** | +19.3 | 0e+00 | 46/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.82×** | +16.9 | 0e+00 | 45/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.63×** | +15.8 | 0e+00 | 44/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +9.3 | 3e-18 | 21/41 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +7.5 | 7e-12 | 13/23 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +7.4 | 1e-11 | 19/34 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +7.1 | 9e-11 | 24/47 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +6.7 | 1e-09 | 18/46 (NCI-H2347, C-33 A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +6.7 | 1e-09 | 17/45 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.46×** | +6.1 | 5e-08 | 16/47 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +5.8 | 3e-07 | 16/42 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.43×** | +5.8 | 3e-07 | 11/31 (NCI-H460, SW480, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.43×** | +5.6 | 1e-06 | 5/15 (NCI-H2030, KATO III, …) | all doses, flat | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.24×** | +4.9 | 5e-05 | 12/42 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.77×** | +4.8 | 5e-05 | 7/46 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.31×** | +4.4 | 4e-04 | 7/47 (SW480, NCI-H460, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.52×** | +3.6 | 0.010 | 0/40 | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.011 | 10/41 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.015 | 5/47 (A-172, HOP62, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.056 | 6/46 (A-172, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7529.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H1573 0.153×, LS 180 0.105×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1573 0.304×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SHP-77 0.122×; ⚠ toxic; cell-cycle shift, explains ~12% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (SW480 0.239×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.901× | -5.8 | 4e-06 | 11/48 (AsPC-1, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7529. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 9.63 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.304× (z -9.6) |
| [[SW480 (line)]] | alt | 11.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +9.9) | [[Thymol (drug)]] 0.5 µM 0.239× (z -9.1) |
| [[LS 180 (line)]] | wt | 6.74 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H460 (line)]] | wt | 5.14 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[PANC-1 (line)]] | alt | 9.20 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.85× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.122× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~12% of this change |
| [[A-172 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7529), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 20 of them with an alert (⚠; 18 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LZTR1]] | +0.53 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[VPS26B]] | +0.52 | +0.36 / +0.55 | both halves | 9e-05 | STRING 422; ⚠ same locus (5.8 kb, same strand: neighbours can correlate without regulation) |
| [[UCKL1]] | +0.51 | +0.37 / +0.30 | both halves | 2e-04 |  |
| [[CEP131]] | +0.50 | +0.16 / +0.58 | ⚠ one half (not replicated) | 0.001 |  |
| [[ADCK5]] | +0.49 | +0.42 / +0.33 | both halves | 1e-04 |  |
| [[TCIRG1]] | +0.48 | +0.26 / +0.28 | both halves | 4e-04 |  |
| [[EIF2B4]] | +0.48 | +0.36 / +0.40 | both halves | 9e-05 |  |
| [[TESK1]] | +0.47 | +0.37 / +0.22 | both halves | 6e-04 |  |
| [[STIMATE]] | +0.47 | +0.31 / +0.44 | both halves | 2e-04 |  |
| [[PLD2]] | +0.47 | +0.23 / +0.37 | both halves | 5e-04 |  |
| [[PPP5C]] | +0.46 | +0.28 / +0.50 | both halves | 3e-04 |  |
| [[SEMA4F]] | +0.45 | +0.26 / +0.38 | both halves | 3e-04 |  |
| [[BRF1]] | +0.45 | +0.28 / +0.38 | both halves | 3e-04 |  |
| [[SAAL1]] | +0.45 | +0.30 / +0.50 | both halves | 2e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 18 of them with an alert (⚠; 18 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DKK2]] | -0.56 | -0.23 / -0.49 | both halves | 5e-04 |  |
| [[FER1L6]] | -0.47 | -0.09 / -0.40 | ⚠ not reproduced | 0.003 |  |
| [[DNM3]] | -0.46 | -0.19 / -0.21 | ⚠ not reproduced | 9e-04 |  |
| [[GRM8]] | -0.45 | -0.11 / -0.31 | ⚠ not reproduced | 0.002 |  |
| [[LINC02981]] | -0.45 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[ZFPM2]] | -0.45 | -0.23 / -0.31 | both halves | 5e-04 |  |
| [[KCNIP4]] | -0.44 | -0.21 / -0.30 | both halves | 6e-04 |  |
| [[NAALADL2-AS2]] | -0.43 | -0.32 / -0.24 | both halves | 5e-04 |  |
| [[LRRC4C]] | -0.42 | -0.13 / -0.26 | ⚠ not reproduced | 0.002 |  |
| [[LINC03042]] | -0.42 | -0.23 / -0.26 | both halves | 5e-04 |  |
| [[SLC13A3]] | -0.41 | -0.04 / -0.27 | ⚠ not reproduced | 0.006 |  |
| [[LINC00534]] | -0.41 | -0.13 / -0.34 | ⚠ not reproduced | 0.002 |  |
| [[PCDH15]] | -0.41 | -0.23 / -0.29 | both halves | 5e-04 |  |
| [[LINC01186]] | -0.39 | -0.21 / -0.25 | both halves | 7e-04 |  |
| [[WWP2]] | -0.39 | -0.29 / -0.37 | both halves | 2e-04 |  |
| [[LINC00922]] | -0.39 | -0.28 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.453). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-9.3, -26.0); signed map (-37.0, -13.6). **Vector** length 46.6, 5.24% of its response variance represented; |z| ≥ 3 in 928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +2.1 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +1.7 | +5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +1.6 | +6.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.6 | +19.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.5 | +15.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.0 | +3.4 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +0.9 | +0.7 |
|  | [[Budesonide (drug)]] 5 µM |  | +0.9 | +2.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +0.8 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.7 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | +2.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA dehydrogenase family member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q25 — chr11:134,253,548-134,265,855 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Acyl-CoA dehydrogenase family; Flavoproteins |
| Reactome | 3 pathways, smallest: Branched-chain amino acid catabolism; Mitochondrial protein degradation; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKU7](https://www.uniprot.org/uniprotkb/Q9UKU7) (Isobutyryl-CoA dehydrogenase, mitochondrial):

> Isobutyryl-CoA dehydrogenase which catalyzes the conversion of 2-methylpropanoyl-CoA to (2E)-2-methylpropenoyl-CoA in the valine catabolic pathway. To a lesser extent, also able to catalyze the oxidation of (2S)-2-methylbutanoyl-CoA.

**Summary**, from NCBI Gene [27034](https://www.ncbi.nlm.nih.gov/gene/27034):

> This gene encodes a member of the acyl-CoA dehydrogenase family of enzymes that catalyze the dehydrogenation of acyl-CoA derivatives in the metabolism of fatty acids or branch chained amino acids. The encoded protein is a mitochondrial enzyme that functions in catabolism of the branched-chain amino acid valine. Defects in this gene are the cause of isobutyryl-CoA dehydrogenase deficiency.[provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:87](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:87) · Entrez [27034](https://www.ncbi.nlm.nih.gov/gene/27034) · UniProt [Q9UKU7](https://www.uniprot.org/uniprotkb/Q9UKU7) · Ensembl [ENSG00000151498](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151498)

## Data

Gene col 7529: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7529); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7529, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7529]; `tensor/DDL_lfc|DDL_z.npy` [7529]; `embed/gene_vectors.npy` [7529]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7529 or target_col == 7529). Every well: [[ACAD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACAD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
