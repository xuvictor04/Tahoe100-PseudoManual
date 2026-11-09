---
symbol: "SNRPG"
type: "gene"
col: 6830
ensembl_id: "ENSG00000143977"
name: "small nuclear ribonucleoprotein polypeptide G"
location: "2p13.3"
module: 29
arm: "+"
pooled_cpm: 22.07
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# SNRPG

*small nuclear ribonucleoprotein polypeptide G* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.93× (z +16.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM: 0.772× (z -3.9, q 0.049, down in 14 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHX15]] (+0.60, fdr 1e-05), [[HAT1]] (+0.59, fdr 1e-05), [[NUDT15]] (+0.59, fdr 2e-05); moves opposite to [[NPIPP1]] (-0.59, fdr 1e-05), [[OSGIN1]] (-0.56, fdr 1e-05), [[GOLGB1]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6830.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.93×** | +16.6 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **6.55×** | +15.2 | 0e+00 | 48/48 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.44×** | +13.9 | 2e-41 | 42/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.34×** | +11.9 | 1e-30 | 40/45 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.96×** | +10.5 | 1e-23 | 39/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +10.1 | 6e-22 | 38/45 (RKO, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.87×** | +9.7 | 2e-20 | 36/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.66×** | +7.6 | 2e-12 | 31/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.41×** | +7.5 | 6e-12 | 25/47 (NCI-H460, A549, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.67×** | +7.4 | 1e-11 | 23/38 (SW480, PANC-1, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.61×** | +7.3 | 1e-11 | 27/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | **1.43×** | +5.5 | 1e-06 | 22/42 (A-172, AsPC-1, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.5 | 2e-06 | 24/47 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.40×** | +5.2 | 6e-06 | 24/48 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | **1.38×** | +4.8 | 8e-05 | 15/33 (Hs 766T, HT-29, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +4.6 | 2e-04 | 19/47 (RPMI-7951, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.008 | 16/47 (A-172, NCI-H2347, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.024 | 10/47 (KATO III, LS 180, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 1.16× | +3.2 | 0.028 | 5/48 (RKO, NCI-H661, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.028 | 11/48 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.044 | 9/48 (PANC-1, A498, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.21×** | +2.9 | 0.065 | 5/48 (NCI-H460, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +2.9 | 0.065 | 13/47 (LOX-IMVI, SW48, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6830.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.772×** | -3.9 | 0.049 | 14/47 (AsPC-1, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.785×** | -3.8 | 0.049 | 12/48 (HS-578T, RPMI-7951, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | **0.792×** | -3.6 | 0.053 | 7/48 (C-33 A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.855× | -3.3 | 0.11 | 9/48 (CHP-212, NCI-H1792, …) | all doses, flat |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.809× | -3.3 | 0.11 | 10/48 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.819× | -3.1 | 0.14 | 9/48 (SW 1088, AsPC-1, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.868× | -3.1 | 0.14 | 12/48 (NCI-H2347, hTERT-HPNE, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.823× | -3.0 | 0.14 | 5/47 (RPMI-7951, NCI-H2347, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.859× | -3.0 | 0.14 | 7/48 (RPMI-7951, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.872× | -3.0 | 0.14 | 9/48 (SHP-77, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6830. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.2 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +12.4) | — |
| [[NCI-H460 (line)]] | wt | 22.5 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.28× (z +12.2) | — |
| [[PANC-1 (line)]] | alt | 22.9 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.56× (z +15.5) | — |
| [[AsPC-1 (line)]] | alt | 25.7 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.17× (z +11.2) | — |
| [[LoVo (line)]] | wt | 17.8 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.01× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 19.1 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.79× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 17.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.59× (z +12.1) | — |
| [[BT-474 (line)]] | alt | 15.9 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.191× (z -8.6) |
| [[CHP-212 (line)]] | wt | 20.0 | 0 | 1 | — | [[Cabozantinib (S-malate) (drug)]] 0.5 µM 0.0587× (z -8.8) |
| [[H4 (line)]] | wt | 17.9 | 0 | 1 | — | [[Darinaparsin (drug)]] 0.05 µM 0.127× (z -9.4) |
| [[HCT15 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Artesunate (drug)]] 5 µM 0.178× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 17.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.01× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0794× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 20.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.49× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 36.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[RKO (line)]] | wt | 31.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.15× (z +9.9) ⚠ toxic | — |
| [[SHP-77 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.113× (z -10.3) ⚠ toxic |
| [[A-172 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6830), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX15]] | +0.60 | +0.57 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 991 |
| [[HAT1]] | +0.59 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[NUDT15]] | +0.59 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[ZNF410]] | +0.57 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[NUDT21]] | +0.57 | +0.58 / +0.60 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 569 |
| [[ALG6]] | +0.57 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[NDC1]] | +0.57 | +0.64 / +0.51 | both halves | 1e-05 | pathway: Metabolism of non-coding RNA; STRING 443 |
| [[SNRNP40]] | +0.57 | +0.57 / +0.58 | both halves | 9e-06 | pathway: Dengue Virus-Host Interactions; STRING 991 |
| [[CPSF6]] | +0.57 | +0.46 / +0.60 | both halves | 2e-05 | pathway: Dengue Virus-Host Interactions; STRING 513 |
| [[POLE2]] | +0.55 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[NDUFS6]] | +0.55 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[TMEM248]] | +0.55 | +0.57 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPIPP1]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[OSGIN1]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[GOLGB1]] | -0.56 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[ATF4]] | -0.56 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[DNAJB2]] | -0.55 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[UBXN4]] | -0.51 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[NBPF10]] | -0.51 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[PRRC2C]] | -0.51 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[KTN1]] | -0.50 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[EIF4EBP3]] | -0.50 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[USP27X]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[UBC]] | -0.50 | -0.35 / -0.54 | both halves | 1e-04 | pathway: Processing of Capped Intron-Containing Pre-mRNA |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.424). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-36.1, -39.6); signed map (-43.5, -24.2). **Vector** length 58.8, 10.3% of its response variance represented; |z| ≥ 3 in 974 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.5 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +3.6 | +7.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.5 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | +3.4 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | +2.9 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +11.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.1 | +2.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.1 | +0.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +0.9 | -0.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -3.6 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | +5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | +1.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.9 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | +1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | +1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein polypeptide G |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:70,281,362-70,293,740 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Sm-G |
| Gene groups (HGNC) | Sm spliceosomal proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 24 pathways, smallest: SLBP independent Processing of Histone Pre-mRNAs; SLBP Dependent Processing of Replication-Dependent Histone Pre-mRNAs; Processing of Capped Intronless Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P62308](https://www.uniprot.org/uniprotkb/P62308) (Small nuclear ribonucleoprotein G):

> Plays a role in pre-mRNA splicing as a core component of the spliceosomal U1, U2, U4 and U5 small nuclear ribonucleoproteins (snRNPs), the building blocks of the spliceosome. Component of both the pre-catalytic spliceosome B complex and activated spliceosome C complexes. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs. As part of the U7 snRNP it is involved in histone 3'-end processing.

**Summary**, from NCBI Gene [6637](https://www.ncbi.nlm.nih.gov/gene/6637):

> The protein encoded by this gene is a component of the U1, U2, U4, and U5 small nuclear ribonucleoprotein complexes, precursors of the spliceosome. The encoded protein may also be a part of the U7 small nuclear ribonucleoprotein complex, which participates in the processing of the 3' end of histone transcripts. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:11163](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11163) · Entrez [6637](https://www.ncbi.nlm.nih.gov/gene/6637) · UniProt [P62308](https://www.uniprot.org/uniprotkb/P62308) · Ensembl [ENSG00000143977](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143977)

## Data

Gene col 6830: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6830); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6830, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6830]; `tensor/DDL_lfc|DDL_z.npy` [6830]; `embed/gene_vectors.npy` [6830]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6830 or target_col == 6830). Every well: [[SNRPG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRPG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
