---
symbol: "ZNF75D"
type: "gene"
col: 11809
ensembl_id: "ENSG00000186376"
name: "zinc finger protein 75D"
location: "Xq26.3"
module: 179
arm: "+"
pooled_cpm: 51.9
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 34
n_dd_up_clean: 8
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# ZNF75D

*zinc finger protein 75D* — Xq26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +11.9, q 5e-30, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.322× (z -26.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLUD1P3]] (+0.69, fdr 1e-05), [[ISY1]] (+0.61, fdr 1e-05), [[GDAP2]] (+0.60, fdr 7e-06); moves opposite to [[EFR3A]] (-0.57, fdr 1e-05), [[EXOC6]] (-0.56, fdr 1e-05), [[TRMT10B]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 179]] (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FLJ12825]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11809.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +11.9 | 5e-30 | 41/48 (MIA PaCa-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.32×** | +6.5 | 3e-08 | 33/48 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.2 | 1e-07 | 31/48 (HS-578T, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.83×** | +5.2 | 2e-05 | 29/48 (LS 180, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.3 | 0.002 | 24/48 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +4.2 | 0.002 | 24/49 (LoVo, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.35×** | +3.7 | 0.016 | 21/47 (SW1417, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +3.7 | 0.017 | 18/48 (LS 180, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.026 | 12/48 (HT-29, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.5 | 0.026 | 11/48 (A-172, A549, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.22×** | +3.2 | 0.080 | 14/47 (AN3 CA, NCI-H460, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.091 | 15/48 (SNU-423, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 16 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11809.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.322×** | -26.7 | 0e+00 | 47/48 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.378×** | -15.6 | 0e+00 | 44/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.453×** | -13.2 | 2e-37 | 40/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.473×** | -12.5 | 1e-33 | 39/48 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.475×** | -12.4 | 2e-33 | 42/48 (KATO III, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.591×** | -8.8 | 1e-16 | 37/48 (NCI-H460, KATO III, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.607×** | -8.0 | 8e-14 | 26/40 (Panc 03.27, KATO III, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.597×** | -8.0 | 1e-13 | 29/44 (A549, KATO III, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.620×** | -7.7 | 1e-12 | 35/47 (AsPC-1, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.544×** | -7.4 | 8e-12 | 35/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.649×** | -7.2 | 3e-11 | 38/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.655×** | -7.1 | 7e-11 | 34/48 (COLO 205, KATO III, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.671×** | -6.7 | 1e-09 | 29/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.604×** | -6.1 | 4e-08 | 30/47 (KATO III, C-33 A, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.708×** | -5.8 | 3e-07 | 31/48 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.562×** | -5.0 | 2e-05 | 32/48 (NCI-H460, SW 1271, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.817×** | -4.8 | 5e-05 | 27/48 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.587×** | -4.7 | 1e-04 | 24/48 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.766×** | -4.5 | 2e-04 | 25/48 (H4, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.836× | -4.2 | 5e-04 | 20/48 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.622×** | -4.1 | 8e-04 | 23/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.788×** | -3.9 | 0.003 | 21/48 (A498, AN3 CA, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.801×** | -3.7 | 0.004 | 21/48 (CHP-212, COLO 205, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.799×** | -3.6 | 0.006 | 22/48 (A498, A549, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.808×** | -3.6 | 0.007 | 21/48 (MIA PaCa-2, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11809. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 156 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -21.9) |
| [[NCI-H460 (line)]] | wt | 57.0 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -23.6) |
| [[SW480 (line)]] | alt | 67.2 | 3 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -17.4) |
| [[A549 (line)]] | wt | 43.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -21.2) |
| [[HOP62 (line)]] | alt | 64.4 | 1 | 5 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -25.2) |
| [[PANC-1 (line)]] | alt | 65.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -27.5) |
| [[COLO 205 (line)]] | alt | 67.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -15.5) |
| [[HS-578T (line)]] | alt | 32.3 | 2 | 3 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -17.0) |
| [[NCI-H1573 (line)]] | alt | 60.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -25.0) |
| [[SNU-423 (line)]] | alt | 73.1 | 2 | 3 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -28.0) |
| [[SW 900 (line)]] | alt | 53.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -17.5) |
| [[AsPC-1 (line)]] | alt | 71.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -14.0) |
| [[LoVo (line)]] | wt | 50.5 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.01× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -17.1) |
| [[LOX-IMVI (line)]] | wt | 38.9 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 45.1 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +11.1) | [[Tucidinostat (drug)]] 0.5 µM 0.347× (z -9.3) |
| [[A498 (line)]] | wt | 44.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -22.1) |
| [[C32 (line)]] | wt | 37.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -11.6) |
| [[H4 (line)]] | wt | 61.1 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.186× (z -10.6) |
| [[Hs 766T (line)]] | wt | 74.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -14.8) |
| [[HT-29 (line)]] | alt | 72.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -17.2) |
| [[hTERT-HPNE (line)]] | wt | 45.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -12.8) |
| [[NCI-H2030 (line)]] | alt | 49.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -15.3) |
| [[NCI-H23 (line)]] | alt | 58.4 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -13.9) |
| [[Panc 03.27 (line)]] | alt | 47.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.297× (z -15.5) |
| [[SNU-1 (line)]] | wt | 48.6 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.173× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~10% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.241× (z -9.8) |
| [[A-172 (line)]] | wt | 19.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -10.6) |
| [[BT-474 (line)]] | alt | 30.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -9.4) |
| [[C-33 A (line)]] | alt | 36.3 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0482× (z -10.1) ⚠ toxic |
| [[J82 (line)]] | alt | 48.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -17.5) |
| [[NCI-H1792 (line)]] | alt | 33.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -19.6) |
| [[SK-MEL-2 (line)]] | alt | 35.5 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +10.2) | — |
| [[SW 1271 (line)]] | alt | 79.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.123× (z -8.7) |
| [[SW1417 (line)]] | alt | 65.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -12.8) |
| [[A-427 (line)]] | wt | 36.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -16.2) |
| [[CFPAC-1 (line)]] | alt | 27.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -15.0) |
| [[HEC-1-A (line)]] | alt | 44.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -13.7) |
| [[HepG2_C3A (line)]] | wt | 38.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 25.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -9.9) |
| [[RKO (line)]] | wt | 32.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 40.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -15.4) |
| [[AN3 CA (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11809), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLUD1P3]] | +0.69 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ISY1]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[GDAP2]] | +0.60 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[MBTD1]] | +0.59 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[SELENOF]] | +0.59 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PIGG]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[PXDNL]] | +0.57 | +0.32 / +0.57 | both halves | 2e-04 |  |
| [[SDHD]] | +0.56 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[SDF4]] | +0.56 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[ZFC3H1]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[CDK13]] | +0.56 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[RNF139-DT]] | +0.55 | +0.43 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFR3A]] | -0.57 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[EXOC6]] | -0.56 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[TRMT10B]] | -0.53 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[RBFA]] | -0.53 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[HUS1]] | -0.53 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[DGAT2]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[CIAO1]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[LRRC8E]] | -0.50 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[POLM]] | -0.50 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[JUND]] | -0.50 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[PIM3]] | -0.50 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[VPS8]] | -0.50 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FLJ12825]] | B | FLJ12825 activity raises ZNF75D's level | lines that do not express FLJ12825 (15) vs lines expressing it (35) | 1.28× lower at baseline in the lines without FLJ12825 | 0.008 | ⚠ within organs, on part of the lines; also absent: HOXC10, HOXC6, HOXC8; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ZNF75D's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | ZNF75D's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | ZNF75D's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66 | 0.352 over the table, 0.029 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Citalopram (hydrobromide) (drug)]] 0.05 µM | C | ZNF75D's natural level raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | ZNF75D's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64 | 0.390 over the table, 0.092 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-12.7, 1.7); signed map (-3.1, -2.4). **Vector** length 103, 29.6% of its response variance represented; |z| ≥ 3 in 1,267 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +11.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.6 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.7 | +5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +6.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | -1.2 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.0 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.3 | -26.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.1 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.3 | -13.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.6 | -3.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -15.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -6.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 75D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.3 — chrX:135,248,920-135,344,109 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZKSCAN24, D8C6, ZSCAN28; previously ZNF82, ZNF75 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P51815](https://www.uniprot.org/uniprotkb/P51815) (Zinc finger protein 75D):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7626](https://www.ncbi.nlm.nih.gov/gene/7626):

> This gene encodes a protein that likely functions as a transcription factor. The protein, which belongs to the ZNF75 family, includes an N-terminal SCAN domain, a KRAB box, and five C2H2-type zinc finger motifs. Another functional gene belonging to this family is located on chromosome 16, while pseudogenes have been identified on chromosomes 11 and 12. Alternative splicing results in multiple transcripts variants. [provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:13145](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13145) · Entrez [7626](https://www.ncbi.nlm.nih.gov/gene/7626) · UniProt [P51815](https://www.uniprot.org/uniprotkb/P51815) · Ensembl [ENSG00000186376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186376)

## Data

Gene col 11809: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11809); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11809, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11809]; `tensor/DDL_lfc|DDL_z.npy` [11809]; `embed/gene_vectors.npy` [11809]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11809 or target_col == 11809). Every well: [[ZNF75D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF75D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
