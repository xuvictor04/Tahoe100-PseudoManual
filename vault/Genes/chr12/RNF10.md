---
symbol: "RNF10"
type: "gene"
col: 336
ensembl_id: "ENSG00000022840"
name: "ring finger protein 10"
location: "12q24.31"
module: 6
arm: "-"
pooled_cpm: 109.07
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RNF10

*ring finger protein 10* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.87× (z +20.6, q 0e+00, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW1417 0.503×, BT-474 0.507×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (BT-474 0.104×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.275×; ⚠ cell-cycle shift, explains ~0% of this change); [[Apalutamide (drug)]] 5 µM in 1 line (SW 1088 0.0827×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF11]] (+0.62, fdr 7e-06), [[CLIP3]] (+0.62, fdr 2e-05), [[TCTA]] (+0.58, fdr 3e-05); moves opposite to [[URB2]] (-0.60, fdr 1e-05), [[UHRF1]] (-0.57, fdr 1e-05), [[POLR1G]] (-0.56, fdr 1e-05).
> It sits in the **-** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FUT4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 336.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.87×** | +20.6 | 0e+00 | 44/48 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.26×** | +19.0 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +12.5 | 1e-33 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +12.2 | 3e-32 | 46/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.63×** | +11.8 | 7e-30 | 43/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.59×** | +10.8 | 3e-25 | 45/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +10.7 | 8e-25 | 39/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.61×** | +10.4 | 1e-23 | 45/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.35×** | +10.4 | 2e-23 | 44/48 (SW480, NCI-H1573, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +9.9 | 2e-21 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +9.9 | 3e-21 | 34/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +9.8 | 4e-21 | 37/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +6.3 | 1e-08 | 32/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +4.8 | 6e-05 | 15/49 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.24×** | +4.5 | 2e-04 | 23/45 (A-427, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +4.4 | 3e-04 | 27/49 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.029 | 18/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 336.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW1417 0.503×, BT-474 0.507×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (BT-474 0.104×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.275×; ⚠ cell-cycle shift, explains ~0% of this change); [[Apalutamide (drug)]] 5 µM in 1 line (SW 1088 0.0827×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | 0.845× | -3.8 | 0.075 | 17/48 (SK-MEL-2, RKO, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.899× | -3.6 | 0.11 | 2/48 (CHP-212, H4) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.866× | -3.4 | 0.13 | 14/48 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.872× | -3.2 | 0.13 | 11/48 (SW 1088, COLO 205, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.873× | -3.2 | 0.13 | 10/49 (SW1417, CFPAC-1, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.875× | -3.1 | 0.13 | 11/49 (SW1417, C32, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.877× | -3.1 | 0.13 | 12/48 (LS 180, SW48, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.878× | -3.1 | 0.13 | 15/48 (SW1417, NCI-H2030, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.878× | -3.1 | 0.13 | 13/49 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.913× | -3.0 | 0.13 | 3/48 (NCI-H661, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 336. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 122 | 13 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.22× (z +21.1) | — |
| [[PANC-1 (line)]] | alt | 90.6 | 12 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.77× (z +22.1) | — |
| [[SW480 (line)]] | alt | 97.8 | 12 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +21.6) | — |
| [[LoVo (line)]] | wt | 120 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +18.5) | — |
| [[AsPC-1 (line)]] | alt | 107 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.61× (z +17.0) | — |
| [[BT-474 (line)]] | alt | 133 | 3 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +10.6) | [[Lonafarnib (drug)]] 5 µM 0.104× (z -15.4) ⚠ toxic |
| [[LS 180 (line)]] | wt | 96.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +14.8) | — |
| [[NCI-H1573 (line)]] | alt | 111 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +12.5) | — |
| [[NCI-H23 (line)]] | alt | 127 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +12.6) | — |
| [[HOP62 (line)]] | alt | 83.5 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +11.0) | — |
| [[SW 900 (line)]] | alt | 140 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +12.5) | — |
| [[SW1417 (line)]] | alt | 114 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.503× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 122 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +18.2) | — |
| [[HT-29 (line)]] | alt | 115 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +13.3) | — |
| [[KATO III (line)]] | alt | 90.6 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +14.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 125 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.9) | — |
| [[NCI-H1792 (line)]] | alt | 119 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +13.8) | — |
| [[H4 (line)]] | wt | 88.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +11.9) | — |
| [[HepG2_C3A (line)]] | wt | 127 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 124 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.4) | — |
| [[RKO (line)]] | wt | 120 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.1) | — |
| [[SW48 (line)]] | wt | 130 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.12× (z +11.9) | — |
| [[A-172 (line)]] | wt | 78.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.2) | — |
| [[A-427 (line)]] | wt | 113 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.09× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 91.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +16.2) | — |
| [[A549 (line)]] | wt | 117 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +14.5) | — |
| [[C-33 A (line)]] | alt | 103 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +8.7) | — |
| [[C32 (line)]] | wt | 97.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.8) | — |
| [[CHP-212 (line)]] | wt | 119 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 167 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.26× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 77.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +13.2) | — |
| [[HS-578T (line)]] | alt | 75.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 86.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +13.0) | — |
| [[SHP-77 (line)]] | alt | 127 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +10.4) | — |
| [[SK-MEL-2 (line)]] | alt | 102 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.2) | — |
| [[SW 1088 (line)]] | alt | 88.5 | 0 | 1 | — | [[Apalutamide (drug)]] 5 µM 0.0827× (z -9.2) |
| [[SW 1271 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 143 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 74.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 85.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 336), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF11]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 | same gene group |
| [[CLIP3]] | +0.62 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[TCTA]] | +0.58 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[UBXN6]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 | STRING 540 |
| [[ATG4D]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[WBP1]] | +0.56 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[GABARAPL1]] | +0.55 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[FBXO2]] | +0.55 | +0.54 / +0.37 | both halves | 8e-05 |  |
| [[CCDC115]] | +0.53 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[STXBP2]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[SAP18]] | +0.52 | +0.41 / +0.39 | both halves | 5e-05 |  |
| [[TCEA2]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[URB2]] | -0.60 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[UHRF1]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 | same gene group |
| [[POLR1G]] | -0.56 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[FEN1]] | -0.55 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[MCM10]] | -0.55 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[CDC25A]] | -0.55 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[POLA1]] | -0.54 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[FUT4]] | -0.53 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[CDC7]] | -0.53 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[MCM3]] | -0.53 | -0.56 / -0.40 | both halves | 4e-05 |  |
| [[SNRPB]] | -0.52 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[FANCC]] | -0.52 | -0.52 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FUT4]] | B | FUT4 activity lowers RNF10's level | lines that do not express FUT4 (10) vs lines expressing it (40) | 1.08× higher at baseline in the lines without FUT4 | 0.089 | ⚠ within organs, on part of the lines; also absent: PIWIL4, LRRK1, LONRF3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **-** arm (projection on the module's main direction -0.460). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (2.9, -51.2); signed map (-17.2, 5.9). **Vector** length 70.9, 17.8% of its response variance represented; |z| ≥ 3 in 1,022 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.3 | -0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.9 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +4.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.6 | +10.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.0 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +10.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | -0.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.5 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | -0.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.3 | +10.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | +0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.0 | +9.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.8 | +0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | +0.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:120,533,480-120,577,588 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0262, RIE2 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5U6](https://www.uniprot.org/uniprotkb/Q8N5U6) (E3 ubiquitin-protein ligase RNF10):

> E3 ubiquitin-protein ligase that catalyzes monoubiquitination of 40S ribosomal proteins RPS2/us5 and RPS3/us3 in response to ribosome stalling. Part of a ribosome quality control that takes place when ribosomes have stalled during translation initiation (iRQC) or elongation. The ribosome quality control is activated in response to ribosome subunit imbalance, amino acid starvation or downstream the EIF2AK4/GCN2-mediated integrated stress response (ISR). RNF10 acts by mediating monoubiquitination …

**Summary**, from NCBI Gene [9921](https://www.ncbi.nlm.nih.gov/gene/9921):

> The protein encoded by this gene contains a ring finger motif, which is known to be involved in protein-protein interactions. The specific function of this protein has not yet been determined. EST data suggests the existence of multiple alternatively spliced transcript variants, however, their full length nature is not known. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10055](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10055) · Entrez [9921](https://www.ncbi.nlm.nih.gov/gene/9921) · UniProt [Q8N5U6](https://www.uniprot.org/uniprotkb/Q8N5U6) · Ensembl [ENSG00000022840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000022840)

## Data

Gene col 336: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 336); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 336, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 336]; `tensor/DDL_lfc|DDL_z.npy` [336]; `embed/gene_vectors.npy` [336]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 336 or target_col == 336). Every well: [[RNF10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
