---
symbol: "CNN3"
type: "gene"
col: 3919
ensembl_id: "ENSG00000117519"
name: "calponin 3"
location: "1p21.3"
module: 29
arm: "+"
pooled_cpm: 56.56
n_lines_expressing: 45
n_dd_up: 43
n_dd_down: 3
n_dd_up_clean: 22
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 3
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# CNN3

*calponin 3* — 1p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (21 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.00× (z +17.0, q 0e+00, up in 36 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.50× (z +6.3, q 4e-08, up in 24 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.901× (z -5.6, q 1e-05, down in 4 of 44 measured lines) ⚠ position not correctable. The strongest without an alert is [[ULK-101 (drug)]] 0.05 µM: 0.780× (z -3.6, q 0.053, down in 18 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAM9]] (+0.71, fdr 7e-06), [[SCARB2]] (+0.66, fdr 7e-06), [[TMEM30A]] (+0.64, fdr 7e-06); moves opposite to [[FBXO28]] (-0.61, fdr 7e-06), [[ZNF593]] (-0.60, fdr 8e-06), [[ALKBH1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MYL9]] → it (grade B ⚠); 3 go from it, the strongest it → [[CLIC4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 23 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3919.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.00×** | +17.0 | 0e+00 | 36/42 (HOP62, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.07×** | +16.7 | 0e+00 | 32/35 (HOP62, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.23×** | +11.5 | 4e-28 | 34/39 (HOP62, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.73×** | +8.1 | 6e-14 | 33/42 (A-172, SNU-423, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +6.3 | 4e-08 | 24/43 (HOP62, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.49×** | +6.2 | 6e-08 | 26/43 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.48×** | +6.1 | 1e-07 | 27/43 (PANC-1, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.46×** | +5.8 | 4e-07 | 28/43 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.42×** | +5.5 | 3e-06 | 28/43 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +5.4 | 3e-06 | 24/42 (HCT15, NCI-H23, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +5.4 | 3e-06 | 24/43 (C32, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +5.3 | 4e-06 | 23/43 (SW1417, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.41×** | +5.1 | 1e-05 | 22/44 (A-172, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.37×** | +4.9 | 5e-05 | 23/43 (NCI-H460, SW480, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.36×** | +4.8 | 6e-05 | 27/42 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +4.8 | 6e-05 | 24/43 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.35×** | +4.7 | 9e-05 | 23/42 (C32, LOX-IMVI, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +4.4 | 2e-04 | 24/43 (C32, LOX-IMVI, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.35×** | +4.4 | 2e-04 | 21/42 (C32, SK-MEL-2, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.69×** | +4.3 | 5e-04 | 20/42 (CFPAC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.61×** | +3.8 | 0.003 | 19/43 (C32, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.8 | 0.004 | 17/43 (A-427, A-172, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.004 | 17/43 (C32, LS 180, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Berbamine (drug)]] 5 µM |  | 1.19× | +3.7 | 0.004 | 20/44 (C-33 A, LoVo, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.007 | 16/43 (HCT15, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.011 | 18/43 (C32, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.016 | 14/43 (hTERT-HPNE, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3919.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.901× | -5.6 | 1e-05 | 4/44 (A-427, NCI-H1573, …) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.780×** | -3.6 | 0.053 | 18/43 (HOP62, J82, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.639×** | -3.6 | 0.053 | 16/42 (NCI-H460, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.736×** | -3.4 | 0.099 | 17/42 (AN3 CA, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.813× | -3.2 | 0.15 | 15/42 (SW 900, SHP-77, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.821× | -3.1 | 0.20 | 16/43 (RKO, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3919. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 127 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +15.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.40× (z +10.3) | — |
| [[A-172 (line)]] | wt | 73.5 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.86× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HOP62 (line)]] | alt | 42.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.54× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 91.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.85× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A498 (line)]] | wt | 93.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.36× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[J82 (line)]] | alt | 146 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1792 (line)]] | alt | 44.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.34× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 26.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.76× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 26.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 85.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.38× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.15× (z +9.6) | — |
| [[A549 (line)]] | wt | 20.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.60× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HS-578T (line)]] | alt | 64.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 57.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LoVo (line)]] | wt | 29.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LOX-IMVI (line)]] | wt | 63.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.64× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[RPMI-7951 (line)]] | alt | 99.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SHP-77 (line)]] | alt | 38.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.25× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 30.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[AN3 CA (line)]] | alt | 204 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -12.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -12.2) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0777× (z -9.6) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 73.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[Panc 03.27 (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW 900 (line)]] | alt | 56.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[AsPC-1 (line)]] | alt | 5.40 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.44 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 90.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 107 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.35 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 85.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 97.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 61.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3919), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM9]] | +0.71 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[SCARB2]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[TMEM30A]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[TMX1]] | +0.61 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[TMEM123]] | +0.61 | +0.57 / +0.59 | both halves | 8e-06 |  |
| [[ENAH]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[ERMP1]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[LAMP2]] | +0.58 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[TWSG1]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[GOLM1]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PGAM1]] | +0.57 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[PGRMC1]] | +0.57 | +0.61 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO28]] | -0.61 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[ZNF593]] | -0.60 | -0.58 / -0.61 | both halves | 8e-06 |  |
| [[ALKBH1]] | -0.58 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[SURF6]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[ISG20L2]] | -0.58 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[NT5C]] | -0.58 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[PPP1R35]] ⚠ | -0.56 | -0.53 / -0.58 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TTF1]] | -0.56 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[ZNF557]] | -0.55 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[C19orf25]] | -0.55 | -0.58 / -0.57 | both halves | 9e-06 |  |
| [[ZNF791]] | -0.55 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[PRPF38B]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[CROCCP2-1]] | -0.54 | -0.47 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYL9]] | B | MYL9 activity raises CNN3's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.84× lower at baseline in the lines without MYL9 | 0.026 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[MAP2K1]] | B | MAP2K1 activity lowers CNN3's level | compounds that target MAP2K1: 4 of 4 raise it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 8.4% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds |
| [[MOXD1]] | B | MOXD1 activity raises CNN3's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 2.22× lower at baseline in the lines without MOXD1 | 0.060 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1 |
| [[FLNC]] | B | FLNC activity raises CNN3's level | lines that do not express FLNC (27) vs lines expressing it (23) | 1.91× lower at baseline in the lines without FLNC | 0.070 | ⚠ within organs, on part of the lines; also absent: EDNRA, MOXD1, ARMCX1 |
| [[CDH2]] | B | CDH2 activity raises CNN3's level | lines that do not express CDH2 (22) vs lines expressing it (28) | 2.01× lower at baseline in the lines without CDH2 | 0.080 | ⚠ within organs, on part of the lines; also absent: ARMCX1, DKK3, RFTN1 |
| [[CELSR2]] | B | CELSR2 activity weakens CNN3's drug response | lines that do not express CELSR2 (7) vs lines expressing it (37) | the lines without CELSR2 respond 1.58× as strongly (z diff -1.75); strongest at Panobinostat 5 µM: 2.20x vs 1.46x (z diff -3.3) | 0.091 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLIC4]] | B | CNN3 activity raises CLIC4's level | lines that do not express CNN3 (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without CNN3 | 0.082 | ⚠ within organs, on part of the lines; also absent: SLC9A9, SLC35F1, CNN3-DT |
| [[CRTAP]] | B | CNN3 activity raises CRTAP's level | lines that do not express CNN3 (5) vs lines expressing it (45) | 2.15× lower at baseline in the lines without CNN3 | 0.086 | ⚠ within organs, on part of the lines; also absent: SLC9A9, SLC35F1, CNN3-DT |
| [[CDH2]] | B | CNN3 activity raises CDH2's level | lines that do not express CNN3 (5) vs lines expressing it (45) | 5.54× lower at baseline in the lines without CNN3 | 0.098 | ⚠ within organs, on part of the lines; also absent: SLC9A9, SLC35F1, CNN3-DT |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.1, -20.7); signed map (-22.3, -39.2). **Vector** length 107, 27.7% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +6.7 | +16.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +6.2 | +17.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +6.0 | +11.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.3 | +5.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +4.5 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.4 | +3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.4 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.3 | +2.7 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -3.8 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.7 | +0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.1 | -0.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.5 | -1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.4 | -0.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.1 | -2.8 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -2.1 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | calponin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.3 — chr1:94,896,949-94,927,223 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Calponin family |
| Hallmark sets | MYOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15417](https://www.uniprot.org/uniprotkb/Q15417) (Calponin-3):

> Thin filament-associated protein that is implicated in the regulation and modulation of smooth muscle contraction. It is capable of binding to actin, calmodulin and tropomyosin. The interaction of calponin with actin inhibits the actomyosin Mg-ATPase activity.

**Summary**, from NCBI Gene [1266](https://www.ncbi.nlm.nih.gov/gene/1266):

> This gene encodes a protein with a markedly acidic C terminus; the basic N-terminus is highly homologous to the N-terminus of a related gene, CNN1. Members of the CNN gene family all contain similar tandemly repeated motifs. This encoded protein is associated with the cytoskeleton but is not involved in contraction. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2157](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2157) · Entrez [1266](https://www.ncbi.nlm.nih.gov/gene/1266) · UniProt [Q15417](https://www.uniprot.org/uniprotkb/Q15417) · Ensembl [ENSG00000117519](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117519)

## Data

Gene col 3919: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3919); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3919, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3919]; `tensor/DDL_lfc|DDL_z.npy` [3919]; `embed/gene_vectors.npy` [3919]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3919 or target_col == 3919). Every well: [[CNN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
