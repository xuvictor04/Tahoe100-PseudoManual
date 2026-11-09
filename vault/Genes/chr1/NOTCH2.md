---
symbol: "NOTCH2"
type: "gene"
col: 5530
ensembl_id: "ENSG00000134250"
name: "notch receptor 2"
location: "1p12"
module: 226
arm: "+"
pooled_cpm: 141.41
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/226"]
generated_by: "tahoemap"
---

# NOTCH2

*notch receptor 2* — 1p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.45× (z +8.9, q 4e-16, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.481× (z -11.9, q 8e-30, down in 31 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.797× (z -3.8, q 0.009, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOTCH2NLA]] (+0.66, fdr 7e-06), [[NBPF26]] (+0.65, fdr 1e-05), [[LOXL2]] (+0.57, fdr 1e-05); moves opposite to [[TAF8]] (-0.52, fdr 1e-05), [[ELMOD3]] (-0.50, fdr 3e-05), [[ZNF169]] (-0.50, fdr 3e-05).
> It is in [[Module 226]], a single-armed module (NOTCH2 Activation and Transmission of Signal to the Nucleus).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FGF5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5530.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +8.9 | 4e-16 | 34/46 (SW1417, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +5.3 | 3e-05 | 29/46 (SW480, NCI-H2030, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.73×** | +4.9 | 2e-04 | 30/47 (NCI-H460, BT-474, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +4.7 | 4e-04 | 31/47 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.58×** | +4.0 | 0.006 | 28/46 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.006 | 23/46 (PANC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.7 | 0.016 | 25/46 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.054 | 22/46 (A498, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5530.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.481×** | -11.9 | 8e-30 | 31/42 (SNU-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.512×** | -11.3 | 4e-27 | 37/47 (RKO, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.533×** | -10.2 | 2e-22 | 42/45 (CFPAC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.630×** | -7.2 | 7e-11 | 36/43 (NCI-H1573, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.772×** | -4.4 | 0.001 | 28/46 (HOP62, C32, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.845× | -4.0 | 0.006 | 18/46 (CHP-212, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.794×** | -3.9 | 0.008 | 23/46 (C32, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.797×** | -3.8 | 0.009 | 24/46 (A-427, CFPAC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.820×** | -3.3 | 0.043 | 22/46 (BT-474, SK-MEL-2, …) | inconsistent across doses |  |
| [[Bendamustine (drug)]] 5 µM |  | **0.815×** | -3.3 | 0.043 | 23/46 (SNU-1, KATO III, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.821×** | -3.3 | 0.043 | 23/46 (HS-578T, SNU-423, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.821×** | -3.3 | 0.043 | 23/46 (CFPAC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.831×** | -3.1 | 0.076 | 20/46 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.833×** | -3.1 | 0.084 | 21/46 (HOP62, C32, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.837× | -3.0 | 0.091 | 18/46 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.881× | -3.0 | 0.091 | 14/46 (NCI-H2347, SW 900, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.827×** | -3.0 | 0.091 | 16/46 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5530. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 176 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -16.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 251 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 271 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[RKO (line)]] | wt | 138 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0799× (z -29.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 83.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -12.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 170 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[Hs 766T (line)]] | wt | 133 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -11.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 296 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.422× (z -10.1) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 446 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.15× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SNU-1 (line)]] | wt | 127 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.123× (z -18.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 176 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -13.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 46.0 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.09× (z +11.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.343× (z -10.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 221 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 157 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.455× (z -9.0) ⚠ toxic |
| [[KATO III (line)]] | alt | 48.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.402× (z -8.6) ⚠ toxic |
| [[LoVo (line)]] | wt | 82.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LOX-IMVI (line)]] | wt | 150 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[MIA PaCa-2 (line)]] | alt | 109 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 41.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H23 (line)]] | alt | 254 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.483× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 179 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.304× (z -11.7) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 144 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[PANC-1 (line)]] | alt | 159 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +12.8) | — |
| [[SNU-423 (line)]] | alt | 243 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.378× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AsPC-1 (line)]] | alt | 71.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -11.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 64.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 53.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +13.5) | — |
| [[hTERT-HPNE (line)]] | wt | 364 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 240 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 78.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 197 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.333× (z -10.6) ⚠ toxic |
| [[SW1417 (line)]] | alt | 97.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +14.4) | — |
| [[SW48 (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[BT-474 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 84.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 214 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.7 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 76.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 113 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5530), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH2NLA]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 | pathway: NOTCH2 Activation and Transmission of Signal to the Nucleus |
| [[NBPF26]] | +0.65 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[LOXL2]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[NOTCH2NLB]] | +0.56 | +0.44 / +0.56 | both halves | 3e-05 | pathway: NOTCH2 Activation and Transmission of Signal to the Nucleus |
| [[NBPF14]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[TAGLN2]] | +0.53 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[NBPF10]] | +0.52 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[CD44]] | +0.49 | +0.42 / +0.53 | both halves | 4e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 556 |
| [[MEX3B]] | +0.49 | +0.47 / +0.38 | both halves | 6e-05 |  |
| [[CTSB]] | +0.48 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[PTHLH]] | +0.48 | +0.47 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[FLNA]] | +0.48 | +0.45 / +0.48 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF8]] | -0.52 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[ELMOD3]] | -0.50 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[ZNF169]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[ASPSCR1]] | -0.46 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[VCPKMT]] | -0.45 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[NCBP3]] | -0.45 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[ALG14]] | -0.44 | -0.44 / -0.49 | both halves | 3e-05 | pathway: Diseases of glycosylation |
| [[GTF3C2]] | -0.43 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[MPPE1]] | -0.43 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[EFCAB7]] | -0.43 | -0.32 / -0.49 | both halves | 1e-04 |  |
| [[KEAP1]] | -0.42 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ZKSCAN2-DT]] | -0.42 | -0.38 / -0.44 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGF5]] | B | FGF5 activity raises NOTCH2's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 2.02× lower at baseline in the lines without FGF5 | 0.035 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702 |
| [[ICAM1]] | B | ICAM1 activity raises NOTCH2's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 1.55× lower at baseline in the lines without ICAM1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[AKT3]] | B | AKT3 activity raises NOTCH2's level | lines that do not express AKT3 (16) vs lines expressing it (34) | 2.01× lower at baseline in the lines without AKT3 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| [[EPB41L2]] | B | EPB41L2 activity raises NOTCH2's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.99× lower at baseline in the lines without EPB41L2 | 0.085 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |
| [[AFF3]] | B | AFF3 activity raises NOTCH2's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 2.04× lower at baseline in the lines without AFF3 | 0.095 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 226]] — NOTCH2 Activation and Transmission of Signal to the Nucleus; 9 genes; every member is in the + arm (projection on the module's main direction 0.684). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.5, -29.5); signed map (44.6, -15.5). **Vector** length 104, 29.9% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +0.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +8.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +1.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +0.6 |
|  | [[Tirabrutinib (drug)]] 0.5 µM |  | +1.6 | +1.1 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +1.5 | +1.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.1 | -10.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -4.5 | -3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.9 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.5 | -3.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.4 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.5 | -3.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.4 | -1.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | notch receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p12 — chr1:119,911,553-120,100,779 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Notch receptors |
| Hallmark sets | NOTCH_SIGNALING, UV_RESPONSE_DN, EPITHELIAL_MESENCHYMAL_TRANSITION, G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 17 pathways, smallest: Defective LFNG causes SCDO3; Pre-NOTCH Processing in the Endoplasmic Reticulum; NOTCH2 intracellular domain regulates transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04721](https://www.uniprot.org/uniprotkb/Q04721) (Neurogenic locus notch homolog protein 2):

> Functions as a receptor for membrane-bound ligands Jagged-1 (JAG1), Jagged-2 (JAG2) and Delta-1 (DLL1) to regulate cell-fate determination. Upon ligand activation through the released notch intracellular domain (NICD) it forms a transcriptional activator complex with RBPJ/RBPSUH and activates genes of the enhancer of split locus. Affects the implementation of differentiation, proliferation and apoptotic programs (By similarity). Involved in bone remodeling and homeostasis. In collaboration with …

**Summary**, from NCBI Gene [4853](https://www.ncbi.nlm.nih.gov/gene/4853):

> This gene encodes a member of the Notch family. Members of this Type 1 transmembrane protein family share structural characteristics including an extracellular domain consisting of multiple epidermal growth factor-like (EGF) repeats, and an intracellular domain consisting of multiple, different domain types. Notch family members play a role in a variety of developmental processes by controlling cell fate decisions. The Notch signaling network is an evolutionarily conserved intercellular …

**Accessions** — [HGNC:7882](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7882) · Entrez [4853](https://www.ncbi.nlm.nih.gov/gene/4853) · UniProt [Q04721](https://www.uniprot.org/uniprotkb/Q04721) · Ensembl [ENSG00000134250](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134250)

## Data

Gene col 5530: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5530); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5530, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5530]; `tensor/DDL_lfc|DDL_z.npy` [5530]; `embed/gene_vectors.npy` [5530]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5530 or target_col == 5530). Every well: [[NOTCH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOTCH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
