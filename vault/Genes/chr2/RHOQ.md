---
symbol: "RHOQ"
type: "gene"
col: 4114
ensembl_id: "ENSG00000119729"
name: "ras homolog family member Q"
location: "2p21"
module: 60
arm: "+"
pooled_cpm: 65.83
n_lines_expressing: 47
n_dd_up: 26
n_dd_down: 14
n_dd_up_clean: 20
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# RHOQ

*ras homolog family member Q* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.60× (z +8.5, q 1e-14, up in 37 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.539× (z -11.3, q 1e-26, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AAK1]] (+0.61, fdr 7e-06), [[RHOQ-AS1]] (+0.59, fdr 1e-05, ⚠ same locus), [[MAP4]] (+0.58, fdr 1e-05), [[ATP2C1]] (+0.56, fdr 1e-05); moves opposite to [[CHAMP1]] (-0.54, fdr 1e-05), [[ZFHX3-AS1]] (-0.51, fdr 1e-05), [[NOL11]] (-0.51, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MYO15B]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SLC22A23]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4114.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +8.5 | 1e-14 | 37/45 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.39×** | +8.4 | 2e-14 | 34/46 (SHP-77, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.52×** | +7.1 | 2e-10 | 36/45 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +6.8 | 2e-09 | 29/45 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +6.6 | 5e-09 | 30/45 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.44×** | +6.6 | 5e-09 | 33/45 (SHP-77, HepG2/C3A, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.42×** | +6.1 | 1e-07 | 28/44 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +5.4 | 4e-06 | 25/45 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +5.4 | 5e-06 | 27/45 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.34×** | +5.3 | 7e-06 | 28/44 (SHP-77, BT-474, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +5.1 | 2e-05 | 21/46 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.32×** | +5.0 | 3e-05 | 26/45 (BT-474, SHP-77, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +4.8 | 5e-05 | 23/45 (NCI-H2030, A-427, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.30×** | +4.7 | 1e-04 | 22/44 (NCI-H460, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | **1.31×** | +4.7 | 1e-04 | 25/44 (SHP-77, BT-474, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 2e-04 | 21/44 (BT-474, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +4.2 | 9e-04 | 18/45 (SNU-423, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.18× | +4.1 | 0.001 | 20/45 (LoVo, HT-29, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.009 | 17/44 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.010 | 16/46 (NCI-H460, A-427, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4114.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.539×** | -11.3 | 1e-26 | 32/45 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.529×** | -11.2 | 2e-26 | 38/45 (LOX-IMVI, C32, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.674×** | -10.2 | 4e-22 | 32/45 (LOX-IMVI, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.631×** | -8.4 | 6e-15 | 30/45 (SHP-77, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.652×** | -7.8 | 7e-13 | 32/45 (C32, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.678×** | -7.1 | 1e-10 | 27/45 (HOP62, HS-578T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.693×** | -6.4 | 1e-08 | 29/44 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.814×** | -5.4 | 6e-06 | 23/45 (RPMI-7951, NCI-H1792, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.751×** | -5.2 | 9e-06 | 30/45 (SW48, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.751×** | -5.2 | 9e-06 | 24/45 (SHP-77, A549, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.761×** | -4.6 | 2e-04 | 25/44 (A549, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.634×** | -3.7 | 0.008 | 15/44 (H4, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.803×** | -3.7 | 0.008 | 21/43 (RKO, A-172, …) | inconsistent across doses | composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **0.817×** | -3.7 | 0.009 | 16/45 (HOP62, HepG2/C3A, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | 0.871× | -3.6 | 0.012 | 12/45 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.838× | -3.3 | 0.037 | 16/45 (HT-29, HOP62, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.846× | -3.0 | 0.094 | 20/45 (hTERT-HPNE, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4114. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 123 | 3 (1 ⚠) | 4 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 3.34× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.6) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.382× (z -10.3) |
| [[C32 (line)]] | wt | 120 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -15.0) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.301× (z -12.9) |
| [[A549 (line)]] | wt | 120 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -17.7) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.274× (z -13.8) |
| [[HT-29 (line)]] | alt | 62.9 | 1 | 3 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.19× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -9.4) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.335× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 95.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -23.2) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.352× (z -12.0) |
| [[BT-474 (line)]] | alt | 34.7 | 1 | 2 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.63× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.9) ⚠ cell-cycle shift, explains ~59% of this change |
| [[HS-578T (line)]] | alt | 99.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -14.8) |
| [[NCI-H1573 (line)]] | alt | 37.9 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -10.4) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 64.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -17.4) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.332× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 75.4 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 34.6 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -9.3) ⚠ cell-cycle shift, explains ~59% of this change |
| [[RKO (line)]] | wt | 80.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.326× (z -10.8) |
| [[A-172 (line)]] | wt | 153 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 219 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 43.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -10.0) ⚠ cell-cycle shift, explains ~59% of this change |
| [[NCI-H460 (line)]] | wt | 90.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.93× (z +10.5) | — |
| [[SW48 (line)]] | wt | 63.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -13.6) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -11.1) |
| [[C-33 A (line)]] | alt | 57.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 17.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +11.0) | — |
| [[HepG2_C3A (line)]] | wt | 40.6 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.60× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.401× (z -8.5) ⚠ cell-cycle shift, explains ~48% of this change |
| [[J82 (line)]] | alt | 53.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +8.5) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[LS 180 (line)]] | wt | 20.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.82× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 49.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 118 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.421× (z -8.7) |
| [[SNU-1 (line)]] | wt | 85.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -9.9) ⚠ cell-cycle shift, explains ~59% of this change |
| [[SW 900 (line)]] | alt | 83.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -11.5) ⚠ cell-cycle shift, explains ~59% of this change |
| [[SW1417 (line)]] | alt | 37.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.341× (z -9.5) |
| [[A-427 (line)]] | wt | 88.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.89 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 31.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4114), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AAK1]] | +0.61 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[RHOQ-AS1]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[MAP4]] | +0.58 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ATP2C1]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CTIF]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[LARP6]] | +0.55 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[MROH1]] | +0.54 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[SNX3]] | +0.54 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[LIMK1]] | +0.53 | +0.57 / +0.57 | both halves | 1e-05 | pathway: RHO GTPase Effectors |
| [[SLC25A29]] | +0.53 | +0.73 / +0.45 | both halves | 3e-05 |  |
| [[GAB2]] | +0.52 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[PLEKHO1]] | +0.52 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[RELL2]] | +0.51 | +0.39 / +0.51 | both halves | 5e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHAMP1]] | -0.54 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[ZFHX3-AS1]] | -0.51 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[NOL11]] | -0.51 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[RBM22]] | -0.50 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[RBM8A]] | -0.49 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[CRADD]] | -0.48 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[ABT1]] | -0.48 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[ZNF414]] | -0.48 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ZNF136]] | -0.47 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[MAP3K1]] | -0.47 | -0.28 / -0.59 | both halves | 3e-04 |  |
| [[CWC22]] | -0.47 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[ZNF518A]] | -0.47 | -0.58 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO15B]] | B | MYO15B activity lowers RHOQ's level | lines that do not express MYO15B (5) vs lines expressing it (45) | 1.61× higher at baseline in the lines without MYO15B | 0.060 | ⚠ within organs, on part of the lines; also absent: ID2, ASRGL1, CTNNA3; maybe low, not absent; its own permutation p |
| [[ATP8B2]] | B | ATP8B2 activity raises RHOQ's level | lines that do not express ATP8B2 (10) vs lines expressing it (40) | 2.48× lower at baseline in the lines without ATP8B2 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: CRIP2, NRSN2, TTC28 |
| [[PLEKHO1]] | B | PLEKHO1 activity raises RHOQ's level | lines that do not express PLEKHO1 (13) vs lines expressing it (37) | 2.13× lower at baseline in the lines without PLEKHO1 | 0.083 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |
| [[ASAP3]] | C | ASAP3 activity raises RHOQ's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 4.53× lower at baseline in the lines without ASAP3 | 0.020 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC22A23]] | C | RHOQ activity lowers SLC22A23's level | lines that do not express RHOQ (3) vs lines expressing it (47) | 2.70× higher at baseline in the lines without RHOQ | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: DPF1, TBC1D19, ARHGEF26; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.399). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-12.2, 11.2); signed map (-12.2, 19.1). **Vector** length 129, 37.4% of its response variance represented; |z| ≥ 3 in 1,227 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.3 | +6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | +8.1 | +7.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.1 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.4 | +6.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.9 | +8.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.7 | +3.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -7.1 | -11.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.1 | -7.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -4.3 | -10.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.9 | -4.6 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -2.9 | -1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ras homolog family member Q |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:46,541,806-46,584,688 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TC10; previously RASL7A, ARHQ |
| Gene groups (HGNC) | Rho family GTPases |
| Reactome | 9 pathways, smallest: RHO GTPases regulate CFTR trafficking; RHOQ GTPase cycle; Translocation of SLC2A4 (GLUT4) to the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [P17081](https://www.uniprot.org/uniprotkb/P17081) (Rho-related GTP-binding protein RhoQ):

> Plasma membrane-associated small GTPase which cycles between an active GTP-bound and an inactive GDP-bound state. In active state binds to a variety of effector proteins to regulate cellular responses. Involved in epithelial cell polarization processes. May play a role in CFTR trafficking to the plasma membrane. Causes the formation of thin, actin-rich surface projections called filopodia.

**Summary**, from NCBI Gene [23433](https://www.ncbi.nlm.nih.gov/gene/23433):

> This gene encodes a member of the Rho family of small GTPases, which cycle between inactive GDP-bound and active GTP-bound states and function as molecular switches in signal transduction cascades. Rho proteins promote reorganization of the actin cytoskeleton and regulate cell shape, attachment, and motility. The encoded protein is an important signalling protein for sarcomere assembly and has been shown to play a significant role in the exocytosis of the solute carrier family 2, facilitated …

**Accessions** — [HGNC:17736](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17736) · Entrez [23433](https://www.ncbi.nlm.nih.gov/gene/23433) · UniProt [P17081](https://www.uniprot.org/uniprotkb/P17081) · Ensembl [ENSG00000119729](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119729)

## Data

Gene col 4114: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4114); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4114, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4114]; `tensor/DDL_lfc|DDL_z.npy` [4114]; `embed/gene_vectors.npy` [4114]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4114 or target_col == 4114). Every well: [[RHOQ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHOQ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
