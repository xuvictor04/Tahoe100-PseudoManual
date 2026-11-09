---
symbol: "CHAF1A"
type: "gene"
col: 9514
ensembl_id: "ENSG00000167670"
name: "chromatin assembly factor 1 subunit A"
location: "19p13.3"
module: 6
arm: "+"
pooled_cpm: 38.12
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CHAF1A

*chromatin assembly factor 1 subunit A* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (25 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +9.5, q 8e-19, up in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~56% of this change. The strongest without an alert is [[venetoclax (drug)]] 0.05 µM: 1.26× (z +3.4, q 0.014, up in 8 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.672× (z -8.9, q 2e-16, down in 30 of 48 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.680× (z -6.1, q 2e-07, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC45]] (+0.91, fdr 7e-06), [[EXO1]] (+0.89, fdr 7e-06), [[RAD54L]] (+0.89, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 26 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 25 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9514.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.53×** | +9.5 | 8e-19 | 31/48 (A549, J82, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.78×** | +9.2 | 1e-17 | 36/47 (PANC-1, SHP-77, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.69×** | +8.3 | 2e-14 | 39/48 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.71×** | +8.2 | 2e-14 | 32/39 (SW1417, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.68×** | +8.2 | 2e-14 | 35/48 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.63×** | +7.7 | 1e-12 | 29/44 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.62×** | +7.6 | 2e-12 | 32/48 (LOX-IMVI, SW480, …) | two highest doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.60×** | +7.1 | 6e-11 | 29/47 (J82, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.56×** | +7.1 | 8e-11 | 32/47 (PANC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.55×** | +6.9 | 2e-10 | 36/48 (LOX-IMVI, HS-578T, …) | two highest doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.50×** | +6.5 | 5e-09 | 29/46 (J82, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.41×** | +5.5 | 2e-06 | 29/48 (PANC-1, SHP-77, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.41×** | +5.2 | 8e-06 | 24/48 (SW480, HS-578T, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.26×** | +5.2 | 8e-06 | 24/48 (SNU-1, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.36×** | +4.9 | 3e-05 | 24/47 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.014 | 8/48 (AsPC-1, HOP62, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.014 | 12/47 (A-427, HCT15, …) | all doses, flat |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.025 | 13/48 (MIA PaCa-2, COLO 205, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.043 | 12/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift |
| [[Vilanterol (drug)]] 5 µM |  | 1.14× | +2.9 | 0.060 | 6/48 (HT-29, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9514.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.672×** | -8.9 | 2e-16 | 30/48 (A498, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.680×** | -6.1 | 2e-07 | 24/48 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.685×** | -6.0 | 3e-07 | 27/48 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.615×** | -5.5 | 5e-06 | 27/48 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.744×** | -4.7 | 3e-04 | 24/48 (HOP62, LS 180, …) | two highest doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.818×** | -4.5 | 6e-04 | 21/48 (COLO 205, HCT15, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.828×** | -4.3 | 0.002 | 19/48 (RKO, HCT15, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.844× | -3.8 | 0.009 | 20/48 (A-172, LS 180, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.787×** | -3.8 | 0.009 | 19/47 (LS 180, SK-MEL-2, …) | two highest doses | low cells (technical?) |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.719×** | -3.7 | 0.010 | 15/48 (RKO, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.776×** | -3.6 | 0.020 | 17/48 (A-427, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.801×** | -3.3 | 0.049 | 13/48 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.754×** | -3.2 | 0.058 | 14/48 (SW480, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.665×** | -3.1 | 0.073 | 14/48 (Hs 766T, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.825×** | -3.1 | 0.084 | 7/48 (RKO, AsPC-1, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.874× | -3.0 | 0.084 | 13/48 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[palbociclib (drug)]] 5 µM |  | **0.677×** | -3.0 | 0.091 | 16/47 (SW480, COLO 205, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.872× | -3.0 | 0.091 | 15/48 (A-427, NCI-H23, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 0.05 µM |  | **0.832×** | -2.9 | 0.100 | 13/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.01 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9514. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 64.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0507× (z -25.4) |
| [[A498 (line)]] | wt | 46.5 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.264× (z -16.7) ⚠ cell-cycle shift, explains ~50% of this change |
| [[J82 (line)]] | alt | 72.5 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +15.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 54.3 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.232× (z -15.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[MIA PaCa-2 (line)]] | alt | 46.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.254× (z -9.7) |
| [[PANC-1 (line)]] | alt | 26.9 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +9.8) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[A549 (line)]] | wt | 18.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +10.0) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[AN3 CA (line)]] | alt | 58.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 31.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0964× (z -16.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 11.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HS-578T (line)]] | alt | 22.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.382× (z -9.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[LOX-IMVI (line)]] | wt | 23.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.396× (z -8.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H2030 (line)]] | alt | 31.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +9.3) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[NCI-H23 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 23.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +8.9) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[SHP-77 (line)]] | alt | 64.0 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +9.2) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[SNU-423 (line)]] | alt | 33.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +8.6) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[SW48 (line)]] | wt | 47.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.199× (z -10.2) ⚠ cell-cycle shift, explains ~91% of this change |
| [[AsPC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 105 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 56.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 52.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9514), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC45]] | +0.91 | +0.90 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 595 |
| [[EXO1]] | +0.89 | +0.90 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 586 |
| [[RAD54L]] | +0.89 | +0.84 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 600 |
| [[DTL]] | +0.89 | +0.89 / +0.88 | both halves | 7e-06 | STRING 410 |
| [[ATAD5]] | +0.88 | +0.86 / +0.90 | both halves | 7e-06 | STRING 524 |
| [[RAD51]] | +0.88 | +0.83 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[FANCA]] | +0.88 | +0.87 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[MCM10]] | +0.88 | +0.90 / +0.86 | both halves | 7e-06 | STRING 456 |
| [[CLSPN]] | +0.88 | +0.87 / +0.88 | both halves | 7e-06 | STRING 493 |
| [[WDR76]] | +0.88 | +0.89 / +0.84 | both halves | 7e-06 |  |
| [[FANCI]] | +0.88 | +0.85 / +0.88 | both halves | 7e-06 | STRING 495 |
| [[E2F2]] | +0.87 | +0.86 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises CHAF1A's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.95× lower at baseline in the lines without E2F2 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises CHAF1A's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.16× lower at baseline in the lines without CDC25A | 0.033 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises CHAF1A's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.11× lower at baseline in the lines without TCF19 | 0.052 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[FAM111B]] | B | FAM111B activity raises CHAF1A's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.45× lower at baseline in the lines without FAM111B | 0.064 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers CHAF1A's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF66]] | B | ZNF66 activity raises CHAF1A's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 1.24× lower at baseline in the lines without ZNF66 | 0.072 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[DSCC1]] | C | DSCC1 activity raises CHAF1A's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.31× lower at baseline in the lines without DSCC1 | 0.022 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.899). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.2, -45.7); signed map (-38.9, -44.8). **Vector** length 132, 43.3% of its response variance represented; |z| ≥ 3 in 1,248 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.68 to 65); *DNA strand elongation* (reactome, mean cos +0.74 to 28); *DNA Replication* (reactome, mean cos +0.73 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +5.3 | +7.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | +5.2 | +9.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~96% of this change | +4.8 | +4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +4.5 | +8.3 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.4 | +3.0 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.2 | +3.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.1 | +3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.7 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +2.6 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +2.6 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -8.2 | -8.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -6.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | -5.6 | -6.0 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -4.8 | -5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.1 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -3.8 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.6 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | chromatin assembly factor 1 subunit A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,402,640-4,445,018 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAF1P150, CAF1B, CAF-1, CAF1, P150, MGC71229 |
| Hallmark sets | G2M_CHECKPOINT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13111](https://www.uniprot.org/uniprotkb/Q13111) (Chromatin assembly factor 1 subunit A):

> Acts as a component of the histone chaperone complex chromatin assembly factor 1 (CAF-1), which assembles histone octamers onto DNA during replication and repair. CAF-1 performs the first step of the nucleosome assembly process, bringing newly synthesized histones H3 and H4 to replicating DNA; histones H2A/H2B can bind to this chromatin precursor subsequent to DNA replication to complete the histone octamer. It may play a role in heterochromatin maintenance in proliferating cells by bringing …

**Summary**, from NCBI Gene [10036](https://www.ncbi.nlm.nih.gov/gene/10036):

> Chromatin assembly factor I (CAF1) is a nuclear complex consisting of p50, p60 (CHAF1B; MIM 601245), and p150 (CHAF1A) subunits that assembles histone octamers onto replicating DNA in vitro (Kaufman et al., 1995 [PubMed 7600578]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:1910](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1910) · Entrez [10036](https://www.ncbi.nlm.nih.gov/gene/10036) · UniProt [Q13111](https://www.uniprot.org/uniprotkb/Q13111) · Ensembl [ENSG00000167670](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167670)

## Data

Gene col 9514: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9514); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9514, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9514]; `tensor/DDL_lfc|DDL_z.npy` [9514]; `embed/gene_vectors.npy` [9514]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9514 or target_col == 9514). Every well: [[CHAF1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHAF1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
