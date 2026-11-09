---
symbol: "TUFM"
type: "gene"
col: 10979
ensembl_id: "ENSG00000178952"
name: "Tu translation elongation factor, mitochondrial"
location: "16p11.2"
module: 12
arm: "-"
pooled_cpm: 49.37
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# TUFM

*Tu translation elongation factor, mitochondrial* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.30× (z +13.1, q 2e-36, up in 45 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.46× (z +3.4, q 0.041, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.655× (z -5.4, q 4e-05, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (RKO 0.342×, C-33 A 0.291×, NCI-H23 0.378×, NCI-H2030 0.389×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.175×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NHP2]] (+0.70, fdr 1e-05), [[TYW1]] (+0.65, fdr 1e-05), [[NME2]] (+0.64, fdr 1e-05); moves opposite to [[ZNF213]] (-0.66, fdr 1e-05), [[TCEAL3]] (-0.64, fdr 2e-05), [[THAP2]] (-0.64, fdr 2e-04).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LACC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10979.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **4.30×** | +13.1 | 2e-36 | 45/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.84×** | +11.6 | 1e-28 | 41/42 (KATO III, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.75×** | +8.4 | 9e-15 | 45/45 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.86×** | +5.6 | 3e-06 | 42/47 (SW480, KATO III, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **1.60×** | +4.2 | 0.002 | 37/46 (HT-29, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.2 | 0.002 | 34/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~58% of this change | **1.63×** | +4.2 | 0.002 | 30/47 (NCI-H1573, A-172, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.53×** | +3.8 | 0.009 | 35/48 (COLO 205, A-172, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.041 | 31/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.046 | 27/48 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.065 | 29/48 (A-172, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.41× | +3.1 | 0.11 | 27/48 (SNU-1, AsPC-1, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | 1.90× | +3.0 | 0.11 | 22/48 (AsPC-1, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10979.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (RKO 0.342×, C-33 A 0.291×, NCI-H23 0.378×, NCI-H2030 0.389×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.175×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.655×** | -5.4 | 4e-05 | 34/48 (RKO, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | 0.511× | -3.2 | 0.39 | 31/48 (SK-MEL-2, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.521× | -3.1 | 0.39 | 29/48 (SW480, HCT15, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10979. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 54.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 58.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.97× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 53.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -9.1) |
| [[A-427 (line)]] | wt | 73.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A498 (line)]] | wt | 49.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A549 (line)]] | wt | 46.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.80× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HOP62 (line)]] | alt | 21.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[Hs 766T (line)]] | wt | 63.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.91× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HS-578T (line)]] | alt | 33.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HT-29 (line)]] | alt | 49.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.81× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[J82 (line)]] | alt | 50.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 50.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.33× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LOX-IMVI (line)]] | wt | 44.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.50× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LS 180 (line)]] | wt | 79.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.13× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H1792 (line)]] | alt | 33.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.79× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H23 (line)]] | alt | 55.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 51.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.67× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[PANC-1 (line)]] | alt | 60.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 55.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A-172 (line)]] | wt | 36.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.81× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[C-33 A (line)]] | alt | 64.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -9.7) |
| [[C32 (line)]] | wt | 29.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.52× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[CFPAC-1 (line)]] | alt | 31.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HEC-1-A (line)]] | alt | 44.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H1573 (line)]] | alt | 33.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2030 (line)]] | alt | 70.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 28.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[RKO (line)]] | wt | 94.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -10.8) |
| [[SHP-77 (line)]] | alt | 117 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SNU-423 (line)]] | alt | 28.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.39× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW 900 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.72× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW1417 (line)]] | alt | 51.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[AN3 CA (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 72.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10979), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*33 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHP2]] | +0.70 | +0.71 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 424 |
| [[TYW1]] | +0.65 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[NME2]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 | STRING 469 |
| [[PRELID1]] | +0.64 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[PRKCSH]] | +0.63 | +0.67 / +0.42 | both halves | 4e-05 | pathway: SARS-CoV-2 Infection |
| [[CHID1]] | +0.62 | +0.74 / +0.41 | both halves | 4e-05 |  |
| [[ATP5F1B]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 | STRING 840 |
| [[CENPX]] | +0.61 | +0.60 / +0.39 | both halves | 5e-05 |  |
| [[PHB1]] | +0.61 | +0.65 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 797 |
| [[PHB2]] | +0.61 | +0.67 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 911 |
| [[HACD3]] | +0.59 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[RNGTT]] | +0.59 | +0.58 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*67 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF213]] | -0.66 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[TCEAL3]] | -0.64 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[THAP2]] | -0.64 | -0.63 / -0.32 | both halves | 2e-04 |  |
| [[ZNF585A]] | -0.64 | -0.62 / -0.30 | both halves | 2e-04 |  |
| [[ZNF181]] | -0.63 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[STK16]] | -0.62 | -0.68 / -0.36 | both halves | 9e-05 |  |
| [[ZNF641]] | -0.62 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[TCEANC]] | -0.62 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[LACC1]] | -0.61 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[CCDC90B]] | -0.60 | -0.63 / -0.37 | both halves | 8e-05 |  |
| [[GATAD1]] | -0.60 | -0.71 / -0.26 | both halves | 4e-04 |  |
| [[F8]] | -0.60 | -0.56 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LACC1]] | B | LACC1 activity lowers TUFM's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.54× higher at baseline in the lines without LACC1 | 0.085 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.465). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-12.6, 7.0); signed map (-50.7, -19.6). **Vector** length 55.7, 15.9% of its response variance represented; |z| ≥ 3 in 680 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.2 | +2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.0 | +2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +3.4 |
|  | [[EX229 (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.1 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.0 | -0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +3.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.2 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | +2.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | +0.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.4 | +0.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.2 | -0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | Tu translation elongation factor, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:28,842,411-28,846,348 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EFTu, EF-TuMT, EFTU |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Translational GTPases |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 8 pathways, smallest: SARS-CoV-2 modulates autophagy; Mitochondrial translation elongation; Mitochondrial translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P49411](https://www.uniprot.org/uniprotkb/P49411) (Elongation factor Tu, mitochondrial):

> GTP hydrolase that promotes the GTP-dependent binding of aminoacyl-tRNA to the A-site of ribosomes during protein biosynthesis. Participates in mitochondrial translation (By similarity). Also plays a role in the regulation of autophagy and innate immunity. Recruits ATG5-ATG12 and NLRX1 at mitochondria and serves as a checkpoint of the RIGI-MAVS pathway. In turn, inhibits RLR-mediated type I interferon while promoting autophagy.

**Summary**, from NCBI Gene [7284](https://www.ncbi.nlm.nih.gov/gene/7284):

> This gene encodes a protein which participates in protein translation in mitochondria. Mutations in this gene have been associated with combined oxidative phosphorylation deficiency resulting in lactic acidosis and fatal encephalopathy. A pseudogene has been identified on chromosome 17. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12420](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12420) · Entrez [7284](https://www.ncbi.nlm.nih.gov/gene/7284) · UniProt [P49411](https://www.uniprot.org/uniprotkb/P49411) · Ensembl [ENSG00000178952](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178952)

## Data

Gene col 10979: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10979); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10979, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10979]; `tensor/DDL_lfc|DDL_z.npy` [10979]; `embed/gene_vectors.npy` [10979]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10979 or target_col == 10979). Every well: [[TUFM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUFM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
