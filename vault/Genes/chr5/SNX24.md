---
symbol: "SNX24"
type: "gene"
col: 753
ensembl_id: "ENSG00000064652"
name: "sorting nexin 24"
location: "5q23.2"
module: 18
arm: "+"
pooled_cpm: 46.9
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# SNX24

*sorting nexin 24* — 5q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.44× (z +10.4, q 2e-22, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.678× (z -7.5, q 3e-11, down in 27 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.821× (z -4.0, q 0.009, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (C32 0.103×, BT-474 0.198×, SK-MEL-2 0.231×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.0612×, SNU-1 0.149×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (LS 180 0.0956×, LoVo 0.323×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (NCI-H23 0.355×, SW480 0.400×); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.194×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RUSC2]] (+0.63, fdr 1e-05), [[SLC22A15]] (+0.61, fdr 1e-05), [[NBPF20]] (+0.59, fdr 1e-05); moves opposite to [[FAM117A]] (-0.47, fdr 1e-04), [[GPRC5C]] (-0.47, fdr 2e-05), [[MAP3K11]] (-0.46, fdr 5e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[BEND7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 753.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +10.4 | 2e-22 | 36/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +7.1 | 3e-10 | 27/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +7.1 | 3e-10 | 27/48 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.32×** | +5.5 | 6e-06 | 27/48 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.21×** | +5.3 | 2e-05 | 20/48 (NCI-H2347, SK-MEL-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.25×** | +4.4 | 0.001 | 20/47 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +4.3 | 0.001 | 16/48 (NCI-H2347, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.22×** | +4.0 | 0.005 | 18/47 (NCI-H1573, SK-MEL-2, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.006 | 18/48 (LOX-IMVI, SK-MEL-2, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.009 | 19/48 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.7 | 0.013 | 16/48 (H4, SK-MEL-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.013 | 17/48 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | 1.14× | +3.6 | 0.016 | 18/48 (LoVo, LS 180, …) | rises with dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.19× | +3.5 | 0.021 | 15/48 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.19× | +3.5 | 0.021 | 18/48 (NCI-H1573, SK-MEL-2, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.021 | 18/48 (Hs 766T, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.046 | 12/47 (HepG2/C3A, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.064 | 9/48 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 753.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (C32 0.103×, BT-474 0.198×, SK-MEL-2 0.231×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.0612×, SNU-1 0.149×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (LS 180 0.0956×, LoVo 0.323×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (NCI-H23 0.355×, SW480 0.400×); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.194×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.678×** | -7.5 | 3e-11 | 27/47 (J82, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.736×** | -6.0 | 7e-07 | 26/48 (NCI-H460, J82, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.857× | -4.4 | 0.002 | 21/48 (NCI-H2030, J82, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.821×** | -4.0 | 0.009 | 19/48 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.813×** | -3.9 | 0.013 | 21/44 (C32, BT-474, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.829×** | -3.8 | 0.014 | 17/47 (LS 180, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.829×** | -3.6 | 0.022 | 19/42 (NCI-H23, SW1417, …) | inconsistent across doses | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.729×** | -3.3 | 0.060 | 16/47 (J82, NCI-H23, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 753. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.5 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.80× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.355× (z -10.3) ⚠ cell-cycle shift, explains ~45% of this change |
| [[J82 (line)]] | alt | 70.4 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 43.9 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.323× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[MIA PaCa-2 (line)]] | alt | 47.4 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.45× (z +14.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 72.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 70.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.355× (z -10.7) |
| [[PANC-1 (line)]] | alt | 66.3 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.494× (z -9.3) ⚠ cell-cycle shift, explains ~45% of this change |
| [[AN3 CA (line)]] | alt | 67.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 42.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 45.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 94.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0612× (z -33.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 44.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.422× (z -8.7) ⚠ toxic |
| [[A549 (line)]] | wt | 64.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[C-33 A (line)]] | alt | 88.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.341× (z -9.8) ⚠ toxic |
| [[C32 (line)]] | wt | 36.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[HCT15 (line)]] | alt | 34.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HEC-1-A (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 79.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.279× (z -10.2) ⚠ toxic |
| [[LS 180 (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0956× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[Panc 03.27 (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[RPMI-7951 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.265× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~76% of this change |
| [[SHP-77 (line)]] | alt | 37.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[SK-MEL-2 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[SNU-1 (line)]] | wt | 62.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW48 (line)]] | wt | 33.3 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.194× (z -8.7) |
| [[SW480 (line)]] | alt | 24.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.400× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 108 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 753), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RUSC2]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SLC22A15]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[NBPF20]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PTPN21]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ULK2]] | +0.58 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[KANK1]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[DTNB]] | +0.56 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[NUTM2A-AS1]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[FARP1]] | +0.56 | +0.50 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[KPNA3]] | +0.55 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[HEG1]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[TTC7B]] | +0.55 | +0.44 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM117A]] | -0.47 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[GPRC5C]] | -0.47 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[MAP3K11]] | -0.46 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[DBP]] | -0.45 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ARID4A]] | -0.45 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[HOOK2]] | -0.45 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[MXD1]] | -0.44 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[INTS6L]] | -0.44 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[KLHL3]] | -0.44 | -0.35 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BEND7]] | B | BEND7 activity raises SNX24's level | lines that do not express BEND7 (12) vs lines expressing it (38) | 1.31× lower at baseline in the lines without BEND7 | 0.039 | ⚠ within organs, on part of the lines; also absent: ZIC2 |
| [[MVB12B]] | B | MVB12B activity raises SNX24's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 2.06× lower at baseline in the lines without MVB12B | 0.066 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[ULK2]] | B | ULK2 activity raises SNX24's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 1.63× lower at baseline in the lines without ULK2 | 0.067 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[HEG1]] | B | HEG1 activity raises SNX24's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 1.87× lower at baseline in the lines without HEG1 | 0.092 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[KRT7]] | B | KRT7 activity lowers SNX24's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 1.20× higher at baseline in the lines without KRT7 | 0.095 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.517). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (19.8, -24.5); signed map (-9.2, 25.8). **Vector** length 109, 27.6% of its response variance represented; |z| ≥ 3 in 1,101 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.8 | +3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.8 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +10.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.1 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.1 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.0 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.8 | -6.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.8 | -7.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.7 | -1.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Ixazomib (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[Vilanterol (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.2 — chr5:122,843,439-123,029,354 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SBBI31 |
| Gene groups (HGNC) | Sorting nexins |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y343](https://www.uniprot.org/uniprotkb/Q9Y343) (Sorting nexin-24):

> May be involved in several stages of intracellular trafficking.

**Summary**, from NCBI Gene [28966](https://www.ncbi.nlm.nih.gov/gene/28966):

> Predicted to enable phosphatidylinositol phosphate binding activity. Predicted to be involved in protein transport. Predicted to be located in cytoplasmic vesicle membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21533](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21533) · Entrez [28966](https://www.ncbi.nlm.nih.gov/gene/28966) · UniProt [Q9Y343](https://www.uniprot.org/uniprotkb/Q9Y343) · Ensembl [ENSG00000064652](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064652)

## Data

Gene col 753: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 753); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 753, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 753]; `tensor/DDL_lfc|DDL_z.npy` [753]; `embed/gene_vectors.npy` [753]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 753 or target_col == 753). Every well: [[SNX24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
