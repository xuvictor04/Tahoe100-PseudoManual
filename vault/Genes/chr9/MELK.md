---
symbol: "MELK"
type: "gene"
col: 9105
ensembl_id: "ENSG00000165304"
name: "maternal embryonic leucine zipper kinase"
location: "9p13.2"
module: 6
arm: "+"
pooled_cpm: 57.07
n_lines_expressing: 47
n_dd_up: 20
n_dd_down: 19
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 15
direction_downstream: 56
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MELK

*maternal embryonic leucine zipper kinase* — 9p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (17 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.63× (z +7.7, q 6e-12, up in 31 of 45 measured lines) ⚠ cell-cycle shift, explains ~74% of this change. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 0.5 µM: 1.28× (z +4.0, q 0.003, up in 18 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.581× (z -12.1, q 4e-31, down in 35 of 45 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.666× (z -9.1, q 2e-17, down in 26 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPK]] (+0.93, fdr 7e-06), [[POLQ]] (+0.93, fdr 7e-06), [[SPC25]] (+0.92, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); 56 go from it, the strongest it → [[CENPP]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 18 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9105.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.63×** | +7.7 | 6e-12 | 31/45 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **1.57×** | +7.1 | 3e-10 | 30/44 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.59×** | +7.0 | 3e-10 | 27/45 (SW480, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.53×** | +6.8 | 2e-09 | 28/45 (PANC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.50×** | +6.2 | 6e-08 | 30/45 (SW480, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.46×** | +6.0 | 2e-07 | 32/44 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.44×** | +5.8 | 7e-07 | 26/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.41×** | +5.5 | 3e-06 | 25/45 (H4, A549, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~84% of this change | **1.43×** | +5.4 | 4e-06 | 26/44 (A549, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.37×** | +5.0 | 3e-05 | 22/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.21×** | +4.3 | 8e-04 | 19/45 (NCI-H23, SW48, …) | rises with dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.35×** | +4.3 | 9e-04 | 17/45 (SW48, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.31×** | +4.3 | 9e-04 | 17/45 (A549, LoVo, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.29×** | +4.0 | 0.002 | 20/45 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.003 | 18/45 (SW480, PANC-1, …) | rises with dose |  |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.015 | 14/45 (SW480, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.14× | +3.0 | 0.077 | 2/45 (SHP-77, SW 1271) | top dose only |  |
| [[Methotrexate (drug)]] 5 µM |  | **1.20×** | +2.9 | 0.094 | 8/45 (SW480, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9105.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.581×** | -12.1 | 4e-31 | 35/45 (LS 180, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.515×** | -9.4 | 2e-18 | 36/45 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.666×** | -9.1 | 2e-17 | 26/45 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.568×** | -8.0 | 2e-13 | 33/45 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.659×** | -6.6 | 5e-09 | 28/45 (HEC-1-A, A-427, …) | top dose only |  |
| [[palbociclib (drug)]] 5 µM |  | **0.483×** | -6.0 | 2e-07 | 26/44 (PANC-1, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.591×** | -5.9 | 3e-07 | 30/45 (SW480, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.626×** | -4.6 | 4e-04 | 25/45 (A-172, SNU-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.711×** | -4.5 | 4e-04 | 26/45 (Hs 766T, A498, …) | all doses, stronger at high dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.775×** | -4.0 | 0.003 | 20/45 (A-172, RKO, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.839× | -3.9 | 0.004 | 14/45 (LoVo, Hs 766T, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.852× | -3.6 | 0.017 | 14/45 (COLO 205, KATO III, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.823×** | -3.6 | 0.017 | 17/45 (A-427, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.796×** | -3.5 | 0.021 | 19/43 (H4, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.737×** | -3.4 | 0.022 | 19/45 (MIA PaCa-2, NCI-H23, …) | all doses, flat | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.788×** | -3.4 | 0.027 | 17/44 (hTERT-HPNE, CHP-212, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.669×** | -3.3 | 0.029 | 18/44 (A498, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.782×** | -3.3 | 0.033 | 16/45 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.864× | -3.3 | 0.033 | 14/45 (SNU-423, HOP62, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.866× | -3.2 | 0.038 | 14/45 (CFPAC-1, NCI-H2030, …) | top dose only |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.754×** | -3.2 | 0.039 | 13/45 (Hs 766T, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.684×** | -3.1 | 0.044 | 18/43 (LS 180, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.89 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9105. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 97.5 | 0 | 8 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.279× (z -16.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -12.4) |
| [[H4 (line)]] | wt | 71.2 | 0 | 7 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.181× (z -11.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.188× (z -11.3) |
| [[A-172 (line)]] | wt | 75.9 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.269× (z -13.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.413× (z -9.3) |
| [[A-427 (line)]] | wt | 82.8 | 0 | 5 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.337× (z -14.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.252× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 163 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.320× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 96.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -12.4) |
| [[LOX-IMVI (line)]] | wt | 52.8 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.270× (z -12.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[LS 180 (line)]] | wt | 36.6 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.118× (z -17.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.241× (z -11.9) |
| [[PANC-1 (line)]] | alt | 120 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +11.2) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[HCT15 (line)]] | alt | 95.7 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.316× (z -10.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.371× (z -9.0) |
| [[HOP62 (line)]] | alt | 63.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -12.4) |
| [[Hs 766T (line)]] | wt | 45.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -11.1) |
| [[SW480 (line)]] | alt | 67.5 | 1 (1 ⚠) | 1 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +8.5) ⚠ cell-cycle shift, explains ~83% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.411× (z -8.6) |
| [[C-33 A (line)]] | alt | 83.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.368× (z -8.8) |
| [[KATO III (line)]] | alt | 55.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -9.7) |
| [[LoVo (line)]] | wt | 31.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.376× (z -10.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H2030 (line)]] | alt | 47.1 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.343× (z -9.3) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 35.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.420× (z -9.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SK-MEL-2 (line)]] | alt | 67.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -11.8) |
| [[SNU-1 (line)]] | wt | 44.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.173× (z -12.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A549 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.82 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9105), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPK]] | +0.93 | +0.94 / +0.92 | both halves | 7e-06 | STRING 652 |
| [[POLQ]] | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | STRING 499 |
| [[SPC25]] | +0.92 | +0.93 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 724 |
| [[FANCI]] | +0.92 | +0.92 / +0.90 | both halves | 7e-06 | STRING 615 |
| [[SPC24]] | +0.91 | +0.90 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[GINS1]] | +0.91 | +0.89 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 606 |
| [[WDHD1]] | +0.90 | +0.86 / +0.91 | both halves | 7e-06 | STRING 569 |
| [[DTL]] | +0.90 | +0.90 / +0.89 | both halves | 7e-06 | STRING 842 |
| [[NCAPG2]] | +0.90 | +0.89 / +0.90 | both halves | 7e-06 | STRING 728 |
| [[BLM]] | +0.90 | +0.91 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[FANCA]] | +0.89 | +0.89 / +0.89 | both halves | 7e-06 |  |
| [[EXO1]] | +0.89 | +0.88 / +0.87 | both halves | 7e-06 | STRING 900 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 5, C 10. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises MELK's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.86× lower at baseline in the lines without CDC25A | 0.012 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises MELK's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.66× lower at baseline in the lines without E2F8 | 0.033 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers MELK's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GGH]] | B | GGH activity raises MELK's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.61× lower at baseline in the lines without GGH | 0.077 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises MELK's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.10× lower at baseline in the lines without E2F2 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[TCF19]] | C | TCF19 activity raises MELK's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 3.26× lower at baseline in the lines without TCF19 | 0.011 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent; co-absent with the target |
| [[DSCC1]] | C | DSCC1 activity raises MELK's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 3.05× lower at baseline in the lines without DSCC1 | 0.016 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises MELK's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.55× lower at baseline in the lines without AURKB | 0.024 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[PBK]] | C | PBK activity raises MELK's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.38× lower at baseline in the lines without PBK | 0.024 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[CENPP]] | C | CENPP activity raises MELK's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.62× lower at baseline in the lines without CENPP | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises MELK's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.69× lower at baseline in the lines without MCM10 | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises MELK's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 3.52× lower at baseline in the lines without MYBL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*56 arrows, 56 of them with an alert ⚠; grade A 0, B 0, C 56. Shown: the 12 strongest; 44 more arrows (44 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CENPP]] | C | [[DIAPH3]], MELK activity raises CENPP's level | lines that do not express DIAPH3, MELK (3) vs lines expressing them (47) | 4.14× lower at baseline in the lines without DIAPH3, MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[PBK]] | C | [[DIAPH3]], MELK, [[TK1]] activity raises PBK's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 4.05× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[IQGAP3]] | C | [[DIAPH3]], MELK, [[TK1]] activity raises IQGAP3's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 3.79× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[PCLAF]] | C | MELK, [[TK1]] activity raises PCLAF's level | lines that do not express MELK, TK1 (3) vs lines expressing them (47) | 3.56× lower at baseline in the lines without MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[KIF15]] | C | [[DIAPH3]], MELK activity raises KIF15's level | lines that do not express DIAPH3, MELK (3) vs lines expressing them (47) | 3.41× lower at baseline in the lines without DIAPH3, MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[LMNB1]] | C | MELK activity raises LMNB1's level | lines that do not express MELK (3) vs lines expressing it (47) | 3.30× lower at baseline in the lines without MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[EME1]] | C | [[DIAPH3]], MELK, [[TK1]] activity raises EME1's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 3.22× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[FANCI]] | C | [[DIAPH3]], MELK, [[TK1]] activity raises FANCI's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 3.15× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CIT]] | C | [[DIAPH3]], MELK activity raises CIT's level | lines that do not express DIAPH3, MELK (3) vs lines expressing them (47) | 3.09× lower at baseline in the lines without DIAPH3, MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[GGH]] | C | MELK, [[TK1]] activity raises GGH's level | lines that do not express MELK, TK1 (3) vs lines expressing them (47) | 3.07× lower at baseline in the lines without MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[SPAG5]] | C | MELK activity raises SPAG5's level | lines that do not express MELK (3) vs lines expressing it (47) | 2.90× lower at baseline in the lines without MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[ZWINT]] | C | [[DIAPH3]], MELK, [[TK1]] activity raises ZWINT's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 2.80× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.927). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.9, -46.8); signed map (-39.8, -43.8). **Vector** length 163, 57.4% of its response variance represented; |z| ≥ 3 in 1,209 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.72 to 28); *DNA Replication* (reactome, mean cos +0.71 to 40); *E2F G1/S* (control, mean cos +0.69 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | +5.8 | +6.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +4.9 | +5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +4.5 | +6.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +4.4 | +7.0 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +4.3 | +4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.3 | +4.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.3 | +2.7 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +3.2 | +3.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.9 | +2.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.9 | +2.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -9.8 | -12.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.1 | -8.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -8.5 | -9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.3 | -9.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | -5.7 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.5 | -6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -3.3 |
|  | [[palbociclib (drug)]] 5 µM |  | -4.3 | -6.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -4.1 | -4.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | -3.5 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | maternal embryonic leucine zipper kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.2 — chr9:36,572,862-36,677,683 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0175 |
| Gene groups (HGNC) | MELK family kinases |
| Hallmark sets | E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14680](https://www.uniprot.org/uniprotkb/Q14680) (Maternal embryonic leucine zipper kinase):

> Serine/threonine-protein kinase involved in various processes such as cell cycle regulation, self-renewal of stem cells, apoptosis and splicing regulation. Has a broad substrate specificity; phosphorylates BCL2L14, CDC25B, MAP3K5/ASK1 and ZNF622. Acts as an activator of apoptosis by phosphorylating and activating MAP3K5/ASK1. Acts as a regulator of cell cycle, notably by mediating phosphorylation of CDC25B, promoting localization of CDC25B to the centrosome and the spindle poles during mitosis. …

**Summary**, from NCBI Gene [9833](https://www.ncbi.nlm.nih.gov/gene/9833):

> Enables calcium ion binding activity; non-membrane spanning protein tyrosine kinase activity; and protein serine/threonine kinase activity. Involved in apoptotic process; cell population proliferation; and protein autophosphorylation. Located in cell cortex and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16870](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16870) · Entrez [9833](https://www.ncbi.nlm.nih.gov/gene/9833) · UniProt [Q14680](https://www.uniprot.org/uniprotkb/Q14680) · Ensembl [ENSG00000165304](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165304)

## Data

Gene col 9105: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9105); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9105, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9105]; `tensor/DDL_lfc|DDL_z.npy` [9105]; `embed/gene_vectors.npy` [9105]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9105 or target_col == 9105). Every well: [[MELK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MELK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
