---
symbol: "FAM136A"
type: "gene"
col: 427
ensembl_id: "ENSG00000035141"
name: "TIM double twin CX3C motif chaperone"
location: "2p13.3"
module: 18
arm: "+"
pooled_cpm: 29.68
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# FAM136A

*TIM double twin CX3C motif chaperone* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.10× (z +19.8, q 0e+00, up in 43 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.46× (z +5.4, q 1e-05, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.468× (z -15.0, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HDDC2]] (+0.68, fdr 1e-05), [[NAA50]] (+0.68, fdr 7e-06), [[NAE1]] (+0.67, fdr 7e-06); moves opposite to [[MTHFR]] (-0.62, fdr 7e-06), [[ANKRD12]] (-0.57, fdr 1e-05), [[ACAP1]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 427.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.10×** | +19.8 | 0e+00 | 43/43 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.01×** | +17.5 | 0e+00 | 39/39 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.49×** | +11.9 | 3e-30 | 39/41 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +5.4 | 1e-05 | 31/47 (A-427, C-33 A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +5.3 | 2e-05 | 26/45 (NCI-H2030, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +4.9 | 8e-05 | 27/48 (SW480, A549, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.8 | 1e-04 | 27/47 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +4.6 | 4e-04 | 26/48 (A549, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.34×** | +4.1 | 0.002 | 27/46 (HT-29, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.74×** | +4.1 | 0.002 | 20/48 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.20× | +3.6 | 0.016 | 16/48 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.030 | 19/48 (LoVo, SW480, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | 1.36× | +3.0 | 0.10 | 12/47 (AsPC-1, Hs 766T, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 427.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.468×** | -15.0 | 0e+00 | 41/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.498×** | -9.8 | 4e-20 | 40/47 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.516×** | -9.3 | 4e-18 | 38/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.551×** | -8.3 | 1e-14 | 41/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.615×** | -6.8 | 1e-09 | 37/48 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.671×** | -5.6 | 2e-06 | 32/47 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.546×** | -4.4 | 8e-04 | 28/48 (SW48, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.608×** | -3.6 | 0.019 | 21/46 (SW48, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.772×** | -3.4 | 0.038 | 16/48 (LoVo, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.644×** | -3.2 | 0.075 | 16/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | 0.853× | -3.1 | 0.092 | 12/48 (HS-578T, NCI-H661, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 427. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 49.3 | 3 (3 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +13.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -14.8) |
| [[SW480 (line)]] | alt | 48.1 | 3 (3 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 7.19× (z +17.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.258× (z -13.6) |
| [[LoVo (line)]] | wt | 35.6 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 6.59× (z +16.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -12.4) |
| [[KATO III (line)]] | alt | 34.4 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 6.32× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 47.6 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +10.0) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.217× (z -12.5) |
| [[PANC-1 (line)]] | alt | 27.4 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +13.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -9.9) |
| [[HT-29 (line)]] | alt | 23.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -9.6) |
| [[LS 180 (line)]] | wt | 42.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +14.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.318× (z -9.9) |
| [[A-427 (line)]] | wt | 51.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.96× (z +14.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -13.8) |
| [[A549 (line)]] | wt | 29.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.48× (z +13.4) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 19.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.54× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.8) |
| [[J82 (line)]] | alt | 19.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 22.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.28× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 19.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -18.8) |
| [[NCI-H460 (line)]] | wt | 24.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.96× (z +13.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -16.1) |
| [[RKO (line)]] | wt | 35.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -14.7) |
| [[A-172 (line)]] | wt | 25.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 31.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +11.0) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 19.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0760× (z -11.9) |
| [[HCT15 (line)]] | alt | 39.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 25.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.40× (z +13.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 39.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -14.8) |
| [[SHP-77 (line)]] | alt | 30.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.35× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 22.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -12.7) |
| [[SNU-423 (line)]] | alt | 20.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.13× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 44.8 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.199× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 28.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -9.6) |
| [[C32 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.190× (z -8.5) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 35.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +9.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 20.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 20.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -14.3) |
| [[NCI-H2347 (line)]] | alt | 22.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 30.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.71× (z +14.2) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 19.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -9.9) |
| [[SNU-1 (line)]] | wt | 28.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -12.2) |
| [[AN3 CA (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 427), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDDC2]] | +0.68 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[NAA50]] | +0.68 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[NAE1]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ZC3HAV1L]] | +0.66 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[DPY19L4]] | +0.63 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[ATIC]] | +0.63 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[WDR12]] | +0.61 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[MRPS35]] | +0.61 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[GOT2]] | +0.61 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[UHMK1]] | +0.61 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[METTL3]] | +0.60 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[DTD2]] | +0.60 | +0.57 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTHFR]] | -0.62 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[ANKRD12]] | -0.57 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ACAP1]] | -0.55 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[KLF2]] | -0.54 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[ZNF324]] | -0.54 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[GABARAPL2]] | -0.54 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[SHOC2]] | -0.53 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[ING1]] | -0.53 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[KLHL4]] | -0.53 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[PMM1]] | -0.53 | -0.43 / -0.48 | both halves | 4e-05 |  |
| [[MARCHF9]] | -0.53 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[CDKN2D]] | -0.53 | -0.37 / -0.53 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises FAM136A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.582). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-24.2, -29.5); signed map (-13.0, -41.9). **Vector** length 79.9, 19.2% of its response variance represented; |z| ≥ 3 in 892 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.6 | +4.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +2.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +17.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +1.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.0 | +2.9 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +2.0 | -0.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | -15.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.6 | -3.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.2 | -5.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.9 | +0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.9 | -6.8 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -1.7 | -1.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.7 | +0.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.6 | +2.1 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | -1.6 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | TIM double twin CX3C motif chaperone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:70,295,976-70,302,067 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14668; previously FAM136A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96C01](https://www.uniprot.org/uniprotkb/Q96C01) (TIM double twin CX3C motif protein):

> Plays a role in proteostasis of the mitochondrion intermembrane space and counteracts aggregation of certain proteins. Required for mitochondrial oxidative phosphorylation.

**Summary**, from NCBI Gene [84908](https://www.ncbi.nlm.nih.gov/gene/84908):

> This gene encodes a mitochondrially localized protein that is highly conserved across species. The gene is expressed in a variety of tissues including human lymphoblast cells and rat neurosensorial epithelium of the cristaampullaris. A mutation in this gene has been associated with familial Meniere's disease, a chronic disorder of the inner ear. Several pseudogenes of this gene are found on other chromosomes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug …

**Accessions** — [HGNC:25911](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25911) · Entrez [84908](https://www.ncbi.nlm.nih.gov/gene/84908) · UniProt [Q96C01](https://www.uniprot.org/uniprotkb/Q96C01) · Ensembl [ENSG00000035141](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000035141)

## Data

Gene col 427: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 427); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 427, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 427]; `tensor/DDL_lfc|DDL_z.npy` [427]; `embed/gene_vectors.npy` [427]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 427 or target_col == 427). Every well: [[FAM136A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM136A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
