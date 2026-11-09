---
symbol: "CDCA5"
type: "gene"
col: 7110
ensembl_id: "ENSG00000146670"
name: "cell division cycle associated 5"
location: "11q13.1"
module: 71
arm: "+"
pooled_cpm: 29.86
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 18
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# CDCA5

*cell division cycle associated 5* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.76× (z +9.3, q 7e-18, up in 32 of 46 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.31× (z +3.2, q 0.048, up in 17 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.485× (z -8.5, q 2e-14, down in 38 of 47 measured lines) ⚠ cell-cycle shift, explains ~65% of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.721× (z -5.4, q 1e-05, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPO]] (+0.88, fdr 7e-06), [[POLQ]] (+0.86, fdr 7e-06), [[SPC25]] (+0.86, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7110.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.76×** | +9.3 | 7e-18 | 32/46 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.80×** | +6.6 | 1e-08 | 30/44 (SW480, KATO III, …) | rises with dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.34×** | +4.8 | 3e-04 | 29/47 (HT-29, A-427, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~80% of this change | **1.50×** | +4.8 | 3e-04 | 26/44 (AsPC-1, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.32×** | +4.6 | 5e-04 | 26/47 (SW480, HT-29, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.50×** | +4.5 | 5e-04 | 24/47 (SW480, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.46×** | +4.4 | 8e-04 | 21/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.44×** | +4.2 | 0.002 | 25/46 (A549, KATO III, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | **1.45×** | +4.2 | 0.002 | 21/46 (LoVo, SW1417, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.41×** | +4.0 | 0.003 | 21/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.26×** | +3.9 | 0.006 | 22/47 (HCT15, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.40×** | +3.7 | 0.012 | 17/39 (LS 180, LOX-IMVI, …) | inconsistent across doses | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +3.6 | 0.013 | 20/46 (SNU-423, SW480, …) | top dose only |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.35×** | +3.5 | 0.018 | 16/47 (MIA PaCa-2, SW48, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.33×** | +3.3 | 0.032 | 11/47 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.048 | 17/46 (SW480, SW48, …) | top dose only |  |
| [[Amsacrine (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.075 | 12/47 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.075 | 9/47 (KATO III, SW480, …) | top dose only |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.078 | 15/46 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.084 | 12/47 (HOP62, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7110.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.485×** | -8.5 | 2e-14 | 38/47 (LOX-IMVI, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.603×** | -8.4 | 2e-14 | 31/47 (A498, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.721×** | -5.4 | 1e-05 | 34/47 (HCT15, A-172, …) | rises with dose | position effect removed |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.544×** | -5.1 | 5e-05 | 29/47 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.661×** | -4.8 | 2e-04 | 27/47 (HT-29, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.630×** | -4.4 | 0.001 | 23/47 (LS 180, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.708×** | -4.0 | 0.004 | 26/46 (A498, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.642×** | -3.7 | 0.015 | 18/47 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.722×** | -3.7 | 0.015 | 19/46 (HEC-1-A, A-427, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.681×** | -3.6 | 0.015 | 15/47 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.734×** | -3.6 | 0.015 | 20/46 (SW 1271, SK-MEL-2, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.747×** | -3.4 | 0.031 | 17/46 (HCT15, Panc 03.27, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.802×** | -3.3 | 0.038 | 21/47 (NCI-H1792, MIA PaCa-2, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.818×** | -3.3 | 0.038 | 19/47 (HOP62, BT-474, …) | rises with dose | position effect removed |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.771×** | -3.0 | 0.090 | 17/46 (KATO III, MIA PaCa-2, …) | all doses, flat |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.611×** | -3.0 | 0.093 | 13/44 (SNU-1, H4, …) | top dose only | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.615×** | -3.0 | 0.095 | 12/47 (Hs 766T, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.776×** | -3.0 | 0.095 | 16/45 (Hs 766T, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.96 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7110. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 33.5 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0836× (z -27.4) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -14.6) |
| [[H4 (line)]] | wt | 37.0 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0230× (z -16.6) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0457× (z -13.6) |
| [[LOX-IMVI (line)]] | wt | 20.3 | 0 | 4 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.218× (z -11.9) ⚠ cell-cycle shift, explains ~69% of this change |
| [[A-172 (line)]] | wt | 23.7 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.251× (z -11.1) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM 0.153× (z -10.7) |
| [[A-427 (line)]] | wt | 48.2 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.191× (z -17.4) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.225× (z -11.1) |
| [[LS 180 (line)]] | wt | 16.2 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0744× (z -18.6) ⚠ cell-cycle shift, explains ~69% of this change |
| [[PANC-1 (line)]] | alt | 39.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +11.9) ⚠ cell-cycle shift, explains ~38% of this change | [[Dinaciclib (drug)]] 5 µM 0.287× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 43.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.1) ⚠ cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 21.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +10.0) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[C32 (line)]] | wt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0312× (z -17.1) ⚠ cell-cycle shift, explains ~89% of this change |
| [[Hs 766T (line)]] | wt | 25.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.282× (z -11.3) ⚠ cell-cycle shift, explains ~69% of this change |
| [[J82 (line)]] | alt | 73.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.368× (z -8.5) ⚠ cell-cycle shift, explains ~69% of this change |
| [[MIA PaCa-2 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 11.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.39× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 28.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +11.5) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H460 (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.323× (z -10.0) ⚠ cell-cycle shift, explains ~69% of this change |
| [[Panc 03.27 (line)]] | alt | 35.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +8.5) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -10.0) |
| [[SNU-423 (line)]] | alt | 23.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +8.9) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SW1417 (line)]] | alt | 50.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +8.7) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SW48 (line)]] | wt | 30.4 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0641× (z -13.1) ⚠ cell-cycle shift, explains ~90% of this change |
| [[AN3 CA (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.23 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7110), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPO]] | +0.88 | +0.87 / +0.90 | both halves | 7e-06 | pathway: Mitotic Anaphase; STRING 455 |
| [[POLQ]] | +0.86 | +0.88 / +0.84 | both halves | 7e-06 | STRING 412 |
| [[SPC25]] | +0.86 | +0.87 / +0.86 | both halves | 7e-06 | pathway: Mitotic Anaphase; STRING 625 |
| [[HAUS8]] | +0.85 | +0.80 / +0.86 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[SHCBP1]] | +0.85 | +0.87 / +0.83 | both halves | 7e-06 | STRING 583 |
| [[ATAD5]] | +0.84 | +0.82 / +0.84 | both halves | 7e-06 |  |
| [[MELK]] | +0.84 | +0.86 / +0.83 | both halves | 7e-06 | STRING 875 |
| [[RAD51]] | +0.84 | +0.86 / +0.83 | both halves | 7e-06 | STRING 568 |
| [[EXO1]] | +0.84 | +0.85 / +0.81 | both halves | 7e-06 | STRING 663 |
| [[BLM]] | +0.84 | +0.89 / +0.81 | both halves | 7e-06 |  |
| [[DDIAS]] | +0.83 | +0.76 / +0.84 | both halves | 7e-06 | STRING 504 |
| [[STIL]] | +0.83 | +0.84 / +0.86 | both halves | 7e-06 | STRING 404 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises CDCA5's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.90× lower at baseline in the lines without CDC25A | 0.025 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CDCA5's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TCF19]] | B | TCF19 activity raises CDCA5's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.49× lower at baseline in the lines without TCF19 | 0.040 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises CDCA5's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.07× lower at baseline in the lines without E2F8 | 0.041 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[PBK]] | C | PBK activity raises CDCA5's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.49× lower at baseline in the lines without PBK | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[ZNF367]] | C | ZNF367 activity raises CDCA5's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 1.94× lower at baseline in the lines without ZNF367 | 0.059 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises CDCA5's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.53× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[DSCC1]] | C | DSCC1 activity raises CDCA5's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.09× lower at baseline in the lines without DSCC1 | 0.067 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises CDCA5's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.59× lower at baseline in the lines without AURKB | 0.071 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises CDCA5's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 1.82× lower at baseline in the lines without MCM10 | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.917). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.3, -48.4); signed map (-41.5, -43.3). **Vector** length 136, 44.3% of its response variance represented; |z| ≥ 3 in 1,120 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *IP3 and IP4 transport between cytosol and nucleus* (reactome, mean cos +0.51 to 4); *IP6 and IP7 transport between cytosol and nucleus* (reactome, mean cos +0.51 to 4); *IPs transport between nucleus and cytosol* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.8 | +9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +4.0 | +3.3 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +3.9 | +4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.7 | +3.6 |
|  | [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +3.6 | +4.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +2.3 | +3.0 |
|  | [[Methotrexate (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.0 | +2.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.9 | +3.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -8.1 | -8.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -7.1 | -8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.1 | +0.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.8 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -4.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.7 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.4 | -2.8 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.4 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle associated 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,066,300-65,084,164 (-) |
| Ensembl biotype | protein_coding |
| Reactome | 10 pathways, smallest: Establishment of Sister Chromatid Cohesion; Resolution of Sister Chromatid Cohesion; S Phase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FF9](https://www.uniprot.org/uniprotkb/Q96FF9) (Sororin):

> Regulator of sister chromatid cohesion in mitosis, stabilizing cohesin complex association with chromatin. May antagonize the action of WAPL which stimulates cohesin dissociation from chromatin. Cohesion ensures that chromosome partitioning is accurate in both meiotic and mitotic cells and plays an important role in DNA repair. Required for efficient DNA double-stranded break repair.

**Summary**, from NCBI Gene [113130](https://www.ncbi.nlm.nih.gov/gene/113130):

> Predicted to enable chromatin binding activity. Involved in double-strand break repair and mitotic sister chromatid cohesion. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14626](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14626) · Entrez [113130](https://www.ncbi.nlm.nih.gov/gene/113130) · UniProt [Q96FF9](https://www.uniprot.org/uniprotkb/Q96FF9) · Ensembl [ENSG00000146670](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146670)

## Data

Gene col 7110: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7110); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7110, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7110]; `tensor/DDL_lfc|DDL_z.npy` [7110]; `embed/gene_vectors.npy` [7110]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7110 or target_col == 7110). Every well: [[CDCA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDCA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
