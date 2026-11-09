---
symbol: "SLC11A2"
type: "gene"
col: 3178
ensembl_id: "ENSG00000110911"
name: "solute carrier family 11 member 2"
location: "12q13.12"
module: 45
arm: "+"
pooled_cpm: 59.45
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 21
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# SLC11A2

*solute carrier family 11 member 2* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Radotinib (drug)]] 5 µM: 1.20× (z +4.7, q 0.001, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.536× (z -12.7, q 4e-34, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPFIBP2]] (+0.64, fdr 8e-06), [[PKDCC]] (+0.63, fdr 1e-05), [[PIK3C2B]] (+0.61, fdr 9e-06); moves opposite to [[KPNA4]] (-0.67, fdr 7e-06), [[GATAD2A]] (-0.61, fdr 1e-05), [[ZNF731P]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HNF1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3178.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **1.20×** | +4.7 | 0.001 | 20/48 (AsPC-1, SW1417, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +4.6 | 0.001 | 22/47 (NCI-H1792, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.23×** | +4.2 | 0.003 | 18/48 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.17× | +4.2 | 0.003 | 21/48 (A-172, AsPC-1, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +4.0 | 0.009 | 18/48 (CFPAC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Fumaric acid (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.009 | 14/49 (HT-29, NCI-H1573, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.009 | 20/48 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.19× | +3.6 | 0.022 | 18/48 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 1.19× | +3.4 | 0.046 | 10/48 (NCI-H2030, HT-29, …) | rises with dose |  |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.091 | 3/49 (C-33 A, NCI-H2122, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.13× | +3.1 | 0.094 | 8/48 (A-172, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.17× | +3.1 | 0.10 | 19/48 (J82, HOP62, …) | top dose only | composition shift |
| [[Capmatinib (drug)]] 0.5 µM |  | 1.24× | +3.0 | 0.11 | 5/49 (SW480, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3178.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.536×** | -12.7 | 4e-34 | 39/48 (SNU-423, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.534×** | -12.3 | 3e-32 | 31/41 (NCI-H1573, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.588×** | -10.0 | 3e-21 | 37/45 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.647×** | -8.9 | 1e-16 | 35/48 (NCI-H1573, A498, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.676×** | -8.0 | 2e-13 | 29/48 (A498, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.688×** | -7.6 | 2e-12 | 35/48 (HepG2/C3A, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.800×** | -6.0 | 1e-07 | 25/49 (A549, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.750×** | -5.8 | 4e-07 | 22/48 (COLO 205, HT-29, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.821×** | -5.2 | 2e-05 | 23/48 (HepG2/C3A, A549, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.771×** | -5.1 | 2e-05 | 24/50 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.790×** | -4.8 | 8e-05 | 23/48 (HepG2/C3A, A498, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.814×** | -4.2 | 0.001 | 21/48 (HT-29, SW 1088, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.797×** | -4.1 | 0.002 | 16/48 (A498, A549, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.802×** | -4.0 | 0.003 | 17/49 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.826×** | -3.9 | 0.004 | 17/48 (NCI-H1573, J82, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.837× | -3.6 | 0.008 | 12/48 (NCI-H1573, SW 900, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.853× | -3.2 | 0.034 | 19/49 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.883× | -3.1 | 0.045 | 11/48 (PANC-1, HOP62, …) | top dose only |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.841× | -3.1 | 0.045 | 8/49 (SW 900, NCI-H2122, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.843× | -3.1 | 0.052 | 10/48 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.845× | -3.0 | 0.056 | 9/49 (J82, A498, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.811×** | -3.0 | 0.065 | 14/48 (COLO 205, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.758×** | -2.9 | 0.067 | 13/48 (MIA PaCa-2, SW48, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3178. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 43.5 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +15.5) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 4.28× (z +11.4) | — |
| [[A498 (line)]] | wt | 104 | 1 (1 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +11.0) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HepG2_C3A (line)]] | wt | 189 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.218× (z -12.3) ⚠ toxic; cell-cycle shift, explains ~77% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.426× (z -9.8) |
| [[HT-29 (line)]] | alt | 78.9 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.412× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 116 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0530× (z -25.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 60.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.453× (z -11.4) |
| [[COLO 205 (line)]] | alt | 112 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -11.1) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.285× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 86.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HS-578T (line)]] | alt | 55.5 | 2 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.93× (z +8.7) ⚠ cell-cycle shift, explains ~5% of this change | [[Dinaciclib (drug)]] 5 µM 0.228× (z -11.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 60.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +8.5) ⚠ cell-cycle shift, explains ~18% of this change | [[Auranofin (drug)]] 5 µM 0.329× (z -11.0) |
| [[A-172 (line)]] | wt | 50.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +19.6) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[C32 (line)]] | wt | 48.4 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -11.7) ⚠ cell-cycle shift, explains ~53% of this change |
| [[H4 (line)]] | wt | 47.3 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -9.1) ⚠ cell-cycle shift, explains ~53% of this change |
| [[HEC-1-A (line)]] | alt | 49.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +8.7) ⚠ cell-cycle shift, explains ~48% of this change | [[Lonafarnib (drug)]] 5 µM 0.107× (z -12.0) ⚠ toxic |
| [[HOP62 (line)]] | alt | 23.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +12.0) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[J82 (line)]] | alt | 49.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +12.5) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 48.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -12.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 77.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -8.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 72.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -10.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 49.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +12.6) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[C-33 A (line)]] | alt | 43.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[CFPAC-1 (line)]] | alt | 43.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +12.6) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.295× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~77% of this change |
| [[NCI-H2347 (line)]] | alt | 64.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.460× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 67.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -10.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 50.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.462× (z -8.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 46.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -12.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 61.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.199× (z -13.9) |
| [[SW1417 (line)]] | alt | 57.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -13.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 41.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -12.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3178), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPFIBP2]] | +0.64 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[PKDCC]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PIK3C2B]] | +0.61 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[FAM111A-DT]] | +0.60 | +0.46 / +0.69 | both halves | 3e-05 |  |
| [[SNX2]] | +0.59 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[NEURL3]] | +0.58 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[RAB9A]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[TNFAIP2]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[CNNM2]] | +0.57 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[WDSUB1]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[GDPD1]] | +0.57 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[DPM3]] | +0.56 | +0.44 / +0.63 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA4]] | -0.67 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[GATAD2A]] | -0.61 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.61 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[ERVK13-1]] | -0.59 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[PDK1-AS1]] | -0.57 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[PSMD2]] | -0.56 | -0.47 / -0.58 | both halves | 2e-05 | pathway: Disorders of transmembrane transporters |
| [[BZW1]] | -0.55 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[ZNF407]] | -0.55 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[TPM3]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[SEC14L1]] | -0.54 | -0.43 / -0.56 | both halves | 3e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[CD59]] | -0.54 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[RNF32-AS1]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HNF1B]] | B | HNF1B activity raises SLC11A2's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 1.54× lower at baseline in the lines without HNF1B | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[TOP2A]] | B | TOP2A activity raises SLC11A2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DNAJC12]] | B | DNAJC12 activity raises SLC11A2's level | lines that do not express DNAJC12 (25) vs lines expressing it (25) | 1.28× lower at baseline in the lines without DNAJC12 | 0.068 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| [[ANKRD33B]] | B | ANKRD33B activity weakens SLC11A2's drug response | lines that do not express ANKRD33B (15) vs lines expressing it (35) | the lines without ANKRD33B respond 1.62× as strongly (z diff -1.70); strongest at Panobinostat 0.5 µM: 0.55x vs 0.70x (z diff -2.5) | 0.086 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.483). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (32.1, 46.9); signed map (50.0, 2.6). **Vector** length 122, 34.7% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +6.4 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | +4.8 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.8 | +4.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +4.4 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.0 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +1.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.0 | +1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.8 | -12.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -5.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.4 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.1 | -3.9 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -3.1 | -4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.0 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 11 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:50,979,401-51,028,566 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DCT1, DMT1, DMT-1, FLJ37416; previously NRAMP2 |
| Gene groups (HGNC) | Solute carrier family 11 |
| Hallmark sets | INFLAMMATORY_RESPONSE, HEME_METABOLISM |
| Reactome | 6 pathways, smallest: Metal ion SLC transporters; Iron uptake and transport; SLC transporter disorders |
| Matched by | ensembl_id |

**Function**, from UniProt [P49281](https://www.uniprot.org/uniprotkb/P49281) (Natural resistance-associated macrophage protein 2):

> Proton-coupled metal ion symporter operating with a proton to metal ion stoichiometry of 1:1. Selectively transports various divalent metal cations, in decreasing affinity: Cd(2+) > Fe(2+) > Co(2+), Mn(2+) >> Zn(2+), Ni(2+), VO(2+). Essential for maintenance of iron homeostasis by modulating intestinal absorption of dietary Fe(2+) and TF-associated endosomal Fe(2+) transport in erythroid precursors and other cells (By similarity). Enables Fe(2+) and Mn(2+) ion entry into mitochondria, and is …

**Summary**, from NCBI Gene [4891](https://www.ncbi.nlm.nih.gov/gene/4891):

> This gene encodes a member of the solute carrier family 11 protein family. The product of this gene transports divalent metals and is involved in iron absorption. Mutations in this gene are associated with hypochromic microcytic anemia with iron overload. A related solute carrier family 11 protein gene is located on chromosome 2. Multiple transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:10908](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10908) · Entrez [4891](https://www.ncbi.nlm.nih.gov/gene/4891) · UniProt [P49281](https://www.uniprot.org/uniprotkb/P49281) · Ensembl [ENSG00000110911](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110911)

## Data

Gene col 3178: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3178); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3178, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3178]; `tensor/DDL_lfc|DDL_z.npy` [3178]; `embed/gene_vectors.npy` [3178]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3178 or target_col == 3178). Every well: [[SLC11A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC11A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
