---
symbol: "TRIM37"
type: "gene"
col: 2942
ensembl_id: "ENSG00000108395"
name: "tripartite motif containing 37"
location: "17q22"
module: 15
arm: "-"
pooled_cpm: 86.84
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# TRIM37

*tripartite motif containing 37* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.25× (z +26.9, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[GSK1059615 (drug)]] 0.5 µM: 0.722× (z -5.3, q 6e-05, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A-427 0.285×, A549 0.409×, SK-MEL-2 0.433×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H2030 0.463×, A549 0.483×, A498 0.535×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.165×, SNU-1 0.134×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Oxaprozin (drug)]] 5 µM in 1 line (NCI-H596 0.127×).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTBK2]] (+0.56, fdr 2e-05), [[ARHGAP17]] (+0.53, fdr 3e-05), [[AIFM1]] (+0.53, fdr 1e-05); moves opposite to [[ZNF432]] (-0.57, fdr 3e-05), [[ADAMTSL4-AS2]] (-0.56, fdr 2e-05), [[SNIP1]] (-0.54, fdr 2e-04).
> It sits in the **-** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GKAP1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2942.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.25×** | +26.9 | 0e+00 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.56×** | +22.1 | 0e+00 | 45/48 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.29×** | +19.5 | 0e+00 | 46/48 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.28×** | +19.3 | 0e+00 | 44/48 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.99×** | +16.2 | 0e+00 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +13.7 | 8e-41 | 41/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.75×** | +13.1 | 2e-37 | 45/48 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +11.8 | 2e-30 | 38/48 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.59×** | +10.9 | 1e-25 | 41/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +10.2 | 1e-22 | 36/48 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +9.5 | 8e-20 | 39/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +9.5 | 1e-19 | 34/48 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +8.4 | 2e-15 | 40/49 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +8.3 | 4e-15 | 35/48 (C32, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +8.2 | 6e-15 | 38/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.83×** | +6.9 | 2e-10 | 37/49 (CFPAC-1, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2942.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A-427 0.285×, A549 0.409×, SK-MEL-2 0.433×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H2030 0.463×, A549 0.483×, A498 0.535×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.165×, SNU-1 0.134×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Oxaprozin (drug)]] 5 µM in 1 line (NCI-H596 0.127×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.722×** | -5.3 | 6e-05 | 27/48 (RKO, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.808×** | -5.0 | 1e-04 | 23/48 (SNU-423, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.874× | -4.5 | 0.001 | 20/48 (J82, H4, …) | top dose only | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.851× | -3.8 | 0.021 | 20/48 (NCI-H661, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Belzutifan (drug)]] 5 µM |  | 0.760× | -3.1 | 0.19 | 14/47 (COLO 205, LS 180, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2942. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 81.4 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +22.3) | — |
| [[SW480 (line)]] | alt | 67.4 | 13 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +18.5) | — |
| [[HOP62 (line)]] | alt | 60.2 | 12 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +18.2) | — |
| [[hTERT-HPNE (line)]] | wt | 70.6 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +17.3) | — |
| [[H4 (line)]] | wt | 50.3 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +17.0) | — |
| [[LoVo (line)]] | wt | 42.6 | 9 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.64× (z +16.9) | — |
| [[CFPAC-1 (line)]] | alt | 79.4 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +18.4) | — |
| [[C32 (line)]] | wt | 37.0 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 3.72× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 36.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +10.8) | — |
| [[J82 (line)]] | alt | 149 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +17.9) | [[Selinexor (drug)]] 5 µM 0.608× (z -9.5) ⚠ cell-cycle shift, explains ~7% of this change |
| [[LS 180 (line)]] | wt | 40.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +13.1) | — |
| [[NCI-H1792 (line)]] | alt | 70.2 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.45× (z +12.4) | — |
| [[PANC-1 (line)]] | alt | 81.5 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.10× (z +11.1) | — |
| [[KATO III (line)]] | alt | 56.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +16.3) | — |
| [[LOX-IMVI (line)]] | wt | 72.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.83× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 75.7 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 68.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.9) | — |
| [[BT-474 (line)]] | alt | 188 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.03× (z +12.0) | — |
| [[HEC-1-A (line)]] | alt | 105 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.5) | — |
| [[HS-578T (line)]] | alt | 88.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.0) | — |
| [[HT-29 (line)]] | alt | 53.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +13.3) | — |
| [[NCI-H1573 (line)]] | alt | 41.7 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.84× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 80.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.4) | — |
| [[Panc 03.27 (line)]] | alt | 79.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.9) | — |
| [[RKO (line)]] | wt | 78.9 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 57.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +14.1) | — |
| [[NCI-H23 (line)]] | alt | 116 | 3 | 0 | [[Cobimetinib (drug)]] 5 µM 2.19× (z +8.9) | — |
| [[A549 (line)]] | wt | 118 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 65.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +14.6) | — |
| [[RPMI-7951 (line)]] | alt | 59.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +16.0) | — |
| [[SNU-1 (line)]] | wt | 83.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 86.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.84× (z +9.5) | — |
| [[A-172 (line)]] | wt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +13.8) | — |
| [[A-427 (line)]] | wt | 224 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 43.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.5) | — |
| [[CHP-212 (line)]] | wt | 134 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +14.1) | — |
| [[HepG2_C3A (line)]] | wt | 52.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 107 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 153 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H596 (line)]] | alt | 75.8 | 0 | 1 | — | [[Oxaprozin (drug)]] 5 µM 0.127× (z -8.6) |
| [[SHP-77 (line)]] | alt | 94.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 136 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 71.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2942), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*32 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTBK2]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[ARHGAP17]] | +0.53 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[AIFM1]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[KIF13A]] | +0.53 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[SOAT1]] | +0.51 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[KPNA3]] | +0.50 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[BLMH]] | +0.49 | +0.44 / +0.52 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[ELMO2]] | +0.49 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[MAZ]] | +0.49 | +0.30 / +0.34 | both halves | 2e-04 |  |
| [[PKIG]] | +0.49 | +0.36 / +0.43 | both halves | 1e-04 |  |
| [[CAMK2G]] | +0.48 | +0.36 / +0.43 | both halves | 1e-04 |  |
| [[HSF2]] | +0.48 | +0.54 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*68 of its nearest partners move opposite, 16 of them with an alert (⚠; 16 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF432]] | -0.57 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[ADAMTSL4-AS2]] | -0.56 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[SNIP1]] | -0.54 | -0.29 / -0.57 | both halves | 2e-04 |  |
| [[TMEM186]] | -0.54 | -0.21 / -0.47 | both halves | 7e-04 |  |
| [[ZNF415]] | -0.54 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[TNFRSF10D]] | -0.53 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[BCL10-AS1]] | -0.53 | -0.26 / -0.48 | both halves | 3e-04 |  |
| [[ZNF275]] | -0.52 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[CCNT1]] | -0.52 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[RALY-AS1]] | -0.51 | -0.24 / -0.39 | both halves | 4e-04 |  |
| [[GNG12-AS1]] | -0.51 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[RECQL5]] | -0.51 | -0.40 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GKAP1]] | C | GKAP1 activity raises TRIM37's level | lines that do not express GKAP1 (3) vs lines expressing it (47) | 2.14× lower at baseline in the lines without GKAP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SEMA3F, TMEM132A, SPDL1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **-** arm (projection on the module's main direction -0.378). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (23.3, -11.8); signed map (-28.0, -15.8). **Vector** length 96.2, 28.2% of its response variance represented; |z| ≥ 3 in 1,433 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (drug)]] 5 µM |  | +4.6 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.1 | +4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.9 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +2.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.8 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +6.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.8 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.4 | -5.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -7.0 | -4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | +1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.4 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | +2.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.4 | -5.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 37 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:58,982,638-59,106,921 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0898, POB1, TEF3; previously MUL |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; Centriolar satellite proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [O94972](https://www.uniprot.org/uniprotkb/O94972) (E3 ubiquitin-protein ligase TRIM37):

> E3 ubiquitin-protein ligase required to prevent centriole reduplication. Probably acts by ubiquitinating positive regulators of centriole reduplication. Mediates monoubiquitination of 'Lys-119' of histone H2A (H2AK119Ub), a specific tag for epigenetic transcriptional repression: associates with some Polycomb group (PcG) multiprotein PRC2-like complex and mediates repression of target genes. Also acts as a positive regulator of peroxisome import by mediating monoubiquitination of PEX5 at …

**Summary**, from NCBI Gene [4591](https://www.ncbi.nlm.nih.gov/gene/4591):

> This gene encodes a member of the tripartite motif (TRIM) family, whose members are involved in diverse cellular functions such as developmental patterning and oncogenesis. The TRIM motif includes zinc-binding domains, a RING finger region, a B-box motif and a coiled-coil domain. The RING finger and B-box domains chelate zinc and might be involved in protein-protein and/or protein-nucleic acid interactions. Mutations in this gene are associated with mulibrey (muscle-liver-brain-eye) nanism, an …

**Accessions** — [HGNC:7523](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7523) · Entrez [4591](https://www.ncbi.nlm.nih.gov/gene/4591) · UniProt [O94972](https://www.uniprot.org/uniprotkb/O94972) · Ensembl [ENSG00000108395](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108395)

## Data

Gene col 2942: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2942); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2942, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2942]; `tensor/DDL_lfc|DDL_z.npy` [2942]; `embed/gene_vectors.npy` [2942]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2942 or target_col == 2942). Every well: [[TRIM37 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM37.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
