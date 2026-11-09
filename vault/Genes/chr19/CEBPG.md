---
symbol: "CEBPG"
type: "gene"
col: 7744
ensembl_id: "ENSG00000153879"
name: "CCAAT enhancer binding protein gamma"
location: "19q13.11"
module: 133
arm: "+"
pooled_cpm: 57.99
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 16
n_dd_up_clean: 31
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# CEBPG

*CCAAT enhancer binding protein gamma* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (8 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 2.01× (z +9.9, q 1e-20, up in 44 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Neratinib (maleate) (drug)]] 0.5 µM: 1.92× (z +9.7, q 9e-20, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.590× (z -7.9, q 2e-12, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XPOT]] (+0.85, fdr 7e-06), [[AARS1]] (+0.82, fdr 7e-06), [[TARS1]] (+0.79, fdr 7e-06).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ASNSP1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RBCK1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7744.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +9.9 | 1e-20 | 44/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.92×** | +9.7 | 9e-20 | 43/48 (NCI-H2030, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.56×** | +9.4 | 1e-18 | 43/48 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM |  | **1.52×** | +8.8 | 2e-16 | 36/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.81×** | +8.8 | 2e-16 | 41/48 (SW 900, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +8.7 | 2e-16 | 36/47 (HOP62, A549, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.79×** | +8.7 | 4e-16 | 38/47 (LOX-IMVI, C-33 A, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +8.5 | 1e-15 | 41/48 (C32, SHP-77, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.45×** | +7.8 | 3e-13 | 35/48 (COLO 205, LS 180, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.67×** | +7.6 | 2e-12 | 39/48 (C-33 A, SHP-77, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.63×** | +7.2 | 2e-11 | 34/48 (C-33 A, RKO, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.55×** | +6.5 | 5e-09 | 35/48 (COLO 205, BT-474, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.56×** | +6.3 | 1e-08 | 35/47 (COLO 205, NCI-H23, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.51×** | +6.1 | 3e-08 | 34/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +6.0 | 9e-08 | 28/46 (HOP62, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.08×** | +5.7 | 4e-07 | 36/48 (LOX-IMVI, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.31×** | +5.6 | 6e-07 | 28/49 (NCI-H460, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +5.6 | 6e-07 | 30/48 (SHP-77, A549, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +5.5 | 9e-07 | 30/48 (SW 900, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7744.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.590×** | -7.9 | 2e-12 | 33/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.417×** | -6.8 | 2e-09 | 38/49 (A-427, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.635×** | -6.8 | 2e-09 | 33/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.645×** | -6.5 | 8e-09 | 30/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.659×** | -5.8 | 1e-06 | 29/47 (SW480, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.725×** | -4.8 | 1e-04 | 26/47 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.562×** | -4.5 | 5e-04 | 27/47 (A-172, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.585×** | -4.2 | 0.002 | 25/47 (SNU-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.766×** | -4.0 | 0.004 | 22/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.831×** | -3.9 | 0.005 | 18/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -3.8 | 0.009 | 23/48 (HS-578T, HT-29, …) | top dose only | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -3.5 | 0.020 | 2/49 (MIA PaCa-2, CHP-212) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.794×** | -3.5 | 0.023 | 18/48 (KATO III, NCI-H2347, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.802×** | -3.3 | 0.038 | 21/48 (PANC-1, RKO, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.860× | -3.2 | 0.049 | 22/48 (A-172, RKO, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.811×** | -3.2 | 0.056 | 16/48 (MIA PaCa-2, KATO III, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.815×** | -3.1 | 0.068 | 14/48 (NCI-H2347, RKO, …) | top dose only |  |
| [[Artesunate (drug)]] 0.05 µM |  | **0.821×** | -3.0 | 0.095 | 14/48 (CFPAC-1, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7744. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 123 | 1 | 11 (6 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.61× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -18.6) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.328× (z -15.7) |
| [[HT-29 (line)]] | alt | 183 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -22.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.211× (z -19.7) |
| [[A-172 (line)]] | wt | 76.7 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.308× (z -11.6) |
| [[A498 (line)]] | wt | 63.4 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.397× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 48.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.25× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 79.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.332× (z -10.2) |
| [[KATO III (line)]] | alt | 113 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.278× (z -13.8) |
| [[LoVo (line)]] | wt | 101 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.326× (z -13.0) |
| [[A549 (line)]] | wt | 67.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +16.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 36.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.82× (z +12.0) | — |
| [[RKO (line)]] | wt | 83.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.123× (z -9.2) |
| [[SW480 (line)]] | alt | 72.1 | 2 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.52× (z +10.5) ⚠ toxic · without an alert: [[Artesunate (drug)]] 5 µM 1.73× (z +9.1) | [[Harringtonine (drug)]] 0.05 µM 0.436× (z -9.1) |
| [[A-427 (line)]] | wt | 74.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -17.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.114× (z -11.2) |
| [[AN3 CA (line)]] | alt | 29.0 | 0 | 2 | — | [[TAK-901 (drug)]] 0.05 µM 0.0491× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 28.1 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.79× (z +9.7) ⚠ toxic · without an alert: [[5-Azacytidine (drug)]] 5 µM 3.36× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 86.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.371× (z -9.1) |
| [[SNU-1 (line)]] | wt | 73.8 | 1 | 1 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.57× (z +9.5) | [[NG25 (drug)]] 5 µM 0.0457× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 40.7 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.96× (z +8.7) ⚠ toxic | — |
| [[C32 (line)]] | wt | 19.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.69× (z +11.0) | — |
| [[COLO 205 (line)]] | alt | 32.4 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.01× (z +9.1) ⚠ toxic | — |
| [[MIA PaCa-2 (line)]] | alt | 58.6 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.96× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 35.4 | 1 | 0 | [[Neratinib (maleate) (drug)]] 0.5 µM 2.87× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 34.8 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.52× (z +10.9) | — |
| [[RPMI-7951 (line)]] | alt | 38.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.87× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 70.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.342× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW48 (line)]] | wt | 87.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.300× (z -9.2) |
| [[BT-474 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 74.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7744), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPOT]] | +0.85 | +0.83 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[AARS1]] | +0.82 | +0.81 / +0.85 | both halves | 7e-06 |  |
| [[TARS1]] | +0.79 | +0.77 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[EIF2S2]] | +0.79 | +0.84 / +0.71 | both halves | 7e-06 | pathway: Cellular response to starvation; STRING 567 |
| [[PCK2]] | +0.78 | +0.71 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[NIBAN1]] | +0.78 | +0.76 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[MARS1]] | +0.77 | +0.76 / +0.80 | both halves | 7e-06 |  |
| [[YARS1]] | +0.77 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[SLC6A9]] | +0.77 | +0.71 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[NARS1]] | +0.77 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[CARS1]] | +0.76 | +0.75 / +0.78 | both halves | 7e-06 |  |
| [[ASNS]] | +0.76 | +0.77 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 676 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASNSP1]] | B | ASNSP1 activity raises CEBPG's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.34× lower at baseline in the lines without ASNSP1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[ASNS]] | C | ASNS's natural level weakens CEBPG's drug response | ASNS's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.68, reverse -0.42; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBCK1]] | C | CEBPG's natural level strengthens RBCK1's drug response | CEBPG's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.03; direction not clear | 0.069 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.864). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.6, 47.6); signed map (-13.1, 23.6). **Vector** length 151, 51.6% of its response variance represented; |z| ≥ 3 in 1,565 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[5-Azacytidine (drug)]] 5 µM |  | +11.3 | +8.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +9.8 | +9.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.6 | +8.8 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +9.5 | +9.7 |
|  | [[Artesunate (drug)]] 5 µM |  | +9.3 | +8.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +9.1 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.1 | +8.5 |
|  | [[Neratinib (drug)]] 5 µM |  | +8.0 | +7.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.1 | -6.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -6.0 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.8 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -4.3 | -3.3 |
|  | [[NG25 (drug)]] 5 µM |  | -4.2 | -4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.1 | -5.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.3 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[Arbutin (drug)]] 0.05 µM |  | -2.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | CCAAT enhancer binding protein gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:33,373,685-33,382,686 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GPE1BP, IG/EBP-1 |
| Gene groups (HGNC) | CCAAT/enhancer binding proteins |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, UV_RESPONSE_UP |
| Reactome | 8 pathways, smallest: Response of EIF2AK1 (HRI) to heme deficiency; ATF4 activates genes in response to endoplasmic reticulum  stress; PERK regulates gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [P53567](https://www.uniprot.org/uniprotkb/P53567) (CCAAT/enhancer-binding protein gamma):

> Transcription factor that binds to the promoter and the enhancer regions of target genes. Binds to the enhancer element PRE-I (positive regulatory element-I) of the IL-4 gene. Binds to the promoter and the enhancer of the immunoglobulin heavy chain. Binds to GPE1, a cis-acting element in the G-CSF gene promoter.

**Summary**, from NCBI Gene [1054](https://www.ncbi.nlm.nih.gov/gene/1054):

> The C/EBP family of transcription factors regulates viral and cellular CCAAT/enhancer element-mediated transcription. C/EBP proteins contain the bZIP region, which is characterized by two motifs in the C-terminal half of the protein: a basic region involved in DNA binding and a leucine zipper motif involved in dimerization. The C/EBP family consist of several related proteins, C/EBP alpha, C/EBP beta, C/EBP gamma, and C/EBP delta, that form homodimers and that form heterodimers with each other. …

**Accessions** — [HGNC:1837](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1837) · Entrez [1054](https://www.ncbi.nlm.nih.gov/gene/1054) · UniProt [P53567](https://www.uniprot.org/uniprotkb/P53567) · Ensembl [ENSG00000153879](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153879)

## Data

Gene col 7744: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7744); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7744, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7744]; `tensor/DDL_lfc|DDL_z.npy` [7744]; `embed/gene_vectors.npy` [7744]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7744 or target_col == 7744). Every well: [[CEBPG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEBPG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
