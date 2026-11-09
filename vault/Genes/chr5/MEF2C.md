---
symbol: "MEF2C"
type: "gene"
col: 1313
ensembl_id: "ENSG00000081189"
name: "myocyte enhancer factor 2C"
location: "5q14.3"
module: 152
arm: "+"
pooled_cpm: 40.78
n_lines_expressing: 36
n_dd_up: 34
n_dd_down: 30
n_dd_up_clean: 30
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 10
direction_downstream: 11
tags: ["gene", "module/152", "written"]
generated_by: "tahoemap"
---

# MEF2C

*myocyte enhancer factor 2C* — 5q14.3

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> MEF2C is a MADS-box transcription factor that licenses the muscle, cardiac and neuronal differentiation programmes, acting as an amplifier of lineage master regulators rather than as a master regulator itself.

## What it is

MEF2C is one of four vertebrate MEF2 proteins ([[MEF2A]], [[MEF2B]], MEF2C, [[MEF2D]]). All share an N-terminal MADS box and adjacent MEF2 domain, which handle DNA binding at an A/T-rich consensus, dimerisation and cofactor contact; the C-terminal half carries transactivation and most regulatory sequence.

MEF2C is not a determination factor on its own — it cannot convert a fibroblast into a myoblast the way MYOD1 can. Its characteristic behaviour is combinatorial: it binds adjacent to myogenic bHLH factors and the pair activate transcription far beyond additivity, through a direct MADS-to-bHLH contact. Because MEF2 sites sit in the promoters of the myogenic regulatory factors and beside E-boxes in muscle structural genes, MEF2C and MyoD form a feed-forward loop that locks the differentiated state in.

Its regulation is largely post-transcriptional, which matters for anyone inferring activity from mRNA. Class IIa histone deacetylases — HDAC4, [[HDAC5]], HDAC7, HDAC9 — bind the MADS/MEF2 surface and hold MEF2 silent; calcium-dependent kinase signalling phosphorylates them, exports them from the nucleus, and frees MEF2 to recruit p300/CBP. p38 MAPK, ERK5 and calcineurin feed into the same switch.

Among the paralogues MEF2C has the most severe loss-of-function phenotype: null embryos fail heart-tube looping and never form a right ventricle. In humans, MEF2C haploinsufficiency from 5q14.3 deletion or point mutation causes severe intellectual disability with epilepsy and absent speech. In cancer, high MEF2C marks an immature subtype of T-cell acute lymphoblastic leukaemia, arising from rearrangement of MEF2C itself or of factors upstream of it.

## What is uncertain

Which MEF2 paralogue acts at the TRIM72 promoter is unsettled: the reporter work established a functional MEF2 site, not which of the four occupies it in a cell. MEF2C's transcript is also a poor proxy for its activity, since HDAC gating is the real switch — and unlike the myogenic bHLH factors MEF2C is expressed in this panel, so its presence is only weak evidence that the protein is doing anything. MEF2C regulons are drawn from muscle, heart, neuronal and immune contexts and overlap generic stress programmes, so an activity score here can track what those targets do for other reasons. Nothing perturbs MEF2C in this dataset in any case, so direction was never available.

## References

- Molkentin et al., 1995, Cell — showed cooperative, more-than-additive activation of muscle genes by MEF2 and myogenic bHLH factors through a direct MADS–bHLH contact.
- Lin et al., 1997, Science — Mef2c-null mouse embryos fail cardiac looping and do not form a right ventricle.
- McKinsey et al., 2000, Nature — signal-dependent nuclear export of a class II histone deacetylase releases MEF2 and permits muscle differentiation.
- Potthoff and Olson, 2007, Development — review of MEF2 as a combinatorial regulator across developmental programmes.
- Jung and Ko, 2010, Biochemical and Biophysical Research Communications — the TRIM72 promoter has a conserved MEF2 site next to an E-box, and MyoD (or myogenin) plus MEF2 activate it synergistically.
- Homminga et al., 2011, Cancer Cell — high MEF2C expression defines an immature T-ALL subtype, activated by rearrangement of MEF2C or of its upstream regulators.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.68× (z +12.1, q 9e-31, up in 30 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.504× (z -11.3, q 8e-27, down in 24 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB30]] (+0.64, fdr 7e-06), [[SNAP25]] (+0.60, fdr 1e-05), [[EPHA3]] (+0.59, fdr 1e-05); moves opposite to [[TPD52L2]] (-0.59, fdr 7e-06), [[PPP2R2C]] (-0.53, fdr 2e-05), [[DOCK9]] (-0.50, fdr 3e-05).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ANGPT1]] → it (grade B ⚠); 11 go from it, the strongest it → [[MIR181A1HG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 6 with an alert ⚠; shown: the 15 strongest. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1313.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +12.1 | 9e-31 | 30/34 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +8.8 | 3e-16 | 26/34 (HOP62, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +8.8 | 3e-16 | 20/34 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.33×** | +7.2 | 8e-11 | 22/34 (A498, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +6.8 | 1e-09 | 17/34 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +6.7 | 3e-09 | 21/34 (HOP62, SW 900, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +6.2 | 5e-08 | 23/33 (LoVo, C32, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.45×** | +6.1 | 6e-08 | 20/34 (SK-MEL-2, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +6.1 | 6e-08 | 17/34 (LoVo, C32, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.35×** | +5.9 | 2e-07 | 18/34 (C32, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +5.8 | 4e-07 | 15/34 (LS 180, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +5.7 | 6e-07 | 19/33 (LoVo, C32, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +5.7 | 6e-07 | 12/33 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +5.6 | 8e-07 | 17/34 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.42×** | +5.4 | 3e-06 | 19/34 (LoVo, C32, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1313.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.504×** | -11.3 | 8e-27 | 24/34 (C32, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.515×** | -10.9 | 2e-25 | 24/34 (C32, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.531×** | -10.5 | 3e-23 | 29/33 (C32, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.539×** | -9.6 | 8e-20 | 23/34 (C32, A-427, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.666×** | -9.5 | 3e-19 | 23/34 (SK-MEL-2, C32, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.575×** | -9.1 | 7e-18 | 25/34 (RPMI-7951, C32, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.600×** | -8.1 | 4e-14 | 26/33 (RPMI-7951, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.619×** | -7.9 | 2e-13 | 24/33 (A-427, NCI-H460, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.630×** | -7.6 | 2e-12 | 22/33 (SK-MEL-2, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.635×** | -7.5 | 4e-12 | 23/33 (NCI-H1792, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.665×** | -6.7 | 9e-10 | 22/33 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.566×** | -6.7 | 1e-09 | 21/34 (RPMI-7951, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.502×** | -5.9 | 2e-07 | 19/32 (H4, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.705×** | -5.5 | 1e-06 | 21/34 (Hs 766T, NCI-H1792, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.789×** | -5.5 | 1e-06 | 17/34 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.839× | -4.1 | 0.001 | 9/34 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **0.780×** | -4.1 | 0.001 | 15/33 (hTERT-HPNE, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1313. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 99.0 | 11 (6 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 4.98× (z +15.2) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.0) | [[Auranofin (drug)]] 5 µM 0.306× (z -11.6) |
| [[C32 (line)]] | wt | 205 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -16.6) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.193× (z -13.4) |
| [[PANC-1 (line)]] | alt | 66.0 | 0 | 5 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.393× (z -10.7) |
| [[A498 (line)]] | wt | 33.0 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.15× (z +10.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.85× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 19.4 | 4 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.01× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 184 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -14.4) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.253× (z -11.4) |
| [[LS 180 (line)]] | wt | 49.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +12.8) | — |
| [[RPMI-7951 (line)]] | alt | 74.0 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.288× (z -9.8) |
| [[A-427 (line)]] | wt | 91.2 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.293× (z -9.5) |
| [[H4 (line)]] | wt | 44.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 49.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 70.0 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.385× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 21.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 6.20× (z +15.6) | — |
| [[SHP-77 (line)]] | alt | 105 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.370× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 17.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.62× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 92.7 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.438× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 70.3 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.349× (z -10.9) |
| [[A-172 (line)]] | wt | 9.15 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.91 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 76.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.86 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 272 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.72 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.09 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.23 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.56 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1313), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB30]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[SNAP25]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[EPHA3]] | +0.59 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[PER2]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 | pathway: Circadian clock |
| [[PRICKLE1]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[NREP]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[PCDH7]] | +0.58 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[CXXC4]] | +0.57 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[ZNF608]] | +0.57 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[MEF2C-AS1]] | +0.57 | +0.57 / +0.57 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[NCAM2]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[LRRC7]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[SOX2]] | +0.55 | +0.45 / +0.52 | both halves | 3e-05 | pathway: Transcriptional Regulation by MECP2; STRING 626 |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPD52L2]] | -0.59 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[PPP2R2C]] | -0.53 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[DOCK9]] | -0.50 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[POC1B]] | -0.49 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[ADCY7]] | -0.48 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[MROH1]] | -0.48 | -0.32 / -0.55 | both halves | 1e-04 |  |
| [[ZNF731P]] | -0.48 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[MICALL1]] | -0.47 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[ZNF710]] | -0.46 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANGPT1]] | B | ANGPT1 activity raises MEF2C's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 4.43× lower at baseline in the lines without ANGPT1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5 |
| [[PCDH18]] | B | PCDH18 activity raises MEF2C's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 4.17× lower at baseline in the lines without PCDH18 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677 |
| [[BCHE]] | B | BCHE activity raises MEF2C's level | lines that do not express BCHE (35) vs lines expressing it (15) | 3.66× lower at baseline in the lines without BCHE | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2 |
| [[LRRC7]] | B | LRRC7 activity raises MEF2C's level | lines that do not express LRRC7 (15) vs lines expressing it (35) | 2.76× lower at baseline in the lines without LRRC7 | 0.027 | ⚠ within organs, on part of the lines; also absent: RNF150, MAP2, KCTD16; maybe low, not absent |
| [[PCDH18]] | B | PCDH18 activity strengthens MEF2C's drug response | lines that do not express PCDH18 (21) vs lines expressing it (13) | the lines without PCDH18 respond 0.91× as strongly (z diff +1.15); strongest at Auranofin 5 µM: 0.56x vs 0.41x (z diff +3.8) | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677; target measured in part of the lines; artifact flags |
| [[LRIG3]] | B | LRIG3 activity raises MEF2C's level | lines that do not express LRIG3 (6) vs lines expressing it (44) | 3.36× lower at baseline in the lines without LRIG3 | 0.050 | ⚠ within organs, on part of the lines; also absent: LRIG3-DT, CPEB2, FZD1 |
| [[PTPN13]] | B | PTPN13 activity raises MEF2C's level | lines that do not express PTPN13 (10) vs lines expressing it (40) | 3.57× lower at baseline in the lines without PTPN13 | 0.051 | ⚠ within organs, on part of the lines; also absent: MAPK10, AGPAT4, ENSG00000236230 |
| [[SMIM10]] | B | SMIM10 activity raises MEF2C's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 3.06× lower at baseline in the lines without SMIM10 | 0.071 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[NR2F1]] | B | NR2F1 activity raises MEF2C's level | lines that do not express NR2F1 (8) vs lines expressing it (42) | 3.77× lower at baseline in the lines without NR2F1 | 0.077 | ⚠ within organs, on part of the lines; also absent: NR2F1-AS1, PCDH15; maybe low, not absent |
| [[MEF2C-AS1]] | C | MEF2C-AS1 activity raises MEF2C's level | lines that do not express MEF2C-AS1 (16) vs lines expressing it (34) | 6.61× lower at baseline in the lines without MEF2C-AS1 | 1e-03 | ⚠ within organs, on part of the lines; also absent: MEF2C, RGS2, ADGRL4; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR181A1HG]] | B | MEF2C activity raises MIR181A1HG's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 2.60× lower at baseline in the lines without MEF2C | 0.013 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID |
| [[ARHGAP24]] | B | MEF2C activity raises ARHGAP24's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 3.28× lower at baseline in the lines without MEF2C | 0.018 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID |
| [[AHR]] | B | MEF2C activity raises AHR's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 2.22× lower at baseline in the lines without MEF2C | 0.035 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID |
| [[PCDH7]] | B | MEF2C activity raises PCDH7's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 3.17× lower at baseline in the lines without MEF2C | 0.045 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID |
| [[ANGPT1]] | B | MEF2C activity raises ANGPT1's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 3.09× lower at baseline in the lines without MEF2C | 0.052 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID |
| [[SPTLC3]] | B | MEF2C activity raises SPTLC3's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 1.41× lower at baseline in the lines without MEF2C | 0.056 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID |
| [[ZNF608]] | B | MEF2C activity raises ZNF608's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 1.24× lower at baseline in the lines without MEF2C | 0.083 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID |
| [[EYA1]] | B | MEF2C activity raises EYA1's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 3.48× lower at baseline in the lines without MEF2C | 0.084 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID |
| [[S100A4]] | B | MEF2C activity lowers S100A4's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 2.30× higher at baseline in the lines without MEF2C | 0.091 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID |
| [[SMIM10]] | B | MEF2C activity raises SMIM10's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 1.80× lower at baseline in the lines without MEF2C | 0.094 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID |
| [[MEF2C-AS1]] | C | MEF2C activity raises MEF2C-AS1's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 5.34× lower at baseline in the lines without MEF2C | 0.002 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.1, 32.1); signed map (37.4, 38.3). **Vector** length 110, 29.1% of its response variance represented; |z| ≥ 3 in 1,171 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +12.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.4 | -0.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | -1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +6.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +5.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +5.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.0 | +6.1 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -5.3 | -7.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.9 | -9.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.9 | -9.5 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -4.6 | -7.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.5 | -7.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.4 | -8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -11.3 |

## What is on record

|  |  |
|---|---|
| Name | myocyte enhancer factor 2C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.3 — chr5:88,717,117-88,904,257 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Myocyte enhancer factor 2 proteins; MADS box family |
| Hallmark sets | MYOGENESIS |
| Reactome | 40 pathways, smallest: MECP2 regulates transcription factors; Cardiogenesis; ERK/MAPK targets |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06413](https://www.uniprot.org/uniprotkb/Q06413) (Myocyte-specific enhancer factor 2C):

> Transcription activator which binds specifically to the MEF2 element present in the regulatory regions of many muscle-specific genes. Controls cardiac morphogenesis and myogenesis, and is also involved in vascular development. Enhances transcriptional activation mediated by SOX18. Plays an essential role in hippocampal-dependent learning and memory by suppressing the number of excitatory synapses and thus regulating basal and evoked synaptic transmission. Crucial for normal neuronal …

**Summary**, from NCBI Gene [4208](https://www.ncbi.nlm.nih.gov/gene/4208):

> This locus encodes a member of the MADS box transcription enhancer factor 2 (MEF2) family of proteins, which play a role in myogenesis. The encoded protein, MEF2 polypeptide C, has both trans-activating and DNA binding activities. This protein may play a role in maintaining the differentiated state of muscle cells. Mutations and deletions at this locus have been associated with severe cognitive disability, stereotypic movements, epilepsy, and cerebral malformation. Alternatively spliced …

**Accessions** — [HGNC:6996](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6996) · Entrez [4208](https://www.ncbi.nlm.nih.gov/gene/4208) · UniProt [Q06413](https://www.uniprot.org/uniprotkb/Q06413) · Ensembl [ENSG00000081189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081189)

## Data

Gene col 1313: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1313); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1313, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1313]; `tensor/DDL_lfc|DDL_z.npy` [1313]; `embed/gene_vectors.npy` [1313]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1313 or target_col == 1313). Every well: [[MEF2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/MEF2C.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
