---
symbol: "PGAM5"
type: "gene"
col: 14478
ensembl_id: "ENSG00000247077"
name: "PGAM family member 5, mitochondrial serine/threonine protein phosphatase"
location: "12q24.33"
module: 4
arm: "+"
pooled_cpm: 9.89
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 3
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# PGAM5

*PGAM family member 5, mitochondrial serine/threonine protein phosphatase* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.07× (z +14.4, q 3e-44, up in 28 of 32 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.47× (z +11.6, q 7e-29, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Temsirolimus (drug)]] 0.5 µM: 0.729× (z -4.1, q 0.023, down in 13 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (A-427 0.242×, RKO 0.281×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.198×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.223×; ⚠ cell-cycle shift, explains ~0% of this change); [[Triclosan (drug)]] 0.05 µM in 1 line (SNU-1 0.0707×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LETM1]] (+0.77, fdr 7e-06), [[BOP1]] (+0.77, fdr 7e-06), [[MYBBP1A]] (+0.76, fdr 7e-06); moves opposite to [[ZNF821]] (-0.66, fdr 7e-06), [[B2M]] (-0.64, fdr 7e-06), [[MICU1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[WNK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 17 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14478.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **3.07×** | +14.4 | 3e-44 | 28/32 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.91×** | +13.2 | 3e-37 | 14/18 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.47×** | +11.6 | 7e-29 | 39/46 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.36×** | +9.5 | 3e-19 | 16/24 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.05×** | +9.2 | 4e-18 | 36/47 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **2.04×** | +8.8 | 1e-16 | 26/37 (LoVo, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.98×** | +8.4 | 3e-15 | 24/34 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.91×** | +8.3 | 8e-15 | 31/47 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.87×** | +8.0 | 7e-14 | 37/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.85×** | +7.9 | 2e-13 | 30/47 (HEC-1-A, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.76×** | +7.3 | 2e-11 | 28/43 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.64×** | +6.3 | 1e-08 | 21/36 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +6.0 | 8e-08 | 25/46 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.55×** | +5.6 | 8e-07 | 18/47 (PANC-1, A549, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.52×** | +5.2 | 8e-06 | 21/45 (SW480, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.44×** | +4.5 | 2e-04 | 19/46 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +4.4 | 4e-04 | 19/47 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.3 | 6e-04 | 16/43 (CFPAC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +4.2 | 7e-04 | 10/47 (A498, A-172, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.78×** | +3.9 | 0.003 | 4/40 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.75×** | +3.7 | 0.005 | 10/44 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.73×** | +3.7 | 0.006 | 10/37 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.007 | 12/42 (A549, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.009 | 9/46 (hTERT-HPNE, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.013 | 6/46 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.014 | 5/46 (NCI-H2030, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14478.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (A-427 0.242×, RKO 0.281×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.198×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.223×; ⚠ cell-cycle shift, explains ~0% of this change); [[Triclosan (drug)]] 0.05 µM in 1 line (SNU-1 0.0707×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.729×** | -4.1 | 0.023 | 13/42 (A-172, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.734×** | -3.9 | 0.030 | 13/47 (MIA PaCa-2, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.795×** | -3.5 | 0.096 | 10/46 (NCI-H23, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~94% of this change | 0.773× | -3.3 | 0.11 | 13/45 (A498, LoVo, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.774× | -3.2 | 0.14 | 13/45 (HepG2/C3A, SW480, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.792× | -3.2 | 0.14 | 9/47 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.629× | -3.1 | 0.14 | 7/47 (MIA PaCa-2, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14478. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 18.1 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.242× (z -12.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -10.3) |
| [[PANC-1 (line)]] | alt | 15.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.41× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SW480 (line)]] | alt | 11.9 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.12× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 11.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.86× (z +8.8) | — |
| [[LoVo (line)]] | wt | 12.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.33× (z +8.8) | — |
| [[RKO (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.281× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 8.51 | 0 | 1 | — | [[Triclosan (drug)]] 0.05 µM 0.0707× (z -8.6) |
| [[SW48 (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14478), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LETM1]] | +0.77 | +0.78 / +0.76 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport |
| [[BOP1]] | +0.77 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.76 | +0.81 / +0.66 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.75 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[ATAD3A]] | +0.75 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[URB2]] | +0.74 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[E2F4]] | +0.73 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[IFRD2]] | +0.73 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[HEATR3]] | +0.73 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[PINX1]] | +0.72 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[WDR77]] | +0.71 | +0.80 / +0.70 | both halves | 7e-06 | STRING 479 |
| [[TMEM33]] | +0.70 | +0.73 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF821]] | -0.66 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[B2M]] | -0.64 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[MICU1]] | -0.64 | -0.68 / -0.53 | both halves | 1e-05 |  |
| [[ATOSA]] | -0.64 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.63 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[HLA-A]] | -0.63 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.62 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[TERF2IP]] | -0.62 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[ZFYVE1]] | -0.62 | -0.66 / -0.57 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.62 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[TMEM59]] | -0.61 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[CERT1]] | -0.60 | -0.49 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNK2]] | B | WNK2 activity raises PGAM5's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.60× lower at baseline in the lines without WNK2 | 0.070 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[SPTBN2]] | B | SPTBN2 activity raises PGAM5's level | lines that do not express SPTBN2 (9) vs lines expressing it (41) | 1.51× lower at baseline in the lines without SPTBN2 | 0.0999 | ⚠ within organs, on part of the lines; also absent: CCDC88C, HID1, ASS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.749). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-12.5, -37.6); signed map (-5.7, -46.7). **Vector** length 69.0, 12.5% of its response variance represented; |z| ≥ 3 in 892 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing in the nucleus* (reactome, mean cos +0.52 to 8); *Folding of actin by CCT/TriC* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.9 | +11.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.6 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +3.1 | +14.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +2.9 | +13.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | +2.8 | +8.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.2 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +4.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +3.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.1 | -0.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~94% of this change | -2.1 | -3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.9 | -1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.6 | -2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | PGAM family member 5, mitochondrial serine/threonine protein phosphatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:132,710,819-132,722,734 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5352, BXLBv68 |
| Gene groups (HGNC) | Serine/threonine phosphatases; Phosphoglycerate mutases |
| Reactome | 8 pathways, smallest: Receptor Mediated Mitophagy; Regulation of pyruvate metabolism; Mitophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96HS1](https://www.uniprot.org/uniprotkb/Q96HS1) (Serine/threonine-protein phosphatase PGAM5, mitochondrial):

> Mitochondrial serine/threonine phosphatase that dephosphorylates various substrates and thus plays a role in different biological processes including cellular senescence or mitophagy. Modulates cellular senescence by regulating mitochondrial dynamics. Mechanistically, participates in mitochondrial fission through dephosphorylating DNM1L/DRP1. Additionally, dephosphorylates MFN2 in a stress-sensitive manner and consequently protects it from ubiquitination and degradation to promote mitochondrial …

**Summary**, from NCBI Gene [192111](https://www.ncbi.nlm.nih.gov/gene/192111):

> Enables protein serine/threonine phosphatase activity. Predicted to be involved in negative regulation of cold-induced thermogenesis and positive regulation of mitochondrial fission. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28763](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28763) · Entrez [192111](https://www.ncbi.nlm.nih.gov/gene/192111) · UniProt [Q96HS1](https://www.uniprot.org/uniprotkb/Q96HS1) · Ensembl [ENSG00000247077](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247077)

## Data

Gene col 14478: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14478); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14478, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14478]; `tensor/DDL_lfc|DDL_z.npy` [14478]; `embed/gene_vectors.npy` [14478]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14478 or target_col == 14478). Every well: [[PGAM5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGAM5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
