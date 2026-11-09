---
symbol: "POLE4"
type: "gene"
col: 3662
ensembl_id: "ENSG00000115350"
name: "DNA polymerase epsilon 4, accessory subunit"
location: "2p12"
module: 1
arm: "+"
pooled_cpm: 10.47
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# POLE4

*DNA polymerase epsilon 4, accessory subunit* — 2p12

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.38× (z +15.7, q 0e+00, up in 18 of 19 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SW480 5.97×, A498 5.60×, A-427 6.00×, PANC-1 3.56×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 4.49×, SW480 7.06×, A498 4.52×, HOP62 6.28×, …; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.271×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.204×; ⚠ cell-cycle shift, explains ~0% of this change); [[Thymopentin (drug)]] 5 µM in 1 line (SNU-423 0.0528×); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (BT-474 0.0804×); [[Clotrimazole (drug)]] 0.5 µM in 1 line (LS 180 0.0549×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC6A11]] (+0.48, fdr 1e-04), [[CXCL1]] (+0.47, fdr 1e-04), [[PTER]] (+0.47, fdr 3e-05); moves opposite to [[KDELR1]] (-0.42, fdr 9e-05), [[ST13]] (-0.41, fdr 2e-04), [[ZCCHC17]] (-0.40, fdr 2e-04).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3662.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SW480 5.97×, A498 5.60×, A-427 6.00×, PANC-1 3.56×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 4.49×, SW480 7.06×, A498 4.52×, HOP62 6.28×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.38×** | +15.7 | 0e+00 | 18/19 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.98×** | +15.2 | 0e+00 | 31/32 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.97×** | +8.1 | 1e-13 | 21/25 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.80×** | +6.5 | 1e-08 | 26/40 (C32, HS-578T, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.7 | 0.020 | 24/40 (NCI-H2347, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | 1.94× | +3.3 | 0.10 | 4/36 (NCI-H460, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.5 µM |  | 1.33× | +3.2 | 0.10 | 8/46 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.33× | +3.1 | 0.10 | 14/46 (C32, A498, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | 1.34× | +3.1 | 0.10 | 16/39 (RPMI-7951, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3662.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.271×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.204×; ⚠ cell-cycle shift, explains ~0% of this change); [[Thymopentin (drug)]] 5 µM in 1 line (SNU-423 0.0528×); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (BT-474 0.0804×); [[Clotrimazole (drug)]] 0.5 µM in 1 line (LS 180 0.0549×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.708× | -3.6 | 0.19 | 14/43 (A-172, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | 0.738× | -3.3 | 0.24 | 17/42 (A-427, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3662. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 19.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +11.0) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 0.5 µM 0.241× (z -8.7) |
| [[A498 (line)]] | wt | 17.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +11.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 10.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.44× (z +8.6) ⚠ toxic; transcription drop | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.138× (z -8.9) |
| [[HOP62 (line)]] | alt | 7.82 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.50× (z +9.2) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 17.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +12.4) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 9.72 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.06× (z +11.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 11.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.65× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 8.46 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0896× (z -10.1) ⚠ toxic |
| [[BT-474 (line)]] | alt | 7.66 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0804× (z -9.2) |
| [[LS 180 (line)]] | wt | 2.95 | 0 | 1 | — | [[Clotrimazole (drug)]] 0.5 µM 0.0549× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 12.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.61× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 6.98 | 0 | 1 | — | [[Thymopentin (drug)]] 5 µM 0.0528× (z -10.4) |
| [[SW 900 (line)]] | alt | 8.66 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.01× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3662), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC6A11]] | +0.48 | +0.35 / +0.36 | both halves | 1e-04 |  |
| [[CXCL1]] | +0.47 | +0.36 / +0.47 | both halves | 1e-04 |  |
| [[PTER]] | +0.47 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[EXOC6]] | +0.47 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[GCFC2]] | +0.46 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[ISOC1]] | +0.45 | +0.37 / +0.44 | both halves | 7e-05 |  |
| [[UQCC2]] | +0.45 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[ZNF280C]] | +0.45 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[NBEAP2]] | +0.45 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[CACHD1]] | +0.44 | +0.34 / +0.41 | both halves | 1e-04 |  |
| [[SF3B3]] | +0.44 | +0.49 / +0.35 | both halves | 1e-04 | STRING 543 |
| [[CLDN1]] | +0.43 | +0.36 / +0.41 | both halves | 9e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDELR1]] | -0.42 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[ST13]] | -0.41 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[ZCCHC17]] | -0.40 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[XAB2]] | -0.39 | -0.37 / -0.25 | both halves | 4e-04 | pathway: Dual incision in TC-NER |
| [[GDAP2]] | -0.39 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[CRAT]] | -0.39 | -0.36 / -0.28 | both halves | 3e-04 |  |
| [[GTF2F1]] | -0.39 | -0.27 / -0.36 | both halves | 3e-04 | pathway: HALLMARK_DNA_REPAIR |
| [[ZFAND2A]] | -0.38 | -0.33 / -0.31 | both halves | 2e-04 |  |
| [[MACO1]] | -0.38 | -0.45 / -0.26 | both halves | 4e-04 |  |
| [[ISY1]] | -0.37 | -0.42 / -0.27 | both halves | 3e-04 | pathway: Dual incision in TC-NER; STRING 446 |
| [[MTCH1]] | -0.37 | -0.47 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.300). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-11.9, 1.2); signed map (13.8, -47.9). **Vector** length 44.0, 6.03% of its response variance represented; |z| ≥ 3 in 644 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +15.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +15.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | +2.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.0 | +0.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -2.4 | -3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | -1.8 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | +0.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.5 | -1.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.0 | -0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.8 | -2.6 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -0.7 | -2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -0.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase epsilon 4, accessory subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p12 — chr2:74,958,643-74,970,128 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p12 |
| Gene groups (HGNC) | DNA polymerases |
| Hallmark sets | DNA_REPAIR, E2F_TARGETS |
| Reactome | 30 pathways, smallest: DNA replication initiation; PCNA-Dependent Long Patch Base Excision Repair; Gap-filling DNA repair synthesis and ligation in GG-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR33](https://www.uniprot.org/uniprotkb/Q9NR33) (DNA polymerase epsilon subunit 4):

> Accessory component of the DNA polymerase epsilon complex. Participates in DNA repair and in chromosomal DNA replication (By similarity).

**Summary**, from NCBI Gene [56655](https://www.ncbi.nlm.nih.gov/gene/56655):

> POLE4 is a histone-fold protein that interacts with other histone-fold proteins to bind DNA in a sequence-independent manner. These histone-fold protein dimers combine within larger enzymatic complexes for DNA transcription, replication, and packaging.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:18755](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18755) · Entrez [56655](https://www.ncbi.nlm.nih.gov/gene/56655) · UniProt [Q9NR33](https://www.uniprot.org/uniprotkb/Q9NR33) · Ensembl [ENSG00000115350](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115350)

## Data

Gene col 3662: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3662); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3662, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3662]; `tensor/DDL_lfc|DDL_z.npy` [3662]; `embed/gene_vectors.npy` [3662]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3662 or target_col == 3662). Every well: [[POLE4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLE4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
