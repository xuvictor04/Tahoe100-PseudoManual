---
symbol: "ABCA15P"
type: "gene"
col: 12096
ensembl_id: "ENSG00000189149"
name: "ATP binding cassette subfamily A member 15, pseudogene"
location: "16p12.2"
module: 125
arm: "+"
pooled_cpm: 12.68
n_lines_expressing: 48
n_dd_up: 32
n_dd_down: 5
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# ABCA15P

*ATP binding cassette subfamily A member 15, pseudogene* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (12 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.61× (z +16.8, q 0e+00, up in 38 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.620× (z -6.3, q 2e-07, down in 21 of 46 measured lines) ⚠ cell-cycle shift, explains ~62% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 10 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (PANC-1 0.0800×, LoVo 0.208×, SW480 0.207×; ⚠ cell-cycle shift, explains ~62% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (MIA PaCa-2 0.105×, PANC-1 0.203×, SNU-423 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (PANC-1 0.242×, C-33 A 0.0634×, MIA PaCa-2 0.230×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.363×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00520]] (+0.66, fdr 7e-06), [[ERICH1]] (+0.63, fdr 1e-05), [[CRYM]] (+0.61, fdr 1e-05, ⚠ same locus), [[ADCY7]] (+0.61, fdr 1e-05); moves opposite to [[DOP1A]] (-0.59, fdr 3e-05), [[PRKACA]] (-0.55, fdr 1e-05), [[MPC2]] (-0.54, fdr 2e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC01088]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12096.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.61×** | +16.8 | 0e+00 | 38/42 (LoVo, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.67×** | +9.5 | 4e-19 | 30/46 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.97×** | +8.4 | 9e-15 | 25/42 (LoVo, SW1417, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +7.2 | 1e-10 | 24/41 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.42×** | +6.5 | 1e-08 | 24/46 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.61×** | +6.2 | 5e-08 | 27/45 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +5.8 | 4e-07 | 21/44 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.55×** | +5.8 | 5e-07 | 20/43 (LoVo, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.55×** | +5.7 | 7e-07 | 23/45 (LoVo, A498, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.53×** | +5.6 | 1e-06 | 21/43 (NCI-H460, hTERT-HPNE, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +5.6 | 1e-06 | 22/38 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.53×** | +5.4 | 4e-06 | 18/41 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.44×** | +4.8 | 7e-05 | 19/42 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.99×** | +4.7 | 9e-05 | 18/33 (LoVo, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **1.92×** | +4.5 | 3e-04 | 13/42 (Hs 766T, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +4.3 | 6e-04 | 16/42 (A-172, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +4.2 | 9e-04 | 12/44 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.007 | 11/42 (NCI-H1573, KATO III, …) | rises with dose | position effect removed |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.018 | 9/43 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.018 | 12/45 (A-427, A549, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.20× | +3.4 | 0.020 | 13/45 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.025 | 7/44 (A498, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.029 | 12/45 (hTERT-HPNE, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12096.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 10 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (PANC-1 0.0800×, LoVo 0.208×, SW480 0.207×; ⚠ cell-cycle shift, explains ~62% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (MIA PaCa-2 0.105×, PANC-1 0.203×, SNU-423 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (PANC-1 0.242×, C-33 A 0.0634×, MIA PaCa-2 0.230×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.363×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.620×** | -6.3 | 2e-07 | 21/46 (PANC-1, LoVo, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | **0.661×** | -5.5 | 1e-05 | 21/40 (CFPAC-1, PANC-1, …) | all doses, flat | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.460×** | -5.3 | 2e-05 | 18/41 (LoVo, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | **0.741×** | -4.0 | 0.011 | 14/30 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **0.754×** | -3.7 | 0.022 | 21/41 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.782× | -3.1 | 0.17 | 4/42 (HS-578T, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12096. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.4 | 0 | 9 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0800× (z -18.1) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 23.7 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 13.3 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[A-427 (line)]] | wt | 13.1 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -11.8) ⚠ cell-cycle shift, explains ~2% of this change |
| [[COLO 205 (line)]] | alt | 7.29 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 23.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.08× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -11.3) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SW480 (line)]] | alt | 12.7 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.169× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 13.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 10.8 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 4.80× (z +9.7) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[BT-474 (line)]] | alt | 8.57 | 1 | 0 | [[Auranofin (drug)]] 5 µM 12.0× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0634× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 9.54 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0943× (z -10.7) ⚠ transcription drop; cell-cycle shift, explains ~69% of this change |
| [[H4 (line)]] | wt | 35.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[HEC-1-A (line)]] | alt | 9.31 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 5.43 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.5× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.196× (z -8.9) ⚠ transcription drop; cell-cycle shift, explains ~69% of this change |
| [[SNU-423 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[A498 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12096), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00520]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ERICH1]] | +0.63 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[CRYM]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 | ⚠ same locus (12.8 kb: neighbours can correlate without regulation) |
| [[ADCY7]] | +0.61 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[RBM19]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[LINC01088]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[C12orf56]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[TATDN1]] | +0.56 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[DHX34]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ATP6V1E2]] | +0.55 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[CPEB1]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ZNF83]] | +0.54 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[LINC01357]] | +0.54 | +0.46 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOP1A]] | -0.59 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[PRKACA]] | -0.55 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[MPC2]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[PIGS]] | -0.53 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ABHD16A]] | -0.52 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ARL3]] | -0.51 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[ALAD]] | -0.51 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[CTDSPL2]] | -0.51 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ADD3]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[USP48]] | -0.50 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[PIN1]] | -0.50 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[GBF1]] | -0.50 | -0.42 / -0.54 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01088]] | B | LINC01088 activity raises ABCA15P's level | lines that do not express LINC01088 (9) vs lines expressing it (41) | 1.60× lower at baseline in the lines without LINC01088 | 0.034 | ⚠ within organs, on part of the lines; also absent: PPP4R4, GPR155, PKIG; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.539). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.2, 49.9); signed map (42.2, -6.0). **Vector** length 111, 27.3% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.7 | +16.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +5.7 | +9.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | +5.1 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +5.0 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +5.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.2 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +3.2 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.3 | -5.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -2.2 | -6.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.0 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily A member 15, pseudogene |
| Locus type | pseudogene |
| Location | 16p12.2 — chr16:21,315,911-21,339,037 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | ABCA15P1, FLJ41766; previously NCRNA00169, CRYM-AS1 |
| Gene groups (HGNC) | ATP binding cassette subfamily A; Unitary pseudogenes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [400508](https://www.ncbi.nlm.nih.gov/gene/400508):

> Predicted to act upstream of or within hematopoietic progenitor cell differentiation. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34405](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34405) · Entrez [400508](https://www.ncbi.nlm.nih.gov/gene/400508) · Ensembl [ENSG00000189149](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189149)

## Data

Gene col 12096: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12096); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12096, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12096]; `tensor/DDL_lfc|DDL_z.npy` [12096]; `embed/gene_vectors.npy` [12096]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12096 or target_col == 12096). Every well: [[ABCA15P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCA15P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
