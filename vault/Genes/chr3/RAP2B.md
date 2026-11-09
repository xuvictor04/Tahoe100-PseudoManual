---
symbol: "RAP2B"
type: "gene"
col: 11190
ensembl_id: "ENSG00000181467"
name: "RAP2B, member of RAS oncogene family"
location: "3q25.2"
module: 228
arm: "+"
pooled_cpm: 70.76
n_lines_expressing: 47
n_dd_up: 11
n_dd_down: 19
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/228"]
generated_by: "tahoemap"
---

# RAP2B

*RAP2B, member of RAS oncogene family* — 3q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 1.66× (z +9.1, q 3e-17, up in 35 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.649× (z -7.8, q 5e-12, down in 24 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP14]] (+0.61, fdr 1e-05), [[BCL10]] (+0.59, fdr 1e-05), [[BTG1]] (+0.59, fdr 1e-05); moves opposite to [[RBBP4]] (-0.53, fdr 3e-05), [[CRTAP]] (-0.51, fdr 3e-05), [[PON2]] (-0.51, fdr 1e-05).
> It is in [[Module 228]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[BARX2]] → it (grade B ⚠); 2 go from it, the strongest it → [[PPT1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11190.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.66×** | +9.1 | 3e-17 | 35/45 (A498, AsPC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +8.5 | 7e-15 | 28/45 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.44×** | +6.1 | 3e-07 | 29/44 (MIA PaCa-2, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.33×** | +5.2 | 4e-05 | 23/44 (J82, BT-474, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.20×** | +4.7 | 3e-04 | 19/44 (J82, SNU-423, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +4.6 | 4e-04 | 19/45 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 1.19× | +4.4 | 7e-04 | 9/46 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.27×** | +4.4 | 8e-04 | 21/44 (A-172, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.003 | 16/45 (NCI-H460, A549, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.003 | 19/45 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.009 | 14/45 (HS-578T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.012 | 17/45 (NCI-H2347, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.5 | 0.024 | 18/44 (LS 180, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.3 | 0.046 | 15/46 (A549, A498, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.049 | 12/46 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.051 | 10/45 (A549, A-427, …) | rises with dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.056 | 11/46 (Panc 03.27, SK-MEL-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11190.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.649×** | -7.8 | 5e-12 | 24/45 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.664×** | -7.1 | 4e-10 | 30/43 (CFPAC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.713×** | -6.1 | 2e-07 | 24/45 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.738×** | -5.5 | 6e-06 | 24/45 (HS-578T, NCI-H460, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.561×** | -5.4 | 6e-06 | 22/34 (HS-578T, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.747×** | -5.2 | 1e-05 | 21/44 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.748×** | -5.2 | 1e-05 | 22/45 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.755×** | -4.8 | 1e-04 | 26/45 (NCI-H460, C32, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.611×** | -4.6 | 2e-04 | 20/44 (NCI-H2347, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.778×** | -4.5 | 4e-04 | 21/45 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.779×** | -4.5 | 4e-04 | 21/45 (NCI-H460, Panc 03.27, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.630×** | -4.3 | 7e-04 | 21/46 (Panc 03.27, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.798×** | -4.0 | 0.002 | 20/45 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.653×** | -4.0 | 0.003 | 16/44 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.662×** | -3.9 | 0.004 | 19/40 (CFPAC-1, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.796×** | -3.8 | 0.006 | 20/44 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.826×** | -3.4 | 0.019 | 17/45 (NCI-H460, NCI-H2347, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.828×** | -3.4 | 0.020 | 22/44 (NCI-H460, A-172, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.842× | -3.1 | 0.049 | 19/45 (NCI-H460, HS-578T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | 0.843× | -3.1 | 0.049 | 16/45 (A498, NCI-H460, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.839× | -3.0 | 0.054 | 17/45 (SW1417, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11190. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 311 | 2 | 19 (11 ⚠) | [[Auranofin (drug)]] 5 µM 2.19× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0898× (z -39.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Binimetinib (drug)]] 0.05 µM 0.479× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 85.0 | 0 | 21 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.346× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 255 | 0 | 11 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[Panc 03.27 (line)]] | alt | 221 | 0 | 11 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.163× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 205 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -19.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[J82 (line)]] | alt | 61.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +13.5) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.93× (z +11.3) | — |
| [[SK-MEL-2 (line)]] | alt | 67.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 67.1 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.05 µM 2.60× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.163× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[C32 (line)]] | wt | 87.9 | 0 | 3 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -10.4) ⚠ cell-cycle shift, explains ~50% of this change |
| [[AsPC-1 (line)]] | alt | 45.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.01× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 34.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.63× (z +9.5) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[HepG2_C3A (line)]] | wt | 52.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.198× (z -11.9) ⚠ toxic |
| [[HS-578T (line)]] | alt | 50.8 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.102× (z -9.8) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 66.4 | 1 | 1 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.79× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.164× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A498 (line)]] | wt | 45.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.46× (z +9.1) | — |
| [[A549 (line)]] | wt | 40.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[COLO 205 (line)]] | alt | 79.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.232× (z -8.7) ⚠ toxic |
| [[HOP62 (line)]] | alt | 42.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.316× (z -10.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 57.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.362× (z -8.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 49.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H1573 (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.319× (z -9.1) ⚠ cell-cycle shift, explains ~42% of this change |
| [[PANC-1 (line)]] | alt | 31.5 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.14× (z +11.7) | — |
| [[RKO (line)]] | wt | 27.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.310× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 31.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.9) ⚠ cell-cycle shift, explains ~99% of this change | — |
| [[A-427 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.9 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 76.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 99.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 32.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11190), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP14]] | +0.61 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[BCL10]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[BTG1]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[H3-3B]] | +0.58 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[MAST4]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[BMP2]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[FAM107B]] | +0.55 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[FAM43A]] | +0.54 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[ISG20]] | +0.54 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[BCL2A1]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[SERTAD1]] | +0.53 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[EHD1]] | +0.53 | +0.43 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP4]] | -0.53 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[CRTAP]] | -0.51 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[PON2]] | -0.51 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[IPO11]] | -0.51 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[NUDT21]] | -0.49 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[NDUFA10]] | -0.49 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[MSI2]] | -0.49 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[STT3B]] | -0.49 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[OGFOD3]] | -0.49 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[ADPGK]] | -0.48 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[RCN2]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[RPUSD4]] | -0.48 | -0.43 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BARX2]] | B | BARX2 activity raises RAP2B's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 1.88× lower at baseline in the lines without BARX2 | 0.057 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[FRMD4B]] | B | FRMD4B activity raises RAP2B's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 1.80× lower at baseline in the lines without FRMD4B | 0.065 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[DAPP1]] | B | DAPP1 activity raises RAP2B's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 2.13× lower at baseline in the lines without DAPP1 | 0.069 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[RNF223]] | B | RNF223 activity raises RAP2B's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 1.75× lower at baseline in the lines without RNF223 | 0.072 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPT1]] | C | RAP2B activity lowers PPT1's level | lines that do not express RAP2B (3) vs lines expressing it (47) | 1.80× higher at baseline in the lines without RAP2B | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, SPRY4-AS1; maybe low, not absent |
| [[TMEM158]] | C | RAP2B activity raises TMEM158's level | lines that do not express RAP2B (3) vs lines expressing it (47) | 4.71× lower at baseline in the lines without RAP2B | 0.091 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, SPRY4-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 228]]; 8 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.1, 3.0); signed map (4.6, 23.4). **Vector** length 120, 31.6% of its response variance represented; |z| ≥ 3 in 1,497 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +9.0 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.3 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +6.0 | +5.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.0 | +6.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.8 | +2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.8 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.4 | +1.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -6.0 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.7 | -4.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.6 | -5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change | -4.1 | -3.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.7 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.6 | -2.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | RAP2B, member of RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.2 — chr3:153,162,226-153,170,627 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAS type GTPase family |
| Hallmark sets | P53_PATHWAY |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P61225](https://www.uniprot.org/uniprotkb/P61225) (Ras-related protein Rap-2b):

> Small GTP-binding protein which cycles between a GDP-bound inactive and a GTP-bound active form. Involved in EGFR and CHRM3 signaling pathways through stimulation of PLCE1. May play a role in cytoskeletal rearrangements and regulate cell spreading through activation of the effector TNIK. May regulate membrane vesiculation in red blood cells.

**Summary**, from NCBI Gene [5912](https://www.ncbi.nlm.nih.gov/gene/5912):

> This intronless gene belongs to a family of RAS-related genes. The proteins encoded by these genes share approximately 50% amino acid identity with the classical RAS proteins and have numerous structural features in common. The most striking difference between the RAP and RAS proteins resides in their 61st amino acid: glutamine in RAS is replaced by threonine in RAP proteins. Evidence suggests that this protein may be polyisoprenylated and palmitoylated. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9862) · Entrez [5912](https://www.ncbi.nlm.nih.gov/gene/5912) · UniProt [P61225](https://www.uniprot.org/uniprotkb/P61225) · Ensembl [ENSG00000181467](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181467)

## Data

Gene col 11190: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11190); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11190, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11190]; `tensor/DDL_lfc|DDL_z.npy` [11190]; `embed/gene_vectors.npy` [11190]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11190 or target_col == 11190). Every well: [[RAP2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAP2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
